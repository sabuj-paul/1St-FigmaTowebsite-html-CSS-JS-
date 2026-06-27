## 2024-05-15 - [Semantic Buttons for Actions]
**Learning:** Using generic anchors (`<a>`) for UI actions like opening/closing sidebars causes accessibility friction and requires hacks (like `return false;`) to prevent jumping. Semantic `<button>` elements are the correct pattern but require explicit CSS resets to match existing navigation styles in legacy codebases.
**Action:** Always prefer `<button type="button">` for UI triggers and ensure the design system/CSS includes a reset for these elements within navigation components.
