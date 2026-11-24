import random
import streamlit as st

# 웹 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 메뉴 추천", page_icon="🍽️")

# 제목 및 안내 문구
st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천")
st.write("아래 버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 골라드립니다!")

# 1. 점심 메뉴 리스트 작성
menus = ["짜장면", "마라탕", "제육볶음", "돈까스", "떡볶이", "햄버거", "초밥"]

# 버튼 생성 (버튼을 누르면 True가 반환되어 아래 코드가 실행됨)
if st.button("🎲 점심 메뉴 추천받기", type="primary"):
    # 2. 랜덤으로 하나 선택하기
    selected_menu = random.choice(menus)
    
    # 결과 출력 및 축하 효과
    st.success(f"오늘의 추천 점심 메뉴는 **[{selected_menu}]** 입니다! 맛있게 드세요 😋")
    st.balloons()
