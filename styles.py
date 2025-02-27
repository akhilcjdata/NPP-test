#styles.py

def get_user_custom_css(user_id=None):
    """Generate CSS with user-specific customizations"""
    user_id = user_id or 'default'
    
    return f"""
    <style>
        /* Global Styles */
        .stTitle {{
            font-size: 2.5rem !important;
            font-weight: bold !important;
            padding-bottom: 2rem !important;
        }}

        /* User-specific container */
        .user-container-{user_id} {{
            position: relative;
            padding: 10px;
            margin-bottom: 20px;
        }}

        /* Extracted Info Styles */
        .extracted-info {{
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #e6e6e6;
            margin: 15px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }}

        /* Section Headers */
        .section-header {{
            color: #1a73e8;
            font-size: 1.3em;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 2px solid #1a73e8;
            font-weight: 500;
        }}

        /* Information Display */
        .info-label {{
            font-weight: 500;
            color: #202124;
            margin-top: 10px;
        }}

        .info-value {{
            margin-left: 8px;
            color: #3c4043;
            padding: 4px 0;
        }}

        /* Button Styling */
        .stButton > button {{
            background-color: #1a73e8;
            color: white;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            font-weight: 500;
            transition: background-color 0.3s ease;
        }}

        .stButton > button:hover {{
            background-color: #1557b0;
        }}

        /* Upload Area Styling */
        .uploadedFile {{
            border: 2px dashed #1a73e8;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            background: #f8f9fa;
            transition: border-color 0.3s ease;
        }}

        .uploadedFile:hover {{
            border-color: #1557b0;
        }}

        /* Progress Indicators */
        .progress-bar-{user_id} {{
            height: 4px;
            background-color: #e0e0e0;
            border-radius: 2px;
            margin: 10px 0;
        }}

        .progress-fill-{user_id} {{
            height: 100%;
            background-color: #1a73e8;
            border-radius: 2px;
            transition: width 0.3s ease;
        }}

        /* Status Indicators */
        .status-indicator {{
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.9em;
            margin: 4px 0;
        }}

        .status-success {{
            background-color: #e6f4ea;
            color: #137333;
        }}

        .status-warning {{
            background-color: #fef7e0;
            color: #ea8600;
        }}

        .status-error {{
            background-color: #fce8e6;
            color: #c5221f;
        }}

        /* Comparison View */
        .comparison-container {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 20px 0;
        }}

        .diff-highlight {{
            background-color: #fff3e0;
            padding: 2px 4px;
            border-radius: 2px;
        }}

        /* Loading States */
        @keyframes pulse-{user_id} {{
            0% {{ opacity: 0.6; }}
            50% {{ opacity: 1; }}
            100% {{ opacity: 0.6; }}
        }}

        .loading-pulse-{user_id} {{
            animation: pulse-{user_id} 1.5s infinite;
        }}

        /* Responsive Design */
        @media (max-width: 768px) {{
            .comparison-container {{
                grid-template-columns: 1fr;
            }}
            
            .extracted-info {{
                padding: 15px;
                margin: 10px 0;
            }}
            
            .section-header {{
                font-size: 1.1em;
            }}
            
            .stTitle {{
                font-size: 2rem !important;
                padding-bottom: 1.5rem !important;
            }}
        }}

        /* Print Styles */
        @media print {{
            .stButton, .uploadedFile {{
                display: none;
            }}
            
            .extracted-info {{
                box-shadow: none;
                border: 1px solid #000;
            }}
            
            .comparison-container {{
                break-inside: avoid;
            }}
        }}

        /* Accessibility Enhancements */
        .info-label, .section-header {{
            outline: none;
        }}

        .stButton > button:focus {{
            outline: 2px solid #4285f4;
            outline-offset: 2px;
        }}

        /* Selection Marker Styles */
        .marker-unselected {{
            color: #5f6368;
        }}

        .marker-selected {{
            color: #1a73e8;
            font-weight: 500;
        }}
    </style>
    """

def get_theme_css(theme='default'):
    """Get theme-specific CSS"""
    THEMES = {
        'default': """
            <style>
                /* Default theme styles - already included in BASE_CSS */
            </style>
        """,
        'dark': """
            <style>
                .extracted-info {
                    background-color: #2d2d2d;
                    border-color: #404040;
                }
                .info-label {
                    color: #e0e0e0;
                }
                .info-value {
                    color: #cccccc;
                }
                .section-header {
                    color: #66b2ff;
                    border-bottom-color: #66b2ff;
                }
                .stButton > button {
                    background-color: #66b2ff;
                }
                .stButton > button:hover {
                    background-color: #3399ff;
                }
                .status-success {
                    background-color: #1e3b2f;
                    color: #7ee2a8;
                }
                .status-warning {
                    background-color: #3d3123;
                    color: #ffd494;
                }
                .status-error {
                    background-color: #3e2427;
                    color: #ffa4a4;
                }
                .marker-unselected {
                    color: #888888;
                }
                .marker-selected {
                    color: #66b2ff;
                }
            </style>
        """,
        'high-contrast': """
            <style>
                .extracted-info {
                    background-color: #ffffff;
                    border: 2px solid #000000;
                }
                .info-label {
                    color: #000000;
                    font-weight: 600;
                }
                .info-value {
                    color: #000000;
                }
                .section-header {
                    color: #000000;
                    border-bottom: 3px solid #000000;
                }
                .stButton > button {
                    background-color: #000000;
                    border: 2px solid #000000;
                }
                .stButton > button:hover {
                    background-color: #333333;
                }
                .status-success {
                    background-color: #d4edda;
                    color: #000000;
                    border: 1px solid #000000;
                }
                .status-warning {
                    background-color: #fff3cd;
                    color: #000000;
                    border: 1px solid #000000;
                }
                .status-error {
                    background-color: #f8d7da;
                    color: #000000;
                    border: 1px solid #000000;
                }
                .marker-unselected {
                    color: #000000;
                    text-decoration: line-through;
                }
                .marker-selected {
                    color: #000000;
                    font-weight: 700;
                }
            </style>
        """
    }
    return THEMES.get(theme, THEMES['default'])

# Export default CSS for backward compatibility
CUSTOM_CSS = get_user_custom_css()