from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

# Create OpenAI client
load_dotenv()  # This loads everything from .env into your system

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    reply = completion.choices[0].message.content

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)


