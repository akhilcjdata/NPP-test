#extraction_processor.py

import re
from typing import Dict, List, Optional, Tuple
import logging
from datetime import datetime

class ExtractionProcessor:
    def __init__(self):
        self.selection_patterns = [
            (r'☒\s*(.*?)(?=(?:☐|☒|\n|$))', 'checkbox'),
            (r'●\s*(.*?)(?=(?:○|●|\n|$))', 'circle'),
            (r':selected:\s*(.*?)(?=(?:\n|$))', 'text'),
            (r'(?<=\d\.\d\s*)([^☐☒\n]*?☒[^☐☒\n]*)', 'numbered'),
            (r'selected\s*(.*?)(?=(?:\n|unselected|$))', 'text_indicator')
        ]
        
        self.value_patterns = {
            'percentage': r'(\d+(?:\.\d+)?)\s*%',
            'currency': r'\$\s*(\d+(?:,\d{3})*(?:\.\d{2})?)',
            'number': r'\b(\d+(?:\.\d+)?)\b'
        }
        
        self.confidence_thresholds = {
            'high': 0.8,
            'medium': 0.6,
            'low': 0.4
        }

    def preprocess_text(self, text: str) -> str:
        """Preprocess text for better extraction"""
        try:
            # Normalize whitespace
            text = ' '.join(text.split())
            
            # Standardize selection markers
            text = text.replace('[ ]', '☐')
            text = text.replace('[x]', '☒')
            text = text.replace('[X]', '☒')
            text = text.replace('(*)', '●')
            text = text.replace('(x)', '☒')
            text = text.replace('(X)', '☒')
            
            # Clean up formatting
            text = re.sub(r'\s+', ' ', text)
            text = re.sub(r'\s*\n\s*', '\n', text)
            
            return text.strip()
            
        except Exception as e:
            logging.error(f"Error in preprocess_text: {str(e)}")
            return text

    def get_relevant_context(self, text: str, target: str, window_size: int = 200) -> str:
        """Extract relevant context around target text"""
        try:
            # Find the target location
            target_index = text.lower().find(target.lower())
            if target_index == -1:
                return text[:window_size]
            
            # Calculate window boundaries
            start = max(0, target_index - window_size // 2)
            end = min(len(text), target_index + window_size // 2)
            
            # Expand to complete sentences
            while start > 0 and text[start] not in '.!?\n':
                start -= 1
            while end < len(text) and text[end] not in '.!?\n':
                end += 1
                
            return text[start:end].strip()
            
        except Exception as e:
            logging.error(f"Error in get_relevant_context: {str(e)}")
            return text[:window_size]

    def calculate_confidence(self, selection: str, type_: str, context: str) -> float:
        """Calculate confidence score for extraction"""
        try:
            confidence = 0.0
            
            # Base confidence by type
            type_confidence = {
                'checkbox': 0.6,
                'circle': 0.6,
                'text': 0.4,
                'numbered': 0.5,
                'text_indicator': 0.4
            }
            confidence += type_confidence.get(type_, 0.3)
            
            # Check for supporting patterns
            if re.search(r'select|choose|mark|indicate', selection, re.I):
                confidence += 0.2
                
            # Check for standard formatting
            if re.match(r'^[a-z]\.\s+\w+', selection):
                confidence += 0.2
                
            # Check context relevance
            if selection.lower() in context.lower():
                confidence += 0.2
            
            return min(confidence, 1.0)
            
        except Exception as e:
            logging.error(f"Error in calculate_confidence: {str(e)}")
            return 0.0

    def preprocess_extract(self, text: str) -> List[Dict]:
        """Extract selections with preprocessing"""
        try:
            text = self.preprocess_text(text)
            selections = []
            
            for pattern, type_ in self.selection_patterns:
                matches = re.finditer(pattern, text, re.MULTILINE)
                for match in matches:
                    selection = match.group(1).strip()
                    if selection:
                        confidence = self.calculate_confidence(
                            selection, 
                            type_,
                            text
                        )
                        selections.append({
                            'text': selection,
                            'type': type_,
                            'confidence': confidence
                        })
            
            return sorted(selections, key=lambda x: x['confidence'], reverse=True)
            
        except Exception as e:
            logging.error(f"Error in preprocess_extract: {str(e)}")
            return []

    def extract_with_confidence(self, 
                              text: str, 
                              field: str, 
                              openai_extractor=None) -> Tuple[str, float]:
        """Extract information with confidence scoring"""
        try:
            # Get relevant context
            context = self.get_relevant_context(text, field)
            
            # Get initial matches
            selections = self.preprocess_extract(context)
            
            # Return high confidence match if found
            high_confidence = [s for s in selections 
                             if s['confidence'] >= self.confidence_thresholds['high']]
            if high_confidence:
                return high_confidence[0]['text'], high_confidence[0]['confidence']
            
            # Use OpenAI for low confidence or no matches
            if openai_extractor and (not selections or 
                selections[0]['confidence'] < self.confidence_thresholds['medium']):
                ai_response = openai_extractor.extract_information(
                    text=context,
                    prompt_template=self.get_enhanced_prompt(field),
                    max_tokens=100
                )
                print("ai_response----",ai_response)
                return ai_response, 0.7  # Base confidence for AI responses
            
            # Return best match if available
            if selections:
                return selections[0]['text'], selections[0]['confidence']
            
            return "", 0.0
            
        except Exception as e:
            logging.error(f"Error in extract_with_confidence: {str(e)}")
            return "", 0.0

    def get_enhanced_prompt(self, field: str) -> str:
        """Generate enhanced prompt for field"""
        return f"""
        Task: Extract selected options from plan document sections.
        
        Format Rules:
        - Selected options are marked with: ☒, ●, "selected", or similar indicators
        - Unselected options are marked with: ☐, ○, "unselected"
        - Numbers may appear like "1.0", "2.0", etc.
        
        Look for selections in these forms:
        1. Direct markers: "☒ selected a. 401(k) Plan"
        2. Text indicators: ":selected: Option B"
        3. Numbers with selections: "1.0 ☒ Plan Type"
        
        Field to extract: {field}
        
        Return ONLY the selected option text, without markers or numbers.
        
        Document Content: {{document_content}}
        """

    def validate_extraction(self, value: str, field_type: str) -> bool:
        """Validate extracted value against expected pattern"""
        try:
            patterns = {
                'percentage': r'^\d+(\.\d+)?%$',
                'currency': r'^\$\d+(,\d{3})*(\.\d{2})?$',
                'selection': r'.*(?:☒|●|selected).*',
                'text': r'^[A-Za-z0-9\s\.,\-\'\"]+$'
            }
            
            pattern = patterns.get(field_type, patterns['text'])
            return bool(re.match(pattern, value))
            
        except Exception as e:
            logging.error(f"Error in validate_extraction: {str(e)}")
            return False

    def compare_extractions(self, 
                          ppa_result: Tuple[str, float], 
                          cycle3_result: Tuple[str, float]) -> Tuple[str, str]:
        """Compare and validate extractions from both documents"""
        try:
            ppa_text, ppa_conf = ppa_result
            cycle3_text, cycle3_conf = cycle3_result
            
            # If both have high confidence, return as is
            if ppa_conf >= self.confidence_thresholds['high'] and \
               cycle3_conf >= self.confidence_thresholds['high']:
                return ppa_text, cycle3_text
            
            # If one has high confidence, try to validate other
            if ppa_conf >= self.confidence_thresholds['high']:
                cycle3_text = self.validate_against_reference(cycle3_text, ppa_text)
            elif cycle3_conf >= self.confidence_thresholds['high']:
                ppa_text = self.validate_against_reference(ppa_text, cycle3_text)
            
            return ppa_text, cycle3_text
            
        except Exception as e:
            logging.error(f"Error in compare_extractions: {str(e)}")
            return ppa_result[0], cycle3_result[0]

    def validate_against_reference(self, text: str, reference: str) -> str:
        """Validate and potentially correct text against a reference"""
        try:
            # If texts are similar enough, use reference format
            if self.calculate_similarity(text, reference) > 0.8:
                return reference
            return text
        except Exception as e:
            logging.error(f"Error in validate_against_reference: {str(e)}")
            return text

    def calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity between two texts"""
        try:
            # Simple word-based similarity
            words1 = set(text1.lower().split())
            words2 = set(text2.lower().split())
            
            intersection = len(words1.intersection(words2))
            union = len(words1.union(words2))
            
            return intersection / union if union > 0 else 0.0
            
        except Exception as e:
            logging.error(f"Error in calculate_similarity: {str(e)}")
            return 0.0