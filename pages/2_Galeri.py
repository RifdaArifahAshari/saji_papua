# -*- coding: utf-8 -*-
"""
Streamlit page: Galeri Budaya Papua.
Presents filterable images of traditional houses, clothing, and portraits.
"""
import streamlit as st
from backend.styles import apply_custom_styles, render_header, render_footer
from backend.galeri_data import GALLERY_ITEMS

# Apply custom styles & header
apply_custom_styles()
render_header()

st.markdown("## 🖼️ Galeri Budaya Papua")
st.markdown("Eksplorasi estetika arsitektur rumah adat, busana tradisional, dan kebudayaan luhur masyarakat Papua.")

# Map filters to pill names
filter_mapping = {
    "house": "🛖 Rumah Adat",
    "clothing": "👘 Pakaian Adat",
    "dance": "🎭 Tarian Tradisional",
    "food": "🍲 Makanan Khas",
    "festival": "🎉 Upacara/Festival",
    "music": "🎵 Alat Musik",
    "tourism": "🗺️ Wisata"
}

pill_options = [
    "Semua", "🛖 Rumah Adat", "👘 Pakaian Adat", "🎭 Tarian Tradisional", 
    "🍲 Makanan Khas", "🎉 Upacara/Festival", "🎵 Alat Musik", "🗺️ Wisata"
]

default_pill = "Semua"
target_open = None

if "galeri_filter" in st.session_state:
    f = st.session_state["galeri_filter"]
    if f in filter_mapping:
        default_pill = filter_mapping[f]
    del st.session_state["galeri_filter"]

if "galeri_open" in st.session_state:
    target_open = st.session_state["galeri_open"]
    # Find the item if target_open is provided
    if target_open and target_open.strip():
        # Show dialog immediately!
        @st.dialog(target_open)
        def show_item_modal(item):
            st.image(item["img"], use_container_width=True)
            st.markdown(f"**Kategori**: {item['category']}")
            st.write(item["desc"])

        for item in GALLERY_ITEMS:
            # If default_pill is set, map it to filter_cat to ensure correct modal pops up
            target_filter = None
            for k, v in filter_mapping.items():
                if v == default_pill:
                    target_filter = k
                    break
                    
            if target_filter and item.get("filter_cat") != target_filter:
                continue
                
            # Match using same logic as HTML (includes)
            if target_open.lower() in item["title"].lower() or target_open.lower() in item["desc"].lower() or target_open.lower() in item["category"].lower():
                show_item_modal(item)
                break
                
    del st.session_state["galeri_open"]

# Set up category pills
selected_pill = st.pills("Kategori", pill_options, default=default_pill, label_visibility="collapsed")
if not selected_pill:
    selected_pill = "Semua"

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
                <div style="background-color: #ffffff; padding: 16px; border: 1px solid rgba(198, 127, 7, 0.18); border-bottom: 3px solid #c67f07; border-radius: 16px 16px 0 0; box-shadow: 0 -4px 15px rgba(150, 120, 90, 0.05);">
                    <span style="background: rgba(176, 55, 30, 0.06); border: 1px solid rgba(176, 55, 30, 0.2); padding: 4px 10px; border-radius: 30px; font-size: 0.75rem; color: #b0371e; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">
                        {item['category']}
                    </span>
                    <h4 style="margin: 10px 0 0 0; font-size: 1.2rem; color: #1e2025; font-weight: 800;">{item['title']}</h4>
                </div>
            """, unsafe_allow_html=True)
            
            st.image(item["img"], use_container_width=True)
            
            st.markdown(f"""
                <div style="padding: 16px; background-color: #ffffff; border: 1px solid rgba(198, 127, 7, 0.18); border-top: none; border-radius: 0 0 16px 16px; box-shadow: 0 8px 20px rgba(150, 120, 90, 0.08); margin-top: -15px;">
                    <p style="font-size: 0.9rem; color: #4a4d55; line-height: 1.6; margin: 0;">{item['desc']}</p>
                </div>
                <div style="margin-bottom: 30px;"></div>
            """, unsafe_allow_html=True)



FESTIVAL_DATA = [
    {
        "suku": "Suku Asmat",
        "items": [
            ("Festival Pisau", "Upacara pengukiran kayu tradisional secara massal."),
            ("Festival Asmat", "Diadakan setiap Agustus untuk merayakan kebanggaan seni ukir Asmat."),
            ("Upacara Mbitoro", "Ritual inisiasi kedewasaan bagi pria muda Asmat.")
        ]
    },
    {
        "suku": "Suku Dani",
        "items": [
            ("Festival Lembah Baliem", "Diadakan tiap bulan Agustus, menampilkan atraksi simulasi perang antardesa."),
            ("Upacara Bakar Batu", "Upacara masak massal Wamena untuk syukuran atau duka cita."),
            ("Upacara Sumpah Babi", "Pesta penyelesaian konflik atau syukuran perdamaian.")
        ]
    },
    {
        "suku": "Suku Amungme",
        "items": [
            ("Upacara Tikim", "Upacara inisiasi sakral bagi anak laki-laki."),
            ("Pesta Panen Ubi", "Diselenggarakan antara bulan September hingga Oktober sebagai wujud syukur hasil bumi.")
        ]
    },
    {
        "suku": "Suku Kamoro",
        "items": [
            ("Upacara Mboti", "Pesta sagu akbar yang dilaksanakan setiap lima tahun sekali."),
            ("Festival Kamoro", "Perayaan tahunan untuk memamerkan seni ukir dan budaya pesisir Kamoro.")
        ]
    },
    {
        "suku": "Suku Biak",
        "items": [
            ("Festival Pesisir Biak", "Diadakan Juni-Juli untuk mempromosikan pariwisata laut dan kebudayaan bahari."),
            ("Upacara Rumsram", "Upacara inisiasi masuknya pemuda ke rumah bujang (Rumsram)."),
            ("Pesta Laut", "Tradisi syukur atas melimpahnya hasil tangkapan laut.")
        ]
    },
    {
        "suku": "Suku Sentani",
        "items": [
            ("Festival Danau Sentani", "Digelar Juni-Juli dengan atraksi tari di atas perahu (Isosolo) dan parade budaya."),
            ("Lomba Perahu Hias", "Balap dayung perahu berhias ukiran Sentani di tengah danau."),
            ("Upacara Mbate", "Syukuran adat atas hasil tangkapan ikan yang melimpah.")
        ]
    }
]

def render_festival_list():
    st.markdown("### 🎉 Hari Besar & Upacara Adat Papua")
    st.markdown("Berbeda dengan artefak fisik, upacara adat dan festival merupakan perayaan tak benda yang diselenggarakan pada waktu tertentu.")
    
    for data in FESTIVAL_DATA:
        with st.expander(f"✨ Upacara Adat {data['suku']}", expanded=True):
            for title, desc in data['items']:
                st.markdown(f"**{title}**")
                st.markdown(f"<span style='color: #787d85; font-size: 0.9rem;'>{desc}</span>", unsafe_allow_html=True)
                st.write("")

if selected_pill == "Semua":
    render_gallery_grid(GALLERY_ITEMS)
    st.markdown("---")
    render_festival_list()
elif selected_pill == "🎉 Upacara/Festival":
    render_festival_list()
else:
    # Map back to filter_cat
    reverse_map = {v: k for k, v in filter_mapping.items()}
    f_cat = reverse_map.get(selected_pill)
    if f_cat:
        filtered_items = [item for item in GALLERY_ITEMS if item.get("filter_cat") == f_cat]
        render_gallery_grid(filtered_items)

render_footer()
