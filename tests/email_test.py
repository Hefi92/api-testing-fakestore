import pytest
import requests

url = "https://jsonplaceholder.typicode.com/users/"

def test_email():
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()

    #tohle mi vytiskne jen 1 poslední email
    for info in data:
        one_email = info["email"]
        print(one_email)
    
    #tohle mi vytiskne všechny emaily z data
    all_emails = (info["email"] for info in data)
    print(list(all_emails))