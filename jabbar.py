import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="JABBAR TV", layout="wide")

# 2. نظام الدخول البسيط
st.title("🔐 بوابة جبار TV")

# اطلب من المستخدم إدخال اسمه
user_name = st.text_input("من فضلك أدخل اسمك للدخول إلى السينما:")

# 3. التحقق من الاسم (يمكنك تغيير "جبار" لأي اسم تريد)
if user_name.lower() == "جبار" or user_name.lower() == "admin":
    st.success(f"أهلاً بك يا {user_name}! تم فتح العرض الحصري.")
    st.markdown("---")
    
    # هنا يظهر الفيلم بعد الدخول
    st.title("🎬 سينما جبار الخاصة")
    st.header("🎞️ فيلم وادي الذئاب: فلسطين")
    
    # فيديو مراد علمدار
    st.video("https://www.youtube.com/watch?v=13n74AQzHh4")
    
else:
    if user_name != "":
        st.error("عذراً، هذا الاسم غير مسجل في قائمة أصدقاء جبار.")
    else:
        st.info("اكتب اسمك في الأعلى واضغط Enter للدخول.")
