---
name: seo-audit
description: 'Technical + on-page + content SEO audit - crawlability, Core Web Vitals (LCP/INP/CLS), indexability, site architecture, E-E-A-T signals, schema, AI Overviews visibility, internal linking. Produces a prioritised fix list. MANDATORY TRIGGER: any mention of "SEO audit", "technical SEO audit", "site audit SEO", "SEO health check", "SEO review", "why arent we ranking", "SEO issues", "audit our SEO". Do NOT use for: Keyword strategy (use `keyword-research`). Content writing (use `seo-content-writing`).'
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/goals-targets.md, assets/team-roles.md, CONFIG.md


# SEO Audit

## What this skill does

A structured audit that identifies every technical, on-page, and content issue preventing a site from ranking. The audit is the mandatory starting point — no keyword strategy, content plan, or link building should begin without knowing the current state of the site.

The audit produces three things: a clear picture of what exists, a diagnosis of what's broken, and a prioritised fix list ordered by ranking impact — so the team knows where to spend the first 30, 60, and 90 days.

Use this skill when:
- Onboarding a new SEO client
- Taking over an existing site with flat or declining rankings
- Diagnosing a traffic drop after a Google algorithm update
- Before building any new content strategy

---

## Phase 1 — Context

> **Data source:** Composio is the default. See the live MCP connectors. The Coverage and Core Web Vitals sections run automatically when `google_search_console` is connected; the rest of the audit (Screaming Frog / Sitebulb / Ahrefs) still needs manual access.

Ask one question at a time:

1. **Data source check** — if the user has already provided audit data inline (indexed page counts, CWV scores, theme name, etc.), use what they gave you. Otherwise: run `COMPOSIO_MANAGE_CONNECTIONS`. If `google_search_console` is live for this client, the audit's Coverage and Core Web Vitals sections will run automatically. If not, request CSV exports of GSC Coverage and Core Web Vitals reports.
2. **Site URL and industry** — eCommerce (Shopify), B2B SaaS, lead gen, publisher, or other?
3. **Tool access** — Ahrefs / Semrush / Moz, Screaming Frog / Sitebulb? (These are NOT in Composio — still need manual access.)
4. **Baseline performance** — is organic traffic flat, declining, or unknown? Any recent traffic drops correlated with algorithm updates?
5. **Known issues** — has Challenger flagged any specific concerns (slow pages, duplicate content, a manual penalty)?
6. **Priority focus** — technical fixes, content quality, or link profile? (Determines where to go deep)

---

## Phase 2 — Technical Audit

### Crawlability and Indexability

These are the foundation. If Google cannot crawl and index pages, nothing else matters.

**Crawlability checks:**
- Robots.txt: Are any important pages or directories blocked from crawling? Misblocked pages are one of the most common audit findings — especially `/wp-admin/`, `/checkout/`, but sometimes critical category or product pages
- Meta robots: Check for accidental `noindex` tags on important pages (common on staging environments that were pushed to production)
- JavaScript rendering: Is important content rendered in JavaScript? Googlebot crawls JS but may miss dynamically injected content — verify with Google Search Console's URL Inspection tool

**Indexability checks** — auto-pulled from GSC via Composio (see the live MCP connectors). CSV-fallback equivalent: GSC → Coverage report.
- Indexed pages count: does it match the expected number of pages?
- "Discovered — currently not indexed": pages Google found but hasn't indexed; high volume here indicates crawl budget issues or low-quality pages
- "Crawled — currently not indexed": pages Google crawled but deemed not worthy of indexing; indicates thin content, duplicate content, or quality signals failure
- "Excluded by 'noindex' tag": confirm these are intentional

**Crawl budget (for large sites, 10,000+ pages):**
- Faceted navigation / filter parameters generating duplicate URLs waste crawl budget
- For Shopify: `/collections/all` and filter combinations are common culprits
- Fix: `noindex` on low-value parameter URLs, or configure via GSC URL parameters

### Site Architecture

- Max depth: any critical page (product, collection, service) should be reachable within 3–4 clicks from the homepage. Pages deeper than 4 clicks are crawled less frequently and pass less link equity
- Orphan pages: every indexable page must have at least one internal link pointing to it; pages with zero internal links are invisible to Google regardless of quality
- Breadcrumbs: are they present and structured? One eCommerce site saw organic CTR drop 40% after removing breadcrumbs; restored to 7% (above baseline) after reinstating them

### Core Web Vitals

These are confirmed Google ranking factors. Auto-pulled from GSC via Composio. PageSpeed Insights is a fallback for new sites without 28 days of CrUX data; the CSV-fallback equivalent of the GSC pull is GSC → Core Web Vitals report.

| Metric | Good | Needs Improvement | Poor | Note |
|--------|------|-------------------|------|------|
| **LCP** (Largest Contentful Paint) | ≤2.5s | 2.5–4s | >4s | Most common fail |
| **INP** (Interaction to Next Paint) | ≤200ms | 200–500ms | >500ms | Replaced FID March 2024 |
| **CLS** (Cumulative Layout Shift) | ≤0.1 | 0.1–0.25 | >0.25 | Layout stability |

