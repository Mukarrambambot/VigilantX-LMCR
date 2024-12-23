"""
Login window for the VigilantX LMCR system.
"""
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable
from utils.security import hash_password
from database.db_manager import DatabaseManager

class LoginWindow(tk.Toplevel):
    def __init__(self, parent: tk.Tk, db_manager: DatabaseManager, on_login: Callable):
        super().__init__(parent)
        self.db_manager = db_manager
        self.on_login = on_login
        
        self.title("VigilantX LMCR - Login")
        self.geometry("400x300")
        self.resizable(False, False)
        
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the login UI components."""
        # Main frame
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="Welcome to VigilantX LMCR",
            font=('Helvetica', 16, 'bold')
        )
        title_label.pack(pady=(0, 20))
        
        # Username
        username_frame = ttk.Frame(main_frame)
        username_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(username_frame, text="Username:").pack(side=tk.LEFT)
        self.username_entry = ttk.Entry(username_frame)
        self.username_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Password
        password_frame = ttk.Frame(main_frame)
        password_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(password_frame, text="Password:").pack(side=tk.LEFT)
        self.password_entry = ttk.Entry(password_frame, show="*")
        self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Login button
        login_btn = ttk.Button(
            main_frame,
            text="Login",
            command=self._handle_login
        )
        login_btn.pack(pady=20)
        
        # Forgot password link
        forgot_pwd_link = ttk.Label(
            main_frame,
            text="Forgot Password?",
            cursor="hand2",
            foreground="blue"
        )
        forgot_pwd_link.pack()
        forgot_pwd_link.bind("<Button-1>", self._show_reset_password)
        
        # Register link
        register_link = ttk.Label(
            main_frame,
            text="New User? Register Here",
            cursor="hand2",
            foreground="blue"
        )
        register_link.pack()
        register_link.bind("<Button-1>", self._show_register)
    
    def _handle_login(self):
        """Handle login button click."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        user = self.db_manager.get_user(username)
        if user and user['password_hash'] == hash_password(password):
            self.on_login(user)
            self.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def _show_reset_password(self, event=None):
        """Show password reset window."""
        # TODO: Implement password reset functionality
        messagebox.showinfo("Reset Password", "Password reset functionality coming soon")
    
    def _show_register(self, event=None):
        """Show registration window."""
        # TODO: Implement registration functionality
        messagebox.showinfo("Register", "Registration functionality coming soon")