## 2024-04-23 - Accessible Mobile Navigation Patterns
**Learning:** Transitioning from `li` with `onclick` to semantic `<button>` elements significantly improves keyboard accessibility, but requires a CSS reset to maintain the original design. Programmatic focus management (shifting focus to the close button on open and back to the toggle on close) is essential for a seamless screen reader and keyboard user experience.
**Action:** Always use semantic buttons for navigation toggles and implement focus management when toggling UI overlays like sidebars or modals.
