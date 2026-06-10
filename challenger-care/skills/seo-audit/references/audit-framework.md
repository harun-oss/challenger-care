# SEO Audit Framework

## Technical Audit Checklist

### Crawlability and Indexability

| Check | Pass criteria | Tool |
|-------|--------------|------|
| Robots.txt accessible | Returns 200, no critical pages blocked | Browser / Screaming Frog |
| XML sitemap submitted | Listed in GSC with no errors, updated within 30 days | GSC → Sitemaps |
| GSC Coverage: Indexed pages | Count matches expected; no unexplained exclusions | GSC → Indexing → Pages |
| GSC Coverage: Discovered not indexed | Under 5% of total pages | GSC |
| GSC Coverage: Crawled not indexed | Under 3% of total pages | GSC |
| GSC Coverage: Manual actions | Zero | GSC → Security & Manual Actions |
| Noindex tags: intentional only | No important pages accidentally tagged noindex | Screaming Frog crawl |
| JS-rendered content | Critical content visible in Fetch as Google | GSC URL Inspection → Rendered |
| Server response codes | No 5xx errors; 3xx redirects are single-hop, not chains | Screaming Frog |

### Core Web Vitals Thresholds

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP | ≤2.5s | 2.5–4s | >4s |
| INP | ≤200ms | 200–500ms | >500ms |
| CLS | ≤0.1 | 0.1–0.25 | >0.25 |

**75th percentile rule:** 75% of real-world visits must meet "Good" for the page to pass.

**INP context:** Replaced FID on March 12, 2024. Measures all user interactions across the page visit (click, tap, keyboard input). Apps injecting JavaScript globally are the most common INP culprit.

### LCP Diagnosis Steps

1. Run PageSpeed Insights on the URL
2. Identify the LCP element (PSI shows this in the "Opportunities" section)
3. Determine cause:
   - Hero image: Is it compressed? WebP format? `loading="eager"` set?
   - Text block: Is the web font render-blocking? Is the server response slow?
   - Image carousel: Is the first slide the LCP element, but loaded lazily?
4. Check TTFB (Time to First Byte) — if above 600ms, server response is the bottleneck, not the asset

### Canonical Tag Audit Checklist

| URL pattern | Expected canonical | Common issue |
|-------------|-------------------|--------------|
| Clean product URL | Self-referencing | Missing canonical |
| Collection-scoped product URL | Clean product URL | Points to wrong URL |
| Variant URL (`?variant=X`) | Clean product URL | Not implemented |
| Paginated collection (`?page=2`) | Page 1 of collection | Points to self |
| Filtered URL (`?sort_by=X`) | Base collection OR noindex | Not implemented |
| Duplicate content (same content, 2 URLs) | The canonical "preferred" URL | Both pages indexed |

**No canonical chains:** If URL A canonicals to URL B, and URL B canonicals to URL C, Google may ignore all three. Fix: all canonicals should point to the final destination URL.

### Site Architecture Checks

| Check | Pass criteria |
|-------|--------------|
| Homepage to deepest key page | ≤4 clicks |
| Orphan pages | Zero on important pages (all have ≥1 internal link) |
| Breadcrumbs present | On product, collection, and blog post pages |
| Redirects | All single-hop 301s; no redirect loops; no 302 where 301 intended |
| Internal link equity to money pages | Key conversion pages have ≥10 inlinks |

---

## E-E-A-T Scoring Rubric

Score each page from 1–5 across each pillar. Total of 20 = maximum E-E-A-T score.

### Experience (1–5)

| Score | Criteria |
|-------|---------|
| 5 | First-hand experience explicitly stated with specific details (named examples, dates, outcomes) |
| 4 | Implied experience; includes case-specific details that demonstrate familiarity |
| 3 | Some original examples but mostly general information |
| 2 | Mostly synthesised from other sources; no first-hand perspective |
| 1 | Entirely generic; could have been written by anyone with no experience of the topic |

### Expertise (1–5)

