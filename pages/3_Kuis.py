# -*- coding: utf-8 -*-
"""
Streamlit page: Game Kuis Budaya Papua.
Features a 5-level trivia game with visual feedback and rewards.
"""
import streamlit as st
from backend.styles import apply_custom_styles, render_header, render_footer
from backend.game import get_level_questions, calculate_level_score, LEVEL_TITLES, LEVEL_POINTS

# Apply custom styles & header
apply_custom_styles()
render_header()

# Initialize session state variables for the game
if "quiz_state" not in st.session_state:
    st.session_state.quiz_state = "intro" # intro, playing, level_done, game_done
if "current_level" not in st.session_state:
    st.session_state.current_level = 1
if "question_idx" not in st.session_state:
    st.session_state.question_idx = 0
if "level_correct" not in st.session_state:
    st.session_state.level_correct = 0
if "total_score" not in st.session_state:
    st.session_state.total_score = 0
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None
if "level_scores" not in st.session_state:
    st.session_state.level_scores = {} # stores scores for each level

# Functions to modify states
def start_game():
    st.session_state.quiz_state = "playing"
    st.session_state.question_idx = 0
    st.session_state.level_correct = 0
    st.session_state.selected_option = None

def reset_game():
    st.session_state.quiz_state = "intro"
    st.session_state.current_level = 1
    st.session_state.question_idx = 0
    st.session_state.level_correct = 0
    st.session_state.total_score = 0
    st.session_state.selected_option = None
    st.session_state.level_scores = {}

# Page title
st.markdown("## 🎮 Game Kuis: Pelestari Budaya Papua")
st.markdown("Uji pengetahuanmu mengenai adat istiadat, tarian, pakaian, makanan, dan sejarah suku-suku Papua.")

