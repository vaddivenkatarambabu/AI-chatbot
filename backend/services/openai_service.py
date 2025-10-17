# backend/services/openai_service.py
import os
import openai
from dotenv import load_dotenv

# Load environment variables (for OPENAI_API_KEY)
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_reply(user_message: str) -> str:
    """
    Sends a user message to the OpenAI Chat API and returns the assistant's reply.
    """

    if not openai.api_key:
        raise ValueError("OpenAI API key is missing. Set OPENAI_API_KEY in your .env file.")

    try:
        # Create a chat completion
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # You can change to gpt-4o or gpt-3.5-turbo
            messages=[
                {"role": "system", "content": "You are a helpful, polite assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=512,
            temperature=0.7,
        )

        # Extract assistant's reply
        reply = response.choices[0].message["content"].strip()
        return reply

    except Exception as e:
        print(f"Error while generating reply: {e}")
        return "Sorry, I couldn't generate a response right now."
