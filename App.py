import streamlit as st

st.set_page_config(
    page_title="Main App",
    page_icon="🏠",
    layout="centered",  # or "wide"
    initial_sidebar_state="collapsed",  # This sets the sidebar to start collapsed

)

st.title("Main Application Page")
st.write("Welcome to the Main App!")