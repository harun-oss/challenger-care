# Keyword Research Process — Detailed Walkthrough

Read this at the start of Phase 3 of the Keyword Research skill for the full step-by-step Keyword Planner workflow.

---

## Google Keyword Planner — Full Walkthrough

### Accessing Keyword Planner

Google Ads → Tools → Keyword Planner

Two modes available:
- **Discover new keywords** — used for research (this is what we use)
- **Get search volume and forecasts** — used to check volume for a specific keyword list you already have

### Running a discovery session

1. Click **Discover new keywords**
2. Choose **Start with keywords** (not "Start with a website" — that pulls keywords from a competitor's page, which is useful for competitive research but not for building your own keyword foundation)
3. Enter seed terms — one per line, or comma-separated
4. **Location:** be specific
   - National: "United States"
   - Regional: "Minnesota" or "Minneapolis-Saint Paul, MN"
   - If you enter a national location for a local client, all volume figures will be national — the local market may be a fraction of those numbers
5. **Language:** English (default)
6. Click **Get results**

### Reading the results

| Column | What it tells you |
|--------|------------------|
| Keyword | The suggested keyword |
| Avg. monthly searches | Google's estimate of monthly search volume in the selected location |
| Competition | Advertiser competition (Low/Medium/High) — reflects how many advertisers are bidding, not SEO difficulty |
| Top of page bid (low range) | Estimated CPC for ads showing at the top of page, bottom of the bid range |
| Top of page bid (high range) | Estimated CPC for ads at the top, upper range — the better proxy for intent |
| Three-month change | Whether volume is trending up or down — useful for seasonal businesses |
| YoY change | Year-over-year trend |

### Applying the volume filter

After getting results:
- Click the filter icon → Avg. monthly searches → Greater than or equal to → 30
- This removes keywords with insufficient volume to generate meaningful traffic

**Interpreting the 30-threshold:**
- 30 searches/month = roughly 1 search per day nationally
- For a local market (single city), multiply the national volume by the city's approximate share of national traffic (major cities: 1–3% of national volume)
- Example: "commercial HVAC repair" shows 1,000 national searches/month → estimated 10–20 searches/month in Minneapolis → borderline, but may still be worth including if top-of-page bid is high (commercial intent)

### Running multiple discovery sessions

If Challenger has multiple distinct service lines or product categories, run a separate Keyword Planner session for each theme rather than mixing everything into one run. This keeps the results cleaner and makes ad group structuring easier.

Example (commercial cleaning company):
- Session 1 seeds: office cleaning, commercial cleaning, janitorial services
- Session 2 seeds: post-construction cleanup, construction site cleaning, after renovation cleaning
- Session 3 seeds: medical office cleaning, healthcare facility cleaning, clinic cleaning service

---

## Keyword Volume and Market Size Reality Check

Keyword Planner shows volume estimates, not guarantees. For new accounts, actual impression volume often differs from projections because:

1. **Match type:** Exact match shows ads to a smaller subset of queries than Keyword Planner's estimate (which reflects broad search intent)
2. **Quality Score at launch:** New accounts often start with lower ad positions until Quality Score data accumulates, meaning fewer impressions even for keywords that have volume
3. **Budget constraints:** If the daily budget is reached early in the day, the account stops showing for the rest of the day regardless of keyword volume
4. **Seasonality:** Monthly averages may mask strong seasonal variation — always check the three-month change and YoY change columns for seasonal businesses

**Set realistic expectations with clients:** A keyword showing 500 searches/month at exact match may generate 200–350 impressions/month in a competitive market where the account is competing at position 3–4. Factor this into projection conversations.

---

## Interpreting Top-of-Page Bid as an Intent Signal

Top-of-page bid (high range) is the most reliable intent signal available in Keyword Planner.

**Why it works:**
Advertisers set bids based on the revenue value of conversions. A high bid means advertisers have found that users searching for this keyword convert at a rate that justifies a high cost-per-click. This is a market-tested signal, not an estimate.

**Practical thresholds (rough guidelines — adjust by vertical):**

| Top-of-page bid (high range) | Intent interpretation |
|-----------------------------|----------------------|
| >$20 | Very high commercial intent — these are premium keywords; every one is likely to convert well |
| $10–$20 | High intent — core campaign keywords |
| $5–$10 | Medium-high intent — include with keyword-level tracking |
| $2–$5 | Medium intent — may be good for Phase 2 expansion |
| <$2 | Low intent or low competition — research keywords; often informational |

**Exception:** Some genuinely high-intent keywords have low bids because they're niche, highly local, or underserved by advertisers. Never filter purely on bid — use it as one signal alongside the keyword's actual phrasing.

---

## Handling Multiple Geographic Targets

For clients targeting multiple cities or states:

**Option 1 — Single national campaign (simplest):**
- Target all locations in one campaign
- Location bid adjustments can increase bids in high-priority cities (Google Ads → Campaigns → Locations → Bid adj.)
- Lower operational overhead; harder to isolate performance by market

**Option 2 — Separate campaigns per market (recommended for different budgets or priorities per market):**
- "Client — Non-Branded — Minneapolis"
- "Client — Non-Branded — Chicago"
- Each campaign can have its own budget, bid strategy, and location-specific ad copy
- More complex to manage but gives full performance visibility per market

**Keyword research tip for multi-market:** Run Keyword Planner separately for each target city. Volume in Chicago will differ from Minneapolis. The seed terms may produce different keyword suggestions — some local terms or colloquialisms vary by geography.

---

## Transitioning Match Types Over Time

### Phase 1: Launch (0–30 days) — Exact match only

Every keyword imported as exact match: `[keyword]`

Purpose: maximum control, clean Search Terms data, budget goes only to clearly intentional queries.

### Phase 2: Expansion (30–90 days) — Introduce phrase match

After 30 days, review the Search Terms report. Look for:
- Relevant queries that your exact match keywords are catching — this validates your keywords are working
- Relevant queries that are NOT in your keyword list — these are expansion candidates

For each valuable expansion pattern, add as phrase match: `"keyword"`.

Example: If `[commercial HVAC repair Minneapolis]` is working and the Search Terms report shows people also searching "affordable commercial HVAC repair Minneapolis" and "licensed commercial HVAC repair Minneapolis" — add these as phrase match to catch the variants.

### Phase 3: Broad match (90+ days) — Selective use only

Broad match can expand reach significantly but requires strong negative keyword lists to prevent waste.

**Only introduce broad match when:**
- 90+ days of account data exist
- Negative keyword list has been actively maintained (at least 3 Search Terms reviews completed)
- The account has enough conversion data to assess what's working vs what's wasting budget

**Never introduce broad match on the entire account simultaneously.** Add it to one ad group, monitor for 2 weeks, then expand if the Search Terms data is clean.
