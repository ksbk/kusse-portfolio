# Accessibility and Semantic Hardening Audit Workflow

## Purpose

This workflow defines a repeatable manual audit process for reviewing user-facing templates and CSS against accessibility and semantic HTML best practices before making code changes.

Use this audit to compare current implementation patterns with expected best practices, identify concrete risks, and scope follow-up fixes without prematurely editing files.

## When to use this audit

Run this audit:

- Before an accessibility hardening sprint.
- Before changing shared templates.
- Before release or reviewer checks.
- After major layout or template changes.

## Audit scope

Primary audit surface:

- `templates/base.html`
- `apps/pages/templates/pages/*.html`
- `apps/projects/templates/projects/*.html`
- `static/css/base.css`
- `static/css/layout.css`
- `static/css/components.css`
- `static/css/main.css`

Secondary surface:

- Tests only when rendering behavior needs regression coverage.

## Review principles

- Audit before editing.
- Compare current implementation against best practices.
- Identify the exact file and exact code pattern for each finding.
- Classify each finding with a clear severity level.
- Map each finding to a current issue or future issue.
- Keep fixes small and targeted.
- Avoid scope creep.
- Do not claim WCAG failures unless clearly justified by evidence.
- Prefer the term "risk" when context or interpretation matters.

## Checklist

Review each area explicitly:

- Landmarks:
	header, nav, main, footer presence and clarity.
- Skip link:
	keyboard reachability, visible reveal, and valid target.
- Heading hierarchy:
	one clear h1 per page and logical h2/h3 progression.
- Link purpose:
	repeated link text is understandable in context.
- Labels and list semantics:
	labels are associated clearly with grouped items.
- Keyboard focus:
	visible focus states for nav, buttons, and normal links.
- Touch targets:
	nav/footer/action links are usable at narrow widths.
- Color contrast risks:
	muted text, focus indicators, and state contrast.
- Article/section/div appropriateness:
	semantic element choice matches content intent.
- Empty states:
	empty content remains understandable and not over-semantic.
- Progressive enhancement:
	page remains usable without JavaScript.
- Reduced motion:
	motion behavior respects reduced-motion preference.
- External link behavior:
	consistent policy and no unnecessary `target="_blank"`.

## Finding classification

- High:
	Blocks understanding or keyboard/screen-reader use.
- Medium:
	Creates ambiguity or weak semantics.
- Low:
	Polish, consistency, or future hardening opportunity.
- Defer:
	Valid item but outside current sprint scope.
- No change:
	Current implementation is acceptable.

## Output format

Use this reusable findings table:

| ID | Area | File | Current implementation | Gap / risk | Severity | Recommendation | Issue mapping | Fix now or defer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A11Y-001 | Example area | path/to/file | Brief fact | Brief risk statement | Medium | Small, concrete next step | KP-XXXX / Backlog | Fix now |

## Issue mapping rules

Map each finding as follows:

- Map direct, in-scope findings to the active sprint issue that best matches the problem.
- If no active issue matches, map to future backlog with a concise issue proposal title.
- Do not split a single semantic problem across multiple issues unless files are independently actionable.
- Keep issue mapping narrow enough to keep each issue small and reviewable.

Sprint 8 mapping reference:

- `KP-8002 - Improve project evidence-list semantics`
- `KP-8003 - Harden skip link and nav touch targets`
- `KP-8004 - Remove redundant project detail heading`
- `KP-8005 - Final accessibility verification`

## Deferred / do-not-touch examples

Treat the following as out of scope unless explicitly prioritized:

- Full card redesign.
- Stretched-card links.
- Adding `target="_blank"` without a clear product decision.
- External-link icons.
- SEO, performance, deployment, or security work.
- Broad CSS architecture refactor.
- Article-to-div mass refactor.
- JavaScript enhancements.

## Reusable AI audit prompt

Copy and adapt this prompt for Copilot or Claude:

```text
Audit-only task: Review this repository for accessibility and semantic HTML risks.

Requirements:
- Audit only. Do not edit files.
- List affected files for every finding.
- For each finding, include: current implementation, gap/risk, severity, and recommendation.
- Classify severity as High, Medium, Low, Defer, or No change.
- Map each finding to an issue (current sprint issue or future backlog).
- Avoid scope creep beyond accessibility and semantic hardening.
- Distinguish definite issues from context-dependent risks.
- Do not claim WCAG failures unless clearly justified.

Focus files:
- templates/base.html
- apps/pages/templates/pages/*.html
- apps/projects/templates/projects/*.html
- static/css/base.css
- static/css/layout.css
- static/css/components.css
- static/css/main.css
- tests only if needed for rendering/verification coverage

Output sections:
1. Executive summary
2. Findings table
3. File-by-file review
4. Issue mapping validation
5. Deferred/do-not-touch list
6. Proposed implementation order
7. Verification checklist
```

## Verification checklist

After changes are implemented (not during audit-only pass), verify:

- `make quality`
- Keyboard tab check
- Skip-link check
- 375px mobile check
- 200% zoom check
- No horizontal overflow check
- Project index/detail review