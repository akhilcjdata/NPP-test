

#section_config.py
SECTIONS = {
    "document_info": {
        "name": "Document Information",
        "start": [
            "Section: Document Information",
            r"\d+\.\d+\s+(?:TYPE OF PLAN|DOCUMENT PACKAGE)",
            r"Section\s*[:|-]\s*Document\s+Information"
        ],
        "end": [
            "Section: Employer Information",
            r"Section\s*[:|-]\s*Employer\s+Information",
            r"\d+\.\d+\s+Employer"
        ]
    },

    "employer_info": {
        "name": "Employer Information",
        "start": [
            "Section: Employer Information",
            r"Section\s*[:|-]\s*Employer\s+Information",
            r"\d+\.\d+\s+Employer"
        ],
        "end": [
            "Section: Plan Administration",
            r"Section\s*[:|-]\s*Plan\s+Administration",
            r"\d+\.\d+\s+Plan\s+Administration"
        ]
    },

    "plan_admin": {
        "name": "Plan Administration",
        "start": [
            "Section: Plan Administration",
            r"Section\s*[:|-]\s*Plan\s+Administration",
            r"\d+\.\d+\s+Plan\s+Information"
        ],
        "end": [
            "Section: Contribution Types",
            r"Section\s*[:|-]\s*Contribution\s+Types",
            r"\d+\.\d+\s+Contribution"
        ]
    },

    "contribution_types": {
        "name": "Contribution Types",
        "start": [
            "Section: Contribution Types",
            r"Section\s*[:|-]\s*Contribution\s+Types",
            r"\d+\.\d+\s+Contribution"
        ],
        "end": [
            "Section: Service",
            r"Section\s*[:|-]\s*Service",
            r"\d+\.\d+\s+Service"
        ]
    },

    "service_types": {
        "name": "Service Types",
        "start": [
            "Section: Service",
            r"Section\s*[:|-]\s*Service",
            r"\d+\.\d+\s+Service"
        ],
        "end": [
            "Section: Eligibility",
            r"Section\s*[:|-]\s*Eligibility",
            r"\d+\.\d+\s+Eligibility"
        ]
    },

    "eligibility_types": {
        "name": "Eligibility Types",
        "start": [
            "Section: Eligibility",
            r"Section\s*[:|-]\s*Eligibility",
            r"\d+\.\d+\s+Eligibility"
        ],
        "end": [
            "Section: Vesting",
            r"Section\s*[:|-]\s*Vesting",
            r"\d+\.\d+\s+Vesting"
        ]
    },

    "vesting_types": {
        "name": "Vesting Types",
        "start": [
            "Section: Vesting",
            r"Section\s*[:|-]\s*Vesting",
            r"\d+\.\d+\s+Vesting"
        ],
        "end": [
            "Section: Compensation",
            r"Section\s*[:|-]\s*Compensation",
            r"\d+\.\d+\s+Compensation"
        ]
    },

    "compensation_types": {
        "name": "Compensation Types",
        "start": [
            "Section: Compensation",
            r"Section\s*[:|-]\s*Compensation",
            r"\d+\.\d+\s+Compensation"
        ],
        "end": [
            "Section: Contributions and Allocations",
            r"Section\s*[:|-]\s*Contributions\s+and\s+Allocations",
            r"\d+\.\d+\s+Contributions\s+and\s+Allocations"
        ]
    },

    "contribution_allocation_types": {
        "name": "Contribution Allocation Types",
        "start": [
            "Section: Contributions and Allocations",
            r"Section\s*[:|-]\s*Contributions\s+and\s+Allocations",
            r"\d+\.\d+\s+Contributions\s+and\s+Allocations"
        ],
        "end": [
            "Section: 401(k) Safe Harbor Contributions",
            r"Section\s*[:|-]\s*401\(k\)\s+Safe\s+Harbor",
            r"\d+\.\d+\s+(?:401\(k\)|401k)\s+Safe\s+Harbor"
        ]
    },

    "safe_harbor_types": {
        "name": "Safe Harbor Types",
        "start": [
            "Section: 401(k) Safe Harbor Contributions",
            r"Section\s*[:|-]\s*401\(k\)\s+Safe\s+Harbor",
            r"\d+\.\d+\s+(?:401\(k\)|401k)\s+Safe\s+Harbor"
        ],
        "end": [
            "Section: Matching Contributions on Elective Deferrals",
            "Section: Matching Contributions",
            r"Section\s*[:|-]\s*Matching\s+Contributions",
            r"\d+\.\d+\s+Matching\s+Contributions"
        ]
    },

    "matching_contribution_types": {
        "name": "Matching Contribution Types",
        "start": [
            "Section: Matching Contributions on Elective Deferrals",
            "Section: Matching Contributions",
            r"Section\s*[:|-]\s*Matching\s+Contributions",
            r"\d+\.\d+\s+Matching\s+Contributions"
        ],
        "end": [
            "Section: Nonelective Contributions",
            r"Section\s*[:|-]\s*Nonelective\s+Contributions",
            r"\d+\.\d+\s+Nonelective\s+Contributions"
        ]
    },

    "nonelective_contribution_types": {
        "name": "Nonelective Contribution Types",
        "start": [
            "Section: Nonelective Contributions",
            "Section: Nonelective Profit Sharing Contributions",
            r"Section\s*[:|-]\s*Nonelective(?:\s+Profit\s+Sharing)?\s+Contributions",
            r"\d+\.\d+\s+Nonelective(?:\s+Profit\s+Sharing)?\s+Contributions"
        ],
        "end": [
            "Section: Prevailing Wage Contribution",
            r"Section\s*[:|-]\s*Prevailing\s+Wage",
            r"\d+\.\d+\s+Prevailing\s+Wage"
        ]
    },

    # Continue with the same pattern for remaining sections...
    "prevailing_wage_contribution_types": {
        "name": "Prevailing Wage Contribution Types",
        "start": [
            "Section: Prevailing Wage Contribution",
            r"Section\s*[:|-]\s*Prevailing\s+Wage",
            r"\d+\.\d+\s+Prevailing\s+Wage"
        ],
        "end": [
            "Section: General Plan Provisions",
            r"Section\s*[:|-]\s*General\s+Plan\s+Provisions",
            r"\d+\.\d+\s+General\s+Plan\s+Provisions"
        ]
    },

    "general_plan_provision_contribution_types": {
        "name": "General Plan Provisions Contribution Types",
        "start": [
            "Section: General Plan Provisions",
            r"Section\s*[:|-]\s*General\s+Plan\s+Provisions",
            r"\d+\.\d+\s+General\s+Plan\s+Provisions"
        ],
        "end": [
            "Section: Retirement and Disability",
            r"Section\s*[:|-]\s*Retirement\s+and\s+Disability",
            r"\d+\.\d+\s+Retirement\s+and\s+Disability"
        ]
    },

    "retirement_and_distribution_contribution_types": {
        "name": "Retirement and Disability Contribution Types",
        "start": [
            "Section: Retirement and Disability",
            r"Section\s*[:|-]\s*Retirement\s+and\s+Disability",
            r"\d+\.\d+\s+Retirement\s+and\s+Disability"
        ],
        "end": [
            "Section: Distributions",
            r"Section\s*[:|-]\s*Distributions",
            r"\d+\.\d+\s+Distributions"
        ]
    },

    "distribution_contribution_types": {
        "name": "Distributions Contribution Types",
        "start": [
            "Section: Distributions",
            r"Section\s*[:|-]\s*Distributions",
            r"\d+\.\d+\s+Distributions"
        ],
        "end": [
            "Section: Other Elections",
            "Section: Other Permitted Elections",
            r"Section\s*[:|-]\s*Other\s+(?:Permitted\s+)?Elections",
            r"\d+\.\d+\s+Other\s+(?:Permitted\s+)?Elections"
        ]
    },

    "permitted_elections_types": {
        "name": "Permitted Election Contribution Types",
        "start": [
            "Section: Other Elections",
            "Section: Other Permitted Elections",
            r"Section\s*[:|-]\s*Other\s+(?:Permitted\s+)?Elections",
            r"\d+\.\d+\s+Other\s+(?:Permitted\s+)?Elections"
        ],
        "end": [
            "Section: Participating Employers",
            r"Section\s*[:|-]\s*Participating\s+Employers",
            r"\d+\.\d+\s+Participating\s+Employers"
        ]
    },

    "participating_employer_types": {
        "name": "Participating Employer Contribution Types",
        "start": [
            "Section: Participating Employers",
            r"Section\s*[:|-]\s*Participating\s+Employers",
            r"\d+\.\d+\s+Participating\s+Employers"
        ],
        "end": [
            "Section: Subsequent (Cycle 4) Legal Changes",
            "Section: Optional Updates",
            r"Section\s*[:|-]\s*(?:Subsequent.*Legal\s+Changes|Optional\s+Updates)",
            r"\d+\.\d+\s+(?:Subsequent|Optional)"
        ]
    },

    "subsequent_employer_types": {
        "name": "Subsequent (Cycle 4) Legal Changes/Optional Updates Contribution Types",
        "start": [
            "Section: Subsequent (Cycle 4) Legal Changes",
            "Section: Optional Updates",
            r"Section\s*[:|-]\s*(?:Subsequent.*Legal\s+Changes|Optional\s+Updates)",
            r"\d+\.\d+\s+(?:Subsequent|Optional)"
        ],
        "end": [
            "Section: Other Provisions",
            r"Section\s*[:|-]\s*Other\s+Provisions",
            r"\d+\.\d+\s+Other\s+Provisions"
        ]
    },

    "other_provision_employer_types": {
        "name": "Other Provisions Contribution Types",
        "start": [
            "Section: Other Provisions",
            r"Section\s*[:|-]\s*Other\s+Provisions",
            r"\d+\.\d+\s+Other\s+Provisions"
        ],
        "end": [
            "Section: Document Requests",
            r"Section\s*[:|-]\s*Document\s+Requests",
            r"\d+\.\d+\s+Document\s+Requests"
        ]
    },

    "document_request_employer_types": {
        "name": "Document Request Contribution Types",
        "start": [
            "Section: Document Requests",
            r"Section\s*[:|-]\s*Document\s+Requests",
            r"\d+\.\d+\s+Document\s+Requests"
        ],
        "end": [
            "Section: Supporting Forms Information",
            r"Section\s*[:|-]\s*Supporting\s+Forms",
            r"\d+\.\d+\s+Supporting\s+Forms"
        ]
    },

    "supporting_forms_information_types": {
        "name": "Supporting Forms Contribution Types",
        "start": [
            "Section: Supporting Forms Information",
            r"Section\s*[:|-]\s*Supporting\s+Forms",
            r"\d+\.\d+\s+Supporting\s+Forms"
        ],
        "end": [
            "Section: Administrative Forms",
            r"Section\s*[:|-]\s*Administrative\s+Forms",
            r"\d+\.\d+\s+Administrative\s+Forms"
        ]
    },

    "administrative_forms_types": {
        "name": "Administrative Forms Contribution Types",
        "start": [
            "Section: Administrative Forms",
            r"Section\s*[:|-]\s*Administrative\s+Forms",
            r"\d+\.\d+\s+Administrative\s+Forms"
        ],
        "end": [
            "Section: General",
            r"Section\s*[:|-]\s*General",
            r"\d+\.\d+\s+General"
        ]
    },

    "general_types": {
        "name": "General Contribution Types",
        "start": [
            "Section: General",
            r"Section\s*[:|-]\s*General",
            r"\d+\.\d+\s+General"
        ],
        "end": ""
    }
}


