# backend/config/__init__.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Base configuration class for the Flask app.
    """
    # General Flask settings
    DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

    # OpenAI settings
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Server settings
    HOST = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    PORT = int(os.getenv("FLASK_RUN_PORT", 5000))

def init_app(app):
    """
    Apply configuration to the Flask app.
    """
    app.config.from_object(Config)
