
import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. حالة الدخول
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# 3. التصميم (CSS) - نسخة مستقرة جداً
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); }
    .movie-card { background: #1a1a1a; padding: 15px; border-radius: 15px; border: 1px solid #333; text-align: center; margin-bottom: 20px; }
    .main-title { color: white; text-align: center; font-size: 50px; font-family: 'Arial Black'; }
    .stButton>button { background-color: #E50914 !important; color: white !important; border-radius: 10px; width: 100%; height: 50px; font-weight: bold; border: none; }
    h3 { color: white !important; font-size: 18px !important; }
</style>
""", unsafe_allow_html=True)

# --- واجهة الدخول ---
if not st.session_state['authenticated']:
    st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        name = st.text_input("أدخل اسمك للدخول:")
        if st.button("دخول إلى السينما"):
            if name:
                st.session_state['authenticated'] = True
                st.rerun()
else:
    # --- واجهة المحتوى ---
    st.markdown("<h2 style='text-align:center; color:white;'>🍿 سينما جبار الخاصة</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🎬 جميع الأفلام", "📺 المسلسلات", "🐥 الكرتون"])

    with tab1:
        # السطر الأول (أفلام أكشن حقيقية)
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
        st.info("سيتم إضافة الحلقات قريباً")

    with tab3:
        st.header("🐥 أفلام كرتون كاملة")
        col_k1, col_k2 = st.columns(2)
        with col_k1:
            st.subheader("كرتون مغامرات")
            st.video("https://www.youtube.com/watch?v=tC_69fLwI-Y")
        with col_k2:
            st.subheader("كرتون مضحك")
            st.video("https://www.youtube.com/watch?v=mY9n7K6fOAs")
