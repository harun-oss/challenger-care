---
name: keyword-research
description: 'SEO keyword discovery + intent classification + competitive gap analysis + clusters + topical authority. MANDATORY TRIGGER: any mention of "SEO keyword research", "what keywords should we rank for", "keyword gap analysis", "competitor keywords", "topical authority", "search intent", "keyword clusters". Do NOT use for: Google Ads keyword research (use `google-ads-keyword-research`). Writing content (use `seo-content-writing`).'
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/competitor-map.md, assets/customer-archetypes.md, assets/team-roles.md, CONFIG.md


# Keyword Research

## What this skill does

Maps the full keyword opportunity for a client — what people are searching for, what intent sits behind those searches, what competitors rank for that Challenger doesn't, and how to organise keywords into clusters that build topical authority rather than chasing isolated rankings.

The shift in 2024–2025 is fundamental: Google rewards comprehensive topic expertise over individual keyword targeting. A site demonstrating deep authority in a subject outranks sites chasing individual keywords. This skill produces the architecture to build that authority systematically.

Use this skill when:
- Starting keyword strategy for a new client
- Expanding an existing content programme
- Running a competitive gap analysis before a content sprint
- Building a topical authority map for a new content hub

---

## Phase 1 — Context

Ask one question at a time:

1. **Client, industry, and business model** — eCommerce, B2B SaaS, lead gen, or publisher? Product categories or service lines?
2. **Target audience** — who is buying? ICP: industry, role, company size, pain points?
3. **Tool access** — Ahrefs, Semrush, Google Search Console, or manual SERP analysis only?
4. **Existing rankings** — if Composio is connected (see the live MCP connectors), pull GSC queries automatically with `use_case` *"pull last 90 days of Google Search Console queries filtered to positions 4–20 for site {url}"*. Otherwise, ask the user to export from GSC → Performance → Queries with a position filter of 4–20.
5. **Competitors** — who are the top 3 competitors? (For gap analysis)
6. **Priority page types** — product/collection pages, blog/content hub, landing pages, or all?

---

## Phase 2 — Search Intent Classification

Every keyword must be classified by intent before assigning it to a page. Targeting the wrong page type for an intent is one of the most common reasons good content doesn't rank.

### The Four Intent Types

| Intent | What the user wants | SERP signals | Content format | Target length |
|--------|--------------------|--------------|--------------|-|
| **Informational** | Answers, education, how-tos | Featured snippets, PAA boxes, guides | Blog post, guide, tutorial | 1,500–2,500+ words |
| **Navigational** | A specific site or brand | Branded results, sitelinks | Brand page, homepage | 300–800 words |
| **Commercial** | Research before buying | Comparison articles, listicles, reviews | Comparison/roundup page | 1,500–2,500 words |
| **Transactional** | Ready to buy or convert | Product pages, shopping results, ads | Product/service page | 800–1,500 words |

### How to Read Intent from SERP Features

Before assigning intent to any keyword, search it and observe what Google shows:

- **Featured Snippet present:** informational intent — Google found a direct answer worth surfacing
- **People Also Ask (PAA) dominant:** informational; user has related sub-questions
- **Shopping results / product carousels:** transactional intent
- **Comparison articles dominate page 1:** commercial intent — users are evaluating options
- **One brand dominates with sitelinks:** navigational intent — don't target this with content
- **AI Overview triggered:** the query is informational or question-based; optimise content to be cited in the AIO, not just to rank position 1

**Rule:** The winning content format on page 1 tells you what Google believes the intent is. Match it.

---

## Phase 3 — Seed Keyword Discovery

Build the initial keyword universe from multiple sources before filtering:

**Source 1 — Client's GSC data (the quick-win goldmine)**
Use the GSC query pull from Phase 1, filtered to positions 4–20: these are keywords Challenger ranks for but doesn't fully capture. Improving from position 7 to 3 is often more impactful than building entirely new rankings.

For each candidate keyword in this band, also pull its current CTR via the same Composio call. Low CTR (below 1.5%) at positions 4–10 = title/meta optimisation opportunity to flag in the deliverable.

**Source 2 — Competitor analysis**
For each competitor:
- Pull top organic pages (by traffic) from Ahrefs / Semrush → Site Explorer → Top Pages
- Export their ranking keywords
- Identify which keywords drive significant traffic for competitors that Challenger ranks outside the top 20 for (the gap)

