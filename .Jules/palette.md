## 2025-01-24 - Semantic Navigation and Focus Management
**Learning:** Replacing non-semantic anchor-based toggles with <button> elements and implementing explicit focus management significantly improves keyboard and screen reader accessibility for mobile navigation. Using CSS transform/visibility instead of display: none enables smooth animations without compromising accessibility states.
**Action:** Always use <button> for UI toggles, manage aria-expanded state, and programmatically handle focus when opening/closing overlays.
