#  # azure_openai_operations.py

# import os
# from dotenv import load_dotenv
# from openai import AzureOpenAI
# from langchain.prompts import PromptTemplate
# import streamlit as st
# from typing import Dict, Optional
# from datetime import datetime, timedelta
# import time
# from threading import Lock
# import logging

# class RateLimiter:
#     def __init__(self, calls_per_minute: int = 60):
#         self.calls_per_minute = calls_per_minute
#         self.calls: Dict[str, list] = {}
#         self.lock = Lock()

#     def can_make_request(self, user_id: str) -> bool:
#         with self.lock:
#             now = datetime.now()
#             minute_ago = now - timedelta(minutes=1)
            
#             # Initialize or clean old calls for user
#             if user_id not in self.calls:
#                 self.calls[user_id] = []
#             self.calls[user_id] = [
#                 timestamp for timestamp in self.calls[user_id] 
#                 if timestamp > minute_ago
#             ]
            
#             # Check if under rate limit
#             if len(self.calls[user_id]) < self.calls_per_minute:
#                 self.calls[user_id].append(now)
#                 return True
#             return False

#     def get_wait_time(self, user_id: str) -> float:
#         with self.lock:
#             if user_id not in self.calls or not self.calls[user_id]:
#                 return 0
            
#             oldest_call = min(self.calls[user_id])
#             wait_time = 60 - (datetime.now() - oldest_call).total_seconds()
#             return max(0, wait_time)

# class AzureOpenAIExtractor:
#     def __init__(self, user_id: Optional[str] = None):
#         """Initialize the Azure OpenAI client with user tracking"""
#         # Load environment variables
#         load_dotenv()
        
#         self.user_id = user_id or st.session_state.get('user_id', 'default')
#         self.client = self.create_azure_openai_instance()
#         self.rate_limiter = RateLimiter()
#         self._processing_status = None
#         self._status_placeholder = None
        
#         # Initialize API usage tracking
#         if 'api_usage' not in st.session_state:
#             st.session_state.api_usage = {}
#         if self.user_id not in st.session_state.api_usage:
#             st.session_state.api_usage[self.user_id] = {
#                 'total_tokens': 0,
#                 'total_calls': 0,
#                 'errors': 0,
#                 'last_call': None
#             }

#     def create_azure_openai_instance(self):
#         """Create and return an instance of AzureOpenAI"""
#         try:
#             return AzureOpenAI(
#                 api_key=os.environ.get('AZURE_OPENAI_API_KEY'),
#                 api_version=os.environ.get('AZURE_OPENAI_VERSION'),
#                 azure_endpoint=os.environ.get('AZURE_OPENAI_ENDPOINT')
#             )
#         except Exception as e:
#             error_msg = f"Error initializing Azure OpenAI: {str(e)}"
#             logging.error(error_msg)
#             raise

#     def extract_information(self, text: str, prompt_template: str, max_tokens: int = 250) -> str:
#         """Extract information using Azure OpenAI with rate limiting and retry"""
#         try:
#             # Initialize status placeholder if not exists
#             if self._status_placeholder is None:
#                 self._status_placeholder = st.empty()

#             # Check rate limiting
#             if not self.rate_limiter.can_make_request(self.user_id):
#                 wait_time = self.rate_limiter.get_wait_time(self.user_id)
#                 if wait_time > 0:
#                     self._status_placeholder.info(f"Processing... Please wait {wait_time:.1f} seconds.")
#                     time.sleep(min(wait_time, 5))
#                     return self.extract_information(text, prompt_template, max_tokens)
#                 return ""

#             # Clear status placeholder
#             self._status_placeholder.empty()

#             # Create prompt
#             prompt = PromptTemplate(
#                 input_variables=["document_content"],
#                 template=prompt_template
#             )
#             formatted_prompt = prompt.format(document_content=text)

#             max_retries = 3
#             current_try = 0
            
#             while current_try < max_retries:
#                 try:
#                     # Make API call
#                     response = self.client.completions.create(
#                         model=os.environ.get('AZURE_OPENAI_DEPLOYMENT'),
#                         prompt=formatted_prompt,
#                         temperature=0,
#                         max_tokens=max_tokens,
#                         top_p=0.1,
#                         frequency_penalty=0,
#                         presence_penalty=0,
#                         best_of=1,
#                         stop=None
#                     )

