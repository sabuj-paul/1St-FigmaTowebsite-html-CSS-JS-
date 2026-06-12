## 2024-06-12 - Focus Management in Mobile Sidebars
**Learning:** In static websites with mobile sidebars, simply toggling visibility (display: none/flex) isn't enough for keyboard accessibility. Shifting focus to the close button when opening and returning focus to the trigger when closing (using a small timeout to account for transitions) provides a much smoother experience for screen reader and keyboard-only users.
**Action:** Always implement programmatic focus management for modal-like components (sidebars, dialogs) and include an Escape key listener.
