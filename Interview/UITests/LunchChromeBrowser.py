import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def driver():
    # Set the path to the chromedriver executable
    driver_path = '/Volumes/Personal/python/Interview/driver/chromedriver'
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_open_example_com(driver):
    driver.get('https://www.example.com')
    assert driver.title == "Example Domain"
