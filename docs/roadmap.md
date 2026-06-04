# drkusse.com Roadmap

This roadmap is a high-level planning document. Detailed actionable tasks are tracked in GitHub Issues and grouped by GitHub Milestones.

## Task ID and Tracking Convention

- `KP` stands for `Kusse Portfolio`.
- Detailed actionable tasks are tracked in GitHub Issues.
- Roadmap sections map to GitHub Milestones.

## Sprint 0 - Foundation

- Goal: Establish planning, requirements, architecture, and repository hygiene baseline.
- Status: Completed
- Scope summary: Project charter, requirements, architecture, public repository decision, and safe repository setup are in place.
- GitHub milestone reference: `Sprint 0 - Foundation`

## Sprint 1 - Content Architecture

- Goal: Finalize information architecture and content model for all core sections.
- Status: Completed
- Scope summary: Navigation model, homepage section model, project and technical portfolio taxonomy, and CV structure definition.
- GitHub milestone reference: `Sprint 1 - Content Architecture`

## Sprint 2 - Core Pages

- Goal: Deliver the first complete set of primary public pages.
- Status: Completed
- Scope summary: Homepage, About, Research, CV, and Contact pages with aligned structure and baseline responsiveness.
- GitHub milestone reference: `Sprint 2 - Core Pages`

## Sprint 3 - Projects and Technical Portfolio

- Goal: Publish portfolio evidence with clear project storytelling.
- Status: Completed
- Scope summary: Software project listing, project detail structure, flagship project presentation, and selected technical portfolio entries.
- GitHub milestone reference: `Sprint 3 - Projects and Technical Portfolio`

## Sprint 4 - Polish and Public Evidence

- Goal: Improve presentation quality and public documentation completeness.
- Status: Completed
- Scope summary: Responsive refinements, visual artifacts, README expansion, deployment notes, and release-oriented documentation.
- GitHub milestone reference: `Sprint 4 - Polish and Public Evidence`

## Sprint 5 - Quality and Automation

- Goal: Strengthen engineering quality gates and delivery reliability.
- Status: Completed
- Scope summary: Automated tests, Ruff linting, pre-commit hooks, GitHub Actions CI, Makefile shortcuts, and quality documentation.
- GitHub milestone reference: `Sprint 5 - Quality and Automation`

## Sprint 6 - Public Portfolio Content and Presentation

- Goal: Improve public-facing portfolio content, evidence framing, presentation details, and reviewer handoff documentation.
- Status: Completed
- Scope summary: Roadmap status alignment, honest public copy review, project presentation refinements, stale placeholder cleanup, basic metadata improvements, and README refresh.
- GitHub milestone reference: `Sprint 6 - Public Portfolio Content and Presentation`

## Sprint 7 - Navigation States, Visual Hierarchy, and Responsive Refinement

- Goal: Improve frontend navigation clarity, visual hierarchy, responsive behavior, focus affordances, and final public-page review.
- Status: Completed
- Scope summary: Heading hierarchy, active navigation state, card grid responsiveness, project index density, accessible focus states, external link attributes, small navigation affordances, and final responsive review.
- GitHub milestone reference: `Sprint 7 - Navigation States, Visual Hierarchy, and Responsive Refinement`

### Issue Plan

- `KP-7001 - Fix heading hierarchy in card interiors`
- `KP-7002 - Add active navigation state`
- `KP-7003 - Improve card grid responsiveness`
- `KP-7004 - Reduce project index card density`
- `KP-7005 - Add accessible focus and active states`
- `KP-7006 - Add rel attributes to external links`
- `KP-7007 - Improve small navigation and link affordances`
- `KP-7008 - Final responsive frontend review`

## Sprint 8 - Accessibility and Semantic Hardening

- Goal: Strengthen the repository-wide accessibility and semantic HTML baseline using a repeatable audit workflow before making targeted fixes.
- Status: Completed
- Scope summary: Repo-wide review of user-facing templates and shared CSS against the accessibility checklist, including page structure, headings and labels, link purpose, label/list semantics, keyboard focus, skip-link behavior, touch targets, reading order, color/contrast risks, and final manual verification.
- GitHub milestone reference: `Sprint 8 - Accessibility and Semantic Hardening`

### Issue Plan

- `KP-8001 - Improve project link clarity`
  - Status: Completed
  - Scope: Early specific fix for repeated project links and evidence-link accessible names.

- `KP-8002 - Audit and improve label/list semantics across templates`
  - Scope: Review visually labelled lists or grouped links across user-facing templates, identify gaps, and make the smallest approved semantic fixes.

- `KP-8003 - Harden keyboard focus, skip link, and touch targets`
  - Scope: Review shared focus behavior, skip-link behavior, primary/footer navigation targets, and mobile tap comfort.

- `KP-8004 - Review heading hierarchy and redundant labels across templates`
  - Scope: Review page headings, section headings, repeated eyebrow/heading text, and labels that do not add useful structure.

- `KP-8005 - Final repo-wide accessibility verification`
  - Scope: Run final manual and automated quality checks, including keyboard navigation, skip link, mobile width, 200% zoom, no horizontal overflow, and targeted regression tests where useful.

## Sprint 9 - Project Visual Evidence and Portfolio Credibility

- Goal: Improve the credibility, clarity, and visual evidence of project entries without redesigning the whole portfolio.
- Status: Planned
- Scope summary: Add optional project screenshots or representative images, improve project proof points, review the balance of project index/detail pages after visual evidence is introduced, and complete a final portfolio credibility review.
- GitHub milestone reference: `Sprint 9 - Project Visual Evidence and Portfolio Credibility`

### Issue Plan

- `KP-9001 - Add project screenshots and visual evidence`
  - Scope: Add optional visual evidence for project entries while preserving clean rendering for projects without images.

- `KP-9002 - Improve project content quality and proof points`
  - Scope: Review project summaries, roles, tech stacks, evidence links, and proof-oriented wording so each project feels credible and specific.

- `KP-9003 - Review project card/detail visual balance after images`
  - Scope: Review spacing, image placement, card density, and detail-page readability after screenshots are introduced.

- `KP-9004 - Final portfolio credibility review`
  - Scope: Review the complete project section from a reviewer/client perspective and document any remaining follow-up work.

### Out of Scope

- No full site redesign.
- No gallery or multi-image system.
- No Cloudinary/R2/CDN integration unless separately approved.
- No image optimization pipeline beyond basic responsive handling.
- No new unrelated apps or sections.
- No SEO/performance/security sprint expansion.
- No rewriting the whole portfolio narrative.
