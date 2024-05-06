import streamlit as st


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("pages/user.py", label="My profile")
    if st.session_state.role in ["tenant"]:
        st.sidebar.page_link("pages/tenant.py", label="View my home")

    if st.session_state.role in ["manager"]:
        st.sidebar.page_link("pages/manager.py", label="Manage users")
        st.sidebar.page_link(
            "pages/owner.py",
            label="Manage admin access",
            disabled=st.session_state.role != "owner",
        )

    if st.session_state.role in ["owner"]:
        st.sidebar.page_link("pages/owner.py", label="Manage users")


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("pages/signup.py", label="Sign Up")
    st.sidebar.page_link("pages/about.py",label = "About")



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
        st.switch_page("app.py")
    menu()
