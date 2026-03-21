import streamlit as st
import os

# 1. إعدادات الصفحة
st.set_page_config(page_title="جبار TV", page_icon="🎬", layout="wide")

# 2. تصميم الواجهة (الألوان واللوغو)
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); }
    .logo-box { 
        display: block; margin: 0 auto; width: 100px; height: 100px; 
        background: #E50914; color: white; text-align: center; 
        line-height: 100px; font-size: 70px; font-family: 'Arial Black'; 
        border-radius: 20px; box-shadow: 0px 0px 30px #ff0000;
    }
    .main-title { color: white; text-align: center; font-size: 60px; font-family: 'Arial Black'; }
    .sub-title { color: #888; text-align: center; font-size: 20px; margin-bottom: 30px; }
</style>
""", unsafe_allow_html=True)

# 3. عرض اللوغو والعناوين بالعربي
st.markdown("<div class='logo-box'>J</div>", unsafe_allow_html=True)
st.markdown("<h1 class='main-title'>JABBAR TV</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>سينما منزلك الخاصة</p>", unsafe_allow_html=True)

# 4. البحث عن فيديوهات MP4 في مجلدك
st.markdown("<h2 style='color: white; border-right: 5px solid #E50914; padding-right: 15px; text-align: right;'>🎬 مكتبة الأفلام</h2>", unsafe_allow_html=True)

ملفات_الفيديو = [ملف for ملف in os.listdir('.') if ملف.endswith('.mp4')]

if ملفات_الفيديو:
    الفيديو_المختار = st.selectbox("اختر الفيديو الذي تريد مشاهدته:", ملفات_الفيديو)
    st.video(الفيديو_المختار) # تشغيل الفيديو المختار من جهازك
else:
    st.warning("⚠️ لم يتم العثور على فيديوهات في المجلد. تأكد من وجود ملفات بصيغة mp4 بجانب ملف البرمجية.")
