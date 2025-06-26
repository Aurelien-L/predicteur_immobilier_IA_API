import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_predict_dynamic_lille():
    payload = {
        "ville": "lille",
        "features": {
            "surface_bati": 90,
            "nombre_pieces": 4,
            "type_local": "Maison",
            "surface_terrain": 250,
            "nombre_lots": 1
        }
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["ville_modele"] == "Lille"

def test_post_predict_dynamic_bordeaux():
    payload = {
        "ville": "bordeaux",
        "features": {
            "surface_bati": 65,
            "nombre_pieces": 2,
            "type_local": "Appartement",
            "surface_terrain": 0,
            "nombre_lots": 1
        }
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["ville_modele"] == "Bordeaux"