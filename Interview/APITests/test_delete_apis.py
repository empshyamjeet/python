import pytest
import requests

@pytest.fixture(scope="module")
def base_url():
    return "https://reqres.in/api"

def test_delete_user(base_url):
    response = requests.delete(f"{base_url}/users/2")
    assert response.status_code == 204
    print(response.text)
