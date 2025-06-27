import os
from joblib import load


"""
    Ce script charge les pipeline enregistré avec Joblib, puis
    crée un dictionnaire définissant quel modèle utiliser pour la
    prédiction du prix au m² des maisons et des appartements
    
"""


pipeline_maisons = load("models/modeles_maisons.joblib")
pipeline_apparts = load("models/modeles_apparts.joblib")

MODELES = {
    "appartement": pipeline_apparts["Arbre de Décision"]["pipeline"],
    "maison": pipeline_maisons["Forêt Aléatoire"]["pipeline"]
}


# Exemple de récupération de score pour un modèle
# print(pipeline_maisons["Arbre de Décision"]["RMSE"])