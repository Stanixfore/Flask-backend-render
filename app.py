from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Initialiser Flask et Flask-CORS
app = Flask(__name__)
CORS(app)

# Configurer l'API OpenAI (remplace par ta clé API)
openai.api_key = "votre_clé_API_OpenAI"

@app.route('/')
def home():
    return "Bienvenue sur le serveur Flask IA ! Utilisez la route /chat pour discuter avec l'IA."

@app.route('/chat', methods=['POST'])
def chat():
    """
    Gère les requêtes POST pour interagir avec l'IA.
    """
    try:
        # Log des données reçues
        print("Requête reçue : ", request.json)
        
        # Extraire le message utilisateur
        user_message = request.json.get("message", "")
        if not user_message.strip():
            print("Erreur : message vide")
            return jsonify({"response": "Message vide. Veuillez entrer un texte valide."}), 400
        
        # Log pour le message utilisateur
        print("Message utilisateur : ", user_message)

        # Envoyer la requête à l'API OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ou "gpt-4" si disponible
            messages=[
                {"role": "system", "content": "Tu es une IA utile et amicale."},
                {"role": "user", "content": user_message}
            ]
        )

        # Extraire la réponse de l'IA
        ai_response = response['choices'][0]['message']['content']
        print("Réponse de l'IA : ", ai_response)
        return jsonify({"response": ai_response})

    except Exception as e:
        # Log pour les erreurs
        print("Erreur interne : ", str(e))
        return jsonify({"response": f"Erreur interne du serveur : {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
