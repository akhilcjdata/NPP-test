# pdf_processor.py

import os
import streamlit as st
from datetime import datetime
from document_processor import DocumentProcessor
from doc_extractor import DocumentSectionExtractor
from azure_openai_operations import AzureOpenAIExtractor
from section_config import SECTIONS
from prompt_list import (DOCUMENT_INFO_PROMPTS, EMPLOYER_INFO_PROMPTS, PLAN_ADMIN_PROMPTS,
                        CONTRIBUTION_TYPES_PROMPTS, SERVICE_TYPES_PROMPTS,
                        ELIGIBILITY_TYPES_PROMPTS, VESTING_TYPES_PROMPTS,
                        COMPENSATION_TYPES_PROMPTS,
                        CONTRIBUTION_ALLOCATION_TYPES_PROMPTS,
                        SAFE_HARBOR_PROMPTS,
                        MATCHING_CONTRIBUTION_PROMPTS, NON_ELECTIVE_PROMPTS,
                        PREVAILING_WAGE_PROMPTS, GENERAL_PLAN_PROMPTS,
                        RETIREMENT_AND_DISBALITIY_PROMPTS,
                        PERMITTED_ELECTION_PROMPTS, DISTRIBUTION_PROMPTS,
                        PARTICIPATING_EMPLOYER_PROMPTS, SUBSEQUENT_CYCLE4_EMPLOYER_PROMPTS,
                        OTHER_PROVISIONS_PROMPTS, DOCUMENT_REQUESTS_PROMPTS,
                        SUPPORTING_FORMS_INFORMATION_PROMPTS, ADMINISTRATIVE_FORMS_PROMPTS,
                        GENERAL_PROMPTS)
import uuid
import logging
import shutil
from threading import Lock
import time
from typing import Dict, Optional, Union, List, Tuple, Any
import concurrent.futures
import hashlib
import gc
from direct_extractor import DirectInfoExtractor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pdf_processor.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("pdf_processor")

class ProcessingQueue:
    _instance = None
    _init_lock = Lock()
    
    def __new__(cls):
        with cls._init_lock:
            if cls._instance is None:
                cls._instance = super(ProcessingQueue, cls).__new__(cls)
                cls._instance.queue = {}
                cls._instance.lock = Lock()
                cls._instance.max_concurrent = 3  # Max concurrent processing jobs
                cls._instance.max_user_retries = 2  # Max retries per user job
        return cls._instance
    
    def add_job(self, user_id: str, job_type: str) -> bool:
        with self.lock:
            # Check total concurrent jobs
            active_jobs = sum(1 for job in self.queue.values() 
                             if job['status'] == 'processing')
            
            if active_jobs >= self.max_concurrent:
                logger.info(f"Max concurrent jobs reached ({self.max_concurrent}). Refusing job for {user_id}")
                return False
            
            # Check if user already has a job
            if user_id in self.queue and self.queue[user_id]['status'] == 'processing':
                logger.info(f"User {user_id} already has an active job")
                return False
            
            # Add job with retry count
            self.queue[user_id] = {
                'current_job': job_type,
                'start_time': datetime.now(),
                'status': 'processing',
                'retry_count': 0,
                'last_error': None
            }
            logger.info(f"Added job for user {user_id}, type: {job_type}")
            return True
    
    def complete_job(self, user_id: str):
        with self.lock:
            if user_id in self.queue:
                del self.queue[user_id]
                logger.info(f"Completed job for user {user_id}")

    def fail_job(self, user_id: str, error: str) -> bool:
        """Mark job as failed, return True if retry is possible"""
        with self.lock:
            if user_id in self.queue:
                self.queue[user_id]['last_error'] = error
                
                # Check if can retry
                if self.queue[user_id]['retry_count'] < self.max_user_retries:
                    self.queue[user_id]['retry_count'] += 1
                    self.queue[user_id]['status'] = 'waiting_retry'
                    logger.info(f"Job for user {user_id} failed, will retry. Attempt {self.queue[user_id]['retry_count']}")
                    return True
                else:
                    # Max retries reached, mark as failed
                    self.queue[user_id]['status'] = 'failed'
                    logger.error(f"Job for user {user_id} failed after {self.max_user_retries} retries")
                    return False
        return False

    def is_processing(self, user_id: str) -> bool:
        with self.lock:
            return user_id in self.queue and self.queue[user_id]['status'] == 'processing'

    def get_queue_status(self) -> Dict:
        """Get queue status summary"""
        with self.lock:
            return {
                'total_jobs': len(self.queue),
                'active_jobs': sum(1 for job in self.queue.values() 
                                 if job['status'] == 'processing'),
                'waiting_jobs': sum(1 for job in self.queue.values() 
                                  if job['status'] == 'waiting_retry'),
                'failed_jobs': sum(1 for job in self.queue.values() 
                                 if job['status'] == 'failed')
            }

