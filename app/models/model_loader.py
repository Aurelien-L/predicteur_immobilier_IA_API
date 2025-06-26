import os
from joblib import load

pipeline_maisons = load("models/modeles_maisons.joblib")
pipeline_apparts = load("models/modeles_apparts.joblib")

MODELES = {
    "appartement": pipeline_apparts["Arbre de Décision"]["pipeline"],
    "maison": pipeline_maisons["Forêt Aléatoire"]["pipeline"]
}


# Exemple de récupération de score pour un modèle
# print(pipeline_maisons["Arbre de Décision"]["RMSE"])