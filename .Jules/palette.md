## 2025-05-15 - Sidebar Focus Management and ARIA Synchronization
**Learning:** For mobile navigation sidebars, replacing anchor tags with semantic <button> elements and synchronizing 'aria-expanded' with programmatic focus management (e.g., using a short setTimeout to wait for CSS transitions) significantly improves screen reader and keyboard navigation reliability.
**Action:** Always use <button> for navigation triggers, manage 'aria-expanded', and explicitly return focus to the trigger element when the sidebar is closed.

## 2025-05-16 - Differentiating Explicit vs. Navigation-Triggered Menu Dismissal Focus
**Learning:** Returning focus to the menu toggle button when closing a mobile drawer via a navigation link causes focus jumps that disrupt smooth anchor scrolling and confuse screen reader users. Explicit dismissal (Close button or Escape key) should restore focus to the trigger, whereas internal navigation closure should dismiss the overlay without forcing focus return.
**Action:** Pass a boolean flag to `hideSidebar(shouldFocusToggle)` so explicit closures restore focus while navigation link selections allow standard anchor scroll focus flow.
