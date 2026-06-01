## 2025-05-14 - Mobile Sidebar Accessibility and Focus Management
**Learning:** Transitioning sidebars off-screen requires setting `visibility: hidden` when inactive to prevent screen readers and keyboard users from interacting with hidden links. Additionally, programmatic focus management (moving focus to the close button on open and returning to the trigger on close) is essential for a seamless keyboard experience.
**Action:** Always pair CSS transforms/transitions for sidebars with visibility toggles and JavaScript focus management to ensure full accessibility.
