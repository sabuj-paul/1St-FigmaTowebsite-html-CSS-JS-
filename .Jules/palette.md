## 2025-05-14 - Accessible Sidebar Focus Management
**Learning:** For static sites using 'display: none' to show/hide sidebars, a short delay (e.g., 100ms) is necessary before programmatically focusing elements within the sidebar to ensure the browser has completed the layout change.
**Action:** Always return focus to the trigger element when closing an overlay and use a small timeout when focusing elements in a newly opened overlay.
