from fastapi import APIRouter, HTTPException
from ..schemas import InputFeatures, PredictionResponse
from ..services.predict import predict_price


router = APIRouter()

@router.post("/predict/lille", response_model=PredictionResponse)
async def predict_lille(data: InputFeatures):
    try:
        prix, type_bien = await predict_price(data)
        return {
            "prix_m2_estime": prix,
            "ville_modele": "Lille",
            "model": type_bien
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    