import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. قاموس الترجمة (عربي / فرنسي)
translations = {
    "العربية": {
        "welcome": "سينما منزلك الخاصة",
        "user_label": "أدخل اسمك للمشاهدة:",
        "login_btn": "دخول للمكتبة",
        "movies": "🎬 قسم الأفلام",
        "series": "📺 قسم المسلسلات",
        "logout": "خروج"
    },
    "Français": {
        "welcome": "VOTRE CINÉMA À DOMICILE",
        "user_label": "Entrez votre nom :",
        "login_btn": "ACCÉDER",
        "movies": "🎬 Section Films",
        "series": "📺 Section Séries",
        "logout": "Déconnexion"
    }
}

# 3. اختيار اللغة من الجانب
lang = st.sidebar.selectbox("🌐 Language / اللغة", ["العربية", "Français"])
t = translations[lang]

# 4. تصميم الواجهة (CSS)
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
    input { text-align: center !important; direction: rtl; }
    .stButton>button { background-color: #E50914 !important; color: white !important; font-weight: bold; width: 100%; border-radius: 10px; height: 45px; border:none; }
</style>
""", unsafe_allow_html=True)

# 5. إدارة حالة الدخول (Session State)
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

# --- الحالة 1: إذا لم يسجل الدخول (تظهر الواجهة الأولى) ---
if not st.session_state['auth']:
    st.markdown("<div class='logo-box'>J</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#888;'>{t['welcome']}</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        username = st.text_input(t['user_label'], placeholder="...")
        if st.button(t['login_btn']):
            if username:
                st.session_state['auth'] = True
                st.session_state['name'] = username
                st.rerun()

# --- الحالة 2: بعد كتابة الاسم (تظهر الأفلام) ---
else:
    st.sidebar.write(f"👤 {st.session_state['name']}")
    if st.sidebar.button(t['logout']):
        st.session_state['auth'] = False
        st.rerun()

    tab1, tab2 = st.tabs([t['movies'], t['series']])
    
    with tab1:
        st.markdown("<h3 style='color:white;'>الأفلام المتاحة</h3>", unsafe_allow_html=True)
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
        
    with tab2:
        st.markdown("<h3 style='color:white;'>المسلسلات المتاحة</h3>", unsafe_allow_html=True)
        st.video("https://media.w3.org/2010/05/sintel/trailer.mp4")
