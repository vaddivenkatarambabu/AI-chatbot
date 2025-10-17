# backend/routes/chat.py
from flask import Blueprint, request, jsonify
from services.openai_service import generate_reply

# Create a Blueprint (lets you organize routes into separate files)
chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    """
    POST /chat
    Expects JSON: { "message": "Hello" }
    Returns JSON: { "reply": "Hi there!" }
    """
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"error": "Missing 'message' field"}), 400

        user_message = data["message"].strip()
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        # Get response from OpenAI service
        reply = generate_reply(user_message)

        return jsonify({"reply": reply}), 200

    except Exception as e:
        print(f"Error in /chat route: {e}")
        return jsonify({"error": "Internal server error"}), 500
