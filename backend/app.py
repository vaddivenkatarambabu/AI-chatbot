# app.py
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# -------------------------
# Initialize Flask app
# -------------------------
app = Flask(__name__)
CORS(app)  # allow frontend requests (React/Vue/etc.)

# -------------------------
# Routes
# -------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "ChatGPT backend is running!"})


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        # Call OpenAI API
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # You can use gpt-4o, gpt-3.5-turbo, etc.
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=512,
            temperature=0.7,
        )

        reply = completion.choices[0].message["content"].strip()
        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


# -------------------------
# Run the server
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
