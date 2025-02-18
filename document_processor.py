# # document_processor.py
# import os
# from azure.ai.formrecognizer import DocumentAnalysisClient
# from azure.core.credentials import AzureKeyCredential
# from dotenv import load_dotenv
# import re
# import streamlit as st
# from typing import Optional, Dict
# from datetime import datetime
# import logging
# from pathlib import Path
# import time
# from threading import Lock

# class ProcessingTracker:
#     def __init__(self):
#         self.processing_status: Dict[str, Dict] = {}
#         self.lock = Lock()
    
#     def start_processing(self, user_id: str, file_path: str):
#         with self.lock:
#             if user_id not in self.processing_status:
#                 self.processing_status[user_id] = {}
            
#             self.processing_status[user_id][file_path] = {
#                 'start_time': datetime.now(),
#                 'status': 'processing',
#                 'error': None
#             }
    
#     def complete_processing(self, user_id: str, file_path: str):
#         with self.lock:
#             if user_id in self.processing_status and file_path in self.processing_status[user_id]:
#                 self.processing_status[user_id][file_path].update({
#                     'status': 'completed',
#                     'end_time': datetime.now()
#                 })
    
#     def fail_processing(self, user_id: str, file_path: str, error: str):
#         with self.lock:
#             if user_id in self.processing_status and file_path in self.processing_status[user_id]:
#                 self.processing_status[user_id][file_path].update({
#                     'status': 'failed',
#                     'error': error,
#                     'end_time': datetime.now()
#                 })

# def preprocess_text(text: str) -> str:
#     """Simple text preprocessing with error handling"""
#     try:
#         if not text:
#             return ""
        
#         # Remove extra whitespace
#         text = re.sub(r'\s+', ' ', text)
#         return text.strip()
#     except Exception as e:
#         logging.error(f"Error in text preprocessing: {str(e)}")
#         return text or ""

# class DocumentProcessor:
#     def __init__(self, user_id: Optional[str] = None):
#         # Load environment variables
#         load_dotenv()
        
#         # Initialize user tracking
#         self.user_id = user_id or st.session_state.get('user_id', 'default')
        
#         # Azure AI Document Intelligence credentials
#         self.document_key = os.environ.get('key_document')
#         self.document_endpoint = os.environ.get('end_point_document')
        
#         if not all([self.document_key, self.document_endpoint]):
#             raise ValueError("Azure Document Intelligence credentials not properly configured")
        
#         # Initialize Document Analysis Client
#         self.document_client = DocumentAnalysisClient(
#             endpoint=self.document_endpoint, 
#             credential=AzureKeyCredential(self.document_key)
#         )
        
#         # Initialize processing tracker
#         self.tracker = ProcessingTracker()
        
#         # Initialize rate limiting
#         self.rate_limit_key = f"doc_processor_rate_{self.user_id}"
#         if self.rate_limit_key not in st.session_state:
#             st.session_state[self.rate_limit_key] = {
#                 'last_call': time.time(),
#                 'calls_this_minute': 0
#             }

#     def _check_rate_limit(self) -> bool:
#         """Check if we're within rate limits"""
#         current_time = time.time()
#         last_call = st.session_state[self.rate_limit_key]['last_call']
#         call_count = st.session_state[self.rate_limit_key]['calls_this_minute']
        
#         # Reset count if more than a minute has passed
#         if current_time - last_call > 60:
#             st.session_state[self.rate_limit_key].update({
#                 'calls_this_minute': 0,
#                 'last_call': current_time
#             })
#             return True
        
#         # Check if within limits (60 calls per minute)
#         if call_count >= 60:
#             return False
        
#         # Update tracking
#         st.session_state[self.rate_limit_key]['calls_this_minute'] += 1
#         return True

#     def process_document(self, file_path: str) -> Optional[str]:
#         """Process a document using Azure Document Intelligence with user isolation"""
#         try:
#             # Validate file path
#             file_path = Path(file_path)
#             if not file_path.exists():
#                 raise FileNotFoundError(f"File not found: {file_path}")
            
#             # Check file size (50MB limit)
#             file_size = file_path.stat().st_size
#             if file_size > 50 * 1024 * 1024:
#                 raise ValueError("File size exceeds 50MB limit")
            
#             # Check rate limit
#             if not self._check_rate_limit():
#                 wait_time = 60 - (time.time() - st.session_state[self.rate_limit_key]['last_call'])
#                 st.warning(f"Rate limit reached. Please wait {wait_time:.1f} seconds.")
#                 time.sleep(min(wait_time, 5))  # Wait max 5 seconds
#                 return self.process_document(str(file_path))
            
#             # Start tracking
#             self.tracker.start_processing(self.user_id, str(file_path))
            
#             # Process document
#             with open(file_path, "rb") as f:
#                 poller = self.document_client.begin_analyze_document(
#                     "prebuilt-document", 
#                     document=f, 
#                     locale="en-US"
#                 )
            
#             result = poller.result()
#             data_dict = result.to_dict()
#             content = data_dict.get('content', '')
            
#             # Preprocess content
#             preprocessed_content = preprocess_text(content)
            