# --- INTRO STATE ---
if st.session_state.quiz_state == "intro":
    st.markdown("""
        <div class="custom-card" style="padding: 30px; border-color: #e5a93c;">
            <h3 style="color: #e5a93c; text-align: center; margin-bottom: 20px;">Selamat Datang di Arena Kuis Etnik Papua!</h3>
            <p style="text-align: center; color: #9ca3af; font-size: 1.1rem; line-height: 1.6;">
                Selesaikan 5 level tantangan kebudayaan. Setiap level memiliki 5 pertanyaan pilihan ganda.<br>
                Semakin tinggi level, semakin besar poin yang bisa Anda dapatkan!
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("### 🏆 Papan Level & Poin:")
    cols = st.columns(5)
    for lvl in range(1, 6):
        pts = LEVEL_POINTS[lvl]
        title = LEVEL_TITLES[lvl].split(":")[1]
        with cols[lvl-1]:
            completed_str = "✅ Selesai" if lvl in st.session_state.level_scores else "🔒 Belum dikerjakan"
            score_str = f"Poin: {st.session_state.level_scores[lvl]}" if lvl in st.session_state.level_scores else f"Max Poin: {pts}"
            st.markdown(f"""
                <div class="custom-card" style="text-align: center; padding: 16px; min-height: 200px; border-color: rgba(229,169,60,0.3);">
                    <div style="font-size: 1.8rem; margin-bottom: 8px;">Level {lvl}</div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: #e5a93c; margin-bottom: 8px;">{title}</div>
                    <div style="font-size: 0.8rem; color: #9ca3af; margin-bottom: 8px;">{score_str}</div>
                    <div style="font-size: 0.75rem; color: #c84b31; font-weight: 700;">{completed_str}</div>
                </div>
            """, unsafe_allow_html=True)
            
    st.write("---")
    
    col_start, col_reset = st.columns([1, 1])
    with col_start:
        # Check if they have unfinished levels
        next_undone_level = 1
        for l in range(1, 6):
            if l not in st.session_state.level_scores:
                next_undone_level = l
                break
        
        st.session_state.current_level = next_undone_level
        level_title = LEVEL_TITLES[st.session_state.current_level]
        
        if len(st.session_state.level_scores) < 5:
            if st.button(f"🚀 Mulai {level_title}"):
                start_game()
                st.rerun()
        else:
            st.success("Selamat! Anda telah menyelesaikan semua level kuis!")
            st.balloons()
            
    with col_reset:
        if st.button("🔄 Ulangi Seluruh Kuis"):
            reset_game()
            st.rerun()

# --- PLAYING STATE ---
elif st.session_state.quiz_state == "playing":
    level = st.session_state.current_level
    q_idx = st.session_state.question_idx
    questions = get_level_questions(level)
    
    if q_idx < len(questions):
        q = questions[q_idx]
        
        st.markdown(f"#### 🏷️ {LEVEL_TITLES[level]}")
        st.markdown(f"**Soal {q_idx + 1} dari 5**")
        
        # Progress bar
        st.progress((q_idx) / 5.0)
        
        # Grid: Left Image, Right Question & Options
        col_img, col_q = st.columns([0.8, 1.2])
        
        with col_img:
            # Display mapped image
            st.image(q["image"], caption="Ilustrasi Budaya Papua", use_container_width=True)
            
        with col_q:
            st.markdown(f"""
                <div class="custom-card" style="border-color: rgba(229,169,60,0.3); margin-bottom: 15px;">
                    <p style="font-size: 1.1rem; font-weight: 600; line-height: 1.5; color: #ffffff; margin: 0;">{q['question']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Answer selections using radio / buttons
            selected_option = st.radio("Pilih jawaban yang benar:", q["options"], index=None, key=f"q_radio_{q['id']}")
            
            st.write("")
            
            if st.button("Kirim Jawaban"):
                if selected_option is None:
                    st.warning("Silakan pilih salah satu opsi jawaban!")
                else:
                    st.session_state.selected_option = selected_option
                    st.session_state.quiz_state = "check_answer"
                    st.rerun()
                    
# --- CHECK ANSWER STATE ---
elif st.session_state.quiz_state == "check_answer":
    level = st.session_state.current_level
    q_idx = st.session_state.question_idx
    questions = get_level_questions(level)
    q = questions[q_idx]
    
    st.markdown(f"#### 🏷️ {LEVEL_TITLES[level]}")
    st.markdown(f"**Hasil Soal {q_idx + 1} dari 5**")
    
    col_img, col_q = st.columns([0.8, 1.2])
    with col_img:
        st.image(q["image"], caption="Ilustrasi Budaya Papua", use_container_width=True)
        
    with col_q:
        user_ans = st.session_state.selected_option
        correct_ans = q["answer"]
        is_correct = (user_ans == correct_ans)
        
        if is_correct:
            st.markdown(f"""
                <div class="success-alert" style="background-color: rgba(76, 175, 80, 0.1); border-color: #4CAF50; color: #81C784;">
                    <span style="font-size: 1.4rem;">🟢 Jawaban Benar!</span>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="success-alert" style="background-color: rgba(244, 67, 54, 0.1); border-color: #f44336; color: #e57373;">
                    <span style="font-size: 1.4rem;">🔴 Jawaban Salah!</span><br>
                    Jawaban Anda: <strong>{user_ans}</strong>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown(f"""
            <div class="custom-card" style="border-color: rgba(229,169,60,0.15);">
                <strong>Kunci Jawaban</strong>: <span style="color: #e5a93c;">{correct_ans}</span><br><br>
                <strong>Penjelasan</strong>:<br>{q['explanation']}
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Lanjutkan"):
            # Update score if correct
            if is_correct:
                st.session_state.level_correct += 1
                
            # Go to next question
            st.session_state.question_idx += 1
            st.session_state.selected_option = None
            
            # If finished all questions in level
            if st.session_state.question_idx >= 5:
                # Calculate level score
                level_score = calculate_level_score(st.session_state.level_correct, level)
                st.session_state.level_scores[level] = level_score
                st.session_state.total_score += level_score
                st.session_state.quiz_state = "level_done"
            else:
                st.session_state.quiz_state = "playing"
            st.rerun()

# --- LEVEL COMPLETED STATE ---
elif st.session_state.quiz_state == "level_done":
    level = st.session_state.current_level
    correct = st.session_state.level_correct
    score = st.session_state.level_scores[level]
    max_pts = LEVEL_POINTS[level]
    
    st.balloons()
    
    st.markdown(f"### 🎉 Level {level} Selesai!")
    
    st.markdown(f"""
        <div class="custom-card" style="text-align: center; border-color: #e5a93c; padding: 40px 20px;">
            <div style="font-size: 4rem; margin-bottom: 10px;">🏆</div>
            <h3 style="color: #e5a93c; margin-bottom: 10px;">Apresiasi Hasil Kerja Keras Anda!</h3>
            <p style="font-size: 1.3rem; color: #ffffff; margin-bottom: 20px;">
                Anda menjawab benar <strong>{correct} dari 5 soal</strong>.
            </p>
            <div style="display: inline-block; padding: 12px 30px; background: rgba(229, 169, 60, 0.1); border: 2px solid #e5a93c; border-radius: 12px; font-size: 1.5rem; font-weight: 700; color: #f5d082; margin-bottom: 20px;">
                Poin Diperoleh: +{score} / {max_pts}
            </div>
            <p style="color: #9ca3af; max-width: 600px; margin: 0 auto; line-height: 1.6;">
                Terima kasih telah berpartisipasi menjaga warisan tradisi Papua. Pengetahuan Anda sangat berharga bagi pelestarian ini.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if level < 5:
            if st.button("➡️ Lanjut ke Level Berikutnya"):
                st.session_state.current_level += 1
                start_game()
                st.rerun()
        else:
            if st.button("🏁 Lihat Hasil Akhir Kuis"):
                st.session_state.quiz_state = "game_done"
                st.rerun()
    with col2:
        if st.button("🏠 Kembali ke Beranda Kuis"):
            st.session_state.quiz_state = "intro"
            st.rerun()

# --- GAME COMPLETED STATE ---
elif st.session_state.quiz_state == "game_done":
    st.balloons()
    st.markdown("### 👑 Selamat! Anda Telah Menamatkan Kuis Budaya Papua!")
    
    total_earned = sum(st.session_state.level_scores.values())
    max_total = sum(LEVEL_POINTS.values())
    
    st.markdown(f"""
        <div class="custom-card" style="text-align: center; border-color: #c84b31; padding: 40px 20px;">
            <div style="font-size: 5rem; margin-bottom: 10px;">🏅</div>
            <h2 style="color: #e5a93c; margin-bottom: 10px;">Gelar: Penjaga Agung Budaya Papua</h2>
            <p style="font-size: 1.2rem; color: #9ca3af; margin-bottom: 20px;">
                Anda telah menyelesaikan seluruh 5 level kuis kebudayaan Papua.
            </p>
            <div style="font-size: 2.2rem; font-weight: 900; color: #c84b31; text-shadow: 0 0 15px rgba(200,75,49,0.3); margin-bottom: 20px;">
                Total Skor: {total_earned} / {max_total} Poin
            </div>
            <p style="color: #f3f4f6; max-width: 600px; margin: 0 auto 20px; line-height: 1.6;">
                Pengetahuan Anda tentang Suku Asmat, Dani, Amungme, Kamoro, Biak, dan Sentani sangat luar biasa! 
                Anda kini resmi dinobatkan sebagai <strong>Duta Digital Pelestarian Papua 2026</strong>.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("### Rincian Poin per Level:")
    cols = st.columns(5)
    for lvl in range(1, 6):
        pts = st.session_state.level_scores.get(lvl, 0)
        max_pts = LEVEL_POINTS[lvl]
        with cols[lvl-1]:
            st.markdown(f"""
                <div class="custom-card" style="text-align: center; padding: 12px; border-color: rgba(229,169,60,0.15);">
                    <strong>Level {lvl}</strong><br>
                    <span style="color: #e5a93c; font-size: 1.2rem; font-weight: 700;">{pts}/{max_pts}</span>
                </div>
            """, unsafe_allow_html=True)
            
    st.write("---")
    if st.button("🔄 Main Lagi dari Awal"):
        reset_game()
        st.rerun()

render_footer()