**Source 3 — SERP-based discovery**
- Google Autocomplete: type Challenger's core topic + alphabet (a, b, c...) and capture suggestions
- People Also Ask: search core topic, expand PAA questions — these map informational sub-topics
- Related Searches (bottom of SERP): broader and adjacent terms worth capturing

**Source 4 — Topical mapping**
- What are all the sub-topics within Challenger's core subject area?
- Use Ahrefs → Keywords Explorer → "Questions" filter for the core topic
- Use Semrush → Topic Research for the core topic

---

## Phase 4 — Keyword Clustering and Topical Authority

Keyword clustering groups terms by how Google treats them — not just lexical similarity. Pages that rank for 20–30 related keywords outperform pages targeting one keyword. Topical authority is built by covering a subject comprehensively across a cluster, not by one perfect page.

**Performance data:**
- Content organised in clusters drives **+30% more organic traffic** than standalone pages
- Cluster content holds rankings **2.5× longer** than isolated content
- Sites with clear topical authority gained **+23% organic visibility** after Google's June 2025 Helpful Content Update; generic multi-topic sites lost **18%** on average

### Cluster Architecture

```
PILLAR PAGE (broad overview, 1,500–3,000 words)
│── Cluster Page 1 (deep sub-topic)
│── Cluster Page 2 (deep sub-topic)
│── Cluster Page 3 (deep sub-topic)
│── Cluster Page 4 (deep sub-topic)
└── Cluster Page 5–15 (deep sub-topics)

Rules:
- Pillar links to every cluster page
- Every cluster page links back to pillar (non-negotiable)
- Related cluster pages link to each other where topically relevant
```

### How to Build Clusters

1. **Group keywords by SERP overlap** — if two keywords frequently return the same top-10 results, they belong on the same page (same cluster)
2. **Map each cluster to one URL** — one page should capture the cluster, not one page per keyword
3. **Identify the pillar keyword** for each cluster — the broadest, highest-volume term becomes the pillar page
4. **Sub-topics become cluster pages** — each sub-topic that requires its own in-depth treatment gets a dedicated page

### eCommerce Cluster Example

**Pillar:** "Golf training aids" (broad category term)
- Cluster: "Golf swing trainers" (product sub-category)
- Cluster: "Best putting trainers for home" (commercial intent)
- Cluster: "How to fix a slice with a training aid" (informational)
- Cluster: "Golf training aids for beginners" (informational/commercial)

### B2B SaaS Cluster Example

**Pillar:** "Project management software" (core category)
- Cluster: "Project management software for agencies" (use-case)
- Cluster: "Asana vs [Client Brand]" (comparison/BOFU)
- Cluster: "[Client Brand] alternatives" (BOFU)
- Cluster: "How to manage remote team projects" (informational)
- Cluster: "[Client Brand] pricing" (BOFU, navigational)

> For full cluster mapping templates and a step-by-step topical authority build guide, read `references/keyword-playbook.md` → Topical Authority and Cluster Architecture.

---

## Phase 5 — Keyword Priority Scoring

Not all keywords should be actioned equally. Score each keyword across three dimensions and rank the list.

### Priority Score Formula

```
Priority Score = (Search Volume score × 0.35) + (Intent Match score × 0.40) + (Opportunity score × 0.25)

Search Volume score (1–5):
  5 = 10,000+ monthly searches
  4 = 1,000–9,999
  3 = 100–999
  2 = 10–99
  1 = <10

Intent Match score (1–5):
  5 = transactional or commercial — directly generates revenue or leads
  4 = commercial — high consideration, conversion-adjacent
  3 = informational with clear product linkage
  2 = informational, loosely related
  1 = navigational or brand competitor

Opportunity score (1–5):
  5 = client ranks 4–10 (improve existing ranking)
  4 = competitors rank 1–3 with weaker domain authority than client
  3 = client ranks 11–20 (page 2 push)
  2 = keyword difficulty <30, no client ranking
  1 = KD >60, no client ranking
```

**Sort by Priority Score descending.** The top 20 keywords are the first content sprint. The full list is the 6–12 month roadmap.

### B2B SaaS BOFU Priority Override

For B2B SaaS clients, BOFU keywords get a priority bonus regardless of volume — they convert at significantly higher rates than informational content. Add +1 to Intent Match score for:
- "[Competitor] alternative" keywords
- "[Competitor] vs [Client Brand]" keywords
- "[Category] software for [industry]" keywords
- "[Client Brand] pricing" keywords

