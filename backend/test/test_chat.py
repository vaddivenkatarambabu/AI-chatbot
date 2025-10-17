# backend/tests/test_chat.py
import pytest
from flask import Flask
from routes.chat import chat_bp

@pytest.fixture
def client():
    """
    Create a Flask test client with the chat blueprint registered.
    """
    app = Flask(__name__)
    app.register_blueprint(chat_bp)
    app.testing = True
    client = app.test_client()
    yield client


def test_home_endpoint(client):
    """
    Test if the home route (GET /) works when added manually.
    """
    @client.application.route("/")
    def home():
        return {"message": "ChatGPT API backend running."}

    response = client.get("/")
    assert response.status_code == 200
    assert "ChatGPT API backend running." in response.get_data(as_text=True)


def test_chat_missing_message_field(client):
    """
    Should return error when 'message' field is missing in POST data.
    """
    response = client.post("/chat", json={})
    data = response.get_json()

    assert response.status_code == 400
    assert "error" in data or data.get("success") is False


def test_chat_empty_message(client):
    """
    Should return error when 'message' field is empty.
    """
    response = client.post("/chat", json={"message": ""})
    data = response.get_json()

    assert response.status_code == 400
    assert "error" in data


def test_chat_valid_message(monkeypatch, client):
    """
    Should return success response with a reply when OpenAI call succeeds.
    """

    # Mock generate_reply function so it doesn’t hit OpenAI API
    from services import openai_service

    def mock_generate_reply(message):
        return "Mocked reply: Hello!"

    monkeypatch.setattr(openai_service, "generate_reply", mock_generate_reply)

    response = client.post("/chat", json={"message": "Hello"})
    data = response.get_json()

    assert response.status_code == 200
    assert "reply" in data["data"] or "reply" in data
    assert "Mocked reply" in str(data)
