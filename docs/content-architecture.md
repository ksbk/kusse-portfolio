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

## KP-1003 — Project Categories

### Recommended Project Categories

The approved project categories for the v1 Projects page are:

1. Flagship Projects
2. Research Software
3. Applied Data and AI Projects
4. Full-Stack and Backend Engineering
5. Engineering Process and Technical Writing

### Taxonomy Rule

Flagship Projects is a featured and evidence-quality grouping, not a project type category.

The remaining categories describe project type.

In implementation later, each project should have one primary type category, may include optional tags, and may optionally be marked as flagship when it meets flagship criteria.

### Purpose Of Each Category

#### Flagship Projects

Purpose: highlight the strongest, most representative evidence of professional work quality for employers, collaborators, and technical reviewers.

#### Research Software

Purpose: show software work grounded in scientific problem-solving, research rigor, and reproducible technical practice.

#### Applied Data and AI Projects

Purpose: present practical data and AI work that demonstrates Python, data processing, modeling, evaluation, and applied problem-solving.

#### Full-Stack and Backend Engineering

Purpose: present software engineering capability across web application development, backend architecture, APIs, and delivery-oriented implementation.

#### Engineering Process and Technical Writing

Purpose: provide supporting evidence of engineering process quality through documentation, architecture communication, development workflow clarity, and technical writing.

### What Belongs In Each Category

#### Flagship Projects

Belongs here: selected high-quality projects from any primary type category when they meet flagship criteria and provide strong, defensible evidence.

#### Research Software

Belongs here: research tools, reproducible analysis workflows, domain-specific computational methods, and software that supports scientific investigation or research outputs.

#### Applied Data and AI Projects

Belongs here: data pipelines, analytical tools, applied machine learning, model-assisted applications, automation workflows, and evaluation-focused data or AI solutions.

#### Full-Stack and Backend Engineering

Belongs here: web applications, backend services, API-driven systems, integration projects, and implementation-focused software with clear engineering structure.

#### Engineering Process and Technical Writing

Belongs here: architecture documentation, implementation notes, technical guides, testing or workflow documentation, and communication artifacts that support software quality and delivery.

### Distinguishing Flagship Work From Supporting Work

A project should be marked as flagship only when most of the following are clearly present:

- Clear problem statement.
- Clear role and ownership.
- Concrete technologies used.
- Evidence such as screenshots, GitHub link, demo, docs, publication, benchmark, or reproducible artifact.
- Modest, defensible outcome or learning result.
- Strong fit with the site's positioning: research background plus practical software engineering.

Supporting work includes credible and relevant projects that do not yet meet enough flagship criteria, but still contributes useful evidence within a primary type category.

### What Should Not Be Included In V1

The v1 Projects taxonomy should not include:

- Placeholder projects without concrete artifacts or evidence.
- Overstated claims about commercial success, production impact, or scale that are not clearly supported.
- Toy or learning exercises presented as production-grade work.
- Private client-sensitive details, confidential information, or sensitive internal context.
- Implementation-level details that belong to later build phases rather than Sprint 1 content architecture decisions.
- Large uncategorized project dumps that reduce clarity for target audiences.

### Risks and Tradeoffs

Flagship as a separate featured grouping improves evidence visibility but can create overlap with type categories. This is acceptable if primary type and flagship status are handled as separate fields in later implementation.

Research Software and Applied Data and AI Projects may overlap in some projects. This should be handled by assigning a single primary type based on the project's core objective and using optional tags for secondary attributes.

Engineering Process and Technical Writing strengthens repository-reviewer credibility but can dilute focus if it grows too large relative to project evidence. It should remain a supporting category rather than replacing project outcomes.

A strict flagship threshold protects credibility, but early in portfolio development it may reduce the number of highlighted entries. This tradeoff is preferable to over-claiming.
