import streamlit as st


def hello_streamlit():
    st.title("Hello, Streamlit!")
    st.write("Welcome to my first Streamlit app")

    if st.button("Click me"):
        st.balloons()
