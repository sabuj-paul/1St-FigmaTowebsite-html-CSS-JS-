## 2025-01-24 - Navigation Accessibility and Semantic Triggers
**Learning:** Replacing non-semantic click targets (like `<li>` or `<a>` with `href="#"`) with proper `<button>` elements significantly improves the accessibility and predictability of navigation controls. Managing `aria-expanded` and programmatic focus transitions ensures a seamless experience for keyboard and screen reader users.
**Action:** Use semantic `<button>` elements for all UI triggers, manage ARIA states programmatically, and ensure focus returns to the initiating element upon closing overlays.
