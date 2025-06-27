import pytest
from app.schemas.features import InputFeatures
from app.services.predict import predict_price

@pytest.mark.asyncio
async def test_predict_price_maison():
    input_data = InputFeatures(
        surface_bati=120,
        nombre_pieces=5,
        type_local="Maison",
        surface_terrain=300,
        nombre_lots=1
    )

    prix, model_type = await predict_price(input_data)
    assert isinstance(prix, float)
    assert model_type == "maison"

@pytest.mark.asyncio
async def test_predict_price_appartement():
    input_data = InputFeatures(
        surface_bati=60,
        nombre_pieces=3,
        type_local="Appartement",
        surface_terrain=0,  # inutile mais requis par le modèle
        nombre_lots=2
    )

    prix, model_type = await predict_price(input_data)
    assert isinstance(prix, float)
    assert model_type == "appartement"