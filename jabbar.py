import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. حالة الدخول
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# 3. التصميم (CSS) - النسخة المستقرة
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); }
    .movie-card { background: #1a1a1a; padding: 15px; border-radius: 15px; border: 1px solid #333; text-align: center; margin-bottom: 20px; }
    .main-title { color: white; text-align: center; font-size: 50px; font-family: 'Arial Black'; }
    .stButton>button { background-color: #E50914 !important; color: white !important; border-radius: 10px; width: 100%; height: 50px; }
</style>
""", unsafe_allow_html=True)

# --- واجهة الدخول ---
if not st.session_state['authenticated']:
    st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        name = st.text_input("أدخل اسمك للدخول إلى عالم الأفلام:")
        if st.button("ACCÉDER / دخول"):
            if name:
                st.session_state['authenticated'] = True
                st.rerun()
else:
    # --- واجهة المكتبة ---
    st.markdown("<h2 style='text-align:center; color:white;'>🍿 سينما جبار الخاصة</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🎬 جميع الأفلام", "📺 المسلسلات", "🐥 الكرتون"])

    with tab1:
        # --- السطر الأول ---
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم الأكشن 1")
            st.video("https://www.youtube.com/watch?v=S3IDV-p7fIs")
            st.markdown("</div>", unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم الأكشن 2")
            st.video("https://www.youtube.com/watch?v=9ay66723-K0")
            st.markdown("</div>", unsafe_allow_html=True)
        with c3:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم مغامرات")
            st.video("https://www.youtube.com/watch?v=5Uf_NInR8Yc")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- السطر الثاني ---
        c4, c5, c6 = st.columns(3)
        with c4:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم خيال علمي")
            st.video("https://www.youtube.com/watch?v=v64KOxKVzvo")
            st.markdown("</div>", unsafe_allow_html=True)
        with c5:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم دراما")
            st.video("https://www.youtube.com/watch?v=SfS_mXWqHZA")
            st.markdown("</div>", unsafe_allow_html=True)
        with c6:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم وثائقي")
            st.video("https://www.youtube.com/watch?v=mY9n7K6fOAs")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.header("📺 قسم المسلسلات")
        st.info("جاري تجهيز حلقات المسلسلات...")

    with tab3:
        st.header("🐥 أفلام كرتون")
        st.video("https://www.youtube.com/watch?v=tC_69fLwI-Y")
