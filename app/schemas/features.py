from pydantic import BaseModel, field_validator
from typing import Literal, Optional


class InputFeatures(BaseModel):
    surface_bati: float
    nombre_pieces: int
    type_local: Literal["Appartement", "Maison"]
    surface_terrain: float
    nombre_lots: Optional[int] = 1

    @field_validator("type_local", mode="before")
    def normalize_type_local(cls, v):
        v = v.strip().lower()
        if v == "maison":
            return "Maison"
        elif v == "appartement":
            return "Appartement"
        raise ValueError("type_local doit être 'Maison' ou 'Appartement'")
