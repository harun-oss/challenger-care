---
name: seo-content-writing
description: 'Writes SEO-optimised articles, guides, comparison pages, PDP SEO copy. Intent-matched structure, E-E-A-T signals, optimised meta tags, schema-ready. MANDATORY TRIGGER: any mention of "write SEO content", "write this article", "write this blog post", "write this guide", "write SEO landing page", "organic content for [keyword]". Do NOT use for: Ad or email copy. Creating content briefs (use `content-brief`).'
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/team-roles.md, CONFIG.md


# SEO Content Writing

## What this skill does

Writes SEO-optimised content that satisfies search intent, demonstrates E-E-A-T, and is structured for both readers and Google's ranking systems. The starting point is always the brief — but if no brief exists, this skill will create the structure before writing.

Content that ranks in 2024–2025 is not content that game search engines. It is content that genuinely answers the user's question better than anything else on the SERP — with first-hand perspective, cited evidence, and clear structure. That is what this skill produces.

Use this skill when:
- Writing new blog posts, guides, or articles from a brief
- Writing or rewriting product and service landing pages
- Writing SaaS comparison pages, alternative pages, and use-case pages
- Updating and improving existing underperforming content

---

## Phase 1 — Brief Intake

Before writing, confirm:

1. **Target keyword and secondary keywords**
2. **Confirmed intent** — informational, commercial, transactional, or navigational?
3. **Target length** — based on SERP benchmark (not a round number target)
4. **E-E-A-T tier** — High (YMYL), Medium (reviews/comparisons), or Standard?
5. **Existing brief** — if `content-brief` skill has already been run, use its output as the structural input here
6. **GSC query context (refresh writes only)** — if this is a refresh of an existing URL, pull its top GSC queries via Composio (`use_case`: *"pull GSC queries for URL {url} last 90 days"* — see the live MCP connectors). Use those queries to inform H2 selection and ensure the refresh doesn't accidentally drop terms the page already ranks for. If Composio is not connected or the pull fails, ask the user for a GSC export filtered to this URL before writing — do not refresh a page without seeing its current query mix; you risk killing terms it already ranks for.

If no brief exists: ask for the keyword, run a quick SERP check, determine intent and structure, then proceed.

---

## Phase 2 — Structure by Intent

The content structure must match the intent. Writing a guide-format article for a transactional keyword, or a product-push landing page for an informational keyword, will fail to rank regardless of quality.

### Informational — Guide or Tutorial

```
H1: [Keyword-matched, reader benefit clear]
Intro (100–150 words): Problem → relevance → what they'll get
[Featured Snippet answer if applicable: 40–60 words, direct answer to the query]
H2: [Core concept or first step]
H2: [Second concept or step]
H2: [Third concept or step]
...
H2: Common mistakes / what to avoid [optional but high E-E-A-T signal]
H2: FAQs (People Also Ask questions) [high AI Overview citation signal]
Conclusion: Recap + clear next step CTA
```

**Length:** 1,500–2,500 words for competitive informational keywords. Do not pad — comprehensiveness over word count. An 800-word post that fully satisfies the query outranks a 3,000-word post that wanders.

### Commercial — Comparison or Roundup

```
H1: Best [Category] for [Audience/Use Case] in [Year]
Intro: Why this matters + methodology (how did you evaluate? what criteria?)
H2: Quick comparison table (feature matrix, pricing, best for)
H2: [Option 1] — detailed review
  H3: What it does well
  H3: Limitations
  H3: Pricing
  H3: Best for
H2: [Option 2] — same structure
...
H2: How to choose (buying guide)
H2: FAQs
Conclusion: Clear recommendation by use case
```

**E-E-A-T requirement:** State the methodology explicitly. "We tested these for 30 days" or "We interviewed 12 agency owners" carries more weight than "We researched these tools." Generic roundups that could have been written by AI without testing anything are precisely what the Helpful Content System penalises.

