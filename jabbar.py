
import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="JABBAR TV", layout="wide")

# 2. نظام الدخول
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

# 3. تصميم الموقع (CSS)
st.markdown("""
<style>
    .stApp { background-color: #000000; color: white; }
    .movie-box { border: 2px solid #E50914; padding: 15px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    .stButton>button { background-color: #E50914 !important; color: white !important; width: 100%; border-radius: 10px; height: 50px; font-weight: bold; border: none; }
</style>
""", unsafe_allow_html=True)

# --- واجهة الدخول ---
if not st.session_state['auth']:
    st.markdown("<h1 style='text-align:center; color:#E50914;'>JABBAR TV</h1>", unsafe_allow_html=True)
    user = st.text_input("أدخل اسمك للدخول:")
    if st.button("دخول"):
        if user:
            st.session_state['auth'] = True
            st.rerun()

# --- واجهة المحتوى ---
else:
    st.markdown("<h2 style='text-align:center;'>🎬 سينما جبار المباشرة</h2>", unsafe_allow_html=True)
    
    # الأقسام (Tabs)
    tab1, tab2, tab3 = st.tabs(["🎥 أفلام", "📺 مسلسلات", "🐥 كرتون"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='movie-box'>", unsafe_allow_html=True)
            st.subheader("فيديو تجريبي 1")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='movie-box'>", unsafe_allow_html=True)
            st.subheader("فيديو تجريبي 2")
            st.video("https://media.w3.org/2010/05/sintel/trailer.mp4")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.subheader("قسم المسلسلات")
        st.video("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")

    with tab3:
        st.subheader("قسم الكرتون")
        st.video("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4")

    if st.sidebar.button("خروج"):
        st.session_state['auth'] = False
        st.rerun()
