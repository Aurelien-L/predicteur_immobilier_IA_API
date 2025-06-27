from app.models.model_loader import MODELES
from app.schemas.features import InputFeatures
import pandas as pd


# Dictionnaire de correspondance entre les noms de champs reçus via l'API
# et les noms attendus dans les pipelines de Machine Learning.
COLUMN_MAPPING = {
    "surface_bati": "Surface reelle bati",
    "nombre_pieces": "Nombre pieces principales",
    "surface_terrain": "Surface terrain",
    "nombre_lots": "Nombre de lots",
    # "type_local": "Type local"  ← Non utilisé pour l'entraînement
}

# Liste des colonnes à utiliser pour chaque type de bien dans le modèle.
COLONNES_ATTENDUES = {
    "maison": [
        "Surface reelle bati", "Nombre de lots",
        "Surface terrain", "Nombre pieces principales"
    ],
    "appartement": [
        "Surface reelle bati",
        "Nombre de lots", "Nombre pieces principales"
    ]
}


async def predict_price(data: InputFeatures):
    """
    Prédit le prix au m² en fonction des caractéristiques d'un bien immobilier.

    Args:
        data (InputFeatures): Données d'entrée validées via Pydantic contenant
                              les informations sur le bien (surface, type, etc.)

    Returns:
        tuple: (prix_m2_estime arrondi à 2 décimales, type de modèle utilisé ["maison" ou "appartement"])
    """
    # Détermination du type de bien à partir du champ `type_local`
    model_type = "maison" if data.type_local.lower() == "maison" else "appartement"

    # Récupération du pipeline de prédiction correspondant
    pipeline = MODELES[model_type]

    # Conversion des données Pydantic en dictionnaire, puis en DataFrame
    df = pd.DataFrame([data.model_dump()])

    # Renommage des colonnes selon le format attendu par le modèle
    df = df.rename(columns=COLUMN_MAPPING)

     # Sélection uniquement des colonnes pertinentes pour ce modèle
    colonnes_utiles = COLONNES_ATTENDUES[model_type]
    df = df[colonnes_utiles]

    # Prédiction du prix à partir du modèle, puis extraction de la première valeur ([0])
    prediction = pipeline.predict(df)[0]

    # Retour du prix arrondi et du type de modèle utilisé
    return round(prediction, 2), model_type