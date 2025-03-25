# Document Information Section Prompts
# prompt_list.py
DOCUMENT_INFO_PROMPTS = {
    'document_package/Plan_Type': """
    Analyze text and extract the selected option in DOCUMENT PACKAGE or TYPE OF PLAN section.
    Return only the selected option without additional text.
    The text content is: {document_content}
    """,

    'firm_name': """
    Look for the firm name in the following specific locations:
    1. After "NAME OF FIRM or FIRM NAME producing this document" or
    2. After "Name of your firm:" or "FIRM NAME"
       
    Choose the most appropriate firm name considering these rules:
    - Prefer names ending in INC., LLC, CORP, etc.
    - Look for names in ALL CAPS if available
      
    Return ONLY the firm name without any prefixes or additional text.
    
    Text content: {document_content}
    """


}


# Employer Information Section Prompts
EMPLOYER_INFO_PROMPTS = {
    'employer_name': """
    Extract the Employer's Name from the document.
    Return only the employer name without any additional text.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'employer_state': """
    Extract the Employer's Principal Office state.
    Return only the state name without any additional text.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,

    'employer_street': """
    Looking for Employer's street address.
    The question asks for: Street address under Employer's Address section.

    Return only one of the following values without any additional text:
    '{street_address}' - if text is provided after 'Street' (replace {street_address} with exact text found)
    'NA' - if no street address is provided

    Check for:
    - Text that appears after '(Street)'
    - Should capture complete street address
    The text content is: {document_content}
    """,
    
    'employer_city': """
    Extract the selected Employer city the document.
    Return only the city name without any additional text.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,

    'employer_state': """
    Extract the selected Employer state the document.
    Return only the state name without any additional text.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'employer_phone': """
    Extract the Employer's telephone number or phone number.
    Return only the telephone number or phone number without any additional text.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,


    'employer_zip': """
    Extract the Employer's zip number.
    Return only the zip without any additional text.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'employer_ein': """
    Extract the Employer's ID (EIN) number.
    Return only the EIN without any additional text.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,


    'Employer_plan_number': """
    Looking for 3-digit Plan Number used for Form 5500 reporting.
    The question asks to select one Plan Number from options 001-004 or specify another number.

    Return only one of the following values without any additional text:
    '001' - if '001' shows '☒ selected '
    '002' - if '002' shows '☒ selected '
    '003' - if '003' shows '☒ selected '
    '004' - if '004' shows '☒ selected '
    '{number}' - if custom number option shows '☒ selected ' (replace {number} with specified number)
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Any specified number if custom option selected
    The text content is: {document_content}
    """,

     'employer_Trust ID (TIN)': """
    Extract the Employer's Trust ID (TIN) number.
    Return only the Trust ID (TIN) number without any additional text.
    If not found, return 'None'.
    The text content is: {document_content}
    """
}


# Document Information Section Prompts and Employer Information Section Prompts remain the same...

# Plan Administration Section Prompts
PLAN_ADMIN_PROMPTS = {
    'plan_information': """
    Extract the selected option from Plan Information.
    Look for either 'New Plan' or 'Restatement'.
    Return only the selected option without additional text.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'plan_name_retained': """
    Extract whether the pre-restatement name of the Plan is being retained.
    Return only 'Yes' or 'No' based on the selection.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'money_purchase_plan': """
    Looking for whether Plan was previously a Money Purchase Plan or contains Money Purchase Plan assets.
    The question asks: "Was this Plan previously a Money Purchase Plan OR does this Plan contain Money Purchase Plan assets due to a merger or similar transfer of assets (i.e., other than as a rollover)?"

    Return only one of the following values without any additional text:
    'No or N/A' - if 'No or N/A (skip to 11)' shows '☒ selected '
    'Yes, money purchase assets were merged or transferred into this plan' - if 'Yes' and 'money purchase assets were merged or transferred into this plan' show '☒ selected '
    'Yes, conversion from money purchase plan: occurred prior to restatement' - if 'Yes', 'the plan is a conversion from a money purchase plan' and 'The conversion occurred prior to this restatement' show '☒ selected '
    'Yes, conversion from money purchase plan: being made with this restatement' - if 'Yes', 'the plan is a conversion from a money purchase plan' and 'The conversion is being made with this restatement' show '☒ selected '
    'none' - if all options show '☐ unselected'
    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Must provide for annuities at 98b or 99b if Yes selected
    - Skip to question 11 for certain selections
    The text content is: {document_content}
    """,

    'conversion_participants_vested_converted_funds': """
    extract what is seletected in the conversion, shall Participants be fully vested in the converted funds?
    if nothing is selected please reture 'None'
    The text content is: {document_content}
    """,
    
    'money_purchase_plan_name': """
    Looking for the name of the money purchase plan.
    Extract what is selected for the name of the money purchase plan?
    if nothing is selected please reture 'None'
    
    The text content is: {document_content}
    """,
    

    'plan_frozen': """
    Extract whether the Plan has been frozen (no new Participants and no further contributions).
    Return only 'Yes' if yes shows '☒ selected'
    Return Onnly 'No' if No shows '☒ selected'
    If Yes and freeze date is provided, include the date.
    if nothing is selected please reture 'None'
    The text content is: {document_content}
    """,


    'initial_effective_date': """
    Looking and extract for Initial Effective Date after text 'Initial Effective Date (month) (day) (year)'
    Extract and Return only the date in MM/DD/YYYY format without any additional text.
    Return 'None' if no date found.

    Check for:
    - Date appearing after 'Initial Effective Date'
    - Ensure day and year in correct format
    The text content is: {document_content}
    """,


    'plan_name': """
    Looking for Plan Name/Title from lines labeled a. through e.
    Combine all provided text lines into complete plan name.

    Return only the complete plan name without additional text.
    If no plan name found, return 'NA'.

    Check for:
    - Text after lines labeled a. through e.
    - Combine text from all provided lines
    - Maintain exact punctuation
    - Skip empty lines marked with underscores
    The text content is: {document_content}
    """,

    'separate_trust_name': """
    Extract the Separate Trust Name/Title of Document.
    If N/A is selected, return 'Same as Plan Name'.
    If specific name provided, return that name.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,

    'witness_signatures': """
    Extract whether witnesses are required for Employer's signature.
    Return only 'Yes' or 'No' based on the selection.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,

    'electronic_signature': """
    Extract whether the document will be signed electronically.
    Return only 'Yes' or 'No' based on the selection.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,

   'affiliated_employer_allocation': """
    Extract whether profit sharing contributions and forfeitures will be allocated to all affiliated adopting employers.
    Return only 'Allocated to all affiliated adopting employers' if option 'Allocated to all affiliated adopting employers' shows '☒ selected'
    if nothing is selected please reture 'None'
    The text content is: {document_content}
    """,

#     # 'plan_year_type': """
#     # Extract the Plan Year type and details.
#     # If calendar year, return 'Calendar Year'.
#     # If specific dates, return start and end dates in MM/DD format.
#     # If 52/53 week year, include that specification.
#     # If not found, return 'NA'.
#     # The text content is: {document_content}
#     # """,


#     # 'short_plan_year': """
#     # Extract Short Plan Year information if specified.
#     # If provided, return start and end dates in MM/DD/YYYY format.
#     # '52/53 week year ending' - if 52/53 week year ending is this option shows '☒ selected '
#     # If not specified, return 'None'.
#     # The text content is: {document_content}
#     # """,

    'plan_year_dates': """
    Looking for Plan Year dates specifically after "Plan Year" text where:

    - The Begin date follows 'Begins' and appears after or before '(month day)'
    - The End date follows 'Ends' and appears after or before '(month day)'
    -

    Return only one of the following formats without any additional text:
    'Begin Date: {found_date}, End Date: {found_date}' - Use exact dates as they appear in text


    Check for:
    - Must find exact text matching 'Begins' followed by a date
    - Must find exact text matching 'Ends' followed by a date
    - Use dates exactly as written in document
    - Do not convert or modify date formats
    - Only extract dates that appear after the marker '(month day)'
    The text content is: {document_content}
    """,


    'administrator': """
    Extract who will be the Administrator.
    If Employer, return 'Employer'.
    If Other, return the specified name.
    If not found, return 'NA'.
    The text content is: {document_content}
    """
}


CONTRIBUTION_TYPES_PROMPTS = {


    'special_ADP_Provision_simple_401k_plan': """
    Looking for SIMPLE 401(k) Plan selection after "Is this a SIMPLE 401(k) Plan?"

    Return only one of the following values without any additional text:
    'No' - if 'No (skip to c./d.)' shows '☒ selected '

    'Yes with minimum contribution amount: ${amount}' - if 'Yes' shows '☒ selected ' and amount specified after '$'

    'Yes with effective date: N/A' - if 'Yes' and 'N/A (New Plan OR Amendment and Restatement...)' show '☒ selected '

    'Yes with effective date: January 1, {year}' - if 'Yes' and 'January 1' option show '☒ selected '

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Dollar amount if specified after '$'
    - Year if specified after 'January 1'
    - Cannot be selected with 11b
    The text content is: {document_content}
    """,

    'adp_safe_harbor_accounts': """
    Looking for ADP Safe Harbor Account requirements after "Must the Plan provide for ADP Safe Harbor Accounts?"

    Return only one of the following values without any additional text:
    'No, there have never been any type of ADP safe harbor contributions, nor will any ever be made in the future' - if this option shows '☒ selected '

    'Yes: safe harbor contributions are being made or might be made in the future' - if 'Yes' and this sub-option show '☒ selected '

    'Yes: all such contributions have been permanently discontinued but must retain accounts' - if 'Yes' and this sub-option show '☒ selected '

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Main 'Yes' selection must match with sub-option selection
    - Cannot be selected with 11b or 21b
    The text content is: {document_content}
    """,

    'acp_safe_harbor': """
    Looking for ACP Safe Harbor selection after "ACP SAFE HARBOR" in text.

    Return only one of the following values without any additional text:
    'Every ADP safe harbor plan year will also be an ACP safe harbor plan year' - if this exact option shows '☒ selected '
    'none' - if option shows '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before option
    - Only applicable if 21d1 selected
    - Will require full restatement to discontinue if selected
    The text content is: {document_content}
    """,

    'contribution_types_elective_deferrals': """
    Looking for Elective Deferral contribution types after "Contribution Types" section.

    Return only one of the following values without any additional text:
    'Pre-tax salary reduction contributions only: currently permitted' - if 'The Plan provides for pre-tax salary reduction contributions only' and 'currently permitted' show '☒ selected '

    'Pre-tax salary reduction contributions only: not currently permitted, but elective deferral accounts must be retained' - if 'The Plan provides for pre-tax salary reduction contributions only' and this option shows '☒ selected '

    For pre-tax and Roth combinations, combine selected options with commas:
    'The Plan provides for both pre-tax and Roth salary reduction contributions:' - if this shows '☒ selected '
    Then add:
    - 'pre-tax deferrals are currently permitted'
    - 'pre-tax deferrals are not currently permitted but accounts must be retained'
    - 'Roth salary reduction contributions are currently permitted'
    - 'Roth salary reduction contributions are not currently permitted, but accounts must be retained'

    For In-plan Roth options, add exact text:
    - 'N/A, no provision should be made for such contributions (skip to 22d)'
    - 'in-plan Roth rollovers currently permitted'
    - 'in-plan Roth rollovers not currently permitted, but accounts must be retained'
    - 'in-plan Roth transfers currently permitted'
    - 'in-plan Roth transfers not currently permitted, but accounts must be retained'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Use exact text as it appears in document
    The text content is: {document_content}
    """,

    'other_contributions': """
    Looking for Other contribution types selected after "Other contributions: (select at least one)".

    Return only one of the following values without any additional text:
    'Money Purchase Employer contributions currently implemented' - if 'Money Purchase Employer contributions' and 'currently implemented' show '☒ selected '
    'Money Purchase Employer contributions not currently implemented, but accounts must be retained' - if 'Money Purchase Employer contributions' and this option show '☒ selected '

    'Matching Contributions on Elective Deferrals currently implemented' - if 'Matching Contributions on Elective Deferrals' and 'currently implemented' show '☒ selected '
    'Matching Contributions on Elective Deferrals not currently implemented, but accounts must be retained' - if 'Matching Contributions on Elective Deferrals' and this option show '☒ selected '

    'Nonelective Profit Sharing Contributions currently implemented' - if 'Nonelective Profit Sharing Contributions' and 'currently implemented' show '☒ selected '
    'Nonelective Profit Sharing Contributions not currently implemented, but accounts must be retained' - if 'Nonelective Profit Sharing Contributions' and this option show '☒ selected '

    'Nonelective Prevailing Wage Contributions (PWCs) currently implemented' - if 'Nonelective Prevailing Wage Contributions (PWCs)' and 'currently implemented' show '☒ selected '
    'Nonelective Prevailing Wage Contributions (PWCs) not currently implemented, but accounts must be retained' - if 'Nonelective Prevailing Wage Contributions (PWCs)' and this option show '☒ selected '

    'Employee Voluntary (after-tax) Contributions currently permitted' - if 'Employee Voluntary (after-tax) Contributions' and 'currently permitted' show '☒ selected '
    'Employee Voluntary (after-tax) Contributions not currently permitted, but accounts must be retained' - if 'Employee Voluntary (after-tax) Contributions' and this option show '☒ selected '

    'Rollover Contributions (other than in-plan Roth rollovers) currently permitted' - if 'Rollover Contributions' and 'currently permitted' show '☒ selected '
    'Rollover Contributions (other than in-plan Roth rollovers) not currently permitted, but accounts must be retained' - if 'Rollover Contributions' and this option show '☒ selected '

    If multiple options show '☒ selected ', combine them with commas.

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Match exact text from document
    - Only include options marked as selected
    The text content is: {document_content}
    """,

    'Additional_401(k)_Plan_features_specific_adp_safe_harbor_accounts': """
    Looking for which specific ADP Safe Harbor Accounts must be provided after "Specific ADP Safe Harbor Accounts. The Plan must provide accounts for:"

    Return only one of the following values without any additional text:
    'Both traditional and qualified (QACA) safe harbor contributions' - if this option shows '☒ selected '
    'Only traditional ADP safe harbor contributions' - if this option shows '☒ selected '
    'Only qualified (QACA) ADP safe harbor contributions' - if this option shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    The text content is: {document_content}
    """,

    'traditional_adp_safe_harbor_status': """
    Looking for status of Traditional ADP Safe Harbor Accounts after "Traditional ADP Safe Harbor Accounts".

    Return only one of the following values without any additional text:
    'Such contributions are currently in effect or may be made in the future' - if this option shows '☒ selected '
    'Such contributions are permanently discontinued, but accounts must be retained' - if this option shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    The text content is: {document_content}
    """,

    'qualified_adp_safe_harbor_status': """
    Looking for status of Qualified (QACA) ADP Safe Harbor Contributions after "Qualified (QACA) ADP Safe Harbor Contributions".

    Return only one of the following values without any additional text:
    'Such contributions are currently in effect or may be made in the future' - if this option shows '☒ selected '
    'Such contributions are permanently discontinued, but accounts must be retained' - if this option shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    The text content is: {document_content}
    """,

    'automatic_contribution_arrangement': """
    Looking for automatic contribution arrangement status after "Does the Plan provide for an automatic contribution arrangement?"

    Return only one of the following values without any additional text:
    'No (there is currently no EACA, QACA, or other automatic contribution arrangement in place, and never has been)' - if this option shows '☒ selected '

    'Yes the Plan should provide for an ACA that does not comply with the EACA or QACA requirements' - if 'Yes' and this sub-option show '☒ selected '

    'Yes the Plan should provide for an EACA, but no QACA' - if 'Yes' and this sub-option show '☒ selected '

    'Yes the Plan should provide for an ACA that complies with the QACA requirements, but no EACA' - if 'Yes' and this sub-option show '☒ selected '

    'Yes the Plan should provide for an ACA that complies with both the QACA and EACA requirements' - if 'Yes' and this sub-option show '☒ selected '

    'Yes the Plan should provide for an ACA that will become a EACA for the Plan Year beginning: {date}' - if 'Yes' and this sub-option show '☒ selected '

    'Yes the Plan should provide for an ACA that will become a QACA for the Plan Year beginning: {date}' - if 'Yes' and this sub-option show '☒ selected '

    'Yes the Plan should provide for an ACA that will become a combined QACA and EACA for the Plan Year beginning: {date}' - if 'Yes' and this sub-option show '☒ selected '

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    The text content is: {document_content}
    """,

    'effective_date_of_current_aca_eaca_qaca': """
    Looking for effective date of current ACA, EACA, or QACA in section 23.11.
    Return only one of the following values without any additional text:
    'Before effective date: {date}' - if option j shows '☒ selected ' and a date is specified 
    'Effective date of document' - if option k shows '☒ selected '
    'After effective date: {date}' - if option l shows '☒ selected ' and a date is specified
    'none' - if all options show '☐ unselected' or 23i5, 23i6, or 23i7 is selected
    Check for:
    - '☒ selected ' or '☐ unselected' before each option 
    - Date specified in options j and l
    - Skip if 23i5, 23i6, or 23i7 is selected
    The text content is: {{document_content}}
    """
   
}



SERVICE_TYPES_PROMPTS = {


    'year_service_method': """
    Look for Year of Service method for Eligibility, Vesting and Benefit Accrual.
    If Hours of Service Method selected, return 'Hours of Service Method'.
    If Elapsed Time Method selected, return 'Elapsed Time Method'. 
    If different methods used, return 'Different methods used'.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'eligibility_service': """
    Look for Eligibility Year of Service method.
    Return one of:
    'N/A - No service required'
    'Hours of Service - Date of hire'
    'Hours of Service - Plan Year'
    'Elapsed Time Method'
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'vesting_service': """
    Look for Vesting Year of Service method.
    Return one of:
    'N/A - 100% vesting'
    'Hours of Service - Date of hire'
    'Hours of Service - Plan Year'
    'Elapsed Time Method'
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'accrual_service': """
    Look for Accrual Year of Service method.
    Return one of:
    'N/A - No service required'
    'Hours of Service - Plan Year'
    'Elapsed Time Method'
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'hours_equivalency': """
    Look for Hours of Service Method Equivalencies.
    Return one of:
    'Actual hours'
    'Days worked (10 hours per day)'
    'Weeks worked (45 hours per week)'
    'Semi-monthly periods (95 hours)'
    'Monthly (190 hours)'
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'equivalency_applies_to': """
    Look for who equivalency method applies to.
    Return one of:
    'All Employees'
    'Employees without service records'
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'hours_for_year': """
    Look for specified hours for Year of Service.
    Return specified number if present.
    Return '1,000' if default.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'predecessor_employers': """
    Look for predecessor employer treatment.
    Return one of:
    'No'
    'Specified employer: [name]'
    'Acquired entities only'
    Include limitations if selected.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,

    'excluded_employees': """
    Look for excluded employee categories.
    Return one of:
    'No exclusions'
    'Same exclusions for all: [list categories]'
    'Different exclusions by type'
    List checked categories only.
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'deferral_exclusions': """
    Look for elective deferral exclusions.
    Return one of:
    'No exclusions'
    'Excluded categories: [list categories]'
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'matching_exclusions': """
    Look for matching contribution exclusions.
    Return one of:
    'No exclusions'
    'Excluded categories: [list categories]'
    If not found, return 'NA'.
    The text content is: {document_content}
    """,
    
    'profit_sharing_exclusions': """
    Look for profit sharing/money purchase contribution exclusions.
    Return one of:
    'No exclusions'
    'Excluded categories: [list categories]'
    If not found, return 'NA'.
    The text content is: {document_content}
    """
}



