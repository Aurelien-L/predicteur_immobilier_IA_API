from fastapi import APIRouter, HTTPException
from ..schemas import InputFeatures, PredictionResponse
from ..services.predict import predict_price

router = APIRouter()
    

@router.post("/predict/bordeaux", response_model=PredictionResponse)
async def predict_bordeaux(data: InputFeatures):
    try:
        prix, type_bien = await predict_price(data)
        return {
            "prix_m2_estime": prix,
            "ville_modele": "Bordeaux",
            "model": type_bien
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    