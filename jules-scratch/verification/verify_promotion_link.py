from playwright.sync_api import sync_playwright, expect
import os

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get the absolute path to the HTML file
        # This is necessary because Playwright's page.goto() needs a proper URL or file path.
        # os.path.abspath() converts the relative path to an absolute one.
        # The 'file://' prefix is required for local files.
        index_path = f"file://{os.path.abspath('index.html')}"

        # 1. Navigate to the main page.
        page.goto(index_path)

        # 2. Locate the promotion card link.
        # We target the anchor tag with the '.card-link' class inside the '#promotions' section.
        promotion_card_link = page.locator("#promotions .card-link")

        # 3. Hover over the card to trigger the hover effect.
        promotion_card_link.hover()

        # 4. Take a screenshot to verify the hover effect is applied.
        # The CSS should add a shadow or lift effect.
        page.screenshot(path="jules-scratch/verification/hover_effect.png")

        # 5. Click the card to navigate to the promotion page.
        promotion_card_link.click()

        # 6. Wait for the new page to load and verify the URL.
        # This ensures the link works correctly.
        # We use a regex to check that the URL contains the promotion page's filename.
        import re
        expect(page).to_have_url(re.compile(".*new-client-promotion.html"))

        # 7. Take a screenshot of the destination page to confirm navigation.
        page.screenshot(path="jules-scratch/verification/promotion_page.png")

        browser.close()

if __name__ == "__main__":
    run_verification()