from fastapi import FastAPI
from .routes.routes_lille import router as lille_router
from .routes.routes_bordeaux import router as bordeaux_router
from .routes.routes_dynamic import router as dynamic_router


app = FastAPI()

app.include_router(lille_router)
app.include_router(bordeaux_router)
app.include_router(dynamic_router)
