
# doc_extractor.py

from typing import Dict, Optional, Union, List
from section_config import SECTIONS
from text_beautification import TextBeautifier
import streamlit as st
from threading import Lock
import logging
from datetime import datetime
import time
import re

class ExtractionTracker:
    def __init__(self):
        self.extraction_history: Dict[str, Dict] = {}
        self.lock = Lock()
        self.stats: Dict[str, Dict] = {}
    
    def track_extraction(self, user_id: str, section_key: str, success: bool, error: Optional[str] = None):
        with self.lock:
            # Initialize user tracking if not exists
            if user_id not in self.extraction_history:
                self.extraction_history[user_id] = {}
                self.stats[user_id] = {
                    'total_extractions': 0,
                    'successful_extractions': 0,
                    'failed_extractions': 0,
                    'last_extraction': None
                }
            
            # Update extraction history
            self.extraction_history[user_id][section_key] = {
                'timestamp': datetime.now(),
                'success': success,
                'error': error
            }
            
            # Update stats
            self.stats[user_id]['total_extractions'] += 1
            if success:
                self.stats[user_id]['successful_extractions'] += 1
            else:
                self.stats[user_id]['failed_extractions'] += 1
            self.stats[user_id]['last_extraction'] = datetime.now()

    def get_user_stats(self, user_id: str) -> Dict:
        with self.lock:
            return self.stats.get(user_id, {})

