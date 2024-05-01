import streamlit as st
from components.menu import main_sidebar
from components.page_config import page_config

page_config()
main_sidebar()

st.title("Dashboard")
