import os
import asyncio
from playwright.async_api import async_playwright

async def verify_navigation():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={'width': 375, 'height': 667},
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/04.1'
        )
        page = await context.new_page()

        file_path = "file://" + os.path.abspath("index.html")
        await page.goto(file_path)

        # 1. Verify Menu Toggle exists and is accessible
        menu_toggle = page.locator("#menu-toggle")
        await menu_toggle.wait_for()
        assert await menu_toggle.get_attribute("aria-label") == "Open menu"
        assert await menu_toggle.get_attribute("aria-expanded") == "false"

        # 2. Open Sidebar and verify state
        await menu_toggle.click()
        await page.wait_for_timeout(500) # Wait for animation/focus shift

        assert await menu_toggle.get_attribute("aria-expanded") == "true"
        sidebar = page.locator("#sidebar-nav")
        assert await sidebar.is_visible()

        # 3. Verify Focus management (Focus should be on close button)
        close_button = page.locator("#close-sidebar")
        is_focused = await close_button.evaluate("el => document.activeElement === el")
        print(f"Close button focused after open: {is_focused}")
        assert is_focused
        assert await close_button.get_attribute("aria-label") == "Close menu"

        # 4. Close Sidebar and verify focus return
        await close_button.click()
        await page.wait_for_timeout(500)

        assert await menu_toggle.get_attribute("aria-expanded") == "false"
        is_toggle_focused = await menu_toggle.evaluate("el => document.activeElement === el")
        print(f"Menu toggle focused after close: {is_toggle_focused}")
        assert is_toggle_focused

        # 5. Verify ARIA hidden on icons
        icons = await page.locator("i.fa-solid, svg").all()
        for icon in icons:
            aria_hidden = await icon.get_attribute("aria-hidden")
            # Some SVGs might not have it if they are not the ones we touched,
            # but our main ones should.
            if await icon.get_attribute("xmlns") == "http://www.w3.org/2000/svg":
                 assert aria_hidden == "true"

        # Capture screenshot
        await menu_toggle.click()
        await page.wait_for_timeout(500)
        await page.screenshot(path="verification/sidebar_open_mobile.png")
        print("Verification successful and screenshot captured.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_navigation())
