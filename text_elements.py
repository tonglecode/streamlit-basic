
import streamlit as st


def text_elements():
    # 제목과 헤더
    st.title("메인 제목")
    st.header("헤더")
    st.subheader("서브헤더")

    # 일반 텍스트
    st.text("일반 텍스트입니다.")

    # 마크다운
    st.markdown("### 마크다운 지원\n- 항목 1\n- 항목 2")

    # 강조 텍스트
    st.success("성공 메시지")
    st.info("정보 메시지")
    st.warning("경고 메시지")
    st.error("에러 메시지")
