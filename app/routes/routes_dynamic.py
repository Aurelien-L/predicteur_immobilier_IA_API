from fastapi import APIRouter, HTTPException
from ..schemas import DynamicInput, PredictionResponse
from ..services.predict import predict_price

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_dynamic(payload: DynamicInput):
    try:
        ville = payload.ville.lower()
        if ville not in ["lille", "bordeaux"]:
            raise HTTPException(status_code=400, detail="Ville non reconnue")
        prix, type_bien = await predict_price(payload.features)
        return {
            "prix_m2_estime": prix,
            "ville_modele": ville.capitalize(),
            "model": type_bien
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))