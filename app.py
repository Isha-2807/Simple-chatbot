from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Load responses from JSON file
with open('/Users/ishagovind/Downloads/chatbot-trial3/config.json', 'r') as f:
    data = json.load(f)
    responses = data['chatbot']['responses']  # Access the nested 'responses' dictionary

# Define mappings for different types of messages
input_mapping = {
    "hello": "greeting",
    "hi": "greeting",
    "hey": "greeting",
    "goodbye": "farewell",
    "bye": "farewell"
}

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').lower()  # Convert to lowercase for consistency
    # Determine the key to look up in the responses based on user input
    response_key = input_mapping.get(user_input, "default")
    # Get the appropriate response or fall back to the default response
    response = responses.get(response_key, "Sorry, I don't understand.")
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5502)
