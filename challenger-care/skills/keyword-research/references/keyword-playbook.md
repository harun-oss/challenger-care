# Keyword Research Playbook

## Keyword Clustering Methodology — Worked Example

Clustering groups keywords by shared SERP results, not just semantic similarity. Two keywords belong in the same cluster when Google shows them the same (or largely overlapping) pages. This is the most reliable way to determine whether to target keywords on one page or separate pages.

### Step-by-step clustering process

**Step 1 — Seed keyword list**
Start with 50–200 keywords from a combination of:
- GSC queries (existing rankings, even low-position ones)
- Ahrefs/Semrush "Matching terms" report for 3–5 seed terms
- Competitor keyword gaps (their rankings, your non-rankings)
- Customer language from reviews, support tickets, survey responses

**Step 2 — Pull SERP overlap data**
For each keyword, note the top 3 ranking URLs. Keywords sharing 2+ of the same top-3 URLs belong in the same cluster.

Manual approach for small lists (under 50 keywords): open each keyword in incognito, note the first 3 organic results.

Tool approach: Ahrefs "Clusters" feature, Semrush Keyword Manager, or Keyword Cupboard all automate SERP overlap clustering.

**Step 3 — Name each cluster and assign a pillar page**
Each cluster needs one primary page (the pillar) that targets the highest-volume keyword. Supporting pages target sub-queries in the same cluster.

**Step 4 — Assign intent to each cluster**
See intent classification table below. A cluster should have a single dominant intent — if keywords within a cluster split across intent types, split them into separate clusters.

**Worked example — CRM software niche:**

| Cluster | Keywords | Intent | Page type |
|---------|----------|--------|-----------|
| CRM basics | "what is crm", "crm definition", "crm explained" | Informational | Blog post / guide |
| CRM comparison | "best crm software", "top crm tools 2025", "crm comparison" | Commercial | Comparison landing page |
| CRM for startups | "crm for small business", "startup crm", "affordable crm" | Commercial | Landing page with intent-specific angle |
| Salesforce alternatives | "salesforce alternatives", "salesforce competitors", "cheaper than salesforce" | Commercial | Alternatives comparison page |
| Klaviyo vs Salesforce | "Klaviyo vs salesforce", "Klaviyo or salesforce" | Commercial | Head-to-head comparison |
| CRM pricing | "crm pricing", "crm software cost", "how much does crm cost" | Commercial/Transactional | Pricing page or comparison |
| CRM setup | "how to set up crm", "crm implementation guide" | Informational | How-to guide |

Each cluster = one page. Targeting all of these on a single "CRM page" would result in intent mismatch and failure to rank for any of them.

---

## Priority Scoring Formula — Example Spreadsheet

Score each cluster from 0–10 on each dimension, then apply the weighted formula:

**Formula:** `(Volume × 0.3) + (Intent × 0.3) + (Competition × 0.2) + (Relevance × 0.2)`

### Scoring each dimension (0–10)

**Volume score:**
| Monthly searches | Score |
|-----------------|-------|
| 10,000+ | 10 |
| 5,000–9,999 | 8 |
| 1,000–4,999 | 6 |
| 500–999 | 4 |
| 100–499 | 2 |
| Under 100 | 1 |

**Intent score:**
| Intent type | Score |
|------------|-------|
| Transactional (ready to buy) | 10 |
| Commercial (comparing, evaluating) | 8 |
| Informational (learning) | 5 |
| Navigational (brand lookup) | 2 |

**Competition score (inverse of difficulty):**
| Keyword Difficulty (Ahrefs) | Score |
|---------------------------|-------|
| Under 20 | 10 |
| 20–34 | 8 |
| 35–49 | 6 |
| 50–64 | 4 |
| 65–79 | 2 |
| 80+ | 0 |

**Relevance score:**
| Relevance to core offering | Score |
|--------------------------|-------|
| Directly converts to core product/service | 10 |
| Adjacent — converts to secondary offering | 7 |
| Content marketing — topical authority value | 5 |
| Tangential — brand awareness only | 2 |

**Worked example — "best crm for startups" cluster:**
- Volume: 2,400/month → Score 6
- Intent: Commercial → Score 8
- Competition: KD 38 → Score 6
- Relevance: Core offering → Score 10

Priority score: (6 × 0.3) + (8 × 0.3) + (6 × 0.2) + (10 × 0.2) = 1.8 + 2.4 + 1.2 + 2.0 = **7.4/10**

**BOFU override:** For SaaS and service businesses, any keyword with transactional intent and direct relevance to the core offering gets elevated to Tier 1 regardless of volume. A 200-search/month "[competitor] alternative" query that converts at 15% is more valuable than a 10,000-search/month informational query that never converts.

