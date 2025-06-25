from app.model_loader import MODELES
from app.schemas import InputFeatures
import pandas as pd

# Mapping des noms API → noms utilisés dans les pipelines
COLUMN_MAPPING = {
    "surface_bati": "Surface reelle bati",
    "nombre_pieces": "Nombre pieces principales",
    "surface_terrain": "Surface terrain",
    "nombre_lots": "Nombre de lots",
    # "type_local": "Type local"  ← Non utilisé pour l'entraînement
}

# Colonnes attendues par chaque modèle
COLONNES_ATTENDUES = {
    "maison": [
        "Surface reelle bati", "Nombre pieces principales",
        "Surface terrain", "Nombre de lots"
    ],
    "appartement": [
        "Surface reelle bati", "Nombre pieces principales",
        "Nombre de lots"
    ]
}

def predict_price(data: InputFeatures):
    model_type = "maison" if data.type_local.lower() == "maison" else "appartement"
    pipeline = MODELES[model_type]

    # On transforme les données Pydantic en dictionnaire (model_dump), puis on les convertis en DataFrame
    df = pd.DataFrame([data.model_dump()])

    # Renommage des colonnes avec les noms attendus par le modèle
    df = df.rename(columns=COLUMN_MAPPING)

     # Sélection uniquement des colonnes utiles pour ce modèle
    colonnes_utiles = COLONNES_ATTENDUES[model_type]
    df = df[colonnes_utiles]

    # On fait la prédiction, puis on récupère la première valeur ([0]) car predict nous retourne une liste
    prediction = pipeline.predict(df)[0]

    # On retourne le prix arrondit à 2 décimales et le type de modèle utilisé
    return round(prediction, 2), model_type