# -*- coding: utf-8 -*-
"""
Streamlit page: Galeri Budaya Papua.
Presents filterable images of traditional houses, clothing, and portraits.
"""
import streamlit as st
from backend.styles import apply_custom_styles, render_header, render_footer

# Apply custom styles & header
apply_custom_styles()
render_header()

st.markdown("## 🖼️ Galeri Budaya Papua")
st.markdown("Eksplorasi estetika arsitektur rumah adat, busana tradisional, dan potret kehidupan masyarakat Papua.")

# Gallery Items database
GALLERY_ITEMS = [
    {
        "category": "Pakaian Adat",
        "title": "Aksesoris & Pakaian Adat",
        "desc": "Busana adat dengan hiasan kerang laut, anyaman jerami, serta mahkota bulu burung Cenderawasih yang sarat makna spiritual.",
        "img": "assets/images/pakaian_adat_papua.png"
    },
    {
        "category": "Rumah Adat",
        "title": "Rumah Honai",
        "desc": "Rumah adat Suku Dani berbentuk bundar dengan atap jerami tebal, dirancang tanpa jendela untuk melindungi dari dinginnya pegunungan.",
        "img": "assets/images/honai_blue_door.jpg"
    },
    {
        "category": "Rumah Adat",
        "title": "Lembah Honai",
        "desc": "Dua rumah Honai tradisional yang berdiri harmonis di tengah alam pegunungan Papua yang asri dan bergunung-gunung.",
        "img": "assets/images/honai_mountains.jpg"
    },
    {
        "category": "Rumah Adat",
        "title": "Rumah Kariwari",
        "desc": "Rumah adat khas Suku Tobati-Enggros di Danau Sentani berbentuk kerucut segi delapan, berfungsi sebagai pusat pendidikan adat pemuda.",
        "img": "assets/images/kariwari_tall.jpg"
    },
    {
        "category": "Rumah Adat",
        "title": "Rumah Jew (Suku Asmat)",
        "desc": "Dikenal sebagai rumah bujang, dihiasi ukiran totem khas Asmat, berfungsi sebagai tempat musyawarah dan ritual adat sakral.",
        "img": "assets/images/kariwari_decorated.jpg"
    },
    {
        "category": "Orang Papua",
        "title": "Potret Sesepuh Adat",
        "desc": "Sesepuh adat Papua mengenakan ikat kepala bulu kasuari dan tindih hidung dari tulang taring babi hutan, memancarkan wibawa kepemimpinan luhur.",
        "img": "assets/images/papuan_portrait.jpg"
    }
]

# Set up category tabs
tabs = st.tabs(["Semua", "🏠 Rumah Adat", "👕 Pakaian Adat", "👤 Orang Papua"])

def render_gallery_grid(items):
    if not items:
        st.info("Tidak ada gambar untuk kategori ini.")
        return
        
    # Render in a grid (3 columns)
    cols = st.columns(3)
    for idx, item in enumerate(items):
        col_idx = idx % 3
        with cols[col_idx]:
            st.markdown(f"""
                <div class="custom-card" style="padding: 0px; overflow: hidden; border-radius: 16px;">
                    <div style="background-color: #0e0f12; padding: 12px; border-bottom: 1px solid rgba(229, 169, 60, 0.15);">
                        <span style="background: rgba(229,169,60,0.1); border: 1px solid rgba(229,169,60,0.3); padding: 4px 8px; border-radius: 30px; font-size: 0.75rem; color: #e5a93c; font-weight: 600;">
                            {item['category']}
                        </span>
                        <h4 style="margin: 8px 0 0 0; font-size: 1.1rem; color: #ffffff;">{item['title']}</h4>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Display image (using st.image so it handles paths cleanly)
            st.image(item["img"], use_container_width=True)
            
            st.markdown(f"""
                <div style="padding: 12px; background: rgba(22, 23, 28, 0.3); border-radius: 0 0 16px 16px;">
                    <p style="font-size: 0.85rem; color: #9ca3af; line-height: 1.5; margin: 0;">{item['desc']}</p>
                </div>
                <div style="margin-bottom: 24px;"></div>
            """, unsafe_allow_html=True)

# Render filtered list in each tab
with tabs[0]:
    render_gallery_grid(GALLERY_ITEMS)

with tabs[1]:
    filtered_items = [i for i in GALLERY_ITEMS if i["category"] == "Rumah Adat"]
    render_gallery_grid(filtered_items)

with tabs[2]:
    filtered_items = [i for i in GALLERY_ITEMS if i["category"] == "Pakaian Adat"]
    render_gallery_grid(filtered_items)

with tabs[3]:
    filtered_items = [i for i in GALLERY_ITEMS if i["category"] == "Orang Papua"]
    render_gallery_grid(filtered_items)

render_footer()
