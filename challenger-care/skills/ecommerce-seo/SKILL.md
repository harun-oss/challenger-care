---
name: ecommerce-seo
description: Shopify-specific SEO execution · canonical tags, faceted navigation, product page optimisation (title, meta, schema, alt), collection page SEO, breadcrumbs, Core Web Vitals, OOS handling. MANDATORY TRIGGER: any mention of "Shopify SEO", "eCommerce SEO", "product page SEO", "collection page SEO", "Shopify canonical", "Shopify speed", "product schema", "ecommerce site architecture". Do NOT use for: Generic keyword research (use `keyword-research`). Content writing (use `seo-content-writing`).
---

> **Permission tier:** stage · **Tools/context:** assets/brand-strategy.md, assets/team-roles.md, CONFIG.md


# eCommerce SEO

## What this skill does

Covers Shopify-specific SEO from technical foundations to page-level optimisation. eCommerce SEO has unique challenges that general SEO does not — duplicate content from collection/product URL patterns, crawl budget waste from faceted navigation, and Core Web Vitals failures driven by app bloat. This skill addresses all of them.

Use this skill when:
- Auditing or fixing a Shopify store's technical SEO
- Optimising product pages and collection pages
- Diagnosing why high-value pages aren't ranking despite good content
- Planning site architecture for a Shopify store
- Implementing product and breadcrumb schema

---

## Phase 1 — Context

Ask one question at a time:

1. **Store URL and platform** — Shopify (assumed) or another platform? Theme name?
2. **Catalogue size** — how many products and collections?
3. **Current organic status** — confirm `google_search_console` and `google_analytics` connections via Composio (see the live MCP connectors). If connected, the audit will run live pulls in Phase 2 and Phase 6 instead of asking the user for screenshots. If not connected, request screenshots or CSV exports of GSC Coverage, GSC Performance, and Core Web Vitals reports before proceeding. If a specific pull fails mid-audit, ask the user for that specific export rather than producing an audit with gaps.
4. **Known issues** — any specific concerns: slow pages, duplicate content warnings in GSC, index bloat?
5. **Priority** — technical fixes, product page optimisation, collection pages, or all?

---

## Phase 2 — Shopify Technical Audit

### Canonical Tag Audit

Shopify auto-generates canonical tags, but custom themes or modifications frequently break them. Verify every canonical type before assuming they are correct.

**Canonical audit checklist:**

| URL type | Should canonicalize to | How to verify |
|----------|----------------------|---------------|
| `/products/product-handle` | Self (clean product URL) | URL Inspection in GSC |
| `/collections/name/products/product-handle` | `/products/product-handle` | Screaming Frog crawl |
| `?variant=12345` | Clean product URL (no variant param) | URL Inspection in GSC |
| Paginated collection pages | Page 1 of that collection | Crawl + manual check |
| Filtered/sorted collection URLs | The base collection URL | Crawl + GSC Coverage |

**Common finding:** Products in multiple collections often have their collection-scoped URL (`/collections/shirts/products/blue-tee`) indexed alongside the canonical product URL. This splits link equity and can cause ranking instability. Fix: confirm theme is correctly implementing canonical to `/products/` URL only.

### Crawl Budget and Faceted Navigation

Faceted navigation (filtering by colour, size, price, brand) creates thousands of near-duplicate URLs. Each filter combination is a new URL. For a 500-product store with 10 filter options, this can generate 10,000+ crawlable URLs, most of which have zero unique value.

**Impact:** Crawl budget wasted on low-value pages means Google crawls core money pages less frequently. Index bloat from these pages can suppress overall domain quality signals.

