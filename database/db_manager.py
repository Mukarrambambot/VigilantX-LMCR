"""
Database management for the VigilantX LMCR system.
"""
import sqlite3
import logging
from pathlib import Path
from typing import Dict, Any, Optional

class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        """Initialize database tables."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Users table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password_hash TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

                # Sensor readings table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS sensor_readings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sensor_type TEXT NOT NULL,
                        value REAL NOT NULL,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

                # System logs table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS system_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        level TEXT NOT NULL,
                        message TEXT NOT NULL,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Database initialization error: {e}")
            raise

    def add_user(self, username: str, password_hash: str, email: str) -> bool:
        """Add a new user to the database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)",
                    (username, password_hash, email)
                )
                conn.commit()
                return True
        except sqlite3.Error as e:
            logging.error(f"Error adding user: {e}")
            return False

    def get_user(self, username: str) -> Optional[Dict[str, Any]]:
        """Retrieve user data by username."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM users WHERE username = ?",
                    (username,)
                )
                result = cursor.fetchone()
                if result:
                    return {
                        'id': result[0],
                        'username': result[1],
                        'password_hash': result[2],
                        'email': result[3],
                        'created_at': result[4]
                    }
                return None
        except sqlite3.Error as e:
            logging.error(f"Error retrieving user: {e}")
            return None