## 2024-05-22 - Focus Management in Single Page Navigation
**Learning:** In the GourmetGarden landing page, clicking an internal navigation link within the mobile sidebar can cause the focus to reset to the document body, potentially overriding programmatic focus-return calls (like `menuBtn.focus()`) in the `hideSidebar` function due to default link behavior and page scroll.
**Action:** Always verify focus state after navigation transitions and ensure `aria-expanded` states are synchronized even if the element that triggered the transition is no longer in the immediate viewport.
