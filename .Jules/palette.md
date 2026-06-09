## 2025-05-14 - [Mobile Sidebar Focus Management]
**Learning:** Returning focus to the trigger button is essential when closing a mobile sidebar via the close button or Escape key. However, if the sidebar closes because the user clicked a navigation link, returning focus to the trigger can be disruptive and may compete with the browser's default behavior of scrolling to the target section.
**Action:** Use a `returnFocus` boolean parameter in the sidebar close function. Set it to `true` for explicit cancellations (Close button, Escape key) and `false` for internal navigation links.
