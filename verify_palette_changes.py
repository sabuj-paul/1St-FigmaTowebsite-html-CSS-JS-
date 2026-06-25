import asyncio
from playwright.async_api import async_playwright
import os

async def verify_ux():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 375, 'height': 667}) # Mobile viewport
        page = await context.new_page()

        file_path = "file://" + os.path.abspath("index.html")
        await page.goto(file_path)

        print("Checking initial state...")
        menu_btn = page.locator("#menuBtn")
        await menu_btn.wait_for(state="visible")

        aria_label = await menu_btn.get_attribute("aria-label")
        aria_expanded = await menu_btn.get_attribute("aria-expanded")
        print(f"Menu button aria-label: {aria_label}, aria-expanded: {aria_expanded}")
        assert aria_label == "Open menu"
        assert aria_expanded == "false"

        # Capture initial state
        os.makedirs("verification/screenshots", exist_ok=True)
        await page.screenshot(path="verification/screenshots/initial_mobile.png")

        print("Testing sidebar open...")
        await menu_btn.click()

        sidebar = page.locator(".sidebar")
        await sidebar.wait_for(state="visible")

        aria_expanded_after = await menu_btn.get_attribute("aria-expanded")
        print(f"Menu button aria-expanded after click: {aria_expanded_after}")
        assert aria_expanded_after == "true"

        # Check focus management
        await page.wait_for_timeout(500) # Wait for setTimeout in script
        focused_id = await page.evaluate("document.activeElement.id")
        print(f"Focused element ID after opening: {focused_id}")
        assert focused_id == "closeBtn"

        await page.screenshot(path="verification/screenshots/sidebar_open.png")

        print("Testing sidebar close (via button)...")
        close_btn = page.locator("#closeBtn")
        await close_btn.click()

        await sidebar.wait_for(state="hidden")
        aria_expanded_closed = await menu_btn.get_attribute("aria-expanded")
        print(f"Menu button aria-expanded after close: {aria_expanded_closed}")
        assert aria_expanded_closed == "false"

        await page.wait_for_timeout(500) # Wait for setTimeout in script
        focused_id_closed = await page.evaluate("document.activeElement.id")
        print(f"Focused element ID after closing: {focused_id_closed}")
        assert focused_id_closed == "menuBtn"

        print("Testing Escape key closing...")
        await menu_btn.click()
        await sidebar.wait_for(state="visible")
        await page.keyboard.press("Escape")
        await sidebar.wait_for(state="hidden")
        print("Sidebar closed with Escape key successfully")

        print("Checking footer accessibility...")
        facebook_link = page.locator('a[aria-label="Facebook"]')
        instagram_link = page.locator('a[aria-label="Instagram"]')
        twitter_link = page.locator('a[aria-label="Twitter"]')

        assert await facebook_link.is_visible()
        assert await instagram_link.is_visible()
        assert await twitter_link.is_visible()
        print("Footer social links have correct aria-labels.")

        print("Checking focus-visible styles...")
        # Move focus via Tab to see if it works (even if we can't easily assert CSS in playwright, we can try to trigger it)
        await page.keyboard.press("Tab")
        await page.screenshot(path="verification/screenshots/focus_visible_test.png")

        await browser.close()
        print("Verification complete!")

if __name__ == "__main__":
    asyncio.run(verify_ux())
