import streamlit as st
import os
import sys

# Add logic to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from logic.hash_logic import calculate_sha256, get_avalanche_info

# Page Config
st.set_page_config(page_title="Hash Functions", page_icon="🔗", layout="wide")

# Load CSS
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
local_css("style.css")

# --- CUSTOM SIDEBAR BRANDING ---
st.sidebar.markdown(f"""
    <div style="text-align:center; padding: 20px 0;">
        <h1 style="color:var(--accent-blue); font-size: 2.2rem; margin-bottom:0;">CRYPTOGRAM</h1>
        <p style="color:var(--accent-purple); font-size: 0.8rem; letter-spacing: 3px; font-weight:bold; margin-top:0;">ADVANCED LAB</p>
        <hr style="border-top: 1px solid var(--border-color); width: 80%; margin: 20px auto;">
    </div>
""", unsafe_allow_html=True)

st.markdown("<h1>Hash <span class='neon-text'>Functions</span></h1>", unsafe_allow_html=True)

col1, col2 = st.columns([0.7, 0.3])

with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h3 class="neon-text">SHA-256 Visualizer</h3>', unsafe_allow_html=True)
    
    h_msg = st.text_input("Input Text", value="Cryptography")
    
    if h_msg:
        h_result = calculate_sha256(h_msg)
        st.write("SHA-256 Hash:")
        st.markdown(f'<div class="formula-box" style="word-break: break-all; color:var(--accent-blue);">{h_result}</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown('<h4 class="neon-text">Avalanche Effect (Ko\'chki Effekti)</h4>', unsafe_allow_html=True)
        st.write("Agar matndan bor-yo'g'i bitta harfni o'zgartirsak nima bo'ladi?")
        
        av_data = get_avalanche_info(h_msg)
        
        st.write(f"O'zgartirilgan matn: `{av_data['modified_input']}`")
        st.write("Yangi Xesh:")
        st.markdown(f'<div class="formula-box" style="word-break: break-all; color:var(--accent-purple);">{av_data["modified"]}</div>', unsafe_allow_html=True)
        
        st.metric("O'zgargan bitlar soni", f"{av_data['diff_bits']} / 256", f"{av_data['percentage']:.1f}%")
        st.info("Ko'rib turganingizdek, kiruvchi ma'lumotning kichik o'zgarishi butunlay boshqa xat hosil qiladi.")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="theory-panel">
            <div class="theory-title">Xesh Funksiyalar</div>
            <p class="theory-text">
                Xesh-funksiya — har qanday o'lchamdagi ma'lumotni belgilangan qat'iy o'lchamdagi (SHA-256 uchun 256 bit) 
                matnga o'zgartirib beradi.
            </p>
            <div class="formula-box">
                y = H(x)
            </div>
            <p class="theory-text">
                Asosiy xususiyatlari:
                <ul style="color:var(--text-secondary); padding-left:20px;">
                    <li>Qaytmaslik (One-way)</li>
                    <li>Deterministik (Bir xil kirish = bir xil chiqish)</li>
                    <li>Kolliziyaga chidamlilik</li>
                </ul>
            </p>
        </div>
    """, unsafe_allow_html=True)
