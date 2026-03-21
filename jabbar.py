
import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. نظام حالة الدخول
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# 3. التصميم (CSS) - نسخة مستقرة تمنع الشاشة السوداء
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); }
    .movie-box { background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 15px; border: 1px solid #333; text-align: center; margin-bottom: 20px; }
    .main-title { color: white; text-align: center; font-size: 40px; font-family: 'Arial Black'; }
    .stButton>button { background-color: #E50914 !important; color: white !important; font-weight: bold; width: 100%; border-radius: 10px; height: 45px; border:none; }
    h1, h2, h3, p { color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- واجهة الدخول ---
if not st.session_state['authenticated']:
    st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
    col_l1, col_l2, col_l3 = st.columns([1, 1.2, 1])
    with col_l2:
        name = st.text_input("أدخل اسمك للدخول:")
        if st.button("دخول للمكتبة"):
            if name:
                st.session_state['authenticated'] = True
                st.rerun()
# --- واجهة المحتوى (أفلام، مسلسلات، كرتون) ---
else:
    st.markdown("<h2 style='text-align:center;'>🍿 سينما جبار المباشرة</h2>", unsafe_allow_html=True)
    
    t1, t2, t3 = st.tabs(["🎥 أفلام تجريبية", "📺 مسلسلات", "🐥 كرتون"])
    
    with t1:
        st.write("### فيديوهات مباشرة تعمل 100%")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<div class='movie-box'>", unsafe_allow_html=True)
            st.subheader("تجربة فيديو 1")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")
            st.markdown("</div>", unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='movie-box'>", unsafe_allow_html=True)
            st.subheader("تجربة فيديو 2")
            st.video("https://media.w3.org/2010/05/sintel/trailer.mp4")
            st.markdown("</div>", unsafe_allow_html=True)

    with t2:
        st.subheader("📺 قسم المسلسلات")
        st.video("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")

    with t3:
        st.subheader("🐥 قسم الكرتون")
        st.video("
