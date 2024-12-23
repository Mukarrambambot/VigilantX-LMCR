"""
Database management for the VigilantX LMCR system.
"""
import sqlite3
import logging
from pathlib import Path
from typing import Dict, Any, Optional
from utils.security import hash_password

# Admin credentials - replace 'your_password_here' with your desired password
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = hash_password("MBHDSHA")

class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def authenticate_user(self, username: str, password: str) -> Optional[Dict[str, Any]]:
        """Authenticate user with username and password."""
        # Check for admin credentials first
        if username == ADMIN_USERNAME and hash_password(password) == ADMIN_PASSWORD_HASH:
            return {
                'id': 0,
                'username': ADMIN_USERNAME,
                'email': 'admin@vigilantx.com',
                'is_admin': True
            }
        
        # Regular user authentication
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM users WHERE username = ? AND password_hash = ?",
                    (username, hash_password(password))
                )
                result = cursor.fetchone()
                if result:
                    return {
                        'id': result[0],
                        'username': result[1],
                        'email': result[3],
                        'created_at': result[4],
                        'is_admin': False
                    }
                return None
        except sqlite3.Error as e:
            logging.error(f"Authentication error: {e}")
            return None

    # ... rest of the DatabaseManager class remains the same ...