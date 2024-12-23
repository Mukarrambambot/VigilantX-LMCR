"""
Main application window for the VigilantX LMCR system.
"""
import tkinter as tk
from tkinter import ttk
from typing import Dict, Any
import logging

class MainWindow(tk.Tk):
    def __init__(self, user_data: Dict[str, Any]):
        super().__init__()
        
        self.user_data = user_data
        self.title("VigilantX LMCR - Pest Detection System")
        self.geometry("1200x800")
        
        self._init_ui()
        
    def _init_ui(self):
        """Initialize the main UI components."""
        # Create main container
        self.main_container = ttk.Frame(self)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Create sidebar
        self._create_sidebar()
        
        # Create main content area
        self._create_main_content()
        
        # Create status bar
        self._create_status_bar()
    
    def _create_sidebar(self):
        """Create the navigation sidebar."""
        sidebar = ttk.Frame(
            self.main_container,
            style="Sidebar.TFrame",
            padding="10"
        )
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # Navigation buttons
        nav_buttons = [
            ("Detection", self._show_detection),
            ("Control", self._show_control),
            ("Energy", self._show_energy),
            ("Profile", self._show_profile)
        ]
        
        for text, command in nav_buttons:
            btn = ttk.Button(
                sidebar,
                text=text,
                command=command,
                width=20
            )
            btn.pack(pady=5)
    
    def _create_main_content(self):
        """Create the main content area."""
        self.content_frame = ttk.Frame(
            self.main_container,
            padding="20"
        )
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Welcome message
        ttk.Label(
            self.content_frame,
            text=f"Welcome, {self.user_data['username']}!",
            font=('Helvetica', 16, 'bold')
        ).pack()
    
    def _create_status_bar(self):
        """Create the status bar."""
        status_bar = ttk.Frame(self, relief=tk.SUNKEN)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # System status
        ttk.Label(
            status_bar,
            text="System Status: Online",
            padding="5"
        ).pack(side=tk.LEFT)
        
        # Connection status
        ttk.Label(
            status_bar,
            text="Connected",
            foreground="green",
            padding="5"
        ).pack(side=tk.RIGHT)
    
    def _show_detection(self):
        """Show detection settings page."""
        self._clear_content()
        # TODO: Implement detection page
        logging.info("Showing detection page")
    
    def _show_control(self):
        """Show control mechanisms page."""
        self._clear_content()
        # TODO: Implement control page
        logging.info("Showing control page")
    
    def _show_energy(self):
        """Show energy management page."""
        self._clear_content()
        # TODO: Implement energy page
        logging.info("Showing energy page")
    
    def _show_profile(self):
        """Show user profile page."""
        self._clear_content()
        # TODO: Implement profile page
        logging.info("Showing profile page")
    
    def _clear_content(self):
        """Clear the main content area."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()