import streamlit as st

entryFile = "app.py"


class PageLink:
    def __init__(self, page: str, label: str = None):
        self.page = "pages/" + page + ".py"

        if label is None:
            self.label = page[0].upper() + page[1:]
        else:
            self.label = label


pageLinks = [
    PageLink("tables"),
    PageLink("charts"),
    PageLink("maps")
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
