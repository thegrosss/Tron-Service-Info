from http.client import responses

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_wallet_info():
    test_address = "TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf"

    response = client.post(url="/wallet/info",
                           params={"address" : test_address})

    assert response.status_code == 200

    data = response.json()

    assert "energy" in data
    assert data["energy"] is not None

def test_get_wallet_entries():
    response = client.get(url="/wallet/entries",
                          params={"page" : 1,
                                  "per_page" : 10})

    assert response.status_code == 200

    data = response.json()

    assert "count" in data
    assert "items" in data

    assert isinstance(data["items"], list)