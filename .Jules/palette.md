## 2025-05-15 - [Mobile Navigation & Accessibility Refactor]
**Learning:** Using `display: none` for mobile sidebars prevents smooth CSS transitions and can cause focus management issues. Switching to `transform: translateX(100%)` and `visibility: hidden` allows for fluid animations while correctly removing the element from the accessibility tree when closed.
**Action:** Always prefer `transform` and `visibility` for slide-in components. Ensure all icon-only toggles are semantic `<button>` elements with `aria-expanded` and `aria-label`.
