# -*- coding: utf-8 -*-
"""
Streamlit page: Chatbot Budaya Papua.
Provides interactive cultural assistance for 6 tribes in Papua.
"""
import streamlit as st
import re
from backend.styles import apply_custom_styles, render_header, render_footer
from backend.chatbot import generate_chatbot_response

# Apply custom styles & header
apply_custom_styles()
render_header()

# Page title
st.markdown("## 💬 Chatbot Budaya Etnik Papua")
st.markdown(
    "Tanyakan apapun mengenai kebudayaan suku Asmat, Dani, Amungme, Kamoro, Biak, dan Sentani. "
    "Anda bisa menanyakan rumah adat, pakaian adat, makanan, tarian, hari besar, atau alat musik mereka."
)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Saya adalah Asisten Budaya Papua. Ada yang bisa saya bantu untuk mengenalkan tradisi 6 suku utama di Papua?"}
    ]

def render_message_content(content, msg_idx):
    """Parses text and renders [GALERI_BTN|filter|open] as st.button"""
    # Split by the GALERI_BTN pattern
    parts = re.split(r'\[GALERI_BTN\|(.*?)\|(.*?)\]', content)
    
    # Parts will be: [text, filter, open, text, filter, open, text]
    for i in range(0, len(parts), 3):
        text_part = parts[i]
        if text_part.strip():
            st.markdown(text_part)
            
        if i + 2 < len(parts):
            filter_cat = parts[i+1]
            open_cat = parts[i+2]
            
            if st.button(f"🖼️ Lihat Gambar di Galeri Budaya", key=f"galeri_btn_{msg_idx}_{i}"):
                st.session_state["galeri_filter"] = filter_cat
                st.session_state["galeri_open"] = open_cat
                st.switch_page("pages/2_Galeri.py")

# Render chat history
for idx, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        render_message_content(msg["content"], idx)

# Quick response options
st.write("---")
st.write("💡 **Rekomendasi Pertanyaan:**")
btn_cols = st.columns(3)
preset_clicked = None

with btn_cols[0]:
    if st.button("🛖 Rumah Adat Suku Dani?", key="q1"):
        preset_clicked = "Apa rumah adat Suku Dani?"
    if st.button("🎭 Tarian Suku Asmat?", key="q4"):
        preset_clicked = "Tarian tradisional Suku Asmat apa saja?"
        
with btn_cols[1]:
    if st.button("👘 Pakaian pria Suku Biak?", key="q2"):
        preset_clicked = "Bagaimana pakaian laki-laki Suku Biak?"
    if st.button("🎵 Alat musik Suku Sentani?", key="q5"):
        preset_clicked = "Sebutkan alat musik Suku Sentani!"

with btn_cols[2]:
    if st.button("🍲 Makanan khas Kamoro?", key="q3"):
        preset_clicked = "Makanan khas Suku Kamoro apa?"
    if st.button("🎉 Upacara Suku Amungme?", key="q6"):
        preset_clicked = "Apa hari besar atau upacara Suku Amungme?"

# Capture user input
user_query = st.chat_input("Ketik pertanyaan Anda di sini... (misal: Suku Asmat makanan)")

# If a preset button was clicked, use its text as query
if preset_clicked:
    user_query = preset_clicked

# Process query if present
if user_query:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    # Generate bot response
    bot_response = generate_chatbot_response(user_query)
    
    is_fallback = False
    if "[FALLBACK]" in bot_response:
        is_fallback = True
        bot_response = "Maaf, saya belum memahami pertanyaan Anda. Kalimat atau kata kunci yang Anda masukkan tidak mencapai batas akurasi (70%). Apakah Anda ingin berbicara dengan admin manusia untuk bantuan lebih lanjut?"
    
    # Display assistant message
    with st.chat_message("assistant"):
        render_message_content(bot_response, len(st.session_state.messages))
        
        if is_fallback:
            st.warning("⚠️ Bantuan Diperlukan")
            if st.button("🧑‍💻 Hubungi Admin Manusia", key=f"admin_btn_{len(st.session_state.messages)}"):
                st.success("Menghubungkan Anda ke saluran bantuan Admin... (Simulasi: Membuka jendela WhatsApp / Email)")
            
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    # Rerun to update input clean state (only if preset button was used to prevent multiple submissions)
    if preset_clicked and not is_fallback:
        st.rerun()

render_footer()