ELIGIBILITY_TYPES_PROMPTS = {

    'conditions_for_eligiblity': """
    Looking for eligibility conditions after "Conditions for Eligibility. Any Eligible Employee will be eligible to participate upon satisfaction of the following:"

    Return only one of the following values without any additional text:
    'No, either (1) this is a 401(k) plan having different eligibility conditions apply for different contribution types or (2) this is a straight profit sharing plan or money purchase plan that requires more than 1 year of service' - if this option shows '☒ selected '

    If 'Yes' shows '☒ selected ', combine selected conditions with commas:
    'Yes', 'Date of Hire' - if these show '☒ selected '
    'Yes', 'AGE: 20 1/2' - if these show '☒ selected '
    'Yes', 'AGE: 21' - if these show '☒ selected '
    'Yes', 'AGE: {specified_age}' - if this shows '☒ selected '
    'Yes', 'SERVICE: {months} months of service' - if this shows '☒ selected '
    'Yes', 'SERVICE: 1 Year of Service' - if this shows '☒ selected '
    'Yes', 'SERVICE: {hours} Hours of Service within {months} consecutive months' - if this shows '☒ selected '
    'Yes', 'SERVICE: other: {specified_service}' - if this shows '☒ selected '

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Specified values for age, months, hours where applicable
    The text content is: {document_content}
    """,

    'waiver_of_conditions': """
    Looking for waiver of eligibility conditions after "Waiver of Conditions" and "if 34b2 or 34b3, are any conditions waived?"

    Return only one of the following values without any additional text:
    'Yes on {date}, service requirement waived' - if 'Yes' shows '☒ selected ' and 'service requirement' shows '☒ selected '
    'Yes on {date}, age requirement waived' - if 'Yes' shows '☒ selected ' and 'age requirement' shows '☒ selected '
    'Yes on {date}, service requirement and age requirement waived' - if both requirements show '☒ selected '

    Add if selected:
    ', waiver is for: {specified_group}' - if this option shows '☒ selected '
    ', Participant must wait until next plan entry date' - if this option shows '☒ selected '

    'none' - if all options show '☐ unselected' or '☐'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Date and group specifications where provided
    The text content is: {document_content}
    """,

    'eligibility_varyby_contribution': """
    Looking for Eligibility conditions for Elective Deferrals after "Eligibility - Elective Deferrals:"

    Return only one of the following values without any additional text:
    'Date of hire (no age or service)' - if this option shows '☒ selected '
    'Eligibility is as follows' - if this option shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

   'age_requirement_elective_deferrals': """
    Looking for Age Requirement for Elective Deferrals after "Age Requirement - Elective Deferrals"

    Return the text of all selected options, combined with commas if multiple are selected.
    Example returns:
    - 'No age requirement (only service)' - if this option is selected
    - 'Age requirement is: 21' - if these options are selected
    - 'Age requirement is: {age}' - if custom age specified
    - If multiple selected: 'No age requirement (only service), Age requirement is: 21'
    - 'None' - if no options show selected

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Exact text as shown in document
    The text content is: {document_content}
    """,

    'service_requirement_elective_deferrals': """
    Looking for Service Requirement for Elective Deferrals after "Service Requirement - Elective Deferrals"

    Return the text of all selected options, combined with commas if multiple are selected.
    Example returns:
    - 'No service requirement (only age)' - if No service requirement (only age) option is ☒ selected 
    - 'Service requirement is: 1 Year of Service' - if these options are selected
    - 'Service requirement is: {months} months' - if months specified
    - 'Service requirement is: {hours} Hours of Service within {months} consecutive months' - if hours specified
    - 'Service requirement is: other: {requirement}' - if other requirement specified
    - If multiple selected: 'No service requirement (only age), Service requirement is: 1 Year of Service'
    - 'None' - if no options show selected

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Exact text as shown in document
    The text content is: {document_content}
    """,

    'eligibility_matching_contribution': """
    Looking for Eligibility conditions for Matching Contribution after "Eligibility - Matching Contribution"

    Return the text of all selected options.
    Example returns:
    - 'Date of hire (no age or service)' - if this option is ☒ selected 
    - 'Eligibility is as follows' - if this option is ☒ selected 
    - 'None' - if no options show ☒ selected 

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Exact text as shown in document
    The text content is: {document_content}
    """,

    'age_requirement_matching_contribution': """
    Looking for Age Requirement for Matching Contribution after "Age Requirement - Matching Contribution"

    Return the text of selected options, combined with commas if multiple selected:
    'No age requirement (only service)' - if 'No age requirement (only service)' shows '☒ selected '
    'Age requirement is:' - if 'Age requirement is:' shows '☒ selected '
    '20 1/2' - if '20 1/2' shows '☒ selected '
    '21' - if '21' shows '☒ selected ' 
    'age {number}' - if 'age ___' shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'service_requirement_matching_contribution': """
    Looking for Service Requirement for Matching Contribution after "Service Requirement - Matching Contribution"

    Return the text of selected options, combined with commas if multiple selected:
    'No service required (only age)' - if 'No service required (only age)' shows '☒ selected '
    'Service requirement is:' - if 'Service requirement is:' shows '☒ selected '
    '{number} months' - if '_______ months' shows '☒ selected '
    '1 Year of Service' - if '1 Year of Service' shows '☒ selected '
    '1 1/2 years' - if '1 1/2 years' shows '☒ selected '
    '2 years' - if '2 years' shows '☒ selected '
    '{hours} Hours of Service within {months} consecutive months' - if 'Hours of Service' shows '☒ selected '
    'other: {requirement}' - if 'other:' shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Numbers specified in blank spaces
    The text content is: {document_content}
    """,

    'waiver_conditions_matching_contribution': """
    Looking for waiver of conditions for Matching Contributions after "Waiver of Conditions - Matching Contribution"

    Return the text of selected options, combined with commas if multiple selected:
    'Yes, if employed on ______________________________ (enter a date)' - if 'Yes, if employed on ______________________________ (enter a date)' shows '☒ selected '
    'service requirement (may let part-time employees into the Plan)' - if 'service requirement (may let part-time employees into the Plan)' shows '☒ selected '
    'age requirement' - if 'age requirement' shows '☒ selected '
    'waiver is for: _____________________________________ ' - if 'waiver is for: _____________________________________' shows '☒ selected '
    'the Participant must wait, however, until the next plan entry date' - if 'the Participant must wait, however, until the next plan entry date' shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'eligibility_profit_sharing_mp': """
    Looking for Eligibility conditions for Profit Sharing or Money Purchase Contribution after "Eligibility - Profit Sharing or Money Purchase Contribution"

    Return the text of selected options, combined with commas if multiple selected:
    'Date of hire (no age or service requirement)' - if 'Date of hire (no age or service requirement)' shows '☒ selected '
    'Eligibility is as follows:' - if 'Eligibility is as follows:' shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'age_requirement_profit_sharing_mp':"""
    Looking for Age Requirement for Profit Sharing or Money Purchase Contribution after "Age Requirement - Profit Sharing or Money Purchase Contribution"

    Return the text of selected options, combined with commas if multiple selected:
    'No age requirement (only service)' - if 'No age requirement (only service)' shows '☒ selected '
    'Age requirement is:' - if 'Age requirement is:' shows '☒ selected '
    '20 1/2' - if '20 1/2' shows '☒ selected '
    '21' - if '21' shows '☒ selected '
    'age _______ (may not exceed 21)' - if 'age _______ (may not exceed 21)' shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'service_requirement_profit_sharing_mp': """
    Looking for Service Requirement for Profit Sharing or Money Purchase Contribution after "Service Requirement - Profit Sharing or Money Purchase Contribution"

    Return the text of selected options, combined with commas if multiple selected:
    'No service required (only age)' - if 'No service required (only age)' shows '☒ selected '
    'Service requirement is:' - if 'Service requirement is:' shows '☒ selected '
    '_______ months (not to exceed 24 months)' - if '_______ months (not to exceed 24 months)' shows '☒ selected '
    '1 Year of Service' - if '1 Year of Service' shows '☒ selected '
    '1 1/2 years' - if '1 1/2 years' shows '☒ selected '
    '2 years' - if '2 years' shows '☒ selected '
    '_______ Hours of Service (not to exceed 1,000) within _______ consecutive months' - if this option shows '☒ selected '
    'other: __________ (may not exceed 2 Years of Service)' - if this option shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'waiver_conditions_ps_mp': """
    Looking for waiver of conditions for Profit Sharing or Money Purchase Contribution after "Waiver of Conditions - Profit Sharing or Money Purchase Contribution"

    Return the text of selected options, combined with commas if multiple selected:
    'Yes, if employed on ____________ (enter a date)' - if 'Yes, if employed on ____________ (enter a date)' shows '☒ selected '
    'service requirement (may let part-time employees into the Plan)' - if 'service requirement (may let part-time employees into the Plan)' shows '☒ selected '
    'age requirement' - if 'age requirement' shows '☒ selected '
    'waiver is for: __________ (e.g., employees of a specific division or employees covered by an IRC §410(b)(6)(C) acquisition)' - if this option shows '☒ selected '
    'the Participant must wait, however, until the next plan entry date' - if 'the Participant must wait, however, until the next plan entry date' shows '☒ selected '
    'none' - if all options show '☐ unselected or :unselected: ☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'entry_date_rules': """
    Looking for Entry Date rules after "Entry Date. Is the entry date the same for all contribution types?"

    Return the text of selected options, combined with commas if multiple selected:
    'No, different entry dates apply for different contribution types' - if 'No, different entry dates apply for different contribution types' shows '☒ selected '

    'Yes, same entry date applies for all contribution types of the Plan' - if 'Yes, same entry date applies for all contribution types of the Plan' shows '☒ selected '

    If 'Yes' is selected, include the selected entry date option:
    'date eligibility requirements are met' - if this option shows '☒ selected '
    'dual entry (1st day of year and 6 months later)' - if this option shows '☒ selected '
    '1st day of the month coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    '1st day of the Plan Year coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    '1st day of the Plan Year quarter coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    'other: ______________________________________________' - if this option shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

   'additional_entry_date': """
    Looking for additional one-time entry date options after "AND, should there be an additional one-time entry date?"

    Return the text of selected options, combined with commas if multiple selected:
    'N0'-if 'No' shows '☒ selected '
    'Yes, and the date is: the date specified at 34c' - if 'Yes' and 'the date specified at 34c' show '☒ selected '
    'Yes, and the date is: other (specify date): _______________' - if 'Yes' and this option show '☒ selected '

    If 'Yes' with other date is selected, include any group limitation:
    'no' - if this option shows '☒ selected '
    'yes, any individuals who worked for the following company immediately before becoming an employee (of the plan sponsor): ______________________' - if this option shows '☒ selected '
    'yes, other (specify group) (must be definitely determinable and nondiscriminatory): _____________' - if this option shows '☒ selected '
    'none' - if all options show '☐ unselected' or ':unselected:'

    Check for:
    - '☒ selected ' or '☐ unselected' or ':unselected:' before each option.
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'entry_date_elective_deferrals': """
    Looking for Entry Date requirements for Elective Deferrals after "Entry Date - Elective Deferrals"

    Return the text of selected options, combined with commas if multiple selected:
    'No entry date requirement (employee enters on the date eligibility requirements are met)' - if 'No entry date requirement (employee enters on the date eligibility requirements are met) (skip to e./f.)' shows '☒ selected '
    'Participant must wait for first entry date:' - if 'Participant must wait for first entry date:' shows '☒ selected '
    'dual entry (1st day of year and 6 months later)' - if this option shows '☒ selected '
    '1st day of the month coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    '1st day of the Plan Year coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    '1st day of the Plan Year quarter coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    'other: ___________________________________________________________' - if this option shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'additional_entry_date_elective_deferrals': """
    Looking for additional one-time entry date options after "AND should there be an additional one-time entry date:"

    Return the text of selected options, combined with commas if multiple selected:
    'No' - if 'No' shows '☒ selected '
    'Yes, and the date is: the date specified at 35g' - if 'Yes, and the date is:' and 'the date specified at 35g' show '☒ selected '
    'Yes, and the date is: other (specify date): {date}' - if 'Yes, and the date is:' and 'other (specify date)' show '☒ selected '

    If 'Yes, and the date is:' selected, include any group limitation:
    'no' - if 'no' shows '☒ selected '
    'yes, any individuals who worked for the following company immediately before becoming an employee (of the plan sponsor): {company}' - if this option shows '☒ selected '
    'yes, other (specify group): {group}' - if this option shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Any text specified in blank spaces replaces {date}, {company}, or {group}
    The text content is: {document_content}
    """,

    'matching_contribution_entry_dates': """
    Looking for Entry Date requirements for Matching Contributions after "Entry Date - Matching Contribution."

    Return the text of selected options, combined with commas if multiple selected:
    'No entry date requirement (employee enters on the date eligibility requirements are met)' - if this option shows '☒ selected '
    'Participant must wait for first entry date:' - if this option shows '☒ selected '
    'dual entry (1st day of year and 6 months later)' - if this option shows '☒ selected '
    '1st day of the month coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    '1st day of the Plan Year coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    '1st day of the Plan Year quarter coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    'other:' - if this option shows '☒ selected ', followed by any text specified after the colon
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,


    'additional_entry_date_matching': """
    Looking for additional one-time entry date options after "AND, should there be an additional one-time entry date:"

    Return the text of selected options, combined with commas if multiple selected:
    'No (skip to 38i./j.)' - if 'No (skip to 38i./j.)' shows '☒ selected '
    'Yes, and the date is: the date specified at 35n' - if 'Yes, and the date is:' and 'the date specified at 35n' show '☒ selected '
    'Yes, and the date is: other (specify date): {date}' - if 'Yes, and the date is:' and 'other (specify date)' show '☒ selected '

    If 'Yes, and the date is:' selected, include any group limitation:
    'no' - if 'no' shows '☒ selected '
    'yes, any individuals who worked for the following company immediately before becoming an employee (of the plan sponsor): {company}' - if this option shows '☒ selected '
    'yes, other (specify group): {group}' - if this option shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Any text specified in blank spaces replaces {date}, {company}, or {group}
    The text content is: {document_content}
    """,

    'entry_date_ps_mp': """
    Looking for Entry Date requirements for Profit Sharing or Money Purchase Contribution after "Entry Date - Profit Sharing or Money Purchase Contribution"

    Return the text of selected options, combined with commas if multiple selected:
    'No entry date requirement (employee enters on the date eligibility requirements are met)' - if this option shows '☒ selected '

    'Participant must wait for first entry date:' - if 'Participant must wait for first entry date:' shows '☒ selected '
    'dual entry (1st day of year and 6 months later)' - if this option shows '☒ selected '
    '1st day of the month coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    '1st day of the Plan Year in which eligibility requirements are met' - if this option shows '☒ selected '
    '1st day of the Plan Year nearest date eligibility requirements are met' - if this option shows '☒ selected '
    '1st day of the Plan Year coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    '1st day of the Plan Year quarter coinciding with or next following date eligibility requirements are met' - if this option shows '☒ selected '
    'other: {text}' - if 'other:' shows '☒ selected '
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    '38.10 additional_one_time_entry_date_ps_mp': """
    Looking for information about additional one-time entry dates for Profit Sharing or Money Purchase Contributions after "AND, should there be an additional one-time entry date:" 

    Return the text of selected options, combined with commas if multiple selected:
    'No' - if this option shows '☒ selected '
    'Yes, and the date is:' - if this option shows '☒ selected '
    'date specified at 35u' - if this option shows '☒ selected '
    'other (specify date):' - if this option shows '☒ selected ', followed by any text specified after the colon
    'no' - if this option shows '☒ selected ' after selecting yes
    'yes, any individuals who worked for the following company immediately before becoming an employee:' - if this option shows '☒ selected ' after selecting yes, followed by any text specified after the colon
    'yes, other (specify group):' - if this option shows '☒ selected ' after selecting yes, followed by any text specified after the colon
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """


}


VESTING_TYPES_PROMPTS = {

    'vesting_schedule': """
    Looking for whether vesting schedule is same for profit sharing, matching and QACA contributions after "Vesting Schedule."
    Check which option is selected:
    Return the text of selected options, combined with commas if multiple selected:
    'N/A -- No matching, profit sharing/pension, or QACA contributions contribution types are provided under this Plan' - if this option shows '☒ selected'

    'Yes, the same vesting schedule applies for ALL contribution types, regardless of when contributions were made' - if this option shows '☒ selected'

    'No, different vesting schedules apply for matching, profit sharing and/or QACA contribution types' - if this option shows '☒ selected'

    'N/A, this is a money purchase plan' - if this option shows '☒ selected'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Selection restrictions noted in parentheses
    The text content is: {document_content}
    """,

    'amendment_to_vesting_schedule': """
    Looking for how the plan handles amendments to the vesting schedule that reduce vested percentages, after "Amendment to Vesting Schedule."
    Check which option is selected:
    Return the text of selected options, combined with commas if multiple selected:

    'Provide affected Participants who have at least 3 years of service with an opportunity to elect to be subject to either the pre-amendment or the post-amendment vesting schedule for contributions made after the change in vesting' - if this option shows '☒ selected'

    'Automatically vest each Participant's entire account balance using the greater of the pre-amendment vested percentage or the post-amendment vested percentage for the Participant's years of service at the time of determination' - if this option shows '☒ selected'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'vesting_all_contribution_types': """
    Looking which option is selected in the Vesting - All Contribution Types subject to vesting. Vesting shall be: (skip if 39b NOT selected)
    Check which option is selected:
    Return the text of selected options, combined with commas if multiple selected:

    '100% upon entering Plan' - if '100% upon entering Plan (skip to 42)' option shows '☒ selected'
    '4-year graded (25% per year)' - if '1. 4-year graded (25% per year)(may not be selected with 23a or 23c) ' option shows '☒ selected'  
    '5-year graded (20% per year)' - if '2. 5-year graded (20% per year)(may not be selected with 23a or 23c) ' option shows '☒ selected'
    '3-year cliff' - if '. 3-year cliff (may not be selected with 23a or 23c)' option shows '☒ selected'
    '6-year graded (2 years 20% then 20% per year)' - if '6-year graded (2 years 20% then 20% per year) (may not be selected with 23a or 23c)' option shows '☒ selected'
    '2-year graded (1 year 50% then 100%)' - if '2-year graded (1 year 50% then 100%)' option shows '☒ selected'
    '2-year cliff' - if '2-year cliff' option shows '☒ selected'
    'Other' - if this option shows '☒ selected'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'vesting_matching_contribution': """
    Looking for vesting schedule for Matching Contribution after "Vesting - Matching Contribution"
    Check which option is selected:
    Return the text of selected options, combined with commas if multiple selected:
    '100% upon entering Plan' - if '100% upon entering Plan' shows '☒ selected'

    If 'Subject to the following vesting schedule:' shows '☒ selected', include selected schedule:
    '4-year graded (25% per year)' - if this option shows '☒ selected'
    '5-year graded (20% per year)' - if this option shows '☒ selected'
    '3-year cliff' - if this option shows '☒ selected'
    '6-year graded (2 years 20% then 20% per year)' - if this option shows '☒ selected'

    If 'Other' shows '☒ selected':
    'Other: {year} Year(s) {percent}%, {year} Years {percent}%...' - listing all specified year/percent pairs

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option 
    - Multiple selections should be combined with commas
    - Year/percent values if Other selected
    - Selection restrictions noted in parentheses
    The text content is: {document_content}
    """,

    'pre_-EGTRRA_matching_vesting': """
    Looking for vesting schedule for pre-EGTRRA matching contributions after "if Plan has a separate vesting schedule for pre-EGTRRA matching contributions"
    Check which option is selected:

    Return the text of selected options, combined with commas if multiple selected:
    'The schedule shown above applies to all matching contributions' - if this option shows '☒ selected'

    If 'Pre-EGTRRA matching contributions are subject to the following vesting schedule:' shows '☒ selected', include selected schedule:
    '4-year graded (25% per year)' - if this option shows '☒ selected'
    '5-year graded (20% per year)' - if this option shows '☒ selected'
    '3-year cliff' - if this option shows '☒ selected'
    '6-year graded (2 years 20% then 20% per year)' - if this option shows '☒ selected'
    '5-year cliff' - if this option shows '☒ selected'
    '7-year graded (3 years 20% then 20% per year)' - if this option shows '☒ selected'

    If 'Other' shows '☒ selected':
    'Other: {year} Year(s) {percent}%, {year} Years {percent}%...' - listing all specified year/percent pairs

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Year/percent values if Other selected
    The text content is: {document_content}
    """,

    'vesting_ps_mp_contribution': """
    Looking for vesting schedule for Profit Sharing or Money Purchase Contribution after "Vesting - Profit Sharing or Money Purchase Contribution"
    Check which option is selected:
    Return the text of selected options, combined with commas if multiple selected:
    '100% upon entering Plan' - if '100% upon entering Plan' shows '☒ selected'

    If 'Subject to the following vesting schedule:' shows '☒ selected', include selected schedule:
    '4-year graded (25% per year)' - if this option shows '☒ selected'
    '5-year graded (20% per year)' - if this option shows '☒ selected'
    '3-year cliff' - if this option shows '☒ selected'
    '6-year graded (2 years 20% then 20% per year)' - if this option shows '☒ selected'

    If 'Other' shows '☒ selected':
    'Other: {year} Year(s) {percent}%, {year} Years {percent}%...' - listing all specified year/percent pairs

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Skip to e.-g. if neither Profit Sharing (22e) nor Money Purchase (22c) selected
    - Year/percent values if Other selected
    - Selection restrictions noted in parentheses
    The text content is: {document_content}
    """,

    'vesting_qaca_contributions': """
    Looking for vesting schedule for QACA contributions after "Vesting - QACA Contributions. Vesting of QACA contributions shall be:"
    Check which option is selected:
    Return the text of selected options, combined with commas if multiple selected:
    'All QACA contributions are fully vested' - if this option shows '☒ selected'

    If 'All QACA contributions have the same vesting schedule:' shows '☒ selected', include selected schedule:
    '2-year cliff' - if this option shows '☒ selected'
    '2-year graded (50% per year)' - if this option shows '☒ selected'
    '{percent}% vested after 1 year, and 100% vested after 2 years' - if this option shows '☒ selected'
    'Other: {text}' - if this option shows '☒ selected'

    If 'Not all QACA contributions have the same vesting schedule.' shows '☒ selected':
    'fully vested' - if this option shows '☒ selected'
    '2-year cliff' - if these options show '☒ selected'
    '2-year graded (50% per year)' - if these options show '☒ selected'
    '{percent}% vested after 1 year, and 100% vested after two years' - if this option shows '☒ selected'
    'Other: {text}' - if this option shows '☒ selected'

    With effective date:
    'effective date of the restatement' - if this option shows '☒ selected'
    'Other: {date}' - if this option shows '☒ selected'

    And prior vesting schedule:
    'fully vested' - if this option shows '☒ selected'
    '2-year cliff' - if these options show '☒ selected'
    '2-year graded (50% per year)' - if these options show '☒ selected'
    '{percent}% vested after 1 year, and 100% vested after two years' - if this option shows '☒ selected'
    'Other: {text}' - if this option shows '☒ selected'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Skip unless 23a or 23c and 1a selected
    - Selection restrictions noted in parentheses
    The text content is: {document_content}
    """,
    


    'forfeitures_left_to_recognize': """
    Looking for whether forfeitures remain to be recognized, after "If Restated Plan and full vesting, are there (or might there be) forfeitures left to recognize?".
    Check which option is selected:
    Return the text of selected options, combined with commas if multiple selected, including sub-options if applicable:

    'No, all forfeitures have already been reallocated or used to reduce prior contributions' - if this option shows '☒ selected'

    'Yes, there are (or may be) forfeitures arising from: matching contributions' - if option 'b' AND sub-option '1' show '☒ selected'

    'Yes, there are (or may be) forfeitures arising from: profit sharing or money purchase (or top heavy) contributions' - if option 'b' AND sub-option '2' show '☒ selected'

    'Yes, there are (or may be) forfeitures arising from: QACA contributions' - if option 'b' AND sub-option '3' show '☒ selected'

    'none' - if all options and sub-options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option and sub-option
    - Multiple selections should be combined with commas, including sub-options under "Yes"
    The text content is: {document_content}
    """,

    'top_heavy_vesting_schedule': """
    Looking for prior top-heavy vesting schedule after "Vesting, if Plan was Top-Heavy prior to PPA, the top--heavy vesting schedule was:"
    Check which option is selected:

    Return the text of selected options, combined with commas if multiple selected:
    'N/A (Top-Heavy always satisfied for all contributions)' - if this option shows '☒ selected'
    '100%' - if this option shows '☒ selected'
    '3-year cliff' - if this option shows '☒ selected'
    '6-year graded' - if this option shows '☒ selected'
    '25% per year' - if this option shows '☒ selected'
    '20% per year' - if this option shows '☒ selected'
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'vesting_service_exclusions': """
    Looking for exclusions to vesting service, after "Vesting service".
    Check which option is selected:
    Return the text of selected options, combined with commas if multiple selected, including sub-options if applicable:

    'No exclusions' - if option 'a' shows '☒ selected'

    'Yes, exclude the following service: Service prior to Effective Date of the Plan or a predecessor plan' - if option 'b' AND sub-option '1' show '☒ selected'

    'Yes, exclude the following service: Service prior to 18th birthday' - if option 'b' AND sub-option '2' show '☒ selected'

    'none' - if all options and sub-options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option and sub-option
    - Multiple selections should be combined with commas, including sub-options under "Yes"
    The text content is: {document_content}
    """,

    'vesting_waiver': """
    Looking for whether a vesting waiver applies to certain employees employed on a certain date, after "Vesting Waiver".
    Check which option is selected:
    Return the text of selected options, including sub-options if applicable:

    'No or N/A -- Vesting schedule(s) apply to all Participants' - if option 'c' shows '☒ selected'

    'Yes, 100% vesting applies for any Participant who was employed on [DATE]' - if option 'd' AND sub-option '1' show '☒ selected'. Replace [DATE] with the actual date entered in the document.

    'Yes, 100% vesting applies for any Participant who: [DESCRIPTION]' - if option 'd' AND sub-option '2' show '☒ selected'. Replace [DESCRIPTION] with the actual description provided in the document.

    'none' - if all options and sub-options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option and sub-option
    - Replace bracketed placeholders with the actual text from the document.
    The text content is: {document_content}
    """,


    'other_vesting_provisions': """
    Looking for exceptions to full vesting upon death, disability, or early retirement, after "Other vesting provisions".
    Check which options are selected:
    Return the text of selected options, combined with commas if multiple selected:

    'Do not vest upon death' - if this option shows '☒ selected'

    'Do not vest upon disability' - if this option shows '☒ selected'

    'Do not vest upon early retirement' - if this option shows '☒ selected'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'forfeitures_shall_occur': """
    Looking for when forfeitures occur, after "Forfeitures shall occur".
    Check which option is selected:
    Return the text of selected options, combined with commas if multiple selected:

    'Earlier of distribution or five 1-year breaks-in-service' - if this option shows '☒ selected'

    'Only after five 1-year breaks-in-service' - if this option shows '☒ selected'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,
}