class ProcessingCache:
    """Cache for processed results"""
    _instance = None
    _init_lock = Lock()
    
    def __new__(cls):
        with cls._init_lock:
            if cls._instance is None:
                cls._instance = super(ProcessingCache, cls).__new__(cls)
                cls._instance.cache = {}
                cls._instance.lock = Lock()
                cls._instance.max_entries = 50  # Maximum cache entries
        return cls._instance
    
    def get_result(self, user_id: str, ppa_hash: str, cycle3_hash: str) -> Optional[Dict]:
        """Get cached result if available"""
        cache_key = f"{user_id}_{ppa_hash}_{cycle3_hash}"
        with self.lock:
            if cache_key in self.cache:
                logger.info(f"Cache hit for {cache_key}")
                return self.cache[cache_key]['result']
        return None
    
    def store_result(self, user_id: str, ppa_hash: str, cycle3_hash: str, result: Dict):
        """Store result in cache"""
        cache_key = f"{user_id}_{ppa_hash}_{cycle3_hash}"
        with self.lock:
            # Manage cache size
            if len(self.cache) >= self.max_entries:
                # Remove oldest entry
                oldest_key = min(self.cache.keys(), 
                               key=lambda k: self.cache[k]['timestamp'])
                del self.cache[oldest_key]
                logger.info(f"Cache full, removed oldest entry: {oldest_key}")
            
            # Store new result
            self.cache[cache_key] = {
                'result': result,
                'timestamp': datetime.now()
            }
            logger.info(f"Stored result in cache: {cache_key}")
    
    def clear_user_cache(self, user_id: str):
        """Clear all cache entries for a user"""
        with self.lock:
            keys_to_remove = [k for k in self.cache.keys() 
                            if k.startswith(f"{user_id}_")]
            for key in keys_to_remove:
                del self.cache[key]
            logger.info(f"Cleared cache for user {user_id}, removed {len(keys_to_remove)} entries")


def calculate_file_hash(file_content: bytes) -> str:
    """Calculate hash from file content for caching"""
    return hashlib.md5(file_content).hexdigest()


