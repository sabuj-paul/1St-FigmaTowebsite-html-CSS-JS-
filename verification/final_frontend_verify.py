import os
from playwright.sync_api import sync_playwright, expect

def test_mobile_menu(page):
    # Load the local index.html
    url = "file://" + os.path.abspath("index.html")
    page.goto(url)

    # Set viewport to mobile
    page.set_viewport_size({"width": 375, "height": 667})

    # 1. Verify toggle exists and has ARIA attributes
    toggle = page.locator("#menu-toggle")
    expect(toggle).to_be_visible()
    expect(toggle).to_have_attribute("aria-expanded", "false")

    # 2. Click toggle and verify sidebar opens and focus shifts
    toggle.click()
    sidebar = page.locator("#sidebar-nav")
    expect(sidebar).to_be_visible()
    expect(toggle).to_have_attribute("aria-expanded", "true")

    close_btn = page.locator("#close-sidebar")
    expect(close_btn).to_be_focused()

    # Take screenshot of open sidebar
    page.screenshot(path="verification/mobile_menu_open.png")

    # 3. Click close and verify sidebar closes and focus returns
    close_btn.click()
    expect(sidebar).not_to_be_visible()
    expect(toggle).to_have_attribute("aria-expanded", "false")
    expect(toggle).to_be_focused()

    # Take screenshot of closed sidebar
    page.screenshot(path="verification/mobile_menu_closed.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_mobile_menu(page)
            print("Verification successful!")
        finally:
            browser.close()