COMPENSATION_TYPES_PROMPTS = {



    'compensation_415_post_severance': """
    Looking for 415 Compensation post-severance pay provisions after "Compensation for 415 purposes ('415 Compensation') Post-Severance Pay"
    Return only the selected items without any additional text: the selected items must be given before each option like this ☒ selected:
    Return the text of selected options, combined with commas if multiple selected:


    'Default provisions of the Relius 415 amendment apply' - if this option shows '☒ selected'
    If 'Non-Default provisions apply:' shows '☒ selected', include selected provisions:
    'Exclude post-severance leave cashouts' - if this option shows '☒ selected'
    'Exclude post-severance deferred compensation' - if this option shows '☒ selected'
    'Include post-severance disability continuation payments: For nonhighly compensated employees only' - if these options show '☒ selected'
    'Include post-severance disability continuation payments: For all Participants and the salary continuation will continue for the following fixed or determinable period: {period}' - if these options show '☒ selected'
    'Include post severance military continuation payments' - if this option shows '☒ selected'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'optional_provisions_compensation_415': """
    Looking for Optional Provisions for 415 compensation after "Optional Provisions (does not apply to just post-severance pay)"
    Return only the selected items without any additional text: the selected items must be given before each option like this ☒ selected:
    Return the text of selected options, combined with commas if multiple selected:

    'Apply the administrative delay ("first few weeks") rule when determining compensation for 415 purposes.' - if this option shows '☒ selected'
    'none' - if option shows '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'plan_compensation': """
    Looking for Plan Compensation definition after "Plan Compensation means:"
    Return only the selected items without any additional text: the selected items must be given before each option like this ☒ selected:

    'W-2 Wages subject to income tax as defined in Reg. 1.415(c)-2(d)(4)' - if this option shows '☒ selected'
    'IRC §3401(a) wages as defined in Reg. 1.415(c)-2(d)(3)' - if this option shows '☒ selected'
    'Simplified 415 Safe Harbor Compensation as defined in Reg. 1.415(c)-2(d)(2)' - if this option shows '☒ selected'
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    The text content is: {document_content}
    """,

    'compensation_determination_period': """
    Looking for Compensation determination period after "AND, Compensation will be based on the following determination period:"
    Return only the selected items without any additional text: the selected items must be given before each option like this ☒ selected:
    Return the text of selected options, combined with commas if multiple selected:

    'The Plan Year' - if this option shows '☒ selected'
    'The Fiscal Year coinciding with or ending within the Plan Year' - if this option shows '☒ selected'
    'The calendar year coinciding with or ending within the Plan Year' - if this option shows '☒ selected'
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'adjustments_compensation': """
    Looking for whether adjustments are made to compensation after "Are adjustments made to compensation?"
    Return only the selected items without any additional text: the selected items must be given before each option like this ☒ selected:
    Return the text of selected options, combined with commas if multiple selected:

    'Yes, however different adjustments apply for different contribution types' - if this option shows '☒ selected'
    'Yes and same adjustments apply for all contribution types of the Plan' - if this option shows '☒ selected'
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'compensation_adjustments_all_contribution_types': """
    Looking for compensation adjustments for all contribution types after "Compensation Adjustments - All Contribution Types"
    Return only the selected items without any additional text: the selected items must be given before each option like this ☒ selected:
    Return the text of selected options, combined with commas if multiple selected:

    'No pre-severance adjustments' - if this option shows '☒ selected'

    'Exclude elective deferrals (401(k), 125, 132(f), 402(k), SEP, 414(h) pickup and 457)' - if this option shows '☒ selected'

    'Exclude all items listed in Reg. 1.414(s)-1(c)(3)' - if this option shows '☒ selected'

    'Exclude Compensation paid during determination period while not a Participant:' - if this option shows '☒ selected'
    If selected, include sub-options:
    'pre-participation Compensation' - if this sub-option shows '☒ selected'
    'limit this provision to the plan year containing the effective date of new plan' - if this sub-option shows '☒ selected'
    'all post-severance Compensation' - if this sub-option shows '☒ selected'

    'Exclude overtime' - if this option shows '☒ selected'
    'Exclude bonuses' - if this option shows '☒ selected'
    'Exclude commissions' - if this option shows '☒ selected'
    'Exclude military continuation payments' - if this option shows '☒ selected'
    'Other: {text}' - if this option shows '☒ selected'
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'post_severance_plan_compensation': """
    Looking for Post-Severance Plan Compensation details.
    Check the selected options:
    Return the text of selected options, combined with commas if multiple selected:

    'Default provisions apply' - if this option shows '☒ selected'

    'Non-Default provisions apply' - if this option shows '☒ selected'
    If 'Non-Default provisions apply' is selected, also check sub-options:
    'Exclude post-severance regular pay (not a 414(s) safe harbor)' 
    'Exclude leave cashouts' 
    'Exclude deferred compensation' 
    'Include disability continuation payments' 
    - Specify 'For nonhighly compensated employees only' or 'For all Participants' if selected
    - Include the fixed/determinable period if 'For all Participants' is selected

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'compensation_adjustments_all_types': """
    Looking for compensation adjustments for all contribution types after "Compensation Adjustments - All Contribution Types"
    Return only the selected items without any additional text: the selected items must be given before each option like this ☒ selected:
    Return the text of selected options, combined with commas if multiple selected:

    'No pre-severance adjustments' - if this option shows '☒ selected'

    'Exclude elective deferrals (401(k), 125, 132(f), 402(k), SEP, 414(h) pickup and 457)' - if this option shows '☒ selected'

    'Exclude all items listed in Reg. 1.414(s)-1(c)(3)' - if this option shows '☒ selected'

    'Exclude Compensation paid during determination period while not a Participant:' - if this option shows '☒ selected'
    If selected, include sub-options:
    'pre-participation Compensation' - if this sub-option shows '☒ selected'
    'limit this provision to the plan year containing the effective date of new plan' - if this sub-option shows '☒ selected'
    'all post-severance Compensation' - if this sub-option shows '☒ selected'

    'Exclude overtime' - if this option shows '☒ selected'
    'Exclude bonuses' - if this option shows '☒ selected'
    'Exclude commissions' - if this option shows '☒ selected'
    'Exclude military continuation payments' - if this option shows '☒ selected'
    'Other: {text}' - if this option shows '☒ selected'
    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    The text content is: {document_content}
    """,

    'post_severance_plan_compensation': """
    Looking for Post-Severance Plan Compensation provisions after "Post-Severance Plan Compensation:"
    Return only the selected items without any additional text: the selected items must be given before each option like this ☒ selected:
    Return the text of selected options, combined with commas if multiple selected:

    'Default provisions apply' - if this option shows '☒ selected'

    If 'Non-Default provisions apply:' shows '☒ selected', include selected provisions:
    'Exclude post-severance regular pay' - if this option shows '☒ selected'
    'Exclude leave cashouts' - if this option shows '☒ selected'
    'Exclude deferred compensation' - if this option shows '☒ selected'

    'Include disability continuation payments: For nonhighly compensated employees only' - if these options show '☒ selected'
    'Include disability continuation payments: For all Participants and the salary continuation will continue for the following fixed or determinable period: {period}' - if these options show '☒ selected'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Skip to e./f. if 50b2b selected
    The text content is: {document_content}
    """,

   'compensation_adjustments_safe_harbor': """
    Looking for compensation adjustments for 401(k) Safe Harbor Matching and Nonelective Contributions after "Compensation Adjustments - 401(k) Safe Harbor Matching and Nonelective Contributions"
    Return only the selected items without any additional text: the selected items must be given before each option like this ☒ selected:
    Return the text of selected options, combined with commas if multiple selected:

    'No adjustments' - if this option shows '☒ selected'

    If 'Yes, the following adjustments are made:' shows '☒ selected', include selected adjustments:
    'Exclude Salary Deferrals (401(k), 125, 132(f), 402(k), SEP, 414(h) pickup and 457)' - if this option shows '☒ selected'
    'Exclude all items listed in Reg. 1.414(s)-1(c)(3)' - if this option shows '☒ selected'

    If 'Exclude Compensation paid during determination period while not a Participant' shows '☒ selected', include sub-options:
    'pre-participation Compensation for both safe harbor nonelective contributions and safe harbor matching contributions' - if this option shows '☒ selected'
    'exclude only for safe harbor matching contributions' - if this option shows '☒ selected'
    'all post-severance Compensation' - if this option shows '☒ selected'

    'Exclude overtime' - if this option shows '☒ selected'
    'Exclude bonuses' - if this option shows '☒ selected'
    'Exclude commissions' - if this option shows '☒ selected'
    'Exclude post-HEART military continuation payments' - if this option shows '☒ selected'
    'Other: {text}' - if this option shows '☒ selected'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Skip to m.-n. if safe harbor contributions not selected
    The text content is: {document_content}
    """,
    'compensation_adjustments_profit_sharing': """
    Looking for compensation adjustments for Profit Sharing/Money Purchase Contributions after "Compensation Adjustments - Profit Sharing (or Money Purchase) Contributions"
    Return only the selected items without any additional text: the selected items must be given before each option like this ☒ selected:
    Return the text of selected options, combined with commas if multiple selected:

    'No adjustments' - if this option shows '☒ selected'

    If 'Yes, the following adjustments are made:' shows '☒ selected', include selected adjustments:
    'Exclude Salary Deferrals (401(k), 125, 132(f), 402(k), SEP, 414(h) pickup and 457)' - if this option shows '☒ selected'
    'Exclude all items listed in Reg. 1.414(s)-1(c)(3)' - if this option shows '☒ selected'

    If 'Exclude Compensation paid during determination period while not a Participant:' shows '☒ selected', include sub-options:
    'pre-participation Compensation' - if this option shows '☒ selected'
    'limit this provision to the plan year containing the effective date of new plan' - if this option shows '☒ selected'
    'all post-severance Compensation' - if this option shows '☒ selected'

    'Exclude overtime' - if this option shows '☒ selected'
    'Exclude bonuses' - if this option shows '☒ selected'
    'Exclude commissions' - if this option shows '☒ selected'
    'Exclude military continuation payments' - if this option shows '☒ selected'
    'Other: {text}' - if this option shows '☒ selected'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Skip unless profit sharing contributions (22e1) or prevailing wage contributions (22f1) selected 
    The text content is: {document_content}
    """,

    'compensation_adjustments_matching': """
    Looking for compensation adjustments for Matching Contributions (other than ADP Safe Harbor) after "Compensation Adjustments - Matching Contributions other than ADP Safe Harbor Matching Contributions"
    Return only the selected items without any additional text: the selected items must be given before each option like this ☒ selected:
    Return the text of selected options, combined with commas if multiple selected:

    'No adjustments' - if this option shows '☒ selected'

    If 'Yes, the following adjustments are made:' shows '☒ selected', include selected adjustments:
    'Exclude Salary Deferrals (401(k), 125, 132(f), 402(k), SEP, 414(h) pickup and 457)' - if this option shows '☒ selected'
    'Exclude all items listed in Reg. 1.414(s)-1(c)(3)' - if this option shows '☒ selected'

    If 'Exclude Compensation paid during determination period while not a Participant:' shows '☒ selected', include sub-options:
    'pre-participation Compensation' - if this option shows '☒ selected'
    'limit this provision to the plan year containing the effective date of new plan' - if this option shows '☒ selected'
    'all post-severance Compensation' - if this option shows '☒ selected'

    'Exclude overtime' - if this option shows '☒ selected'
    'Exclude bonuses' - if this option shows '☒ selected'
    'Exclude commissions' - if this option shows '☒ selected'
    'Exclude military continuation payments' - if this option shows '☒ selected'
    'Other: {text}' - if this option shows '☒ selected'

    'none' - if all options show '☐ unselected'

    Check for:
    - '☒ selected' or '☐ unselected' before each option
    - Multiple selections should be combined with commas
    - Skip to m./n. if matching contributions (22d1) NOT selected
    The text content is: {document_content}
    """



  

    # '415_compensation_default': """
    # Look for 415 Compensation post-severance pay provisions.
    # Return only one of the following without any additional text:
    # 'Default provisions apply'
    # 'Non-default provisions'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # '415_compensation_exclusions': """
    # Look for 415 compensation non-default exclusions.
    # Return only the selected items without any additional text:
    # 'Leave cashouts excluded'
    # 'Deferred compensation excluded'
    # 'Both excluded'
    # 'No exclusions'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # '415_disability_payments': """
    # Look for 415 disability continuation payments.
    # Return only one of the following without any additional text:
    # 'For non-HCEs only'
    # 'For all participants'
    # 'Not included'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # '415_military_payments': """
    # Look for 415 military continuation payments.
    # Return only one of the following without any additional text:
    # 'Included'
    # 'Not included'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'plan_compensation_definition': """
    # Look for Plan Compensation definition.
    # Return only one of the following without any additional text:
    # 'W-2 Wages'
    # 'IRC §3401(a) wages'
    # 'Simplified 415 Safe Harbor'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'compensation_period': """
    # Look for compensation determination period.
    # Return only one of the following without any additional text:
    # 'Plan Year'
    # 'Fiscal Year'
    # 'Calendar Year'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'adjustment_type': """
    # Look for compensation adjustment application.
    # Return only one of the following without any additional text:
    # 'Different by contribution type'
    # 'Same for all types'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'pre_severance_status': """
    # Look for pre-severance adjustments status.
    # Return only one of the following without any additional text:
    # 'No pre-severance adjustments'
    # 'Has adjustments'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'deferrals_excluded': """
    # Look for elective deferrals exclusion status.
    # Return only one of the following without any additional text:
    # 'Excluded'
    # 'Not excluded'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'regulatory_items_excluded': """
    # Look for Reg. 1.414(s)-1(c)(3) items exclusion.
    # Return only one of the following without any additional text:
    # 'Excluded'
    # 'Not excluded'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'non_participant_compensation': """
    # Look for compensation paid while not a participant.
    # Return only one of the following without any additional text:
    # 'Excluded'
    # 'Not excluded'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'post_severance_status': """
    # Look for post-severance compensation status.
    # Return only one of the following without any additional text:
    # 'Excluded'
    # 'Not excluded'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'overtime_status': """
    # Look for overtime compensation status.
    # Return only one of the following without any additional text:
    # 'Excluded'
    # 'Not excluded'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'bonus_status': """
    # Look for bonus compensation status.
    # Return only one of the following without any additional text:
    # 'Excluded'
    # 'Not excluded'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'commission_status': """
    # Look for commission compensation status.
    # Return only one of the following without any additional text:
    # 'Excluded'
    # 'Not excluded'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'elective_deferrals_treatment': """
    # Look for elective deferrals compensation treatment.
    # Return only one of the following without any additional text:
    # 'No adjustments'
    # 'Has specific adjustments'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'elective_deferrals_specific_exclusions': """
    # Look for specific elective deferrals exclusions.
    # Return only selected items without additional text:
    # 'Reg. 1.414(s)-1(c)(3) items'
    # 'Pre/post participation'
    # 'Overtime/bonuses/commissions'
    # 'Military continuation'
    # 'No exclusions'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'safe_harbor_treatment': """
    # Look for safe harbor contributions treatment.
    # Return only one of the following without any additional text:
    # 'No adjustments'
    # 'Has specific adjustments'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'safe_harbor_specific_exclusions': """
    # Look for specific safe harbor exclusions.
    # Return only selected items without additional text:
    # 'Salary deferrals'
    # 'Reg items'
    # 'Pre/post participation'
    # 'Overtime/bonuses/commissions'
    # 'No exclusions'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'matching_contribution_treatment': """
    # Look for matching contributions treatment.
    # Return only one of the following without any additional text:
    # 'No adjustments'
    # 'Has specific adjustments'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'matching_specific_exclusions': """
    # Look for specific matching contribution exclusions.
    # Return only selected items without additional text:
    # 'Salary deferrals'
    # 'Reg items'
    # 'Pre/post participation'
    # 'Overtime/bonuses/commissions'
    # 'No exclusions'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'profit_sharing_treatment': """
    # Look for profit sharing treatment.
    # Return only one of the following without any additional text:
    # 'No adjustments'
    # 'Has specific adjustments'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'profit_sharing_specific_exclusions': """
    # Look for specific profit sharing exclusions.
    # Return only selected items without additional text:
    # 'Salary deferrals'
    # 'Reg items'
    # 'Pre/post participation'
    # 'Overtime/bonuses/commissions'
    # 'No exclusions'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'post_severance_provisions': """
    # Look for post-severance provisions type.
    # Return only one of the following without any additional text:
    # 'Default provisions'
    # 'Non-default provisions'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'regular_pay_treatment': """
    # Look for post-severance regular pay treatment.
    # Return only one of the following without any additional text:
    # 'Excluded'
    # 'Not excluded'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'leave_cashout_treatment': """
    # Look for leave cashout treatment.
    # Return only one of the following without any additional text:
    # 'Excluded'
    # 'Not excluded'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'deferred_comp_treatment': """
    # Look for post-severance deferred compensation treatment.
    # Return only one of the following without any additional text:
    # 'Excluded'
    # 'Not excluded'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'military_continuation_treatment': """
    # Look for military continuation pay treatment.
    # Return only one of the following without any additional text:
    # 'Default date applies'
    # 'Alternative date specified'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # '415_effective_date': """
    # Look for 415 regulations effective date.
    # Return only one of the following without any additional text:
    # 'Default date applies'
    # 'Alternative date specified'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'heart_effective_date': """
    # Look for HEART provisions effective date.
    # Return only one of the following without any additional text:
    # 'January 1, 2009'
    # 'Alternative date specified'
    # 'NA'
    # The text content is: {document_content}
    # """,

    # 'disability_continuation': """
    # Look for disability continuation payments policy.
    # Return only one of the following without any additional text:
    # 'Non-HCEs only'
    # 'All participants'
    # 'Not specified'
    # 'NA'
    # The text content is: {document_content}
    # """
}


CONTRIBUTION_ALLOCATION_TYPES_PROMPTS = {

    'salary_reduction_limit': """
    Look for Employee Salary Reduction Election limit.
    Return only one of the following without any additional text:
    'Up to specified percentage'
    'Percentage range specified'
    'Up to maximum allowed'
    'NA'
    'Unselected'
    The text content is: {document_content}
    """,

    'additional_deferral_date': """
    Look for Special Effective Date for elective deferrals.
    Return only one of the following without any additional text:
    'Date specified'
    'Not specified'
    'NA'
    'Unselected'
    The text content is: {document_content}
    """,

    'bonus_election': """
    Look for Separate Bonus Election.
    Return only one of the following without any additional text:
    'Percentage specified'
    'Not allowed'
    'NA'
    'Unselected'
    The text content is: {document_content}
    """,

    'hce_limit': """
    Look for Separate HCE Limit.
    Return only one of the following without any additional text:
    'Percentage limit'
    'Other limit'
    'No limit'
    'NA'
    'Unselected'
    The text content is: {document_content}
    """,

    'election_modification_frequency': """
    Look for frequency of Salary Reduction Election modifications.
    Return only one of the following without any additional text:
    'Annually'
    'Semi-annually'
    'Quarterly'
    'Monthly'
    'Any pay period'
    'Other specified'
    'NA'
    'Unselected'
    The text content is: {document_content}
    """,

    'catchup_contributions': """
   Look for whether Plan permits catch-up contributions.
   Return only one of the following without any additional text:
   'Yes'
   'No'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'catchup_aggregation': """
   Look for catch-up contributions aggregation with other Elective Deferrals.
   Return only one of the following without any additional text:
   'No aggregation'
   'Yes aggregated'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'aca_deferral_type': """
   Look for type of automatic elective deferral in ACA.
   Return only one of the following without any additional text:
   'Pre-tax'
   'Roth'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'aca_election_requirement': """
   Look for ACA new election requirement.
   Return only one of the following without any additional text:
   'New election required'
   'No new election required'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'aca_participant_scope': """
   Look for which participants ACA applies to.
   Return only one of the following without any additional text:
   'No affirmative election'
   'No minimum election'
   'New participants only'
   'New hires only'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'aca_deferral_amount': """
   Look for initial ACA deferral amount.
   Return only one of the following without any additional text:
   'Percentage specified'
   'Dollar amount specified'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'aca_escalation': """
   Look for ACA escalation provisions.
   Return only one of the following without any additional text:
   'No escalation'
   'Percentage escalation'
   'Dollar escalation'
   'Custom schedule'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'aca_escalation_timing': """
   Look for timing of ACA escalation.
   Return only one of the following without any additional text:
   'Hire anniversary'
   'Entry anniversary'
   'Plan Year start'
   'Calendar Year start'
   'Other timing'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,
   'qaca_deferral_type': """
   Look for type of QACA automatic deferral.
   Return only one of the following without any additional text:
   'Pre-tax'
   'Roth'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'qaca_election_requirement': """
   Look for QACA new election requirement.
   Return only one of the following without any additional text:
   'New election required'
   'No new election required'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'qaca_participant_scope': """
   Look for scope of QACA automatic deferrals.
   Return only one of the following without any additional text:
   'Minimum election not made'
   'No affirmative election'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'qaca_deferral_amount': """
   Look for QACA automatic deferral amount type.
   Return only one of the following without any additional text:
   'Constant percentage'
   'Initial with escalation'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'qaca_escalation_schedule': """
   Look for QACA escalation schedule.
   Return only one of the following without any additional text:
   'One percentage point'
   'Custom percentage points'
   'Standard schedule'
   'Custom schedule'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'qaca_eaca_status': """
   Look for whether QACA includes EACA provisions.
   Return only one of the following without any additional text:
   'No EACA'
   'Includes EACA'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'qaca_withdrawal_rights': """
   Look for QACA withdrawal provisions.
   Return only one of the following without any additional text:
   'No withdrawals'
   '90-day withdrawal'
   'Custom period withdrawal'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'eaca_deferral_type': """
   Look for EACA automatic deferral type.
   Return only one of the following without any additional text:
   'Pre-tax'
   'Roth'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'eaca_election_requirement': """
   Look for EACA new election requirement.
   Return only one of the following without any additional text:
   'New election required'
   'No new election required'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'eaca_participant_scope': """
   Look for EACA automatic deferral scope.
   Return only one of the following without any additional text:
   'Minimum election not made'
   'No affirmative election'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'eaca_deferral_amount': """
   Look for EACA automatic deferral amount.
   Return only one of the following without any additional text:
   'Fixed percentage'
   'Percentage with escalation'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'eaca_affirmative_election': """
   Look for EACA affirmative election requirements.
   Return only one of the following without any additional text:
   'Annual notice required'
   'No annual notice required'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'eaca_withdrawal_rights': """
   Look for EACA withdrawal provisions.
   Return only one of the following without any additional text:
   'No withdrawals'
   '90-day withdrawal'
   'Custom period withdrawal'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'eaca_escalation_timing': """
   Look for timing of EACA escalation.
   Return only one of the following without any additional text:
   'Hire anniversary'
   'Entry anniversary'
   'Plan Year start'
   'Calendar Year start'
   'Custom timing'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'eaca_eligibility': """
   Look for EACA eligibility scope.
   Return only one of the following without any additional text:
   'All participants'
   'Limited participants'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'eaca_coverage_status': """
   Look for EACA coverage for participants with affirmative elections.
   Return only one of the following without any additional text:
   'Remain covered'
   'Not covered'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'affirmative_escalation': """
   Look for escalation of affirmative elections.
   Return only one of the following without any additional text:
   'No escalation'
   'Voluntary only'
   'Automatic for all'
   'Automatic with conditions'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'escalation_exclusions': """
   Look for exclusions from automatic escalation.
   Return only one of the following without any additional text:
   'No exclusions'
   'Prior elections excluded'
   'Other exclusions'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'annual_increase_rate': """
   Look for annual increase percentage.
   Return only one of the following without any additional text:
   '1%'
   'Other percentage'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """,

   'escalation_maximum': """
    Look for maximum escalation limit.
    Return only one of the following without any additional text:
    '100%'
    '10%'
    'Other maximum'
    'NA'
    'Unselected'
    The text content is: {document_content}
    """,

   'escalation_date': """
   Look for when escalation occurs.
   Return only one of the following without any additional text:
   'Plan Year start'
   'Election anniversary'
   'Other timing'
   'NA'
   The text content is: {document_content}
   """,

   'first_escalation': """
   Look for timing of first escalation.
   Return only one of the following without any additional text:
   'Second escalation date'
   'First escalation date'
   'NA'
   'Unselected'
   The text content is: {document_content}
   """

}