### Transactional — Product or Service Landing Page

```
H1: [Product/Service Name] — [Key Benefit]
Hero section: Value proposition in 1–2 sentences. What it does. For whom. Why it's different.
H2: Features / What's included (benefit-led, not spec-led)
H2: [Use case or customer type] — show how it solves a specific problem
H2: Social proof (testimonials, case study, data)
H2: Pricing / How it works
H2: FAQs (schema-ready)
CTA: prominent, repeated at natural decision points
```

**Length:** 800–1,500 words. More copy is not more convincing for transactional pages — clarity and trust signals convert.

### B2B SaaS — Comparison Page (BOFU)

The highest-converting organic page type for SaaS. [Competitor] vs [Brand] and "[Tool] alternatives" pages convert at much higher rates than informational content because users are actively in the decision phase.

```
H1: [Competitor] vs [Brand]: Which is right for you?
Intro: Honest framing — both tools are good at different things; this helps you decide
H2: Quick summary (for skimmers) — 1-paragraph answer with clear recommendation by use case
H2: Feature comparison table (honest; don't hide weaknesses)
H2: [Competitor] strengths and best use cases
H2: [Brand] strengths and best use cases
H2: Pricing comparison (be transparent; hidden cost concerns kill conversion)
H2: What [Competitor] users say when they switch [if applicable — review data]
H2: Who should choose which
H2: FAQs
CTA: Free trial / demo — direct, not buried
```

**Honest framing is essential.** A comparison page that is clearly biased reads as a sales pitch and users leave. A page that genuinely helps users decide — even if it occasionally says "competitor X is better for Y use case" — builds trust and converts.

---

## Phase 3 — E-E-A-T Integration

E-E-A-T signals cannot be bolted on after writing. They must be woven through the content from the start.

### Experience signals (most important for the Helpful Content System)

- Write in the first person for medium/high E-E-A-T tiers: "When we ran this for a client last quarter..." not "According to experts..."
- Include specific details that only someone with first-hand experience would know: numbers, outcomes, failed approaches, what surprised you
- Reference actual examples — not hypothetical scenarios

### Expertise signals

- State the author's credentials or relevant experience in the byline or intro
- Use precise, field-accurate language — generic descriptions signal non-expert authorship
- Cite primary sources (original research, official documentation) not secondary summaries

### Authoritativeness signals

- Reference other authoritative sources by name and link to them
- Include expert quotes where relevant (ideally first-party quotes, not recycled quotes)
- Link to original data rather than citing statistics without a source

### Trust signals

- Publish and last-updated dates must be visible
- Cite every statistic with a link to its source
- Acknowledge nuance and limitations — content that presents only one side feels promotional
- Include a clear CTA to contact or get help — opaque, anonymous content is lower trust

---

## Phase 4 — Meta Tags and Schema

Every piece of content needs these before publishing:

### Title Tag

**Formula by page type:**
- Blog post/guide: `[Target keyword] — [Brand]` (under 60 chars)
- Comparison page: `[Competitor] vs [Brand]: [Key differentiator]`
- Product/service page: `[Product Name] — [Key Benefit] | [Brand]`
- Roundup: `Best [Category] for [Audience] ([Year]) — [Brand]`

**Rules:**
- Under 60 characters (600 pixels) — beyond this gets truncated
- Target keyword at the start
- Brand at the end
- No keyword stuffing — one clear focus

### Meta Description

**Formula:** `[Answer/benefit in first clause] — [additional value or CTA] | [Brand]`

**Example:** `Compare the top project management tools for agencies. Feature-by-feature breakdown, pricing, and our recommendation. — Challenger`

**Rules:**
- 155–160 characters
- Include target keyword naturally (Google bolds it)
- Clear CTA ("Compare", "See", "Learn", "Get")
- Unique per page — never auto-populate with the first paragraph

### Schema