**75th percentile rule:** 75% of real-world page visits must pass the "Good" threshold for the page to pass Core Web Vitals.

**INP note:** INP replaced First Input Delay (FID) on March 12, 2024. It is significantly more demanding — FID only measured the first interaction, INP measures all interactions throughout the page visit. Apps that injected JavaScript have the most exposure here.

**Common LCP failures (in order of frequency):**
1. Unoptimised hero images (not compressed, not using next-gen formats)
2. Third-party scripts blocking render (chat widgets, tracking pixels, review apps)
3. Render-blocking CSS or JavaScript
4. Slow server response time (TTFB above 600ms)

### Canonical Tags

- Every page should have a self-referencing canonical tag (even if no duplicates exist)
- No canonical chains (A → B → C; Google ignores chains)
- For eCommerce: product pages must canonicalize to clean `/products/` URLs, not collection-scoped URLs
- For Shopify: verify variant URLs (`?variant=12345`) canonicalize to clean product URLs

### HTTPS and Mobile

- HTTPS: confirm SSL is active across all pages; mixed content warnings (HTTP assets on HTTPS pages) can suppress rankings
- Mobile-first indexing is now Google's default for all sites — test with Google's Mobile-Friendly Test

> For the full technical audit checklist with pass/fail criteria for every item, read `references/audit-framework.md` → Technical Audit Checklist.

---

## Phase 3 — On-Page Audit

### Title Tags

Audit a sample of 20–30 pages across key page types:

| Issue | Signal | Fix |
|-------|--------|-----|
| Missing title tag | Critical — GSC will generate one automatically (usually bad) | Write optimised titles for all key pages |
| Over 60 characters (600px) | Gets truncated in SERPs | Trim to 55–60 chars |
| Duplicate title tags | Multiple pages competing for same query | Differentiate by page type and target keyword |
| Missing target keyword | Low relevance signal | Lead with keyword, brand at end |
| Keyword stuffing | Spam signal | One clear keyword focus per page |

**Formula by page type:**
- Product page: `[Product Name] — [Brand]` (55–60 chars)
- Collection/category: `[Category] | Shop [Brand]` or `Best [Category] — [Brand]`
- Blog post: `[Target keyword phrase] — [Brand]`
- Homepage: `[Brand] — [One-line value proposition]`

### Meta Descriptions

Not a ranking factor, but directly impacts CTR. Treat as ad copy.

- 155–160 characters max
- Unique per page (duplicate metas are a missed opportunity, not a penalty)
- Include target keyword naturally (Google bolds it in SERPs)
- Clear CTA: "Shop", "Learn", "Get", "See", "Download"
- If Google is rewriting metas for many pages, the existing metas are a poor match for the query — this is a content alignment issue, not a meta issue

### Header Structure

- One H1 per page, containing the primary target keyword
- H2s for main subtopics; H3s for sub-sections under H2s
- Do not skip levels (H1 → H3 with no H2)
- Do not use headers purely for styling — they are semantic signals

### Internal Linking

- Audit the internal link profile for key money pages: how many pages link to them? Low internal link count to important pages = low link equity reaching them
- Anchor text: internal links should use descriptive, keyword-relevant anchor text — not "click here" or "read more"
- Orphan pages: run a crawl (Screaming Frog / Sitebulb) and filter for pages with zero inlinks

---

## Phase 4 — Content and E-E-A-T Audit

E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) is not a direct ranking score but influences how Google's quality systems evaluate pages. The **Trust pillar is weighted most heavily**.

### Content Quality Signals

For each key page type, assess:

| Signal | Present? | Issue if absent |
|--------|----------|----------------|
| Author byline with credentials | Specialist content needs this | Generic, unattributed content signals low E-E-A-T |
| First-hand experience or original research | Highest priority | Generic summaries now rank poorly vs. experience-based content |
| Publication and last-updated date visible | Freshness signal | Hidden dates look like the content is being hidden |
| Cited sources and data | Trust signal | Claims without sourcing are a YMYL risk |
| Sufficient depth for intent | Satisfies query | Thin pages (fewer than 300 words, no substantive content) are excluded from index |

### Content Freshness

- Content not updated in 12+ months loses competitive position on high-competition keywords
- Content updated within 30–90 days is cited significantly more often in AI Overviews
- Average freshness of top-ranking pages: ~393 days (vs. ~500 days for losing pages)
- Create a staleness list: pages last updated >12 months ago that still receive clicks in GSC — these are update priorities

### Thin and Duplicate Content

- **Thin content:** pages with fewer than 300 words of substantive content; auto-generated pages; tag and archive pages with minimal content
- **Duplicate content:** same or near-identical content on multiple URLs (common with Shopify facets, pagination, and product variant pages)
- Run a site crawl and filter for pages below 200 words — assess whether they should be consolidated, expanded, or noindexed

---

## Phase 5 — Schema and AI Overviews

### Schema Audit

Check which schema types are implemented and whether they are error-free in Google's Rich Results Test.

