## 2025-05-15 - [Accessible Mobile Sidebar Pattern]
**Learning:** In projects without a framework, programmatic focus management (using IDs and setTimeout) is essential for screen reader users to discover mobile menu content. Additionally, using semantic <button> elements instead of <a> for toggles prevents default jump behaviors and provides correct role identification.

**Action:** Always implement a focus trap or at least move focus to the first interactive element when opening overlays, and return focus to the trigger upon closing.
