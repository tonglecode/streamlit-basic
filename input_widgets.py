import streamlit as st


def input_widgets():
    # 텍스트 입력
    name = st.text_input("이름을 입력하세요")

    # 숫자 입력
    age = st.number_input("나이를 입력하세요", min_value=0, max_value=150)

    # 슬라이더
    score = st.slider("점수", 0, 100, 50)

    # 선택박스
    color = st.selectbox("좋아하는 색상", ["빨강", "파랑", "초록"])

    # 다중 선택
    fruits = st.multiselect("좋아하는 과일", ["사과", "바나나", "오렌지"])

    # 체크박스
    is_student = st.checkbox("학생입니까?")

    # 라디오 버튼
    gender = st.radio("성별", ["남성", "여성"])

    if st.button("제출"):
        st.write("입력 결과:")
        st.write(f"이름: {name}")
        st.write(f"나이: {age}")
        st.write(f"점수: {score}")
        st.write(f"좋아하는 색상: {color}")
        st.write(f"좋아하는 과일: {fruits}")
        st.write(f"학생 여부: {is_student}")
        st.write(f"성별: {gender}")
