"""
Registration page functionality.
"""
import streamlit as st
from database.db_manager import DatabaseManager
from utils.security import validate_password

def render_registration_form(db_manager: DatabaseManager):
    """Render the registration form."""
    with st.form("registration_form"):
        username = st.text_input("Username", key="reg_username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password", key="reg_password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        _show_password_requirements()
        
        submit = st.form_submit_button("Register")
        
        if submit:
            return _handle_registration(db_manager, username, email, password, confirm_password)
    return False

def _show_password_requirements():
    """Display password requirements."""
    st.markdown("""
    **Password Requirements:**
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number
    - At least one special character
    """)

def _handle_registration(db_manager, username, email, password, confirm_password):
    """Handle the registration form submission."""
    if not all([username, email, password, confirm_password]):
        st.error("Please fill in all fields")
        return False
    
    if password != confirm_password:
        st.error("Passwords do not match")
        return False
    
    # Validate password
    is_valid, message = validate_password(password)
    if not is_valid:
        st.error(message)
        return False
    
    # Attempt registration
    if db_manager.add_user(username, password, email):
        st.success("Registration successful! Please login.")
        return True
    
    st.error("Username or email already exists")
    return False