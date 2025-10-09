import os
from playwright.sync_api import sync_playwright, Page, expect

def verify_changes(page: Page):
    """
    This script verifies the following changes:
    1. The main header has the "Book Now" button next to the text.
    2. The calendar navigation buttons are icons.
    3. The sticky header appears on scroll with the correct styling.
    """
    file_path = os.path.abspath('index.html')
    page.goto(f'file://{file_path}')

    # 1. Verify the initial page layout (main header and nav icons)
    # Check that the main title card has the correct flex layout
    expect(page.locator('#title-card')).to_have_css('display', 'flex')
    # Check that the calendar nav buttons contain SVGs
    expect(page.locator('#cal-back svg')).to_be_visible()

    # Take a screenshot of the entire page to see the general layout
    page.screenshot(path='jules-scratch/verification/verification_fullpage.png', full_page=True)

    # 2. Scroll down to trigger the sticky header
    page.evaluate('window.scrollTo(0, 500)')

    # 3. Wait for the sticky header to be visible and take a screenshot of it
    sticky_header = page.locator('#sticky-header')

    # The 'scrolled' class is added by the script.js, let's wait for it
    expect(page.locator('body.scrolled #sticky-header')).to_be_visible()

    # Assert correct styling on the sticky header
    expect(sticky_header).to_have_css('background-color', 'rgb(160, 82, 45)') # --brand-primary
    expect(sticky_header).to_have_css('color', 'rgb(255, 255, 255)') # --card-bg (white)

    # Take a screenshot of only the sticky header element for focused verification
    sticky_header.screenshot(path='jules-scratch/verification/verification_sticky_header.png')


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    verify_changes(page)
    browser.close()