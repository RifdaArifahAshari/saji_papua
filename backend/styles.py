# -*- coding: utf-8 -*-
"""
Helper module for Saji Papua style injections.
Ensures UI consistency across all multi-page Streamlit views.
"""
import streamlit as st

def apply_custom_styles():
    """
    Injects custom CSS to style Streamlit to match the Saji Papua brand guidelines.
    """
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800;900&display=swap');
            
            /* Application Background & Typography */
            .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
                background-color: #070709 !important;
                background-image: 
                    radial-gradient(circle at 10% 20%, rgba(200, 75, 49, 0.08) 0%, transparent 40%),
                    radial-gradient(circle at 90% 80%, rgba(229, 169, 60, 0.08) 0%, transparent 40%),
                    url("data:image/svg+xml,%3Csvg width='80' height='80' viewBox='0 0 80 80' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M40 0 L80 40 L40 80 L0 40 Z M40 10 L70 40 L40 70 L10 40 Z' fill='%23e5a93c' fill-opacity='0.015' fill-rule='evenodd'/%3E%3C/svg%3E") !important;
                background-attachment: fixed !important;
                color: #f3f4f6 !important;
                font-family: 'Inter', sans-serif !important;
            }
            
            /* Hide Streamlit default decorations */
            [data-testid="stHeader"] {
                display: none !important;
            }
            
            /* Sidebar Styling */
            [data-testid="stSidebar"] {
                background-color: #0e0f12 !important;
                border-right: 1px solid rgba(229, 169, 60, 0.15) !important;
            }
            [data-testid="stSidebarNav"] {
                background-color: #0e0f12 !important;
            }
            
            /* Custom headers */
            h1, h2, h3, h4, h5, h6 {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 700 !important;
                letter-spacing: -0.01em !important;
                color: #ffffff !important;
            }
            
            /* Style Streamlit Markdown links */
            .stApp a {
                color: #e5a93c !important;
                text-decoration: none !important;
                font-weight: 600 !important;
                transition: all 0.2s ease !important;
            }
            .stApp a:hover {
                color: #f7d070 !important;
                text-shadow: 0 0 8px rgba(229, 169, 60, 0.4) !important;
            }

            /* Custom Premium Card */
            .custom-card {
                background: rgba(22, 23, 28, 0.6);
                border: 1px solid rgba(229, 169, 60, 0.15);
                border-radius: 20px;
                padding: 24px;
                margin-bottom: 20px;
                backdrop-filter: blur(16px);
                transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            }
            .custom-card:hover {
                border-color: rgba(229, 169, 60, 0.4);
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5), 0 0 20px rgba(229, 169, 60, 0.15);
            }
            
            /* Custom primary buttons styling */
            .stButton>button {
                background: linear-gradient(135deg, #e5a93c 0%, #b88126 100%) !important;
                color: #070709 !important;
                border: none !important;
                border-radius: 12px !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                font-size: 1rem !important;
                padding: 10px 24px !important;
                box-shadow: 0 4px 15px rgba(229, 169, 60, 0.3) !important;
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
                width: 100%;
            }
            .stButton>button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 20px rgba(229, 169, 60, 0.5), 0 0 0 3px rgba(229, 169, 60, 0.2) !important;
                color: #070709 !important;
            }
            
            /* Custom Secondary Button/Tab style */
            div[data-testid="stHorizontalBlock"] .stButton>button {
                background: rgba(255, 255, 255, 0.03) !important;
                color: #f3f4f6 !important;
                border: 1px solid rgba(229, 169, 60, 0.15) !important;
                box-shadow: none !important;
            }
            div[data-testid="stHorizontalBlock"] .stButton>button:hover {
                background: rgba(229, 169, 60, 0.08) !important;
                border-color: #e5a93c !important;
                color: #e5a93c !important;
            }
            
            /* Chat message bubbles */
            [data-testid="stChatMessage"] {
                background-color: rgba(22, 23, 28, 0.5) !important;
                border: 1px solid rgba(255, 255, 255, 0.05) !important;
                border-radius: 15px !important;
            }
            [data-testid="stChatMessage"]:nth-of-type(even) {
                background-color: rgba(229, 169, 60, 0.05) !important;
                border: 1px solid rgba(229, 169, 60, 0.15) !important;
            }
            
            /* Style elements for quiz options */
            .quiz-option-btn button {
                text-align: left !important;
                justify-content: flex-start !important;
                margin-bottom: 8px !important;
            }
            
            /* Custom input styling */
            input, textarea, select {
                background-color: rgba(0, 0, 0, 0.4) !important;
                border: 1px solid rgba(229, 169, 60, 0.15) !important;
                color: #f3f4f6 !important;
                border-radius: 12px !important;
            }
            
            /* Custom Success Alert */
            .success-alert {
                background-color: rgba(229, 169, 60, 0.1);
                border: 1px solid #e5a93c;
                border-radius: 12px;
                padding: 16px;
                color: #f7d070;
                margin-bottom: 16px;
            }
            
            /* Tagline and Badge styles */
            .tagline {
                display: inline-flex;
                align-items: center;
                gap: 8px;
                padding: 6px 16px;
                background: rgba(200, 75, 49, 0.1);
                border: 1px solid rgba(200, 75, 49, 0.3);
                border-radius: 100px;
                color: #c84b31;
                font-weight: 600;
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
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 20px 0; border-bottom: 1px solid rgba(255,255,255,0.05); margin-bottom: 30px;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <svg style="width: 40px; height: 40px; fill: #e5a93c; filter: drop-shadow(0 0 8px rgba(229, 169, 60, 0.6));" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="none" stroke="currentColor" stroke-width="4" stroke-dasharray="10 6" />
                    <path d="M50 15 L80 45 L50 75 L20 45 Z" fill="none" stroke="currentColor" stroke-width="3" />
                    <circle cx="50" cy="45" r="8" fill="#c84b31" />
                    <line x1="50" y1="15" x2="50" y2="75" stroke="currentColor" stroke-width="2" />
                    <line x1="20" y1="45" x2="80" y2="45" stroke="currentColor" stroke-width="2" />
                </svg>
                <span style="font-size: 1.8rem; font-weight: 800; font-family: 'Outfit', sans-serif; background: linear-gradient(135deg, #fff 40%, #e5a93c 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Saji<span style="color: #c84b31; -webkit-text-fill-color: initial; margin-left: 2px;">Papua</span></span>
            </div>
            <div style="background: rgba(200, 75, 49, 0.15); border: 1px solid rgba(200, 75, 49, 0.3); padding: 8px 16px; border-radius: 12px; font-family: 'Outfit', sans-serif; font-size: 0.9rem; font-weight: 600; color: #f5d082; display: flex; align-items: center; gap: 6px;">
                🌌 Preservasi Etnik-Digital 2026
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    """
    Renders the custom footer.
    """
    st.markdown("""
        <div style="margin-top: 60px; padding-top: 30px; border-top: 1px solid rgba(255,255,255,0.05); text-align: center; color: #6b7280; font-size: 0.85rem;">
            <p>© 2026 Saji Papua. Dibuat dengan dedikasi untuk melestarikan kebudayaan dan bahasa daerah Papua.</p>
            <p style="margin-top: 6px; font-size: 0.8rem; color: rgba(229, 169, 60, 0.5);">Etnik-Digital Preservation Framework</p>
        </div>
    """, unsafe_allow_html=True)
