
import asyncio
import os
from playwright.async_api import async_playwright

async def verify_ux():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 375, 'height': 667})
        page = await context.new_page()

        # Load the local index.html file
        file_path = "file://" + os.path.abspath("index.html")
        await page.goto(file_path)

        # 1. Verify ARIA labels on mobile menu buttons
        menu_btn = page.locator("#menuBtn")
        aria_label = await menu_btn.get_attribute("aria-label")
        print(f"Menu Button ARIA label: {aria_label}")
        assert aria_label == "Open menu"

        # 2. Test Sidebar Opening and Focus
        await menu_btn.click()
        await page.wait_for_timeout(500) # Wait for transition

        close_btn = page.locator("#closeBtn")
        is_visible = await close_btn.is_visible()
        print(f"Close Button visible: {is_visible}")

        focused_id = await page.evaluate("document.activeElement.id")
        print(f"Focused element ID after open: {focused_id}")
        assert focused_id == "closeBtn"

        await page.screenshot(path="verification/screenshots/sidebar_open.png")

        # 3. Test Sidebar Closing and Focus Return
        await close_btn.click()
        await page.wait_for_timeout(500)

        focused_id = await page.evaluate("document.activeElement.id")
        print(f"Focused element ID after close: {focused_id}")
        assert focused_id == "menuBtn"

        # 4. Test Navigation Links
        # Open again
        await menu_btn.click()
        await page.wait_for_timeout(500)

        # Click "About Us" link in sidebar
        about_link = page.locator(".sidebar a[href='#about-us']")
        await about_link.click()
        await page.wait_for_timeout(500)

        # Sidebar should be hidden
        sidebar_display = await page.evaluate("document.querySelector('.sidebar').style.display")
        print(f"Sidebar display after nav: {sidebar_display}")
        assert sidebar_display == "none"

        # Verify URL hash
        url = page.url
        print(f"Current URL: {url}")
        assert "#about-us" in url

        # 5. Verify Footer Social Links ARIA labels
        facebook_link = page.locator(".social-links a[aria-label='Facebook']")
        assert await facebook_link.count() == 1
        print("Footer social links ARIA labels verified.")

        # 6. Verify Focus Visible Styles
        # Go to top
        await page.goto(file_path)
        # Tab to the logo or first link
        await page.keyboard.press("Tab") # Skip link or logo
        await page.keyboard.press("Tab") # Next link
        await page.wait_for_timeout(100)
        await page.screenshot(path="verification/screenshots/focus_visible_nav.png")

        # Tab to "Explore Menu" button
        # It's inside .about-info
        await page.focus(".btn-ctn")
        await page.keyboard.press("Tab") # This might move focus to next element, but let's try to focus it via keyboard
        # Reset and tab many times
        await page.goto(file_path)
        for _ in range(5):
            await page.keyboard.press("Tab")
            await page.wait_for_timeout(50)

        await page.screenshot(path="verification/screenshots/focus_visible_cycle.png")
        print("Focus visible screenshots captured.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_ux())
