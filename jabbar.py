
 
        # سطر جديد من الأفلام
        col4, col5, col6 = st.columns(3)
        with col4:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم جديد 1")
            st.video("ضع_رابط_اليوتيوب_هنا")
            st.markdown("</div>", unsafe_allow_html=True)
        with col5:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم جديد 2")
            st.video("ضع_رابط_اليوتيوب_هنا")
            st.markdown("</div>", unsafe_allow_html=True)
        with col6:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.subheader("فيلم جديد 3")
            st.video("ضع_رابط_اليوتيوب_هنا")
            st.markdown("</div>", unsafe_allow_html=True)