**Fix sequence:**
1. Identify faceted URL patterns (typically contain `?filter.`, `sort_by=`, or tag parameters)
2. Add `<meta name="robots" content="noindex, follow">` to all filter/sort combination pages
3. Do NOT use canonical tags to handle faceted navigation — use noindex (Google's recommendation)
4. Block `?sort_by=` parameters in robots.txt if they have no value to users either

**The /collections/all page:**
Shopify creates `/collections/all` by default — a catch-all page listing every product. It has no SEO value and dilutes crawl budget. Add it to robots.txt: `Disallow: /collections/all`

### Pagination

Shopify paginates collections automatically. All paginated pages (`?page=2`, `?page=3`) should have canonical tags pointing to page 1 of the collection — Shopify handles this by default, but verify it is working in your theme.

### Robots.txt and Sitemap

Shopify generates both automatically. Verify:
- `sitemap.xml` lists all published products and collections (exclude draft/archived)
- Robots.txt is not accidentally blocking important directories
- GSC → Sitemaps shows the sitemap is submitted and being read without errors

---

## Phase 3 — Product Page Optimisation

Product pages are transactional-intent pages. They need to rank for "[product name]", "[product name] [brand]", and long-tail variants while clearly communicating value to buyers.

### Title Tag Formula

```
[Product Name] — [Brand]
```

**Examples:**
- `Osprey Kyte 46L Hiking Pack — GearCo` ✓
- `Men's Running Shoes | Free Shipping — ShoeStore` ✗ (generic, keyword too late)

**Rules:**
- 55–60 characters (600px maximum before truncation)
- Product name first, brand last
- Include a key attribute if it fits within the character limit (size, colour, material)
- No keyword stuffing — one clear product focus

### Meta Description Formula

```
[Key benefit/use case]. [Key spec or differentiator]. [CTA]. [Optional: shipping/returns reassurance]
```

**Example:** `Lightweight 46L women's hiking pack with back-panel suspension. Built for overnight trails. Order now — free shipping and 60-day returns.`

**Rules:**
- 155–160 characters
- Include the product name and one key attribute naturally
- Clear CTA ("Order", "Shop", "Get")
- Unique per product — never auto-populate with the first sentence of the product description

### Product Schema (JSON-LD)

Implement on every product page. Product schema with reviews and pricing confirmed +30% CTR.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Product Name]",
  "image": ["[Product image URL]"],
  "description": "[Product description]",
  "sku": "[SKU]",
  "brand": {
    "@type": "Brand",
    "name": "[Brand Name]"
  },
  "offers": {
    "@type": "Offer",
    "url": "[Product page URL]",
    "priceCurrency": "USD",
    "price": "[Price]",
    "priceValidUntil": "[YYYY-MM-DD — 90 days out]",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[Average rating]",
    "reviewCount": "[Number of reviews]"
  }
}
```

**Required fields for rich results:** At least one of: `offers`, `review`, or `aggregateRating`.

**Availability values:** `InStock`, `OutOfStock`, `PreOrder`, `BackOrder`, `LimitedAvailability`, `OnlineOnly`, `Discontinued`

### Image Alt Text

Every product image needs a descriptive alt text — not empty, not "product image", not a keyword dump.

**Formula:** `[Product name] — [key attribute(s)]`

**Examples:**
- `Osprey Kyte 46L hiking pack — back view showing suspension system` ✓
- `hiking pack` ✗ (too vague)
- `best hiking pack for women free shipping overnight delivery` ✗ (keyword stuffing)

### User-Generated Reviews

Product reviews are an active SEO signal — they create ongoing content freshness on the product page, contain natural buyer language that matches long-tail search queries, and directly contribute to E-E-A-T (Experience pillar). Ensure reviews are crawlable (rendered in HTML, not JavaScript-only) and that review schema reflects them.

### Out-of-Stock Product Handling

**Do not delete or 404 an out-of-stock product page.** Deleting a product URL destroys its accumulated PageRank and backlinks. Even a temporary outage can cause ranking loss that takes months to recover.

**Correct approach:**
- Keep the page live with visible disabled buy button
- Update schema: `"availability": "https://schema.org/OutOfStock"`
- Add internal links to similar available products on the page
- If permanently discontinued: 301 redirect to the most relevant product or category — do not 404

---

## Phase 4 — Collection Page Optimisation

Collection pages are the highest-value eCommerce pages for mid-funnel keywords ("women's hiking boots", "premium coffee equipment"). They attract commercial-intent traffic at scale. Yet most Shopify stores have nearly empty collection pages with only a header and a product grid.

### Page Structure

```
H1: [Target keyword — e.g., "Women's Hiking Boots"]
Intro paragraph (35–50 words): Target keyword in first sentence. Why these are worth buying. One key brand differentiator.
[Product grid]
Detailed content section (300–500 words, below grid): 
  - Guide content relevant to the category (buying guide, use-case guidance)
  - Internal links to related collections
  - FAQ relevant to the category
```

The content below the grid is critical — it is what Google reads for topical relevance when the product grid is largely image/price data.

### Internal Linking to Collections

Collection pages rank when they have internal link equity flowing to them. Most Shopify stores concentrate links on the homepage and product pages, leaving collections under-linked.

**Internal linking hierarchy:**
1. **Main navigation:** Top 5–8 collections in the primary nav receive the most consistent link equity
2. **Homepage body links:** Link to key collections from the homepage body text — carries more weight than navigation
3. **Blog posts:** Every blog post should link to at least one relevant collection
4. **Collection descriptions:** Cross-link related collections from each collection's content section

**Rule:** No key collection page should be more than 2 clicks from the homepage.

---

## Phase 5 — Site Architecture

### Depth

Every product and collection page should be reachable within **3–4 clicks from the homepage**. Pages deeper than 4 clicks are crawled less frequently and pass less link equity.

**Ideal Shopify architecture:**
```
Homepage (click 0)
└── Collection (click 1) — e.g., /collections/womens-hiking-boots
    └── Product (click 2) — e.g., /products/osprey-kyte-46
