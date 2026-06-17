## 2025-01-24 - [Mobile Sidebar Focus Management]
**Learning:** Returning focus to the menu trigger button when the sidebar is explicitly closed (via 'Close' button or Escape key) is essential for keyboard navigation continuity. However, if the sidebar closes because the user navigated to a section, returning focus to the trigger can be counter-productive as the user's intent was to move to new content.
**Action:** Use a parameter in the close function (e.g., `hideSidebar(returnFocus)`) to distinguish between explicit cancellation and navigation-triggered closure.
