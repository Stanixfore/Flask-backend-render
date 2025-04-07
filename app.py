from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Initialiser Flask et Flask-CORS
app = Flask(__name__)
CORS(app)

# Configurer la clé API OpenAI
openai.api_key = "ta_clé_API_OpenAI"

@app.route('/')
def home():
    return "Bienvenue sur le serveur Flask IA !"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Vérifier la requête
        user_message = request.json.get("message", "")
        if not user_message.strip():
            return jsonify({"response": "Message vide. Veuillez entrer un texte valide."}), 400

        # Envoyer la requête à l'API OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Tu es une IA utile et amicale."},
                {"role": "user", "content": user_message}
            ]
        )

        # Extraire la réponse de l'IA
        ai_response = response['choices'][0]['message']['content']
        return jsonify({"response": ai_response})

    except Exception as e:
        return jsonify({"response": f"Erreur interne : {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
