## 2025-05-14 - Selective Focus Return on Sidebar Close
**Learning:** When closing a mobile sidebar after a navigation event, returning focus to the original trigger button can be disorienting or overridden by the browser's default anchor scrolling. It is better to only return focus to the trigger when the user explicitly cancels/closes the menu without navigating.
**Action:** Implement 'hide' functions with a 'returnFocus' boolean parameter and use 'setTimeout' (approx 300ms) to ensure focus shifts occur after transitions are complete.
