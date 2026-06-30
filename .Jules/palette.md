## 2025-06-30 - Focus Management for Mobile Sidebars
**Learning:** In simple static sites, mobile menus often use anchor tags for toggles. Converting these to semantic `<button>` elements with `aria-expanded` and programmatic focus management (focusing the close button on open, returning focus to the trigger on close) significantly improves the experience for keyboard and screen reader users. Using a small `setTimeout` (100ms) for the focus shift ensures the transition has begun and the element is ready to receive focus.

**Action:** Always refactor `<a>` based toggles to `<button type="button">` and implement the `show/hide` focus return pattern.
