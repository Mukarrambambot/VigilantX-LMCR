"""
Authentication pages initialization.
"""
import streamlit as st
from database.db_manager import DatabaseManager
from .login import render_login_form
from .register import render_registration_form

def login_page(db_manager: DatabaseManager):
    """Render the login page."""
    st.title("Login to VigilantX LMCR")
    
    # Add tabs for login and registration
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        return render_login_form(db_manager)
    
    with tab2:
        render_registration_form(db_manager)
    
    return False