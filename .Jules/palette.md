## 2025-05-15 - Sidebar Focus Management and ARIA Synchronization
**Learning:** For mobile navigation sidebars, replacing anchor tags with semantic <button> elements and synchronizing 'aria-expanded' with programmatic focus management (e.g., using a short setTimeout to wait for CSS transitions) significantly improves screen reader and keyboard navigation reliability.
**Action:** Always use <button> for navigation triggers, manage 'aria-expanded', and explicitly return focus to the trigger element when the sidebar is closed.
