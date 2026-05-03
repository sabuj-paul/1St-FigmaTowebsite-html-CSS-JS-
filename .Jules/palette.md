## 2024-05-03 - [Mobile Navigation Accessibility and Focus Management]
**Learning:** In static HTML/JS projects, mobile sidebars often lack semantic triggers and focus management. Using `<button>` elements instead of `<a>` tags for toggles, combined with explicit focus shifting (e.g., via `setTimeout` to account for transitions), significantly improves the experience for keyboard and screen reader users.
**Action:** Always replace icon-only anchor toggles with semantic buttons and implement focus loops for overlays.
