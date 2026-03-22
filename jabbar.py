


import streamlit as st

# 1. إعدادات الصفحة والتصميم
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# تصميم الواجهة بالألوان التي تحبها
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); }
    .logo-box { background: #E50914; color: white; text-align: center; padding: 10px; border-radius: 15px; font-size: 50px; font-weight: bold; box-shadow: 0 0 20px #ff0000; width: 80px; margin: 0 auto; }
    h1, h2, h3, p { color: white !important; text-align: center; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center; }
    .stTabs [data-baseweb="tab"] { color: #888; font-weight: bold; }
    .stTabs [aria-selected="true"] { color: #E50914 !important; border-bottom-color: #E50914 !important; }
</style>
""", unsafe_allow_html=True)

# 2. نظام اللغات
lang = st.sidebar.selectbox("🌐 Language / اللغة", ["العربية", "Français"])
t = {
    "العربية": {"w": "سينما منزلك الخاصة", "u": "أدخل اسمك للمشاهدة:", "b": "دخول", "m": "🎬 قسم الأفلام", "s": "📺 قسم المسلسلات", "k": "🐥 أفلام كرتون"},
    "Français": {"w": "VOTRE CINÉMA À DOMICILE", "u": "Entrez votre nom :", "b": "ACCÉDER", "m": "🎬 Films", "s": "📺 Séries", "k": "🐥 Enfants"}
}[lang]

# 3. نظام الدخول والترحيب
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<div class='logo-box'>J</div>", unsafe_allow_html=True)
    st.markdown(f"<h1>JABBAR TV</h1><p>{t['w']}</p>", unsafe_allow_html=True)
    name = st.text_input(t['u'])
    if st.button(t['b']):
        if name:
            st.session_state.auth = True
            st.session_state.name = name
            st.rerun()
else:
    # 4. عرض الأقسام والأفلام
    st.markdown(f"<h3>مرحباً يا {st.session_state.name}</h3>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs([t['m'], t['s'], t['k']])
    
    with tab1:
        st.header("🎞️ مكتبة الأفلام")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("فيلم 1")
            # إذا رفعت الفيلم بـ Terminal، ضع اسمه هنا
            st.video("movie1.mp4") 
        with col2:
            st.subheader("فيلم 2")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")
