import streamlit as st
from components.page_config import page_config

page_config()

# Creates an `h1`
st.title("Hello Streamlit")

# Dummy login
login_button = st.button("Login")
if login_button:
    st.session_state["auth_user"] = "example@example.com"
    st.session_state["auth_token"] = "dummy-token"
    st.switch_page("pages/dashboard.py")