# Section validation rules
SECTION_RULES = {
    "document_info": {
        "required_fields": ["TYPE OF PLAN", "DOCUMENT PACKAGE"],
        "min_length": 50,
        "max_length": 5000
    },
    "employer_info": {
        "required_fields": ["Employer", "Principal Office"],
        "min_length": 50,
        "max_length": 5000
    },
    "plan_admin": {
        "required_fields": ["Plan Information"],
        "min_length": 50,
        "max_length": 10000
    },
    "contribution_types": {
        "required_fields": ["Contribution"],
        "min_length": 50,
        "max_length": 10000
    },
    "service_types": {
        "required_fields": ["Service Crediting"],
        "min_length": 50,
        "max_length": 8000
    },
    "eligibility_types": {
        "required_fields": ["Eligibility"],
        "min_length": 50,
        "max_length": 8000
    },
    "vesting_types": {
        "required_fields": ["Vesting"],
        "min_length": 50,
        "max_length": 8000
    },
    "compensation_types": {
        "required_fields": ["Compensation"],
        "min_length": 50,
        "max_length": 8000
    },
    "contribution_allocation_types": {
        "required_fields": ["Contributions", "Allocations"],
        "min_length": 50,
        "max_length": 10000
    },
    "safe_harbor_types": {
        "required_fields": ["Safe Harbor", "Contributions"],
        "min_length": 50,
        "max_length": 10000
    },
    "matching_contribution_types": {
        "required_fields": ["Matching", "Contributions"],
        "min_length": 50,
        "max_length": 10000
    },
    "nonelective_contribution_types": {
        "required_fields": ["Nonelective", "Contributions"],
        "min_length": 50,
        "max_length": 10000
    },
    "prevailing_wage_contribution_types": {
        "required_fields": ["Prevailing Wage"],
        "min_length": 50,
        "max_length": 8000
    },
    "general_plan_provision_contribution_types": {
        "required_fields": ["General Plan Provisions"],
        "min_length": 50,
        "max_length": 10000
    },
    "retirement_and_distribution_contribution_types": {
        "required_fields": ["Retirement", "Disability"],
        "min_length": 50,
        "max_length": 10000
    },
    "distribution_contribution_types": {
        "required_fields": ["Distributions"],
        "min_length": 50,
        "max_length": 10000
    },
    "permitted_elections_types": {
        "required_fields": ["Elections"],
        "min_length": 50,
        "max_length": 8000
    },
    "participating_employer_types": {
        "required_fields": ["Participating Employers"],
        "min_length": 50,
        "max_length": 8000
    },
    "subsequent_employer_types": {
        "required_fields": ["Legal Changes", "Updates"],
        "min_length": 50,
        "max_length": 8000
    },
    "other_provision_employer_types": {
        "required_fields": ["Other Provisions"],
        "min_length": 50,
        "max_length": 8000
    },
    "document_request_employer_types": {
        "required_fields": ["Document Requests"],
        "min_length": 50,
        "max_length": 5000
    },
    "supporting_forms_information_types": {
        "required_fields": ["Supporting Forms"],
        "min_length": 50,
        "max_length": 5000
    },
    "administrative_forms_types": {
        "required_fields": ["Administrative Forms"],
        "min_length": 50,
        "max_length": 5000
    },
    "general_types": {
        "required_fields": ["General"],
        "min_length": 50,
        "max_length": 5000
    }
}

