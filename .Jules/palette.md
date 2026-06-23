# Palette's Journal

## 2025-05-15 - Sidebar Accessibility and Transition Patterns
**Learning:** When using CSS transitions for sidebars (e.g., `transform: translateX(100%)`), it is crucial to also use `visibility: hidden` in the inactive state. This prevents keyboard users from accidentally tabbing into interactive elements within the hidden sidebar. Additionally, focus management using `setTimeout` (matching the transition duration) ensures that focus shifts occur after the element is visually present and stable.
**Action:** Always pair `transform` with `visibility` for off-screen menus, and use a 300ms delay for programmatic focus shifts to match the transition-ease.
