#warning_suppressor.py

import sys
import io
import logging
import warnings
import contextlib
import threading

class StreamlitWarningFilter(logging.Filter):
    def filter(self, record):
        # Suppress specific Streamlit warnings
        suppress_messages = [
            'missing ScriptRunContext',
            'You cannot create Status widgets after rendering non-Status widgets',
        ]
        return not any(msg in record.getMessage() for msg in suppress_messages)

class SuppressStreamlitWarnings:
    _global_lock = threading.Lock()
    _warnings_suppressed = False

    def __init__(self):
        self.original_stderr = sys.stderr
        self.original_logging_levels = {}
        self.warning_filters = []

    def __enter__(self):
        with self._global_lock:
            # Suppress stderr
            sys.stderr = io.StringIO()

            # Suppress warnings globally
            warnings.filterwarnings('ignore', category=UserWarning)
            warnings.filterwarnings('ignore', category=RuntimeWarning)

            # Configure logging suppression
            loggers_to_suppress = [
                'streamlit',
                'root',
                ''  # root logger
            ]

            for logger_name in loggers_to_suppress:
                logger = logging.getLogger(logger_name)
                
                # Store original logging level
                self.original_logging_levels[logger_name] = logger.level
                
                # Set to critical to minimize logging
                logger.setLevel(logging.CRITICAL)
                
                # Add custom filter
                warning_filter = StreamlitWarningFilter()
                logger.addFilter(warning_filter)
                self.warning_filters.append((logger, warning_filter))

            # Mark warnings as suppressed
            self._warnings_suppressed = True

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with self._global_lock:
            # Restore stderr
            sys.stderr = self.original_stderr

            # Restore original warning filters
            warnings.resetwarnings()

            # Restore logging levels and remove filters
            for logger_name, level in self.original_logging_levels.items():
                logger = logging.getLogger(logger_name)
                logger.setLevel(level)

            # Remove custom filters
            for logger, warning_filter in self.warning_filters:
                logger.removeFilter(warning_filter)

            # Mark warnings as no longer suppressed
            self._warnings_suppressed = False

        return False  # Propagate any exceptions

def suppress_streamlit_warnings():
    """
    A decorator that suppresses Streamlit warnings for a function.
    Can be used as a decorator or a context manager.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            with SuppressStreamlitWarnings():
                return func(*args, **kwargs)
        return wrapper
    
    # Allow usage as both decorator and context manager
    return SuppressStreamlitWarnings() if callable(decorator) else decorator

def patch_streamlit_warnings():
    """
    Global patch to reduce Streamlit warnings.
    Call this early in your application initialization.
    
    Note: This method is intentionally left minimal to avoid import errors.
    """
    try:
        import streamlit as st
        
        # Attempt to modify Streamlit's warning behavior if possible
        # This is a best-effort approach and may need adjustments based on Streamlit version
        try:
            # Attempt to suppress specific warnings
            import logging
            streamlit_logger = logging.getLogger('streamlit')
            streamlit_logger.setLevel(logging.ERROR)
        except Exception:
            pass
    except ImportError:
        # Streamlit not available - do nothing
        pass

# Optional: Add a more comprehensive warning suppression
def silence_warnings():
    """
    Comprehensive warning silencing method
    """
    import warnings
    
    # Suppress all warnings
    warnings.filterwarnings('ignore')
    
    # Additional logging suppression
    logging.getLogger('streamlit').setLevel(logging.CRITICAL)
    logging.getLogger().setLevel(logging.CRITICAL)