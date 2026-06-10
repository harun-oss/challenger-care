# eCommerce SEO Playbook

## Full Shopify Technical Audit Checklist

### Section 1 — Crawlability and Indexation

| Check | Pass criteria | How to verify |
|-------|--------------|---------------|
| robots.txt accessible | Returns 200; no important directories accidentally blocked | Browser: yoursite.com/robots.txt |
| sitemap.xml submitted | Listed in GSC Sitemaps; no errors; updated within 30 days | GSC → Indexing → Sitemaps |
| sitemap content | Lists all published products, collections, blog posts; excludes drafts/archived | View sitemap source + count vs live pages |
| GSC Coverage: Indexed | Count matches expected published pages | GSC → Indexing → Pages |
| GSC Coverage: Discovered not indexed | Under 5% of total pages | GSC → Indexing → Pages |
| GSC Coverage: Crawled not indexed | Under 3% of total pages | GSC → Indexing → Pages |
| Manual actions | Zero | GSC → Security & Manual Actions |
| /collections/all | Blocked in robots.txt or noindexed | Browser: yoursite.com/collections/all |
| Faceted navigation URLs | All ?filter.* and sort_by= URLs have noindex tag | Screaming Frog crawl |
| Paginated collection pages | Canonical points to page 1 of collection | URL Inspection in GSC |
| Variant URLs | ?variant=X canonicals to clean product URL | URL Inspection for 5 sample variant URLs |
| Collection-scoped product URLs | /collections/name/products/handle canonicals to /products/handle | Screaming Frog crawl |
| Internal search URLs | ?q= and search result pages blocked | robots.txt + crawl check |
| Noindex: intentional only | No important pages accidentally tagged noindex | Screaming Frog: filter by noindex |

### Section 2 — Technical Health

| Check | Pass criteria | How to verify |
|-------|--------------|---------------|
| HTTPS | All pages served over HTTPS; no mixed content | Browser console; SSL checker |
| HTTP → HTTPS redirects | HTTP version 301s to HTTPS; single hop | Browser; redirect checker |
| www vs non-www | One version canonical; the other 301s to preferred | Browser both versions |
| Redirect chains | No chains (A→B→C); all hops are single 301s | Screaming Frog → Redirect Chains |
| 404 errors | Zero on important pages; soft 404s resolved | GSC → Indexing → Not Found (404) |
| Server response time (TTFB) | Under 600ms | PageSpeed Insights → TTFB |
| Broken internal links | Zero | Screaming Frog crawl → Response Codes |
| Duplicate H1 tags | No two pages share an H1 | Screaming Frog → H1 column |
| Orphan pages | All important pages have ≥1 internal link | Screaming Frog → orphan pages report |

### Section 3 — Core Web Vitals (Shopify-specific)

| Metric | Good threshold | Shopify median | Common cause |
|--------|---------------|----------------|-------------|
| LCP | ≤2.5s | ~4.2s | Unoptimised hero/product images |
| INP | ≤200ms | Varies | App JavaScript injected globally |
| CLS | ≤0.1 | Varies | Images without dimensions, app injections |

**75th percentile rule:** 75% of real-world page visits must pass "Good" for the metric to be considered passing. A page that loads fast for 60% of visitors is still failing.

**Diagnosis order:**
1. Run home, top collection, and top product page through PageSpeed Insights (mobile AND desktop separately)
2. Check GSC → Experience → Core Web Vitals for site-wide patterns
3. For LCP: identify the LCP element in PSI; determine if TTFB or asset is the bottleneck
4. For INP: check Chrome DevTools Performance tab; look for long tasks (>50ms) in the main thread
5. For CLS: use Cumulative Layout Shift diagnostic in PSI; look for injected elements above content

---

## Product Schema JSON-LD Templates

