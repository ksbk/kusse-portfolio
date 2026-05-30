# drkusse.com Content Architecture

This document records Sprint 1 content architecture decisions for drkusse.com.

## KP-1001 — Navigation Structure

### Primary Navigation

The approved primary navigation for v1 is:

1. Home
2. About
3. Research
4. Projects
5. CV
6. Contact

### Secondary and Footer Links

The following links may appear in secondary navigation areas or the site footer:

- GitHub
- LinkedIn
- Email / Contact CTA
- Writing, only if content exists later
- Repository Docs, optional footer link for GitHub and process reviewers
- Privacy / Imprint, only if needed for deployment or legal context

### Rationale

The primary navigation should stay simple, professional, and easy to scan for the site's main audiences: employers and recruiters, research collaborators, technical clients or collaborators, and people reviewing the public GitHub repository.

The selected items map directly to the documented MVP scope:

- Home introduces the professional identity, featured work, and primary contact path.
- About provides concise background, positioning, and professional context.
- Research keeps research background and scientific problem-solving visible as a core differentiator.
- Projects groups software projects and technical portfolio work under one clear top-level label.
- CV gives employers and recruiters a direct route to professional summary, skills, selected work, research, education, and download or contact actions.
- Contact provides a clear action path for employers, collaborators, clients, and professional contacts.

Projects is intentionally used as the top-level label instead of splitting Software Projects and Technical Portfolio. The distinction between project types should be handled inside the Projects section through categories, filters, headings, or project metadata rather than by adding more top-level navigation items.

Secondary links are reserved for supporting actions and context. GitHub and Repository Docs are useful for people reviewing the public development process, but they should not make the main site navigation feel like a repository dashboard. LinkedIn and email support professional contact paths without competing with the main content structure.

### Intentionally Excluded From Main Navigation

The following items should not be included in the primary navigation for v1:

- Blog or Writing, unless real content exists and publishing it becomes an active part of the site.
- Architecture, Roadmap, ADRs, issue links, milestones, or other repository process pages.
- Separate Software Projects and Technical Portfolio top-level items.
- Skills as a standalone top-level item.
- Theme controls or other visual preferences.
- Admin, login, payments, dashboards, comments, or client portal features.

These exclusions keep the navigation focused on public professional content and avoid exposing implementation, repository management, or out-of-scope product concepts as primary visitor paths.

### Risks and Tradeoffs

Combining software projects and technical portfolio work under Projects may make technical categories less visible from the top-level navigation. This should be addressed through clear project taxonomy in the Projects section.

Keeping Blog or Writing out of the main navigation reduces clutter for v1, but it may need to be revisited if writing becomes a meaningful content area.

Giving Research a top-level navigation item uses valuable navigation space, but it is justified because the project charter treats research background and scientific problem-solving as core parts of the site's professional identity.