---

## SERP Feature → Intent Decision Table

| SERP feature | What it signals | Content format to match |
|-------------|-----------------|------------------------|
| Featured Snippet (paragraph) | Informational — question or definition | Article with direct 40–60 word answer in first section |
| Featured Snippet (list) | Informational — process or ranking | Numbered or bulleted guide |
| Featured Snippet (table) | Commercial/informational — comparison | Article with comparison table |
| People Also Ask (PAA) | Informational sub-questions | Each PAA is a potential H2 or FAQ |
| Shopping results | Transactional — product purchase intent | Product page or category page (not a blog post) |
| Local Pack | Local transactional intent | Local landing page with NAP schema |
| Image Pack | Visual intent | Image-rich content with descriptive alt text |
| Video Carousel | Visual/instructional | Embed video or create video content alongside text |
| AI Overview (informational) | High-volume informational | Structure content for AI citation (FAQ schema, direct answers) |
| AI Overview (commercial) | Consideration phase | Neutral comparison content with structured data |
| Sitelinks | Navigational | Ensure homepage and key pages are well-structured |
| News results | Trending/timely | Timely content updated frequently |

**Key rule:** If the top 3 organic results are all product or category pages, Google has classified the query as transactional. Do not publish a blog post for that keyword — it will not rank. Publish a transactional page or it will not compete.

---

## AI Overviews Keyword Classification Guide

Not all keywords are equally affected by AI Overviews. Understanding which keywords trigger AI Overviews — and which don't — shapes keyword prioritisation strategy for 2024–2025.

### Trigger rates by query type

| Query type | AI Overview trigger rate | CTR impact | Strategy |
|-----------|-------------------------|------------|---------|
| Informational questions ("how to", "what is", "why does") | ~57.9% | −61% CTR when AIO present | Optimise for AIO citation; also worth ranking #1 for the 40% without AIO |
| Comparison queries ("X vs Y", "best X") | ~20–25% | −35–45% CTR | Include structured comparison tables; aim for AIO citation |
| Shopping/product queries ("buy X", "X price") | ~3.2% | Minimal | Low AIO risk; focus on traditional organic ranking |
| Brand navigational ("X brand website") | <5% | Minimal | Low AIO risk; focus on branded awareness |
| Local queries ("X near me") | <10% | Minimal | Low AIO risk; Local Pack matters more |
| Technical/professional queries | ~15–25% (varies) | −20–40% CTR | AIO citation possible; structured data helps |

### AI Overviews citation signals (what gets cited)

Based on observed patterns, pages cited in AI Overviews tend to share these characteristics:
1. Direct, concise answers to the query question (40–60 words) appearing early in the content
2. Structured data present (FAQ, HowTo, Article schema — even if deprecated for rich results)
3. Numbered or bulleted lists that directly answer sub-questions
4. High E-E-A-T signals: author credentials, cited sources, update dates
5. Clean HTML structure — AI systems parse structured text more reliably than JavaScript-rendered content

**The AIO visibility opportunity:** Brands cited in AI Overviews receive 35% more organic clicks than brands ranking #1 without AIO citation on the same query. For informational content, AIO citation is now a more valuable outcome than position #1 in traditional results.

### Keyword exclusion criteria for AI Overview risk

Flag keywords with high AIO exposure as requiring a different strategy:
- Pure informational queries with exact-match question format (highest AIO rate)
- "Definition" or "meaning" queries (nearly always AIO)
- General "how to" queries on non-technical topics

For these, either:
a) Optimise explicitly for AIO citation (rather than just organic ranking)
b) De-prioritise and focus budget on lower-AIO keywords (commercial, transactional)
c) Approach from a more specific, experiential angle that generic AI answers can't replicate

---

## Tools Comparison: Ahrefs vs Semrush vs Google Search Console

| Feature | Ahrefs | Semrush | Google Search Console |
|---------|--------|---------|----------------------|
| Keyword volume data | ✓ (reliable) | ✓ (reliable) | ✓ (actual clicks/impressions, most accurate) |
| Keyword difficulty | ✓ (link-based) | ✓ (link + content factors) | ✗ |
| Keyword clustering | ✓ (built-in) | ✓ (Keyword Manager) | ✗ |
| SERP feature tracking | ✓ | ✓ | Partial (limited) |
| AI Overview detection | Partial | ✓ (separate tracking) | ✗ |
| Competitor keyword gaps | ✓ (Content Gap) | ✓ (Keyword Gap) | ✗ |
| Actual query data | ✗ (estimated) | ✗ (estimated) | ✓ (only your site) |
| Backlink data | ✓ (best in class) | ✓ (good) | ✗ |
| Content Gap analysis | ✓ | ✓ | ✗ |
| Rank tracking | ✓ | ✓ | Partial (average position) |
| Best for | Link-focused audits, backlink research | All-in-one including PPC | Truth check on own rankings |

