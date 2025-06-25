from fastapi import APIRouter, HTTPException
from app.schemas import InputFeatures, DynamicInput
from app.predict import predict_price

router = APIRouter()

@router.post("/predict/lille")
def predict_lille(data: InputFeatures):
    try:
        prix, type_bien = predict_price(data)
        return {
            "prix_m2_estime": prix,
            "ville_modele": "Lille",
            "model": type_bien
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.post("/predict/bordeaux")
def predict_bordeaux(data: InputFeatures):
    try:
        prix, type_bien = predict_price(data)
        return {
            "prix_m2_estime": prix,
            "ville_modele": "Bordeaux",
            "model": type_bien
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.post("/predict")
def predict_dynamic(payload: DynamicInput):
    try:
        ville = payload.ville.lower()
        if ville not in ["lille", "bordeaux"]:
            raise HTTPException(status_code=400, detail="Ville non reconnue")
        prix, type_bien = predict_price(payload.features)
        return {
            "prix_m2_estime": prix,
            "ville_modele": ville.capitalize(),
            "model": type_bien
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))