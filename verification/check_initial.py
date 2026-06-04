import asyncio
import os
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        # Use absolute path for file:// URL
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        # Take screenshot of the whole page
        await page.screenshot(path="verification/initial_desktop.png", full_page=True)

        # Test mobile view
        await page.set_viewport_size({"width": 375, "height": 667})
        await page.screenshot(path="verification/initial_mobile.png")

        # Open sidebar
        await page.click(".menu-button")
        await asyncio.sleep(0.5) # Wait for any transition
        await page.screenshot(path="verification/initial_sidebar.png")

        await browser.close()

if __name__ == "__main__":
    os.makedirs("verification", exist_ok=True)
    asyncio.run(run())
