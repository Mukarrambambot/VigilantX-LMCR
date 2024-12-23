"""
Main entry point for the VigilantX LMCR system.
"""
import tkinter as tk
import logging
from pathlib import Path
from config import DB_PATH
from database.db_manager import DatabaseManager
from gui.auth.login_window import LoginWindow
from gui.main_window import MainWindow

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

def on_successful_login(user_data):
    """Handle successful login."""
    main_window = MainWindow(user_data)
    main_window.mainloop()

def main():
    """Main application entry point."""
    setup_logging()
    logging.info("Starting VigilantX LMCR system")
    
    # Ensure database directory exists
    Path(DB_PATH).parent.mkdir(exist_ok=True)
    
    # Initialize database
    db_manager = DatabaseManager(DB_PATH)
    
    # Create root window (hidden)
    root = tk.Tk()
    root.withdraw()
    
    # Show login window
    login_window = LoginWindow(root, db_manager, on_successful_login)
    login_window.mainloop()

if __name__ == "__main__":
    main()