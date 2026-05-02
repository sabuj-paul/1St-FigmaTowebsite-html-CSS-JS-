## 2024-05-24 - Semantic Sidebar and Focus Management
**Learning:** Replacing anchor-based navigation triggers with semantic `<button>` elements and programmatically managing focus (moving to close button on open, returning to toggle on close) significantly improves the experience for screen reader and keyboard users in a static site.
**Action:** Always use `<button>` for UI triggers that don't navigate to a new URL, and ensure focus is shifted to the most relevant element during state transitions.
