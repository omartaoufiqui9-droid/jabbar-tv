import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# 2. تصميم CSS احترافي (اللوغو والواجهة)
st.markdown("""
<style>
    /* خلفية متدرجة سينمائية قوية */
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #000000 100%);
    }

    /* تصميم اللوغو البرمجي (حرف J المتوهج) */
    .logo-container {
        text-align: center;
        padding-top: 50px;
    }
    .logo-box {
        display: inline-block;
        width: 100px;
        height: 100px;
        line-height: 100px;
        background-color: #E50914;
        color: white;
        font-size: 70px;
        font-family: 'Arial Black';
        border-radius: 20px;
        box-shadow: 0px 0px 30px #ff0000;
        margin-bottom: 10px;
    }

    /* عنوان JABBAR TV */
    .main-title {
        color: #E50914;
        text-align: center;
        font-size: 75px;
        font-family: 'Arial Black', sans-serif;
        text-shadow: 2px 2px 15px rgba(229, 9, 20, 0.4);
        margin: 0;
    }

    /* تحسين الأزرار */
    .stButton>button {
        background-color: #E50914 !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 20px !important;
        border-radius: 8px !important;
        height: 55px !important;
    }
</style>
""", unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state['auth'] = False

# واجهة الدخول
if not st.session_state['auth']:
    # عرض اللوغو البرمجي
    st.markdown("""
    <div class='logo-container'>
        <div class='logo-box'>J</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#555;'>VOTRE CINÉMA À DOMICILE</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.text_input("Identifiant")
        st.text_input("Mot de passe", type="password")
        if st.button("ACCÉDER"):
            st.session_state['auth'] = True
            st.rerun()
else:
    # واجهة العرض الرئيسية
    st.markdown("<h1 style='color: white;'>🎬 مكتبة جبار الشخصية</h1>", unsafe_allow_html=True)
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
