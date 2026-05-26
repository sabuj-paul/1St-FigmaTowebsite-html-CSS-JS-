## 2024-05-26 - Mobile Sidebar Focus Management
**Learning:** Programmatic focus management in animated mobile sidebars requires small delays (100ms-300ms) to ensure the target element is visible and interactive before focusing, and to prevent focus from being lost during transition or anchor navigation.
**Action:** Always use setTimeout for focus shifts in sidebars with transitions, and prioritize focus return to the trigger element on close.
