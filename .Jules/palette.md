## 2025-01-24 - Accessible Animated Sidebars
**Learning:** Using `visibility: hidden` combined with `right: -250px` (or transform) instead of `display: none` allows for smooth CSS transitions while ensuring that links within the hidden sidebar are not focusable by keyboard users.
**Action:** Always prefer `visibility` + `position/transform` for off-screen navigation menus to balance animation polish with accessibility.

## 2025-01-24 - Focus Management in Overlays
**Learning:** Programmatically shifting focus to a close button when an overlay opens, and returning it to the trigger when it closes, is a critical "invisible" UX win for keyboard and screen reader users.
**Action:** Implement `element.focus()` in sidebar/modal toggle functions, using a small `setTimeout` if transitions are involved.
