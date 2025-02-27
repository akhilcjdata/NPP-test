
# document_processor.py
import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.core.pipeline.policies import RetryPolicy
from dotenv import load_dotenv
import re
import streamlit as st
from typing import Optional, Dict, List, Any, Tuple
from datetime import datetime, timedelta
import logging
from pathlib import Path
import time
from threading import Lock
import hashlib
import gc

class ProcessingCache:
    """Cache for document processing results"""
    def __init__(self, max_size: int = 50, ttl_minutes: int = 60):
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.max_size = max_size
        self.ttl = timedelta(minutes=ttl_minutes)
        self.lock = Lock()
    
    def get(self, key: str) -> Optional[str]:
        """Get cached result if valid"""
        with self.lock:
            if key in self.cache:
                entry = self.cache[key]
                if datetime.now() - entry['timestamp'] < self.ttl:
                    return entry['content']
                else:
                    # Clean expired entry
                    del self.cache[key]
        return None
    
    def set(self, key: str, content: str):
        """Cache processing result with timestamp"""
        with self.lock:
            # Enforce cache size limit
            if len(self.cache) >= self.max_size:
                # Remove oldest entry
                oldest_key = min(self.cache, key=lambda k: self.cache[k]['timestamp'])
                del self.cache[oldest_key]
            
            self.cache[key] = {
                'content': content,
                'timestamp': datetime.now()
            }
    
    def clear_user_cache(self, user_id: str):
        """Clear all cache entries for a user"""
        with self.lock:
            user_keys = [k for k in self.cache.keys() if k.startswith(f"{user_id}_")]
            for key in user_keys:
                del self.cache[key]
    
    def get_stats(self) -> Dict[str, int]:
        """Get cache statistics"""
        with self.lock:
            return {
                'size': len(self.cache),
                'max_size': self.max_size
            }


class ClientPool:
    """Pool of Azure Document Analysis Clients"""
    def __init__(self, pool_size: int = 5):
        load_dotenv()
        self.document_key = os.environ.get('KEY_DOCUMENT')
        self.document_endpoint = os.environ.get('END_POINT_DOCUMENT')
        
        if not all([self.document_key, self.document_endpoint]):
            raise ValueError("Azure Document Intelligence credentials not properly configured")
        
        self.pool_size = pool_size
        self.clients: List[DocumentAnalysisClient] = []
        self.in_use: List[bool] = [False] * pool_size
        self.lock = Lock()
        self._initialize_pool()
    
    def _initialize_pool(self):
        """Initialize the client pool"""
        for _ in range(self.pool_size):
            client = DocumentAnalysisClient(
                endpoint=self.document_endpoint, 
                credential=AzureKeyCredential(self.document_key),
                # Add retry policy for resilience
                retry_policy=RetryPolicy(
                    retry_total=3,
                    retry_on_status_codes=[500, 502, 503, 504]
                )
            )
            self.clients.append(client)
    
    def get_client(self) -> Tuple[int, DocumentAnalysisClient]:
        """Get an available client from the pool"""
        with self.lock:
            for i, in_use in enumerate(self.in_use):
                if not in_use:
                    self.in_use[i] = True
                    return i, self.clients[i]
            
            # If all clients are in use, wait and retry
            time.sleep(0.5)
            return self.get_client()
    
    def release_client(self, index: int):
        """Release client back to the pool"""
        with self.lock:
            self.in_use[index] = False


class ProcessingTracker:
    def __init__(self):
        self.processing_status: Dict[str, Dict] = {}
        self.lock = Lock()
    
    def start_processing(self, user_id: str, file_path: str):
        with self.lock:
            if user_id not in self.processing_status:
                self.processing_status[user_id] = {}
            
            self.processing_status[user_id][file_path] = {
                'start_time': datetime.now(),
                'status': 'processing',
                'error': None
            }
    
    def complete_processing(self, user_id: str, file_path: str):
        with self.lock:
            if user_id in self.processing_status and file_path in self.processing_status[user_id]:
                self.processing_status[user_id][file_path].update({
                    'status': 'completed',
                    'end_time': datetime.now()
                })
    
    def fail_processing(self, user_id: str, file_path: str, error: str):
        with self.lock:
            if user_id in self.processing_status and file_path in self.processing_status[user_id]:
                self.processing_status[user_id][file_path].update({
                    'status': 'failed',
                    'error': error,
                    'end_time': datetime.now()
                })
    
    def clear_user_status(self, user_id: str):
        """Clear processing status for a user"""
        with self.lock:
            if user_id in self.processing_status:
                del self.processing_status[user_id]


def preprocess_text(text: str) -> str:
    """Optimized text preprocessing with error handling"""
    try:
        if not text:
            return ""
        
        # Process in chunks for large texts
        if len(text) > 100000:
            chunks = [text[i:i+100000] for i in range(0, len(text), 100000)]
            result = []
            for chunk in chunks:
                # Remove extra whitespace
                processed = re.sub(r'\s+', ' ', chunk)
                result.append(processed.strip())
            return ' '.join(result)
        else:
            # Remove extra whitespace
            return re.sub(r'\s+', ' ', text).strip()
            
    except Exception as e:
        logging.error(f"Error in text preprocessing: {str(e)}")
        return text or ""


