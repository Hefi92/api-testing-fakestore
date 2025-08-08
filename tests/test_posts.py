import pytest
import requests

def test_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Learning testing API.",
        "body": "POST method verification.",
        "userId": 3
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 201
    data = response.json()

    assert isinstance(data, dict)
    assert data["userId"] == 3

def test_post_1():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Data adding to post '1'.",
        "body": "Check the conditions by 'assert'.",
        "userId": 1
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 201
    data = response.json()

    assert data["id"] == 101
    assert data["userId"] == payload["userId"]

    def test_post_9999():
        payload = {
        "title": "Testing error scenario.",
        "body": "This test will lead to error.",
        "userId": 9999
    }

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.post(url, json=payload)
    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
