# key_phrases.py
import re


PLAN_ADMIN_PHRASES = {
    "plan_year": {
        "phrases": [
            "Plan Year",
            "SIMPLE 401(k) Plan",
            "calendar year",
            "52/53 week year"
        ],
        "context": {
            "question_identifiers": [
                "The calendar year",
                "Begins",
                "Ends",
                "Short Plan Year",
                "52/53 week year"
            ],
            "options": {
                "main_options": [
                    "a. The calendar year",
                    "b. Begins",
                    "c. 52/53 week year"
                ],
                "sub_options": {
                    "b": ["1. Ends"],
                    "c": ["1. Date nearest to"]
                }
            },
            "selection_markers": {
                "unselected": ["○", "☐"],
                "selected": ["●", "☒"]
            },
            "value_fields": {
                "date": r'_{3,}\s*\((month day)\)\s*([A-Za-z]+\s+\d{1,2})',  # Matches "June 1"
                "simple": r'_{3,}'
            }
        }
    },
    "effective_dates": {
        "phrases": [
            "Effective Date",
            "This restatement"
        ],
        "context": {
            "question_identifiers": [
                "This restatement",
                "(month) (day) (year)"
            ],
            "options": {
                "main_options": [
                    "b. This restatement"
                ]
            },
            "value_patterns": {
                "date": r'\(month\)\s*\(day\)\s*\(year\)\s*([A-Za-z0-9\s,]+)',
                "simple_date": r'[A-Za-z]+\s+\d+,\s+\d{4}'  # Matches "June 1, 2003"
            },
            "selection_markers": {
                "unselected": ["○", "☐"],
                "selected": ["●", "☒"]
            }
        }
    },
    "contribution_types": {
        "phrases": [
            "Elective Deferrals",
            "pre-tax salary reduction",
            "Roth salary reduction"
        ],
        "context": {
            "question_identifiers": [
                "Elective Deferrals",
                "pre-tax salary reduction",
                "Roth salary reduction",
                "In-plan Roth conversions"
            ],
            "options": {
                "main_options": [
                    "a. The Plan provides for pre-tax salary reduction contributions only",
                    "b. The Plan provides for both pre-tax and Roth salary reduction contributions"
                ],
            },
            "selection_markers": {
                "unselected": ["○", "☐"],
                "selected": ["●", "☒"]
            }
        }
    }
}

# Helper functions for key phrase processing
def find_question_context(text: str, phrases: list) -> dict:
    """Find the relevant question context based on key phrases"""
    result = {
        'found': False,
        'start_index': -1,
        'end_index': -1,
        'question_text': ''
    }
    
    # Look for any of the key phrases
    for phrase in phrases:
        index = text.find(phrase)
        if index != -1:
            # Found a phrase, now find question boundaries
            result['found'] = True
            result['start_index'] = index
            
            # Find question number before phrase
            start = text.rfind('\n', 0, index)
            if start != -1:
                result['start_index'] = start
            
            # Find end of question (next question number or section)
            end = text.find('\n', index)
            while end != -1:
                next_line = text[end+1:text.find('\n', end+1) if text.find('\n', end+1) != -1 else len(text)]
                if re.match(r'\d+\.\d+', next_line.strip()):
                    break
                end = text.find('\n', end+1)
            
            result['end_index'] = end if end != -1 else len(text)
            result['question_text'] = text[result['start_index']:result['end_index']].strip()
            break
    print("----",result)
    return result

def extract_selections(question_text: str, pattern: dict) -> dict:
    """Extract selections from question text"""
    selections = {
        'main_option': None,
        'sub_options': [],
        'values': {}
    }
    
    # Check if pattern has the required structure
    if not isinstance(pattern, dict) or 'context' not in pattern:
        return selections

    context = pattern['context']
    
    # Check for main options
    if 'options' in context and 'main_options' in context['options']:
        for option in context['options']['main_options']:
            # Look for selected markers
            for marker in context['selection_markers']['selected']:
                if f"{marker} {option}" in question_text:
                    selections['main_option'] = option
                    break
            if selections['main_option']:
                break
    
    # If main option found, look for its sub-options
    if selections['main_option'] and 'sub_options' in context['options']:
        option_letter = selections['main_option'][0]  # Get 'a', 'b', etc.
        if option_letter in context['options']['sub_options']:
            for sub_opt in context['options']['sub_options'][option_letter]:
                for marker in context['selection_markers']['selected']:
                    if f"{marker} {sub_opt}" in question_text:
                        selections['sub_options'].append(sub_opt)
                        # Look for values if they exist
                        if 'value_fields' in context:
                            for field_type, pattern in context['value_fields'].items():
                                value_match = re.search(pattern, question_text)
                                if value_match:
                                    selections['values'][sub_opt] = value_match.group(2)
    
    return selections
