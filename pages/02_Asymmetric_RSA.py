import streamlit as st
import os
import sys

# Add logic to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import logic.rsa_logic as rsa

# Page Config
st.set_page_config(page_title="RSA Visualizer", page_icon="🔮", layout="wide")

# Load CSS
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
local_css("style.css")

st.markdown("<h1>RSA <span class='neon-text'>Algorithm</span></h1>", unsafe_allow_html=True)

col1, col2 = st.columns([0.7, 0.3])

with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h3 class="neon-text">Asimmetrik Shifrlash Panel</h3>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        p = st.number_input("P (Tub son)", value=61, step=2)
    with c2:
        q = st.number_input("Q (Tub son)", value=53, step=2)
    
    if rsa.is_prime(p) and rsa.is_prime(q) and p != q:
        public_key, private_key, phi = rsa.generate_keypair(p, q)
        n = public_key[1]
        e = public_key[0]
        d = private_key[0]
        
        st.info(f"Kalitlar: Public({e}, {n}) | Private({d}, {n})")
        
        msg = st.text_input("Plaintext", value="HELLO")
        if st.button("Shifrlash (RSA)"):
            ciphertext = rsa.encrypt(public_key, msg)
            st.write("Shifrlangan ma'lumot:")
            st.code(ciphertext)
            
            decrypted = rsa.decrypt(private_key, ciphertext)
            st.success(f"Deshifrlangan: {decrypted}")
    else:
        st.warning("Iltimos, har xil tub sonlarni tanlang.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="theory-panel">
            <div class="theory-title">RSA Nazariyasi</div>
            <p class="theory-text">
                RSA — birinchi va eng mashhur asimmetrik shifrlash algoritmi. 
                U ikki xil kalitdan foydalanadi: Ommaviy (Public) va Maxfiy (Private).
            </p>
            <div class="formula-box">
                1. n = p * q <br>
                2. &phi; = (p-1)(q-1) <br>
                3. e * d &equiv; 1 (mod &phi;)
            </div>
            <p class="theory-text" style="font-size:0.85rem;">
                Tizim xavfsizligi katta sonlarni ko'paytuvchilarga ajratish (factorization) qiyinligiga asoslangan.
            </p>
        </div>
    """, unsafe_allow_html=True)
