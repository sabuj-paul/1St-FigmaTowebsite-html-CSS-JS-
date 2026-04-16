## 2024-12-16 - Initial UX & Accessibility Audit
**Learning:** Static landing pages often overlook semantic interactivity and smooth state transitions in mobile navigation. Using `display: none` for sidebars prevents smooth animations and can disrupt focus management.
**Action:** Replace `display: none` with `transform` and `visibility` for smooth transitions. Use semantic `<button>` elements with ARIA attributes for all interactive toggles.

## 2024-12-16 - Accessibility Baseline
**Learning:** Decorative icons and icon-only links (like social media) are common accessibility gaps. Decorative icons should be hidden from screen readers, and icon-only links need descriptive labels.
**Action:** Add `aria-hidden="true"` to decorative icons and `aria-label` to social links.