def calculate_file_hash(file_path: str) -> str:
    """Calculate file hash for caching"""
    try:
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            # Read in chunks to handle large files
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        logging.error(f"Error calculating file hash: {str(e)}")
        # Return timestamp-based hash as fallback
        return f"ts_{int(time.time())}"


class DocumentProcessor:
    # Shared resources
    _client_pool = None
    _processing_cache = None
    _tracker = None
    _init_lock = Lock()
    
    def __init__(self, user_id: Optional[str] = None):
        # Initialize user tracking
        self.user_id = user_id or st.session_state.get('user_id', 'default')
        
        # Initialize shared resources only once
        with self._init_lock:
            if DocumentProcessor._client_pool is None:
                DocumentProcessor._client_pool = ClientPool(pool_size=5)
            if DocumentProcessor._processing_cache is None:
                DocumentProcessor._processing_cache = ProcessingCache(max_size=100)
            if DocumentProcessor._tracker is None:
                DocumentProcessor._tracker = ProcessingTracker()
        
        # Initialize rate limiting with safer access
        self.rate_limit_key = f"doc_processor_rate_{self.user_id}"
        self._ensure_rate_limit_state()

    def _ensure_rate_limit_state(self):
        """Safely initialize rate limit state"""
        if self.rate_limit_key not in st.session_state:
            st.session_state[self.rate_limit_key] = {
                'last_call': time.time(),
                'calls_this_minute': 0
            }

    def _check_rate_limit(self) -> bool:
        """Check if we're within rate limits, with backoff"""
        # Ensure rate limit state exists
        self._ensure_rate_limit_state()
        
        current_time = time.time()
        rate_state = st.session_state[self.rate_limit_key]
        last_call = rate_state['last_call']
        call_count = rate_state['calls_this_minute']
        
        # Reset count if more than a minute has passed
        if current_time - last_call > 60:
            st.session_state[self.rate_limit_key].update({
                'calls_this_minute': 0,
                'last_call': current_time
            })
            return True
        
        # Check if within limits (60 calls per minute)
        if call_count >= 60:
            # Calculate backoff time (exponential backoff with max wait of 15s)
            wait_time = min(2 ** (call_count - 60) * 0.1, 15)
            time.sleep(wait_time)
            return False
        
        # Update tracking
        st.session_state[self.rate_limit_key]['calls_this_minute'] += 1
        st.session_state[self.rate_limit_key]['last_call'] = current_time
        return True

    def process_document(self, file_path: str) -> Optional[str]:
        """Process a document using Azure Document Intelligence with optimized caching"""
        try:
            # Validate file path
            file_path = Path(file_path)
            if not file_path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
            
            # Check file size (50MB limit)
            file_size = file_path.stat().st_size
            if file_size > 50 * 1024 * 1024:
                raise ValueError("File size exceeds 50MB limit")
            
            # Check cache first - use hash for more reliable caching
            file_hash = calculate_file_hash(str(file_path))
            cache_key = f"{self.user_id}_{file_hash}"
            cached_content = self._processing_cache.get(cache_key)
            
            if cached_content:
                logging.info(f"Cache hit for file {file_path.name}")
                return cached_content
            
            # Check rate limit with adaptive backoff
            while not self._check_rate_limit():
                if st.empty().warning("Rate limit reached. Applying backoff strategy..."):
                    time.sleep(1)  # Show warning briefly
            
            # Start tracking
            self._tracker.start_processing(self.user_id, str(file_path))
            
            # Process document using client pool
            client_index, client = self._client_pool.get_client()
            try:
                # Process in memory-efficient way
                with open(file_path, "rb") as f:
                    poller = client.begin_analyze_document(
                        "prebuilt-document", 
                        document=f, 
                        locale="en-US"
                    )
                
                result = poller.result()
                
                # Extract content and handle memory
                content = result.content
                del result  # Help garbage collection
                gc.collect()  # Force garbage collection
                
                # Preprocess content in chunks
                preprocessed_content = preprocess_text(content)
                
                # Cache the result
                self._processing_cache.set(cache_key, preprocessed_content)
                
                # Mark as complete
                self._tracker.complete_processing(self.user_id, str(file_path))
                
                return preprocessed_content
                
            except Exception as e:
                error_msg = f"Error processing {file_path}: {str(e)}"
                logging.error(error_msg)
                self._tracker.fail_processing(self.user_id, str(file_path), str(e))
                raise
            
            finally:
                # Always release the client back to pool
                self._client_pool.release_client(client_index)
                
        except Exception as e:
            error_msg = f"Error processing {file_path}: {str(e)}"
            logging.error(error_msg)
            st.error(f"Error: {str(e)}")
            return None

    def get_processing_status(self, file_path: str) -> Dict:
        """Get processing status for a specific file"""
        return self._tracker.processing_status.get(self.user_id, {}).get(str(file_path), {})

    def cleanup_user_data(self):
        """Cleanup user-specific data"""
        try:
            # Clean up rate limiting data
            if self.rate_limit_key in st.session_state:
                del st.session_state[self.rate_limit_key]
            
            # Clean up processing status
            self._tracker.clear_user_status(self.user_id)
            
            # Clean up cache for this user
            self._processing_cache.clear_user_cache(self.user_id)
                
        except Exception as e:
            logging.error(f"Error cleaning up user data: {str(e)}")