import streamlit as st

# إعداد الصفحة لتكون عريضة واحترافية
st.set_page_config(page_title="JABBAR TV", layout="wide")

# إخفاء القوائم الجانبية لتركيز الانتباه على الفيلم
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_name=True)

st.title("🎬 جبار TV - العرض الحصري")

# عرض الفيلم بمشغل كبير
st.subheader("🎞️ فيلم وادي الذئاب: فلسطين")
video_url = "https://www.youtube.com/watch?v=13n74AQzHh4"

# وضع الفيديو في منتصف الصفحة
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    st.video(video_url)

st.success("تم تشغيل الفيلم بنجاح على سيرفرات جبار!")
