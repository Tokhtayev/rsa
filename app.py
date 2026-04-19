import streamlit as st
import rsa_logic as rsa
import base64

# Page Config
st.set_page_config(
    page_title="RSA Antigravity Visualizer",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# --- CUSTOM COMPONENTS ---

def glass_card_start(title="", subtitle=""):
    st.markdown(f"""
        <div class="glass-card">
            <h3 style="margin-top:0; color:var(--accent-blue);">{title}</h3>
            <p style="color:var(--text-secondary); font-size:0.9rem;">{subtitle}</p>
    """, unsafe_allow_html=True)

def glass_card_end():
    st.markdown("</div>", unsafe_allow_html=True)

# --- APP LOGIC ---

st.markdown("<h1>RSA <span class='neon-text'>ANTIGRAVITY</span> VISUALIZER</h1>", unsafe_allow_html=True)

# Sidebar for Primes
with st.sidebar:
    st.markdown("<h2 class='neon-text'>Konfiguratsiya</h2>", unsafe_allow_html=True)
    st.write("RSA kalitlarini yaratish uchun ikkita tub sonni tanlang.")
    
    p = st.number_input("P (Tub son)", value=61, step=2)
    q = st.number_input("Q (Tub son)", value=53, step=2)
    
    if not rsa.is_prime(p) or not rsa.is_prime(q):
        st.warning("Iltimos, tub sonlarni kiriting!")
        st.stop()
    
    if p == q:
        st.warning("P va Q bir-biridan farq qilishi kerak!")
        st.stop()

    # Generate Keys
    public_key, private_key, phi = rsa.generate_keypair(p, q)
    n = public_key[1]
    e = public_key[0]
    d = private_key[0]

    st.success("Kalitlar muvaffaqiyatli yaratildi! ✅")
    
    st.markdown("### Public Key (e, n)")
    st.code(f"({e}, {n})")
    
    st.markdown("### Private Key (d, n)")
    st.code(f"({d}, {n})")

# Main Content
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    glass_card_start("Encryption", "Matnni shifrlash uchun bu yerga yozing.")
    message = st.text_input("Plaintext", value="HELLO")
    
    if st.button("Shifrlash (Encrypt)", key="encrypt_btn"):
        ciphertext = rsa.encrypt(public_key, message)
        st.session_state.ciphertext = ciphertext
        st.balloons()
    
    st.markdown("<br>", unsafe_allow_html=True)
    if 'ciphertext' in st.session_state:
        st.write("Shifrlangan ma'lumot (Ciphertext):")
        st.markdown(f"<div class='math-box'>{st.session_state.ciphertext}</div>", unsafe_allow_html=True)
    glass_card_end()

with col2:
    glass_card_start("Math Visualizer", "RSA algoritmi bosqichlari.")
    
    st.markdown(f"""
    <div style="font-size: 0.95rem;">
        <p>1. <b>N ni hisoblash:</b> n = p * q = {p} * {q} = <span class="neon-text">{n}</span></p>
        <p>2. <b>Eyler funksiyasi (Φ):</b> (p-1)*(q-1) = <span class="neon-text">{phi}</span></p>
        <p>3. <b>E (Public Exponent):</b> phi bilan o'zaro tub son: <span class="neon-text">{e}</span></p>
        <p>4. <b>D (Private Exponent):</b> e * d ≡ 1 (mod phi) -> <span class="neon-text">{d}</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("Bu matematik hisob-kitoblar RSA xavfsizligining asosidir.")
    glass_card_end()

st.markdown("<br><br>", unsafe_allow_html=True)

# Decryption Section
if 'ciphertext' in st.session_state:
    st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)
    # Using a wide column to center the floating result
    c1, mid, c2 = st.columns([1, 2, 1])
    with mid:
        glass_card_start("Decryption Result", "Asl matnga qaytarish.")
        if st.button("Deshifrlash (Decrypt)", key="decrypt_btn"):
            decrypted_msg = rsa.decrypt(private_key, st.session_state.ciphertext)
            st.markdown(f"""
                <div style="text-align:center;">
                    <h2 style="color:var(--accent-purple); margin-top:10px;">Deshifrlangan Matn:</h2>
                    <h1 style="-webkit-text-fill-color: var(--accent-blue);">{decrypted_msg}</h1>
                </div>
            """, unsafe_allow_html=True)
        glass_card_end()
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align:center; margin-top: 100px; color: var(--text-secondary); opacity: 0.5;">
    RSA Antigravity Visualization • Premium UI/UX Edition
</div>
""", unsafe_allow_html=True)
