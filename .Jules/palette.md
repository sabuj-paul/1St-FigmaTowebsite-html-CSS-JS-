## 2024-05-19 - Focus Management in Static Navigation
**Learning:** In static HTML pages using anchor links for internal navigation within a mobile sidebar, programmatic focus return (e.g., returning focus to the menu button upon closing) often requires a short delay (100ms) to ensure the browser has finished processing the navigation and potential body-focus reset.
**Action:** Use `setTimeout(() => { element.focus(); }, 100);` when returning focus to a trigger element after sidebar closure on mobile.

## 2024-05-19 - ARIA State Sync for Custom Components
**Learning:** Custom UI components like sidebars built with CSS display/visibility must have their accessibility state (`aria-expanded`) manually synchronized via JavaScript to ensure screen readers accurately reflect the interface state.
**Action:** Always update the `aria-expanded` attribute on the trigger element within the show/hide functions.
