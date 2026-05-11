## 2026-05-11 - Accessible Mobile Sidebar Pattern
**Learning:** In static restaurant sites with off-canvas menus, using 'display: none' for hiding sidebars prevents smooth transitions, while 'transform' alone keeps links in the tab order. Combining 'transform', 'visibility', and 'aria-expanded' provides the best balance of performance and accessibility.
**Action:** Always use 'visibility: hidden' with 'transform' for sidebars, and implement manual focus trapping by shifting focus to the close button upon opening.
