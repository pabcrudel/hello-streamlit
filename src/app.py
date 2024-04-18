import streamlit as st
from components.menu import menu

# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role


def save_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role


# Selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "User"],
    key="_role",
    on_change=save_role,
)

# Render the sidebar menu
menu()

# Creates an `h1`
st.title("Hello Streamlit")
