## 2025-06-06 - Mobile Sidebar Focus Management & Anchor Behavior
**Learning:** In animated or 'display: none/flex' sidebars, programmatic focus management requires careful timing to ensure the target element is visible and interactive. Using `<a>` elements as accessible buttons for closing overlays requires preventing the default anchor behavior (scrolling to top with `href="#"`) to avoid UX regressions.

**Action:** Always include `return false;` or `event.preventDefault()` on decorative/functional anchors and use modest delays (100-150ms) for focus shifts to balance accessibility and responsiveness.
