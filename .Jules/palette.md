## 2024-05-24 - Semantic Navigation & Focus Management
**Learning:** Replacing non-semantic list-item/anchor triggers with <button> elements improves accessibility, but requires CSS resets to maintain visual consistency. Programmatic focus management (moving focus to close button on open, returning to toggle on close) is essential for a smooth screen reader experience in off-screen sidebars.
**Action:** Use <button> for all interactive triggers. Implement aria-expanded/aria-controls and synchronize with JS focus() calls (with a short timeout for transition-heavy elements).
