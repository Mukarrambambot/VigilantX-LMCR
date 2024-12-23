"""
Authentication pages for the VigilantX LMCR system.
"""
import streamlit as st
from database.db_manager import DatabaseManager
from utils.security import validate_password

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

def render_registration_form(db_manager: DatabaseManager):
    """Render the registration form."""
    with st.form("registration_form"):
        username = st.text_input("Username", key="reg_username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password", key="reg_password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        # Show password requirements
        st.markdown("""
        **Password Requirements:**
        - Minimum 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one number
        - At least one special character
        """)
        
        submit = st.form_submit_button("Register")
        
        if submit:
            if not all([username, email, password, confirm_password]):
                st.error("Please fill in all fields")
                return
            
            if password != confirm_password:
                st.error("Passwords do not match")
                return
            
            # Validate password
            is_valid, message = validate_password(password)
            if not is_valid:
                st.error(message)
                return
            
            # Attempt registration
            if db_manager.add_user(username, password, email):
                st.success("Registration successful! Please login.")
            else:
                st.error("Username or email already exists")