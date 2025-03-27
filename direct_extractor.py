#direct_extractor.py


import re
import logging
from typing import Dict

class DirectInfoExtractor:
    """Class for directly extracting information from document text using regex patterns"""
    
    def __init__(self):
        self.logger = logging.getLogger("direct_extractor")
    
    def extract_employer_info(self, text):
        """Extract employer information directly using regex patterns"""
        try:
            employer_info = {}
            
            # Extract employer name
            employer_name_patterns = [
                # Original patterns
                r'1\.2\s+EMPLOYER\'S\s+NAME.*?(?:a\.|[aA])\.\s*([\w\s,\.&\-\']+?)(?:\s*\n|$|\s*b\.)',
                r'EMPLOYER.*?NAME.*?(?:a\.|[aA])\.\s*([\w\s,\.&\-\']+?)(?:\s*\n|$|\s*b\.)',
                r'Employer\'s\s+Name:?\s*([\w\s,\.&\-\']+?)(?:\s*\n|$)',
                # New patterns for the different format (5.0)
                r'5\.0\s+Employer\'s\s+Name.*?(?:a\.|[aA])\.\s*([\w\s,\.&\-\']+?)(?:\s*\n|$|\s*b\.)'
            ]
            self._extract_field_with_validation(text, employer_info, 'employer_name', employer_name_patterns)
            
            # Extract street address
            street_patterns = [
                # Original patterns
                r'Street:\s*([\w\s\d,\.#\-\']+?)(?:\s*\n|$|\s*(?:City:|d\.))',
                r'(?:c\.|[cC])\.\s*Street:\s*([\w\s\d,\.#\-\']+?)(?:\s*\n|$|\s*(?:City:|d\.))',
                # New patterns for address in different format (8.0)
                r'8\.0.*?(?:a\.|[aA])\.\s*\(Street\)\s*([\w\s\d,\.#\-\']+?)(?:\s*\n|$)',
                r'\(Street\)\s*([\w\s\d,\.#\-\']+?)(?:\s*\n|$)'
            ]
            self._extract_field_with_validation(text, employer_info, 'street', street_patterns)
            
            # Extract city
            city_patterns = [
                # Original patterns
                r'City:\s*([\w\s\-\']+?)(?:\s*\n|$|\s*(?:State:|e\.))',
                r'(?:d\.|[dD])\.\s*City:\s*([\w\s\-\']+?)(?:\s*\n|$|\s*(?:State:|e\.))',
                # New patterns for city in different format
                r'(?:b\.|[bB])\.\s*\(City\)\s*([\w\s\-\']+?)(?:\s*\n|$)',
                r'\(City\)\s*([\w\s\-\']+?)(?:\s*\n|$)'
            ]
            self._extract_field_with_validation(text, employer_info, 'city', city_patterns)
            
            # Extract state
            state_patterns = [
                # Original patterns
                r'State:\s*([\w\s\-\']+?)(?:\s*\n|$|\s*(?:Zip:|f\.))',
                r'(?:e\.|[eE])\.\s*State:\s*([\w\s\-\']+?)(?:\s*\n|$|\s*(?:Zip:|f\.))',
                # New patterns for state in different format
                r'(?:c\.|[cC])\.\s*\(State\)\s*([\w\s\-\']+?)(?:\s*\n|$)',
                r'\(State\)\s*([\w\s\-\']+?)(?:\s*\n|$)',
                # Principal Office state pattern
                r'6\.0.*?(?:a\.|[aA])\.\s*\(State\)\s*([\w\s\-\']+?)(?:\s*\n|$)'
            ]
            self._extract_field_with_validation(text, employer_info, 'state', state_patterns)
            
            # Extract zip
            zip_patterns = [
                # Original patterns
                r'Zip:\s*(\d[\d\-]+)(?:\s*\n|$|\s*(?:Telephone:|g\.))',
                r'(?:f\.|[fF])\.\s*Zip:\s*(\d[\d\-]+)(?:\s*\n|$|\s*(?:Telephone:|g\.))',
                # New patterns for zip in different format
                r'(?:d\.|[dD])\.\s*\(Zip\)\s*(\d[\d\-]+)(?:\s*\n|$)',
                r'\(Zip\)\s*(\d[\d\-]+)(?:\s*\n|$)'
            ]
            self._extract_field_with_validation(text, employer_info, 'zip', zip_patterns)
            
            # Extract phone
            phone_patterns = [
                # Original patterns
                r'Telephone:\s*([\d\-\(\)\s\.]+?)(?:\s*\n|$|\s*(?:Tax|h\.))',
                r'(?:g\.|[gG])\.\s*Telephone:\s*([\d\-\(\)\s\.]+?)(?:\s*\n|$|\s*(?:Tax|h\.))',
                # New patterns for phone in different format
                r'(?:e\.|[eE])\.\s*Telephone\s*([\d\-\(\)\s\.]+?)(?:\s*\n|$)',
                # Direct pattern for telephone
                r'Telephone\s+([\d\-\(\)\s\.]+?)(?:\s*\n|$)'
            ]
            self._extract_field_with_validation(text, employer_info, 'phone', phone_patterns)
            
            # If phone is still NA, try looking for phone numbers directly
            if employer_info.get('phone') == 'NA':
                # Look for common phone number patterns (XXX-XXX-XXXX)
                phone_pattern = r'\b(\d{3}-\d{3}-\d{4})\b'
                match = re.search(phone_pattern, text)
                if match:
                    employer_info['phone'] = match.group(1)
            
            # Extract EIN
            ein_patterns = [
                # Original patterns
                r'Tax(?:payer)?\s+Identification\s+Number(?:\s*\(TIN\))?:\s*(\d[\d\-]+)(?:\s*\n|$)',
                r'(?:h\.|[hH])\.\s*Tax(?:payer)?\s+Identification\s+Number(?:\s*\(TIN\))?:\s*(\d[\d\-]+)(?:\s*\n|$)',
                # New patterns for EIN in different format
                r'9\.0\s+Employer\'s\s+ID\s+\(EIN\).*?(?:a\.|[aA])\.\s*(\d[\d\-]+)(?:\s*\n|$)',
                r'Employer\'s\s+ID\s+\(EIN\).*?(?:a\.|[aA])\.\s*(\d[\d\-]+)(?:\s*\n|$)',
                # Direct pattern for EIN
                r'(?:EIN|TIN)(?:\s*\([^\)]+\))?(?::|\.|\s)\s*(\d{2}-\d{7})'
            ]
            self._extract_field_with_validation(text, employer_info, 'ein', ein_patterns)
            
            # If EIN is still NA, try looking for EIN directly
            if employer_info.get('ein') == 'NA':
                # Look for common EIN pattern (XX-XXXXXXX)
                ein_pattern = r'\b(\d{2}-\d{7})\b'
                match = re.search(ein_pattern, text)
                if match:
                    employer_info['ein'] = match.group(1)
            
            
            # Extract Employer's Fiscal Year End
            fiscal_year_patterns = [
                r'Employer\'s\s+Fiscal\s+Year\s+[Ee]nds:?\s*(\d{1,2}\/\d{1,2})(?:\s*\n|$|\s+\d)',
                r'Fiscal\s+Year\s+[Ee]nds:?\s*(\d{1,2}\/\d{1,2})(?:\s*\n|$|\s+\d)',
                r'(?:i\.|[iI])\.\s*(?:Employer\'s\s+)?Fiscal\s+Year\s+[Ee]nds:?\s*(\d{1,2}\/\d{1,2})(?:\s*\n|$|\s+\d)',
                r'(?:i\.|[iI])\.\s*(\d{1,2}\/\d{1,2})(?:\s*\n|$|\s+\d)'  # For "i. MM/DD" format
            ]

            self._extract_field_with_validation(text, employer_info, 'fiscal_year_end', fiscal_year_patterns)

            # If fiscal_year_end is still NA or contains unwanted text, try more precise patterns
            if employer_info.get('fiscal_year_end') == 'NA' or len(employer_info.get('fiscal_year_end', '').split()) > 1:
                # Extract just the MM/DD pattern without additional text
                date_pattern = re.compile(r'(\d{1,2}\/\d{1,2})')
                
                # First look in the context of "Fiscal Year ends"
                fiscal_year_text = re.search(r'Fiscal\s+Year\s+[Ee]nds.*?(?:\n|$)', text, re.IGNORECASE | re.DOTALL)
                if fiscal_year_text:
                    date_match = date_pattern.search(fiscal_year_text.group(0))
                    if date_match:
                        employer_info['fiscal_year_end'] = date_match.group(1)
                
                # If still not found or contains unwanted text, look after "i."
                if employer_info.get('fiscal_year_end') == 'NA' or len(employer_info.get('fiscal_year_end', '').split()) > 1:
                    i_text = re.search(r'(?:i\.|[iI])\..*?(?:\n|$)', text)
                    if i_text:
                        date_match = date_pattern.search(i_text.group(0))
                        if date_match:
                            employer_info['fiscal_year_end'] = date_match.group(1)
                
                # If we have a fiscal_year_end but it contains additional text, clean it
                if employer_info.get('fiscal_year_end') != 'NA' and len(employer_info.get('fiscal_year_end', '').split()) > 1:
                    # Extract just the MM/DD pattern
                    date_match = date_pattern.search(employer_info.get('fiscal_year_end', ''))
                    if date_match:
                        employer_info['fiscal_year_end'] = date_match.group(1)
            
            # Try additional extraction methods if fields are still missing
            self._extract_from_address_block(text, employer_info)
            
            # Clean up all extracted values
            self._cleanup_extracted_values(employer_info)
            
            return employer_info
            
        except Exception as e:
            self.logger.error(f"Error in extract_employer_info: {str(e)}")
            return {
                'employer_name': 'NA',
                'street': 'NA',
                'city': 'NA',
                'state': 'NA',
                'zip': 'NA',
                'phone': 'NA',
                'ein': 'NA',
                'fiscal_year_end': 'NA'
            }
    
    def _extract_field_with_validation(self, text, result_dict, field_name, patterns):
        """Extract field using patterns with validation to avoid marker-only matches"""
        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match and match.group(1).strip():
                value = match.group(1).strip()
                # Validate: Skip if it's just a letter marker or single digit
                if not re.match(r'^[a-zA-Z0-9]\.?$', value):
                    result_dict[field_name] = value
                    return
        
        # If not found, set to NA
        result_dict[field_name] = 'NA'
    
    def _extract_from_address_block(self, text, result_dict):
        """Try to extract missing fields from an address block pattern"""
        # Look for address block with all components
        address_block_patterns = [
            # Original format
            r'(?:Street|Address)[^\n]*?([\w\s\d,\.#\-\']+)[^\n]*?(?:City|,)[^\n]*?([\w\s\-\']+)[^\n]*?(?:State|,)[^\n]*?([\w\s\-\']+)[^\n]*?(?:Zip|,)[^\n]*?(\d[\d\-]+)',
            # New format with 8.0 Address section
            r'8\.0\s+Employer\'s\s+Address.*?\(Street\)[^\n]*?([\w\s\d,\.#\-\']+)[^\n]*?\(City\)[^\n]*?([\w\s\-\']+)[^\n]*?\(State\)[^\n]*?([\w\s\-\']+)[^\n]*?\(Zip\)[^\n]*?(\d[\d\-]+)'
        ]
        
        for pattern in address_block_patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                # Update missing fields
                if result_dict.get('street') == 'NA':
                    result_dict['street'] = match.group(1).strip()
                
                if result_dict.get('city') == 'NA':
                    city_value = match.group(2).strip()
                    if not re.match(r'^[a-zA-Z0-9]\.?$', city_value):  # Validate
                        result_dict['city'] = city_value
                
                if result_dict.get('state') == 'NA':
                    state_value = match.group(3).strip()
                    if not re.match(r'^[a-zA-Z0-9]\.?$', state_value):  # Validate
                        result_dict['state'] = state_value
                
                if result_dict.get('zip') == 'NA':
                    result_dict['zip'] = match.group(4).strip()
                
                # Once we find a match, exit the loop
                break
        
        # Try sequential extraction for address components
        self._extract_sequential_address_parts(text, result_dict)
    
    def _extract_sequential_address_parts(self, text, result_dict):
        """Extract address parts by looking at sequential letter markers"""
        # For original format
        if result_dict.get('city') == 'NA' or result_dict.get('state') == 'NA':
            sequence_pattern = r'[cC]\.\s*Street:.*?([dD]\.\s*City:.*?)([eE]\.\s*State:.*?)([fF]\.\s*Zip:)'
            match = re.search(sequence_pattern, text, re.DOTALL | re.IGNORECASE)
            
            if match:
                # Extract city if missing
                if result_dict.get('city') == 'NA':
                    city_part = match.group(1)
                    city_match = re.search(r'City:\s*([\w\s\-\']+)', city_part, re.IGNORECASE)
                    if city_match:
                        city_value = city_match.group(1).strip()
                        if not re.match(r'^[a-zA-Z0-9]\.?$', city_value):  # Validate
                            result_dict['city'] = city_value
                
                # Extract state if missing
                if result_dict.get('state') == 'NA':
                    state_part = match.group(2)
                    state_match = re.search(r'State:\s*([\w\s\-\']+)', state_part, re.IGNORECASE)
                    if state_match:
                        state_value = state_match.group(1).strip()
                        if not re.match(r'^[a-zA-Z0-9]\.?$', state_value):  # Validate
                            result_dict['state'] = state_value
        
        # For new format
        if result_dict.get('phone') == 'NA' or result_dict.get('ein') == 'NA':
            # Try to extract phone and EIN together
            sequence_pattern = r'8\.0.*?(?:e\.|[eE])\.\s*Telephone\s*([\d\-\(\)\s\.]+?)(?:\s*\n|$).*?9\.0.*?(?:a\.|[aA])\.\s*(\d{2}-\d{7})'
            match = re.search(sequence_pattern, text, re.DOTALL | re.IGNORECASE)
            
            if match:
                # Extract phone if missing
                if result_dict.get('phone') == 'NA':
                    phone_value = match.group(1).strip()
                    if not re.match(r'^[a-zA-Z0-9]\.?$', phone_value):  # Validate
                        result_dict['phone'] = phone_value
                
                # Extract EIN if missing
                if result_dict.get('ein') == 'NA':
                    ein_value = match.group(2).strip()
                    if not re.match(r'^[a-zA-Z0-9]\.?$', ein_value):  # Validate
                        result_dict['ein'] = ein_value


    def extract_effective_date(self, text: str) -> Dict[str, str]:
        """Extract both initial effective date and restatement date from plan admin section"""
        try:
            result = {}
            
            # Pattern to match effective date
            effective_date_patterns = [
                r'Initial\s+Effective\s+Date.*?\(enter\s+month\s+day,\s+year\).*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})',
                r'Initial\s+Effective\s+Date.*?(?:enter|month).*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})',
                r'Effective\s+Date.*?\(enter\s+month\s+day,\s+year\).*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})',
                r'6\.0\s+EFFECTIVE\s+DATE.*?a\.\s*\(enter\s+month\s+day,\s+year\).*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})'
            ]
            
            # Patterns for restatement date
            restatement_date_patterns = [
                r'This\s+restatement\s*\(month\)\s*\(day\)\s*\(year\)\s*([A-Za-z]+\s+\d{1,2},?\s*\d{4})',
                r'This\s+restatement.*?\((?:month|enter).*?\).*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})',
                r'This\s+restatement.*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})',
                r'restatement\s+date.*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})'
            ]
            
            # Initialize default values
            result['effective_date'] = 'NA'
            result['restatement_date'] = 'NA'
            
            # Try each effective date pattern
            for pattern in effective_date_patterns:
                match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
                if match:
                    effective_date = match.group(1).strip()
                    result['effective_date'] = effective_date
                    break
            
            # Try each restatement date pattern
            for pattern in restatement_date_patterns:
                match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
                if match:
                    restatement_date = match.group(1).strip()
                    result['restatement_date'] = restatement_date
                    break
            
            # If still not found, look for dates near specific sections
            sections = re.split(r'(\d+\.\d+)', text)
            for i, section in enumerate(sections):
                # Check for effective date
                if result['effective_date'] == 'NA' and "Effective Date" in section and i < len(sections) - 1:
                    # Check the next section for a date
                    next_section = sections[i+1]
                    date_match = re.search(r'([A-Za-z]+\s+\d{1,2},?\s*\d{4})', next_section)
                    if date_match:
                        result['effective_date'] = date_match.group(1).strip()
                
                # Check for restatement date
                if result['restatement_date'] == 'NA' and "restatement" in section.lower() and i < len(sections) - 1:
                    # Check the current and next section for a date
                    combined_text = section + sections[i+1]
                    date_match = re.search(r'([A-Za-z]+\s+\d{1,2},?\s*\d{4})', combined_text)
                    if date_match:
                        result['restatement_date'] = date_match.group(1).strip()
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error extracting dates: {str(e)}")
            return {
                'effective_date': 'NA',
                'restatement_date': 'NA'
            }

    

    def extract_plan_year_dates(self, text: str) -> Dict[str, str]:
        """
        Extract plan year beginning and ending dates from the provided text.
        
        Args:
            self: Reference to the instance of the class
            text (str): The text containing plan year dates
            
        Returns:
            Dict[str, str]: Dictionary containing 'plan_year_dates' with extracted dates
        """
        result = {}
        try:
            # Pattern for beginning date - modified to skip dates inside parentheses
            begin_patterns = [
                r'beginning\s+on.*?\(month\s+day\).*?([A-Za-z]+\s+\d{1,2})(?!\s*\))',
                r'Begins.*?\(month\s+day\).*?([A-Za-z]+\s+\d{1,2})(?!\s*\))',
                r'beginning\s+on.*?\(month\s+day,?\s*year\).*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})(?!\s*\))',
                r'Begins.*?\(month\s+day,?\s*year\).*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})(?!\s*\))',
                r'beginning\s+on.*?d\.\s*\(enter\s+month\s+day,\s+year\).*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})(?!\s*\))',
                r'beginning\s+on.*?\(enter\s+month\s+day,?\s*year.*?\)(.+?)(?:and|1\.)',
                r'SHORT\s+PLAN\s+YEAR.*?beginning\s+on.*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})(?!\s*\))'
            ]

            # Pattern for ending date - modified to skip dates inside parentheses
            end_patterns = [
                r'ending\s+on.*?\(month\s+day\).*?([A-Za-z]+\s+\d{1,2})(?!\s*\))',
                r'Ends.*?\(month\s+day\).*?([A-Za-z]+\s+\d{1,2})(?!\s*\))',
                r'ending\s+on.*?\(month\s+day,?\s*year\).*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})(?!\s*\))',
                r'Ends.*?\(month\s+day,?\s*year\).*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})(?!\s*\))',
                r'and\s+ending\s+on:.*?\(enter\s+month\s+day,\s+year\).*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})(?!\s*\))',
                r'ending\s+on.*?1\.\s*and\s+ending\s+on:.*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})(?!\s*\))',
                r'ending\s+on:.*?([A-Za-z]+\s+\d{1,2},?\s*\d{4})(?!\s*\))'
            ]

            # Extract begin date
            begin_date = "NA"
            for pattern in begin_patterns:
                match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
                if match:
                    begin_date = match.group(1).strip()
                    begin_date = re.sub(r'[?☒☐].*$', '', begin_date).strip()
                    break

            # Extract end date
            end_date = "NA"
            for pattern in end_patterns:
                match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
                if match:
                    end_date = match.group(1).strip()
                    end_date = re.sub(r'[?☒☐].*$', '', end_date).strip()
                    break

            # Special case for sections with both dates - without relying on section number
            if begin_date == "NA" and end_date == "NA":
                short_plan_year_match = re.search(
                    r'SHORT\s+PLAN\s+YEAR.*?beginning\s+on.*?ending\s+on:', 
                    text, 
                    re.IGNORECASE | re.DOTALL
                )
                if short_plan_year_match:
                    section_text = short_plan_year_match.group(0)
                    dates = re.findall(
                        r'([A-Za-z]+\s+\d{1,2}(?:,?\s*\d{4})?)', 
                        section_text
                    )
                    if len(dates) >= 2:
                        begin_date = dates[0].strip()
                        end_date = dates[1].strip()
                    elif len(dates) == 1:
                        begin_date = dates[0].strip()

            result['plan_year_dates'] = f"Begin Date: {begin_date}, End Date: {end_date}"
            return result
        except Exception as e:
            print(f"Error extracting plan year dates: {str(e)}")
            return {'plan_year_dates': 'NA'}
    
    def _cleanup_extracted_values(self, result_dict):
        """Remove trailing standalone letters from all extracted values"""
        for field, value in result_dict.items():
            if value != 'NA':
                # Remove trailing single letter markers (a.,b.,c.,d., etc.)
                cleaned_value = re.sub(r'\s+[a-zA-Z]\.?$', '', value)
                result_dict[field] = cleaned_value