### Standard In-Stock Product

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Osprey Kyte 46L Hiking Pack",
  "image": [
    "https://www.gearco.com/cdn/shop/products/kyte-46-front.jpg",
    "https://www.gearco.com/cdn/shop/products/kyte-46-back.jpg"
  ],
  "description": "Lightweight 46L women's hiking pack with adjustable back-panel suspension. Built for overnight trails and multi-day hikes.",
  "sku": "OSP-KYTE46-BLK",
  "brand": {
    "@type": "Brand",
    "name": "Osprey"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.gearco.com/products/osprey-kyte-46",
    "priceCurrency": "USD",
    "price": "229.95",
    "priceValidUntil": "2025-09-30",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "seller": {
      "@type": "Organization",
      "name": "GearCo"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.7",
    "reviewCount": "143",
    "bestRating": "5",
    "worstRating": "1"
  }
}
```

### Out-of-Stock Product (keep page live — do NOT delete)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Osprey Kyte 46L Hiking Pack — Black",
  "sku": "OSP-KYTE46-BLK",
  "offers": {
    "@type": "Offer",
    "priceCurrency": "USD",
    "price": "229.95",
    "availability": "https://schema.org/OutOfStock",
    "itemCondition": "https://schema.org/NewCondition"
  }
}
```

Add to the page alongside the out-of-stock schema:
- Visible disabled "Add to Cart" button (don't hide the page's purchase intent)
- "Notify me when back in stock" email capture
- Internal links to 3 similar available products: "You might also like..."

### Product with Multiple Variants (use Offer for each)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Running Shoe Model X",
  "offers": [
    {
      "@type": "Offer",
      "name": "Size 8 / Black",
      "sku": "RSX-8-BLK",
      "price": "129.99",
      "priceCurrency": "USD",
      "availability": "https://schema.org/InStock"
    },
    {
      "@type": "Offer",
      "name": "Size 9 / Black",
      "sku": "RSX-9-BLK",
      "price": "129.99",
      "priceCurrency": "USD",
      "availability": "https://schema.org/OutOfStock"
    }
  ]
}
```

Note: The canonical URL for ALL variant URLs (`?variant=12345`) should point to the clean product URL. The schema above goes on the clean product URL.

### BreadcrumbList Schema (required on all product pages)

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.gearco.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Women's Hiking Packs",
      "item": "https://www.gearco.com/collections/womens-hiking-packs"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Osprey Kyte 46L",
      "item": "https://www.gearco.com/products/osprey-kyte-46"
    }
  ]
}
```

**CTR impact:** Breadcrumb-format SERP snippets have a documented +15% CTR improvement vs standard URL display. One client saw a 40% CTR drop after a theme update removed breadcrumb schema — recovering it restored performance within 6 weeks.

---

## Collection Page Content Templates

Most Shopify collection pages are empty: a header, a product grid, and nothing else. Google reads nearly zero text content on these pages and has no basis to rank them for mid-funnel keywords.

The fix is not just "add content." The content must be structured to serve the reader first, then Google.

### Template — Women's Hiking Boots Collection Page

```html
<!-- H1 — target keyword exactly or near-exactly -->
<h1>Women's Hiking Boots</h1>

<!-- Intro paragraph: 35–50 words, keyword in first sentence -->
<p>
  Our women's hiking boots are built for trails from day hikes to week-long expeditions. 
  Waterproof, lightweight, and fitted for a narrower last — browse the full range below, 
  with options for low, mid, and high-cut profiles.
</p>

<!-- [Product grid loads here] -->

<!-- Below-the-fold content: 300–500 words -->
<div class="collection-content">
  <h2>How to Choose Women's Hiking Boots</h2>
  <p>
    The right boot depends on three factors: terrain, load, and foot width. Here's 
    how to think through each before buying...
  </p>
  
  <!-- Guide content: use-case based, not keyword-stuffed -->
  
  <h2>Related Categories</h2>
  <!-- Internal links to adjacent collections -->
  <ul>
    <li><a href="/collections/womens-trail-runners">Women's Trail Running Shoes</a></li>
    <li><a href="/collections/waterproof-hiking-boots">Waterproof Hiking Boots</a></li>
    <li><a href="/collections/hiking-socks">Hiking Socks</a></li>
  </ul>
  
  <h2>Frequently Asked Questions</h2>
  <!-- FAQ targeting PAA questions for "women's hiking boots" -->
  <div itemscope itemtype="https://schema.org/FAQPage">
    <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
      <h3 itemprop="name">What's the difference between hiking boots and trail runners?</h3>
      <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
        <p itemprop="text">
          Hiking boots offer more ankle support and are better for heavy loads and 
          technical terrain. Trail runners are lighter and better for established 
          trails and day hikes with minimal pack weight...
        </p>
      </div>
    </div>
  </div>
</div>
```