# Section relationships for context awareness
SECTION_RELATIONSHIPS = {
    "document_info": ["employer_info"],
    "employer_info": ["document_info", "plan_admin"],
    "plan_admin": ["employer_info", "contribution_types"],
    "contribution_types": ["plan_admin", "service_types"],
    "service_types": ["contribution_types", "eligibility_types"],
    "eligibility_types": ["service_types", "vesting_types"],
    "vesting_types": ["eligibility_types", "compensation_types"],
    "compensation_types": ["vesting_types", "contribution_allocation_types"],
    "contribution_allocation_types": ["compensation_types", "safe_harbor_types"],
    "safe_harbor_types": ["contribution_allocation_types", "matching_contribution_types"],
    "matching_contribution_types": ["safe_harbor_types", "nonelective_contribution_types"],
    "nonelective_contribution_types": ["matching_contribution_types", "prevailing_wage_contribution_types"],
    "prevailing_wage_contribution_types": ["nonelective_contribution_types", "general_plan_provision_contribution_types"],
    "general_plan_provision_contribution_types": ["prevailing_wage_contribution_types", "retirement_and_distribution_contribution_types"],
    "retirement_and_distribution_contribution_types": ["general_plan_provision_contribution_types", "distribution_contribution_types"],
    "distribution_contribution_types": ["retirement_and_distribution_contribution_types", "permitted_elections_types"],
    "permitted_elections_types": ["distribution_contribution_types", "participating_employer_types"],
    "participating_employer_types": ["permitted_elections_types", "subsequent_employer_types"],
    "subsequent_employer_types": ["participating_employer_types", "other_provision_employer_types"],
    "other_provision_employer_types": ["subsequent_employer_types", "document_request_employer_types"],
    "document_request_employer_types": ["other_provision_employer_types", "supporting_forms_information_types"],
    "supporting_forms_information_types": ["document_request_employer_types", "administrative_forms_types"],
    "administrative_forms_types": ["supporting_forms_information_types", "general_types"],
    "general_types": ["administrative_forms_types"]
}

