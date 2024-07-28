import openai
from flask import Flask, request, jsonify

# Configurar tu clave API de OpenAI (requiere una cuenta en OpenAI)
openai.api_key = 'API_KEY'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Configuración de Flask
app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    prompt = data.get('prompt', '')
    response = generate_response(prompt)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(port=5000)
