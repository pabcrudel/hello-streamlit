import streamlit as st
from components.page_config import page_config
from components.menu import main_sidebar


def main_header(section_title: str, section_name: str = None):
    if section_name is None:
        title = section_title
    else:
        title = section_title + " | " + section_name

    page_config(title)
    main_sidebar()

    st.title(title)
