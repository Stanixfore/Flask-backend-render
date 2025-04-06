from flask import Flask, request, jsonify
from flask_cors import CORS  # Gestion des autorisations CORS
import openai

# Initialiser Flask et Flask-CORS
app = Flask(__name__)
CORS(app)  # Activer CORS pour permettre l'accès depuis ton extension

# Configurer l'API OpenAI (assurez-vous que votre clé API est configurée)
openai.api_key = "votre_clé_API_OpenAI"

# Page d'accueil (facultative)
@app.route('/')
def home():
    """
    Page d'accueil du serveur Flask.
    """
    return "Bienvenue sur le serveur Flask IA ! Utilisez la route /chat pour interagir avec l'IA."

# Endpoint /chat pour gérer les requêtes de l'extension
@app.route('/chat', methods=['POST'])
def chat():
    """
    Gère les requêtes POST pour interagir avec l'IA.
    """
    try:
        # Extraire le message utilisateur depuis la requête JSON
        user_message = request.json.get("message", "")
        if not user_message.strip():
            return jsonify({"response": "Veuillez entrer un message valide."}), 400

        # Envoyer la requête à l'API OpenAI ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ou utilisez "gpt-4" si disponible
            messages=[
                {"role": "system", "content": "Tu es une IA utile et amicale."},
                {"role": "user", "content": user_message}
            ]
        )

        # Extraire la réponse de l'IA
        ai_response = response['choices'][0]['message']['content']
        return jsonify({"response": ai_response})

    except Exception as e:
        # Gestion des erreurs
        return jsonify({"response": f"Erreur interne du serveur : {str(e)}"}), 500

# Lancer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)
