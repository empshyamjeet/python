import pytest
import requests
import json

@pytest.fixture(scope="module")
def base_url():
    return "https://reqres.in/api"

def test_create_user(base_url):
    data = {
        "name": "chaya",
        "job": "BA"
    }
    response = requests.post(f"{base_url}/users", data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 201
    print(response.text)
