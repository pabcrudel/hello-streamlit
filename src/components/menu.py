import streamlit as st
from typing import List

entryFile = "app.py"


class PageLink:
    def __init__(self, page: str, label: str = None):
        self.page = "pages/" + page + ".py"

        if label is None:
            self.label = page[0].upper() + page[1:]
        else:
            self.label = label


class SectionLink:
    def __init__(self, name: str, pages: List[PageLink]):
        self.name = name
        self.pages = pages


navigationItems = [
    PageLink("tables"),
    PageLink("charts"),
    PageLink("maps")
]


def authenticated_menu():
    # Show a navigation menu for authenticated users
    # Top heading of the menu
    st.sidebar.write("### Hello Streamlit")

    def logout():
        del st.session_state["auth_user"]
        del st.session_state["auth_token"]

    # Create a button that handles logout
    st.sidebar.button("Logout", on_click=logout)

    st.sidebar.divider()

    # Display links to each page
    for navigationItem in navigationItems:
        if isinstance(navigationItem, PageLink):
            st.sidebar.container(border=True).page_link(
                navigationItem.page,
                label=navigationItem.label,
            )
        elif isinstance(navigationItem, SectionLink):
            expander = st.sidebar.expander(navigationItem.name)
            for pageLink in navigationItem.pages:
                expander.page_link(
                    pageLink.page,
                    label=pageLink.label
                )


def main_sidebar():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "auth_token" not in st.session_state:
        st.switch_page(entryFile)
    else:
        authenticated_menu()
