## 2024-04-09 - Navigation Accessibility & Focus States
**Learning:** Using non-semantic elements with `onclick` handlers for navigation toggles prevents keyboard users from accessing core site features. Additionally, decorative icons without `aria-hidden` create unnecessary noise for screen readers.
**Action:** Always refactor icon-only toggles to use `<button>` elements with `aria-label`, and synchronize `aria-expanded` states in JavaScript. Apply `:focus-visible` styles using the primary accent color (`--deepgold`) to provide high-contrast feedback without affecting mouse users.