### Content length guidelines

| Collection size | Recommended content length |
|----------------|--------------------------|
| Under 20 products | 150–300 words below grid |
| 20–100 products | 300–500 words below grid |
| Over 100 products | 500–700 words below grid (sub-category faceting more important) |

**Caution:** Do not stuff the same paragraph with 15 keyword variations. Google's spam detection specifically looks for keyword density patterns. Write for the reader; the keywords will occur naturally.

---

## Site Architecture Decision Trees

### Decision Tree 1 — How Many Navigation Levels?

```
Catalogue size?
├── Under 50 products
│   └── Single-level: Homepage → Products
│       No collections needed (or 2–3 max)
├── 50–300 products  
│   └── Two-level: Homepage → Collections → Products
│       5–15 collections in main nav
│       Each collection: 10–30 products
└── 300+ products
    └── Three-level: Homepage → Top-level categories → Sub-collections → Products
        Example: Hiking → Women's Hiking → Women's Hiking Boots
        Max depth: Product pages at click 3 from homepage
```

### Decision Tree 2 — Should This Get Its Own Collection Page?

```
Does this grouping have search demand?
├── No (no one searches "[this group] + buy/shop")
│   └── Don't create a separate collection; cross-link from content instead
└── Yes (e.g., "waterproof hiking boots" gets 2,400 searches/month)
    ├── Are there at least 6 products that fit this grouping?
    │   ├── Yes → Create the collection page
    │   └── No → Wait until you have 6+ products; use a filtered URL in the meantime
    └── Already covered by an existing collection?
        ├── Yes → Add it as a filter/facet, not a separate URL
        └── No → Create the collection with unique H1 and content
```

### Decision Tree 3 — What to Do with Out-of-Stock Products

```
Is the product temporarily out of stock?
├── Yes (restocking within 90 days)
│   ├── Keep page live
│   ├── Update schema: "availability": "OutOfStock"
│   ├── Add "notify me" email capture
│   └── Add internal links to similar available products
└── No (permanently discontinued)
    ├── Does the product have backlinks or significant PageRank?
    │   ├── Yes → 301 redirect to most relevant product or collection
    │   └── No, few/no backlinks → 301 redirect still preferred; 404 loses any residual equity
    └── Is there a product that directly replaces it?
        ├── Yes → 301 redirect to the replacement product
        └── No → 301 redirect to the collection it belonged to
```

**Key rule:** Never 404 a product that had organic traffic or backlinks. The PageRank accumulated by that URL is permanently destroyed by a 404. A 301 redirect to the most relevant available page preserves that equity.

---

## Core Web Vitals — Shopify-Specific Diagnostic Guide

### Phase 1: Identifying the Problem

**Step 1 — Run PageSpeed Insights (PSI)**
URL: https://pagespeed.web.dev
Run separately for:
- Homepage (brand authority + first impression)
- Top collection page (highest organic traffic driver)
- Top product page (conversion page)
Run each on both mobile AND desktop — Google uses mobile scores for ranking signals.

