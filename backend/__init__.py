# backend/__init__.py
from flask import Flask
from flask_cors import CORS
from config import init_app
from routes.chat import chat_bp

def create_app():
    """
    Flask application factory.
    Creates and configures the Flask app instance.
    """
    app = Flask(__name__)

    # Load configuration (from backend/config/__init__.py)
    init_app(app)

    # Enable Cross-Origin Resource Sharing
    CORS(app)

    # Register Blueprints (routes)
    app.register_blueprint(chat_bp)

    # Health check / root route
    @app.route("/", methods=["GET"])
    def home():
        return {"message": "ChatGPT backend is running!"}

    return app
