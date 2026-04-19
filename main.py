import streamlit as st
import os

# Page Config
st.set_page_config(
    page_title="Cryptographic Lab",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

# --- DASHBOARD ---
st.markdown("<h1>Cryptographic <span class='neon-text'>Lab</span></h1>", unsafe_allow_html=True)

col1, col2 = st.columns([0.7, 0.3])

with col1:
    st.markdown("""
        <div class="glass-card">
            <h2 class="neon-text">Xush Kelibsiz!</h2>
            <p style="color:var(--text-secondary); font-size:1.1rem; line-height:1.6;">
                Bu laboratoriya kriptografiya olamiga interaktiv sayohat qilish uchun mo'ljallangan. 
                Bu yerda siz klassik shifrlardan tortib, zamonaviy asimmetrik shifrlash va xesh-funksiyalarigacha bo'lgan 
                jarayonlarni vizual tarzda o'rganishingiz mumkin.
            </p>
            <br>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:15px; border-left:4px solid var(--accent-blue);">
                    <h3 style="color:var(--accent-blue); margin:0;">Modulli Tizim</h3>
                    <p style="color:var(--text-secondary); font-size:0.9rem;">Har bir algoritm alohida modul sifatida ajratilgan.</p>
                </div>
                <div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:15px; border-left:4px solid var(--accent-purple);">
                    <h3 style="color:var(--accent-purple); margin:0;">Vizual Ta'lim</h3>
                    <p style="color:var(--text-secondary); font-size:0.9rem;">Matematika va amaliyotni bir vaqtning o'zida ko'ring.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card">
            <h3 class="neon-text">Laboratoriya Maqsadi</h3>
            <p style="color:var(--text-secondary);">
                Kriptografik laboratoriyaning asosiy maqsadi — talabalarga algoritmlarning ishlash prinsipini 
                shunchaki quruq formulalar orqali emas, balki real vaqtda o'zgaruvchi vizual elementlar orqali tushuntirishdir.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="theory-panel">
            <div class="theory-title">Stats & Info</div>
            <div class="formula-box">
                Active Modules: 4<br>
                Style: Antigravity<br>
                Powered by: Streamlit
            </div>
            <p class="theory-text">
                Kriptografiya — bu ma'lumotlar maxfiyligini ta'minlash haqidagi fan. 
                Laboratoriya quyidagi bo'limlardan iborat:
                <ul style="color:var(--text-secondary); padding-left:20px;">
                    <li>Klassik Shifrlar</li>
                    <li>RSA (Asimmetrik)</li>
                    <li>SHA-256 (Hashing)</li>
                </ul>
            </p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align:center; margin-top: 50px; color: var(--text-secondary); opacity: 0.5;">
    Cryptographic Lab • Future of Education • by Tokhtayev
</div>
""", unsafe_allow_html=True)
