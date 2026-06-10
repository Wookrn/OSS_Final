import streamlit as st
import requests

st.title("추천 시스템")

st.write("관심 분야 입력")

category = st.selectbox("카테고리 선택", ["A", "B", "C"])

if st.button("추천 받기"):
    payload = {"category": category}

    try:
        response = requests.post("http://localhost:8000/recommend", json=payload)

        if response.status_code == 200:
            result = response.json()
            
            st.success("추천 결과")

            st.write(f"카테고리: {result['category']}")
            st.write(f"추천: {result['recommendation']}")
        else:
            st.error("추천 요청 실패")

    except Exception as e:
        st.error(f"오류 발생: {e}")