class DocumentSectionExtractor:
    def __init__(self, user_id: Optional[str] = None):
        self.sections = SECTIONS
        self.beautifier = TextBeautifier()
        self.user_id = user_id or st.session_state.get('user_id', 'default')
        self.tracker = ExtractionTracker()
        
        # Initialize rate limiting with safer initialization
        self.rate_limit_key = f"extractor_rate_{self.user_id}"
        self._ensure_rate_limit_initialized()

    def _ensure_rate_limit_initialized(self):
        """Safely initialize rate limit state"""
        if self.rate_limit_key not in st.session_state:
            st.session_state[self.rate_limit_key] = {
                'last_call': time.time(),
                'calls_this_minute': 0
            }

    def _check_rate_limit(self) -> bool:
        """Check if we're within rate limits with safe initialization"""
        # Ensure rate limit is initialized
        self._ensure_rate_limit_initialized()
        
        current_time = time.time()
        last_call = st.session_state[self.rate_limit_key]['last_call']
        
        # Reset counter if minute has passed
        if current_time - last_call >= 60:
            st.session_state[self.rate_limit_key].update({
                'calls_this_minute': 0,
                'last_call': current_time
            })
            return True
            
        # Check limit (60 calls per minute)
        if st.session_state[self.rate_limit_key]['calls_this_minute'] >= 60:
            return False
            
        st.session_state[self.rate_limit_key]['calls_this_minute'] += 1
        return True
    
    

    def find_end_position(self, text: str, end_marker: Union[str, List[str]], start_index: int) -> int:
        """Find the earliest end position from multiple possible end markers"""
        try:
            if not end_marker:
                return -1
            
            # Convert text to lowercase for case-insensitive search
            text_lower = text.lower()
            
            # Ensure we have a list to work with
            markers = end_marker if isinstance(end_marker, list) else [end_marker]
            
            positions = []
            for marker in markers:
                pos = -1
                
                # Try regex pattern matching first
                if isinstance(marker, str) and marker.startswith(r"\d"):
                    try:
                        pattern = re.compile(marker, re.IGNORECASE)
                        match = pattern.search(text[start_index:])
                        if match:
                            pos = start_index + match.start()
                    except Exception:
                        pass
                
                # If regex didn't match, try case-insensitive string search
                if pos == -1:
                    marker_lower = marker.lower()
                    pos = text_lower.find(marker_lower, start_index)
                    
                    # If still not found, try without "Section:" prefix
                    if pos == -1 and "section:" in marker_lower:
                        without_prefix = marker_lower.replace("section:", "").strip()
                        pos = text_lower.find(without_prefix, start_index)
                
                if pos != -1:
                    positions.append(pos)
            
            return min(positions) if positions else len(text)
                
        except Exception as e:
            logging.error(f"Error finding end position for user {self.user_id}: {str(e)}")
            return -1

    
        
    def extract_section(self, text: str, section_key: str) -> Optional[str]:
        """Extract and beautify a specific section with rate limiting and tracking"""
        try:
            # Check rate limit
            if not self._check_rate_limit():
                wait_time = 60 - (time.time() - st.session_state[self.rate_limit_key]['last_call'])
                st.warning(f"Rate limit reached. Please wait {wait_time:.1f} seconds.")
                time.sleep(min(wait_time, 5))
                return self.extract_section(text, section_key)

            if section_key not in self.sections:
                error_msg = f"Section key '{section_key}' not found in configured sections"
                self.tracker.track_extraction(self.user_id, section_key, False, error_msg)
                return None

            section = self.sections[section_key]
            start_markers = section["start"] if isinstance(section["start"], list) else [section["start"]]
            end_marker = section["end"]

            # Convert text to lowercase for case-insensitive search
            text_lower = text.lower()
            
            # Find all start markers and their positions
            start_positions = []
            
            for start_marker in start_markers:
                # Try regex pattern matching first
                if isinstance(start_marker, str) and start_marker.startswith(r"\d"):
                    try:
                        pattern = re.compile(start_marker, re.IGNORECASE)
                        match = pattern.search(text)
                        if match:
                            start_positions.append((match.start(), len(match.group(0))))
                            continue
                    except Exception:
                        pass
                
                # Try case-insensitive string search
                start_marker_lower = start_marker.lower()
                found_index = text_lower.find(start_marker_lower)
                if found_index != -1:
                    start_positions.append((found_index, len(start_marker)))
                    continue
                    
                # If still not found, try without "Section:" prefix
                if "section:" in start_marker_lower:
                    without_prefix = start_marker_lower.replace("section:", "").strip()
                    found_index = text_lower.find(without_prefix)
                    if found_index != -1:
                        start_positions.append((found_index, len(without_prefix)))
            
            # If we found any start markers, use the earliest one
            if start_positions:
                # Sort by position
                start_positions.sort(key=lambda x: x[0])
                start_index = start_positions[0][0]
                marker_length = start_positions[0][1]
                
                # Find end position using the existing function
                end_index = self.find_end_position(text, end_marker, start_index + marker_length)
                
                # Extract and beautify text
                if end_index == -1:
                    extracted_text = text[start_index:].strip()
                else:
                    extracted_text = text[start_index:end_index].strip()
                
                beautified_text = self.beautifier.beautify_text(extracted_text)
                
                # Track successful extraction
                self.tracker.track_extraction(self.user_id, section_key, True)
                
                return beautified_text
            else:
                # No matching start marker found
                error_msg = f"No matching start marker found for section: {section_key}"
                self.tracker.track_extraction(self.user_id, section_key, False, error_msg)
                return None

        except Exception as e:
            error_msg = f"Error extracting section {section_key}: {str(e)}"
            self.tracker.track_extraction(self.user_id, section_key, False, str(e))
            logging.error(error_msg)
            return None

    def extract_all_sections(self, text: str) -> Dict[str, str]:
        """Extract and beautify all sections with tracking"""
        results = {}
        
        for section_key in self.sections.keys():
            try:
                extracted = self.extract_section(text, section_key)
                if extracted:
                    results[section_key] = extracted
                    
            except Exception as e:
                error_msg = f"Error processing section {section_key}: {str(e)}"
                self.tracker.track_extraction(self.user_id, section_key, False, str(e))
                logging.error(error_msg)
                continue
        
        return results

    def get_extraction_stats(self) -> Dict:
        """Get extraction statistics for current user"""
        return self.tracker.get_user_stats(self.user_id)

    def cleanup_user_data(self):
        """Clean up user-specific data"""
        try:
            # Clean up rate limiting data
            if self.rate_limit_key in st.session_state:
                del st.session_state[self.rate_limit_key]
            
            # Clean up extraction history
            if self.user_id in self.tracker.extraction_history:
                del self.tracker.extraction_history[self.user_id]
            
            # Clean up stats
            if self.user_id in self.tracker.stats:
                del self.tracker.stats[self.user_id]
                
        except Exception as e:
            logging.error(f"Error cleaning up user data: {str(e)}")