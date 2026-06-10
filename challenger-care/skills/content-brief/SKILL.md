---
name: content-brief
description: 'Turns a target keyword into a complete writer brief - SERP analysis, search intent, structure (H1/H2/H3), E-E-A-T requirements, target length, schema, internal linking, meta formulas. MANDATORY TRIGGER: any mention of "content brief", "SEO brief", "brief a writer", "content outline", "structure for this post", "brief for [keyword]". Do NOT use for: Writing the content (use `seo-content-writing`). Keyword discovery (use `keyword-research`).'
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/voc/quote-library.md, assets/team-roles.md, CONFIG.md, assets/claim-library.md


# Content Brief

## What this skill does

Translates a target keyword into a complete, writer-ready brief. A good brief means the writer has everything they need to produce a page that satisfies both the reader's intent and Google's quality signals — without requiring multiple back-and-forths.

The brief is the highest-leverage document in a content programme. A weak brief produces content that needs to be rewritten. A strong brief produces content that ranks.

Use this skill when:
- Briefing an in-house writer or freelancer for a new page
- Producing the content structure before a writing sprint
- Ensuring a content team is aligned on E-E-A-T requirements before writing
- Creating briefs for a content calendar

---

## Phase 1 — Keyword and Intent Confirmation

Before structuring anything, confirm:

1. **Target keyword** — the primary keyword this page should rank for
2. **Secondary keywords** — related terms the page should also capture (from keyword clustering)
3. **Confirmed intent** — what is the user *actually* trying to do? (Do not assume — check the SERP)
4. **Target audience** — who is reading this? What do they already know? What do they want to walk away with?
5. **URL / page context** — new page or update? If update, automatically pull the URL's current GSC query mix via Composio (`use_case`: *"pull GSC queries and clicks for URL {url} last 90 days"* — see the live MCP connectors). The brief should reference the actual queries Google is sending — not assumed intent. If Composio isn't connected, request a GSC export filtered to this URL.

---

## Phase 2 — SERP Analysis

Search the target keyword in an incognito browser and analyse what is ranking.

**Answer these before writing the brief:**

1. **What content format dominates page 1?**
   - List post ("10 best X") → informational/commercial intent; listicle format
   - How-to guide → informational; tutorial format
   - Product/category page → transactional intent; page should be a landing page, not a blog post
   - Comparison page → commercial intent; head-to-head format
   - Single detailed guide → informational; long-form comprehensive format
   
   *The dominant format is Google's implicit instruction. Match it.*

2. **What is the average length of the top 3 results?**
   Use this as a depth benchmark — not a word count target, but a signal of how comprehensively the topic needs to be covered.

3. **What SERP features appear?**
   - Featured Snippet: structure content to answer the target question in 40–60 words in the first substantive section
   - People Also Ask: each PAA question is a potential H2 or H3 in the content
   - AI Overview: note what source is being cited and what format it uses — this informs the content's answer structure

4. **What are the top 3 pages missing?**
   Gaps in the current top-ranking content are the opportunity. What isn't being covered well? What angle is absent? What experience or data would make this page more useful than what's there?

---

## Phase 3 — E-E-A-T Requirements

E-E-A-T requirements vary by topic type. Assess the brief's requirements before writing begins — a writer who doesn't know what signals are required will produce generic content that fails Google's quality systems.

**Determine the E-E-A-T tier:**

| Tier | Topic type | Requirements |
|------|-----------|-------------|
| **High** | Financial, medical, legal, safety, civic | Author must have verifiable credentials. Cite all claims. Medical/legal disclaimer required. No unsourced claims. |
| **Medium** | Product reviews, SaaS comparisons, how-to guides, educational content | First-hand experience preferred. Case studies or worked examples required. Cite sources for statistics. Author bio with relevant background. |
| **Standard** | General informational content, brand storytelling | Author attribution. Accurate, up-to-date information. Link to primary sources where relevant. |

**Specify in the brief:**
- Author: who should write this, and what credentials/experience should they have or reference?
- Experience signals: should the writer include first-hand experience, a case study, original data, or a specific example from practice?
- Citations required: yes/no, and what kind (primary research, industry data, expert quotes)?
- Last-updated date: must be visible on the published page

---

## Phase 4 — Content Structure

The content structure is the core of the brief. Produce a full H1/H2/H3 outline with guidance on each section.

### Structure Template

```
PAGE BRIEF: [Target keyword]
URL: [Target URL slug — e.g., /blog/keyword-research-guide]
Target primary keyword: [Keyword]
Secondary keywords: [Keyword 2], [Keyword 3], [Keyword 4]
Search intent: [Informational / Commercial / Transactional / Navigational]
Target audience: [Who — their role, knowledge level, what they want to achieve]
Target word count: [X–X words, based on SERP benchmark]
E-E-A-T tier: [High / Medium / Standard]

TITLE TAG: [Keyword — Brand] (55–60 chars)
META DESCRIPTION: [150–160 char description with keyword + CTA]
H1: [Exact H1 text — matches target keyword closely]

INTRO (100–150 words):
  - Lead with the reader's problem or context, not the definition of the keyword
  - Establish why this matters to them specifically
  - State clearly what they will get from this page
  [If Featured Snippet present: include a direct 40–60 word answer in the first section]

H2: [First major subtopic]
  - What to cover: [2–3 sentences of guidance]
  - Target length: ~[X] words
  - Include: [any specific data, examples, or formats required]
  H3: [Sub-point if needed]
  H3: [Sub-point if needed]

H2: [Second major subtopic]
  - What to cover: ...
  - Include: ...

[Continue for all H2s]

CONCLUSION:
  - Summarise the key takeaways (not a word-for-word repetition of the article)
  - Direct next step: what should the reader do? (CTA appropriate to intent)

INTERNAL LINKS REQUIRED:
  - Link to: [URL] using anchor text "[anchor text]"
  - Link to: [URL] using anchor text "[anchor text]"

SCHEMA: [Product / Article / BreadcrumbList / FAQ — see Phase 5]
```

