## 2025-05-14 - Accessible Mobile Navigation Patterns
**Learning:** Replacing anchor-based menu toggles with semantic `<button>` elements and implementing programmatic focus management significantly improves keyboard and screen reader accessibility without changing the visual design.
**Action:** Use `<button type="button">` for all UI toggles, add `aria-expanded` and `aria-label`, and ensure focus is explicitly moved to the first interactive element in a modal/sidebar and returned to the trigger upon closing.
