from pydantic import BaseModel, field_validator
from typing import Literal, Optional


# Schéma Pydantic représentant les caractéristiques d'un bien immobilier.
class InputFeatures(BaseModel):
    """
    Schéma de données d'entrée pour une prédiction de prix au m².

    Attributs :
        surface_bati (float) : Surface bâtie réelle du bien (en m²).
        nombre_pieces (int) : Nombre de pièces principales.
        type_local (str) : Type du bien ('Appartement' ou 'Maison').
        surface_terrain (float) : Surface du terrain (en m²).
        nombre_lots (Optional[int]) : Nombre de lots (facultatif, défaut = 1).
    """
    surface_bati: float
    nombre_pieces: int
    type_local: Literal["Appartement", "Maison"]
    surface_terrain: float
    nombre_lots: Optional[int] = 1

    @field_validator("type_local", mode="before")
    def normalize_type_local(cls, v):
        """
        Valide et normalise le champ 'type_local' :
        - Supprime les espaces autour
        - Convertit en minuscules pour vérifier la validité
        - Renvoie la forme capitalisée attendue par le modèle

        Args:
            v (str): Valeur brute reçue pour 'type_local'

        Returns:
            str: 'Maison' ou 'Appartement' si valide

        Raises:
            ValueError: Si la valeur est autre que 'maison' ou 'appartement'
        """
        v = v.strip().lower()
        if v == "maison":
            return "Maison"
        elif v == "appartement":
            return "Appartement"
        raise ValueError("type_local doit être 'Maison' ou 'Appartement'")
