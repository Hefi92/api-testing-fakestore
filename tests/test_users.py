import pytest
import requests

def test_get_user():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()

    assert len(data) >= 5
    assert isinstance(data, list)

    assert data[0]["name"] == "Leanne Graham"

    emails = [user["email"] for user in data]
    assert "Julianne.OConner@kory.org" in emails

    suites = [user["address"]["suite"] for user in data]
    assert "Suite 351" in suites

    for user in data:
        assert isinstance(user["username"], str)

def test_get_user_9999():

    url = "https://jsonplaceholder.typicode.com/users/9999"

    response = requests.get(url)
    assert response.status_code == 404

    data = response.json()

    assert data == {}



