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

## KP-1002 — Homepage Sections

### Section Order

The approved homepage section order for v1 is:

1. Hero
2. Featured Work
3. Research + Software Identity
4. Skills Summary
5. Ways to Engage
6. Contact CTA

### Section Purposes and Content Direction

#### Hero

Purpose: establish who Kusse Sukuta Bersha is, what professional value the site presents, and where visitors should go next.

Suggested direction: introduce Kusse as a research-trained software developer working across Python, data, applied AI, full-stack web development, research software, and technical writing. The message should be concise and credible, with primary paths toward Projects, CV, and Contact.

#### Featured Work

Purpose: give employers, collaborators, clients, and technical reviewers immediate evidence of relevant work without requiring them to browse the full project catalogue first.

Suggested direction: Highlight 1–3 selected pieces of work, with one flagship item if available. Each item should show the problem, role, technology area, and outcome or evidence. The full project catalogue belongs on the Projects page.

#### Research + Software Identity

Purpose: connect the research background to practical software engineering ability, which is a core differentiator for the site.

Suggested direction: explain the relationship between scientific problem-solving, research software, applied development, and clear technical communication. This section should be concise and should point deeper research or background detail to the Research and About pages.

#### Skills Summary

Purpose: help recruiters, collaborators, and technical reviewers quickly understand the main capability areas.

Suggested direction: group skills into a short set of professional categories, such as Python and automation, data and SQL, applied AI and algorithms, full-stack web development, and research software or technical writing. The section should stay high-level and avoid becoming a complete skills inventory.

#### Ways to Engage

Purpose: provide lightweight audience routing without adding complexity to the primary navigation.

Suggested direction: route key audiences toward the most relevant next step: employers and recruiters toward CV and selected projects, research collaborators toward Research and technical work, clients or technical collaborators toward Projects and Contact, and GitHub reviewers toward repository or documentation links in secondary/footer areas.

#### Contact CTA

Purpose: give visitors a clear final action after they have reviewed the homepage.

Suggested direction: invite relevant professional contact for employment, research software, technical collaboration, or software development work. The CTA should point to Contact and may include email, LinkedIn, or GitHub as supporting links.

### Intentionally Excluded From The Homepage In V1

The homepage should not include:

- A full CV or resume content; the CV page should handle that.
- A complete project catalogue; the Projects page should handle that.
- Long personal biography; the About page should handle that.
- Detailed architecture, roadmap, ADR, milestone, or issue content.
- Blog or Writing sections unless real content exists and publishing becomes an active part of the site.
- Login, admin, payments, private dashboards, comments, or client portal concepts.
- Broad claims about outcomes, client work, production impact, or expertise that are not supported by available evidence.
- A long unstructured skills list without project or professional context.

### Risks and Tradeoffs

The homepage needs to serve several audiences without becoming overloaded. The section order should therefore prioritize a clear professional introduction, selected evidence, concise identity framing, lightweight skills, audience routing, and a final contact path.

Featured Work depends on having credible selected work available. If project evidence is still limited, the section should use modest language and emphasize problem, role, technology area, and evidence rather than overstating outcomes.

The Research + Software Identity section may compete with About or Research page content if it becomes too detailed. It should summarize the positioning and route visitors to deeper pages.

The Skills Summary is useful for scanning, but it should not replace project evidence. Skills should be framed as capability areas and supported elsewhere by selected work.
