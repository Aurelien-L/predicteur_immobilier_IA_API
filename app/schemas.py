from pydantic import BaseModel
from typing import Literal, Optional

class InputFeatures(BaseModel):
    surface_bati: float
    nombre_pieces: int
    type_local: Literal["Appartement", "Maison"]
    surface_terrain: float
    nombre_lots: Optional[int] = 1

class DynamicInput(BaseModel):
    ville: Literal["lille", "bordeaux"]
    features: InputFeatures