from pydantic import BaseModel


class PredictionResponse(BaseModel):
    prix_m2_estime: float
    ville_modele: str
    model: str