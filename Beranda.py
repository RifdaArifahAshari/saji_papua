# -*- coding: utf-8 -*-
"""
Beranda (Homepage) & Navigation Router for Saji Papua.
Entry point of the Streamlit Multi-Page application.
"""
import streamlit as st
from backend.styles import apply_custom_styles, render_header, render_footer

# 1. Page Configuration
st.set_page_config(
    page_title="Saji Papua: Pelestarian Budaya Etnik-Digital",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Main Page Render Function
def render_beranda():
    # Apply theme colors
    apply_custom_styles()
    render_header()
    
    # Custom CSS specific to Hero & Statistics sections
    st.markdown("""
        <style>
            .hero-title {
                font-size: 3.2rem;
                font-weight: 900;
                line-height: 1.1;
                margin-bottom: 20px;
                font-family: 'Outfit', sans-serif;
                background: linear-gradient(135deg, #ffffff 40%, #e5a93c 80%, #c84b31 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .hero-subtitle {
                font-size: 1.1rem;
                color: #9ca3af;
                margin-bottom: 30px;
                line-height: 1.6;
            }
            .stat-num {
                font-size: 3rem;
                font-weight: 900;
                color: #e5a93c;
                text-shadow: 0 0 15px rgba(229, 169, 60, 0.25);
                line-height: 1;
                margin-bottom: 6px;
            }
            .stat-num.highlight {
                color: #c84b31;
                text-shadow: 0 0 15px rgba(200, 75, 49, 0.3);
            }
            .stat-lbl {
                font-size: 1rem;
                font-weight: 600;
                color: #f3f4f6;
            }
            .stat-desc {
                font-size: 0.8rem;
                color: #6b7280;
            }
        </style>
    """, unsafe_allow_html=True)

    # Hero Grid Layout (Left Content, Right SVG Visual)
    col1, col2 = st.columns([1.2, 0.8])
    
    with col1:
        st.markdown('<div class="tagline">🌌 Preservasi Etnik-Digital 2026</div>', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Saji Papua: Menjaga Denyut Nadi Tradisi di Era Digital</h1>', unsafe_allow_html=True)
        st.markdown(
            '<p class="hero-subtitle">Eksplorasi warisan budaya agung tanah Papua melalui sentuhan etnik-digital yang presisi. '
            'Menghubungkan tradisi luhur suku Dani, Asmat, Amungme, Kamoro, Biak, dan Sentani dengan komputasi masa depan.</p>', 
            unsafe_allow_html=True
        )
        
        # Call-To-Action buttons
        st.write("")
        btn_cols = st.columns([1, 1.2, 1])
        with btn_cols[0]:
            if st.button("Jelajahi Papua", type="primary", use_container_width=True):
                st.switch_page("pages/2_Galeri.py")
        with btn_cols[1]:
            if st.button("Coba Fitur Penerjemah", use_container_width=True):
                st.switch_page("pages/4_Penerjemah.py")
                
    with col2:
        # Ethnic digital art SVG
        st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; padding: 10px;">
                <svg style="width: 100%; max-width: 320px; filter: drop-shadow(0 10px 30px rgba(0, 0, 0, 0.7)) drop-shadow(0 0 40px rgba(229, 169, 60, 0.25));" viewBox="0 0 400 500" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <!-- Shield Base -->
                    <path d="M200 40 C320 120, 320 320, 200 460 C80 320, 80 120, 200 40 Z" fill="#141416" stroke="#e5a93c" stroke-width="4" />
                    <!-- Inner Shield Decor -->
                    <path d="M200 70 C290 140, 290 300, 200 420 C110 300, 110 140, 200 70 Z" fill="#1b1c21" stroke="#c84b31" stroke-width="2" />

                    <!-- Center Carving Motif (Etnik-Digital) -->
                    <line x1="200" y1="70" x2="200" y2="420" stroke="#e5a93c" stroke-width="2" stroke-dasharray="6 4" />

                    <!-- Digital Nodes & Circles (Asmat Face Representation) -->
                    <circle cx="200" cy="180" r="28" fill="none" stroke="#e5a93c" stroke-width="2" />
                    <circle cx="200" cy="180" r="14" fill="#c84b31" />

                    <!-- Left and Right Digital Wings (Asmat Wave) -->
                    <path d="M200 220 Q270 240 270 200" stroke="#e5a93c" stroke-width="3" />
                    <path d="M200 220 Q130 240 130 200" stroke="#e5a93c" stroke-width="3" />
                    <circle cx="270" cy="200" r="6" fill="#e5a93c" />
                    <circle cx="130" cy="200" r="6" fill="#e5a93c" />

                    <!-- Lower Mask Carving -->
                    <path d="M200 280 Q290 310 200 370 Q110 310 200 280 Z" fill="none" stroke="#e5a93c" stroke-width="2" />
                    <path d="M200 300 Q260 320 200 350 Q140 320 200 300 Z" fill="none" stroke="#c84b31" stroke-width="1.5" />
                    <circle cx="200" cy="325" r="8" fill="#e5a93c" />

                    <!-- Digital Lines Overlay -->
                    <line x1="50" y1="250" x2="100" y2="250" stroke="#e5a93c" stroke-width="1.5" stroke-dasharray="4 4" />
                    <circle cx="50" cy="250" r="4" fill="#e5a93c" />
                    <line x1="350" y1="250" x2="300" y2="250" stroke="#e5a93c" stroke-width="1.5" stroke-dasharray="4 4" />
                    <circle cx="350" cy="250" r="4" fill="#e5a93c" />
                </svg>
            </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # Statistics Section
    st.markdown("### 📊 Dampak Preservasi Budaya")
    stat_cols = st.columns(3)
    
    with stat_cols[0]:
        st.markdown("""
            <div class="custom-card" style="text-align: center;">
                <div class="stat-num">250+</div>
                <div class="stat-lbl">Suku Adat</div>
                <div class="stat-desc">Keragaman adat istiadat luhur yang hidup berdampingan.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with stat_cols[1]:
        st.markdown("""
            <div class="custom-card" style="text-align: center;">
                <div class="stat-num highlight">300+</div>
                <div class="stat-lbl">Bahasa Daerah</div>
                <div class="stat-desc">Kekayaan linguistik unik yang dilindungi secara formal.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with stat_cols[2]:
        st.markdown("""
            <div class="custom-card" style="text-align: center;">
                <div class="stat-num">1</div>
                <div class="stat-lbl">Portal Otomata</div>
                <div class="stat-desc">Aplikasi pelestarian struktural bahasa pertama di Indonesia.</div>
            </div>
        """, unsafe_allow_html=True)

    render_footer()

# 3. Define navigation structure
beranda_page = st.Page(render_beranda, title="Beranda", icon="🏠", default=True)
galeri_page = st.Page("pages/2_Galeri.py", title="Galeri Budaya", icon="🖼️")
chatbot_page = st.Page("pages/1_Chatbot.py", title="Chatbot", icon="💬")
penerjemah_page = st.Page("pages/4_Penerjemah.py", title="Penerjemah", icon="🗣️")
kuis_page = st.Page("pages/3_Kuis.py", title="Game (Kuis)", icon="🎮")

# Create Navigation
pg = st.navigation({
    "Saji Papua": [
        beranda_page,
        galeri_page,
        chatbot_page,
        penerjemah_page,
        kuis_page
    ]
})

# Run app routing
pg.run()
