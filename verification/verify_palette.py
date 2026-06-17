import asyncio
import os
from playwright.async_api import async_playwright

async def run_cuj():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        video_dir = os.path.abspath("verification/videos")
        os.makedirs(video_dir, exist_ok=True)
        os.makedirs("verification/screenshots", exist_ok=True)

        context = await browser.new_context(
            viewport={'width': 375, 'height': 667},
            record_video_dir=video_dir
        )
        page = await context.new_page()

        abs_path = os.path.abspath("index.html")
        await page.goto(f"file://{abs_path}")
        await page.wait_for_timeout(500)

        # 1. Open Sidebar
        print("Opening sidebar...")
        await page.click("#menuBtn")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="verification/screenshots/1_sidebar_open.png")

        # 2. Click a link (Menu) in the sidebar
        print("Clicking Menu link in sidebar...")
        await page.locator("#sidebarNav").get_by_role("link", name="Menu", exact=True).click()
        await page.wait_for_timeout(1000)
        await page.screenshot(path="verification/screenshots/2_after_nav.png")

        # 3. Open Sidebar again and close with Escape
        print("Opening sidebar and closing with Escape...")
        await page.click("#menuBtn")
        await page.wait_for_timeout(1000)
        await page.keyboard.press("Escape")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="verification/screenshots/3_after_escape.png")

        # 4. Tab to see focus visible
        print("Tabbing to see focus visible...")
        # Start tabbing from top
        await page.keyboard.press("Tab") # Logo
        await page.wait_for_timeout(500)
        await page.screenshot(path="verification/screenshots/4_focus_logo.png")

        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_cuj())
