
import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", page_icon="🎬", layout="wide")

# العنوان الرئيسي
st.title("🎬 جبار TV - عالم الأفلام")
st.markdown("---")

# قسم فيلم مراد علمدار
st.header("🎞️ فيلم وادي الذئاب: فلسطين")
st.image("https://الصورة_البوستر_اختياري") # يمكنك إضافة رابط صورة بوستر هنا

# رابط الفيلم من يوتيوب
video_url = "https://www.youtube.com/watch?v=13n74AQzHh4"
st.video(video_url)

st.info("الفيلم مدبلج للعربية - مشاهدة ممتعة مع مراد علمدار!")

# قسم لإضافة أفلام أخرى مستقبلاً
st.markdown("---")
st.subheader("🔜 أفلام ستضاف قريباً")
st.write("أخبرني يا جبار بالأفلام التي يريدها أصدقاؤك لنضيفها هنا!")
