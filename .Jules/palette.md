# Palette Journal - GourmetGarden

## 2024-04-07 - Semantic Buttons for Sidebar Toggles
**Learning:** In static HTML/JS projects, mobile sidebar toggles often use `<a>` tags with inline `onclick` handlers. This creates an inaccessible interaction for screen readers (missing role) and keyboard users (no focus/activation parity unless explicitly handled). Replacing them with semantic `<button>` elements with `aria-label` and `aria-expanded` provides the necessary state communication and standard accessibility behaviors automatically.
**Action:** Always convert generic `<a>` or `<li>` toggles to semantic `<button>` elements and use `aria-expanded` for state tracking in future projects.