SAFE_HARBOR_PROMPTS = {
    'safe_harbor_effective_date': """
    Look for special effective date for 401(k) Safe Harbor Contributions.
    Return only one of the following without any additional text:
    'No special date'
    'Yes - [specified date]'
    'NA'
    The text content is: {document_content}
    """,

    'current_safe_harbor_selection': """
    Look for which ADP safe harbor contribution option is currently selected.
    Return only one of the following values without any additional text:
    'no_formula' - if "No formula currently effective" is selected
    'traditional_basic_matching' - if "traditional Basic Matching Formula" is selected
    'traditional_enhanced_matching' - if "traditional Enhanced Matching Formula" is selected
    'traditional_nonelective' - if "traditional Nonelective Formula" is selected
    'traditional_reserved_nonelective' - if "reserve the right to amend the Plan... traditional Nonelective" is selected
    'qaca_basic_matching' - if "QACA Basic Matching Formula" is selected
    'qaca_enhanced_matching' - if "QACA Enhanced Matching Formula" is selected
    'qaca_nonelective' - if "QACA Nonelective Formula" is selected
    'qaca_reserved_nonelective' - if "reserve the right to amend the Plan... QACA Nonelective" is selected
    'none' - if no option is selected
    The text content is: {document_content}
    """,

    'safe_harbor_duration': """
    Look for how long the ADP safe harbor contribution remains in effect.
    Return only one of the following values without any additional text:
    'until_amended' - if formula stays in effect until an amendment is adopted
    'until_plan_year_end' - if formula stays in effect until the end of current plan year
    'none' - if no option is selected
    The text content is: {document_content}
    """,

    'safe_harbor_exclusions': """
    Look for which options are selected regarding 401(k) Safe Harbor Contribution exclusions.
    Return only one of the following values without any additional text:
    'additional_exclusions_custom_service' - if option b is selected with b3 (service requirement: 500 hours within 6 months) and b6 (standard entry dates)
    'no_additional_exclusions' - if option a is selected
    'other' - for any other combination
    
    The text content is: {document_content}
    """

}


MATCHING_CONTRIBUTION_PROMPTS = {

'employer_matching_contribution': """
Look for which type of Employer Matching Contribution (other than 401(k) Safe Harbor Matching Contributions) is selected.
Return only one of the following values without any additional text:
'discretionary_flexible' - if option a.1 is selected (flexible discretionary match)
'discretionary_rigid_no_notice' - if option a.2 is selected (rigid match without notice)
'discretionary_rigid_with_notice' - if option a.3 is selected (rigid match with potential notice)
'fixed_plus_none' - if option b is selected with b.1 (fixed percentage plus no additional)
'fixed_plus_flexible' - if option b is selected with b.2.a (fixed percentage plus flexible discretionary)
'fixed_plus_rigid_no_notice' - if option b is selected with b.2.b (fixed percentage plus rigid without notice)
'fixed_plus_rigid_with_notice' - if option b is selected with b.2.c (fixed percentage plus rigid with notice)
'discretionary_tiered' - if option c is selected (discretionary percentage of tiers)
'fixed_tiered' - if option d is selected (fixed percentage of tiers)
'service_based' - if option e is selected (based on years of service)
'none' - if no option is selected
The text content is: {document_content},
""",

'elective_deferrals_match_limit': """
Look for how elective deferrals are taken into account for matching contributions.
Return only one of the following values without any additional text:
'all_deferrals' - if option a is selected (all deferrals will be matched)
'percentage_limit' - if option b is selected (deferrals up to specified percentage)
'dollar_limit' - if option c is selected (deferrals up to specified dollar amount)
'discretionary_limit' - if option d is selected (discretionary percentage or dollar amount)
'none' - if no option is selected
The text content is: {document_content}
""",

'catch_up_contributions_matching': """
Look for whether catch-up elective deferral contributions are taken into account in applying matching contributions.
Return only one of the following values without any additional text:
'no' - if option e is selected (catch-up contributions not taken into account)
'yes' - if option f is selected (catch-up contributions taken into account)
'none' - if no option is selected
The text content is: {document_content}
""",

'matching_contribution_limit': """
Look for the overall limit on matching contributions for any Participant for any Plan Year.
Return only one of the following values without any additional text:
'no_limit' - if option a is selected (no additional limit)
'dollar_limit' - if option b is selected (dollar amount limit)
'percentage_limit' - if option c is selected (percentage of compensation limit)
'none' - if no option is selected
The text content is: {document_content}
""",

'matching_computation_period': """
Look for which period is used to determine fixed matching contributions.
Return only one of the following values without any additional text:
'annual' - if option a is selected (entire year with potential true-up)
'payroll_period' - if option b is selected (each payroll period, no true-up)
'monthly' - if option c is selected (monthly periods with potential true-up)
'quarterly' - if option d is selected (quarterly periods with potential true-up)
'discretionary' - if option e is selected (discretionary calculation methodology)
'none' - if no option is selected
The text content is: {document_content}
""",

'qmac_status': """
Look for whether matching contributions will be Qualified Matching Contributions.
Return only one of the following values without any additional text:
'no' - if option a is selected (not QMACs)
'yes' - if option b is selected (all matching contributions are QMACs)
'none' - if no option is selected
The text content is: {document_content}
""",

'matching_contribution_eligibility': """
Look for which participants are eligible to receive matching contributions.
Return only one of the following values without any additional text:
'year_of_service' - if option a is selected (complete Year of Service)
'service_and_last_day' - if option b is selected (Year of Service and last day active)
'last_day' - if option c is selected (employed on last day)
'last_day_or_500_hours' - if option d is selected (last day active or 500+ Hours of Service)
'any_time_employed' - if option e is selected (employed at any time)
'custom' - if option f is selected (other custom criteria)
'none' - if no option is selected
The text content is: {document_content}
""",

'ratio_percentage_failsafe': """
Look for whether IRC §410(b)(1)(B) ratio percentage fail-safe provisions are included.
Return only one of the following values without any additional text:
'no' - if option g is selected (no fail-safe provisions)
'yes' - if option h is selected (includes fail-safe provisions)
'none' - if no option is selected
The text content is: {document_content}
""",


'matching_contribution_waivers': """
Look for which events allow participants to receive matching contributions despite not being employed at year end.
Return a list containing any of the following values that are selected, or 'none' if no options are selected:
'death' - if option a is selected
'disability' - if option b is selected
'retirement' - if option c is selected
Return the list without any additional text.
Example return values:
[] - if none selected
['death'] - if only death selected
['death', 'disability'] - if both death and disability selected
['death', 'disability', 'retirement'] - if all options selected
The text content is: {document_content}
""",

'forfeiture_allocation_group': """
Look for which group receives the reallocation of forfeitures when "Reallocated comp to comp" is selected.
Return only one of the following values without any additional text:
'all_participants' - if option c.1 is selected
'nhce_only' - if option c.2 is selected
'none' - if neither is selected or if option c is not selected
The text content is: {document_content}
""",

}


NON_ELECTIVE_PROMPTS = {

'profit_sharing_contribution_type': """
Look for which type of Employer Profit Sharing Contribution is selected.
Return only one of the following values without any additional text:
'discretionary_no_profit_limit' - if option a is selected (Discretionary, but not limited to profits)
'discretionary_from_profits' - if option b is selected (Discretionary, out of profits)
'fixed_percentage' - if option c is selected (Fixed contribution equal to specified percentage)
'none' - if no option is selected
The text content is: {document_content}
""",

'profit_sharing_allocation_method': """
Look for which allocation method is selected for profit sharing contributions.
Return only one of the following values without any additional text:
'integrated_safe_harbor' - if option d is selected (Integrated design-based safe harbor)
'non_integrated_safe_harbor' - if option e is selected (Non-integrated design-based safe harbor)
'general_nondiscrimination' - if option f is selected (General Nondiscrimination Testing/Cross-Testing)
'none' - if no option is selected
The text content is: {document_content}
""",


'money_purchase_contribution': """
Look for which Money Purchase contribution method is selected.
Return only one of the following values without any additional text:
'integrated design-based safe harbor' - if only option g is selected (Integrated safe harbor)
'integrated_contribution formula' - if options g and g.1 are selected (Integrated with contribution formula)
'integrated_allocation formula' - if options g and g.2 are selected (Integrated with allocation formula)
'Non-integrated design-based safe harbor' - if option h is selected (Non-integrated safe harbor)
'General Nondiscrimination Testing/Cross Testing' - if option i is selected (General Nondiscrimination Testing)
'none' - if no option is selected
The text content is: {document_content}
""",

'contribution_formula_selection': """
Look for which Money Purchase contribution formula option is selected.
Return 'none' if no option is selected.
The text content is: {document_content}
""",

'Integrated Allocation/nonintegrated_allocation': """
Look for how nonintegrated allocation or Integrated Allocation and permitted disparity are applied.
Return only one of the following values without any additional text:
'no' - if only option a is selected
'yes_3%' - if option b and 1 are selected (Yes with 3% non-integrated percentage)
'yes_4%' - if option b and 2 are selected (Yes with 4% non-integrated percentage)
'yes_5%' - if option b and 3 are selected (Yes with 5% non-integrated percentage)
'yes_7.5%' - if option b and 4 are selected (Yes with 7.5% non-integrated percentage)   
'none' - if no option is selected
The text content is: {document_content}
""",

'integrated_allocation_option': """
Look for which Integrated Allocation option is selected by checking the circular selection indicators (○/●).
Return only one of the following values without any additional text:
'5.7_percent_and_twb' - if "5.7% and TWB" is selected
'5.7_percent_and_20_percent_twb' - if "5.7% and 20% of TWB" is selected 
'5.7_percent_and_{amount}_dollars' - if "5.7% and $____" is selected (replace {amount} with actual amount)
'5.4_percent_and_80_percent_twb_plus_1_dollar' - if "5.4% and 80% of TWB plus $1.00" is selected
'5.4_percent_and_{percent}_percent_twb' - if "5.4% and ___% of TWB" is selected (replace {percent} with actual percentage)
'5.4_percent_and_80_percent_twb_plus_{amount}_dollars' - if "5.4% and 80% of wage base plus $____" is selected (replace {amount} with actual amount)
'4.3_percent_and_{amount}_dollars' - if "4.3% and $____" is selected (replace {amount} with actual amount)
'4.3_percent_and_{percent}_percent_twb' - if "4.3% and ___%" is selected (replace {percent} with actual percentage)
'none' - if no option is selected
The text content is: {document_content}
""",

'non_integrated_allocation_option': """
Look for which Non-Integrated Allocation option is selected and any specified point values.
Return only one of the following values without any additional text:
'compensation_to_total_compensation_ratio' - if "Compensation to total of all Compensation" is selected
'equal_dollar_all_participants' - if "In the same dollar amount to all Participants (per capita)" is selected
'equal_dollar_per_service_hour' - if "In the same dollar amount per Hour of Service completed by each Participant" is selected
'point_system_service_{points}_per_year_no_limit' - if Point System selected with points for Year of Service and No limitation (replace {points} with actual number)
'point_system_service_{points}_per_year_limit_{years}' - if Point System selected with points and year limit (replace {points} and {years} with actual numbers)
'point_system_service_{points}_vesting' - if Point System selected with points for vesting service (replace {points} with actual number)
'point_system_service_{points}_eligibility' - if Point System selected with points for eligibility service (replace {points} with actual number)
'point_system_{points}_per_{amount}_compensation' - if Point System selected with points per compensation amount (replace {points} and {amount} with actual numbers)
'point_system_{points}_per_age_year' - if Point System selected with points for each year of age (replace {points} with actual number)
'none' - if no option is selected
The text content is: {document_content}
""",

'general_nondiscrimination_allocation': """
Look for which General Nondiscrimination/Cross-Testing option is selected and any specified values.
Return only one of the following values without any additional text:
'new_comparability_separate_groups' - if option for separate groups for each Participant is selected

'new_comparability_classifications_prorata' - if classifications with pro-rata allocation is selected
'new_comparability_classifications_equal' - if classifications with equal dollar amounts is selected
'new_comparability_classifications_mixed_{prorata_groups}_{equal_groups}' - if classifications with mixed methods (replace {prorata_groups} and {equal_groups} with specified groups)

'new_comparability_monthly_shift' - if classification shift handled by months
'new_comparability_daily_shift' - if classification shift handled by days
'new_comparability_single_class_shift' - if classification shift uses single classification

'super_integrated_{base_percent}_plus_{additional_percent}_above_{amount}' - if super integrated with base percentage and additional percentage above amount (replace with actual values)
'super_integrated_{base_percent}_plus_excess_above_{amount}' - if super integrated with base percentage and excess above amount (replace with actual values)

'age_weighted_7.5_percent' - if age weighted with 7.5% interest
'age_weighted_8.0_percent' - if age weighted with 8.0% interest
'age_weighted_8.5_percent' - if age weighted with 8.5% interest
'age_weighted_8.5_percent_with_safe_harbor' - if age weighted with 8.5% interest and including safe harbor

'none' - if no option is selected

The text content is: {document_content}
""",

'gateway_contribution_recognition': """
Look for when 415 Compensation is recognized for determining Gateway Contribution.
Return only one of the following values without any additional text:
'first_day_plan_year' - if "First day of the Plan Year" is selected
'participant_entry_date' - if "Date Participant entered the Plan" is selected
'none' - if no option is selected
The text content is: {document_content}
""",

'profit_sharing_allocation_eligibility': """
Look for the selected option for when Participants shall share in Profit Sharing contributions based on whether the circular indicator is marked as selected or unselected.
Return only one of the following values without any additional text:
'If completed a Year of Service' - if option a is marked as selected
'If completed a Year of Service and actively employed on last day of Plan Year' - if option b is marked as selected
'If actively employed on last day of Plan Year' - if option c is marked as selected
'If actively employed on last day of Plan Year or have completed more than 500 Hours of Service' - if option d is marked as selected
'If employed at any time during the Plan Year' - if option e is marked as selected
'If {custom_condition}' - if option f is marked as selected (replace {custom_condition} with specified text)
'none' - if all options are marked as unselected
Check the word 'selected' or 'unselected' after each circular indicator (○) to determine which option is chosen.
The text content is: {document_content}
""",

'ratio_percentage_fail_safe_provision': """
Look for whether IRC §410(b)(1)(B) ratio percentage fail-safe provisions are included based on whether the circular indicator (○) is marked as selected or unselected.
Return only one of the following values without any additional text:
'No'- if 'No' option is marked as selected
'Yes' - if 'Yes' option is marked as selected
'none' - if all options are marked as unselected
Check the word 'selected' or 'unselected'.
The text content is: {document_content}
""",

'waiver_of_allocation_conditions': """
Look for which conditions are waived for allocations by checking for "selected☒" or "unselected☐" after each option.
Return one of the following values without any additional text:
'Death' - if only Death shows "selected☒"
'Disability' - if only Disability shows "selected☒"
'Early or Normal Retirement' - if only Early or Normal Retirement shows "selected☒"
'Death, Disability' - if both Death and Disability show "selected☒"
'Death, Early or Normal Retirement' - if both Death and Early or Normal Retirement show "selected☒"  
'Disability, Early or Normal Retirement' - if both Disability and Early or Normal Retirement show "selected☒"
'Death, Disability, Early or Normal Retirement' - if all three options show "selected☒"
'none' - if all options show "unselected☐"
Check for "selected☒" to determine selected options and "unselected☐" for unselected options.
The text content is: {document_content}
""",

'Discretionary Qualified Nonelective Contribution': """
Look for how Discretionary Qualified Nonelective Contributions are handled by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'No additional discretionary QNEC' - if 'No' option is marked as selected
'Yes with determinable formula' - if 'Yes, pursuant to a definitely determinable formula' is marked as selected
'Yes with operational flexibility' - if 'Yes, but such contributions should be operationally flexible' is marked as selected
'none' - if all options show unselected
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'Discretionary QNEC': """
Look for whether the Discretionary QNEC should be contributed for all participants or only NHCEs by checking if 'all participants' or 'only NHCEs' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'all participants' - if 'all participants' option shows 'selected'
'only NHCEs' - if 'only NHCEs' option shows 'selected'
'none' - if both options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'Discretionary contribution be based on':"""
Look for which compensation basis is used for contributions by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'Compensation for deferral purposes' - if the deferral compensation option is marked as selected
'415 Compensation' - if the 415 Compensation option is marked as selected  
'414(s) Compensation' - if the 414(s) Compensation option is marked as selected
'none' - if all options show unselected
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
"""
}

