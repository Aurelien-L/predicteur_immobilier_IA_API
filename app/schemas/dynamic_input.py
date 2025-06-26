from pydantic import BaseModel, field_validator
from typing import Literal, Optional
from app.schemas.features import InputFeatures


class DynamicInput(BaseModel):
    ville: Literal["lille", "bordeaux"]
    features: InputFeatures

    @field_validator("ville", mode="before")
    def normalize_ville(cls, v):
        v = v.strip().lower()
        if v in ["lille", "bordeaux"]:
            return v
        raise ValueError("ville doit être 'lille' ou 'bordeaux'")