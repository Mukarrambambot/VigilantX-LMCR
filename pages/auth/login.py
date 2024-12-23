"""
Login page functionality.
"""
import streamlit as st
from database.db_manager import DatabaseManager

def render_login_form(db_manager: DatabaseManager):
    """Render the login form."""
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            user_data = db_manager.authenticate_user(username, password)
            if user_data:
                st.session_state.user_data = user_data
                st.success("Login successful!")
                return True
            st.error("Invalid credentials!")
    return False