## 2025-05-14 - Context-Aware Focus Management in Mobile Sidebars
**Learning:** In SPAs or landing pages with mobile sidebars, focus should only be returned to the trigger (menu button) upon explicit closure (Close button or Escape); for navigation-triggered closure, forced focus return should be avoided to prevent 'focus jumps' that confuse users.
**Action:** Implement a conditional `returnFocus` parameter in sidebar toggle functions to differentiate between explicit and implicit (navigation) closure.
