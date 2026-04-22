## 2024-12-30 - [Enhanced Mobile Sidebar Accessibility]
**Learning:** Programmatic focus management (e.g., shifting focus to a close button when opening an overlay) requires a short delay (e.g., 100ms) to ensure the target element is visible and capable of receiving focus during CSS transitions.
**Action:** Always use `setTimeout` when shifting focus to elements appearing via transitions.
