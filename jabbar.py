import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. نظام اللغات
translations = {
    "العربية": {
        "welcome": "سينما منزلك الخاصة",
        "user_label": "أدخل اسمك للمشاهدة:",
        "login_btn": "دخول للمكتبة",
        "movies": "🎬 أفلام أكشن مترجمة",
        "series": "📺 مسلسلات",
        "kids": "🐥 أفلام كرتون"
    },
    "Français": {
        "welcome": "VOTRE CINÉMA À DOMICILE",
        "user_label": "Entrez votre nom :",
        "login_btn": "ACCÉDER",
        "movies": "🎬 Films d'Action",
        "series": "📺 Séries TV",
        "kids": "🐥 Dessins Animés"
    }
}

# 3. إدارة حالة الدخول
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

lang = st.sidebar.selectbox("🌐 Language / اللغة", ["العربية", "Français"])
t = translations[lang]

# 4. التصميم (CSS) - إصلاح شامل لتجنب الأخطاء
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
    input { text-align: center !important; border-radius: 10px !important; }
    .stButton>button { background-color: #E50914 !important; color: white !important; font-weight: bold; width: 100%; border:none; border-radius: 10px; }
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

# --- واجهة المحتوى ---
else:
    st.sidebar.success(f"مرحباً {st.session_state['user_name']}")
    if st.sidebar.button("خروج / Logout"):
        st.session_state['authenticated'] = False
        st.rerun()

    st.markdown(f"<h2 style='color:white; text-align:center;'>{t['welcome']}</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([t['movies'], t['series'], t['kids']])
    
    with tab1:
        st.header("🔥 أفلام أكشن حقيقية (مترجمة)")
        st.subheader("1. فيلم القناص المحترف")
        st.video("https://www.youtube.com/watch?v=S3IDV-p7fIs")
        st.markdown("---")
        st.subheader("2. فيلم المهمة المستحيلة")
        st.video("https://www.youtube.com/watch?v=9ay66723-K0")

    with tab2:
        st.header("📺 قسم المسلسلات")
        st.info("جاري إضافة أحدث المسلسلات...")
        st.video("https://www.youtube.com/watch?v=v64KOxKVzvo")
        
    with tab3:
        st.header("🐥 أفلام كرتون ممتعة")
        st.video("https://www
