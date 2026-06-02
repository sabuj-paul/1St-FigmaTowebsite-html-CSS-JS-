## 2025-05-14 - Sidebar Focus Management
**Learning:** Programmatic focus management in animated sidebars requires a small timeout (e.g., 100ms) to ensure the target element (like a close button) is interactive and that focus isn't swallowed by the transition itself.
**Action:** Always use a short setTimeout when shifting focus to elements within a container that is undergoing a CSS transition.
