import streamlit as st
import os
import sys

# Add logic to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from logic.caesar_logic import caesar_encrypt, caesar_decrypt
from logic.vigenere_logic import vigenere_encrypt, vigenere_decrypt

# Page Config
st.set_page_config(page_title="Classic Ciphers", page_icon="🗝️", layout="wide")

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

st.markdown("<h1>Classic <span class='neon-text'>Ciphers</span></h1>", unsafe_allow_html=True)

col1, col2 = st.columns([0.7, 0.3])

with col1:
    tab1, tab2 = st.tabs(["Caesar", "Vigenere"])
    
    with tab1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="neon-text">Caesar Cipher Visualizer</h3>', unsafe_allow_html=True)
        c_msg = st.text_input("Plaintext (Caesar)", value="HELLO")
        c_shift = st.slider("Shift (Key)", 1, 25, 3)
        
        if st.button("Shifrlash", key="c_enc"):
            encrypted = caesar_encrypt(c_msg, c_shift)
            st.success(f"Natija: {encrypted}")
            st.markdown(f'<div class="formula-box">Enc(x) = (x + {c_shift}) mod 26</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="neon-text">Vigenere Cipher Visualizer</h3>', unsafe_allow_html=True)
        v_msg = st.text_input("Plaintext (Vigenere)", value="CRYPTOGRAPHY")
        v_key = st.text_input("Key (So'z)", value="KEY")
        
        if st.button("Shifrlash", key="v_enc"):
            encrypted = vigenere_encrypt(v_msg, v_key)
            st.success(f"Natija: {encrypted}")
            st.markdown(f'<div class="formula-box">Ci = (Pi + Ki) mod 26</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="theory-panel">
            <div class="theory-title">Nazariya</div>
            <p class="theory-text">
                <b>Sezar shifri:</b> Eng qadimgi shifrlash usullaridan biri. 
                Har bir harf alifboda ma'lum bir pozitsiyaga (shift) suriladi.
            </p>
            <div class="formula-box">
                E = (x + n) mod 26
            </div>
            <p class="theory-text" style="margin-top:20px;">
                <b>Vigenere shifri:</b> Polialfavit shifrlash usuli bo'lib, 
                Sezar shifridan farqli ravishda kalit so'zdan foydalanadi. 
                Bu usul Sezarga qaraganda ancha chidamli hisoblanadi.
            </p>
        </div>
    """, unsafe_allow_html=True)