PREVAILING_WAGE_PROMPTS = {

'prevailing_wage_distribution_restrictions': """
Look for whether Prevailing Wage Contributions are subject to distribution restrictions by checking if 'No' or 'Yes' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'No' - if 'No' is marked as selected
'Yes' - if 'Yes' is marked as selected  
'none' - if both options show unselected
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'Highly Compensated Employees_prevailing_wage_exclusion': """
Look for whether Highly Compensated Employees are excluded from Prevailing Wage Contributions by checking if 'No' or 'Yes' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'No' - if 'No' is marked as selected
'Yes' - if 'Yes' is marked as selected
'none' - if both options show unselected
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'prevailing_wage_profit_sharing': """
Look for whether profit sharing contributions are reduced by Prevailing Wage Contributions by checking if options are marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'No' - if 'No, the Prevailing Wage Contribution will be added' is marked as selected
'Yes' - if 'Yes' is marked as selected
'none' - if both options show unselected
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'employer_nonelective_contributions_offset': """ 
Look for whether employer nonelective contributions are reduced by Prevailing Wage Contributions by checking if options are marked as 'selected' or 'unselected'. Return only one of the following values without any additional text: 
'No' - if 'No, the Prevailing Wage Contribution will be added' is marked as selected 
'Yes' - if 'Yes' is marked as selected 
'none' - if both options show unselected Check for the word 'selected' or 'unselected' after each option to determine which is chosen. 
The text content is: {document_content}
""",

}

GENERAL_PLAN_PROMPTS = {

'trust_earnings_allocation_method': """
Look for how Trust earnings are allocated by checking if options are marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'Beginning balance' - if option 'Beginning balance' is marked as selected
'Ending balance including contributions' - if 'Ending balance' and 'Including contributions' are marked as selected
'Ending balance excluding YTD contributions' - if 'Ending balance' and 'Excluding YTD contributions' are marked as selected  
'Ending balance excluding half YTD contributions' - if 'Ending balance' and 'Excluding 1/2 YTD contributions' are marked as selected
'Ending balance excluding non-payroll and half payroll' - if 'Ending balance' and 'Excluding YTD non-payroll contributions except excluding only 1/2 of payroll contributions' are marked as selected
'Weighted average' - if 'Weighted average' is marked as selected
'Other: {method}' - if 'Other' is marked as selected (replace {method} with specified text)
'none' - if all options show unselected
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'top_heavy_provisions': """
Look for whether Top-Heavy provisions are included by checking if options are marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'Yes' - if 'Yes' is marked as selected
'No' - if 'No (may only select if governmental plan or if Plan covers exclusively union employees)' is marked as selected
'none' - if both options show unselected
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'top_heavy_minimum_benefit_plan': """
Look for which Plan provides top-heavy minimum benefit by checking if options are marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
''N/A (DC and DB Plans not maintained)'' - if 'N/A (DC and DB Plans not maintained)' is marked as selected
'Defined Contribution Plan, with 5% minimum' - if 'Defined Contribution Plan, with 5% minimum' is marked as selected
'Defined Benefit Plan, with 2% minimum accrual' - if 'Defined Benefit Plan, with 2% minimum accrual' is marked as selected
'Provide full top-heavy minimums in each Plan' - if 'Provide full top-heavy minimums in each Plan' is marked as selected
'none' - if all options show unselected
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'ADP_testing_method': """ Determine the method used for ADP testing by checking if options are marked as 'selected' or 'unselected'. 
Return only one of the following values without any additional text: 
'Current year method' - if 'Current year method' is marked as selected 
'Prior year method' - if 'Prior year method' is marked as selected 
'none' - if both options show unselected Check for the word 'selected' after each option to determine which is chosen. 
The text content is: {document_content}""",


'first_year_new_plan ': """
Determine the method for NHCP's actual deferral ratio for the first year of a new plan or for the first year as a 401(k) Plan by checking which option is marked as 'selected'.
Return only one of the following values without any additional text:
'Use the following to determine NHCP's actual deferral ratio' - if 'Use the following to determine NHCP's actual deferral ratio' is marked as selected
'3% (a prior-year test election)' - if '3% (a prior-year test election)' is marked as selected
'current year method for the first Plan Year' - if 'current year method for the first Plan Year' is marked as selected
'N/A (e.g., this is an existing 401(k) Plan)' - if 'N/A (e.g., this is an existing 401(k) Plan)' is marked as selected
'none' - if all options show unselected
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'ACP_testing_method': """
Determine the method for calculating NHCP's actual contribution ratio by checking which option is marked as 'selected'.
Return only one of the following values without any additional text:
'Current year method' - if 'Current year method' is marked as selected
'Prior year method' - if 'Prior year method' is marked as selected
'none' - if all options show unselected
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'first_year_contribution_ratio_method': """
Determine the method for NHCP's actual contribution ratio for the first year of a new plan or for the first year as a 401(m) Plan by checking which option is marked as 'selected'.
Return only one of the following values without any additional text:
'Use the following to determine NHCP's actual contribution ratio' - if 'Use the following to determine NHCP's actual contribution ratio' is marked as selected
'3% (a prior-year test election)' - if '3% (a prior-year test election)' is marked as selected
'current year method for the first Plan Year' - if 'current year method for the first Plan Year' is marked as selected
'N/A (e.g., this is an existing 401(m) Plan)' - if 'N/A (e.g., this is an existing 401(m) Plan)' is marked as selected
'none' - if all options show unselected
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'corrective_contribution_method_to_correct_ADP_test': """
Determine the method for corrective contributions to correct a failed ADP test by checking which option is marked as 'selected'.
Return only one of the following values without any additional text:
'flexible formula (but recorded and transmitted in writing to participants)' - if 'flexible formula (but recorded and transmitted in writing to participants)' is marked as selected
'fixed formula' - if 'fixed formula' is marked as selected
'none' - if all options show unselected

If 'fixed formula' is selected, further determine the allocation method for QNEC contributions by checking:
'QNEC contribution to NHCEs, allocated as follows' - if this option is marked as selected
Return one of the following values without any additional text:
'pro-rata on compensation' - if 'pro-rata on compensation' is marked as selected
'using the bottom-up ("targeted") method' - if 'using the bottom-up ("targeted") method' is marked as selected
'per-capita' - if 'per-capita' is marked as selected
'none' - if all options show unselected

If 'fixed formula' is selected and QNEC allocation is determined, further determine the allocation method for QMAC contributions by checking:
'QMAC contribution to NHCEs, allocated as follows' - if this option is marked as selected
Return one of the following values without any additional text:
'pro-rata on deferrals' - if 'pro-rata on deferrals' is marked as selected
'using the bottom-up ("targeted") method' - if 'using the bottom-up ("targeted") method' is marked as selected
'per-capita' - if 'per-capita' is marked as selected
'none' - if all options show unselected

Finally, determine the allocation of contributions by checking:
'will be allocated to' - if this option is marked as selected
Return one of the following values without any additional text:
'all NHCEs in the test' - if 'all NHCEs in the test' is marked as selected
'those NHCEs employed on the last day of the plan year' - if 'those NHCEs employed on the last day of the plan year' is marked as selected
'none' - if all options show unselected

Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'corrective_contribution_method_to_correct_ACP_test': """
Determine the allocation method for corrective contributions to correct a failed ACP test by checking which option is marked as 'selected'.
Return only one of the following values without any additional text:
'flexible (but recorded and transmitted in writing to participants)' - if 'flexible (but recorded and transmitted in writing to participants)' is marked as selected
'fixed formula' - if 'fixed formula' is marked as selected
'none' - if all options show unselected

If 'fixed formula' is selected, further determine the allocation method for QNEC contributions by checking:
'QNEC contribution to NHCEs, allocated as follows' - if this option is marked as selected
Return one of the following values without any additional text:
'pro-rata on compensation' - if 'pro-rata on compensation' is marked as selected
'using the bottom-up ("targeted") method' - if 'using the bottom-up ("targeted") method' is marked as selected
'per-capita' - if 'per-capita' is marked as selected
'none' - if all options show unselected

If 'fixed formula' is selected and QNEC allocation is determined, further determine the allocation method for QMAC contributions by checking:
'QMAC contribution to NHCEs, allocated as follows' - if this option is marked as selected
Return one of the following values without any additional text:
'pro-rata on deferrals' - if 'pro-rata on deferrals' is marked as selected
'using the bottom-up ("targeted") method' - if 'using the bottom-up ("targeted") method' is marked as selected
'per-capita' - if 'per-capita' is marked as selected
'none' - if all options show unselected

If 'fixed formula' is selected and QMAC allocation is determined, further determine the allocation method for matching contributions by checking:
'matching contribution to NHCEs, allocated as follows' - if this option is marked as selected
Return one of the following values without any additional text:
'pro-rata on deferrals' - if 'pro-rata on deferrals' is marked as selected
'using the bottom-up ("targeted") method' - if 'using the bottom-up ("targeted") method' is marked as selected
'per-capita' - if 'per-capita' is marked as selected
'none' - if all options show unselected

Finally, determine the allocation of contributions by checking:
'will be allocated to' - if this option is marked as selected
Return one of the following values without any additional text:
'all NHCEs in the test' - if 'all NHCEs in the test' is marked as selected
'those NHCEs employed on the last day of the plan year' - if 'those NHCEs employed on the last day of the plan year' is marked as selected
'none' - if all options show unselected

Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'Highly_Compensated_Employee_elections': """
Look for HCE elections based on two types of indicators in the preprocessed text:
1. For main options (No/Yes): Look for 'selected' or 'unselected' after each option
2. For sub-options: Look for '☒ selected ' or '☐ unselected' after each sub-option

Return only one of the following values without any additional text:
'No special elections' - if 'No' option shows 'selected'
'Top paid group only' - if 'Yes' shows 'selected' and only top-paid group shows '☒ selected '
'Calendar year lookback only' - if 'Yes' shows 'selected' and only calendar year shows '☒ selected '
'Top paid group and calendar year lookback' - if 'Yes' shows 'selected' and both sub-options show '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

The text content is: {document_content}
""",


'Plan_accept_rollovers': """
Look for rollover acceptance rules by checking:
1. For main Yes/No options: Check word 'selected' or 'unselected' after each option
2. For additional groups: Check for '☒ selected ' or '☐ unselected' after each option

Return only one of the following values without any additional text:
'No' - if 'No' option shows 'selected'
'Yes' - if only 'Yes, by all currently employed Participants' shows 'selected' with no additional groups showing '☒ selected '
'Yes, Participants who are no longer employed' - if 'Yes' shows 'selected' and only this additional group shows '☒ selected '
'Yes, Eligible Employees expected to enter the Plan' - if 'Yes' shows 'selected' and only this additional group shows '☒ selected '
'Yes, Participants who are no longer employed, Eligible Employees expected to enter the Plan' - if 'Yes' shows 'selected' and both additional groups show '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after Yes/No options
- '☒ selected ' or '☐ unselected' after additional group options
The text content is: {document_content}
""",

'distribution_of_rollover_contributions': """
Determine if distributions of rollover contributions can be made at any time by checking which option is marked as 'selected'.
Return one of the following values without any additional text:
'No, only at such time(s) as amounts attributable to employer contributions are distributable' - if 'No, only at such time(s) as amounts attributable to employer contributions are distributable' is marked as selected
'Yes' - if 'Yes' is marked as selected
'none' - if all options show unselected

Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'exclude_rollovers_contributions_5000_threshold': """
Look for whether rollover contributions are excluded from $5,000 threshold calculations by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'No or N/A' - if 'No or N/A' shows 'selected'
'Yes, exclude rollover contributions' - if 'Yes, exclude rollover contributions' shows 'selected'  
'none' - if all options show 'unselected'

Check for:
- 'selected' or 'unselected' after each option
The text content is: {document_content}
""",


'voluntary_aftertax_rollovers': """
Look for whether Plan accepts rollovers of after-tax voluntary contributions when Plan doesn't provide current voluntary after-tax contributions by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'No or N/A' - if 'No or N/A' shows 'selected'
'Yes' - if 'Yes' shows 'selected'
'none' - if all options show 'unselected'

Check for:
- 'selected' or 'unselected' after each option to determine selection
The text content is: {document_content}
""",

'pre_1987_deductible_QVECs': """
Look for whether deductible QVECs were permitted prior to 1/1/87 by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'No or N/A' - if 'No or N/A (new Plan effective after 12/31/86)' shows 'selected'
'Yes' - if 'Yes' shows 'selected'
'none' - if all options show 'unselected'

Check for:
- 'selected' or 'unselected' after each option
The text content is: {document_content}
""",

'participant_loans_permitted': """
Look for whether Participant loans are made by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'No' - if 'No' shows 'selected'
'Yes' - if 'Yes' shows 'selected'
'none' - if all options show 'unselected'

Check for:
- 'selected' or 'unselected' after each option
The text content is: {document_content}
""",

'directed_investments': """
Look for whether the Plan permits Directed Investments by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'No' - if 'No' shows 'selected'
'Yes' - if 'Yes' shows 'selected'
'none' - if all options show 'unselected'

Check for:
- 'selected' or 'unselected' after each option
The text content is: {document_content}
""",


'directed_investment_accounts': """
Look for which accounts permit Directed Investments by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For specific accounts: Check for '☒ selected ' or '☐ unselected' after each option

Return only one of the following values without any additional text:
'All Accounts' - if 'All Accounts' shows 'selected'
'Pre-Tax Elective Deferral Accounts' - if this option shows '☒ selected '
'Roth Elective Deferral Accounts' - if this option shows '☒ selected '
'Matching Contributions Accounts' - if this option shows '☒ selected '
'Qualified Matching Accounts' - if this option shows '☒ selected '
'Nonelective Contribution Accounts' - if this option shows '☒ selected '
'Qualified Nonelective Contribution Accounts' - if this option shows '☒ selected '
'Rollover Accounts' - if this option shows '☒ selected '
'After-Tax Voluntary Contribution Accounts' - if this option shows '☒ selected '
'Other: {specified_accounts}' - if Other option shows '☒ selected ' (replace with specified text)
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific account options
The text content is: {document_content}
""",

'life_insurance_purchase': """
Look for whether Life Insurance may be purchased for death benefits by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'No' - if 'No' shows 'selected'
'Yes, at Administrator\'s option' - if this option shows 'selected'
'Yes, at option of each Participant' - if this option shows 'selected'
'none' - if all options show 'unselected'

Check for:
- 'selected' or 'unselected' after each option
The text content is: {document_content}
""",

'employer_securities_purchase': """
Look for whether Qualifying Employer securities or real property may be purchased by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'No' - if 'No' shows 'selected'
'Yes' - if 'Yes' shows 'selected'
'none' - if all options show 'unselected'

Check for:
- 'selected' or 'unselected' after each option
The text content is: {document_content}
"""

}


RETIREMENT_AND_DISBALITIY_PROMPTS = {


'normal_retirement_age_additional': """
Look for additional Normal Retirement Age conditions by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For later age limit: Check for '☒ selected ' or '☐ unselected' and any specified numbers

Return only one of the following values without any additional text:
'N/A' - if 'N/A' shows 'selected'
'{number} anniversary' - if anniversary option shows 'selected' (replace {number} with specified value)
'{number}th birthday or {number} anniversary' - if birthday option shows '☒ selected ' (replace {number} with specified values)
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after birthday option
- Numbers specified in blank spaces
The text content is: {document_content}
""",

'money_purchase_normal_retirement_age': """
Look for Normal Retirement Age for money purchase assets by checking:
1. For main age: Check for number specified before 'birthday' in option d
2. For later conditions: Check for 'selected' or 'unselected' after each option
3. For additional limits: Check for '☒ selected ' or '☐ unselected' and any specified numbers

Return only one of the following values without any additional text:
'{number}th birthday' - if only birthday age is specified in d (replace {number} with specified value)
'{number}th birthday and {number} anniversary' - if both birthday and f option show specified values
'{number}th birthday not later than {number}th birthday' - if birthday and limit 1 are specified
'{number}th birthday not later than {number}th birthday or {number} anniversary' - if all values are specified
'N/A' - if 'N/A' shows 'selected'
'none' - if no values specified and all options show 'unselected' and '☐ unselected'

Check for:
- Numbers specified before 'birthday'
- 'selected' or 'unselected' after options
- '☒ selected ' or '☐ unselected' for additional limits
- Numbers specified in all blank spaces
The text content is: {document_content}
""",

'normal_retirement_date': """
Look for the Normal Retirement Date (NRD) by checking if 'First day of the month on or next following NRA', 'First day of the month nearest NRA', 'Anniversary Date on or next following NRA', 'Anniversary Date nearest NRA', or 'Participant's NRA' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'First day of the month on or next following NRA' - if 'First day of the month on or next following NRA' option shows 'selected'
'First day of the month nearest NRA' - if 'First day of the month nearest NRA' option shows 'selected'
'Anniversary Date on or next following NRA' - if 'Anniversary Date on or next following NRA' option shows 'selected'
'Anniversary Date nearest NRA' - if 'Anniversary Date nearest NRA' option shows 'selected'
'Participant's NRA' - if 'Participant's NRA' option shows 'selected'
'none' - if all options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",


'early_retirement_date': """
Look for the Early Retirement Date by checking if 'None provided', 'First day of the month coinciding with or next following...', or 'Anniversary Date coinciding with or next following...' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'None provided' - if 'None provided' option shows 'selected'
'First day of the month coinciding with or next following...' - if 'First day of the month coinciding with or next following...' option shows 'selected'
'Anniversary Date coinciding with or next following...' - if 'Anniversary Date coinciding with or next following...' option shows 'selected'
'none' - if all options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",
  

'Participant_disability_determination_method': """
Look for how Participant disability is determined by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'No disability benefits provided' - if this option shows 'selected'
'By a physician appointed by Administrator' - if this option shows 'selected'
'Under the Social Security Act' - if this option shows 'selected'
'As determined in accordance with the provisions of the Plan prior to this restatement: {text}' - if this option shows 'selected' (replace {text} with specified provisions)
'none' - if all options show 'unselected'

Check for:
- 'selected' or 'unselected' after each option
The text content is: {document_content}
"""

}