class PDFProcessor:
    _processing_queue = ProcessingQueue()
    _processing_cache = ProcessingCache()
    _instance_count = 0
    _instance_lock = Lock()
    
    def __init__(self, user_id: Optional[str] = None):
        self.user_id = user_id or str(uuid.uuid4())
        self.direct_extractor = DirectInfoExtractor()
        
        # Increment instance counter
        with PDFProcessor._instance_lock:
            PDFProcessor._instance_count += 1
            logger.info(f"Creating PDFProcessor instance #{PDFProcessor._instance_count} for user {self.user_id}")
        
        # Get desktop path - using different methods for different OS
        if os.name == 'nt':  # Windows
            self.desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        else:  # Linux/Mac
            self.desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        
        # Create main folders on desktop
        self.main_folders = {
            'NPPG': os.path.join(self.desktop_path, 'NPPG_Files'),
            'PPA': os.path.join(self.desktop_path, 'NPPG_Files', 'PPA'),
            'Cycle3': os.path.join(self.desktop_path, 'NPPG_Files', 'Cycle3'),
            'Reports': os.path.join(self.desktop_path, 'NPPG_Files', 'Reports')
        }
        
        # Create folders
        self.folders = self._initialize_user_folders()
        
        # Initialize components with dependency injection for better testing
        self.doc_processor = self._create_document_processor()
        self.section_extractor = self._create_section_extractor()
        self.openai_extractor = self._create_openai_extractor()
        
        # Threading configuration
        self.max_workers = 4  # Maximum concurrent workers for this instance

    def _create_document_processor(self) -> DocumentProcessor:
        """Create document processor with dependency injection"""
        return DocumentProcessor(self.user_id)
    
    def _create_section_extractor(self) -> DocumentSectionExtractor:
        """Create section extractor with dependency injection"""
        return DocumentSectionExtractor(self.user_id)
    
    def _create_openai_extractor(self) -> AzureOpenAIExtractor:
        """Create OpenAI extractor with dependency injection"""
        return AzureOpenAIExtractor(self.user_id)

    def _initialize_user_folders(self) -> Dict[str, str]:
        """Create and return user-specific folders with error handling"""
        try:
            # First ensure NPPG_Files directory exists on desktop
            nppg_root = os.path.join(self.desktop_path, 'NPPG_Files')
            os.makedirs(nppg_root, exist_ok=True)
            
            # Create main folders
            for folder in self.main_folders.values():
                os.makedirs(folder, exist_ok=True)
            
            # Create user-specific folders
            user_folders = {
                'ppa': os.path.join(self.main_folders['PPA'], str(self.user_id)),
                'cycle3': os.path.join(self.main_folders['Cycle3'], str(self.user_id)),
                'reports': os.path.join(self.main_folders['Reports'], str(self.user_id)),
                'temp': os.path.join(self.main_folders['NPPG'], f'temp_{str(self.user_id)}')
            }
            
            # Create user folders
            for folder_path in user_folders.values():
                os.makedirs(folder_path, exist_ok=True)
            
            logger.info(f"Initialized folders for user {self.user_id}")
            return user_folders
            
        except Exception as e:
            error_msg = f"Error initializing folders for user {self.user_id} on Desktop: {str(e)}"
            logger.error(error_msg)
            raise Exception(error_msg)

    def _get_relevant_excerpt(self, section_text: str, field: str, context_chars: int = 1000) -> str:
        """Extract relevant portion of text around field information with optimized search"""
        if not section_text:
            return ""
        
        try:
            # Optimize for large texts
            if len(section_text) > 10000:
                # Fast initial search
                field_lower = field.lower().replace('_', ' ')
                text_lower = section_text.lower()
                
                # Quick search for direct occurrence
                direct_pos = text_lower.find(field_lower)
                if direct_pos != -1:
                    start = max(0, direct_pos - context_chars // 2)
                    end = min(len(section_text), direct_pos + context_chars // 2)
                else:
                    # Create search terms from field name
                    search_terms = field.replace('_', ' ').split()
                    
                    # Search in chunks for very large texts
                    chunk_size = 5000
                    best_pos = 0
                    max_score = 0
                    
                    for i in range(0, len(text_lower), chunk_size // 2):  # Overlapping chunks
                        chunk = text_lower[i:i+chunk_size]
                        score = sum(chunk.count(term.lower()) for term in search_terms)
                        if score > max_score:
                            max_score = score
                            best_pos = i + chunk_size // 2  # Middle of best chunk
                    
                    # Extract context around best position
                    start = max(0, best_pos - context_chars // 2)
                    end = min(len(section_text), best_pos + context_chars // 2)
            else:
                # For smaller texts, use the original algorithm
                search_terms = field.replace('_', ' ').split()
                best_pos = 0
                max_score = 0
                text_lower = section_text.lower()
                
                # Find best position based on term density
                for i in range(len(text_lower)):
                    score = sum(1 for term in search_terms 
                              if term.lower() in text_lower[i:i+100])
                    if score > max_score:
                        max_score = score
                        best_pos = i
                
                # Extract context around best position
                start = max(0, best_pos - context_chars // 2)
                end = min(len(section_text), best_pos + context_chars // 2)
            
            # Extend to complete sentences
            while start > 0 and section_text[start] != '.':
                start -= 1
            while end < len(section_text) and section_text[end] != '.':
                end += 1
                if end == len(section_text) - 1:
                    break
                
            return section_text[start:end].strip()
            
        except Exception as e:
            logger.error(f"Error getting excerpt: {str(e)}")
            return section_text[:context_chars] if section_text else ""

    def save_file(self, uploaded_file, folder_key: str) -> Optional[str]:
        """Save uploaded file with enhanced error handling and retries"""
        if uploaded_file:
            max_retries = 3
            retry_delay = 0.5
            
            for attempt in range(max_retries):
                try:
                    # Create timestamp for unique filename
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    unique_filename = f"{timestamp}_{uploaded_file.name}"
                    file_path = os.path.join(self.folders[folder_key], unique_filename)
                    
                    # Write file
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Verify file was written successfully
                    if not os.path.exists(file_path):
                        raise FileNotFoundError(f"Failed to write file: {file_path}")
                    
                    # File size verification
                    expected_size = len(uploaded_file.getvalue())
                    actual_size = os.path.getsize(file_path)
                    
                    if expected_size != actual_size:
                        logger.warning(f"File size mismatch: expected {expected_size}, got {actual_size}. Retrying...")
                        continue
                    
                    logger.info(f"Successfully saved file: {file_path}")
                    return file_path
                    
                except Exception as e:
                    error_msg = f"Error saving file (attempt {attempt+1}/{max_retries}): {str(e)}"
                    logger.error(error_msg)
                    
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay * (attempt + 1))  # Exponential backoff
                    else:
                        logger.error(f"Failed to save file after {max_retries} attempts")
                        return None
        return None

    def _cleanup_temp_files(self):
        """Clean up temporary files with improved error handling"""
        try:
            temp_folder = os.path.join(self.main_folders['NPPG'], f'temp_{self.user_id}')
            if os.path.exists(temp_folder):
                # Delete files individually to handle permission issues
                for root, dirs, files in os.walk(temp_folder, topdown=False):
                    for name in files:
                        try:
                            os.remove(os.path.join(root, name))
                        except Exception as e:
                            logger.warning(f"Could not remove file {name}: {str(e)}")
                    
                    for name in dirs:
                        try:
                            os.rmdir(os.path.join(root, name))
                        except Exception as e:
                            logger.warning(f"Could not remove directory {name}: {str(e)}")
                
                # Recreate empty temp folder
                try:
                    shutil.rmtree(temp_folder)
                except Exception as e:
                    logger.warning(f"Could not remove temp folder: {str(e)}")
                
                os.makedirs(temp_folder, exist_ok=True)
                logger.info(f"Cleaned temp files for user {self.user_id}")
        except Exception as e:
            logger.error(f"Error cleaning temp files for user {self.user_id}: {str(e)}")

    def _process_field_comparison(self, args) -> Tuple[str, Dict[str, str]]:
        """Process field comparison for parallel execution"""
        section_key, field, base_prompt, ppa_section, cycle3_section = args
        
        try:
            # Get relevant excerpts
            ppa_excerpt = self._get_relevant_excerpt(ppa_section, field)
            cycle3_excerpt = self._get_relevant_excerpt(cycle3_section, field)
            
            # Prepare comparison prompt
            prompt = f"""
            Compare and extract information from these two document sections:

            Previous Plan Document:
            {ppa_excerpt}

            Restated Plan Document:
            {cycle3_excerpt}

            {base_prompt}
            
            Return in format:
            PPA: <extracted_info>
            CYCLE3: <extracted_info>
            """
            
            # Extract information using OpenAI
            response = self.openai_extractor.extract_information(
                text=prompt,
                prompt_template="{document_content}",
                max_tokens=250
            )
            
            result = {}
            if response:
                # Parse response
                parts = response.split('PPA:')
                if len(parts) > 1:
                    ppa_cycle3_parts = parts[1].split('CYCLE3:')
                    if len(ppa_cycle3_parts) > 1:
                        ppa_info = ppa_cycle3_parts[0].strip()
                        cycle3_info = ppa_cycle3_parts[1].strip()
                        
                        result = {
                            'ppa': ppa_info,
                            'cycle3': cycle3_info
                        }
            
            return field, result
        except Exception as e:
            logger.error(f"Error processing field {field} in section {section_key}: {str(e)}")
            return field, {}



    def process_files_simultaneously(self, ppa_file, cycle3_file):
        """Process both files simultaneously with multi-threading and caching"""
        if not self._processing_queue.add_job(self.user_id, 'pdf_processing'):
            st.warning("Processing is already in progress or maximum concurrent jobs reached. Please wait.")
            return None
        
        progress_placeholder = st.empty()
        
        try:
            # Calculate file hashes for caching
            ppa_hash = calculate_file_hash(ppa_file.getvalue())
            cycle3_hash = calculate_file_hash(cycle3_file.getvalue())
            
            # Check cache first
            cached_result = self._processing_cache.get_result(self.user_id, ppa_hash, cycle3_hash)
            if cached_result:
                progress_placeholder.success("Using cached results!")
                return cached_result
            
            # Save and process files
            progress_placeholder.info("Saving files...")
            ppa_path = self.save_file(ppa_file, 'ppa')
            cycle3_path = self.save_file(cycle3_file, 'cycle3')
            
            if not all([ppa_path, cycle3_path]):
                raise ValueError("Failed to save one or both uploaded files")
            
            # Extract text from documents
            progress_placeholder.info("Extracting text from documents...")
            ppa_text = self.doc_processor.process_document(ppa_path)
            cycle3_text = self.doc_processor.process_document(cycle3_path)
            
            if not all([ppa_text, cycle3_text]):
                raise ValueError("Failed to extract text from one or both documents")
            
            # Extract sections
            progress_placeholder.info("Extracting document sections...")
            ppa_sections = self.section_extractor.extract_all_sections(ppa_text)
            cycle3_sections = self.section_extractor.extract_all_sections(cycle3_text)
            
            # Release memory
            del ppa_text, cycle3_text
            gc.collect()
            
            # Initialize results dictionary
            results = {'ppa': {}, 'cycle3': {}}
            
            # Define sections to process
            section_prompts = [
                ('document_info', DOCUMENT_INFO_PROMPTS),
                ('employer_info', EMPLOYER_INFO_PROMPTS),
                ('plan_admin', PLAN_ADMIN_PROMPTS),
                ('contribution_types', CONTRIBUTION_TYPES_PROMPTS),
                ('service_types', SERVICE_TYPES_PROMPTS),
                ('eligibility_types', ELIGIBILITY_TYPES_PROMPTS),
                ('vesting_types', VESTING_TYPES_PROMPTS),
                ('compensation_types', COMPENSATION_TYPES_PROMPTS),
                ('contribution_allocation_types', CONTRIBUTION_ALLOCATION_TYPES_PROMPTS),
                ('safe_harbor_types', SAFE_HARBOR_PROMPTS),
                ('matching_contribution_types', MATCHING_CONTRIBUTION_PROMPTS),
                ('nonelective_contribution_types', NON_ELECTIVE_PROMPTS),
                ('prevailing_wage_contribution_types',PREVAILING_WAGE_PROMPTS),
                ('general_plan_provision_contribution_types',GENERAL_PLAN_PROMPTS),
                ('retirement_and_distribution_contribution_types',RETIREMENT_AND_DISBALITIY_PROMPTS),
                ('distribution_contribution_types',DISTRIBUTION_PROMPTS),
                ('permitted_elections_types',PERMITTED_ELECTION_PROMPTS),
                ('participating_employer_types',PARTICIPATING_EMPLOYER_PROMPTS),
                ('subsequent_employer_types',SUBSEQUENT_CYCLE4_EMPLOYER_PROMPTS),
                ('other_provision_employer_types',OTHER_PROVISIONS_PROMPTS),
                ('document_request_employer_types',DOCUMENT_REQUESTS_PROMPTS),
                ('supporting_forms_information_types',SUPPORTING_FORMS_INFORMATION_PROMPTS),
                ('administrative_forms_types',ADMINISTRATIVE_FORMS_PROMPTS),
                ('general_types',GENERAL_PROMPTS)
            ]
            
            # Process sections with progress tracking
            for section_index, (section_key, prompts) in enumerate(section_prompts):
                progress_placeholder.info(f"Processing section {section_index+1}/{len(section_prompts)}: {section_key.replace('_', ' ').title()}")
                
                try:
                    # Get corresponding sections
                    ppa_section = next(
                        (text for key, text in ppa_sections.items() 
                        if SECTIONS[key]["name"] == SECTIONS[section_key]["name"]), 
                        None
                    )
                    cycle3_section = next(
                        (text for key, text in cycle3_sections.items() 
                        if SECTIONS[key]["name"] == SECTIONS[section_key]["name"]), 
                        None
                    )
                    
                    # Special handling for employer_info section - use direct extraction
                    if section_key == 'employer_info' and ppa_section and cycle3_section:
                        # Use direct extraction for employer info
                        ppa_employer_info = self.direct_extractor.extract_employer_info(ppa_section)
                        cycle3_employer_info = self.direct_extractor.extract_employer_info(cycle3_section)
                        
                        # Create formatted results for display
                        results['ppa'][section_key] = {
                            'employer_name': ppa_employer_info['employer_name'],
                            'street': ppa_employer_info['street'],
                            'city': ppa_employer_info['city'],
                            'state': ppa_employer_info['state'],
                            'zip': ppa_employer_info['zip'],
                            'phone': ppa_employer_info['phone'],
                            'ein': ppa_employer_info['ein'],
                            'fiscal_year_end': ppa_employer_info['fiscal_year_end']

                        }
                        
                        results['cycle3'][section_key] = {
                            'employer_name': cycle3_employer_info['employer_name'],
                            'street': cycle3_employer_info['street'],
                            'city': cycle3_employer_info['city'],
                            'state': cycle3_employer_info['state'],
                            'zip': cycle3_employer_info['zip'],
                            'phone': cycle3_employer_info['phone'],
                            'ein': cycle3_employer_info['ein'],
                            'fiscal_year_end': ppa_employer_info['fiscal_year_end']
                        }
                        
                        # Update progress
                        progress_pct = int((section_index + 1) / len(section_prompts) * 100)
                        progress_placeholder.progress(min(progress_pct, 100))
                        
                        # Skip the regular processing for this section
                        continue
                    
                    # Special handling for plan_admin section - use direct extraction for dates
                    if section_key == 'plan_admin' and ppa_section and cycle3_section:
                        # Extract dates directly from both documents
                        ppa_effective_date = self.direct_extractor.extract_effective_date(ppa_section)
                        cycle3_effective_date = self.direct_extractor.extract_effective_date(cycle3_section)
                        # results['ppa'][section_key]['restatement_date'] = ppa_effective_date.get('restatement_date', 'NA')
                        # results['cycle3'][section_key]['restatement_date'] = cycle3_effective_date.get('restatement_date', 'NA')
                        
                        ppa_plan_year_dates = self.direct_extractor.extract_plan_year_dates(ppa_section)
                        cycle3_plan_year_dates = self.direct_extractor.extract_plan_year_dates(cycle3_section)
                        
                        # Initialize section dictionaries if they don't exist
                        if section_key not in results['ppa']:
                            results['ppa'][section_key] = {}
                        if section_key not in results['cycle3']:
                            results['cycle3'][section_key] = {}
                        
                        # Add the directly extracted date fields
                        results['ppa'][section_key]['effective_date'] = ppa_effective_date.get('effective_date', 'NA')
                        results['cycle3'][section_key]['effective_date'] = cycle3_effective_date.get('effective_date', 'NA')
                        results['ppa'][section_key]['restatement_date'] = ppa_effective_date.get('restatement_date', 'NA')
                        results['cycle3'][section_key]['restatement_date'] = cycle3_effective_date.get('restatement_date', 'NA')
                        
                        results['ppa'][section_key]['plan_year_dates'] = ppa_plan_year_dates.get('plan_year_dates', 'NA')
                        results['cycle3'][section_key]['plan_year_dates'] = cycle3_plan_year_dates.get('plan_year_dates', 'NA')
                        
                        # Continue with regular processing for other fields in this section,
                        # but remove the fields we've already processed from the prompts
                        modified_prompts = {k: v for k, v in prompts.items() 
                                        if k not in ['initial_effective_date', 'plan_year_dates']}
                        
                        # Process other fields in the section using Azure OpenAI
                        # Prepare tasks for parallel processing
                        tasks = []
                        for field, base_prompt in modified_prompts.items():
                            tasks.append((section_key, field, base_prompt, ppa_section, cycle3_section))
                        
                        # Process in parallel
                        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                            future_to_field = {executor.submit(self._process_field_comparison, task): task[1] 
                                            for task in tasks}
                            
                            completed = 0
                            for future in concurrent.futures.as_completed(future_to_field):
                                field = future_to_field[future]
                                try:
                                    processed_field, result = future.result()
                                    if result:
                                        if 'ppa' in result:
                                            results['ppa'][section_key][processed_field] = result['ppa']
                                        if 'cycle3' in result:
                                            results['cycle3'][section_key][processed_field] = result['cycle3']
                                except Exception as e:
                                    logger.error(f"Error processing field {field}: {str(e)}")
                                
                                # Update progress
                                completed += 1
                                progress_pct = int((section_index/len(section_prompts) + 
                                                completed/(len(modified_prompts) * len(section_prompts))) * 100)
                                progress_placeholder.progress(min(progress_pct, 100))
                        
                        # Skip the regular processing for this section since we've handled it
                        continue
                    
                    if ppa_section and cycle3_section:
                        results['ppa'][section_key] = {}
                        results['cycle3'][section_key] = {}
                        
                        # Prepare tasks for parallel processing
                        tasks = []
                        for field, base_prompt in prompts.items():
                            tasks.append((section_key, field, base_prompt, ppa_section, cycle3_section))
                        
                        # Process in parallel
                        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                            future_to_field = {executor.submit(self._process_field_comparison, task): task[1] 
                                            for task in tasks}
                            
                            completed = 0
                            for future in concurrent.futures.as_completed(future_to_field):
                                field = future_to_field[future]
                                try:
                                    processed_field, result = future.result()
                                    if result:
                                        if 'ppa' in result:
                                            results['ppa'][section_key][processed_field] = result['ppa']
                                        if 'cycle3' in result:
                                            results['cycle3'][section_key][processed_field] = result['cycle3']
                                except Exception as e:
                                    logger.error(f"Error processing field {field}: {str(e)}")
                                
                                # Update progress
                                completed += 1
                                progress_pct = int((section_index/len(section_prompts) + 
                                                completed/(len(prompts) * len(section_prompts))) * 100)
                                progress_placeholder.progress(min(progress_pct, 100))
                
                except Exception as e:
                    logger.error(f"Error processing section {section_key}: {str(e)}")
                    continue
            
            # Cache the results
            self._processing_cache.store_result(self.user_id, ppa_hash, cycle3_hash, results)
            progress_placeholder.success("Processing complete!")
            
            return results
            
        except Exception as e:
            error_msg = f"Error processing files for user {self.user_id}: {str(e)}"
            logger.error(error_msg)
            progress_placeholder.error(f"Error: {str(e)}")
            
            if self._processing_queue.fail_job(self.user_id, str(e)):
                progress_placeholder.warning("Will retry processing...")
                time.sleep(2)  # Brief pause before retry
                return self.process_files_simultaneously(ppa_file, cycle3_file)
            
            return None
        
        finally:
            self._cleanup_temp_files()
            self._processing_queue.complete_job(self.user_id)

    def cleanup_user_data(self):
        """Clean up all user-specific data"""
        try:
            # Complete any pending jobs
            self._processing_queue.complete_job(self.user_id)
            
            # Clean up temp folder
            self._cleanup_temp_files()
            
            # Clean up cache
            self._processing_cache.clear_user_cache(self.user_id)
            
            # Clean up component data
            if hasattr(self, 'doc_processor') and self.doc_processor:
                self.doc_processor.cleanup_user_data()
            
            if hasattr(self, 'section_extractor') and self.section_extractor:
                self.section_extractor.cleanup_user_data()
                
            if hasattr(self, 'openai_extractor') and self.openai_extractor:
                self.openai_extractor.cleanup_user_data()
                
            logger.info(f"Cleaned up all data for user {self.user_id}")
            
        except Exception as e:
            logger.error(f"Error cleaning up user data: {str(e)}")
    
    def __del__(self):
        """Destructor to ensure cleanup"""
        try:
            self.cleanup_user_data()
            
            # Decrement instance counter
            with PDFProcessor._instance_lock:
                PDFProcessor._instance_count -= 1
                logger.info(f"Destroyed PDFProcessor instance for user {self.user_id}. Remaining instances: {PDFProcessor._instance_count}")
        except:
            pass  # Silent cleanup in destructor