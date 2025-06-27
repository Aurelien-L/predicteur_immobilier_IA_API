from fastapi import APIRouter, HTTPException
from ..schemas import InputFeatures, PredictionResponse
from ..services.predict import predict_price

# Création d'un routeur FastAPI pour les routes liées à Bordeaux
router = APIRouter()
    

@router.post("/predict/bordeaux", response_model=PredictionResponse)
async def predict_bordeaux(data: InputFeatures):
    """
    Endpoint POST /predict/bordeaux

    Reçoit en entrée les caractéristiques d'un bien immobilier (surface, nombre de pièces, etc.)
    sous forme d'un objet `InputFeatures`, puis retourne une estimation du prix au m²
    en utilisant un modèle de machine learning spécifique.

    Args:
        data (InputFeatures): Données d'entrée décrivant le bien immobilier à évaluer.

    Returns:
        dict: Un dictionnaire contenant :
            - prix_m2_estime (float) : le prix estimé au m² (arrondi à 2 décimales),
            - ville_modele (str) : toujours "Bordeaux",
            - model (str) : type de modèle utilisé ("maison" ou "appartement").

    Raises:
        HTTPException: Erreur 400 en cas de problème lors de la prédiction (erreur de données, modèle, etc.).
    """
    try:
         # Appel du service de prédiction (asynchrone) avec les données d'entrée
        prix, type_bien = await predict_price(data)

        # Construction de la réponse standardisée
        return {
            "prix_m2_estime": prix,
            "ville_modele": "Bordeaux",
            "model": type_bien
        }
    except Exception as e:
        # Si une erreur survient, on la capture et on renvoie une HTTPException 400 avec le message d'erreur
        raise HTTPException(status_code=400, detail=str(e))
    