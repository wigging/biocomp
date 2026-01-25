"""Tests for the app module."""

import pytest

import biocomp.app
from biocomp.app import app, biocomp_version


def test_biocomp_version():
    result = biocomp_version()
    assert result["version"] == "26.1"


@pytest.fixture
def client():
    return app.test_client()


@pytest.mark.asyncio
async def test_index(client):
    response = await client.get("/")
    assert response.status_code == 200
    data = await response.get_data(as_text=True)
    assert "BioComp" in data
    assert "Ultimate analysis" in data
    assert "Biomass composition" in data


@pytest.mark.asyncio
async def test_docs(client):
    response = await client.get("/docs")
    assert response.status_code == 200
    data = await response.get_data(as_text=True)
    assert "BioComp" in data
    assert "Documentation" in data
    assert "Quick start" in data


@pytest.mark.asyncio
async def test_params(client, monkeypatch):
    mock_bc = {
        "x_daf": [0.1, 0.2, 0.3, 0.1, 0.1, 0.1, 0.1],
        "x_wet": [0.1, 0.2, 0.3, 0.1, 0.1, 0.1, 0.1],
        "y_daf": [0.1, 0.2, 0.3, 0.1, 0.1, 0.1, 0.1],
        "y_wet": [0.1, 0.2, 0.3, 0.1, 0.1, 0.1, 0.1],
        "y_wetash": [0.1, 0.2, 0.3, 0.1, 0.1, 0.1, 0.1],
        "y_rm1": [0.1, 0.2, 0.3],
        "y_rm2": [0.1, 0.2, 0.3],
        "y_rm3": [0.1, 0.2, 0.3],
    }
    mock_splits = (0.6, 0.8, 0.8, 1.0, 1.0)
    mock_return = (0.53, 0.06, mock_bc, mock_splits)

    monkeypatch.setattr(biocomp.app, "calc_biocomp", lambda form: mock_return)

    response = await client.post("/params", form={"carbon": "53", "hydrogen": "6"})
    assert response.status_code == 200
    data = await response.get_data(as_text=True)
    assert "CELL" in data
    assert "HEMI" in data
    assert "LIG-C" in data
    assert "α = 0.6" in data
