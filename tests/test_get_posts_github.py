import pytest
import requests


def test_get_posts_ok():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 50
    keys = ["userId", "id", "title", "body"]
    for key in keys:
        assert key in data[0] 
        assert isinstance(data[0][key], (int, str)) 

def test_get_post_id_1():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1 



    