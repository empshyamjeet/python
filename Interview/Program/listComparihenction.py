from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set headless=False to see the browser
    page = browser.new_page()
    page.goto("https://www.google.com")
    # Add your actions here
    browser.close()