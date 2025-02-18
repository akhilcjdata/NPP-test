#pdf_processor.py

import os
import streamlit as st
from datetime import datetime
from document_processor import DocumentProcessor
from doc_extractor import DocumentSectionExtractor
from azure_openai_operations import AzureOpenAIExtractor
from section_config import SECTIONS
from prompt_list import (DOCUMENT_INFO_PROMPTS, EMPLOYER_INFO_PROMPTS,PLAN_ADMIN_PROMPTS,
                         CONTRIBUTION_TYPES_PROMPTS,SERVICE_TYPES_PROMPTS,
                         ELIGIBILITY_TYPES_PROMPTS,VESTING_TYPES_PROMPTS,
                         COMPENSATION_TYPES_PROMPTS,
                         CONTRIBUTION_ALLOCATION_TYPES_PROMPTS,
                         SAFE_HARBOR_PROMPTS,
                         MATCHING_CONTRIBUTION_PROMPTS,
                         NON_ELECTIVE_PROMPTS,
                         PREVAILING_WAGE_PROMPTS,GENERAL_PLAN_PROMPTS,
                         RETIREMENT_AND_DISBALITIY_PROMPTS,PERMITTED_ELECTION_PROMPTS,DISTRIBUTION_PROMPTS,PARTICIPATING_EMPLOYER_PROMPTS,
                         SUBSEQUENT_CYCLE4_EMPLOYER_PROMPTS,OTHER_PROVISIONS_PROMPTS,DOCUMENT_REQUESTS_PROMPTS,SUPPORTING_FORMS_INFORMATION_PROMPTS,
                         ADMINISTRATIVE_FORMS_PROMPTS,GENERAL_PROMPTS
                         )
from key_phrases import PLAN_ADMIN_PHRASES
import uuid
import logging
import shutil
from threading import Lock
from typing import Dict, Optional, Union, List

class ProcessingQueue:
    def __init__(self):
        self.queue: Dict[str, Dict] = {}
        self.lock = Lock()
    
    def add_job(self, user_id: str, job_type: str) -> bool:
        with self.lock:
            if user_id in self.queue and self.queue[user_id]['status'] == 'processing':
                return False
            
            self.queue[user_id] = {
                'current_job': job_type,
                'start_time': datetime.now(),
                'status': 'processing'
            }
            return True
    
    def complete_job(self, user_id: str):
        with self.lock:
            if user_id in self.queue:
                del self.queue[user_id]

    def is_processing(self, user_id: str) -> bool:
        with self.lock:
            return user_id in self.queue and self.queue[user_id]['status'] == 'processing'

