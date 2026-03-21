import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. قاموس الترجمة
translations = {
    "العربية": {
        "welcome": "سينما منزلك الخاصة",
        "user_label": "أدخل اسمك للمشاهدة:",
        "login_btn": "دخول للمكتبة",
        "movies": "🎬 الأفلام المختارة",
        "series": "📺 المسلسلات الحصرية",
        "watch": "مشاهدة الآن"
    },
    "Français": {
        "welcome": "VOTRE CINÉMA À DOMICILE",
        "user_label": "Entrez votre nom :",
        "login_btn": "ACCÉDER",
        "movies": "🎬 Films Vedettes",
        "series": "📺 Séries Exclusives",
        "watch": "Regarder"
    }
}

lang = st.sidebar.selectbox("🌐 Language", list(translations.keys()))
t = translations[lang]

# 3. روابط أفلام تجريبية (بما أنه ليس لديك ملفات)
مكتبة_الأفلام = {
    "Big Buck Bunny (فلم كرتون)": "https://www.w3schools.com/html/mov_bbb.mp4",
    "فيديو الطبيعة الخلابة": "http://techslides.com/demos/sample-videos/small.mp4",
}

مكتبة_المسلسلات = {
    "الحلقة الأولى (تجريبية)": "https://media.w3.org/2010/05/sintel/trailer.mp4",
}

# 4. التصميم (CSS)
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); }
    .logo-box { 
        display: block; margin: 0 auto; width: 80px; height: 80px; 
        background: #E50914; color: white; text-align: center; 
        line-height: 80px; font-size: 50px; font-family: 'Arial Black'; 
        border-radius: 15px; box-shadow: 0px 0px 20px #ff0000;
    }
    .movie-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px; border: 1px solid #444; text-align: center; }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state['auth'] = False

# --- واجهة الدخول ---
if not st.session_state['auth']:
    st.markdown("<div class='logo-box'>J</div>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='color:white; text-align:center;'>JABBAR TV</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        name = st.text_input(t['user_label'], placeholder="اكتب اسمك...")
        if st.button(t['login_btn']):
            if name:
                st.session_state['auth'] = True
                st.session_state['user'] = name
                st.rerun()
# --- واجهة العرض المباشر ---
else:
    section = st.sidebar.radio("القسم", [t['movies'], t['series']])
    st.markdown(f"<h2 style='color:white; text-align:right;'>{section}</h2>", unsafe_allow_html=True)
    
    المحتوى = مكتبة_الأفلام if section == t['movies'] else مكتبة_المسلسلات
    
    cols = st.columns(2)
    for i, (عنوان, رابط) in enumerate(المحتوى.items()):
        with cols[i % 2]:
            st.markdown(f"<div class='movie-card'><h3 style='color:white;'>{عنوان}</h3></div>", unsafe_allow_html=True)
            if st.button(f"{t['watch']} - {عنوان}"):
                st.session_state['video_url'] = رابط

    if 'video_url' in st.session_state:
        st.markdown("---")
        st.video(st.session_state['video_url'])