```

Products are naturally 2 clicks from the homepage in a well-structured Shopify store. If they're deeper, the collection hierarchy needs simplification.

### Breadcrumbs

Breadcrumbs serve three SEO functions: they flatten effective site depth, distribute link equity upward to collection pages, and generate breadcrumb-format SERP snippets (confirmed +15% CTR improvement).

Implement `BreadcrumbList` schema on all product pages:

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://store.com"},
    {"@type": "ListItem", "position": 2, "name": "Women's Hiking Boots", "item": "https://store.com/collections/womens-hiking-boots"},
    {"@type": "ListItem", "position": 3, "name": "Osprey Kyte 46L", "item": "https://store.com/products/osprey-kyte-46"}
  ]
}
```

---

## Phase 6 — Core Web Vitals for Shopify

The median Shopify store LCP is **4.2 seconds** — well above Google's 2.5s "Good" threshold. Improving CWV on Shopify is almost always an app and image issue, not a fundamental architecture problem.

### INP Note

INP replaced FID on March 12, 2024. It measures all interactions throughout a page visit (not just the first), making it significantly more demanding. Apps that inject JavaScript globally are the primary INP culprit on Shopify.

### Diagnostic Process

1. Run the URL in **PageSpeed Insights** — note LCP, INP, and CLS scores for both mobile and desktop
2. Check **GSC → Core Web Vitals** for site-wide patterns (are issues on product pages, collection pages, or all pages?) — auto-pulled via Composio when connected; see the live MCP connectors
3. Use Chrome DevTools Performance tab to identify the largest contentful element (usually the hero image or first product image)

### Common Fixes (by impact)

| Issue | Impact | Fix |
|-------|--------|-----|
| Unoptimised hero/product images | LCP — high | Compress to WebP, add explicit width/height attributes, use `loading="eager"` on above-the-fold images |
| App JavaScript loading globally | INP + LCP — high | Audit every installed app; remove unused apps; restrict app JS to pages where it's needed |
| Third-party scripts (chat, reviews, pixels) | LCP + INP — medium | Defer or lazy-load third-party scripts that aren't needed on initial load |
| Render-blocking CSS/JS | LCP — medium | Minify; defer non-critical scripts |
| Slow server response (TTFB >600ms) | LCP — medium | Shopify's CDN is generally fast; TTFB issues usually come from a slow app making server-side requests |
| Unstable layout elements | CLS — medium | Set explicit dimensions on images, embeds, and ad units; avoid inserting content above existing elements |

**Theme recommendation:** Shopify's native themes (Dawn, Ride, Taste) are optimised for CWV. Third-party themes vary widely — check performance before recommending a new theme purchase.

---

## Phase 7 — Synthesis Brief

Before building the final deliverable, write a brief summary for orchestrator handoff.

**eCommerce SEO Key Findings**
- Canonical architecture issues: which URL types are broken (collection-scoped vs clean product URLs, variant parameters, paginated pages) and impact scope
- Faceted navigation problems: number of unnecessary filter combinations indexed, estimated crawl budget waste, fix recommendations
- Schema gaps: which product pages lack schema, which collection pages lack breadcrumb/product schema, impact on rich results eligibility
- Category page priority list: ranked by organic opportunity (search volume x difficulty x current ranking position) for content expansion

**Priority for downstream skills:** ecommerce-seo must resolve canonical and faceted navigation issues before keyword-research begins. Then product/collection page optimisation can proceed. Core Web Vitals improvements enable better rankings across all pages after technical foundation is cleared.

*If running standalone, share this with the operator before the full deliverable.*

---

## QA Gate

Before delivering eCommerce SEO recommendations or confirming fixes:

- [ ] Canonical audit complete — product pages, collection-scoped URLs, variant URLs, paginated pages
- [ ] /collections/all confirmed blocked or noindexed
- [ ] Faceted navigation URLs confirmed noindexed
- [ ] At least 10 product pages audited: title tag, meta description, schema, image alt text
- [ ] At least 5 collection pages audited: H1, intro content, internal linking, schema
- [ ] Core Web Vitals status confirmed (PageSpeed Insights, mobile and desktop)
- [ ] Top INP/LCP culprits identified (app JS? images? third-party scripts?)
- [ ] BreadcrumbList schema specified for product pages
- [ ] Out-of-stock handling policy confirmed

---

## Reference Files

- `references/ecommerce-playbook.md` — Full Shopify technical audit checklist, product schema JSON-LD templates, collection page content templates, site architecture decision trees, and Core Web Vitals Shopify-specific diagnostic guide. Required for Phase 2 audit, Phase 3 product page schema, and Phase 4 collection page templates.

---

## References

- **[eCommerce SEO Playbook](references/ecommerce-playbook.md)** — Full Shopify technical audit checklist, product schema JSON-LD templates, collection page content templates, site architecture decision trees, and Core Web Vitals Shopify-specific diagnostic guide.
- **[Brand](../../assets/brand-strategy.md)** — Read before producing any DOCX or markdown deliverable. Contains colours, typography, and component patterns for branded output.
- **[SEO Audit](../seo-audit/SKILL.md)** — Use for the full technical audit that feeds into this skill's execution work.
- **[Keyword Research](../keyword-research/SKILL.md)** — Use to determine which collection pages and product categories to prioritise for SEO investment.
