from fastapi import FastAPI
from app.routes import router as predict_router

app = FastAPI()

# On inclue les routes
app.include_router(predict_router)

