## 2026-06-15 - Focus Management in Animated Sidebars
**Learning:** In projects with CSS transitions or `display: flex/none` toggles, programmatically shifting focus (e.g., to a Close button or back to a Trigger) often fails if executed immediately because the element might not be fully interactive or the browser's focus ring might not render correctly during the animation.
**Action:** Use a short `setTimeout` (e.g., 300ms) to delay the `.focus()` call, ensuring it happens after the transition has begun or completed.
