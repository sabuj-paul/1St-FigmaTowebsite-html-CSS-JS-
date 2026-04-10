## 2024-05-20 - Semantic Mobile Navigation
**Learning:** In static HTML projects, mobile toggles often rely on non-semantic 'onclick' handlers on list items, which completely excludes keyboard and screen reader users. Transitioning to <button> elements with aria-expanded and aria-controls is the most efficient way to restore accessibility without external dependencies.
**Action:** Always refactor 'li' or 'a' toggles to semantic <button> elements and synchronize 'aria-expanded' states via the toggle script.
