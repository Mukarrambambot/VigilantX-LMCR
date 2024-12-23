"""
Main entry point for the VigilantX LMCR system.
"""
import logging
from pathlib import Path
import streamlit as st
from config import DB_PATH
from database.db_manager import DatabaseManager
from pages.auth import login_page
from pages.dashboard import dashboard_page

def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('vigilantx.log'),
            logging.StreamHandler()
        ]
    )

def main():
    """Main application entry point."""
    # Configure Streamlit page
    st.set_page_config(
        page_title="VigilantX LMCR",
        page_icon="🔒",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    setup_logging()
    logging.info("Starting VigilantX LMCR system")

    # Initialize session state
    if 'user_data' not in st.session_state:
        st.session_state.user_data = None

    # Ensure database directory exists
    Path(DB_PATH).parent.mkdir(exist_ok=True)

    # Initialize database
    db_manager = DatabaseManager(DB_PATH)

    # Show appropriate page based on authentication status
    if st.session_state.user_data is None:
        if login_page(db_manager):
            st.rerun()
    else:
        dashboard_page(st.session_state.user_data)

if __name__ == "__main__":
    main()