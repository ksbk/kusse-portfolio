# Fast Accessibility and Semantic Checklist

Use this quick checklist before opening a PR or when reviewing user-facing templates and CSS.

## Core checklist

- Page structure:
  confirm clear structural landmarks (header, nav, main, footer) where appropriate.
- One clear h1:
  confirm a single primary page heading.
- Headings and labels:
  confirm heading order is logical and labels are clear for grouped content.
- Link purpose:
  confirm link text is understandable in context, especially when repeated.
- Icon-only links:
  confirm icon-only controls have accessible names.
- Keyboard navigation:
  confirm all key interactions are reachable by keyboard.
- Visible focus:
  confirm focus remains visible. Browser-default focus is acceptable if clearly visible.
- Skip link:
  confirm skip link exists, is keyboard reachable, and targets main content.
- Touch targets:
  confirm interactive items are usable on mobile widths.
- Reading order:
  confirm keyboard/screen-reader order matches intended reading sequence.
- Color and contrast:
  confirm text and focus indicators are perceivable; do not rely on color alone.
- Reduced motion:
  confirm motion respects reduced-motion settings where motion exists.
- External link behavior:
  confirm behavior is consistent. Do not require `target="_blank"` by default.
- No scope creep:
  limit review and fixes to approved accessibility/semantic scope.

## Fast local checks

Run quality checks:

```bash
make quality
```

Manual verification checks:

- Keyboard tab-through from top of page.
- Skip-link activation and main-content jump.
- 375px mobile viewport review.
- 200% zoom review.
- No horizontal overflow review.
- Project index/detail page review where applicable.

## Review chain

Use this sequence for every finding:

1. Standard
2. Repository comparison
3. Gap (or risk)
4. Affected file
5. Issue mapping
6. Smallest approved fix

## Out-of-scope reminders

- Do not treat stretched-card links as a default recommendation.
- Do not require `target="_blank"`.
- Do not require custom focus styling when browser focus is already visible.
- Do not add automated axe, Lighthouse, Playwright, or CI setup in this checklist task.
- Do not implement sprint fixes from this checklist alone.
