import streamlit as st


def page_config(page_title: str = "Hello Streamlit"):
    st.set_page_config(
      page_title,
      menu_items={
          'Report a bug':
          "https://github.com/pablocru/hello-streamlit/issues",
      }
    )
