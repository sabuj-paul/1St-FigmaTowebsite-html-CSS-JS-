## 2024-05-24 - Accessible Mobile Navigation Refactor
**Learning:** Transitioning from `display: none` to `transform` and `visibility` for sidebars allows for smooth animations while maintaining accessibility. Programmatic focus management (moving focus to the close button on open and returning to the trigger on close) is essential for screen reader users and keyboard navigators.
**Action:** Always use `transform` and `visibility` for UI overlays, and ensure interactive toggles are semantic `<button>` elements with correct ARIA states and focus handling.
