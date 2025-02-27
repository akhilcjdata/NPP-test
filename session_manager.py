from typing import Dict, Optional
from threading import Lock
import logging
from datetime import datetime
import os
import shutil

class SessionManager:
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SessionManager, cls).__new__(cls)
                cls._instance.sessions = {}
                cls._instance.active_processes = {}
                cls._instance.max_concurrent_processes = 3
        return cls._instance
    
    def create_session(self, user_id: str) -> Dict:
        """Create a new session for a user"""
        with self._lock:
            if user_id not in self.sessions:
                self.sessions[user_id] = {
                    'created_at': datetime.now(),
                    'last_activity': datetime.now(),
                    'processing_status': {},
                    'temp_files': []
                }
            return self.sessions[user_id]
    
    def get_session(self, user_id: str) -> Optional[Dict]:
        """Get existing session for a user"""
        return self.sessions.get(user_id)
    
    def update_activity(self, user_id: str):
        """Update last activity time for a session"""
        if user_id in self.sessions:
            self.sessions[user_id]['last_activity'] = datetime.now()
    
    def can_start_process(self, user_id: str) -> bool:
        """Check if user can start a new process"""
        with self._lock:
            active_count = len([p for p in self.active_processes.values() if p == 'processing'])
            if active_count >= self.max_concurrent_processes:
                return False
            if user_id in self.active_processes:
                return False
            self.active_processes[user_id] = 'processing'
            return True
    
    def complete_process(self, user_id: str):
        """Mark process as complete"""
        with self._lock:
            if user_id in self.active_processes:
                del self.active_processes[user_id]
    
    def cleanup_session(self, user_id: str):
        """Clean up session data"""
        try:
            if user_id in self.sessions:
                # Clean up temp files
                for file_path in self.sessions[user_id]['temp_files']:
                    if os.path.exists(file_path):
                        os.remove(file_path)
                
                # Clean up temp directory
                temp_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'NPPG_Files', f'temp_{user_id}')
                if os.path.exists(temp_dir):
                    shutil.rmtree(temp_dir)
                
                # Remove session
                del self.sessions[user_id]
                
                # Clean up active processes
                if user_id in self.active_processes:
                    del self.active_processes[user_id]
                    
        except Exception as e:
            logging.error(f"Error cleaning up session {user_id}: {str(e)}")