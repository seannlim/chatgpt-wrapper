from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# Create OpenAI client
client = OpenAI(api_key="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")

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


