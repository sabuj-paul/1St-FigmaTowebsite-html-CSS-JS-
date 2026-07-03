## 2025-05-14 - [Mobile Navigation Focus Management]
**Learning:** For mobile sidebars, semantic buttons and programmatic focus management are crucial for accessibility. Returning focus to the trigger on close and moving it to the close button on open ensures a seamless keyboard/screen reader flow.
**Action:** Always use `<button type="button">` for toggles and implement `element.focus()` with a slight delay if transitions are involved.
