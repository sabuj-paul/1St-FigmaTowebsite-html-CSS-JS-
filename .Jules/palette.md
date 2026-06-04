## 2025-01-24 - Context-Aware Sidebar Focus Management
**Learning:** Returning focus to the trigger button is standard for closing a sidebar, but yanking focus back to the top of the page when a user clicks an internal navigation link is disorienting. Focus should stay within the target section in those cases.
**Action:** Use a conditional flag in sidebar toggle functions to distinguish between explicit "Close" actions (return focus) and "Navigate" actions (allow focus to move to the new section).
