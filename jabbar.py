import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬")

# كود لتعديل الواجهة للعربية
st.markdown("""
    <style>
    .main { text-align: right; direction: rtl; }
    div.stButton > button { width: 100%; border-radius: 10px; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 مرحباً بكم في جبار TV")
st.write("الرجاء كتابة اسمك للدخول إلى السينما الخاصة بنا")

# خانة الدخول
user = st.text_input("أدخل اسمك هنا:")

if user:
    if user.lower() == "جبار" or user == "jabbar":
        st.success(f"أهلاً بك يا {user}! مشاهدة ممتعة.")
        st.balloons()
        st.markdown("---")
        
        # عرض فيلم مراد علمدار
        st.header("🎞️ فيلم وادي الذئاب: فلسطين")
        st.video("https://www.youtube.com/watch?v=13n74AQzHh4")
    else:
        st.error("عذراً، هذا الاسم غير مسجل. جرب كتابة 'جبار'")
else:
    st.info("نحن بانتظار دخولك..")