**Recommended combination:**
- Use GSC for ground truth on what you actually rank for (not estimates)
- Use Ahrefs or Semrush for competitor research and new keyword discovery
- Cross-reference volume estimates: if Ahrefs and Semrush diverge significantly, the true volume is usually between the two

---

## Industry-Specific Keyword Benchmarks

### eCommerce (Shopify / DTC)

| Category | Typical keyword type | Avg. KD | Avg. volume | Priority |
|---------|---------------------|---------|-------------|---------|
| Brand + product | "[Brand] [Product Name]" | 10–30 | 100–5,000 | Very High |
| Category transactional | "buy [category]", "[category] for sale" | 30–60 | 500–20,000 | High |
| Category commercial | "best [category]", "top [product type]" | 40–70 | 1,000–50,000 | High |
| Comparison | "[Brand A] vs [Brand B]" | 20–50 | 200–10,000 | High |
| Gift/occasion | "[product] gift ideas", "[occasion] gifts" | 20–50 | 500–50,000 | Seasonal |
| Problem/solution | "how to [problem product solves]" | 15–45 | 500–30,000 | Medium |
| Review | "[product] review" | 15–40 | 100–5,000 | Medium |

### SaaS / B2B

| Category | Typical keyword type | Avg. KD | Priority |
|---------|---------------------|---------|---------|
| Direct brand | "[Brand] login", "[Brand] pricing" | 5–20 | Very High (brand protection) |
| BOFU alternatives | "[Competitor] alternatives", "best [category] software" | 40–75 | Very High |
| BOFU comparison | "[Competitor] vs [Brand]" | 20–50 | Very High |
| Use case | "[Software category] for [industry/role]" | 25–55 | High |
| Integration | "[Tool A] [Tool B] integration" | 10–30 | High |
| Problem-aware | "how to [problem software solves]" | 20–50 | Medium (TOFU) |
| Category educational | "what is [software category]" | 30–60 | Low (TOFU/awareness only) |

**SaaS prioritisation principle:** A 300-search/month "[Competitor] alternative" query with 15% conversion rate produces more revenue than a 30,000-search/month "what is [software category]" query with 0.1% conversion. Always weight BOFU keywords above their raw volume suggests.

### Service Business / Agency

| Category | Typical keyword type | Priority |
|---------|---------------------|---------|
| Service + location | "[Service] [City]", "[Service] [City] agency" | Very High |
| Service type | "[Specific service type]", "[niche] [service]" | High |
| Industry + service | "[Industry] [Service]" | High |
| Pricing | "[Service] pricing", "how much does [service] cost" | High |
| Problem-aware | "how to [solve business problem]" | Medium |
| Authority content | "[Industry] trends", "[Topic] guide for [audience]" | Low–Medium |

---

## Topical Authority Cluster Template

Use this template to map a topical authority cluster before building content.

```
TOPICAL CLUSTER: [Core topic]
Pillar page target keyword: [Primary keyword — highest volume, broadest intent]
Pillar page URL: /[slug]

CLUSTER PAGES (supporting):
1. [Sub-topic keyword] → /[slug] | Intent: [I/C/T] | Priority: [H/M/L]
2. [Sub-topic keyword] → /[slug] | Intent: [I/C/T] | Priority: [H/M/L]
3. [Sub-topic keyword] → /[slug] | Intent: [I/C/T] | Priority: [H/M/L]
4. [Sub-topic keyword] → /[slug] | Intent: [I/C/T] | Priority: [H/M/L]
5. [Sub-topic keyword] → /[slug] | Intent: [I/C/T] | Priority: [H/M/L]

INTERNAL LINKING PLAN:
- Pillar links to: all cluster pages (in body content, not just footer)
- Cluster pages link to: pillar page (in intro or first H2) + 2–3 adjacent cluster pages
- Anchor text: exact or near-match target keyword of destination page

CONTENT PUBLISHING ORDER:
1. Publish pillar page first (establishes the hub)
2. Publish BOFU cluster pages next (immediate revenue impact)
3. Publish TOFU cluster pages (topical authority build)
4. Update pillar with links to each cluster page as published

EXPECTED TIMELINE:
- Pillar + first 2 cluster pages: Week 1–2
- Rankings movement typically visible: Month 3–4
- Full cluster authority established: Month 6–9
```

**Benchmark:** Pillar + 5 cluster pages strategy has produced +30% organic traffic, 2.5× longer ranking longevity, and +23% visibility gain vs. isolated page publishing in documented case studies.