**Step 2 — Identify the LCP element**
PSI shows the LCP element in the "Opportunities" section. Common LCP elements in Shopify:
- Hero image (homepage, collection page)
- First product image in the grid (collection page)
- Main product image (product page)
- Text block (if images are deferred but text is large)

**Step 3 — Check GSC for site-wide patterns**
GSC → Experience → Core Web Vitals
Look for: which page types are failing (product pages? collection pages? all pages?)
If all page types fail: global JavaScript injection (apps) is the likely culprit
If only product pages fail: product image handling or product-specific app scripts

### Phase 2: LCP Fix Sequence

| Root cause | Diagnosis signal | Fix |
|-----------|-----------------|-----|
| Hero image unoptimised | PSI shows large image as LCP element; image is JPEG or PNG above 200KB | Convert to WebP; compress to under 100KB; serve via Shopify's CDN with `?width=` param |
| Hero image lazy-loaded | PSI: render-blocking; image marked `loading="lazy"` | Change `loading="lazy"` to `loading="eager"` for the first image above the fold only |
| Hero image no explicit dimensions | CLS related | Add `width` and `height` attributes to all `<img>` tags |
| Slow TTFB (>600ms) | PSI shows TTFB in yellow or red | Identify which app is making server-side requests; common culprits: review apps, inventory apps, live-chat with server-side initialisation |
| Render-blocking third-party scripts | PSI flags render-blocking resources | Defer non-critical scripts: `<script defer src="...">` or load after `DOMContentLoaded` |

### Phase 3: INP Fix Sequence (apps are the #1 culprit)

**Audit installed apps:**
1. Go to Shopify Admin → Apps
2. List every installed app
3. For each app: does it inject JavaScript on pages where it isn't needed?
4. Identify apps loading globally (on all pages) vs. only where needed

**The INP app audit:**
```
For each installed app:
├── Is it actively used on this store?
│   └── No → Uninstall (dormant apps still load their scripts)
├── Does it inject JavaScript on product pages?
│   └── Only needed on checkout/cart → restrict to those pages
├── Does it have a "defer loading" option in app settings?
│   └── Yes → Enable it
└── Does it have known INP issues?
    └── Check the app's reviews/changelog for performance mentions
```

**Typical INP offenders (2024–2025):**
- Review apps that load full scripts on every page load
- Live chat widgets loading immediately on page
- Size chart apps running JavaScript globally
- Loyalty/rewards apps initialising on product pages
- Wishlist apps running global event listeners

**Fix path:** Contact the app developer. If the app cannot be configured to load only where needed, evaluate whether the feature justifies the INP cost. For most stores, a 50ms INP improvement is worth more in organic traffic than any single app feature.

### Phase 4: CLS Fix Sequence

Common CLS causes on Shopify:
1. **Images without dimensions:** Add `width` and `height` to all `<img>` tags. Shopify's CDN supports responsive sizing via `?width=X&height=Y` parameters.
2. **App-injected banners/bars:** Apps that inject announcement bars or cookie consent banners above the header. These push content down as they load.
3. **Font swaps:** Web fonts loading and causing text reflow. Use `font-display: swap` with `<link rel="preload">` for critical fonts.
4. **Late-loading embeds:** Embedded social content, YouTube iframes without fixed dimensions.

### Shopify theme performance baseline

| Theme type | Typical PSI mobile score | Recommendation |
|-----------|------------------------|----------------|
| Shopify native (Dawn, Ride, Taste, Craft) | 60–85 | Start here; most optimisable |
| Popular third-party (Prestige, Impulse, etc.) | 40–65 | Varies; run PSI before committing |
| Heavily customised legacy themes | 20–50 | May require rebuild; evaluate cost vs performance gain |
| Custom headless (Hydrogen) | 70–95 | Highest potential; highest implementation cost |

**Recommendation for new stores or theme changes:** Always run PSI on a staging version before pushing a new theme to production. Theme purchases are not refundable after significant customisation.
