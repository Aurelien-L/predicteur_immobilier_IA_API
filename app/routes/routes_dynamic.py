from fastapi import APIRouter, HTTPException
from ..schemas import DynamicInput, PredictionResponse
from ..services.predict import predict_price

# Création d'un routeur FastAPI pour la prédiction dynamique (ville choisie via payload)
router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_dynamic(payload: DynamicInput):
    """
    Endpoint POST /predict

    Reçoit un payload contenant :
    - la ville ciblée ("lille" ou "bordeaux")
    - les caractéristiques du bien immobilier

    Retourne une prédiction du prix au m² en utilisant le modèle approprié
    pour la ville sélectionnée.

    Args:
        payload (DynamicInput): Données combinées comprenant la ville (`ville`)
                                 et les caractéristiques du bien (`features`).

    Returns:
        dict: Un dictionnaire contenant :
            - prix_m2_estime (float) : le prix estimé au m² (arrondi à 2 décimales),
            - ville_modele (str) : "Lille" ou "Bordeaux",
            - model (str) : type de bien détecté ("maison" ou "appartement").

    Raises:
        HTTPException: 
            - 400 si la ville n’est pas supportée,
            - 400 si une erreur se produit pendant la prédiction.
    """

    try:
        # On met en minuscule la ville reçue pour éviter les problèmes de casse
        ville = payload.ville.lower()

        # Vérifie que la ville fait bien partie des options autorisées
        if ville not in ["lille", "bordeaux"]:
            raise HTTPException(status_code=400, detail="Ville non reconnue")
        
        # On appelle le service de prédiction avec les caractéristiques du bien
        prix, type_bien = await predict_price(payload.features)

        # On construit la réponse structurée avec le nom capitalisé de la ville
        return {
            "prix_m2_estime": prix,
            "ville_modele": ville.capitalize(),
            "model": type_bien
        }
    except Exception as e:
        # Gestion générique des erreurs avec une réponse 400
        raise HTTPException(status_code=400, detail=str(e))