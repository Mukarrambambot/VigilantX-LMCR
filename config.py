"""
Configuration settings for the VigilantX LMCR system.
"""

APP_TITLE = "VigilantX LMCR - Pest Detection System"
DB_PATH = "vigilantx.db"

# Color scheme
COLORS = {
    'primary': '#2c3e50',
    'secondary': '#34495e',
    'accent': '#3498db',
    'warning': '#e74c3c',
    'success': '#2ecc71',
    'background': '#ecf0f1',
    'text': '#2c3e50',
}

# Default sensor thresholds
DEFAULT_THRESHOLDS = {
    'motion': 60,
    'temperature': 25,
    'humidity': 70,
    'light': 50
}