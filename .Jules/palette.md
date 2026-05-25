## 2025-05-14 - Visual Focus Verification in Playwright
**Learning:** Playwright's `locator.click()` often simulates a mouse click which does not trigger `:focus-visible` CSS styles, making it difficult to verify focus indicators in automated screenshots.
**Action:** Use `page.keyboard.press("Tab")` or explicit `element.focus()` in combination with keyboard-like interactions when verifying visual focus indicators in Playwright.
