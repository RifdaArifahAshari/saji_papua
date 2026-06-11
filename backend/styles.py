# -*- coding: utf-8 -*-
"""
Helper module for Saji Papua style injections.
Ensures UI consistency across all multi-page Streamlit views.
Now updated to match the Light Theme of index.html.
"""
import streamlit as st

def apply_custom_styles():
    """
    Injects custom CSS to style Streamlit to match the Saji Papua brand guidelines (Light Theme).
    """
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800;900&display=swap');
            
            /* Application Background & Typography */
            .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
                background-color: #faf8f5 !important;
                background-image: 
                    radial-gradient(circle at 10% 20%, rgba(176, 55, 30, 0.04) 0%, transparent 40%),
                    radial-gradient(circle at 90% 80%, rgba(198, 127, 7, 0.04) 0%, transparent 40%),
                    url("data:image/svg+xml,%3Csvg width='80' height='80' viewBox='0 0 80 80' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M40 0 L80 40 L40 80 L0 40 Z M40 10 L70 40 L40 70 L10 40 Z' fill='%23c67f07' fill-opacity='0.02' fill-rule='evenodd'/%3E%3C/svg%3E") !important;
                background-attachment: fixed !important;
                color: #1e2025 !important;
                font-family: 'Inter', sans-serif !important;
            }
            
            /* Hide Streamlit default decorations */
            [data-testid="stHeader"] {
                display: none !important;
            }
            
            /* Sidebar Styling */
            [data-testid="stSidebar"] {
                background-color: rgba(250, 248, 245, 0.98) !important;
                border-right: 1px solid rgba(198, 127, 7, 0.18) !important;
            }
            [data-testid="stSidebarNav"] {
                background-color: transparent !important;
            }
            [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] span {
                color: #4a4d55 !important;
            }
            
            /* Custom headers */
            h1, h2, h3, h4, h5, h6 {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 700 !important;
                letter-spacing: -0.01em !important;
                color: #1e2025 !important;
            }
            
            /* Text colors */
            p, span, div, label {
                color: #1e2025;
            }
            
            /* Style Streamlit Markdown links */
            .stApp a {
                color: #c67f07 !important;
                text-decoration: none !important;
                font-weight: 600 !important;
                transition: all 0.2s ease !important;
            }
            .stApp a:hover {
                color: #965b02 !important;
                text-shadow: 0 0 8px rgba(198, 127, 7, 0.2) !important;
            }

            /* Custom Premium Card */
            .custom-card {
                background: rgba(255, 255, 255, 0.85);
                border: 1px solid rgba(198, 127, 7, 0.18);
                border-radius: 20px;
                padding: 24px;
                margin-bottom: 20px;
                backdrop-filter: blur(16px);
                transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
                color: #1e2025 !important;
                box-shadow: 0 8px 30px rgba(150, 120, 90, 0.08);
            }
            .custom-card p, .custom-card div {
                color: #1e2025 !important;
            }
            .custom-card:hover {
                border-color: #c67f07;
                transform: translateY(-5px);
                box-shadow: 0 12px 40px rgba(150, 120, 90, 0.12);
            }
            
            /* Custom primary buttons styling */
            .stButton>button {
                background: linear-gradient(135deg, #c67f07 0%, #965b02 100%) !important;
                color: #ffffff !important;
                border: none !important;
                border-radius: 12px !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                font-size: 1rem !important;
                padding: 10px 24px !important;
                box-shadow: 0 4px 15px rgba(198, 127, 7, 0.2) !important;
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
                width: 100%;
            }
            .stButton>button p {
                color: #ffffff !important;
            }
            .stButton>button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 20px rgba(198, 127, 7, 0.35), 0 0 0 3px rgba(198, 127, 7, 0.15) !important;
            }
            
            /* Custom Secondary Button/Tab style */
            div[data-testid="stHorizontalBlock"] .stButton>button {
                background: rgba(255, 255, 255, 0.8) !important;
                color: #1e2025 !important;
                border: 1px solid rgba(198, 127, 7, 0.18) !important;
                box-shadow: none !important;
            }
            div[data-testid="stHorizontalBlock"] .stButton>button p {
                color: #1e2025 !important;
            }
            div[data-testid="stHorizontalBlock"] .stButton>button:hover {
                background: rgba(198, 127, 7, 0.05) !important;
                border-color: #c67f07 !important;
                color: #c67f07 !important;
            }
            div[data-testid="stHorizontalBlock"] .stButton>button:hover p {
                color: #c67f07 !important;
            }
            
            /* Chat message bubbles */
            [data-testid="stChatMessage"] {
                background-color: #ffffff !important;
                border: 1px solid rgba(0, 0, 0, 0.06) !important;
                border-radius: 18px !important;
                box-shadow: 0 2px 8px rgba(0,0,0,0.02) !important;
                color: #1e2025 !important;
            }
            [data-testid="stChatMessage"]:nth-of-type(even) {
                background-color: #b0371e !important;
                border: 1px solid rgba(176, 55, 30, 0.15) !important;
                color: #ffffff !important;
                box-shadow: 0 4px 12px rgba(176, 55, 30, 0.15) !important;
            }
            [data-testid="stChatMessage"]:nth-of-type(even) p, [data-testid="stChatMessage"]:nth-of-type(even) span, [data-testid="stChatMessage"]:nth-of-type(even) div {
                color: #ffffff !important;
            }
            
            /* Style elements for quiz options */
            .quiz-option-btn button {
                text-align: left !important;
                justify-content: flex-start !important;
                margin-bottom: 8px !important;
            }
            
            /* Custom input styling */
            input, textarea, select {
                background-color: #faf8f5 !important;
                border: 1px solid rgba(198, 127, 7, 0.18) !important;
                color: #1e2025 !important;
                border-radius: 12px !important;
            }
            
            input:focus, textarea:focus, select:focus {
                background-color: #ffffff !important;
                border-color: #c67f07 !important;
                box-shadow: 0 0 8px rgba(198, 127, 7, 0.3) !important;
            }
            
            /* Custom Success Alert */
            .success-alert {
                background-color: rgba(76, 175, 80, 0.1);
                border: 1px solid #4CAF50;
                border-radius: 12px;
                padding: 16px;
                color: #2e7d32;
                margin-bottom: 16px;
            }
            .success-alert p, .success-alert h4 {
                color: #2e7d32 !important;
            }
            
            /* Tagline and Badge styles */
            .tagline {
                display: inline-flex;
                align-items: center;
                gap: 8px;
                padding: 6px 16px;
                background: rgba(176, 55, 30, 0.06);
                border: 1px solid rgba(176, 55, 30, 0.25);
                border-radius: 100px;
                color: #b0371e;
                font-weight: 700;
                font-size: 0.85rem;
                letter-spacing: 0.05em;
                text-transform: uppercase;
                margin-bottom: 16px;
            }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    """
    Renders the custom Saji Papua navigation bar/header.
    """
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 20px 0; border-bottom: 1px solid rgba(0,0,0,0.05); margin-bottom: 30px;">
            <div style="display: flex; align-items: center; gap: 12px; text-decoration: none;">
                <svg style="width: 40px; height: 40px; fill: #c67f07; filter: drop-shadow(0 2px 4px rgba(198, 127, 7, 0.2));" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="none" stroke="currentColor" stroke-width="4" stroke-dasharray="10 6" />
                    <path d="M50 15 L80 45 L50 75 L20 45 Z" fill="none" stroke="currentColor" stroke-width="3" />
                    <circle cx="50" cy="45" r="8" fill="#b0371e" />
                    <line x1="50" y1="15" x2="50" y2="75" stroke="currentColor" stroke-width="2" />
                    <line x1="20" y1="45" x2="80" y2="45" stroke="currentColor" stroke-width="2" />
                </svg>
                <span style="font-size: 1.5rem; font-weight: 800; font-family: 'Outfit', sans-serif; background: linear-gradient(135deg, #1e2025 40%, #c67f07 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Saji<span style="color: #b0371e; -webkit-text-fill-color: initial; margin-left: 2px;">Papua</span></span>
            </div>
            <div style="background: rgba(176, 55, 30, 0.06); border: 1px solid rgba(176, 55, 30, 0.25); padding: 8px 16px; border-radius: 100px; font-family: 'Outfit', sans-serif; font-size: 0.85rem; font-weight: 700; color: #b0371e; display: flex; align-items: center; gap: 6px; letter-spacing: 0.05em; text-transform: uppercase;">
                🌌 Preservasi Etnik-Digital 2026
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    """
    Renders the custom footer.
    """
    st.markdown("""
        <div style="margin-top: 60px; padding-top: 30px; border-top: 1px solid rgba(0,0,0,0.05); text-align: center; color: #787d85; font-size: 0.85rem;">
            <p>© 2026 Saji Papua. Dibuat dengan dedikasi untuk melestarikan kebudayaan dan bahasa daerah Papua.</p>
            <p style="margin-top: 6px; font-size: 0.8rem; color: #965b02;">Etnik-Digital Preservation Framework</p>
        </div>
    """, unsafe_allow_html=True)
