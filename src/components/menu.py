import streamlit as st

entryFile = "app.py"


class PageLink:
    def __init__(self, page, label):
        self.page = "pages/" + page + ".py"
        self.label = label


pageLinks = [
    PageLink("tables", "Table"),
    PageLink("charts", "Charts"),
    PageLink("maps", "Maps")
]


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link(entryFile, label="Switch accounts")

    # Display links to each page
    for pageLink in pageLinks:
        st.sidebar.page_link(pageLink.page, label=pageLink.label)


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link(entryFile, label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page(entryFile)
    menu()
