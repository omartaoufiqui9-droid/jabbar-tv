import streamlit as st

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
        st.session_state['authenticated']

