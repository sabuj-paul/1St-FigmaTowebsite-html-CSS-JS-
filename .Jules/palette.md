## 2025-05-15 - [Enhance Sidebar and Social Links Accessibility]
**Learning:** Interactive icon-only elements (like mobile menu toggles and social links) in this repository were initially implemented using non-semantic `<li>` and `<a>` tags with `onclick` handlers, which are not keyboard-accessible or screen-reader friendly.
**Action:** Always replace anchor-based or list-item-based toggles with semantic `<button>` elements, add `aria-label` for icon-only components, and manage `aria-expanded` state for toggles to ensure proper accessibility.
