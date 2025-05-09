import pytest
import requests

@pytest.fixture(scope="module")
def base_url():
    return "https://reqres.in/api"

def test_get_users(base_url):
    response = requests.get(f"{base_url}/users?page=2")
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
    print(response.json())
    print(response.headers)

def test_get_user_data(base_url):
    response = requests.get(f"{base_url}/users?page=2")
    assert response.status_code == 200
    assert response.json()['data'][0]['id'] == 7

def test_get_user_names(base_url):
    response = requests.get(f"{base_url}/users?page=2")
    assert response.status_code == 200
    assert response.json()['data'][1]['id'] == 8
    assert "Michael" in [user['first_name'] for user in response.json()['data']]
    assert "Lindsay" in [user['first_name'] for user in response.json()['data']]
    print(response.text)
