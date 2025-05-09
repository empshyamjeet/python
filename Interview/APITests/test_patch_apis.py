import pytest
import requests
import json

@pytest.fixture(scope="module")
def base_url():
    return "https://reqres.in/api"

def test_patch_user(base_url):
    data = {
        "name": "chaya",
        "job": "BAA"
    }
    response = requests.patch(f"{base_url}/users", data=json.dumps(data), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    print(response.text)