These pages generate the most qualified pipeline even at low search volumes.

---

## Phase 6 — AI Overviews Keyword Strategy

AI Overviews now appear on ~30% of US desktop queries. For AI Overview queries, organic CTR drops by ~61% — but brands **cited** in AI Overviews earn 35% more organic clicks and 91% more paid clicks than non-cited brands.

The strategic implication: for informational and question-based keywords, optimise content to be *cited in* the AI Overview, not just to rank position 1.

**Query types most likely to trigger AI Overviews:**
- 7+ word queries: 46.4% trigger rate
- Question-based queries: 57.9% trigger rate
- Single-word queries: 9.5% trigger rate
- Shopping/transactional: ~3.2% trigger rate (lowest — eCommerce is largely protected)

**AI Overview optimisation signals:**
- Structured, factual content with clear answers at the top
- Structured data (schema markup) — AI systems cite structured data 4× more often than unstructured text
- E-E-A-T demonstrated (author credentials, citations, original research)
- Content freshness (updated within 30–90 days)

**Flag any keyword** in the priority list that has a high AI Overview trigger likelihood — these need content optimised for citation, not just position 1.

**Automated AIO check:** for the top 30 priority keywords, batch-fire Composio web search calls and parse responses for AIO presence + citation source. Eliminates the manual SERP-checking step that today takes ~1 hour per keyword research project.

---

## Phase 7 — Synthesis Brief

Before delivering the final keyword plan, write a brief summary for orchestrator handoff.

**Keyword Research Key Findings**
- Top 3 priority clusters with pillar keywords, monthly search volume, keyword difficulty, and opportunity scores
- Intent distribution breakdown: X% transactional, Y% commercial, Z% informational keywords
- AI Overviews exposure: X% of target keywords trigger AIO, Z% currently cite client, A keywords have competitor citations but client doesn't
- Top negative/filter keywords that should be excluded from content strategy

**Priority for downstream skills:** content-brief should begin with cluster 1 pillar page and top BOFU keywords first. Secondary clusters and informational content should follow. Rank tracker should monitor all top 30 keywords weekly.

*If running standalone, share this with the operator before the full deliverable.*

---

## Phase 8 — Output

Deliver a keyword plan with the following structure:

1. **Summary:** Total opportunity, top 10 priority keywords, key competitive gaps
2. **Priority keyword list:** Top 30–50 keywords, sorted by priority score, with intent, volume, difficulty, and current ranking noted
3. **Cluster map:** 3–5 topic clusters, each with pillar keyword and sub-topics
4. **BOFU list:** All bottom-of-funnel keywords identified (competitor comparisons, alternatives, pricing, use-case) — especially important for SaaS
5. **AI Overviews exposure:** Which target keywords trigger AI Overviews and what content format is being cited
6. **Content sprint plan:** First 12 URLs to create or optimise, in priority order, with intent and format specified

---

## QA Gate

Before delivering the keyword plan:

- [ ] Every keyword has intent classified (not assumed)
- [ ] SERP checked for at least top 15 priority keywords — format matches intent
- [ ] Competitive gap analysis run against at least 2 competitors
- [ ] Keyword clusters mapped — each cluster has a pillar keyword and at least 3 sub-topics
- [ ] Priority scoring applied — no flat "nice to have" list
- [ ] BOFU keywords explicitly called out for SaaS clients
- [ ] AI Overviews trigger rate assessed for top informational keywords
- [ ] Existing GSC rankings (pos. 4–20) included as quick-win opportunities

---

## Reference Files

- `references/keyword-playbook.md` — Full topical authority cluster templates, priority scoring worked examples, B2B SaaS BOFU keyword frameworks, eCommerce keyword architecture, and AI Overviews optimisation guide. Required before Phase 4 for cluster mapping and Phase 5 for priority scoring.

---

## References

- **[Keyword Playbook](references/keyword-playbook.md)** — Full topical authority cluster templates, priority scoring worked examples, B2B SaaS BOFU keyword frameworks, eCommerce keyword architecture, and AI Overviews optimisation guide.
- **[Brand](../../assets/brand-strategy.md)** — Read before producing any DOCX or markdown deliverable. Contains colours, typography, and component patterns for branded output.
- **[Content Brief](../content-brief/SKILL.md)** — Use after keyword research to turn prioritised keywords into detailed writer briefs.
- **[SEO Audit](../seo-audit/SKILL.md)** — Run before keyword research if the technical foundation hasn't been confirmed.
