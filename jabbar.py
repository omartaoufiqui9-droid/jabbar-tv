import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. اللغات (عربي / فرنسي)
translations = {
    "العربية": {
        "welcome": "مرحباً بك في جبار TV",
        "movies": "🎬 قسم الأفلام",
        "series": "📺 قسم المسلسلات",
        "watch": "شاهد الآن"
    },
    "Français": {
        "welcome": "Bienvenue sur JABBAR TV",
        "movies": "🎬 Section Films",
        "series": "📺 Section Séries",
        "watch": "Regarder"
    }
}

# 3. اختيار اللغة في الجانب
lang = st.sidebar.selectbox("Language / اللغة", ["العربية", "Français"])
t = translations[lang]

# 4. التصميم البسيط (ليعمل على كل الأجهزة)
st.markdown(f"<h1 style='text-align:center; color:red;'>JABBAR TV</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:gray;'>{t['welcome']}</p>", unsafe_allow_html=True)

# 5. عرض روابط فيديوهات مباشرة (تعمل بدون ملفات)
tab1, tab2 = st.tabs([t['movies'], t['series']])

with tab1:
    st.write("فيديو تجريبي للأفلام:")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

with tab2:
    st.write("فيديو تجريبي للمسلسلات:")
    st.video("https://media.w3.org/2010/05/sintel/trailer.mp4")
