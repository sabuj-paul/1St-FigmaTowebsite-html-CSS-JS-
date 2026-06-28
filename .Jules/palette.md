## 2025-05-15 - Focus Trap vs. Focus Management
**Learning:** For mobile sidebars, full focus traps can be complex and exceed micro-UX line limits (<50 lines). Efficient focus management—shifting focus to the close button on open and returning it to the trigger on close—provides 90% of the accessibility benefit with much less code.
**Action:** Prioritize programmatic focus shift to the primary close action and focus return to the toggle for all modal-like UI components.

## 2025-05-15 - Anchor Navigation IDs
**Learning:** When updating navigation links to use descriptive anchors (e.g., #menu, #about), ensuring the corresponding IDs exist in the DOM is critical for functional correctness.
**Action:** Always verify that every internal navigation target has a matching ID in the HTML before submitting navigation changes.
