# display_utils.py
# import streamlit as st
# from typing import Dict, Optional
# import logging

# SECTIONS_TO_DISPLAY = [
#     ('document_info', "Document Information"),
#     ('employer_info', "Employer Information"),
#     ('plan_admin', "Plan Administration"),
#     # ('contribution_types', "Contribution Types"),
#     # ('service_types', "Service Types"),
#     # ('eligibility_types', "Eligibility Types"),
#     # ('vesting_types', "Vesting Types"),
#     # ('compensation_types', "Compensation Types"),
#     # ('contribution_allocation_types', "Contribution Allocation Types"),
#     # ('safe_harbor_types', 'Safe Harbor Types'),
#     # ('matching_contribution_types', 'Matching Contribution Types'),
#     # ('nonelective_contribution_types', 'Nonelective Contribution Types'),
#     # ('prevailing_wage_contribution_types', 'Prevailing Wage Contribution Types'),
#     # ('general_plan_provision_contribution_types', 'General Plan Provisions Contribution Types'),
#     # ('retirement_and_distribution_contribution_types', 'Retirement and Disability Contribution Types'),
#     # ('distribution_contribution_types', 'Distributions Contribution Types'),
#     # ('permitted_elections_types', 'Permitted Election Contribution Types'),
#     # ('participating_employer_types', 'Participating Employer Contribution Types'),
#     # ('subsequent_employer_types', 'Subsequent (Cycle 4) Legal Changes/Optional Updates Contribution Types'),
#     # ('other_provision_employer_types', 'Other Provisions Contribution Types'),
#     # ('document_request_employer_types', 'Document Request Contribution Types'),
#     # ('supporting_forms_information_types', 'Supporting Forms Contribution Types'),
#     # ('administrative_forms_types', 'Administrative Forms Contribution Types'),
#     # ('general_types', 'General Contribution Types')
# ]

# def display_section_results(results: dict, section_name: str, user_id: str):
#     """Display section results in a formatted way"""
#     try:
#         section_key = f"{user_id}_{section_name}"
        
#         # Display section header in blue with underline
#         st.markdown(
#             f"""
#             <div style='color: #0d6efd; font-size: 1.3em; 
#             border-bottom: 2px solid #0d6efd; margin-bottom: 15px; 
#             padding-bottom: 8px;'>
#                 {section_name}
#             </div>
#             """, 
#             unsafe_allow_html=True
#         )
        
#         if results:
#             for field, value in results.items():
#                 # Field name in bold
#                 display_field = field.replace('_', ' ').title()
#                 st.markdown(
#                     f"""
#                     <div style='font-weight: bold; color: #202124; 
#                     margin-top: 10px;'>
#                         {display_field}:
#                     </div>
#                     <div style='margin-left: 8px; color: #3c4043; 
#                     padding: 4px 0;'>
#                         {value}
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )
#         else:
#             st.warning(f"No {section_name} results extracted")
#     except Exception as e:
#         logging.error(f"Error displaying section: {str(e)}")
#         st.error("Error displaying section results")


# def display_results(results: Dict, file_type: str, column):
#     try:
#         with column:
#             # Create card-like container with white background and shadow
#             st.markdown(
#                 """
#                 <div style='background-color: #ffffff; padding: 20px; 
#                 border-radius: 8px; border: 1px solid #e6e6e6; 
#                 margin: 15px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.05);'>
#                 """,
#                 unsafe_allow_html=True
#             )
            
#             if results:
#                 for section_key, section_name in SECTIONS_TO_DISPLAY:
#                     if section_key in results:
#                         display_section_results(
#                             results[section_key],
#                             section_name,
#                             section_key
#                         )
#             else:
#                 st.warning("No results to display")
            
#             st.markdown("</div>", unsafe_allow_html=True)
#     except Exception as e:
#         logging.error(f"Error displaying results: {str(e)}")
#         st.error("Error displaying results")



# def get_display_status(user_id: str) -> Dict:
#     """Get display status for a specific user"""
#     status_key = f"display_status_{user_id}"
#     if status_key not in st.session_state:
#         st.session_state[status_key] = {
#             'sections_displayed': 0,
#             'errors': 0,
#             'last_section': None
#         }
#     return st.session_state[status_key]

# def update_display_status(user_id: str, section: str, success: bool):
#     """Update display status for a specific user"""
#     status = get_display_status(user_id)
    
#     if success:
#         status['sections_displayed'] += 1
#     else:
#         status['errors'] += 1
#     status['last_section'] = section

# def cleanup_display_status(user_id: str):
#     """Clean up display status for a specific user"""
#     status_key = f"display_status_{user_id}"
#     if status_key in st.session_state:
#         del st.session_state[status_key]

# def reset_display(user_id: str):
#     """Reset display for a specific user"""
#     cleanup_display_status(user_id)
#     status = get_display_status(user_id)
#     status['sections_displayed'] = 0
#     status['errors'] = 0
#     status['last_section'] = None


#display_utils.py
import streamlit as st
from typing import Dict, Optional
import logging