DISTRIBUTION_PROMPTS = {

'joint_survivor_annuity_distributions': """
Look for whether Plan Distributions are made in Joint and Survivor Annuities by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'No' - if 'No (cannot be selected with 1c) ' shows 'selected'
'Yes 100% of Participant\'s accounts' - if 'Yes' and '100% of Participant\'s accounts' show 'selected'
'Yes {number}% of Participant\'s accounts' - if 'Yes' and percentage option show 'selected' (replace {number} with specified percentage)
'none' - if all options show 'unselected'

Check for:
- 'selected' or 'unselected' after each option
- Specified percentage value if applicable
The text content is: {document_content}
""",


'joint_survivor_annuity_rules': """
Look for whether certain benefits will be subject to the Joint and Survivor Annuity rules by checking if 'No or N/A' or 'Yes' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'No or N/A (transfer of assets from pension plan not permitted) (cannot be selected with 10f or 88b)' - if 'No or N/A' option shows 'selected'
'Yes (must be selected if 10f or 88b selected) Note: If Yes, only Money Purchase assets (10f) or other transferred assets, if applicable, as well as any accounts that are permitted to be invested in certain annuity contracts, will be subject to the Joint and Survivor Annuity rules' - if 'Yes' option shows 'selected'
'none' - if both options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'post_severance_distribution_options': """
Look for Post-Severance Distribution Options by checking for '☒ selected ' or '☐ unselected' after each option.
Return only one of the following values without any additional text:
'Lump sum' - if only 'Lump sum' shows '☒ selected '
'Installments' - if only 'Installments' shows '☒ selected '
'Partial withdrawals' - if only 'Partial withdrawals' shows '☒ selected '
'Partial withdrawals or installments only for Participants required to take minimum distributions' - if only this option shows '☒ selected '
'Any form of annuity for only those accounts subject to QJSA requirements' - if only this option shows '☒ selected '
'Qualified Longevity Annuity Contracts' - if only this option shows '☒ selected '
'Other non-annuity form of benefit: {specified}' - if this option shows '☒ selected ' (replace {specified} with text provided)
'Other form of annuity form of benefit: {specified}' - if this option shows '☒ selected ' (replace {specified} with text provided)
'N/A (only the QJSA)' - if this option shows '☒ selected '
Multiple selections should be combined with commas
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' after each option
- Any specified text in blank spaces for 'Other' options
The text content is: {document_content}
""",

'distribution_payment_form': """
Look for distribution may be made in by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For limitations: Check for '☒ selected ' or '☐ unselected' and any specified text

Return only one of the following values without any additional text:
'Cash only (insurance contracts or other property allocated to the participant\'s account, and participant loan notes, may be treated as cash for this purpose)' - if this option shows 'selected'
'Cash or property' - if this shows 'selected' with no limitations showing '☒ selected '
'Cash or property Except that the following limitation(s) shall apply: {limitations}' - if 'Cash or property' shows 'selected' and limitations show '☒ selected ' (replace {limitations} with specified text)
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' for limitations
- Specified text in limitations blank space
The text content is: {document_content}
""",

'termination_distribution_timing': """
Look for when distributions over $5,000 may be made upon termination by checking for 'selected' or 'unselected' after each option.
Return only one of the following values without any additional text:
'Only upon death, disability or retirement' - if this option shows 'selected'
'As soon as feasible after termination of employment' - if this option shows 'selected'
'Only after Participant incurs 1-year break-in-service' - if this option shows 'selected'
'{number} months after termination of employment' - if this option shows 'selected' (replace {number} with specified months)
'On or after the Anniversary Date following termination of employment' - if this option shows 'selected'
'As soon as administratively feasible following the valuation date coincident with or next following the termination of employment' - if this option shows 'selected'
'Other: {text}' - if this option shows 'selected' (replace {text} with specified text)
'none' - if all options show 'unselected'

Check for:
- 'selected' or 'unselected' after each option
- Number specified for months option
- Text specified for Other option
The text content is: {document_content}
""",

'lump_sum_distribution_under_5000': """
Look for the lump-sum distribution option for amounts of $5,000 or less by checking if 'Same as above', 'As soon as feasible after termination of employment', 'Only after Participant incurs 1-year break-in-service', 'On or after the Anniversary Date following termination of employment', or 'As soon as administratively feasible following the valuation date coincident with or next following the termination of employment' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'Same as above' - if 'Same as above' option shows 'selected'
'As soon as feasible after termination of employment' - if 'As soon as feasible after termination of employment' option shows 'selected'
'Only after Participant incurs 1-year break-in-service' - if 'Only after Participant incurs 1-year break-in-service' option shows 'selected'
'On or after the Anniversary Date following termination of employment' - if 'On or after the Anniversary Date following termination of employment' option shows 'selected'
'As soon as administratively feasible following the valuation date coincident with or next following the termination of employment' - if 'As soon as administratively feasible following the valuation date coincident with or next following the termination of employment' option shows 'selected'
'none' - if all options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'Participant_consent(mandatory_distributions)': """
Look for mandatory distribution rules by checking:
1. For main Yes/No options: Check for 'selected' or 'unselected' after each option
2. For threshold amounts: Check for 'selected' or 'unselected' after each amount option

Return only one of the following values without any additional text:
'No, Participant consent is required for all distributions (NO mandatory distributions)' - if option a shows 'selected'
'Yes, Participant consent is needed only if the distribution exceeds: $5,000' - if option b and option 1 show 'selected'
'Yes, Participant consent is needed only if the distribution exceeds: $1,000' - if option b and option 2 show 'selected'
'Yes, Participant consent is needed only if the distribution exceeds: ${amount}' - if option b and option 3 show 'selected' (replace {amount} with specified amount)
'none' - if all options show 'unselected'

Check for:
- 'selected' or 'unselected' after each option
- Any specified amount in the blank space if option 3 is selected
The text content is: {document_content}
""",

'required_minimum_distributions_upon_death': """
Look for the required minimum distribution option upon the death of the Participant prior to the commencement of benefit distributions by checking if 'begin within 1 year of death, with spousal exception', 'be made within 5 years of death for all beneficiaries', 'be made within 5 years for nonspouse, with spousal exception', or 'be made (under one of these two methods) pursuant to the election of the Participant or beneficiary' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'begin within 1 year of death, with spousal exception' - if 'begin within 1 year of death, with spousal exception' option shows 'selected'
'be made within 5 years of death for all beneficiaries' - if 'be made within 5 years of death for all beneficiaries' option shows 'selected'
'be made within 5 years for nonspouse, with spousal exception' - if 'be made within 5 years for nonspouse, with spousal exception' option shows 'selected'
'be made (under one of these two methods) pursuant to the election of the Participant or beneficiary' - if 'be made (under one of these two methods) pursuant to the election of the Participant or beneficiary' option shows 'selected'
'none' - if all options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'death_benefit_no_beneficiary': """
Look for the option for the payment of any death benefit if no valid designation of beneficiary exists by checking if 'the Participant's estate' or 'the Participant's spouse, children, or parents, then estate' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'the Participant's estate' - if 'the Participant's estate' option shows 'selected'
'the Participant's spouse, children, or parents, then estate' - if 'the Participant's spouse, children, or parents, then estate' option shows 'selected'
'none' - if both options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'divorce_revoke_beneficiary_designation': """
Look for whether divorce revokes any designation of beneficiary to the spouse by checking if 'No' or 'Yes' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'No' - if 'No' option shows 'selected'
'Yes' - if 'Yes' option shows 'selected'
'none' - if both options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'minimum_distributions_requirement': """
Look for any modification to the required beginning date rule by checking for '☒ selected ' or '☐ unselected' and any specified text.
Return only one of the following values without any additional text:
'{specified_text}' - if option shows '☒ selected ' (replace {specified_text} with the text provided)
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' for the option
- Any specified text in the blank space if selected
The text content is: {document_content}
""",

'hardship_distributions': """
Look for whether Hardship Distributions may be made by checking if 'No' or 'Yes' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'No (skip to 109)' - if 'No (skip to 109)' option shows 'selected'
'Yes (may not be selected with 1c)' - if 'Yes (may not be selected with 1c)' option shows 'selected'
'none' - if both options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'hardship_determination': """
Look for how hardship shall be determined by checking if 'Safe Harbor standards of 401(k) Regulations' or 'Facts and circumstances' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'Safe Harbor standards of 401(k) Regulations' - if 'Safe Harbor standards of 401(k) Regulations' shows 'selected'
'Facts and circumstances' - if 'Facts and circumstances' shows 'selected'
'none' - if both options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'hardship_distribution_accounts': """
Look for which accounts permit hardship distributions by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For specific accounts: Check for '☒ selected ' or '☐ unselected' after each account option

Return only one of the following values without any additional text:
'All of the following accounts' - if 'All of the following accounts' shows 'selected'
'From the following accounts only: Pre-Tax Elective Deferral Accounts' - if 'From the following accounts only' shows 'selected' and 'Pre-Tax Elective Deferral Accounts' shows '☒ selected '
'From the following accounts only: Roth Elective Deferral Accounts' - if 'From the following accounts only' shows 'selected' and 'Roth Elective Deferral Accounts' shows '☒ selected '
'From the following accounts only: Matching Contribution Accounts' - if 'From the following accounts only' shows 'selected' and 'Matching Contribution Accounts' shows '☒ selected '
'From the following accounts only: Nonelective Contribution Accounts and Prevailing Wage Contributions' - if 'From the following accounts only' shows 'selected' and this account shows '☒ selected '
'From the following accounts only: Rollover Accounts' - if 'From the following accounts only' shows 'selected' and 'Rollover Accounts' shows '☒ selected '
'From the following accounts only: Transfer Accounts' - if 'From the following accounts only' shows 'selected' and 'Transfer Accounts' shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options 
- '☒ selected ' or '☐ unselected' after specific account options
The text content is: {document_content}
""",

'hardship_distribution_following_limitations': """
Look for limitations on hardship distributions by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For specific limitations: Check for '☒ selected ' or '☐ unselected' and any specified values

Return only one of the following values without any additional text:
'N/A. No limitations' - if 'N/A. No limitations' shows 'selected'
'The minimum amount of a distribution is ${amount}' - if 'The following limitations' shows 'selected' and this limitation shows '☒ selected '
'No more than {number} distribution(s) may be made to a Participant during a Plan Year' - if 'The following limitations' shows 'selected' and this limitation shows '☒ selected '
'Distributions may only be made from accounts which are fully Vested' - if 'The following limitations' shows 'selected' and this limitation shows '☒ selected '
'A Participant does not include a former employee at the time of the hardship distribution' - if 'The following limitations' shows 'selected' and this limitation shows '☒ selected '
'Hardship distributions are subject to the following limitation: {text}' - if 'The following limitations' shows 'selected' and this limitation shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific limitations
- Any specified values in blank spaces
The text content is: {document_content}
""",

'hardship_distributions_beneficiaries': """
Look for whether hardship distributions are allowed for beneficiary expenses by checking for '☒ selected ' or '☐ unselected' and any specified date.
Return only one of the following values without any additional text:
'Hardship distributions are allowed for beneficiary expenses' - if this option shows '☒ selected ' with no date specified
'Hardship distributions are allowed for beneficiary expenses {date}' - if option shows '☒ selected ' and date is specified (replace {date} with specified date)
'none' - if option shows '☐ unselected'
Check for:
- '☒ selected ' or '☐ unselected' after the option
- Any specified date in the blank space
The text content is: {document_content}
""",

'inservice_distributions_non_hardship': """
Look for whether non-hardship in-service distributions are permitted by checking:
1. For main Yes/No options: Check for 'selected' or 'unselected' after each option
2. For specific conditions: Check for '☒ selected ' or '☐ unselected' after each condition

Return only one of the following values without any additional text:
'No' - if 'No (skip to 111)' shows 'selected'
'Yes, if the Participant has attained age {age}' - if 'Yes' shows 'selected' and 'attained age' shows '☒ selected '
'Yes, if the Participant has attained age {age} however the only funds available for in-service distribution are money purchase accounts' - if 'Yes' shows 'selected' and both attained age and money purchase restriction show '☒ selected '
'Yes, if the Participant has reached Normal Retirement Age' - if 'Yes' shows 'selected' and 'reached Normal Retirement Age' shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific conditions
- Any specified age in blank space
The text content is: {document_content}
""",


'profit_sharing_inservice_distributions': """
Look for Profit Sharing in-service distribution rules by checking:
1. For main Yes/No options: Check for 'selected' or 'unselected' after each option 
2. For age/retirement conditions: Check for '☒ selected ' or '☐ unselected' and any specified ages
3. For money purchase fund options: Check for 'selected' or 'unselected' and any specified ages

Return only one of the following values without any additional text:
'No' - if 'No (skip to 111)' shows 'selected'
'Yes, if the Participant has attained age {age}' - if 'Yes' and attained age option show '☒ selected '
'Yes, if the Participant has reached Normal Retirement Age' - if 'Yes' and NRA option show '☒ selected ' 
'Yes, if the Participant has with respect to money purchase funds, NRA' - if 'Yes' and money purchase NRA option show 'selected'
'Yes, if the Participant has with respect to money purchase funds, age 62' - if 'Yes' and money purchase age 62 option show 'selected'
'Yes, if the Participant has with respect to money purchase funds, age {age}' - if 'Yes' and money purchase custom age option show 'selected'
'Yes, if the Participant has with respect to money purchase funds, earlier of NRA or age 62' - if 'Yes' and this option shows 'selected'
'Yes, if the Participant has with respect to money purchase funds, earlier of NRA or age {age}' - if 'Yes' and this option shows 'selected'
'none' - if all options show 'unselected' or '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options and money purchase options
- '☒ selected ' or '☐ unselected' for age/retirement conditions
- Any specified ages in blank spaces
The text content is: {document_content}
""",

'inservice_distribution_accounts': """
Look for which accounts permit in-service distributions are permitted by returning exactly what shows as 'selected' or '☒ selected '.
Return only one of the following values without any additional text:
'All accounts' - if 'All accounts' shows 'selected'
'From the following accounts only: Elective Deferral Accounts (select at least one of the following): pre-tax deferrals' - if these exact options show '☒ selected '  
'From the following accounts only: Elective Deferral Accounts (select at least one of the following): Roth deferrals (may select only with 22b)' - if these exact options show '☒ selected '
'From the following accounts only: Matching Contributions (select at least one of the following): ordinary matching contributions (may select only with 22d)' - if these exact options show '☒ selected '
'From the following accounts only: Matching Contributions (select at least one of the following): QMACs' - if these exact options show '☒ selected '
'From the following accounts only: Matching Contributions (select at least one of the following): ADP safe harbor matching contributions (may be selected only with 21d)' - if these exact options show '☒ selected '
'From the following accounts only: Nonelective Contribution Accounts and, when applicable, Prevailing Wage Contribution Accounts (select at least one of the following)' - if this option shows '☒ selected '
'From the following accounts only: Nonelective Contribution Accounts and, when applicable, Prevailing Wage Contribution Accounts (select at least one of the following): profit sharing contributions (may only be selected with 22e or 22f)' - if this exact option shows '☒ selected '
'From the following accounts only: Nonelective Contribution Accounts and, when applicable, Prevailing Wage Contribution Accounts (select at least one of the following): QNECs' - if this exact option shows '☒ selected '
'From the following accounts only: Nonelective Contribution Accounts and, when applicable, Prevailing Wage Contribution Accounts (select at least one of the following): ADP safe harbor nonelective contributions (may be selected only with 21d)' - if this exact option shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific account options
The text content is: {document_content}
""",

'inservice_distribution_provisions': """
Look for provisions that apply to in-service distributions by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For specific provisions: Check for '☒ selected ' or '☐ unselected' and any specified values

Return only one of the following values without any additional text:
'None' - if 'None' shows 'selected'
'The following provisions: The minimum amount of a distribution is ${amount} (may not exceed $1,000)' - if this provision shows '☒ selected '
'The following provisions: No more than {number} distribution(s) may be made to a Participant during a Plan Year' - if this provision shows '☒ selected '
'The following provisions: Distributions may only be made from accounts which are fully Vested (may be selected only if 40b, 41b, 41d, 41f, 41h, 41j, 41k or 83j selected)' - if this provision shows '☒ selected '
'The following provisions: In-service distributions may be made subject to the following provisions: {text} (must be definitely determinable and not subject to discretion)' - if this provision shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific provisions
- Any specified values in blank spaces
The text content is: {document_content}
""",

'accounts_permitting_inservice_distributions': """
Look for which accounts permit in-service distributions by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For specific accounts: Check for '☒ selected ' or '☐ unselected' after each sub-option

Return only one of the following values without any additional text:
'All accounts' - if 'All accounts' shows 'selected'
'From the following accounts only: Elective Deferral Accounts (select at least one of the following) (may be selected only if 22a or 22b): pre-tax deferrals' - if these exact options show '☒ selected '
'From the following accounts only: Elective Deferral Accounts (select at least one of the following) (may be selected only if 22a or 22b): Roth deferrals (may select only with 22b)' - if these exact options show '☒ selected '
'From the following accounts only: Matching Contributions (select at least one of the following) (may be selected only if 22d): ordinary matching contributions' - if these exact options show '☒ selected '
'From the following accounts only: Matching Contributions (select at least one of the following) (may be selected only if 22d): QMACs (may be selected only with 22a1, 22ba, 22d1, or 22g1)' - if these exact options show '☒ selected '
'From the following accounts only: Matching Contributions (select at least one of the following) (may be selected only if 22d): ADP safe harbor matching contributions (may be selected only with 21d)' - if these exact options show '☒ selected '
'From the following accounts only: Nonelective Contribution Accounts (select at least one of the following) (skip unless 22e): profit sharing contributions and any amounts in any money purchase account within this profit sharing plan' - if these exact options show '☒ selected '
'From the following accounts only: Nonelective Contribution Accounts (select at least one of the following) (skip unless 22e): QNECs (may be selected only with 22a1, 22ba, 22d1, or 22g1)' - if these exact options show '☒ selected '
'From the following accounts only: Nonelective Contribution Accounts (select at least one of the following) (skip unless 22e): ADP safe harbor nonelective contributions (may be selected only with 21d)' - if these exact options show '☒ selected '
'From the following accounts only: Prevailing Wage Contribution Accounts (may only be selected with 22f)' - if this exact option shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific account options
The text content is: {document_content}
""",

'additional_inservice_distribution_events': """
Look for additional in-service distribution provisions by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For specific conditions: Check for '☒ selected ' or '☐ unselected' after each option
3. For money purchase provisions: Check for 'selected' or 'unselected' and any specified values

Return only one of the following values without any additional text:
'In-service distributions may be made if: The Participant has been a Participant for at least 5 years' - if these exact options show '☒ selected ' and 'selected'
'In-service distributions may be made if: The amount to be distributed has accumulated in the Plan for at least 2 years' - if these exact options show '☒ selected ' and 'selected'
'In-service distributions may be made if: Either of the preceding two conditions is met' - if these exact options show '☒ selected ' and 'selected'
'In-service distributions may be made if: Both the conditions in g1 and g2 are met' - if these exact options show '☒ selected ' and 'selected'
'The Participant must also have attained the age specified at 109b' - if this exact option shows '☒ selected '
'Matching contributions (other than QMACs and ADP safe harbor matching contributions) (may select only with 109c AND 22d, or if 109d2a)' - if this exact option shows '☒ selected '
'Nonelective contributions (other than QNECs and ADP safe harbor nonelective contributions) (may select only with 109c AND 22e or 22f, or if 109d3a)' - if this exact option shows '☒ selected '
'In-service distributions of money purchase pension plan funds are available prior to normal retirement age: Yes, at age 62' - if these exact options show '☒ selected ' and 'selected'
'In-service distributions of money purchase pension plan funds are available prior to normal retirement age: Yes, at age: {age}' - if these options show '☒ selected ' and 'selected'
'No' - if this retroactive option shows 'selected'
'Yes, effective as of the first day of the 2007 plan year' - if this retroactive option shows 'selected'
'Yes, effective as of: {date}' - if this retroactive option shows 'selected'
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific conditions
- Any specified ages or dates in blank spaces
The text content is: {document_content}
""",

'inservice_distribution_limitations': """
Look for limitations that apply to in-service distributions by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For specific limitations: Check for '☒ selected ' or '☐ unselected' and any specified values

Return only one of the following values without any additional text:
'None' - if 'None' shows 'selected'
'The following limitations: The minimum amount of a distribution is ${amount} (may not exceed $1,000)' - if this exact option shows '☒ selected '
'The following limitations: No more than {number} distribution(s) may be made to a Participant during a Plan Year' - if this exact option shows '☒ selected '
'The following limitations: Distributions may only be made from accounts which are fully Vested (may be selected only if 40b, 41b, 41d, 41f, 41g or 83j selected)' - if this exact option shows '☒ selected '
'The following limitations: In-service distributions are subject to the following limitation: {text} (must be definitely determinable and not subject to discretion)' - if this exact option shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific limitations
- Any specified values in blank spaces
The text content is: {document_content}
""",

'additional_inservice_distribution_events_ps_match': """
Look for additional in-service distribution provisions for profit sharing and matching contributions by checking:
1. For main option g: Check for '☒ selected ' or '☐ unselected'
2. For conditions 1-4: Check for 'selected' or 'unselected'
3. For age requirement: Check for '☒ selected ' or '☐ unselected'
4. For contribution sources: Check for '☒ selected ' or '☐ unselected'

Return only one of the following values without any additional text:
'In-service distributions may be made if: The Participant has 5 years of participation' - if g and option 1 show '☒ selected ' and 'selected'
'In-service distributions may be made if: The amount to be distributed has accumulated in the Plan for at least 2 years' - if g and option 2 show '☒ selected ' and 'selected'
'In-service distributions may be made if: Either of the preceding two conditions is met' - if g and option 3 show '☒ selected ' and 'selected'
'In-service distributions may be made if: Both the conditions in g1 and g2 are met' - if g and option 4 show '☒ selected ' and 'selected'
'The Participant must also have attained the age specified at 109b' - if option 5 shows '☒ selected '
'Matching contributions (other than QMACs and ADP safe harbor matching contributions) (may select only with (1) both 109c and 22d, or (2) with 109d2a)' - if option 6 shows '☒ selected '
'Nonelective contributions (other than QNECs and ADP safe harbor nonelective contributions) (may select only if 109c and either 22e or 22f, or if 109d3a or 109d4)' - if option 7 shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' after options g, 5, 6, and 7
- 'selected' or 'unselected' after options 1-4
The text content is: {document_content}
""",

'money_purchase_inservice_distributions': """
Look for whether in-service distributions from money purchase plans are permitted by checking:
1. For main Yes/No options: Check for 'selected' or 'unselected' after each option
2. For specific conditions: Check for '☒ selected ' or '☐ unselected' and any specified age

Return only one of the following values without any additional text:
'No' - if 'No (skip to 112)' shows 'selected'
'Yes, if the Participant has attained age 62' - if 'Yes' shows 'selected' and 'age 62 (may not be selected with 2.)' shows '☒ selected '
'Yes, if the Participant has attained age: {age}' - if 'Yes' shows 'selected' and 'age: ______ (not less than 62) (may not be selected with 1.)' shows '☒ selected '
'Yes, if the Participant has attained Normal Retirement Age' - if 'Yes' shows 'selected' and 'Normal Retirement Age' shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific conditions
- Any specified age in blank space
The text content is: {document_content}
""",

'money_purchase_inservice_limitations': """
Look for limitations that apply to in-service distributions by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For specific limitations: Check for '☒ selected ' or '☐ unselected' and any specified values

Return only one of the following values without any additional text:
'N/A. No limitations' - if 'N/A. No limitations' shows 'selected'
'The following limitations: The minimum amount of a distribution is ${amount} (may not exceed $1,000)' - if this exact option shows '☒ selected '
'The following limitations: No more than {number} distribution(s) may be made to a Participant during a Plan Year' - if this exact option shows '☒ selected '
'The following limitations: Distributions may only be made from accounts which are fully Vested (may be selected only if 40b or 42b selected)' - if this exact option shows '☒ selected '
'The following limitations: In service distributions are subject to the following limitation: {text} (must be definitely determinable and not subject to discretion, e.g., prevailing wage contributions only)' - if this exact option shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific limitations
- Any specified values in blank spaces
The text content is: {document_content}
""",

'inplan_roth_rollover_restrictions': """
Look for restrictions on In-Plan Roth Rollover Conversions by checking for '☒ selected ' or '☐ unselected' after each option.
Return only one of the following values without any additional text:
'In-service distribution only. Only Participants who are Employees may elect an In-Plan Roth Rollover' - if this exact option shows '☒ selected '
'No transfer of loans. Loans may not be distributed as part of an In-Plan Roth Rollover (may not be selected with 89a)' - if this exact option shows '☒ selected '
'In-service distribution only. Only Participants who are Employees may elect an In-Plan Roth Rollover, No transfer of loans. Loans may not be distributed as part of an In-Plan Roth Rollover (may not be selected with 89a)' - if both options show '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' after each option
The text content is: {document_content}
""",


'inplan_roth_rollover_provisions': """
Look for in-service distribution provisions for In-Plan Roth Rollovers by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For specific conditions: Check for '☒ selected ' or '☐ unselected' and any specified values
3. For source options: Check for 'selected' or 'unselected' and '☒ selected ' or '☐ unselected'
4. For other provisions: Check for 'selected' or 'unselected' and '☒ selected ' or '☐ unselected'

Return only one of the following values without any additional text:
'Only existing in-service distribution provisions apply. The Plan\'s existing in-service distribution provisions apply (may be selected only with 109b)' - if this option shows 'selected'

For option d selections:
'The Participant has attained age {age}' - if this option shows '☒ selected '
'The Participant has {years} years of participation (specify minimum of 5 years)' - if this option shows '☒ selected '
'The amounts being distributed have accumulated in the Plan for at least {years} years (at least 2)' - if this option shows '☒ selected '
'Other (describe): {text}' - if this option shows '☒ selected '

For source options:
'All qualifying Accounts' - if this option shows 'selected'
'Pre-Tax Elective Deferral Account' - if this option shows '☒ selected '
'Account(s) attributable to any Employer matching contributions' - if this option shows '☒ selected '
'Account attributable to Employer profit sharing contributions (may only be selected with 22e)' - if this option shows '☒ selected '
'Qualified Nonelective Contribution Account (including any ADP safe harbor nonelective contributions)' - if this option shows '☒ selected '
'Rollover Account (may only be selected with 22h)' - if this option shows '☒ selected '
'Other: {text}' - if this option shows '☒ selected '

For other provisions:
'No other provisions' - if this option shows 'selected'
'The minimum amount that may be rolled over is ${amount} (may not exceed $1,000)' - if this option shows '☒ selected '
'Distributions may only be made from accounts which are fully Vested' - if this option shows '☒ selected '
'In-service distributions may be made subject to the following provisions: {text}' - if this option shows '☒ selected '
'Distribution for withholding also permitted' - if this option shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific conditions
- Any specified values in blank spaces
The text content is: {document_content}
""",
'inplan_roth_rollover_effective_date': """
Look for effective date of In-Plan Roth Rollover provisions by checking for '☒ selected ' or '☐ unselected' and specified date.
Return only one of the following values without any additional text:
'Effective date: {date}' - if option shows '☒ selected ' (replace {date} with specified date)
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' after the option
- Specified date in blank space
The text content is: {document_content}
""",

'inplan_roth_rollover_cessation': """
Look for cessation date of In-Plan Roth Rollover provisions by checking for '☒ selected ' or '☐ unselected' and specified date.
Return only one of the following values without any additional text:
'Effective date of cessation of In-Plan Roth Rollovers: {date}' - if option shows '☒ selected ' (replace {date} with specified date)
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' after the option
- Specified date in blank space
The text content is: {document_content}
""",

'inplan_roth_transfer_effective_date': """
Look for special retroactive effective date for In-Plan Roth Transfers by checking:
1. For main option: Check for '☒ selected ' or '☐ unselected'
2. For specific date options: Check for 'selected' or 'unselected' and any specified date

Return only one of the following values without any additional text:
'Special retroactive effective date: January 1, 2013' - if main option shows '☒ selected ' and 'January 1, 2013' shows 'selected'
'Special retroactive effective date: {date}' - if main option shows '☒ selected ' and custom date option shows 'selected'
'none' - if options show '☐ unselected' and 'unselected'

Check for:
- '☒ selected ' or '☐ unselected' after main option
- 'selected' or 'unselected' after date options
- Specified date in blank space
The text content is: {document_content}
""",

'inplan_roth_transfer_sources': """
Look for permitted sources for In-Plan Roth transfers by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For specific accounts: Check for '☒ selected ' or '☐ unselected' and any specified text

Return only one of the following values without any additional text:
'The Vested portion of any qualifying Account' - if this option shows 'selected'
'Only from the Vested portion of the following accounts: Pre-Tax Elective Deferral Account' - if main option g and this account show 'selected' and '☒ selected '
'Only from the Vested portion of the following accounts: Account(s) attributable to Employer matching contributions (includes any ADP/ACP test safe harbor matching contributions) (may only be selected with 21d or 22d)' - if main option g and this account show 'selected' and '☒ selected '
'Only from the Vested portion of the following accounts: Nonelective Account attributable to Employer profit sharing contributions (may only be selected with 22e)' - if main option g and this account show 'selected' and '☒ selected '
'Only from the Vested portion of the following accounts: Qualified Nonelective Contribution Account (includes any ADP test safe harbor nonelective contributions) (may not be selected unless 22a1, 22b, 22d, or 22g)' - if main option g and this account show 'selected' and '☒ selected '
'Only from the Vested portion of the following accounts: Rollover Account (may only be selected with 86b)' - if main option g and this account show 'selected' and '☒ selected '
'Only from the Vested portion of the following accounts: Voluntary employee contributions (may only be selected with 22g)' - if main option g and this account show 'selected' and '☒ selected '
'Only from the Vested portion of the following accounts: Other: {text}' - if main option g and this option show 'selected' and '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific accounts
- Any specified text in Other option
The text content is: {document_content}
""",

'inplan_roth_transfer_limitations': """
Look for other limitations on In-Plan Roth Transfers by checking:
1. For main options: Check for 'selected' or 'unselected' after each option
2. For specific limitations: Check for '☒ selected ' or '☐ unselected' and any specified values

Return only one of the following values without any additional text:
'No other limitations' - if this option shows 'selected'
'The minimum amount that may be transferred is ${amount} (may not exceed $1,000)' - if this limitation shows '☒ selected '
'Transfers may only be made from accounts which are fully Vested (may not be selected with 40a)' - if this limitation shows '☒ selected '
'No more than {number} transfer(s) may be made during a Plan Year' - if this limitation shows '☒ selected '
'Only Participants who are Employees may elect an In-Plan Roth Transfer' - if this limitation shows '☒ selected '
'Transfers are subject to the following limitations (describe): {text}' - if this limitation shows '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific limitations
- Any specified values in blank spaces
The text content is: {document_content}
""",


'military_distribution': """
Look for whether the Plan provide for continued benefit accruals for those in military by checking if 'No' or 'Yes' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'No' - if 'No' option shows 'selected'
'Yes' - if 'Yes' option shows 'selected'
'none' - if both options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'distributions_deemed_severence_military': """
Look for whether the Plan permits distributions on account of the deemed severance of employment for persons in the military by checking if 'No' or 'Yes' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'No' - if 'No' option shows 'selected'
'Yes' - if 'Yes' option shows 'selected'
'none' - if both options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
""",

'qualified_reservist_distribution_military': """
Look for whether the Plan permits Qualified Reservist distributions on account of the deemed severance of employment for persons in the military by checking if 'No' or 'Yes' is marked as 'selected' or 'unselected'.
Return only one of the following values without any additional text:
'No' - if 'No' option shows 'selected'
'Yes' - if 'Yes' option shows 'selected'
'none' - if both options show 'unselected'
Check for the word 'selected' or 'unselected' after each option to determine which is chosen.
The text content is: {document_content}
"""
}


PERMITTED_ELECTION_PROMPTS = {

'miscellaneous_elections': """
Look for which miscellaneous options are selected by checking for '☒ selected ' or '☐ unselected' after each option.
Return only one of the following values without any additional text:
'Rule of parity. Exclude rule of parity (all years count) (may be selected only with 25)' - if this option shows '☒ selected '
'Change in eligibility. If eligibility is being made more strict as of the effective date of the restatement, then all Participants must meet the new requirements, rather than being grandfathered (skip if 10a)' - if this option shows '☒ selected '
'Deemed 125 compensation. Amounts included in compensation because of an election under Code §125(a) shall include deemed 125 compensation as described by IRS Revenue Ruling 2002-27.' - if this option shows '☒ selected '
'Definition of Spouse. The term Spouse includes a spouse under federal law as well as the following: {text}' - if this option shows '☒ selected '
'Top Heavy Offset by Match. Do not treat matching contributions toward the top-heavy minimum contribution (may be selected only with 83a and [21d1 or 22d1]' - if this option shows '☒ selected '
'Administrative Delay. Apply the administrative delay ("first few weeks") rule when determining compensation for 415 purposes.' - if this option shows '☒ selected '
'Rate of Deferral. The Plan will include a Participant\'s Elective Deferrals that are made prior to the effective date the matching contribution component of the Plan (may not be selected unless 22d1)' - if this option shows '☒ selected '
'All IRC 410(b)(6)(C) events: Do not exclude (i.e., include) employees who are acquired in any 410(b)(6)(C) transaction (may not be selected with i.)' - if this option shows '☒ selected '
'Specific IRC 410(b)(6)(C) events: Do not exclude (i.e., include) employees who are acquired in a specific 410(b)(6)(C) transaction: {text}' - if this option shows '☒ selected '
'Exclude Discretionary Safe Harbor Contribution for HCEs. For a plan that excludes HCEs the ADP safe harbor, also remove the document language that nonetheless permits the Employer to operationally make a discretionary safe harbor contribution for the HCEs, i.e., the exclusion of HCEs from is absolute (may not be selected unless 59b1)' - if this option shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' after each option
- Any specified text in blank spaces
The text content is: {document_content}
""",

'additional_plan_coordination': """
Look for additional plan coordination provisions by checking:
1. For main Yes/No options: Check for 'selected' or 'unselected' after each option
2. For specific provisions: Check for '☒ selected ' or '☐ unselected' and any specified text

Return only one of the following values without any additional text:
'No, or all coordination issues have already been specified (e.g., coordination of top-heavy minimums at Question 83)' - if this option shows 'selected'
'Yes: Language necessary to coordinate how the overall 415 limit will be determined in a manner that will prelude employer discretion: {text}' - if option b and this provision show 'selected' and '☒ selected '
'Yes: Language necessary to coordinate maximum permitted disparity if the employer has more than one plan that provides permitted disparity: {text}' - if option b and this provision show 'selected' and '☒ selected '
'Yes: Language to protect any benefits not otherwise provided for by the above specifications: {text}' - if option b and this provision show 'selected' and '☒ selected '
'none' - if all options show 'unselected' and '☐ unselected'

Check for:
- 'selected' or 'unselected' after main options
- '☒ selected ' or '☐ unselected' after specific provisions
- Any specified text in blank spaces
The text content is: {document_content}
"""

}




