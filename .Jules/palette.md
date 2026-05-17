## 2024-05-22 - Improved Mobile Sidebar Accessibility
**Learning:** Using `aria-expanded` on the trigger and `aria-hidden` on the sidebar provides clear semantic signals to screen readers about the menu's state. Programmatic focus management (returning focus to the trigger on close) ensures a smooth experience for keyboard-only users.
**Action:** Always include ARIA state management and focus return when implementing modal-like overlays or mobile navigation drawers.
