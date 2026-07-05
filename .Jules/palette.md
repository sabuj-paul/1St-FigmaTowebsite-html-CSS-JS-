## 2025-05-14 - Mobile Menu Accessibility and Focus Management
**Learning:** Transitioning from anchor-based toggles to semantic buttons significantly improves screen reader clarity, but requires explicit focus management to maintain a fluid keyboard experience. Programmatic focus shifts (using a slight delay to account for visibility/animations) ensure the user is immediately placed in the correct context when a modal-like sidebar opens.
**Action:** Always use <button> for UI toggles, assign clear IDs, and implement focus-return logic to the trigger element when the overlay is closed.