**High-impact schema (audit for presence):**
- Product schema with price, availability, and aggregateRating (eCommerce) — confirmed +30% CTR
- BreadcrumbList — confirmed +15% CTR; also aids site structure understanding
- Article / BlogPosting with datePublished and dateModified (content sites)
- SoftwareApplication (B2B SaaS)
- Organization with contact details and sameAs links to social profiles

**Deprecated — safe to keep, no longer generates rich results:**
- FAQPage (deprecated for most sites; only health/government still eligible)
- HowTo (fully phased out for desktop and mobile)

**AI citation note:** Structured data is cited by AI systems (ChatGPT, Gemini, Perplexity) 4× more often than unstructured text. Proper schema implementation directly influences AI Overview inclusion.

### AI Overviews Visibility

AI Overviews now appear on ~30% of US desktop queries. Brands cited in AI Overviews earn **35% more organic clicks** than non-cited brands on the same queries.

**Audit questions:**
- Search 10–15 target queries in an incognito browser — does an AI Overview appear?
- Is Challenger's site being cited in those AI Overviews?
- What content type is being cited (blog post, product page, comparison page)?

**Automated path:** for the 10–15 target queries, use Composio's web search tool to fetch SERP snapshots in parallel rather than checking each manually in incognito. Parse each response for AI Overview presence and citation source. Keeps the audit reproducible across team members.

This informs both the content strategy and schema priorities — content that is cited in AI Overviews tends to have structured data, clear factual statements, and demonstrated E-E-A-T.

---

## Phase 6 — Prioritised Fix List

Organise findings into three tiers:

**Tier 1 — Quick wins (fix in Week 1–2, high impact, low effort):**
- Accidental noindex tags on important pages
- Missing or broken canonical tags
- Missing title tags or duplicate titles on high-traffic pages
- /collections/all or equivalent unblocked (eCommerce)
- Missing self-referencing canonicals

**Tier 2 — Medium-term (fix in Month 1–2, high impact, moderate effort):**
- Core Web Vitals: LCP and INP improvements (image optimisation, script deferral)
- Orphan pages receiving no internal links
- Thin content pages — expand or consolidate
- Schema implementation on product/service pages
- Internal linking to key money pages

**Tier 3 — Strategic (Month 2–6, high impact, high effort):**
- Site architecture restructure (if pages are too deep)
- Topical authority content plan (pillar + cluster build-out)
- E-E-A-T improvements (author pages, original research, case studies)
- Digital PR / link building plan
- AI Overviews optimisation strategy

---

## Phase 7 — Synthesis Brief

Before building the final deliverable, write a brief summary for orchestrator handoff.

**SEO Audit Key Findings**
- Crawl error count and specific pages affected (blocked, noindexed, redirect chains)
- Core Web Vitals status: which metric failing (LCP/INP/CLS), percentage of pages affected, desktop vs mobile
- Top 3 technical fixes ranked by impact (what must be fixed first before anything else can succeed)
- Content gap themes (thin content, missing E-E-A-T signals, staleness patterns across page types)

**Priority for downstream skills:** keyword-research should focus on [e.g., product page optimisation in ecommerce-seo first, then keyword clustering]. Content planning should wait until Core Web Vitals and canonicalisation are cleared.

*If running standalone, share this with the operator before the full deliverable.*

---

## QA Gate

Before delivering the audit:

- [ ] GSC Coverage report reviewed — unexplained excluded pages investigated
- [ ] Core Web Vitals status confirmed (Good/Needs Improvement/Poor) per page type
- [ ] At least 20 key pages audited for title tag, meta, H1, and canonical
- [ ] Schema tested in Google's Rich Results Test for at least one page per type
- [ ] Internal link audit run — at least 3 orphan pages or low-inlink money pages identified
- [ ] AI Overviews checked for 10+ target queries
- [ ] Prioritised fix list tiered (Tier 1/2/3) with effort and impact noted per item
- [ ] Findings deliverable format confirmed — in-conversation summary, DOCX, or PPTX slide → If DOCX or PPTX: read the **[Brand](../../assets/brand-strategy.md)** file before formatting

---

## Reference Files

- `references/audit-framework.md` — Full technical audit checklist with pass/fail criteria, Core Web Vitals diagnosis steps, E-E-A-T scoring rubric, schema audit checklist, and algorithm update impact guide. Required before Phase 2 to ensure consistent checklist coverage.

---

## References

- **[Audit Framework](references/audit-framework.md)** — Full technical audit checklist with pass/fail criteria, Core Web Vitals diagnosis steps, E-E-A-T scoring rubric, schema audit checklist, and algorithm update impact guide.
- **[Brand](../../assets/brand-strategy.md)** — Read when producing any branded output (PPTX, DOCX). Colours, typography, and component patterns.
- **[Keyword Research](../keyword-research/SKILL.md)** — Run after the audit to build the keyword and content strategy on a clean technical foundation.
- **[eCommerce SEO](../ecommerce-seo/SKILL.md)** — Use for Shopify-specific execution of technical fixes identified in the audit.
- **_SEO Reporting (not in this plugin · ask operator)_** — Use after the audit to track ongoing improvements and benchmark progress against the audit baseline.
