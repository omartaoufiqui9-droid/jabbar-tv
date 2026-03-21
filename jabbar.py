import streamlit as st
import os

# إعداد الصفحة مع أيقونة سينمائية
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# تصميم CSS احترافي (السر في الجمال)
st.markdown("""
    <style>
    /* 1. الخلفية الشبكية مع تعتيم سينمائي */
    .stApp {
        background-image: linear-gradient(to bottom, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.9) 100%), 
                          url('https://assets.nflxext.com/ffe/siteui/vlv3/5e16108b-dc50-4291-a3c6-64797c678a87/e52410a5-e362-421b-8777-695027581b7e/MA-en-20240311-popsignuptwoweeks-perspective_alpha_website_medium.jpg');
        background-size: cover;
        background-attachment: fixed;
    }

    /* 2. تحسين شكل العناوين */
    .main-title {
        color: #E50914;
        text-align: center;
        font-size: 85px;
        font-family: 'Arial Black', sans-serif;
        text-shadow: 2px 2px 15px rgba(229, 9, 20, 0.5);
        margin-bottom: 0px;
    }
    .sub-title {
        color: white;
        text-align: center;
        font-size: 22px;
        margin-bottom: 40px;
        font-weight: 300;
    }

    /* 3. تصميم صندوق الأفلام (Card Style) */
    .movie-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s;
    }
    .movie-card:hover {
        transform: scale(1.05);
        border: 1px solid #E50914;
    }

    /* 4. تجميل الأزرار */
    .stButton>button {
        background-color: #E50914;
        color: white;
        border: none;
        border-radius: 4px;
        font-weight: bold;
        padding: 15px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff1f2a;
        box-shadow: 0px 0px 20px rgba(229, 9, 20, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    # واجهة الدخول الفخمة
    st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>السينما كما لم تراها من قبل</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        user = st.text_input("Username", placeholder="جبار")
        password = st.text_input("Password", type="password", placeholder="••••")
        if st.button("Démarrer la session"):
            if user.lower() in ["جبار", "jabbar"] and password == "1234":
                st.session_state['auth'] = True
                st.rerun()
            else:
                st.error("⚠️ خطأ في البيانات")
else:
    # واجهة المكتبة بعد الدخول
    st.markdown("<h2 style='color: white; border-left: 5px solid #E50914; padding-left: 15px;'>المحتوى الحصري</h2>", unsafe_allow_html=True)
    
    movies_path = os.path.expanduser("~/mediaserver/movies")
    if os.path.exists(movies_path):
        files = [f for f in os.listdir(movies_path) if f.endswith(('.mp4', '.mkv'))]
        if files:
            cols = st.columns(3)
            for i, movie in enumerate(files):
                with cols[i % 3]:
                    st.markdown(f"<div class='movie-card'>", unsafe_allow_html=True)
                    st.write(f"🍿 **{movie.replace('.mp4', '')}**")
                    st.video(os.path.join(movies_path, movie))
                    st.markdown("</div>", unsafe_allow_html=True)
