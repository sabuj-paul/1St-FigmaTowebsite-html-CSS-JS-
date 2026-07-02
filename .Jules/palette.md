## 2025-05-14 - Navigation & Focus Accessibility
**Learning:** Icon-only toggles (hamburger/close) and social links without labels are major blockers for screen readers. Using `:focus-visible` instead of `:focus` avoids unwanted outlines for mouse users while providing clarity for keyboard users.
**Action:** Always include `aria-label` for icons and use `:focus-visible` for global focus states using brand colors.
