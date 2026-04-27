## 2024-05-24 - Accessible and Smooth Mobile Navigation
**Learning:** Transitioning UI overlays like sidebars with `display: none` creates jarring UX and breaks accessibility. Using `visibility` and `transform` allows for smooth CSS animations while correctly hiding content from screen readers and maintaining the focusable state only when visible.
**Action:** Always prefer `visibility` and `transform` for sidebar animations and implement explicit focus management (using `setTimeout` to wait for transitions) when opening and closing overlays.
