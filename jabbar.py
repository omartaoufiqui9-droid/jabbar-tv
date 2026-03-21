
import streamlit as st
import os

# 1. إعداد الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🍿", layout="wide")

# 2. تصميم CSS السينمائي
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to bottom, rgba(0,0,0,0.8), rgba(0,0,0,0.9)), 
                          url('https://assets.nflxext.com/ffe/siteui/vlv3/5e16108b-dc50-4291-a3c6-64797c678a87/e52410a5-e362-421b-8777-695027581b7e/MA-en-20240311-popsignuptwoweeks-perspective_alpha_website_medium.jpg');
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .main-title { color: white; text-align: center; font-size: 70px; font-family: 'Arial Black'; margin-top: 50px; }
    .stButton>button { background-color: #E50914; color: white; height: 60px; width: 100%; font-size: 24px; border-radius: 5px; border: none; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown("<div class='main-title'>JABBAR TV</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        user = st.text_input("اسم المستخدم (جبار)")
        password = st.text_input("كلمة المرور", type="password")
        if st.button("دخول >"):
            if user.lower() in ["جبار", "jabbar"] and password == "1234":
                st.session_state['auth'] = True
                st.rerun()
else:
    st.markdown("<h1 style='color: #E50914;'>🎬 مكتبة وادي الذئاب</h1>", unsafe_allow_html=True)
    
    # مسار الأفلام
    movies_path = os.path.expanduser("~/mediaserver/movies")
    
    if os.path.exists(movies_path):
        files = [f for f in os.listdir(movies_path) if f.endswith(('.mp4', '.mkv'))]
        if not files:
            st.warning("المجلد فارغ! سأقوم بإضافة حلقة تجريبية لك...")
        else:
            cols = st.columns(3)
            for i, movie in enumerate(files):
                with cols[i % 3]:
                    st.info(f"📺 {movie.replace('.mp4', '')}")
                    with open(os.path.join(movies_path, movie), 'rb') as f:
                        st.video(f.read())
