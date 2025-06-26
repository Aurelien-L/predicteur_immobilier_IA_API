import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_predict_bordeaux():
    payload = {
        "surface_bati": 80,
        "nombre_pieces": 3,
        "type_local": "Appartement",
        "surface_terrain": 0,
        "nombre_lots": 2
    }
    response = client.post("/predict/bordeaux", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prix_m2_estime" in data
    assert data["ville_modele"] == "Bordeaux"