class PDFProcessor:
    _processing_queue = ProcessingQueue()

    def __init__(self, user_id: Optional[str] = None):
        self.user_id = user_id or str(uuid.uuid4())
        self.desktop_path = 'C:/NPPG_Files'
        
        # Create main folders
        self.main_folders = {
            'NPPG': self.desktop_path,
            'PPA': os.path.join(self.desktop_path, 'PPA'),
            'Cycle3': os.path.join(self.desktop_path, 'Cycle3'),
            'Reports': os.path.join(self.desktop_path, 'Reports')
        }
        
        # Create folders
        self.folders = self._initialize_user_folders()
        
        # Initialize components
        self.doc_processor = DocumentProcessor(self.user_id)
        self.section_extractor = DocumentSectionExtractor(self.user_id)
        self.openai_extractor = AzureOpenAIExtractor(self.user_id)

    def _initialize_user_folders(self) -> Dict[str, str]:
        """Create and return user-specific folders"""
        try:
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
            
            for folder_path in user_folders.values():
                os.makedirs(folder_path, exist_ok=True)
            
            return user_folders
            
        except Exception as e:
            error_msg = f"Error initializing folders for user {self.user_id}: {str(e)}"
            logging.error(error_msg)
            raise Exception(error_msg)

    def process_section_with_phrases(self, section_text: str, field: str, section_key: str) -> dict:
        """Process section text using key phrases"""
        try:
            # Get relevant context and phrases
            phrases = PLAN_ADMIN_PHRASES.get(section_key, {}).get(field, {})
            if not phrases:
                return {'text': section_text}

            # Process with phrases
            context = self.section_extractor.extract_section_with_phrases(
                section_text,
                section_key
            )
            return context

        except Exception as e:
            logging.error(f"Error processing section with phrases: {str(e)}")
            return {'text': section_text}

    def process_files_simultaneously(self, ppa_file, cycle3_file):
        """Process both files simultaneously with enhanced phrase processing"""
        if not self._processing_queue.add_job(self.user_id, 'pdf_processing'):
            st.warning("Processing is already in progress for your session. Please wait.")
            return None
        
        try:
            # Save files
            ppa_path = self.save_file(ppa_file, 'ppa')
            cycle3_path = self.save_file(cycle3_file, 'cycle3')
            
            if not all([ppa_path, cycle3_path]):
                raise ValueError("Failed to save one or both uploaded files")
            
            # Extract text from documents
            ppa_text = self.doc_processor.process_document(ppa_path)
            cycle3_text = self.doc_processor.process_document(cycle3_path)
            
            if not all([ppa_text, cycle3_text]):
                raise ValueError("Failed to extract text from one or both documents")
            
            # Extract sections with phrase processing
            ppa_sections = self.section_extractor.extract_all_sections(ppa_text)
            cycle3_sections = self.section_extractor.extract_all_sections(cycle3_text)
            
            results = {
                'ppa': {},
                'cycle3': {}
            }

            section_prompts = [
                        ('document_info', DOCUMENT_INFO_PROMPTS),
                        ('employer_info', EMPLOYER_INFO_PROMPTS),
                        ('plan_admin', PLAN_ADMIN_PROMPTS),
                        ('contribution_types', CONTRIBUTION_TYPES_PROMPTS),
                        ('service_types', SERVICE_TYPES_PROMPTS),  # This matches your config's "section_types"
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

            # Process each section
            for section_key, prompts in section_prompts:
                try:
                    # Get sections with phrase information
                    ppa_section = ppa_sections.get(section_key, {})
                    cycle3_section = cycle3_sections.get(section_key, {})
                    
                    if ppa_section.get('text') and cycle3_section.get('text'):
                        results['ppa'][section_key] = {}
                        results['cycle3'][section_key] = {}
                        
                        # Process each field
                        for field, base_prompt in prompts.items():
                            # Process with key phrases
                            ppa_context = self.process_section_with_phrases(
                                ppa_section['text'],
                                field,
                                section_key
                            )
                            cycle3_context = self.process_section_with_phrases(
                                cycle3_section['text'],
                                field,
                                section_key
                            )
                            
                            # Use phrase information if available
                            if 'phrases' in ppa_context:
                                results['ppa'][section_key][field] = ppa_context['phrases']
                                results['cycle3'][section_key][field] = cycle3_context['phrases']
                            else:
                                # Fall back to regular extraction
                                prompt = f"""
                                Compare and extract information from these two document sections:

                                Previous Plan Document:
                                {ppa_context['text']}

                                Restated Plan Document:
                                {cycle3_context['text']}

                                {base_prompt}
                                
                                Return in format:
                                PPA: <extracted_info>
                                CYCLE3: <extracted_info>
                                """
                                
                                response = self.openai_extractor.extract_information(
                                    text=prompt,
                                    prompt_template="{document_content}",
                                    max_tokens=250,
                                    section_key=section_key, 
                                    field=field
                                )
                                
                                if response:
                                    # Parse response
                                    parts = response.split('PPA:')
                                    if len(parts) > 1:
                                        ppa_cycle3_parts = parts[1].split('CYCLE3:')
                                        if len(ppa_cycle3_parts) > 1:
                                            results['ppa'][section_key][field] = ppa_cycle3_parts[0].strip()
                                            results['cycle3'][section_key][field] = ppa_cycle3_parts[1].strip()
                
                except Exception as e:
                    logging.error(f"Error processing section {section_key}: {str(e)}")
                    continue
            
            return results
            
        except Exception as e:
            error_msg = f"Error processing files for user {self.user_id}: {str(e)}"
            logging.error(error_msg)
            st.error(error_msg)
            return None
            
        finally:
            self._cleanup_temp_files()
            self._processing_queue.complete_job(self.user_id)

    def save_file(self, uploaded_file, folder_key: str) -> Optional[str]:
        """Save uploaded file with enhanced error handling"""
        if uploaded_file:
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                unique_filename = f"{timestamp}_{uploaded_file.name}"
                file_path = os.path.join(self.folders[folder_key], unique_filename)
                
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"Failed to write file: {file_path}")
                
                return file_path
                
            except Exception as e:
                logging.error(f"Error saving file for user {self.user_id}: {str(e)}")
                return None
        return None

    def _cleanup_temp_files(self):
        """Clean up temporary files"""
        try:
            temp_folder = os.path.join(self.main_folders['NPPG'], f'temp_{self.user_id}')
            if os.path.exists(temp_folder):
                shutil.rmtree(temp_folder)
                os.makedirs(temp_folder, exist_ok=True)
        except Exception as e:
            logging.error(f"Error cleaning temp files for user {self.user_id}: {str(e)}")

    def cleanup_user_data(self):
        """Clean up all user-specific data"""
        try:
            self._processing_queue.complete_job(self.user_id)
            temp_folder = os.path.join(self.main_folders['NPPG'], f'temp_{self.user_id}')
            if os.path.exists(temp_folder):
                shutil.rmtree(temp_folder)
                os.makedirs(temp_folder, exist_ok=True)
                
        except Exception as e:
            logging.error(f"Error cleaning up user data: {str(e)}")