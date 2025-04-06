import openai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Charger la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(user_message):
    """
    Génère une réponse à partir d'un message utilisateur en utilisant l'API OpenAI.

    Args:
        user_message (str): Le message envoyé par l'utilisateur.

    Returns:
        str: La réponse générée par l'IA ou un message d'erreur en cas de problème.
    """
    # Validation du message utilisateur
    if not user_message.strip():
        return "Message vide. Veuillez entrer une question ou une phrase valide."

    try:
        # Appel à l'API OpenAI pour générer une réponse
        response = openai.Completion.create(
            engine="text-davinci-003",  # Modèle utilisé
            prompt=f"Utilisateur : {user_message}\nIA :",
            max_tokens=150,            # Longueur maximale de la réponse
            temperature=0.7            # Niveau de créativité des réponses
        )
        # Extraire et retourner la réponse textuelle générée par l'IA
        return response.choices[0].text.strip()
    except Exception as e:
        # Retourner un message d'erreur en cas de problème
        return f"Erreur : {str(e)}"
