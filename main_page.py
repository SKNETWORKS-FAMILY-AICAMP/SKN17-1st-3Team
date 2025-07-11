import streamlit as st

st.title('프로젝트용 시범 페이지입니다.')
st.subheader("원하는 기능을 선택하세요",divider='rainbow')

col1,col2= st.columns(2,gap='small')

with col1:
    st.link_button('자동차 분석 링크','http://localhost:8501/car_analysis',use_container_width=True)

with col2:
    st.link_button('기업 FAQ 분석 정보','http://localhost:8501/faq',use_container_width=True )

