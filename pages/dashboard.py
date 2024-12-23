"""
Main dashboard page for the VigilantX LMCR system.
"""
import streamlit as st # type: ignore

def dashboard_page(user_data: dict):
    """Render the main dashboard."""
    st.title(f"Welcome, {user_data['username']}!")
    
    # Sidebar navigation
    with st.sidebar:
        st.title("Navigation")
        page = st.radio(
            "Go to",
            ["Detection", "Control", "Energy", "Profile"]
        )
    
    # Main content
    if page == "Detection":
        detection_section()
    elif page == "Control":
        control_section()
    elif page == "Energy":
        energy_section()
    elif page == "Profile":
        profile_section(user_data)

def detection_section():
    """Render detection settings."""
    st.header("Detection Settings")
    # Add detection UI components here

def control_section():
    """Render control mechanisms."""
    st.header("Control Mechanisms")
    # Add control UI components here

def energy_section():
    """Render energy management."""
    st.header("Energy Management")
    # Add energy UI components here

def profile_section(user_data: dict):
    """Render user profile."""
    st.header("User Profile")
    st.write(f"Email: {user_data['email']}")
    st.write(f"Member since: {user_data['created_at']}")