const playwright = require('playwright');

(async () => {
  const browser = await playwright.chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto('file://' + process.cwd() + '/index.html');
  await page.setViewportSize({ width: 1280, height: 2500 }); // Larger height to capture footer
  await page.screenshot({ path: 'verification/restaurant_home_v2.png', fullPage: true });
  await browser.close();
})();
