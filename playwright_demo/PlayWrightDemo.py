from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Launch Chrome browser
        browser = p.chromium.launch(channel="chrome", headless=False)  # Set headless=True if no UI needed
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Go to a website
        page.goto("https://example.com")

        # Step 2: Verify the page title
        assert "Example Domain" in page.title()
        print("✅ Title verified!")

        # Step 3: Click on the More Information link
        page.click("text=More information")

        # Step 4: Wait for navigation and verify new page URL
        page.wait_for_load_state("networkidle")
        assert "iana.org" in page.url
        print("✅ Navigation and URL verified!")

        # Close the browser
        browser.close()

if __name__ == "__main__":
    run()
