# -*- coding: utf-8 -*-
"""
Streamlit page: Penerjemah & Simulator Otomata Tobati.
Translates sentences and displays step-by-step FSA and PDA operations.
"""
import streamlit as st
import time
from backend.styles import apply_custom_styles, render_header, render_footer
from backend.terjemahan import validate_and_translate, LEXICON, PRESETS_VALID, PRESETS_INVALID

# Apply custom styles & header
apply_custom_styles()
render_header()

st.markdown("## 🗣️ Penerjemah & Validator Otomata Tobati")
st.markdown(
    "Saksikan bagaimana teori otomata (FSA dan PDA) memproses kalimat bahasa Tobati "
    "dengan pola **SOV (Subjek-Objek-Verba)** atau **OSV (Objek-Subjek-Verba)** secara visual."
)

# Render Lexicon database in a premium expander
with st.expander("📚 Kamus & Lexicon Bahasa Tobati (Klik untuk membuka)"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Subjek (S)**")
        for word, info in LEXICON["subjects"].items():
            st.markdown(f"- **{word}** → *{info['indo']}*")
            
    with col2:
        st.markdown("**Objek (O)**")
        for word, info in LEXICON["objects"].items():
            st.markdown(f"- **{word}** → *{info['indo']}*")
            
    with col3:
        st.markdown("**Verba / Kata Kerja (V)**")
        for word, info in LEXICON["verbs"].items():
            st.markdown(f"- **{word}** → *{info['indo']}*")

st.write("---")

# Main section layout
col_input, col_preset = st.columns([1.2, 0.8])

selected_preset = None

with col_preset:
    st.markdown("💡 **Pilih Contoh Kalimat:**")
    st.markdown("*Valid (Pola SOV atau OSV):*")
    for pr, desc in PRESETS_VALID.items():
        if st.button(f"🟢 {pr}", key=f"pv_{pr}"):
            selected_preset = pr
            
    st.markdown("*Tidak Valid:*")
    for pr, desc in PRESETS_INVALID.items():
        if st.button(f"🔴 {pr}", key=f"pi_{pr}"):
            selected_preset = pr

with col_input:
    st.markdown("✍️ **Masukan Kalimat Tobati:**")
    
    # Text input prefilled with selected preset if clicked
    default_input = "aka kai aibi"
    if selected_preset:
        default_input = selected_preset
        
    sentence_input = st.text_input(
        "Ketik kalimat di sini (gunakan huruf kecil, pisahkan dengan spasi):",
        value=default_input
    )
    
    sim_speed = st.selectbox(
        "Kecepatan Simulasi:",
        options=[("Sedang (1.0s)", 1.0), ("Cepat (0.3s)", 0.3), ("Lambat (2.0s)", 2.0)],
        index=0
    )
    
    btn_start = st.button("🚀 Mulai Validasi & Terjemahkan")

# Run validation and simulation
if btn_start or selected_preset:
    if not sentence_input.strip():
        st.warning("Masukkan kalimat terlebih dahulu!")
    else:
        st.write("### ⚙️ Proses Simulasi Otomata:")
        
        is_valid, steps, translation_text, error_msg = validate_and_translate(sentence_input)
        
        # Display simulation step by step with delays
        progress_bar = st.progress(0.0)
        status_text = st.empty()
        table_placeholder = st.empty()
        
        simulated_steps = []
        
        for idx, step in enumerate(steps):
            simulated_steps.append(step)
            
            # Format the stack visual
            stack_visual = " | ".join(step["stack"])
            
            # Construct a small visualization log
            status_text.markdown(f"""
                <div class="custom-card" style="border-left: 5px solid {'#e5a93c' if step['status'] != 'error' else '#c84b31'};">
                    <strong>Langkah ke-{step['step']}</strong>: Memproses token <strong>'{step['token']}'</strong> ({step['type']})<br>
                    <strong>FSA State</strong>: {step['prev_state'].upper()} ➔ {step['curr_state'].upper()}<br>
                    <strong>PDA Stack</strong>: [ {stack_visual} ]<br><br>
                    <em>{step['desc']}</em>
                </div>
            """, unsafe_allow_html=True)
            
            # Render a summary table in real-time
            table_data = []
            for s in simulated_steps:
                table_data.append({
                    "Langkah": s["step"],
                    "Kata": s["token"],
                    "Tipe": s["type"],
                    "FSA State": f"{s['prev_state'].upper()} -> {s['curr_state'].upper()}",
                    "PDA Stack": str(s["stack"]),
                    "Status": "✅ OK" if s["status"] == "success" or s["status"] == "info" else "❌ ERROR"
                })
            table_placeholder.table(table_data)
            
            progress_bar.progress((idx + 1) / len(steps))
            
            # Sleep based on chosen speed
            time.sleep(sim_speed[1])
            
        status_text.empty()
        st.write("---")
        
        # Show final results
        st.write("### 🏁 Hasil Akhir Analisis:")
        if is_valid:
            st.markdown(f"""
                <div class="success-alert" style="background-color: rgba(76, 175, 80, 0.1); border-color: #4CAF50; color: #81C784; padding: 24px;">
                    <h4 style="color: #81C784; margin-top: 0;">🎉 KALIMAT VALID!</h4>
                    <p style="font-size: 1.1rem; color: #ffffff; margin-bottom: 0;">
                        {translation_text}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown(f"""
                <div class="success-alert" style="background-color: rgba(244, 67, 54, 0.1); border-color: #f44336; color: #e57373; padding: 24px;">
                    <h4 style="color: #e57373; margin-top: 0;">❌ STRUKTUR TIDAK VALID</h4>
                    <p style="color: #ffffff; margin-bottom: 10px;">
                        Kalimat ditolak oleh sistem otomata Tobati.
                    </p>
                    <p style="font-size: 0.95rem; color: #ffcdd2; margin-bottom: 0; line-height: 1.5;">
                        <strong>Saran Perbaikan:</strong><br>{error_msg}
                    </p>
                </div>
            """, unsafe_allow_html=True)

render_footer()
