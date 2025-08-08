import requests

BASE_URL = "https://fakestoreapi.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def test_get_all_products():
    response = requests.get(f"{BASE_URL}/products", headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
