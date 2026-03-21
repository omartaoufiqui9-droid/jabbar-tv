import streamlit as st

# إعدادات الصفحة الفخمة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="centered")

# تصميم CSS احترافي لتغيير شكل الموقع بالكامل
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
        direction: rtl;
        text-align: center;
    }
    .stTextInput input {
        background-color: #262730;
        color: white;
        border-radius: 10px;
        border: 1px solid #ff4b4b;
        text-align: center;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        width: 100%;
        font-weight: bold;
        border: none;
    }
    .welcome-text {
        font-size: 50px;
        font-weight: bold;
        color: #ff4b4b;
        text-shadow: 2px 2px 4px #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# واجهة الدخول
st.markdown('<p class="welcome-text">JABBAR TV</p>', unsafe_allow_html=True)
st.write("---")
st.subheader("🎥 عالمك الخاص للأفلام")

# خانة الدخول بتصميم جديد
user = st.text_input("👤 ادخل اسمك المستعار للبدء", placeholder="اكتب اسمك هنا...")

if user:
    if user.lower() == "جبار" or user == "jabbar":
        st.balloons()
        st.success(f"مرحباً بك يا {user} في واجهتك المفضلة")
        
        # عرض الفيلم بشكل سينمائي
        st.markdown("### 🎞️ الآن يعرض: وادي الذئاب فلسطين")
        st.video("https://www.youtube.com/watch?v=13n74AQzHh4")
        
        st.info("💡 مشاهدة ممتعة! يمكنك تشغيل الفيلم بملء الشاشة الآن.")
    else:
        st.error("⚠️ عذراً، هذا الاسم غير مسجل لدينا.")
else:
    st.markdown("---")
    st.write("🔒 يرجى تسجيل الدخول للوصول إلى المحتوى الحصري")    
