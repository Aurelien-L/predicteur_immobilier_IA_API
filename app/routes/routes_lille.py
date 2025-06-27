from fastapi import APIRouter, HTTPException
from ..schemas import InputFeatures, PredictionResponse
from ..services.predict import predict_price

# Création du routeur FastAPI pour les routes spécifiques à la ville de Lille
router = APIRouter()

@router.post("/predict/lille", response_model=PredictionResponse)
async def predict_lille(data: InputFeatures):
    """
    Endpoint POST /predict/lille

    Utilise le modèle de prédiction spécifique à Lille pour estimer le prix au m²
    d’un bien immobilier en fonction de ses caractéristiques.

    Args:
        data (InputFeatures): Les caractéristiques du bien à évaluer :
            - surface_bati
            - nombre_pieces
            - surface_terrain
            - nombre_lots
            - type_local (maison ou appartement)

    Returns:
        dict: Un dictionnaire contenant :
            - prix_m2_estime (float) : le prix estimé au m² (arrondi à 2 décimales),
            - ville_modele (str) : "Lille" (fixe),
            - model (str) : type de bien détecté ("maison" ou "appartement").

    Raises:
        HTTPException: Retourne une erreur 400 avec le message d’erreur en cas de problème
                       pendant la prédiction (ex. : données invalides, modèle indisponible).
    """

    try:
        # Appelle le service de prédiction avec les données d'entrée
        prix, type_bien = await predict_price(data)

        # Retourne les résultats sous forme de dictionnaire structuré
        return {
            "prix_m2_estime": prix,
            "ville_modele": "Lille",
            "model": type_bien
        }
    
    except Exception as e:
        # Gestion d'erreur générique : envoie une exception HTTP 400 avec le message d'erreur
        raise HTTPException(status_code=400, detail=str(e))
    