SECTIONS_TO_DISPLAY = [
    ('document_info', "Document Information"),
    ('employer_info', "Employer Information"),
    ('plan_admin', "Plan Administration"),
    ('contribution_types', "Contribution Types"),
    ('service_types', "Service Types"),
    ('eligibility_types', "Eligibility Types"),
    ('vesting_types', "Vesting Types"),
    ('compensation_types', "Compensation Types"),
    ('contribution_allocation_types', "Contribution Allocation Types"),
    ('safe_harbor_types', 'Safe Harbor Types'),
    ('matching_contribution_types', 'Matching Contribution Types'),
    ('nonelective_contribution_types', 'Nonelective Contribution Types'),
    ('prevailing_wage_contribution_types', 'Prevailing Wage Contribution Types'),
    ('general_plan_provision_contribution_types', 'General Plan Provisions Contribution Types'),
    ('retirement_and_distribution_contribution_types', 'Retirement and Disability Contribution Types'),
    ('distribution_contribution_types', 'Distributions Contribution Types'),
    ('permitted_elections_types', 'Permitted Election Contribution Types'),
    ('participating_employer_types', 'Participating Employer Contribution Types'),
    ('subsequent_employer_types', 'Subsequent (Cycle 4) Legal Changes/Optional Updates Contribution Types'),
    ('other_provision_employer_types', 'Other Provisions Contribution Types'),
    ('document_request_employer_types', 'Document Request Contribution Types'),
    ('supporting_forms_information_types', 'Supporting Forms Contribution Types'),
    ('administrative_forms_types', 'Administrative Forms Contribution Types'),
    ('general_types', 'General Contribution Types')
]

def display_section_results(results: dict, section_name: str, user_id: str):
    """Display section results in a formatted way"""
    try:
        section_key = f"{user_id}_{section_name}"
        
        # Display section header in blue with underline
        st.markdown(
            f"""
            <div style='color: #0d6efd; font-size: 1.3em; 
            border-bottom: 2px solid #0d6efd; margin-bottom: 15px; 
            padding-bottom: 8px;'>
                {section_name}
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        if results:
            for field, value in results.items():
                # Clean field name for display
                display_field = field.replace('_', ' ').title()
                
                # Display field and value with styling
                st.markdown(
                    f"""
                    <div style='font-weight: bold; color: #202124; 
                    margin-top: 10px;'>
                        {display_field}:
                    </div>
                    <div style='margin-left: 8px; color: #3c4043; 
                    padding: 4px 0;'>
                        {value}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.warning(f"No {section_name} results extracted")
    except Exception as e:
        logging.error(f"Error displaying section: {str(e)}")
        st.error("Error displaying section results")

def display_results(results: Dict, file_type: str, column):
    """Display all results in a formatted layout"""
    try:
        with column:
            # Create card-like container
            st.markdown(
                """
                <div style='background-color: #ffffff; padding: 20px; 
                border-radius: 8px; border: 1px solid #e6e6e6; 
                margin: 15px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.05);'>
                """,
                unsafe_allow_html=True
            )
            
            # Display file type header
            st.markdown(
                f"""
                <div style='font-size: 1.5em; font-weight: bold; 
                color: #202124; margin-bottom: 20px;'>
                    {file_type}
                </div>
                """,
                unsafe_allow_html=True
            )
            
            if results:
                for section_key, section_name in SECTIONS_TO_DISPLAY:
                    if section_key in results:
                        display_section_results(
                            results[section_key],
                            section_name,
                            section_key
                        )
            else:
                st.warning("No results to display")
            
            st.markdown("</div>", unsafe_allow_html=True)
    except Exception as e:
        logging.error(f"Error displaying results: {str(e)}")
        st.error("Error displaying results")

def get_display_status(user_id: str) -> Dict:
    """Get display status for a specific user"""
    status_key = f"display_status_{user_id}"
    if status_key not in st.session_state:
        st.session_state[status_key] = {
            'sections_displayed': 0,
            'errors': 0,
            'last_section': None
        }
    return st.session_state[status_key]

def update_display_status(user_id: str, section: str, success: bool):
    """Update display status for a specific user"""
    status = get_display_status(user_id)
    
    if success:
        status['sections_displayed'] += 1
    else:
        status['errors'] += 1
    status['last_section'] = section

def cleanup_display_status(user_id: str):
    """Clean up display status for a specific user"""
    status_key = f"display_status_{user_id}"
    if status_key in st.session_state:
        del st.session_state[status_key]

def reset_display(user_id: str):
    """Reset display for a specific user"""
    cleanup_display_status(user_id)
    status = get_display_status(user_id)
    status['sections_displayed'] = 0
    status['errors'] = 0
    status['last_section'] = None

def display_comparison(ppa_results: Dict, cycle3_results: Dict, user_id: str):
    """Display side-by-side comparison of results"""
    try:
        # Create columns for comparison
        col1, col2 = st.columns(2)
        
        # Display results in columns
        with col1:
            display_results(ppa_results, "Previous Plan", col1)
        with col2:
            display_results(cycle3_results, "Restated Plan", col2)
            
    except Exception as e:
        logging.error(f"Error displaying comparison: {str(e)}")
        st.error("Error displaying comparison results")