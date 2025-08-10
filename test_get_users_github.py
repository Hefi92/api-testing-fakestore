import pytest
import requests

def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data["username"], str) 
    assert "address" in data 
    