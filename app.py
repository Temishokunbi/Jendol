from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "your-api-key"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful chatbot for Jendol Superstores."},
                  {"role": "user", "content": user_input}]
    )
    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == '__main__':
    app.run(debug=True)
