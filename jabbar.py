import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. نظام اللغات
translations = {
    "العربية": {
        "welcome": "سينما منزلك الخاصة",
        "user_label": "أدخل اسمك للمشاهدة:",
        "login_btn": "دخول للمكتبة",
        "movies": "🎬 قسم الأفلام",
        "series": "📺 قسم المسلسلات",
        "kids": "🐥 أفلام كرتون"
    },
    "Français": {
        "welcome": "VOTRE CINÉMA À DOMICILE",
        "user_label": "Entrez votre nom :",
        "login_btn": "ACCÉDER",
        "movies": "🎬 Section Films",
        "series": "📺 Section Séries",
        "kids": "🐥 Dessins Animés"
    }
}

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

lang = st.sidebar.selectbox("🌐 Language / اللغة", ["العربية", "Français"])
t = translations[lang]

# 3. التصميم (CSS) - الشكل الفخم (تم إصلاح الأقواس)
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); }
    .logo-box { 
        display: block; margin: 0 auto; width: 80px; height: 80px; 
        background: #E50914; color: white; text-align: center; 
        line-height: 80px; font-size: 50px; font-family: 'Arial Black'; 
        border-radius: 15px; box-shadow: 0px 0px 20px #ff0000;
    }
    .main-title { color: white; text-align: center; font-size: 40px; font-family: 'Arial Black'; }
    input { text-align: center !important; border-radius: 10px !important; color: black !important; }
    .stButton>button { background-color: #E50914 !important; color: white !important; font-weight: bold; width: 100%; border-radius: 10px; height: 45px; border:none; }
    .movie-box { background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 15px; border: 1px solid #333; margin-bottom: 20px; text-align: center; }
    h3, h2, h1 { color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- واجهة الدخول ---
if not st.session_state['authenticated']:
    st.markdown("<div class='logo-box'>J</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#888;'>{t['welcome']}</p>", unsafe_allow_html=True)
    
    col_login1, col_login2, col_login3 = st.columns([1, 1.2, 1])
    with col_login2:
        name_input = st.text_input(t['user_label'], key="user_name_input")
        if st.button(t['login_btn']):
            if name_input:
                st.session_state['authenticated'] = True
                st.session_state['user_name'] = name_input
                st.rerun()

# --- واجهة عرض المحتوى التجريبي ---
else:
    st.sidebar.success(f"مرحباً {st.session_state['user_name']}")
    if st.sidebar.button("خروج"):
        st.session_state['authenticated'] = False
        st
