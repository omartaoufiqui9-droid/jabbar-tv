
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

# 3. التصميم (CSS) - الشكل الفخم الذي طلبته
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

# --- واجهة عرض الأفلام ---
else:
    st.sidebar.success(f"مرحباً {st.session_state['user_name']}")
    if st.sidebar.button("خروج"):
        st.session_state['authenticated'] = False
        st.rerun()

    st.markdown(f"<h2 style='color:white; text-align:center;'>{t['welcome']}</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([t['movies'], t['series'], t['kids']])
    
    with tab1:
        st.header("🎞️ مكتبة الأفلام")
        
        # السطر الأول (3 أفلام)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<div class='movie-box'>", unsafe_allow_html=True)
            st.subheader("فيلم أكشن 1")
            st.video("https://www.youtube.com/watch?v=S3IDV-p7fIs")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='movie-box'>", unsafe_allow_html=True)
            st.subheader("فيلم أكشن 2")
            st.video("https://www.youtube.com/watch?v=9ay66723-K0")
            st.markdown("</div>", unsafe_allow_html=True)
        with col3:
            st.markdown("<div class='movie-box'>", unsafe_allow_html=True)
            st.subheader("فيلم مغامرات")
            st.video("https://www.youtube.com/watch?v=5Uf_NInR8Yc")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")

        # السطر الثاني (3 أفلام أخرى)
        col4, col5, col6 = st.columns(3)
        with col4:
            st.markdown("<div class='movie-box'>", unsafe_allow_html=True)
            st.subheader("فيلم خيال")
            st.video("https://www.youtube.com/watch?v=v64KOxKVzvo")
            st.markdown("</div>", unsafe_allow_html=True)
        with col5:
            st.markdown("<div class='movie-box'>", unsafe_allow_html=True)
            st.subheader("فيلم تشويق")
            st.video("https://www.youtube.com/watch?v=SfS_mXWqHZA")
            st.markdown("</div>", unsafe_allow_html=True)
        with col6:
            st.markdown("<div class='movie-box'>", unsafe_allow_html=True)
            st.subheader("فيلم جديد")
            st.video("https://www.youtube.com/watch?v=mY9n7K6fOAs")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.header("📺 قسم المسلسلات")
        st.write("سيتم إضافة الحلقات هنا قريباً...")

    with tab3:
        st.header("🐥 أفلام كرتون")
        st.video("https://www.youtube.com/watch?v=tC_69fLwI-Y")