### H2 Topic Sources

Pull H2 topics from:
1. People Also Ask questions for the target keyword — these are real user sub-questions
2. H2s used by the top 3 ranking pages (what are they covering?)
3. Gaps in the top 3 pages (what are they NOT covering that they should?)
4. Secondary keyword clusters that belong on this page

---

## Phase 5 — Schema Recommendation

Specify the schema type required for the page in the brief. The writer/developer needs this before publishing.

| Page type | Recommended schema |
|-----------|-------------------|
| Blog post / article | `Article` or `BlogPosting` with `datePublished`, `dateModified`, `author` |
| Product page | `Product` with `offers`, `aggregateRating`, `availability` |
| Comparison / listicle | `Article` + `BreadcrumbList` |
| FAQ section | `FAQPage` (only eligible for government/health sites — for others, still implement for AI citation benefit) |
| Software / SaaS feature page | `SoftwareApplication` + `AggregateRating` |
| How-to guide | `HowTo` (deprecated for rich results but still implement for AI citation) |
| Ecommerce category | `BreadcrumbList` + `CollectionPage` |

**Key reminder:** HowTo and FAQPage no longer generate rich results for most sites (deprecated 2024–2025). However, AI systems (Gemini, Perplexity, ChatGPT) still extract structured data 4× more often than unstructured text — implement schema even where it no longer generates rich results in Google Search.

---

## Phase 6 — Internal Linking Plan

Specify required internal links in the brief. Writers and editors miss this step unless it is explicit.

For every brief, specify:
1. **Links this page should receive** — which existing pages on the site should link *to* this new page? (Brief the editor to add these after publishing)
2. **Links this page should give** — which existing pages should this page link *to*? Use descriptive anchor text matching the target keyword of the destination page

**Rule:** Every new page should have at least 3 internal links pointing to it within 30 days of publishing. Pages with zero internal links are invisible regardless of content quality.

---

## Phase 7 — Synthesis Brief

Before finalising the brief, write a summary for orchestrator handoff.

**Content Brief Key Findings**
- Confirmed search intent (Informational/Commercial/Transactional/Navigational) with SERP format rationale (list post, guide, comparison, product page)
- E-E-A-T tier assigned (High/Medium/Standard) with specific signal requirements (author credentials, cited sources, first-hand examples needed)
- Target word count: X–X words based on top 3 ranking pages benchmark
- Top 5 priority keywords this page must capture (pillar + secondary keywords)
- Competitive content gaps: what are top 3 pages NOT covering that this brief fills

**Priority for downstream skills:** seo-content-writing should follow this H1/H2/H3 outline verbatim for consistency with search intent. Internal linking plan must be executed within 30 days of publishing. After content publishes, seo-reporting should monitor SERP position weekly and flag for update if CTR underperforms by month 2.

*If running standalone, share this with the operator before briefing the writer.*

---

## QA Gate

Before sending the brief to a writer:

- [ ] SERP checked in incognito — format, length, and top 3 gaps documented
- [ ] Intent confirmed against SERP (not assumed)
- [ ] E-E-A-T tier specified with clear requirements for this specific topic
- [ ] H1/H2/H3 outline complete with guidance on each section
- [ ] Target word count set (based on SERP benchmark, not a round number)
- [ ] Title tag and meta description drafted (55–60 chars and 155–160 chars respectively)
- [ ] Schema type specified
- [ ] Internal links required — both inbound (who should link to this) and outbound (what this should link to)
- [ ] Featured Snippet opportunity flagged if applicable (write the 40–60 word direct answer)

---

## Reference Files

- `references/brief-playbook.md` — Full brief templates by content type (guide, comparison, product page, SaaS landing page), SERP feature → content format decision table, E-E-A-T signal checklist by tier, and schema implementation reference. Required before Phase 4 for content structure templates and Phase 3 for E-E-A-T tier requirements.

---

## References

- **[Brief Playbook](references/brief-playbook.md)** — Full brief templates by content type (guide, comparison, product page, SaaS landing page), SERP feature → content format decision table, E-E-A-T signal checklist by tier, and schema implementation reference.
- **[Brand](../../assets/brand-strategy.md)** — Read before producing any DOCX or markdown deliverable. Contains colours, typography, and component patterns for branded output.
- **[SEO Content Writing](../seo-content-writing/SKILL.md)** — Use after the brief is complete to write the actual content.
- **[Keyword Research](../keyword-research/SKILL.md)** — Use before the brief to confirm keyword clusters and intent.
