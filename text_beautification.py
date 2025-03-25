#text_beautification____________
import re
import logging
from typing import List, Optional, Dict, Tuple

class TextBeautifier:

    def __init__(self):
        self.indent_size = 4
        
        # Section number pattern definition
        self.section_number_pattern = r'\d+\.\d+'  # Matches patterns like 10.1, 214.0 etc.
        
        # Updated marker patterns to handle both circle and checkbox markers
        self.marker_patterns = {
            'option_markers': [
                (r'(?:^|\s)O(?:\s|$)', '☐ unselected'),    # O marker
                (r'(?:^|\s)○(?:\s|$)', '☐ unselected'),    # ○ marker (circle)
                (r'(?<=\s)·(?=\s)', '☒ selected'),         # · marker
                (r'(?<=\s)●(?=\s)', '☒ selected'),         # ● marker
                (r'(?:^|\s)☐(?:\s|$)', '☐ unselected'),    # Existing ☐ marker
                (r'(?:^|\s)☒(?:\s|$)', '☒ selected')       # Existing ☒ marker
            ],
            'text_indicators': [
                (":unselected:", ""),
                (":selected:", ""),
                (" - ", " "),
                ("( )", "")
            ]
        }

        # Updated replacements
        self.replacements = [
            (" · ", " ☒ selected "),
            (" ● ", " ☒ selected "),
            (" ○ ", " ☐ unselected "),
            ("☐", " ☐ unselected"),     # Handle existing checkbox
            ("☒", " ☒ selected"),       # Handle existing selected checkbox
            (":unselected:", ""),
            (":selected:", ""),
            (" - ", " "),
            ("( )", "")
        ]
        
        # Question patterns
        self.question_patterns = {
            'numbered': r'\d+\.\d+\s+[A-Z].*\?',
            'sub_numbered': r'\d+\.\d+[a-z].*\?',
            'general': r'\d+\.\d+\s+.*\?',
            'any': r'.*\?\s*$'
        }
        
        # Value patterns
        self.value_patterns = {
            'date': r'_{3,}\s*\(((?:MM)?(?:DD)?(?:YYYY)?|month|day|year|month day|month day year)\)\s*([A-Za-z0-9\s,]*)',
            'number': r'_{3,}\s*\((?:number|amount)\)\s*(\d[\d,\.]*)',
            'text': r'_{3,}\s*\((.*?)\)\s*([A-Za-z0-9\s,\.]*)',
            'simple_field': r'_{3,}',  # For simple underscored fields
            'option': r'([○●☐☒])\s*([a-z]\.)\s*(.*?)(?=(?:[○●☐☒]|\n|$))'
        }
        
        # Address field patterns - added for processing address fields in curly brackets
        self.address_fields = [
            "state", "street", "city", "phone", "zip", "ein"
        ]

    
    def fix_broken_words(self, text: str) -> str:
        """Fix words that have been incorrectly split with spaces around 'o'"""
        # Handle cases with spaces
        text = re.sub(r'([a-z])\s+o\s+([a-z])', r'\1o\2', text, flags=re.IGNORECASE)
        # Handle cases with punctuation
        text = re.sub(r'([a-z])\s*o\s*([.,;])\s*([a-z])', r'\1o\2\3', text, flags=re.IGNORECASE)
        return text
    
    def process_address_fields(self, text: str) -> str:
        """Process address fields in curly brackets and add colon"""
        # Create a pattern that matches any of the address fields in curly brackets
        pattern = r'\(({})\)'.format('|'.join(self.address_fields))
        
        def replace_address_field(match):
            field = match.group(1)
            return field.capitalize() + ": "
        
        return re.sub(pattern, replace_address_field, text, flags=re.IGNORECASE)


    def standardize_selection_markers(self, text: str) -> str:
        """Enhanced selection marker standardization"""
        # First fix any broken words
        text = self.fix_broken_words(text)
        
        # Process address fields in curly brackets
        text = self.process_address_fields(text)
        
        # Handle all types of markers
        for old, new in self.replacements:
            text = text.replace(old, new)
        
        # Clean up duplicates and spacing
        text = re.sub(r'(?:unselected\s+){2,}', 'unselected', text)
        text = re.sub(r'(?:selected\s+){2,}', 'selected', text)
        text = re.sub(r'☐\s+unselected', '☐ unselected', text)
        text = re.sub(r'☒\s+selected', '☒ selected', text)
        
        # Ensure space after markers
        text = re.sub(r'(☐ unselected|☒ selected)([^\s])', r'\1 \2', text)
        
        # Handle form fields
        text = re.sub(r'_{3,}\s*\((.*?)\)', ' _____', text)
        text = re.sub(r'_{3,}', ' _____', text)
        
        # Clean up any resulting multiple spaces
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()

    

    def process_value_fields(self, text: str) -> str:
        """Process fields with underscores and values"""
        for pattern_type, pattern in self.value_patterns.items():
            if pattern_type == 'option':
                continue
                
            matches = re.finditer(pattern, text)
            for match in matches:
                if pattern_type == 'date':
                    field_type, value = match.groups()
                else:
                    value = match.group(1)
                
                if value and value.strip():
                    # Replace underscores and parenthetical with just the value
                    text = text.replace(match.group(0), value.strip())
                else:
                    # Remove empty fields
                    text = text.replace(match.group(0), '')
        
        return text


    def process_question_structure(self, text: str) -> str:
        """Process complex question structures"""
        lines = text.split('\n')
        processed_lines = []
        current_question = None
        indentation_level = 0
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Handle question numbers
            if re.match(r'^\d+\.\d+\s+', line):
                if current_question:
                    processed_lines.append('')
                current_question = line
                indentation_level = 0
                processed_lines.append(line)
                continue
            
            # Handle options with values
            if re.match(r'^[○●☐☒]\s*[a-z]\.', line):
                line = self.process_value_fields(line)
                line = ' ' * (self.indent_size * indentation_level) + line
                processed_lines.append(line)
                indentation_level = 1
                continue
            
            # Handle sub-options
            if re.match(r'^\d+\.', line) and indentation_level > 0:
                line = self.process_value_fields(line)
                line = ' ' * (self.indent_size * indentation_level) + line
                processed_lines.append(line)
                continue
            
            # Regular text
            if current_question:
                line = ' ' * (self.indent_size * indentation_level) + line
            processed_lines.append(line)
        
        return '\n'.join(processed_lines)



    def clean_text(self, text: str) -> str:
        """Enhanced text cleaning"""
        if not text:
            return ""
            
        try:
            # Basic cleanup
            text = text.replace("(one)", "")
            text = text.replace(":un:", "")
            
            # Process address fields
            text = self.process_address_fields(text)
            
            # Process markers and structure
            text = self.standardize_selection_markers(text)
            text = self.process_question_structure(text)
            
            # Clean up lines
            lines = []
            current_line = ""
            
            for line in text.split('\n'):
                line = line.strip()
                if not line:
                    if current_line:
                        lines.append(current_line)
                        current_line = ""
                    continue
                
                # Question check
                question_match = re.match(r'(\d+\.\d+\s+)(.*)', line)
                if question_match:
                    if current_line:
                        lines.append(current_line)
                    current_line = line
                    continue
                
                # Selection marker check (handle both types)
                if any(marker in line for marker in ['☐ unselected', '☒ selected']):
                    if current_line:
                        lines.append(current_line)
                    current_line = line
                else:
                    if current_line:
                        current_line = f"{current_line} {line}"
                    else:
                        current_line = line
            
            if current_line:
                lines.append(current_line)
            
            return '\n'.join(lines)
        
        except Exception as e:
            logging.error(f"Error in clean_text: {str(e)}")
            return text

    def calculate_indent_level(self, line: str) -> int:
        """Enhanced indentation calculation"""
        stripped = line.strip()
        indent_level = 0
        
        # No indent for sections/questions
        if re.match(self.section_number_pattern, stripped):
            return 0
        
        # Handle options
        if stripped.startswith(('a.', 'b.', 'c.', 'd.', 'e.', 'f.')):
            indent_level = 1
        
        # Handle suboptions
        if re.match(r'^\d+\.', stripped):
            indent_level = 2
        
        # Handle selection markers
        if stripped.startswith(('☐', '☒')):
            indent_level = 1
        
        return indent_level

    def beautify_text(self, text: str) -> str:
        """Main beautification method"""
        if not text:
            return ""
        
        try:
            # Process text
            text = self.clean_text(text)
            
            # Format lines
            formatted_lines = []
            prev_line_empty = True
            
            for line in text.split('\n'):
                if not line.strip():
                    if not prev_line_empty:
                        formatted_lines.append('')
                    prev_line_empty = True
                    continue
                
                stripped = line.strip()
                
                # Add space before questions
                if re.match(r'^\d+\.\d+\s+', stripped) and not prev_line_empty:
                    formatted_lines.append('')
                
                # Calculate indentation
                indent_level = self.calculate_indent_level(line)
                formatted_line = ' ' * (self.indent_size * indent_level) + stripped
                formatted_lines.append(formatted_line)
                
                prev_line_empty = False
            
            result = '\n'.join(formatted_lines)
            
            # Print the result to console for debugging
            #print("--- Result from beautify_text ---")
            #print(result[:200] + "..." if len(result) > 200 else result)
            
            # Write to file with safer approach
            try:
                # Create a safe version for writing
                safe_result = ""
                for char in result:
                    if ord(char) < 128:  # ASCII only
                        safe_result += char
                    else:
                        # Replace special characters
                        if char == '☐':
                            safe_result += "[UNCHECKED]"
                        elif char == '☒':
                            safe_result += "[CHECKED]"
                        else:
                            safe_result += "?"
                
                # Write the full text to file 
                # with open('output_test.txt', 'w', encoding='utf-8') as file:
                #     file.write(safe_result)
                #     file.flush()
                
                # print(f"Successfully wrote {len(safe_result)} characters to output_test.txt")
                
                # # Also save with different encoding as backup
                # with open('output_backup.txt', 'a', encoding='cp1252', errors='replace') as file:
                #     file.write(result)
                #     file.flush()
                
                # print(f"Also wrote backup file with Windows encoding")
                
            except Exception as file_error:
                print(f"Error writing to file: {str(file_error)}")
            
            return result
            
        except Exception as e:
            logging.error(f"Error in beautify_text: {str(e)}")
            print(f"Error in beautify_text: {str(e)}")
            return f"Error beautifying text: {str(e)}"   