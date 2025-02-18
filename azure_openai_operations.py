#azure_openai_operations.py

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from langchain.prompts import PromptTemplate
import streamlit as st
from typing import Dict, Optional
from datetime import datetime, timedelta
import time
from threading import Lock
import logging
from key_phrases import PLAN_ADMIN_PHRASES

class RateLimiter:
    def __init__(self, calls_per_minute: int = 60):
        self.calls_per_minute = calls_per_minute
        self.calls: Dict[str, list] = {}
        self.lock = Lock()

    def can_make_request(self, user_id: str) -> bool:
        with self.lock:
            now = datetime.now()
            minute_ago = now - timedelta(minutes=1)
            
            # Initialize or clean old calls for user
            if user_id not in self.calls:
                self.calls[user_id] = []
            self.calls[user_id] = [
                timestamp for timestamp in self.calls[user_id] 
                if timestamp > minute_ago
            ]
            
            # Check if under rate limit
            if len(self.calls[user_id]) < self.calls_per_minute:
                self.calls[user_id].append(now)
                return True
            return False

    def get_wait_time(self, user_id: str) -> float:
        with self.lock:
            if user_id not in self.calls or not self.calls[user_id]:
                return 0
            
            oldest_call = min(self.calls[user_id])
            wait_time = 60 - (datetime.now() - oldest_call).total_seconds()
            return max(0, wait_time)

class AzureOpenAIExtractor:
    def __init__(self, user_id: Optional[str] = None):
        """Initialize the Azure OpenAI client with user tracking"""
        # Load environment variables
        load_dotenv()
        
        self.user_id = user_id or st.session_state.get('user_id', 'default')
        self.client = self.create_azure_openai_instance()
        self.rate_limiter = RateLimiter()
        self._processing_status = None
        self._status_placeholder = None
        
        # Initialize API usage tracking
        if 'api_usage' not in st.session_state:
            st.session_state.api_usage = {}
        if self.user_id not in st.session_state.api_usage:
            st.session_state.api_usage[self.user_id] = {
                'total_tokens': 0,
                'total_calls': 0,
                'errors': 0,
                'last_call': None
            }

    def create_azure_openai_instance(self):
        """Create and return an instance of AzureOpenAI"""
        try:
            return AzureOpenAI(
                api_key=os.environ.get('AZURE_OPENAI_API_KEY'),
                api_version=os.environ.get('AZURE_OPENAI_VERSION'),
                azure_endpoint=os.environ.get('AZURE_OPENAI_ENDPOINT')
            )
        except Exception as e:
            error_msg = f"Error initializing Azure OpenAI: {str(e)}"
            logging.error(error_msg)
            raise

    def enhance_prompt_with_phrases(self, text: str, section_key: str, field: str) -> str:
        """Enhance prompt with key phrase information"""
        try:
            phrases = PLAN_ADMIN_PHRASES.get(section_key, {}).get(field, {})
            if phrases:
                # Add phrase-specific instructions
                phrase_instructions = f"""
                Pay special attention to:
                - Key phrases: {', '.join(phrases.get('phrases', []))}
                - Question identifiers: {', '.join(phrases.get('context', {}).get('question_identifiers', []))}
                - Selected options marked with ☒, ●
                - Unselected options marked with ☐, ○
                """
                text = phrase_instructions + "\n" + text
            return text
        except Exception as e:
            logging.error(f"Error enhancing prompt: {str(e)}")
            return text



    def extract_information(self, text: str, prompt_template: str, max_tokens: int = 250, 
                    section_key: str = None, field: str = None) -> str:
        """Extract information using Azure OpenAI with enhanced prompts"""
        try:
            # Enhanced prompt identifier
            prompt_source = {
                'section': section_key if section_key else 'No section',
                'field': field if field else 'No field',
                'text_length': len(text),
                'template_length': len(prompt_template)
            }
            prompt_identifier = f"Section: {prompt_source['section']}, Field: {prompt_source['field']}"
            
            # Log more details about the prompt
            logging.info(f"""
            Prompt Details:
            - {prompt_identifier}
            - Text Length: {prompt_source['text_length']}
            - Template Length: {prompt_source['template_length']}
            """)

            if self._status_placeholder is None:
                self._status_placeholder = st.empty()

            # Rest of your rate limiting code...

            if section_key and field:
                text = self.enhance_prompt_with_phrases(text, section_key, field)

            prompt = PromptTemplate(
                input_variables=["document_content"],
                template=prompt_template
            )
            formatted_prompt = prompt.format(document_content=text)

            # Log detailed token information
            token_count = len(formatted_prompt.split())
            logging.info(f"""
            Token Information for {prompt_identifier}:
            - Total Tokens: {token_count}
            - Content Tokens: {len(text.split())}
            - Template Tokens: {len(prompt_template.split())}
            """)

            max_retries = 3
            current_try = 0
            
            while current_try < max_retries:
                try:
                    response = self.client.completions.create(
                        model=os.environ.get('AZURE_OPENAI_DEPLOYMENT'),
                        prompt=formatted_prompt,
                        temperature=0,
                        max_tokens=max_tokens,
                        top_p=0.1,
                        frequency_penalty=0,
                        presence_penalty=0,
                        best_of=1,
                        stop=None
                    )

                    # Your usage statistics code...
                    return response.choices[0].text.strip()
                    
                except Exception as e:
                    error_str = str(e)
                    if "maximum context length" in error_str:
                        logging.error(f"""
                        Token limit exceeded:
                        - {prompt_identifier}
                        - Token count: {token_count}
                        - Text length: {prompt_source['text_length']}
                        - Template length: {prompt_source['template_length']}
                        """)
                    
                    current_try += 1
                    if current_try == max_retries:
                        logging.error(f"Error in {prompt_identifier} after {max_retries} attempts: {error_str}")
                        return ""
                    time.sleep(1)

        except Exception as e:
            logging.error(f"""
            Error in extraction:
            - User ID: {self.user_id}
            - {prompt_identifier}
            - Error: {str(e)}
            """)
            return ""

    def get_usage_stats(self) -> Dict:
        """Get usage statistics for the current user"""
        return st.session_state.api_usage.get(self.user_id, {
            'total_tokens': 0,
            'total_calls': 0,
            'errors': 0,
            'last_call': None
        })

    def cleanup_user_data(self):
        """Cleanup user-specific data"""
        try:
            # Clean up API usage data
            if self.user_id in st.session_state.api_usage:
                del st.session_state.api_usage[self.user_id]
            
            # Clean up rate limiter data
            if self.user_id in self.rate_limiter.calls:
                del self.rate_limiter.calls[self.user_id]
                
            # Clean up status placeholder
            if self._status_placeholder:
                self._status_placeholder.empty()
                self._status_placeholder = None
                
        except Exception as e:
            logging.error(f"Error cleaning up user data: {str(e)}")