PARTICIPATING_EMPLOYER_PROMPTS = {

    '165.0 participating_employers': """
    Look for whether there are participating employers to be included by checking:
    1. For main Yes/No options: Check for 'selected' or 'unselected' after each option
    2. If Yes is selected, check for additional options with '☒ selected ' or '☐ unselected'

    Return only one of the following values without any additional text:
    'No (skip to 165)' - if 'No (skip to 165)' shows '☒ selected '
    'Yes list in SPD' - if 'Yes' shows 'selected' and 'list the Participating Employers in the SPD' shows '☒ selected '
    'Yes include agreements' - if 'Yes' shows 'selected' and 'include Participation Agreements for Participating Employers' shows '☒ selected '
    'Yes include agreements no resolution' - if 'Yes' shows 'selected' and both 'include Participation Agreements' and 'No Adopting Resolution' show '☒ selected '
    'none' - if no options show 'selected' or '☒ selected '

    Check for:
    - 'selected' or 'unselected' after main Yes/No options
    - '☒ selected ' or '☐ unselected' after additional options
    The text content is: {document_content}
    """,

    '165.5 participation_agreement_signing': """
    Look for E-Sign. Select the option below if the Participation Agreements will be signed electronically (i.e., using an e-signature) (leave blank if not 
    applicable) by checking for '☒ selected ' or '☐ unselected'.

    Return only one of the following values without any additional text:
    'The Participation Agreements will be signed electronically' - if this option shows '☒ selected '
    'none' - if option shows '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before the option
    The text content is: {document_content}
    """,

    '165.6 participation_agreement_presentation': """
    Look for Presentation. Select the option below if each participation agreement shall be its own separate file (maximum 5). If selected, the first five 
    forms will print as separate files; forms for employers 6 to 20 will be in one combined file by checking for '☒ selected ' or '☐ unselected'.

    Return only one of the following values without any additional text:
    'Participation Agreements will be in a separate file' - if option shows '☒ selected '
    'none' - if option shows '☐ unselected'

    Check for:
    - '☒ selected ' or '☐ unselected' before the option
    The text content is: {document_content}
    """

}

