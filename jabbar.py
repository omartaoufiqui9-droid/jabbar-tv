import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. اللغات (إضافة قسم الكرتون)
translations = {
    "العربية": {
        "welcome": "سينما منزلك الخاصة",
        "user_label": "أدخل اسمك للمشاهدة:",
        "login_btn": "دخول للمكتبة",
        "movies": "🎬 أفلام",
        "series": "📺 مسلسلات",
        "kids": "🐥 أفلام كرتون",
        "logout": "خروج"
    },
    "Français": {
        "welcome": "VOTRE CINÉMA À DOMICILE",
        "user_label": "Entrez votre nom :",
        "login_btn": "ACCÉDER",
        "movies": "🎬 Films",
        "series": "📺 Séries",
        "kids": "🐥 Dessins Animés",
        "logout": "Quitter"
    }
}

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

lang = st.sidebar.selectbox("🌐 Language / اللغة", ["العربية", "Français"])
t = translations[lang]

# 4. التصميم (CSS)
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); }
    .logo-box { 
        display: block; margin: 0 auto; width: 80px; height: 80px; 
        background: #E50914; color: white; text-align: center; 
        line-height: 80px; font-size: 50px; font-family: 'Arial Black'; 
        border-radius: 15px; box-shadow: 0px 0px 20px #ff0000;
    }
    .main-title { color: white; text-align: center; font-size: 50px; font-family: 'Arial Black'; }
    .stButton>button { background-color: #E50914 !important; color: white !important; border-radius: 10px; border:none; }
</style>
""", unsafe_allow_html=True)

# --- واجهة الدخول ---
if not st.session_state['authenticated']:
    st.markdown("<div class='logo-box'>J</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#888;'>{t['welcome']}</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        name_input = st.text_input(t['user_label'], key="user_name_input")
        if st.button(t['login_btn']):
            if name_input:
                st.session_state['authenticated'] = True
                st.session_state['user_name'] = name_input
                st.rerun()
else:
    # --- واجهة المحتوى (3 أقسام) ---
    st.sidebar.success(f"أهلاً {st.session_state['user_name']}")
    if st.sidebar.button(t['logout']):
        st.session_state['authenticated'] = False
        st.rerun()

    st.markdown(f"<h2 style='color:white; text-align:center;'>{t['welcome']}
