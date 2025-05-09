import pytest
import requests
import json

@pytest.fixture(scope="module")
def base_url():
    return "https://reqres.in/api"

def test_update_user(base_url):
    data = {
        "name": "chaya",
        "job": "BAA"
    }
    response = requests.put(f"{base_url}/users/2", data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    print(response.text)
