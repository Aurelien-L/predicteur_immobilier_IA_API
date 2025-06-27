from pydantic import BaseModel

# Schéma de sortie utilisé dans les réponses de l'API après prédiction.
class PredictionResponse(BaseModel):
    """
    Schéma de réponse renvoyé par l'API après la prédiction du prix au m².

    Attributs :
        prix_m2_estime (float) : Le prix estimé au m², calculé par le modèle.
        ville_modele (str) : La ville associée au modèle utilisé ('Lille' ou 'Bordeaux').
        model (str) : Le type de modèle utilisé pour la prédiction ('maison' ou 'appartement').
    """
    prix_m2_estime: float
    ville_modele: str
    model: str