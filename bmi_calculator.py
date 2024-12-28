import streamlit as st


def bmi_calculator():
    st.title("BMI 계산기")
    st.write("키와 체중을 입력하여 BMI를 계산해보세요.")

    # 사이드바에 입력 위젯 배치
    with st.sidebar:
        height = st.number_input(
            "키(cm)", min_value=100, max_value=250, value=170)
        weight = st.number_input(
            "체중(kg)", min_value=20, max_value=200, value=60)

        calculate = st.button("계산하기")

    # BMI 계산
    if calculate:
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        st.header("계산 결과")
        st.write(f"BMI: {bmi:.2f}")

        # BMI 판정
        if bmi < 18.5:
            st.warning("저체중")
        elif bmi < 23:
            st.success("정상")
        elif bmi < 25:
            st.warning("과체중")
        else:
            st.error("비만")

        # BMI 차트
        import plotly.graph_objects as go

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=bmi,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "BMI"},
                gauge={
                    'axis': {'range': [None, 35]},
                    'steps': [
                        {'range': [0, 18.5], 'color': "lightgray"},
                        {'range': [18.5, 23], 'color': "lightgreen"},
                        {'range': [23, 25], 'color': "yellow"},
                        {'range': [25, 35], 'color': "red"}
                    ]
                }
            )
        )

        st.plotly_chart(fig)


if __name__ == "__main__":
    bmi_calculator()
