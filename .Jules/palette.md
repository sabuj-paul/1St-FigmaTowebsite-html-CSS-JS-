## 2025-01-24 - Focus Visibility & SVG Hygiene
**Learning:** Providing explicit `:focus-visible` styles using the brand's primary color (`--deepgold`) significantly improves keyboard navigation without impacting the visual design for mouse users. Also, non-standard SVG attributes like `length` (instead of `height`) can cause rendering issues and should be replaced with standard ones.
**Action:** Always check icon-only interactive elements for ARIA labels and ensure a custom focus indicator is present that matches the design system.
