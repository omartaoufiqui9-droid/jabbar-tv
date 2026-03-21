import streamlit as st

# 1. إعداد الصفحة وتصميم Netflix الأسود
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# تصميم CSS لجعل الموقع يشبه التطبيقات العالمية
st.markdown("""
    <style>
    .main { background-color: #000000; color: white; direction: rtl; }
    .stTextInput input { background-color: #333; color: white; border-radius: 5px; border: 1px solid #ff4b4b; text-align: center; }
    .stButton>button { background-color: #e50914; color: white; border-radius: 5px; width: 100%; font-weight: bold; border: none; height: 3em; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; justify-content: center; }
    .stTabs [data-baseweb="tab"] { color: white; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. نظام الدخول (تكتب أي اسم لتدخل)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/ff/Netflix-new-icon.png", width=100) # يمكنك تغييرها بشعارك
    st.title("JABBAR TV")
    st.subheader("مرحباً بك في سينما منزلك")
    
    user_input = st.text_input("ادخل اسمك المستعار للدخول:", placeholder="مثلاً: جبار")
    if st.button("دخول"):
        if user_input:
            st.session_state['logged_in'] = True
            st.session_state['user_name'] = user_input
            st.rerun()
        else:
            st.error("من فضلك اكتب أي اسم أولاً")

# 3. محتوى الموقع بعد الدخول
else:
    st.title(f"🎬 أهلاً بك يا {st.session_state['user_name']} في جبار TV")
    
    # أقسام الموقع
    tab1, tab2, tab3 = st.tabs(["🎥 قسم الأفلام", "📺 قسم المسلسلات", "⭐ المفضلة"])

    with tab1:
        st.header("أفلام مختارة لك")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("وادي الذئاب: فلسطين")
            st.video("https://www.youtube.com/watch?v=13n74AQzHh4")
        with col2:
            st.subheader("فيلم أكشن آخر")
            st.info("سيتم إضافة الفيلم القادم قريباً")

    with tab2:
        st.header("المسلسلات")
        st.warning("جاري تجهيز حلقات المسلسلات.. انتظرونا!")

    if st.button("تسجيل الخروج"):
        st.session_state['logged_in'] = False
        st.rerun()
