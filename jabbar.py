import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. نظام حالة الدخول
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# 3. التصميم (CSS) الفخم لتجنب أخطاء التنسيق
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); }
    .movie-card { background: #1a1a1a; padding: 15px; border-radius: 15px; border: 1px solid #333; text-align: center; margin-bottom: 20px; }
    .main-title { color: white; text-align: center; font-size: 50px; font-family: 'Arial Black'; }
    .stButton>button { background-color: #E50914 !important; color: white !important; border-radius: 10px; width: 100%; height: 50px; font-weight: bold; border: none; }
</style>
""", unsafe_allow_html=True)

# --- واجهة الدخول ---
if not st.session_state['authenticated']:
    st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        name = st.text_input("أدخل اسمك للدخول إلى مكتبة جبار:")
        if st.button("دخول للسينما"):
            if name:
                st.session_state['authenticated'] = True
                st.rerun()

# --- واجهة السينما المنظمة ---
else:
    st.markdown("<h2 style='text-align:center; color:white;'>🎬 مكتبة جبار للأفلام الحقيقية</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🍿 جميع الأفلام", "📺 المسلسلات", "🐥 الكرتون"])

    with tab1:
        # السطر الأول (3 أفلام بجانب بعضها)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم أكشن 1")
            st.video("https://www.youtube.com/watch?v=kYI_sX8InB4")
            st.markdown("</div>", unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم أكشن 2")
            st.video("https://www.youtube.com/watch?v=qEvY-pY59oY")
            st.markdown("</div>", unsafe_allow_html=True)
        with c3:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم أكشن 3")
            st.video("https://www.youtube.com/watch?v=SfS_mXWqHZA")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.header("📺 قسم المسلسلات")
        st.video("https://www.youtube.com/watch?v=v64KOxKVzvo")

    with tab3:
        st.header("🐥 أفلام كرتون")
        st.video("https://www.youtube.com/watch?v=tC_69fLwI-Y") 
import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. اللغات (عربي وفرنسي مع قسم الكرتون)
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

# 3. التأكد من حالة الدخول
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# اختيار اللغة من الجانب
lang = st.sidebar.selectbox("🌐 Language / اللغة", ["العربية", "Français"])
t = translations[lang]

# 4. التصميم (CSS) الفخم الذي أعجبك
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
    input { text-align: center !important; direction: rtl; border-radius: 10px !important; color: black !important; }
    .stButton>button { background-color: #E50914 !important; color: white !important; font-weight: bold; width: 100%; height: 45px; border:none; border-radius: 10px; }
    .movie-card { background: #1a1a1a; padding: 10px; border-radius: 15px; border: 1px solid #333; margin-bottom: 20px; }
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

# --- واجهة المحتوى (أفلام، مسلسلات، كرتون) ---
else:
    st.sidebar.success(f"مرحباً {st.session_state['user_name']}")
    if st.sidebar.button("خروج / Logout"):
        st.session_state['authenticated'] = False
        st.rerun()

    st.markdown(f"<h2 style='color:white; text-align:center;'>{t['welcome']}</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([t['movies'], t['series'], t['kids']])
    
    with tab1:
        st.header("🎞️ مكتبة الأفلام")
        # عرض الأفلام في مربعات (3 أعمدة)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم القناص")
            st.video("https://www.youtube.com/watch?v=S3IDV-p7fIs")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم أكشن 2")
            st.video("https://www.youtube.com/watch?v=9ay66723-K0")
            st.markdown("</div>", unsafe_allow_html=True)
        with col3:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم مغامرات")
            st.video("https://www.youtube.com/watch?v=5Uf_NInR8Yc")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.header("📺 المسلسلات")
        st.video("https://www.youtube.com/watch?v=v64KOxKVzvo")

    with tab3:
        st.header("🐥 أفلام كرتون")
        st.video("https://www.youtube.com/watch?v=tC_69fLwI-Y")
