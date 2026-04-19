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

        # Simple visual regression check - ensure header logo is visible
        logo = await page.query_selector(".logo")
        assert logo is not None
        assert await logo.is_visible()
        print("✅ Header logo visible")

        # Ensure 'Book a Table' button is visible on desktop
        await page.set_viewport_size({"width": 1280, "height": 800})
        book_btn = await page.query_selector(".btn")
        assert await book_btn.is_visible()
        print("✅ Book a Table button visible on desktop")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