SUBSEQUENT_CYCLE4_EMPLOYER_PROMPTS = {


'bba_provisions': """
Look for which BBA provisions apply by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'For a 401(k) plan, implement the hardship provisions of the Bipartisan Budget Act of 2018 (complete Questions 166-167) (must be selected if 1a and 108b)' - if 'For a 401(k) plan, implement the hardship provisions of the Bipartisan Budget Act of 2018 (complete Questions 166-167) (must be selected if 1a and 108b)' shows '☒ selected '

'For C3 restatement of a non-401(k) ("straight") PS plan, optionally reflect some or all provisions of BPA\'18 (i.e., as if the plan was a 401(k) rules) (may not be selected unless 1b and either 22g or 108b selected)' - if 'For C3 restatement of a non-401(k) ("straight") PS plan, optionally reflect some or all provisions of BPA\'18 (i.e., as if the plan was a 401(k) rules) (may not be selected unless 1b and either 22g or 108b selected)' shows '☒ selected '

'Coordination Amendment Only: This Coordination Amendment was already timely adopted separately' - if 'Coordination Amendment Only' shows '☒ selected ' and 'This Coordination Amendment was already timely adopted separately' shows '☒ selected '

'Coordination Amendment Only: Build a file for employer signature' - if 'Coordination Amendment Only' shows '☒ selected ' and 'Build a file for employer signature (must be timely adopted)' shows '☒ selected '

'Coordination Amendment Only: Include a copy of the FIS-adopted mass submitter amendment' - if 'Coordination Amendment Only' shows '☒ selected ' and 'Include a copy of the FIS-adopted mass submitter amendment to show timely compliance' shows '☒ selected '

'None of the preceding options apply (may not be selected if 1a and 108b) (skip to 180)' - if 'None of the preceding options apply (may not be selected if 1a and 108b) (skip to 180)' shows '☒ selected '

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'hardship_provisions_budget_act': """
Look for whether to include hardship provisions of the Budget Act of 2018 by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'No (skip to 180)' - if 'No (skip to 180)' shows '☒ selected '
'Yes. (Answer below as applicable)' - if 'Yes. (Answer below as applicable)' shows '☒ selected '
'Yes. (Answer below as applicable): Yes. Beginning on the Effective Date, Elective Deferrals (and employee contributions, if applicable) will not be suspended on account of a hardship distribution, regardless of the date of the distribution.' - if 'Yes' and this deferral option show '☒ selected '
'Yes. (Answer below as applicable): No. The Participant\'s suspension of Elective Deferrals that began before the Effective Date will continue for the six-month period.' - if 'Yes' and this deferral option show '☒ selected '
'Yes. (Answer below as applicable): Yes. QNECs and QMACs are available for hardship distributions.' - if 'Yes' and this QNEC option shows '☒ selected '
'Yes. (Answer below as applicable): No. QNECs and QMACs are not available for hardship distributions' - if 'Yes' and this QNEC option shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'hardship_distribution_sources': """
Look for whether QNECs and QMACs are available for hardship distributions by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Yes. QNECs and QMACs are available for hardship distributions' - if 'Yes. QNECs and QMACs are available for hardship distributions' shows '☒ selected '
'No. QNECs and QMACs are not available for hardship distributions' - if 'No. QNECs and QMACs are not available for hardship distributions' shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'hardship_loan_requirement': """
Look for whether loan requirement applies for hardship distributions by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Amendment Section 3.1(b) APPLIES (i.e., Participants are required to obtain a Plan loan) indefinitely, unless and until the Plan is further amended' - if this option shows '☒ selected '
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'hardship_elective_deferral_earnings': """
Look for whether earnings on Elective Deferrals are excluded from hardship distributions by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Earnings on amounts attributable to Elective Deferrals are NOT available for hardship distributions (may not be selected unless 1a)' - if this option shows '☒ selected '
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'hardship_needs_events': """
Look for which hardship needs/events provisions do not apply by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Amendment Section 3.3 will NOT apply (and so casualty losses are limited to federally declared disasters, pursuant to Code §165(h)' - if this option shows '☒ selected '
'Amendment Section 3.4 will NOT apply (and so the Plan will not make hardship distributions on account of Disaster Losses)' - if this option shows '☒ selected '
'Amendment Section 3.3 will NOT apply (and so casualty losses are limited to federally declared disasters, pursuant to Code §165(h), Amendment Section 3.4 will NOT apply (and so the Plan will not make hardship distributions on account of Disaster Losses)' - if both options show '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",


'hardship_effective_dates': """
Look for special effective dates by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Other general Effective Date: {date}' - if 'Other general Effective Date: {date} (may not be earlier than the first day of the first Plan Year beginning on or after January 1, 2019 or after the Latest Effective Date)' shows '☒ selected '

'Special Effective Date for Amendment Section 2.2a: {date}' - if 'Special Effective Date for Amendment Section 2.2a: {date} (Enter a special effective date, no sooner than the first day of the 2019 Plan Year)' shows '☒ selected '

'Special Effective Date for Amendment Section 2.3a: {date}' - if 'Special Effective Date for Amendment Section 2.3a: {date} (Enter a special effective date, no sooner than the first day of the 2019 Plan Year)' shows '☒ selected '

'Special Effective Date for Amendment Section 2.3b: {date}' - if 'Special Effective Date for Amendment Section 2.3b: {date} (Enter a special effective date, no sooner than the first day of the 2019 Plan Year)' shows '☒ selected '

'Special Effective Date for Amendment Section 2.3c: {date}' - if 'Special Effective Date for Amendment Section 2.3c: {date} (Enter a special effective date for the expansion of hardship needs/events, no sooner than January 1, 2018)' shows '☒ selected '

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
"""

}


OTHER_PROVISIONS_PROMPTS = {

'QDIA_inclusion': """
Look for whether to include Qualified Default Investment Alternative by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'No (skip to 181)' - if 'No (skip to 181)' shows '☒ selected '
'Yes' - if 'Yes' shows '☒ selected '
'Yes, However, I want to skip to Q181 at this time' - if 'Yes' shows '☒ selected ' and 'However, I want to skip to Q181 at this time' shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",


'basic_QDIA_characteristics': """
Look for QDIA characteristics by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Multiple Primary QDIA' - if 'Multiple Primary QDIA' shows '☒ selected '

'Multiple Primary QDIA Investment objectives: {text}' - if 'Multiple Primary QDIA' and 'Investment objectives: {text}' show '☒ selected '

'Multiple Primary QDIA Risk/return characteristics: {text}' - if 'Multiple Primary QDIA' and 'Risk/return characteristics: {text}' show '☒ selected '

'Multiple Primary QDIA Fees/expenses: {text}' - if 'Multiple Primary QDIA' and 'Fees/expenses: {text}' show '☒ selected '

'Multiple Primary QDIA Description of Investments: Year of NRA: {year}, Name of Investment: {name}' - if 'Multiple Primary QDIA' and 'Description of Investments' show '☒ selected ' (repeat for each year/name pair)

For investments:
'a. Name of Investment: {name}'
'b. Name of Investment: {name}'
'c. Name of Investment: {name}'
'd. Name of Investment: {name}'
'e. Name of Investment: {name}'
'f. Name of Investment: {name}'
'g. Name of Investment: {name}'
'h. Name of Investment: {name}'
'i. Name of Investment: {name}'
'j. Name of Investment: {name}'

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Any specified text in blank spaces
- All investment names listed under each letter
The text content is: {document_content}
""",

'qdia_optout_frequency': """
Look for how often participants can elect out of default investment by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'At any time' - if 'At any time' shows '☒ selected '
'Quarterly' - if 'Quarterly' shows '☒ selected '
'Other: {text}' - if 'Other: {text} (must be at least quarterly)' shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Any specified text after Other option
The text content is: {document_content}
""",


'qdia_fees_restrictions': """
Look for fees and restrictions that apply for transfers out of default election by checking for any specified text.

Return only one of the following values without any additional text:
'{text}' - if any text is specified after 'i.' (replace {text} with specified fees/restrictions)
'none' - if no text is specified

Check for:
- Any text specified after 'i.'
The text content is: {document_content}
""",

'Separate_adp_safe_harbor_amendment': """
Look for whether a separate amendment should be adopted for ADP safe harbor method by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'No (skip to 190)' - if 'No (skip to 190)' shows '☒ selected '
'Yes' - if 'Yes' shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'ADP_safe_harbor_effective_dates': """
Look for effective dates for the ADP safe harbor amendment.

Return only one of the following formats without any additional text:
'Current plan year: {date}, Forthcoming plan year: {date}' - if both dates are specified (replace {date} with specified dates)
'Current plan year: {date}' - if only current plan year date is specified
'Forthcoming plan year: {date}' - if only forthcoming plan year date is specified
'none' - if no dates are specified

Check for:
- Date specified after 'current plan year'
- Date specified after 'forthcoming plan year'
The text content is: {document_content}
""",

'Current_plan_year_safe_harbor': """
Look for whether there is a current "maybe" safe harbor election being activated by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Yes, the Plan is adopting an amendment at least 30 days prior to the end of the current Plan Year to make the ADP safe harbor nonelective contribution for the current Plan Year. (NOTE: This contribution will be a Qualified Nonelective Safe Harbor Contribution if 23i3 or 23i4 has been selected)' - if this option shows '☒ selected '
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'Forthcoming_plan_year_safe_harbor': """
Look for which safe harbor formula will be used in forthcoming Plan Year by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Not applicable' - if 'Not applicable (may only be selected with 181e)' shows '☒ selected '

'No safe harbor contribution will be made for the forthcoming Plan Year: Use the current-year ADP testing method' - if 'No safe harbor contribution will be made for the forthcoming Plan Year' and 'Use the current-year ADP testing method for the forthcoming plan year' show '☒ selected '

'No safe harbor contribution will be made for the forthcoming Plan Year: Use the prior-year ADP testing method' - if 'No safe harbor contribution will be made for the forthcoming Plan Year' and 'Use the prior-year ADP testing method for the forthcoming plan year' show '☒ selected '

'Traditional Formula: Basic Matching' - if 'Traditional Formula' and 'Basic Matching' show '☒ selected '

'Traditional Formula: Enhanced Matching' - if 'Traditional Formula' and 'Enhanced Matching' show '☒ selected '

'Traditional Formula: Nonelective' - if 'Traditional Formula' and 'Nonelective' show '☒ selected '

'Traditional Formula: Reserve the right to amend the plan in the forthcoming plan year to make a Nonelective Safe Harbor Contribution' - if 'Traditional Formula' and this option show '☒ selected '

'QACA Formula: Basic Matching' - if 'QACA Formula' and 'Basic Matching' show '☒ selected '

'QACA Formula: Enhanced Matching' - if 'QACA Formula' and 'Enhanced Matching' show '☒ selected '

'QACA Formula: Nonelective' - if 'QACA Formula' and 'Nonelective' show '☒ selected '

'QACA Formula: Reserve the right to amend the plan to make a Nonelective Safe Harbor Contribution' - if 'QACA Formula' and this option show '☒ selected '

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'safe_harbor_amendment_duration': """
Look for how long the amendment's provisions will remain in effect by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'remain in effect until such time (if any) that the employer changes these provisions by adopting a subsequent amendment' - if 'remain in effect until such time (if any) that the employer changes these provisions by adopting a subsequent amendment' shows '☒ selected '
'be effective for only the forthcoming plan year' - if 'be effective for only the forthcoming plan year' shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'trust_earnings_allocation': """
Look for how Trust earnings are allocated by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Beginning balance' - if 'Beginning balance' shows '☒ selected '
'Ending balance Including contributions' - if 'Ending balance' and 'Including contributions' show '☒ selected '
'Ending balance Excluding YTD contributions' - if 'Ending balance' and 'Excluding YTD contributions' show '☒ selected '
'Ending balance Excluding 1/2 YTD contributions' - if 'Ending balance' and 'Excluding 1/2 YTD contributions' show '☒ selected '
'Ending balance Excluding YTD non-payroll contributions except excluding only 1/2 of payroll contributions' - if 'Ending balance' and this option show '☒ selected '
'Weighted average' - if 'Weighted average' shows '☒ selected '
'Other: {text}' - if 'Other: {text}' shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Any specified text after Other option
The text content is: {document_content}
"""

}


DOCUMENT_REQUESTS_PROMPTS = {

'include_amendments': """
Look for which amendments to include by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'In-Plan Roth Transfers (may only be selected with 165b)' - if 'In-Plan Roth Transfers (may only be selected with 165b)' shows '☒ selected '
'Amendment to remove restriction on forfeitures reducing QNECs, QMACs and SH contributions' - if 'Amendment to remove restriction on forfeitures reducing QNECs, QMACs and SH contributions' shows '☒ selected '
'Amendment for hardship provisions of the Budget Act of 2018 (may only be selected with 166b)' - if 'Amendment for hardship provisions of the Budget Act of 2018 (may only be selected with 166b)' shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'basic_supporting_forms': """
Look for which basic supporting forms are included by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'No basic forms' - if 'No basic forms' shows '☒ selected '

'Includes all forms--SPD-8.5 x 11, Short Form Q&A, Annual Notices, Tax Notices (402(f)), Administrative Forms with Guide, Resolution, Tax Forms, Notice and Index' - if this option shows '☒ selected '

'Select Individual Forms: SPD-8.5 x 11' - if 'Select Individual Forms' and 'SPD-8.5 x 11' show '☒ selected '
'Select Individual Forms: Short Form Q&A' - if 'Select Individual Forms' and 'Short Form Q&A' show '☒ selected '
'Select Individual Forms: Resolution' - if 'Select Individual Forms' and 'Resolution' show '☒ selected '
'Select Individual Forms: Annual Contribution Notice' - if 'Select Individual Forms' and 'Annual Contribution Notice' show '☒ selected '
'Select Individual Forms: Annual Investment Notice' - if 'Select Individual Forms' and 'Annual Investment Notice' show '☒ selected '
'Select Individual Forms: Tax Notices (402(f))' - if 'Select Individual Forms' and 'Tax Notices (402(f))' show '☒ selected '
'Select Individual Forms: Administrator\'s Guide' - if 'Select Individual Forms' and 'Administrator\'s Guide' show '☒ selected '
'Select Individual Forms: Index' - if 'Select Individual Forms' and 'Index' show '☒ selected '
'Select Individual Forms: Administrative Forms: General Forms' - if 'Select Individual Forms' and 'Administrative Forms' and 'General Forms' show '☒ selected '
'Select Individual Forms: Administrative Forms: Distribution Forms (General)' - if 'Select Individual Forms' and 'Administrative Forms' and 'Distribution Forms (General)' show '☒ selected '
'Select Individual Forms: Administrative Forms: Distribution Forms (Death)' - if 'Select Individual Forms' and 'Administrative Forms' and 'Distribution Forms (Death)' show '☒ selected '
'Select Individual Forms: Administrative Forms: Distribution Forms (In-Service)' - if 'Select Individual Forms' and 'Administrative Forms' and 'Distribution Forms (In-Service)' show '☒ selected '
'Select Individual Forms: Administrative Forms: Loan Forms' - if 'Select Individual Forms' and 'Administrative Forms' and 'Loan Forms' show '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'additional_supporting_forms': """
Look for which additional supporting forms are included by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'No additional forms' - if 'No additional forms' shows '☒ selected '

'Also include the following forms: Tax Forms' - if 'Also include the following forms' shows '☒ selected ' and 'Tax Forms' shows '☒ selected '

'Also include the following forms: Notice to Interested Parties' - if 'Also include the following forms' shows '☒ selected ' and 'Notice to Interested Parties' shows '☒ selected '

'Also include the following forms: Submission Instructions (Submission Forms)' - if 'Also include the following forms' shows '☒ selected ' and 'Submission Instructions (Submission Forms)' shows '☒ selected '

'Also include the following forms: Appendix for Plan Expense Allocations (appears at the end of the SPD)' - if 'Also include the following forms' shows '☒ selected ' and 'Appendix for Plan Expense Allocations (appears at the end of the SPD)' shows '☒ selected '

'Also include the following forms: Appendix for Rollovers From Other Plans (appears at the end of the SPD; applies only if Plan accepts rollovers) (may only be selected with 22h)' - if 'Also include the following forms' shows '☒ selected ' and this option shows '☒ selected '

'Also include the following forms: Include an SMM for hardship provisions of the Budget Act of 2018 (applies only if 166b selected' - if 'Also include the following forms' shows '☒ selected ' and this option shows '☒ selected '

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'explanation_of_forms': """
Look for whether to exclude administrator page from forms packages by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Do NOT include administrator page with forms packages' - if 'Do NOT include administrator page with forms packages' shows '☒ selected '
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",


'form_font_options': """
Look for which font option is selected by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'9pt Times' - if '9pt Times' shows '☒ selected '
'8.5pt Arial' - if '8.5pt Arial' shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",


'drafting_preferences': """
Look for which drafting preference is selected by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Standard (single, ragged)' - if 'Standard (single, ragged)' shows '☒ selected '
'Single, right justified' - if 'Single, right justified' shows '☒ selected '
'Double, ragged' - if 'Double, ragged' shows '☒ selected '
'Double, right justified' - if 'Double, right justified' shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'spd_headers_footers': """
Look for whether to include SPD (8.5 x 11) headers/footers in SPD by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'No' - if 'No' shows '☒ selected '
'Yes Header for SPD: {text}' - if 'Yes' shows '☒ selected ' and 'Header for SPD' shows '☒ selected '
'Yes Footer for SPD: {text}' - if 'Yes' shows '☒ selected ' and 'Footer for SPD' shows '☒ selected '
'Yes Footer for SPD title page: {text}' - if 'Yes' shows '☒ selected ' and 'Footer for SPD title page' shows '☒ selected ' and custom text entered
'Yes Footer for SPD title page: same as footer at 2. above' - if 'Yes' shows '☒ selected ' and 'Footer for SPD title page' and 'same as footer at 2. above' show '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Any specified text for headers/footers
The text content is: {document_content}
""",

'spd_booklet_format': """
Look for SPD booklet format preferences by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'No' - if 'No' shows '☒ selected '
'Yes 9pt Times Booklet Cover Style I Heading: {text}' - if 'Yes', '9pt Times', and 'Booklet Cover Style I' show '☒ selected '
'Yes 9pt Times Booklet Cover Style II Heading: {text}' - if 'Yes', '9pt Times', and 'Booklet Cover Style II' show '☒ selected '
'Yes 9pt Times Booklet Cover Style III Heading: {text}' - if 'Yes', '9pt Times', and 'Booklet Cover Style III' show '☒ selected '
'Yes 9pt Times Booklet Cover Style IV Heading: {text}' - if 'Yes', '9pt Times', and 'Booklet Cover Style IV' show '☒ selected '
'Yes 9pt Times Booklet Cover Style V Heading: {text}' - if 'Yes', '9pt Times', and 'Booklet Cover Style V' show '☒ selected '
'Yes 8.5pt Arial Booklet Cover Style I Heading: {text}' - if 'Yes', '8.5pt Arial', and 'Booklet Cover Style I' show '☒ selected '
'Yes 8.5pt Arial Booklet Cover Style II Heading: {text}' - if 'Yes', '8.5pt Arial', and 'Booklet Cover Style II' show '☒ selected '
'Yes 8.5pt Arial Booklet Cover Style III Heading: {text}' - if 'Yes', '8.5pt Arial', and 'Booklet Cover Style III' show '☒ selected '
'Yes 8.5pt Arial Booklet Cover Style IV Heading: {text}' - if 'Yes', '8.5pt Arial', and 'Booklet Cover Style IV' show '☒ selected '
'Yes 8.5pt Arial Booklet Cover Style V Heading: {text}' - if 'Yes', '8.5pt Arial', and 'Booklet Cover Style V' show '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
"""

}


SUPPORTING_FORMS_INFORMATION_PROMPTS = {

'additional_contact_info': """
Look for additional contact information by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Employer (may only be selected with 19a or 19b1) Fax: {fax} Email: {email}' - if 'Employer (may only be selected with 19a or 19b1)' shows '☒ selected '

'Administrator (may only be selected with 19b2) Fax: {fax} Email: {email}' - if 'Administrator (may only be selected with 19b2)' shows '☒ selected '

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option 
- Any specified fax numbers after 'Fax:'
- Any specified email addresses after 'Email:'
The text content is: {document_content}
""",

'plan_expense_allocations': """
Look for what plan expenses may be assessed against participant accounts by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'No - not known or appendix will be completed later' - if 'No - not known or appendix will be completed later (skip to 197)' shows '☒ selected '

'Distribution following termination. Amount: ${amount}' - if 'Distribution following termination. Amount: ${amount}' shows '☒ selected '

'Limitation on small account distributions. The Plan will not charge any fee for processing a distribution if participant\'s vested account balance does not exceed ${amount}' - if this option shows '☒ selected '

'Installment distribution. Amount: ${amount}' - if 'Installment distribution. Amount: ${amount}' shows '☒ selected '

'Administrative processing fee to eliminate certain small account distributions' - if this option shows '☒ selected '

'Participant loan: Amount of application fee: ${amount}' - if 'Participant loan' and 'Amount of application fee' show '☒ selected '

'Participant loan: Amount of annual maintenance fee: ${amount}' - if 'Participant loan' and 'Amount of annual maintenance fee' show '☒ selected '

'QDRO. Amount: ${amount}' - if 'QDRO. Amount: ${amount}' shows '☒ selected '

'Hardship distribution. Amount: ${amount}' - if 'Hardship distribution. Amount: ${amount}' shows '☒ selected '

'In-service distribution. Amount: ${amount}' - if 'In-service distribution. Amount: ${amount}' shows '☒ selected '

'RMD. Amount: ${amount}' - if 'RMD. Amount: ${amount}' shows '☒ selected '

'Participant direction of investment: brokerage account option. Amount: ${amount}' - if this option shows '☒ selected '

'Benefit calculation. Amount: ${amount}' - if 'Benefit calculation. Calculation of benefits, including determination of substantially equal payments. Amount: ${amount}' shows '☒ selected '

'Terminated participants may incur a pro-rata share of the plan\'s expenses even though active participants are not charged this fee' - if this option shows '☒ selected '

'Other: {text}' - if any 'Other (describe)' option shows '☒ selected '

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Any specified amounts after 'Amount: $'
- Any specified text after 'Other (describe)'
The text content is: {document_content}
""",


'spd_cola_2021_limits': """
Look for whether to update SPD to include 2021 COLA limits (Note: The SPD currently reflects the 2020 dollar limitations on benefits and contributions) by checking for '☒ selected ' or '☐ unselected' before each option.
Return only one of the following values without any additional text:
'Regular 401(k) deferral limit: ${amount}' - if 'Yes, include amounts for the 2021 tax year as follows' and 'Regular 401(k) deferral limit: ${amount}' show '☒ selected '

'SIMPLE 401(k) deferral limit: ${amount}' - if 'Yes, include amounts for the 2021 tax year as follows' and 'SIMPLE 401(k) deferral limit: ${amount}' show '☒ selected '

'Regular 401(k) catch-up limit: ${amount}' - if 'Yes, include amounts for the 2021 tax year as follows' and 'Regular 401(k) catch-up limit: ${amount}' show '☒ selected '

'SIMPLE 401(k) catch-up limit: ${amount}' - if 'Yes, include amounts for the 2021 tax year as follows' and 'SIMPLE 401(k) catch-up limit: ${amount}' show '☒ selected '

'Annual compensation limit (401(a)(17)): ${amount}' - if 'Yes, include amounts for the 2021 tax year as follows' and 'Annual compensation limit (401(a)(17)): ${amount}' show '☒ selected '

'415 dollar limit: ${amount}' - if 'Yes, include amounts for the 2021 tax year as follows' and '415 dollar limit: ${amount}' show '☒ selected '

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Any specified amounts after '$'
The text content is: {document_content}
""",


'spd_optional_language': """
Look for whether to include optional SPD language by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Yes, include Spanish Text with Administrator Office Hours: {hours}' - if 'Yes, include the following' and 'Spanish Text' show '☒ selected ' and office hours are specified

'Yes, include Spanish Text' - if 'Yes, include the following' and 'Spanish Text. Include in introduction (refers participants to Administrator)' show '☒ selected ' with no office hours specified

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Any specified office hours after 'Administrator Office Hours'
The text content is: {document_content}
""",

'annual_notices_optional_language': """
Look for optional language to include in Annual Notices by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Effective Date of Notice: {date}' - if 'Effective Date of Notice: Fill in effective date of notice(s). Notice is effective for the forthcoming Plan Year beginning on:' shows '☒ selected '

'Cover Letter dated {date} Contact: {name}' - if 'Cover Letter' shows '☒ selected ' and both date and contact name are specified

'Cover Letter dated {date}' - if 'Cover Letter' shows '☒ selected ' and only date is specified

'Cover Letter Contact: {name}' - if 'Cover Letter' shows '☒ selected ' and only contact name is specified

'Cover Letter with Separate QDIA Letter dated {date} Contact: {name}' - if 'Cover Letter', 'Separate QDIA Letter', and both date and contact show '☒ selected '

'Cover Letter with Separate QDIA Letter' - if 'Cover Letter' and 'Separate QDIA Letter' show '☒ selected ' with no date or contact specified

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Specified date after 'effective for the forthcoming Plan Year beginning on:'
- Specified date after 'Cover letter should be dated as follows'
- Specified name after 'Include name of person to contact'
The text content is: {document_content}
""",

'loan_limitations': """
Look for what loan limitations apply by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'N/A. No limitations' - if 'N/A. No limitations' shows '☒ selected '
If 'The following limitations' shows '☒ selected ', combine all selected options with commas:

'The following limitations: Loans are participant-directed investment' - if 'The following limitations' and 'Loans are participant-directed investment' show '☒ selected '

'The following limitations: Loans only for hardship/financial necessity' - if 'The following limitations' and 'Loans only for hardship/financial necessity' show '☒ selected '

'The following limitations: Minimum loans of ${amount}' - if 'The following limitations' and 'Minimum loans of $____ (not more than $1,000)' show '☒ selected '

'The following limitations: Only {number} outstanding loan(s) per Participant' - if 'The following limitations' and 'Only ___ outstanding loan(s) per Participant' show '☒ selected '

'The following limitations: Loan balances due and payable upon distributable event' - if 'The following limitations' and 'Loan balances due and payable upon distributable event' show '☒ selected '

'The following limitations: Loan balances due upon termination of employment' - if 'The following limitations' and 'Loan balances due upon termination of employment' show '☒ selected '

'The following limitations: Loans are repaid by: payroll deduction' - if 'The following limitations', 'Loans are repaid by', and 'payroll deduction' show '☒ selected '

'The following limitations: Loans are repaid by: ACH' - if 'The following limitations', 'Loans are repaid by', and 'ACH' show '☒ selected '

'The following limitations: Loans are repaid by: check only for prepayment' - if 'The following limitations', 'Loans are repaid by', 'check', and 'only for prepayment' show '☒ selected '

'The following limitations: Loans are repaid by: check only for terminated employees' - if 'The following limitations', 'Loans are repaid by', 'check', and 'only for terminated employees' show '☒ selected '

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Any specified amounts, numbers or additional details
The text content is: {document_content}
""",

'loan_source_accounts': """
Look for which accounts loans may be made from by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'All Accounts' - if 'All Accounts' shows '☒ selected '

If 'From the following accounts only' shows '☒ selected ', combine all selected options with commas:
'From the following accounts only: {selected options}' - where selected options can include any combination of:
- 'Pre-Tax Elective Deferral Accounts' if shows '☒ selected '
- 'Roth Elective Deferral Accounts (may only be selected with 22b)' if shows '☒ selected '
- 'Matching Contribution Accounts (may only be selected with 22d)' if shows '☒ selected '
- 'Qualified Matching Accounts (includes Safe Harbor matching contributions)' if shows '☒ selected '
- 'Nonelective Contribution Accounts (may only be selected with 22e or 22f)' if shows '☒ selected '
- 'Qualified Nonelective Contribution Accounts (includes Safe Harbor nonelective contributions)' if shows '☒ selected '
- 'Rollover Accounts (may only be selected with 22h)' if shows '☒ selected '
- 'After-Tax Voluntary Contribution Accounts (may only be selected with 22g)' if shows '☒ selected '
- 'Other: {text}' if shows '☒ selected ' (replace {text} with specified text)

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Any specified text after 'Other'
The text content is: {document_content}
""",

'loan_limit_determination': """
Look for how loan limits will be determined by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'By determining the limits by only considering the restricted accounts' - if 'By determining the limits by only considering the restricted accounts' shows '☒ selected '
'By determining the limits taking into account a Participant\'s entire interest in the Plan' - if 'By determining the limits taking into account a Participant\'s entire interest in the Plan' shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'loan_interest_rate': """
Look for how loan interest rate is determined by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
If 'Loans will be granted at the following interest rate' shows '☒ selected ', combine all selected options with commas:
'Loans will be granted at: {percentage} percentage points over the prime interest rate' - if option 1 shows '☒ selected ' (replace {percentage} with specified number)
'Loans will be granted at: {rate}%' - if option 2 shows '☒ selected ' (replace {rate} with specified percentage)
'Loans will be granted at: the Administrator will establish the rate in a nondiscriminatory manner, based on a commercially reasonable rate of interest' - if option 3 shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Specified percentage points in option 1
- Specified rate percentage in option 2
The text content is: {document_content}
""",

'loan_refinancing': """
Look for whether loans may be refinanced by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Loans may be refinanced' - if 'Loans may be refinanced' shows '☒ selected '
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
""",

'eligible_rollover_sources': """
Look for which sources the Plan will accept direct rollovers from for eligible rollover distributions (only applies if Appendix for Rollovers was selected) by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'N/A--blank form provided; appendix to be completed later' - if 'N/A--blank form provided; appendix to be completed later' shows '☒ selected '

If 'The Plan will accept a direct rollover of an eligible rollover distribution from:' shows '☒ selected ', combine all selected sources with commas:
'Direct rollovers accepted from: {selected sources}' - where selected sources can include any combination of:
- 'qualified plan described in IRC §401(a), EXCLUDING after-tax employee contributions' if shows '☒ selected '
- 'qualified plan described in IRC §401(a), INCLUDING after-tax employee contributions (requires after-tax contributions allowed)' if shows '☒ selected '
- 'qualified plan described in IRC §403(a) (an annuity plan), EXCLUDING after-tax employee contributions' if shows '☒ selected '
- 'qualified plan described in IRC §403(a) (an annuity plan), INCLUDING after-tax employee contributions (requires after-tax contributions allowed)' if shows '☒ selected '
- 'annuity contract described in IRC §403(b) (a tax-sheltered annuity), EXCLUDING after-tax employee contributions' if shows '☒ selected '
- 'annuity contract described in IRC §403(b) (a tax-sheltered annuity), INCLUDING after-tax employee contributions (requires after-tax contributions allowed)' if shows '☒ selected '
- 'Roth elective deferral account from a qualified plan described in IRC §401(a) (requires Roth deferrals allowed)' if shows '☒ selected '
- 'Roth elective deferral account from a qualified plan described in IRC §403(b) (requires Roth deferrals allowed)' if shows '☒ selected '
- 'eligible plan under IRC §457(b) which is maintained by a governmental employer (governmental 457 plan)' if shows '☒ selected '

If 'Participant Rollover Contributions (other than direct rollovers) from Other Plans' shows '☒ selected ', combine all selected sources with commas:
'Participant rollovers accepted from: {selected sources}' - where selected sources can include any combination of:
- 'qualified plan described in IRC §401(a)' if shows '☒ selected '
- 'qualified plan described in IRC §403(a) (an annuity plan)' if shows '☒ selected '
- 'annuity contract described in IRC §403(b) (a tax-sheltered annuity)' if shows '☒ selected '
- 'eligible plan under IRC §457(b) which is maintained by a governmental employer' if shows '☒ selected '

'none' - if all options show '☐ unselected' or if Appendix for Rollovers not selected

Check for:
- '☒ selected ' or '☐ unselected' before each option
- This section only applies if Appendix for Rollovers was selected in question 192b5
- After-tax inclusions require after-tax contributions to be allowed (22g or 86h selected)
- Roth deferral rollovers require Roth deferrals to be allowed (22b3 selected)
The text content is: {document_content}
""",

'participant_rollover_from_iras': """
Look for whether Plan accepts participant rollover contributions from traditional IRAs by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'will' - if 'will' shows '☒ selected '
'will not' - if 'will not' shows '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- This specifically applies to rollovers from traditional IRAs only
The text content is: {document_content}
""",

'valuation_date_frequency': """
Look for whether and how frequently valuation dates are shown in SPD by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'No' - if 'No' shows '☒ selected '

If 'Yes' shows '☒ selected ', combine with the selected frequency:
'Yes: daily' - if 'Yes' and 'daily' show '☒ selected '
'Yes: semi-annually' - if 'Yes' and 'semi-annually' show '☒ selected '
'Yes: quarterly' - if 'Yes' and 'quarterly' show '☒ selected '
'Yes: other: {text}' - if 'Yes' and 'other' show '☒ selected ' (replace {text} with specified frequency)

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Specified text after 'other:'
- This determines if and how SPD shows valuation date frequency if more frequent than annually
The text content is: {document_content}
""",

'optional_index_information': """
Look for optional index information by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Include blank lines to enter amendment information' - if 'Include blank lines to enter amendment information' shows '☒ selected '
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
The text content is: {document_content}
"""
}

ADMINISTRATIVE_FORMS_PROMPTS = {

'deferral_elections_optional_language': """
Look for which optional language to include for Deferral Elections (applies only if automatic contribution arrangements are selected in questions 51a, 51b or 51c) by checking for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Lapse of Affirmative Elections. Affirmative deferral elections will lapse at the end of each Plan Year' - if this option shows '☒ selected '

If 'Voluntary Escalation of Affirmative Elections' shows '☒ selected ', combine applicable selections with commas:
'Voluntary Escalation: {selected options}' - where selected options include:
- 'Escalation amount: {percent}% of Compensation up to maximum of {max_percent}%' if option 1 shows '☒ selected '
- 'Escalation amount: {text}' if option 2 shows '☒ selected '
- 'Timing: first day of each Plan Year' if option 3 shows '☒ selected '
- 'Timing: anniversary of date of participation' if option 4 shows '☒ selected '
- 'Timing: {text}' if option 5 shows '☒ selected '
- 'Apply escalation in first period' if option 6 shows '☒ selected '

'Suspended Deferrals. A Participant\'s deferral election will NOT be treated as lapsing at the start of any suspension period' - if this option shows '☒ selected '

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Any specified percentages or text in blank spaces
- This section only applies if automatic contribution arrangements are selected (51a, 51b or 51c)
- Voluntary Escalation requires automatic contribution increase provisions (55b)
- Suspended Deferrals option requires hardship (108c) or qualified military service provisions (112d or 112f)
The text content is: {document_content}
""",

'spd_automatic_rollover_language': """
Look for whether to include optional language in SPD and Forms regarding automatic IRA rollovers for mandatory distributions. Note that this section:
1. Only applies if Plan provides for mandatory distributions exceeding $1,000
2. Should be skipped to 206c unless 103b1 is selected
3. Determines treatment of mandatory distributions under $1,000

Check for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Automatic IRA Rollover - amount. If no participant election is made, mandatory distributions of at least: ${amount} will be automatically rolled over to an IRA' - if this option shows '☒ selected ' (replace {amount} with specified amount which must be $1,000 or less)
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Specified dollar amount cannot exceed $1,000
- This section determines whether mandatory distributions under specified amount will be:
 * Automatically rolled over to an IRA if selected
 * Distributed in lump-sum if not selected
- Only applicable with mandatory distributions over $1,000 (103b1)
The text content is: {document_content}
""",

'distribution_election_form_ira_rollover': """
Look for whether to include automatic IRA rollover institution details in Distribution Election Form. Note that this section:
1. Determines if IRA institution details should be pre-filled or left blank for later completion
2. Applies to the financial institution that will establish automatic IRA rollovers
3. Requires both institution name and address if selected
4. Affects whether form comes with blank fields or specified institution details

Check for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Automatic IRA Rollover - issuer. Include name and address of the financial institution where the IRA will be established. Name: {name}, Address: {address}' - if this option shows '☒ selected ' (replace with specified institution details)
'none' - if option shows '☐ unselected' indicating distribution form will include blank fields for later completion

Check for:
- '☒ selected ' or '☐ unselected' before option
- Specified institution name after 'Name of IRA Institution:'
- Specified address after 'Address:'
- Impact on distribution form fields (pre-filled vs blank)
The text content is: {document_content}
""",


'spd_erisa_404c_compliance': """
Look for whether SPD should include ERISA 404(c) compliance description for participant-directed investments. Note that this section:

Check for '☒ selected ' or '☐ unselected' before the option.

Return only one of the following values without any additional text:
'ERISA 404(c). Yes, the SPD should describe that compliance with ERISA 404(c) is intended.' - if this option shows '☒ selected '
'none' - if option shows '☐ unselected' indicating no ERISA 404(c) compliance description will be included

Check for:
- '☒ selected ' or '☐ unselected' before the option
- Only applicable if participant investment directions are allowed (90b selected)
- Affects how SPD describes plan's intended ERISA 404(c) compliance status
The text content is: {document_content}
""",


'spd_special_trustee_contact': """
Look for Special Trustee contact information to include in SPD for duty to collect. Note that this section:
1. Only applies if Special Trustee was specified in question 20e
2. Requires Special Trustee title if selected
3. Determines which contact information to use for Special Trustee

Check for:
- '☒ selected ' or '☐ unselected' before title option
- '☒ selected ' or '☐ unselected' before contact information options
- Any specified contact details if option 3 selected

Return only one of the following values without any additional text:
'Special Trustee Title: {title}, Use Employer address and telephone number' - if title provided and option 1 shows '☒ selected '

'Special Trustee Title: {title}, Use Trustee address and telephone number' - if title provided and option 2 shows '☒ selected '

'Special Trustee Title: {title}, Use address: {street}, {city}, {state} {zip}, Telephone: {phone}' - if title provided and option 3 shows '☒ selected ' (replace with specified contact details)

'none' - if options show '☐ unselected' or section not applicable (20e not selected)

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Specified title after 'Special Trustee Title:'
- Complete address and phone details if option 3 selected
- Only applicable if Special Trustee specified in 20e
The text content is: {document_content}
""",

'trust_agreement_details': """
Look for Trust Agreement specifications regarding Custodian and Applicable State Law. Note that this section:
1. Identifies if there's a Custodian
2. Determines which state law applies to the separate trust
3. Custodian details must be completed if insurance company arrangement (3a) is selected

Check for:
- '☒ selected ' or '☐ unselected' before Custodian option
- '☒ selected ' or '☐ unselected' before state law options
- Any specified text for Custodian and 'Other' state law option

Return only one of the following values without any additional text:
'Custodian: {name}' - if 'Custodian' shows '☒ selected ' (replace with specified name)

If 'Applicable State Law' shows '☒ selected ', combine with selected basis:
'Custodian: {name}, Applicable State Law: based on the Employer address and telephone number' - if option 1 shows '☒ selected '
'Custodian: {name}, Applicable State Law: based on the Trustee address and telephone number' - if option 2 shows '☒ selected '
'Custodian: {name}, Applicable State Law: based on the Insurer' - if option 3 shows '☒ selected '
'Custodian: {name}, Applicable State Law: Other: {specified_law}' - if option 4 shows '☒ selected '

'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Specified Custodian name if required (mandatory with 3a)
- Trustee address option only available if 20a1 selected
- Insurer option only available if 3a selected
- Any specified text for Other state law option
The text content is: {document_content}
""",

'additional_supporting_documents': """
Look for whether additional documents should be included in supporting forms package. Note that this section:
1. Is optional additional documentation
2. Allows up to three extra documents to be generated
3. Can include forms, amendments or other supporting materials

Check for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Document 1: {text}' - if 'Document 1' shows '☒ selected ' (replace with specified document name)
'Document 2: {text}' - if 'Document 2' shows '☒ selected ' (replace with specified document name)
'Document 3: {text}' - if 'Document 3' shows '☒ selected ' (replace with specified document name)
'Document 1: {text1}, Document 2: {text2}' - if both Document 1 and 2 show '☒ selected '
'Document 1: {text1}, Document 3: {text3}' - if both Document 1 and 3 show '☒ selected '
'Document 2: {text2}, Document 3: {text3}' - if both Document 2 and 3 show '☒ selected '
'Document 1: {text1}, Document 2: {text2}, Document 3: {text3}' - if all documents show '☒ selected '
'none' - if all options show '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before each option
- Specified document names/descriptions after each selected option
- Optional section - not required for form package completion
The text content is: {document_content}
""",

'assent_warning': """
Looking for whether user has acknowledged requirement to affirm terms and conditions in Question 2 before plan document can be built.
The question states: "Assent to Question 2 required. The plan document being requested will not be built by our system until you affirm the terms and conditions stated at Question 2"

Check for '☒ selected ' or '☐ unselected' before the option.

Return only one of the following values without any additional text:
'I understand that I must go back and complete Question 2 in order to build the plan document.' - if 'I understand that I must go back and complete Question 2 in order to build the plan document.' shows '☒ selected '
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before option
- Blocks document generation until acknowledged
The text content is: {document_content}
"""

}


GENERAL_PROMPTS = {

'language_version_release_date': """
Looking for which Language Version and Release Date is selected.
The question asks for the Language Version/Release Date selection.

Check for '☒ selected ' or '☐ unselected' before the option.

Return only one of the following values without any additional text:
'11.0 4/23/2020' - if '11.0 4/23/2020' shows '☒ selected '
'none' - if option shows '☐ unselected'

Check for:
- '☒ selected ' or '☐ unselected' before option
The text content is: {document_content}
""",

'optional_reporting_fields': """
Looking for which Optional Fields for Reporting Purposes are selected.
The question allows selection of various optional reporting fields including IDs, contacts, and dates.

Check for '☒ selected ' or '☐ unselected' before each option.

Return only one of the following values without any additional text:
'Reporting ID' - if 'Reporting ID' shows '☒ selected '
'Reporting Code' - if 'Reporting Code' shows '☒ selected '
'Reporting Status' - if 'Reporting Status' shows '☒ selected '
'Contact1 Name' - if 'Contact1 Name' shows '☒ selected '
'Contact1 Email Address' - if 'Contact1 Email Address' shows '☒ selected '
'Contact2 Name' - if 'Contact2 Name' shows '☒ selected '
'Contact2 Email Address' - if 'Contact2 Email Address' shows '☒ selected '
'Plan Termination Date' - if 'Plan Termination Date' shows '☒ selected '
'Reporting Other' - if 'Reporting Other' shows '☒ selected '

If multiple options show '☒ selected ', combine them with commas:
Example: 'Reporting ID, Contact1 Name, Contact1 Email Address'

'none' - if all options show '☐ unselected'



Check for:
- '☒ selected ' or '☐ unselected' before each option
- Multiple selections should be combined
The text content is: {document_content}
""",



}


# Example of how to compose prompts using common helpers
def build_prompt(base_prompt: str, common_prompt: str) -> str:
    """Combine a base prompt with a common helper prompt"""
    return f"""
    {base_prompt}
    
    {common_prompt}
    
    The text content is: {{document_content}}
    """