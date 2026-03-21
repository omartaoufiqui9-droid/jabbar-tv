
import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. قاموس اللغات (Translations)
translations = {
    "Français": {
        "welcome": "VOTRE CINÉMA À DOMICILE",
        "user_label": "Identifiant",
        "pass_label": "Mot de passe",
        "login_btn": "ACCÉDER",
        "header": "🎬 Bibliothèque de JABBAR",
        "logout": "Déconnexion"
    },
    "العربية": {
        "welcome": "سينما منزلك الخاصة",
        "user_label": "اسم المستخدم",
        "pass_label": "كلمة المرور",
        "login_btn": "دخول",
        "header": "🎬 مكتبة جبار الشخصية",
        "logout": "خروج"
    },
    "English": {
        "welcome": "YOUR HOME CINEMA",
        "user_label": "Username",
        "pass_label": "Password",
        "login_btn": "ACCESS",
        "header": "🎬 JABBAR's Library",
        "logout": "Logout"
    }
}

# 3. اختيار اللغة في الشريط الجانبي
st.sidebar.title("🌐 Language")
lang = st.sidebar.selectbox("Choisir / اختر", list(translations.keys()))
t = translations[lang]

# 4. تصميم CSS (نفس التصميم الفخم في صورتك)
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); }
    .logo-box { 
        display: block; margin: 0 auto; width: 100px; height: 100px; 
        background: #E50914; color: white; text-align: center; 
        line-height: 100px; font-size: 70px; font-family: 'Arial Black'; 
        border-radius: 20px; box-shadow: 0px 0px 30px #ff0000;
    }
    .main-title { color: white; text-align: center; font-size: 60px; font-family: 'Arial Black'; margin-top: 10px; }
    .stButton>button { background-color: #E50914 !important; color: white !important; font-weight: bold; width: 100%; border: none; height: 50px; }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<div class='logo-box'>J</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#888; letter-spacing: 2px;'>{t['welcome']}</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.text_input(t['user_label'])
        st.text_input(t['pass_label'], type="password")
        if st.button(t['login_btn']):
            st.session_state['auth'] = True
            st.rerun()
else:
    # واجهة المكتبة المترجمة
    col_h, col_l = st.columns([0.8, 0.2])
    with col_h: st.markdown(f"<h1 style='color: white;'>{t['header']}</h1>", unsafe_allow_html=True)
    with col_l: 
        if st.button(t['logout']): 
            st.session_state['auth'] = False
            st.rerun()
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