def validate_section_config():
    """Validate the section configuration"""
    try:
        for section_key, section in SECTIONS.items():
            # Check required keys
            required_keys = ["name", "start", "end"]
            for key in required_keys:
                if key not in section:
                    raise KeyError(f"Missing required key '{key}' in section '{section_key}'")
            
            # Validate start and end markers
            if isinstance(section["start"], str):
                section["start"] = [section["start"]]
            if isinstance(section["end"], str):
                section["end"] = [section["end"]]
            
            if not isinstance(section["start"], list) or not isinstance(section["end"], list):
                raise TypeError(f"Start and end markers must be strings or lists in section '{section_key}'")
            
            # Validate rules if they exist
            if section_key in SECTION_RULES:
                rules = SECTION_RULES[section_key]
                if not isinstance(rules["required_fields"], list):
                    raise TypeError(f"Required fields must be a list in rules for section '{section_key}'")
                if not isinstance(rules["min_length"], int) or not isinstance(rules["max_length"], int):
                    raise TypeError(f"Length limits must be integers in rules for section '{section_key}'")
                if rules["min_length"] > rules["max_length"]:
                    raise ValueError(f"Min length cannot be greater than max length in rules for section '{section_key}'")
            
            # Validate relationships
            if section_key in SECTION_RELATIONSHIPS:
                if not isinstance(SECTION_RELATIONSHIPS[section_key], list):
                    raise TypeError(f"Relationships must be a list for section '{section_key}'")
                for related_section in SECTION_RELATIONSHIPS[section_key]:
                    if related_section not in SECTIONS:
                        raise ValueError(f"Invalid related section '{related_section}' in relationships for '{section_key}'")
        
        return True
    except Exception as e:
        print(f"Configuration validation error: {str(e)}")
        return False

# Validate configuration on import
if not validate_section_config():
    raise ValueError("Invalid section configuration")