| Score | Criteria |
|-------|---------|
| 5 | Author credentials visible and relevant; content uses precise, field-accurate language throughout |
| 4 | Author attributed; content reflects domain knowledge |
| 3 | Content is generally accurate; no expertise signals |
| 2 | Some inaccuracies; generic treatment of the subject |
| 1 | Factual errors, oversimplification, or non-expert language |

### Authoritativeness (1–5)

| Score | Criteria |
|-------|---------|
| 5 | Site is a recognised authority in the space; content cites and is cited by other authority sources |
| 4 | Site has established presence; content links to primary sources |
| 3 | Moderate domain presence; some citations |
| 2 | Little domain authority; few citations |
| 1 | No authority signals; no citations |

### Trustworthiness (1–5)

| Score | Criteria |
|-------|---------|
| 5 | All claims cited; publication and update dates visible; author bio with credentials; transparent about methodology |
| 4 | Most claims cited; dates visible; author attributed |
| 3 | Some citations; author attributed but no credentials |
| 2 | Few citations; dates missing or hidden; anonymous authorship |
| 1 | Unverified claims; no authorship; no dates; no contact information |

**E-E-A-T Score interpretation:**
- 16–20: Strong; maintain
- 11–15: Acceptable; improve Expertise and Experience signals
- 6–10: Needs significant work before this content can compete on high-intent queries
- Under 6: Complete rewrite or removal

---

## Schema Audit Checklist

| Schema type | Check | Tool |
|-------------|-------|------|
| Product (eCommerce) | Required fields present: offers OR review OR aggregateRating | Google Rich Results Test |
| BreadcrumbList | Present on product and collection pages; hierarchy is correct | Rich Results Test |
| Article / BlogPosting | datePublished and dateModified present; author present | Rich Results Test |
| SoftwareApplication (SaaS) | name, description, applicationCategory, operatingSystem | Rich Results Test |
| Organization | name, url, logo, sameAs (social profiles) | Rich Results Test |
| FAQPage | Implemented even if deprecated (AI citation benefit) | Validate syntax only |
| Errors | Zero validation errors in Rich Results Test | Rich Results Test |

**Deprecated schema (no rich results, still implement for AI citation):**
- FAQPage: deprecated for most sites in 2024; only health/government entities still eligible
- HowTo: fully deprecated for all sites in 2024

---

## Algorithm Update Impact Guide

When a traffic drop coincides with a known Google update, use this to diagnose the likely cause:

| Update type | Primary target | Diagnosis signal | Recovery approach |
|-------------|---------------|-----------------|------------------|
| Core Update | Overall quality and relevance | Broad rankings change across many pages and competitors | E-E-A-T improvements; content quality; topical authority build-out |
| Helpful Content (now core) | Low-quality, AI-generated, or unhelpful content | Pages with thin content or low E-E-A-T signals lose most | Rewrite thin content; remove or consolidate low-value pages |
| Link Spam Update | Manipulative link patterns | Sites with unnatural link profiles lose rankings | Disavow toxic links; build editorial links via digital PR |
| Product Reviews | Shallow product reviews | Review pages ranking poorly | Add first-hand experience; testing; unique insights |

**Check the update calendar:** Google publishes confirmed algorithm updates at https://developers.google.com/search/updates/ranking. Cross-reference traffic drops against this calendar before diagnosing.

---

## Prioritised Fix Template

Use this structure when delivering the audit output:

```
TIER 1 — Quick wins (Week 1–2)
[Issue] → [Impact] → [Specific fix]
Example: 4 product pages have accidental noindex tags → lost from Google index → remove noindex from template

TIER 2 — Medium-term (Month 1–2)
[Issue] → [Impact] → [Specific fix]
Example: LCP above 4s on collection pages → confirmed ranking signal → compress hero images to WebP, defer app scripts

TIER 3 — Strategic (Month 2–6)
[Issue] → [Impact] → [Specific fix]
Example: Zero topical authority structure → missing 30% organic traffic from cluster content → build pillar + 5 cluster pages on core topic
```
