# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# @pytest.fixture(scope="module")
# def driver():
#     # Set the path to the chromedriver executable
#     driver_path = '/Volumes/Personal/python/Interview/driver/chromedriver'
#     service = Service(driver_path)
#     driver = webdriver.Chrome(service=service)
#     yield driver
#     driver.quit()

# def test_open_example_com(driver):
#     driver.get('https://www.example.com')
#     assert driver.title == "Example Domain"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("user-data-dir=/Users/shyamjeet/Library/Application Support/Google/Chrome")
chrome_options.add_argument("profile-directory=Profile 1")

# Define the correct ChromeDriver path
service = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.linkedin.com/feed/")

