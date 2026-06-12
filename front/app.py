import streamlit as st
import requests

st.title("게임 장르 추천 앱")

st.write("자신의 취향에 맞는 선택지를 골라주세요")

play_style = st.selectbox(
    "몇명이서 하는 걸 선호하시나요?",
    ["혼자","함께"]
)

game_type = st.selectbox(
    "어떤 방식을 선호하시나요?",
    ["경쟁","협력"]
)


if st.button("추천 받기"):

    payload = {
        "play_style": play_style, 
        "game_type": game_type
        }

    try:
        response = requests.post("http://backend:8000/recommend", json=payload)

        if response.status_code == 200:
            result = response.json()
            
            st.success(f"추천 결과: {result['recommendation']}")

            st.write(f"플레이 스타일: {result['play_style']}")
            st.write(f"게임 유형: {result['game_type']}")
            st.write(f"추천 장르: {result['recommendation']}")

        else:
            st.error("추천 요청 실패")

    except Exception as e:
        st.error(f"오류 발생: {e}")
