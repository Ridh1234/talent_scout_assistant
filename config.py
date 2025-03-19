# Configuration settings for the TalentScout Hiring Assistant
# Contains constants and configuration values used throughout the application

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini API configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-pro"  # Gemini model

# Application settings
APP_TITLE = "TalentScout Hiring Assistant"
APP_DESCRIPTION = "AI-powered assistant for initial candidate screening"

# Conversation settings
MAX_TECHNICAL_QUESTIONS = 5
MIN_TECHNICAL_QUESTIONS = 3

# Candidate information fields to collect
CANDIDATE_INFO_FIELDS = [
    "Full Name",
    "Email Address",
    "Phone Number",
    "Years of Experience",
    "Desired Position(s)",
    "Current Location",
    "Tech Stack"
]

# Exit keywords
EXIT_KEYWORDS = ["exit", "quit", "bye", "goodbye", "end"]

# Error messages
ERROR_API_KEY = "Gemini API key not found. Please set the GEMINI_API_KEY environment variable."
ERROR_GENERIC = "I'm having trouble processing your request. Please try again."

# UI Configuration
UI_THEME_COLOR = "#0e76a8"  # LinkedIn blue
UI_SECONDARY_COLOR = "#f5f5f5"
UI_CHAT_USER_COLOR = "#E8F0FE"
UI_CHAT_BOT_COLOR = "#FFFFFF"