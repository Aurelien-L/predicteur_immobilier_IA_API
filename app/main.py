from fastapi import FastAPI
from .routes.routes_lille import router as lille_router
from .routes.routes_bordeaux import router as bordeaux_router
from .routes.routes_dynamic import router as dynamic_router

# Création de l'application FastAPI
app = FastAPI()

# Inclusion des routes spécifiques au modèle de Lille
app.include_router(lille_router)

# Inclusion des routes spécifiques au modèle de Bordeaux
app.include_router(bordeaux_router)

# Inclusion des routes dynamiques qui choisissent le modèle selon la ville envoyée
app.include_router(dynamic_router)
