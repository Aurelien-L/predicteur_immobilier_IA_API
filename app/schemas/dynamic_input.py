from pydantic import BaseModel, field_validator
from typing import Literal, Optional
from app.schemas.features import InputFeatures

# Schéma Pydantic utilisé pour les requêtes dynamiques, 
# où la ville est spécifiée dans les données avec ses caractéristiques.
class DynamicInput(BaseModel):
    """
    Schéma d'entrée pour l'endpoint dynamique de prédiction (/predict).

    Attributs :
        ville (str) : Doit être 'lille' ou 'bordeaux' (insensible à la casse).
        features (InputFeatures) : Caractéristiques du bien immobilier.
    """

    ville: Literal["lille", "bordeaux"]
    features: InputFeatures

    @field_validator("ville", mode="before")
    def normalize_ville(cls, v):
        """
        Valide et normalise le champ 'ville' :
        - Supprime les espaces autour
        - Convertit en minuscules
        - Vérifie que la valeur fait partie des choix autorisés
        
        Args:
            v (str): Valeur saisie pour 'ville'

        Returns:
            str: Valeur normalisée si valide

        Raises:
            ValueError: Si la ville n'est pas 'lille' ou 'bordeaux'
        """
        
        v = v.strip().lower()
        if v in ["lille", "bordeaux"]:
            return v
        raise ValueError("ville doit être 'lille' ou 'bordeaux'")