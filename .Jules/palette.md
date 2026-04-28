## 2024-05-15 - Accessible Sidebar Navigation Pattern
**Learning:** Using 'display: none' for sidebars prevents smooth transitions and can cause issues with focus management if not handled carefully. Combining 'transform: translateX(100%)' with 'visibility: hidden' allows for CSS transitions while ensuring the sidebar is hidden from both visual and assistive technologies when closed.
**Action:** Use transform and visibility for sidebars. Always implement focus management (trap focus or shift focus to close button) and return focus to the trigger upon closing.

## 2024-05-15 - Semantic Navigation Toggles
**Learning:** Anchor tags (<a>) with 'href="#"' used as buttons are confusing for screen readers and lack semantic clarity.
**Action:** Use semantic <button> elements with 'aria-label' and 'aria-expanded' for interactive UI toggles, even if they are nested within list items for layout purposes.
