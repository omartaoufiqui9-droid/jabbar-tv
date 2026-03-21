
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
        st.video("https://www.youtube.com/watch?v=tC_69fLwI-Y") import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV - TEST", page_icon="🎬", layout="wide")

# 2. حالة الدخول
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# 3. التصميم (CSS) لمنع تداخل الأكواد
st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; }
    .test-card { border: 2px solid #E50914; padding: 10px; border-radius: 10px; margin-bottom: 20px; }
    h1, h2, h3 { text-align: center; color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- واجهة الدخول ---
if not st.session_state['authenticated']:
    st.markdown("<h1>JABBAR TV</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        name = st.text_input("أدخل اسمك للتجربة:")
        if st.button("دخول"):
            if name:
                st.session_state['authenticated'] = True
                st.rerun()
else:
    # --- واجهة تجربة الأقسام ---
    st.markdown("<h2>🧪 تجربة أقسام السينما</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🎥 تجربة الأفلام", "📺 تجربة المسلسلات", "🐥 تجربة الكرتون"])

    with tab1:
        st.subheader("تجربة تشغيل فيلم مباشر")
        st.markdown("<div class='test-card'>", unsafe_allow_html=True)
        # فيديو تجريبي 1 (Direct MP4)
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.subheader("تجربة تشغيل مسلسل مباشر")
        st.markdown("<div class='test-card'>", unsafe_allow_html=True)
        # فيديو تجريبي 2 (Direct MP4)
        st.video("https://media.w3.org/2010/05/sintel/trailer.mp4")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab3:
        st.subheader("تجربة تشغيل كرتون مباشر")
        st.markdown("<div class='test-card'>", unsafe_allow_html=True)
        # فيديو تجريبي 3 (Direct MP4)
        st.video("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.sidebar.button("تسجيل خروج"):
        st.session_state['authenticated'] = False
        st.rerun()
