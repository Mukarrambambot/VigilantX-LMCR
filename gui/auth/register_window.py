"""
Registration window for the VigilantX LMCR system.
"""
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable
import re
from utils.security import hash_password, validate_password
from database.db_manager import DatabaseManager

class RegisterWindow(tk.Toplevel):
    def __init__(self, parent: tk.Tk, db_manager: DatabaseManager):
        super().__init__(parent)
        self.db_manager = db_manager
        
        self.title("VigilantX LMCR - Register")
        self.geometry("500x400")
        self.resizable(False, False)
        
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the registration UI components."""
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="Create New Account",
            font=('Helvetica', 16, 'bold')
        )
        title_label.pack(pady=(0, 20))
        
        # Username
        username_frame = ttk.Frame(main_frame)
        username_frame.pack(fill=tk.X, pady=5)
        ttk.Label(username_frame, text="Username:").pack(side=tk.LEFT)
        self.username_entry = ttk.Entry(username_frame)
        self.username_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Email
        email_frame = ttk.Frame(main_frame)
        email_frame.pack(fill=tk.X, pady=5)
        ttk.Label(email_frame, text="Email:").pack(side=tk.LEFT)
        self.email_entry = ttk.Entry(email_frame)
        self.email_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Password
        password_frame = ttk.Frame(main_frame)
        password_frame.pack(fill=tk.X, pady=5)
        ttk.Label(password_frame, text="Password:").pack(side=tk.LEFT)
        self.password_entry = ttk.Entry(password_frame, show="*")
        self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Confirm Password
        confirm_frame = ttk.Frame(main_frame)
        confirm_frame.pack(fill=tk.X, pady=5)
        ttk.Label(confirm_frame, text="Confirm:").pack(side=tk.LEFT)
        self.confirm_entry = ttk.Entry(confirm_frame, show="*")
        self.confirm_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Password requirements
        req_frame = ttk.LabelFrame(main_frame, text="Password Requirements", padding="10")
        req_frame.pack(fill=tk.X, pady=10)
        ttk.Label(req_frame, text="• Minimum 8 characters\n• At least one uppercase letter\n• At least one lowercase letter\n• At least one number\n• At least one special character").pack()
        
        # Register button
        register_btn = ttk.Button(
            main_frame,
            text="Register",
            command=self._handle_register
        )
        register_btn.pack(pady=20)
        
        # Login link
        login_link = ttk.Label(
            main_frame,
            text="Already have an account? Login Here",
            cursor="hand2",
            foreground="blue"
        )
        login_link.pack()
        login_link.bind("<Button-1>", self._show_login)
    
    def _validate_email(self, email: str) -> bool:
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def _handle_register(self):
        """Handle registration button click."""
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()
        
        # Validate input
        if not all([username, email, password, confirm]):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        if not self._validate_email(email):
            messagebox.showerror("Error", "Invalid email format")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match")
            return
        
        # Validate password strength
        is_valid, message = validate_password(password)
        if not is_valid:
            messagebox.showerror("Error", message)
            return
        
        # Hash password and create user
        password_hash = hash_password(password)
        if self.db_manager.add_user(username, password_hash, email):
            messagebox.showinfo("Success", "Registration successful! Please login.")
            self.destroy()
        else:
            messagebox.showerror("Error", "Username or email already exists")
    
    def _show_login(self, event=None):
        """Close registration window to show login."""
        self.destroy()