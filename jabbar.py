import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. حالة الدخول
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# 3. التصميم (CSS) الفخم
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); }
    .movie-card { background: #1a1a1a; padding: 15px; border-radius: 15px; border: 2px solid #E50914; text-align: center; margin-bottom: 20px; }
    .main-title { color: white; text-align: center; font-size: 50px; font-family: 'Arial Black'; text-shadow: 2px 2px 10px #ff0000; }
    .stButton>button { background-color: #E50914 !important; color: white !important; border-radius: 10px; width: 100%; height: 50px; font-weight: bold; border: none; }
    h3 { color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- واجهة الدخول ---
if not st.session_state['authenticated']:
    st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        name = st.text_input("أدخل اسمك للمشاهدة المباشرة:", key="login_name")
        if st.button("دخول الآن"):
            if name:
                st.session_state['authenticated'] = True
                st.rerun()
else:
    # --- واجهة السينما المباشرة ---
    st.markdown("<h2 style='text-align:center; color:white;'>🎬 أفلام ومقاطع مباشرة (بدون يوتيوب)</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🎥 أفلام MP4", "📺 مسلسلات", "🐥 كرتون"])

    with tab1:
        st.info("هذه الفيديوهات تعمل مباشرة من السيرفر (Direct MP4)")
        
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم الأكشن (1)")
            # رابط مباشر MP4
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with c2:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم المغامرة (2)")
            # رابط مباشر آخر
            st.video("https://media.w3.org/2010/05/sintel/trailer.mp4")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.subheader("📺 بث مباشر / حلقات")
        # فيديو طويل مباشر
        st.video("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")

    with tab3:
        st.subheader("🐥 كرتون للأطفال")
        st.video("