Specify in the brief and implement in the page:
- Blog post: `Article` with `datePublished`, `dateModified`, `author` (name + credentials)
- Comparison page: `Article` + `BreadcrumbList`
- Product page: `Product` with `offers`, `aggregateRating`, `availability`
- SaaS landing page: `SoftwareApplication` + `AggregateRating`
- FAQ section: `FAQPage` (implement for AI citation benefit even if rich results are deprecated for most sites)

---

## Phase 5 — Content Quality Checklist

Before delivering any piece of content:

- [ ] Intro leads with the reader's problem or context — not a definition of the keyword or "In today's digital world..."
- [ ] Featured Snippet answer written (if SERP shows a snippet): direct, 40–60 words, in the first substantive section
- [ ] No section is padding — every H2 earns its place; delete anything that doesn't advance the reader
- [ ] At least one E-E-A-T signal per major section (specific example, first-hand reference, cited data, credential)
- [ ] Every statistic linked to its primary source
- [ ] No unverified claims — if uncertain, qualify ("according to...", "in our experience...")
- [ ] Internal links specified and placed (not "add links later")
- [ ] Title tag under 60 chars, keyword first
- [ ] Meta description 155–160 chars, CTA included
- [ ] Schema type specified for the developer
- [ ] Page last-updated date will be visible on publish

---

## Phase 6 — Synthesis Brief

Before final delivery, write a summary for orchestrator handoff.

**SEO Content Writing Key Findings**
- Intent alignment status: confirmed [Informational/Commercial/Transactional/Navigational], structure applied matches top-ranking format (e.g., comparison page with 4 sections, 2,100 words)
- E-E-A-T signals embedded: X first-hand examples, Y cited primary sources, Z author credentials/background stated
- Internal links placed: X internal links to related content (specify anchor text targets)
- Schema markup type specified: Article/Product/SoftwareApplication/BreadcrumbList with dateModified required

**Priority for downstream skills:** seo-reporting should monitor this page weekly starting week 2 post-publish. Content should rank within 3–6 months for target keyword. If CTR underperforms expected position by month 2, flag for title/meta update or content refresh.

*If running standalone, share with AM; ready for publishing.*

---

## QA Gate

Before delivering the final content:

- [ ] Content format matches confirmed SERP intent (not assumed)
- [ ] Length is appropriate for intent and SERP benchmark — not padded, not thin
- [ ] E-E-A-T tier requirements met (High/Medium/Standard as specified in brief)
- [ ] Title tag and meta description both drafted, both within character limits
- [ ] Schema type specified
- [ ] Internal links in place (not "TBD")
- [ ] No intro that starts with "In today's...", "In this article...", or a keyword definition
- [ ] Content quality checklist complete

---

## Reference Files

- `references/writing-playbook.md` — Intro formulas by intent type, E-E-A-T integration patterns with worked examples, comparison page structure templates, SaaS landing page copy framework, and the 2024–2025 Helpful Content System checklist. Required before Phase 2 for structure templates and Phase 3 for E-E-A-T integration patterns.

---

## References

- **[Content Writing Playbook](references/writing-playbook.md)** — Intro formulas by intent type, E-E-A-T integration patterns with worked examples, comparison page structure templates, SaaS landing page copy framework, and the 2024–2025 Helpful Content System checklist.
- **[Brand](../../assets/brand-strategy.md)** — Read when content carries branding or is produced for a DOCX/PPTX output.
- **[Content Brief](../content-brief/SKILL.md)** — Use before writing to produce the full structural brief. Writing without a brief produces inconsistent results.
- **[Keyword Research](../keyword-research/SKILL.md)** — Use before the brief if no keyword research has been done yet; establishes intent and clustering before content structure.
- **_SEO Reporting (not in this plugin · ask operator)_** — Use after publishing to track content performance and flag pages that need updating.
- **[Email Copywriting](../email-copywriting/SKILL.md)** — Use for email copy specifically. Different intent, different format, different skill.
