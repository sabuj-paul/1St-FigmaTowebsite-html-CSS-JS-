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
        await page.set_viewport_size({"width": 375, "height": 812})

        await page.click("#menu-toggle")
        await page.wait_for_timeout(500)

        await page.screenshot(path="verification/mobile_sidebar_open.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
