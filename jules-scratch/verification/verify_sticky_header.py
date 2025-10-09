import os
from playwright.sync_api import sync_playwright, expect

def run_verification():
    """
    This script verifies the sticky header functionality.
    It opens the local index.html file, scrolls down to trigger the header,
    and takes a screenshot for visual confirmation.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Arrange: Go to the local index.html file.
        # We construct an absolute file path to ensure Playwright can find it.
        file_path = "file://" + os.path.abspath("index.html")
        page.goto(file_path)

        # 2. Act: Scroll down the page to trigger the sticky header.
        # The script is set to trigger when scrolling past the #title-card element.
        # Scrolling to the bottom of the page ensures it will be visible.
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        # 3. Assert: Check that the sticky header is visible.
        # We use expect().to_be_visible() which waits for the element to appear.
        sticky_header = page.locator("#sticky-header")
        expect(sticky_header).to_be_visible()

        # 4. Screenshot: Capture the result.
        screenshot_path = "jules-scratch/verification/verification.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run_verification()