#                     # Update usage statistics
#                     st.session_state.api_usage[self.user_id].update({
#                         'total_calls': st.session_state.api_usage[self.user_id]['total_calls'] + 1,
#                         'total_tokens': st.session_state.api_usage[self.user_id]['total_tokens'] + response.usage.total_tokens,
#                         'last_call': datetime.now()
#                     })

#                     return response.choices[0].text.strip()
                    
#                 except Exception as e:
#                     current_try += 1
#                     if current_try == max_retries:
#                         logging.error(f"Error in extraction after {max_retries} attempts: {str(e)}")
#                         return ""
#                     time.sleep(1)  # Wait before retrying

#         except Exception as e:
#             logging.error(f"Error in extraction for user {self.user_id}: {str(e)}")
#             return ""

#     def get_usage_stats(self) -> Dict:
#         """Get usage statistics for the current user"""
#         return st.session_state.api_usage.get(self.user_id, {
#             'total_tokens': 0,
#             'total_calls': 0,
#             'errors': 0,
#             'last_call': None
#         })

#     def cleanup_user_data(self):
#         """Cleanup user-specific data"""
#         try:
#             # Clean up API usage data
#             if self.user_id in st.session_state.api_usage:
#                 del st.session_state.api_usage[self.user_id]
            
#             # Clean up rate limiter data
#             if self.user_id in self.rate_limiter.calls:
#                 del self.rate_limiter.calls[self.user_id]
                
#             # Clean up status placeholder
#             if self._status_placeholder:
#                 self._status_placeholder.empty()
#                 self._status_placeholder = None
                
#         except Exception as e:
#             logging.error(f"Error cleaning up user data: {str(e)}")



# azure_openai_operations.py

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
        
        # Initialize API usage tracking with safer initialization
        self._ensure_api_usage_initialized()

    def _ensure_api_usage_initialized(self):
        """Safely initialize API usage tracking"""
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

    def extract_information(self, text: str, prompt_template: str, max_tokens: int = 250) -> str:
        """Extract information using Azure OpenAI with rate limiting and retry"""
        try:
            # Make sure API usage is initialized
            self._ensure_api_usage_initialized()
            
            # Initialize status placeholder if not exists
            if self._status_placeholder is None:
                self._status_placeholder = st.empty()

            # Check rate limiting
            if not self.rate_limiter.can_make_request(self.user_id):
                wait_time = self.rate_limiter.get_wait_time(self.user_id)
                if wait_time > 0:
                    self._status_placeholder.info(f"Processing... Please wait {wait_time:.1f} seconds.")
                    time.sleep(min(wait_time, 5))
                    return self.extract_information(text, prompt_template, max_tokens)
                return ""

            # Clear status placeholder
            self._status_placeholder.empty()

            # Create prompt
            prompt = PromptTemplate(
                input_variables=["document_content"],
                template=prompt_template
            )
            formatted_prompt = prompt.format(document_content=text)

            max_retries = 3
            current_try = 0
            
            while current_try < max_retries:
                try:
                    # Make API call
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

                    # Update usage statistics
                    st.session_state.api_usage[self.user_id].update({
                        'total_calls': st.session_state.api_usage[self.user_id]['total_calls'] + 1,
                        'total_tokens': st.session_state.api_usage[self.user_id]['total_tokens'] + response.usage.total_tokens,
                        'last_call': datetime.now()
                    })

                    return response.choices[0].text.strip()
                    
                except Exception as e:
                    current_try += 1
                    if current_try == max_retries:
                        logging.error(f"Error in extraction after {max_retries} attempts: {str(e)}")
                        return ""
                    time.sleep(1)  # Wait before retrying

        except Exception as e:
            logging.error(f"Error in extraction for user {self.user_id}: {str(e)}")
            return ""

    def get_usage_stats(self) -> Dict:
        """Get usage statistics for the current user"""
        self._ensure_api_usage_initialized()
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
            if 'api_usage' in st.session_state and self.user_id in st.session_state.api_usage:
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