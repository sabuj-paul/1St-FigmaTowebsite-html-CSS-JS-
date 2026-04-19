import asyncio
import os
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        url = "file://" + os.path.abspath("index.html")
        await page.goto(url)

        # Test 1: ARIA labels and focus visibility on desktop
        print("Test 1: Desktop Footer Accessibility")
        facebook_link = await page.query_selector('a[aria-label="Facebook"]')
        assert facebook_link is not None, "Facebook link missing aria-label"
        print("✅ Facebook aria-label found")

        # Test 2: Mobile Navigation Accessibility
        print("\nTest 2: Mobile Navigation Accessibility")
        await page.set_viewport_size({"width": 375, "height": 812})

        menu_toggle = await page.query_selector("#menu-toggle")
        assert menu_toggle is not None, "Menu toggle button not found"
        assert await menu_toggle.get_attribute("aria-expanded") == "false", "aria-expanded should be false initially"
        print("✅ Menu toggle aria-expanded is false initially")

        await menu_toggle.click()
        await page.wait_for_timeout(500) # Wait for sidebar

        assert await menu_toggle.get_attribute("aria-expanded") == "true", "aria-expanded should be true after click"
        print("✅ Menu toggle aria-expanded is true after opening")

        # Check focus shift
        focused_id = await page.evaluate("document.activeElement.id")
        assert focused_id == "close-sidebar", f"Focus should be on close-sidebar, but is on {focused_id}"
        print("✅ Focus correctly shifted to close-sidebar")

        close_button = await page.query_selector("#close-sidebar")
        await close_button.click()
        await page.wait_for_timeout(500)

        assert await menu_toggle.get_attribute("aria-expanded") == "false", "aria-expanded should be false after closing"
        print("✅ Menu toggle aria-expanded is false after closing")

        focused_id_after = await page.evaluate("document.activeElement.id")
        assert focused_id_after == "menu-toggle", f"Focus should return to menu-toggle, but is on {focused_id_after}"
        print("✅ Focus correctly returned to menu-toggle")

        await page.screenshot(path="verification/mobile_nav_verified.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
