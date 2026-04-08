# Palette's Journal - GourmetGarden UX & Accessibility

## 2025-01-24 - Enhancing Interactive Accessibility
**Learning:** Icon-only interactive elements (like mobile menu toggles and social links) are invisible to screen readers without ARIA labels. Additionally, keyboard users often lose track of their position when focus indicators are missing or low-contrast.
**Action:** Always provide `aria-label` for icon-only buttons and implement high-contrast `:focus-visible` styles using the brand's primary accent color. Ensure mobile menu states are communicated via `aria-expanded`.
