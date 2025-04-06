from flask import Flask, request, jsonify
from flask_cors import CORS  # Importer Flask-CORS
from chat_logic import generate_response  # Importer ta logique d'IA

# Création de l'application Flask
app = Flask(__name__)
CORS(app)  # Activer CORS pour toutes les routes

# Route pour la page d'accueil (optionnel)
@app.route('/')
def home():
    """
    Page d'accueil du serveur Flask.
    """
    return "Bienvenue sur le serveur Flask IA ! Utilisez la route /chat pour discuter avec l'IA."

# Route pour interagir avec l'IA
@app.route('/chat', methods=['POST'])
def chat():
    """
    Gère les requêtes POST envoyées par l'extension de navigateur.
    Attend un message utilisateur et renvoie une réponse générée par l'IA.
    """
    try:
        # Extraire le message utilisateur depuis les données JSON de la requête
        user_message = request.json.get("message", "")
        if not user_message.strip():
            return jsonify({"response": "Message vide. Veuillez entrer une question ou une phrase valide."}), 400

        # Utiliser la fonction pour générer une réponse de l'IA
        response = generate_response(user_message)
        return jsonify({"response": response})
    
    except Exception as e:
        # Gérer les erreurs et retourner une réponse appropriée
        return jsonify({"response": f"Erreur interne du serveur : {str(e)}"}), 500

# Lancer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)
