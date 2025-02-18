

import streamlit as st
from pdf_processor import PDFProcessor
from display_utils import display_results
from report_generator import download_excel_report
import uuid
import os
from pathlib import Path
import time
from styles import get_user_custom_css, get_theme_css

def initialize_session_state():
    """Initialize session state variables"""
    if 'user_id' not in st.session_state:
        st.session_state.user_id = str(uuid.uuid4())
    if 'processor' not in st.session_state:
        st.session_state.processor = PDFProcessor(st.session_state.user_id)
    if 'processing_status' not in st.session_state:
        st.session_state.processing_status = {}
    if 'theme' not in st.session_state:
        st.session_state.theme = 'default'



def main():
    # Initialize session state
    initialize_session_state()
    
    # Configure page
    st.set_page_config(
        page_title="CONFLICT REPORT CREATOR",
        page_icon="📄",
        layout="wide"
    )
    
    # Add main header with styling
    st.markdown("""
        <h1 style='text-align: center; color: #1a73e8; padding: 1rem 0; margin-bottom: 2rem; border-bottom: 2px solid #1a73e8;'>
            Conflict Report Creator
        </h1>
    """, unsafe_allow_html=True)
    
    # Apply custom CSS
    user_css = get_user_custom_css(st.session_state.user_id)
    theme_css = get_theme_css(st.session_state.theme)
    st.markdown(user_css, unsafe_allow_html=True)
    st.markdown(theme_css, unsafe_allow_html=True)
    
    # File upload columns
    col1, col2 = st.columns(2)
    with col1:
        st.header("Upload Previous Plan Document")
        ppa_file = st.file_uploader(
            "Drag and drop file here", 
            type=['pdf'], 
            key=f"left_{st.session_state.user_id}"
        )
    
    with col2:
        st.header("Upload Restated Plan Document")
        cycle3_file = st.file_uploader(
            "Drag and drop file here", 
            type=['pdf'], 
            key=f"right_{st.session_state.user_id}"
        )
    
    # Process button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        process_button = st.button(
            "Process Documents",
            type="primary",
            use_container_width=True,
            key="process_button"
        )
    
    if process_button:
        if ppa_file is None or cycle3_file is None:
            st.error("Please upload both PDF files before processing.")
        else:
            if st.session_state.processing_status.get(st.session_state.user_id):
                st.warning("Processing is already in progress.")
                return
            
            try:
                # Set processing status
                st.session_state.processing_status[st.session_state.user_id] = True
                
                # Process files with progress indicator
                with st.spinner("Processing files..."):
                    processor = st.session_state.processor
                    results = processor.process_files_simultaneously(ppa_file, cycle3_file)
                    
                    if results:
                        # Display results in columns
                        result_col1, result_col2 = st.columns(2)
                        display_results(results['ppa'], 'Previous Plan', result_col1)
                        display_results(results['cycle3'], 'Restated Plan', result_col2)
                        
                        # Add separator
                        st.markdown("---")
                        
                        # Download report button
                        col1, col2, col3 = st.columns([1, 2, 1])
                        with col2:
                            download_excel_report(
                                results['ppa'], 
                                results['cycle3'],
                                st.session_state.user_id
                            )
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            
            finally:
                # Clear processing status
                if st.session_state.user_id in st.session_state.processing_status:
                    del st.session_state.processing_status[st.session_state.user_id]


def cleanup_session():
    """Clean up session data"""
    try:
        if 'processor' in st.session_state:
            st.session_state.processor.cleanup_user_data()
        if 'processing_status' in st.session_state:
            st.session_state.processing_status = {}
    except Exception as e:
        st.error(f"Error cleaning up session: {str(e)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"Application error: {str(e)}")
    finally:
        cleanup_session()