#             # Mark as complete
#             self.tracker.complete_processing(self.user_id, str(file_path))
            
#             return preprocessed_content
            
#         except Exception as e:
#             error_msg = f"Error processing {file_path}: {str(e)}"
#             logging.error(error_msg)
#             st.error(error_msg)
            
#             # Track failure
#             self.tracker.fail_processing(self.user_id, str(file_path), str(e))
#             return None

#     def get_processing_status(self, file_path: str) -> Dict:
#         """Get processing status for a specific file"""
#         return self.tracker.processing_status.get(self.user_id, {}).get(str(file_path), {})

#     def cleanup_user_data(self):
#         """Cleanup user-specific data"""
#         try:
#             # Clean up rate limiting data
#             if self.rate_limit_key in st.session_state:
#                 del st.session_state[self.rate_limit_key]
            
#             # Clean up processing status
#             if self.user_id in self.tracker.processing_status:
#                 del self.tracker.processing_status[self.user_id]
                
#         except Exception as e:
#             logging.error(f"Error cleaning up user data: {str(e)}")


#document_processor.py
import fitz  # PyMuPDF
import re
import logging
from typing import Optional, Dict
from threading import Lock
from datetime import datetime

class ProcessingStats:
    def __init__(self):
        self.stats: Dict[str, Dict] = {}
        self.lock = Lock()
    
    def update_stats(self, user_id: str, **kwargs):
        with self.lock:
            if user_id not in self.stats:
                self.stats[user_id] = {
                    'pages_processed': 0,
                    'total_chars': 0,
                    'start_time': None,
                    'end_time': None,
                    'errors': 0
                }
            self.stats[user_id].update(kwargs)
    
    def get_stats(self, user_id: str) -> Dict:
        with self.lock:
            return self.stats.get(user_id, {})

class DocumentProcessor:
    def __init__(self, user_id: Optional[str] = None):
        self.user_id = user_id
        self.stats = ProcessingStats()
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize extracted text"""
        try:
            # Remove unnecessary whitespace
            text = re.sub(r'\s+', ' ', text)
            text = text.strip()
            
            # Handle line breaks properly
            text = re.sub(r'(?<=[.!?])\s+', '\n', text)
            
            # Remove duplicate newlines
            text = re.sub(r'\n\s*\n', '\n', text)
            
            # Clean up any remaining whitespace issues
            lines = [line.strip() for line in text.split('\n')]
            text = '\n'.join(line for line in lines if line)
            
            return text
            
        except Exception as e:
            logging.error(f"Error cleaning text: {str(e)}")
            return text
    
    def extract_text_from_page(self, page) -> str:
        """Extract text from a single PDF page with enhanced handling"""
        try:
            # Get text blocks with their coordinates
            blocks = page.get_text("blocks")
            
            # Sort blocks by vertical position (top to bottom)
            sorted_blocks = sorted(blocks, key=lambda b: (b[1], b[0]))
            
            # Extract and clean text from each block
            text_parts = []
            for block in sorted_blocks:
                text = block[4]
                if text.strip():
                    text_parts.append(text.strip())
            
            return '\n'.join(text_parts)
            
        except Exception as e:
            logging.error(f"Error extracting text from page: {str(e)}")
            return ""
    
    def process_document(self, file_path: str) -> Optional[str]:
        """Process PDF document and extract text with enhanced error handling"""
        try:
            # Update start time
            self.stats.update_stats(
                self.user_id,
                start_time=datetime.now()
            )
            
            # Open and process PDF
            with fitz.open(file_path) as doc:
                text_parts = []
                total_chars = 0
                
                # Process each page
                for page_num in range(len(doc)):
                    try:
                        page = doc[page_num]
                        page_text = self.extract_text_from_page(page)
                        
                        if page_text:
                            text_parts.append(page_text)
                            total_chars += len(page_text)
                            
                            # Update processing stats
                            self.stats.update_stats(
                                self.user_id,
                                pages_processed=page_num + 1,
                                total_chars=total_chars
                            )
                            
                    except Exception as e:
                        logging.error(f"Error processing page {page_num}: {str(e)}")
                        self.stats.update_stats(
                            self.user_id,
                            errors=self.stats.get_stats(self.user_id).get('errors', 0) + 1
                        )
                        continue
                
                # Combine and clean all extracted text
                combined_text = '\n'.join(text_parts)
                cleaned_text = self.clean_text(combined_text)
                
                # Update completion time
                self.stats.update_stats(
                    self.user_id,
                    end_time=datetime.now()
                )
                
                return cleaned_text
                
        except Exception as e:
            error_msg = f"Error processing document: {str(e)}"
            logging.error(error_msg)
            self.stats.update_stats(
                self.user_id,
                errors=self.stats.get_stats(self.user_id).get('errors', 0) + 1,
                end_time=datetime.now()
            )
            return None
    
    def get_processing_stats(self) -> Dict:
        """Get processing statistics for current user"""
        return self.stats.get_stats(self.user_id)
    
    def cleanup_stats(self):
        """Clean up statistics for current user"""
        with self.stats.lock:
            if self.user_id in self.stats.stats:
                del self.stats.stats[self.user_id]