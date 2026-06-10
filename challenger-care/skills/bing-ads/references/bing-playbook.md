# Bing Ads Playbook

## LinkedIn Profile Targeting — Bid Adjustment Recommendations

LinkedIn targeting is Bing's most powerful differentiator over Google. Use it to layer professional audience signals on top of keyword or shopping campaigns for B2B and professional product clients.

### When to Use LinkedIn Targeting

**Use for:**
- B2B and SaaS clients (always — this is a significant advantage over Google)
- High-AOV products where the buyer's profession matters (e.g., professional equipment, premium productivity tools)
- Products targeting specific job functions (e.g., marketing tools targeting marketers, accounting software targeting finance)
- Clients where Bing's older, higher-income demographic is the actual target

**Do not use for:**
- Mass consumer eCommerce with no professional angle
- Low-AOV products where the added CPM uplift won't justify the conversion improvement
- Clients where geo is the primary constraint (the intersection of LinkedIn + geo will shrink reach too far)

### LinkedIn Targeting Dimensions

| Dimension | What it is | Best for |
|-----------|-----------|---------|
| Company | Specific company names | Account-based B2B (large clients with target account lists) |
| Industry | Broad industry vertical (e.g., "Computer Software", "Financial Services") | Most B2B use cases |
| Job Function | Department or function (e.g., "Marketing", "Engineering", "Finance") | B2B tools targeting by department |

**Note:** You cannot combine all three in a single layer without severely shrinking reach. Start with one dimension.

### Recommended Bid Adjustments by Segment

Apply these as **observation** modifiers first (do not restrict — layer on top of the existing audience):

| Segment type | Starting bid adjustment | Review threshold |
|-------------|------------------------|-----------------|
| Top-performing industry (1–3 industries) | +20–30% | After 30 days |
| Top-performing job function | +20–25% | After 30 days |
| Specific high-value company | +30–40% | After 30 days |
| Underperforming segment | -20% | After 30 days |
| Irrelevant segment | Remove from targeting | After 30 days |

**Setup steps:**
1. Microsoft Advertising → select the ad group → Audiences
2. Add "LinkedIn Profile" targeting
3. Select dimension type (start with Industry or Job Function)
4. Set as observation (not targeting) to avoid restricting reach
5. Apply bid modifier at ad group level
6. Review in "Audience" report after 30 days

### Reporting LinkedIn Performance

Pull via: Reports → Audience → LinkedIn Profile Targeting Report

Look for:
- Which industry/job function has the lowest CPA?
- Which segments are generating clicks but no conversions? (Reduce modifier)
- Is the LinkedIn-targeted segment converting at a better rate than the baseline?

If a LinkedIn segment is outperforming the baseline by more than 25%, increase modifier to +40–50% and consider building a dedicated LinkedIn-targeted ad group.

---

## Microsoft Merchant Center — Setup and Feed Troubleshooting

### Merchant Center Account Setup

1. Go to [merchantcenter.microsoft.com](https://merchantcenter.microsoft.com)
2. Sign in with the same Microsoft account linked to the Ads account
3. Create a new store: Store name = Client Name, Store URL = client's domain
4. Verify domain ownership:
   - Option A: Add the provided meta tag to the homepage HTML
   - Option B: Upload an HTML file to the root of the website
   - Option C: Google Analytics verification (if GA is connected to the Microsoft Ads account)
5. After verification, claim the domain

### Connecting Merchant Center to Microsoft Advertising

1. Microsoft Advertising → Tools → Merchant Center Stores
2. Link the verified store to the Ads account
3. The Shopping campaigns will now be able to pull from the product feed

### Product Feed Options

**Option A: Google Merchant Center Import (recommended)**
1. In Merchant Center, go to Feed Management → Import from Google
2. Authorize Google Merchant Center access
3. Select the Google feed to sync
4. Set sync frequency: Daily
5. This keeps Bing feed in sync with the Google feed automatically — no extra maintenance

**Option B: Manual Feed Upload**
1. Prepare a TSV or XML file in Google's product feed format (Bing accepts the same schema)
2. Upload via Merchant Center → Feeds → File upload
3. Set to update daily via scheduled fetch or manual re-upload
4. Required fields: id, title, description, link, image_link, price, availability, condition, brand, gtin/mpn

### Feed Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| "Domain not verified" | URL mismatch between Merchant Center and the product URLs | Ensure all product URLs use the verified domain exactly (including www vs non-www) |
| "Missing required attribute" | Feed is missing a required field | Add the field for all products; gtin is commonly missing — add if available |
| "Invalid price" | Price format issue | Ensure format: `19.99 USD` (space between amount and currency code) |
| "Availability mismatch" | Feed says "in stock" but landing page says "out of stock" | Sync feed update frequency or update feed manually |
| "Disapproved: adult content" | Product triggered adult content policy | Review product description and image; resubmit after changes |
| "Crawl error" | Product URL not accessible by Bing's crawler | Confirm URL is live; check robots.txt isn't blocking Bingbot |
| Feed approved but no Shopping impressions | Campaign not linked to Merchant Center store | Ads account → Shopping campaign → Settings → check store link |

### Shopping Campaign Optimisation

After setup, review Shopping performance monthly:

**Product-level review:**
- Which products have the most impressions but lowest CTR? (Title or image may be weak — test a new title)
- Which products convert well but have low impression share? (Increase bids for those product groups)
- Which products spend budget but never convert? (Exclude from Shopping campaign after 60 days)

**Bid strategy path:**
| Stage | Bid strategy | When to advance |
|-------|-------------|----------------|
| New campaign | Maximize Clicks | 30 days / enough data to see conversion patterns |
| Learning | Maximize Conversions | 30 conv/month |
| Scaled | Target ROAS | Stable ROAS, 30+ conv/month, set below actual ROAS |

---

## Bing vs. Google — Key Differences Quick Reference

| Factor | Bing (Microsoft Advertising) | Google Ads |
|--------|------------------------------|-----------|
| Audience age | Skews 35+ | Broad |
| Device split | Desktop-heavy (~60–70%) | More balanced |
| Average CPC | 20–40% lower for same keywords | Benchmark |
| Match type breadth | Broader — tighten match types more aggressively | More precise |
| Unique feature | LinkedIn profile targeting | Smart Bidding precision |
| Shopping | Microsoft Merchant Center required | Google Merchant Center |
| Conversion tag | Universal Event Tracking (UET) | Google Ads conversion tag |

---

## Common Bing-Specific Gotchas

**1. Broad Match is very broad**
Bing's Broad Match captures significantly more unrelated queries than Google's. On a new import, switch Broad Match keywords to Phrase Match immediately. Review the search term report after 14 days and add negatives aggressively.

**2. Import doesn't transfer negative keyword lists**
Google Ads negative keyword lists (applied at the campaign level) don't import cleanly. After importing, re-check that all campaign-level negatives are applied. Manually re-add the GH standard negative keyword list if used.

**3. Ad extensions may need re-verification**
Sitelinks, callouts, and structured snippets import but may show as "Under Review" in Bing. Allow 24–48 hours. If still under review after 48 hours, edit and resubmit.

**4. Auto-tagging with UTM**
Microsoft Advertising has its own auto-tagging ({msclkid}) which conflicts with UTM parameters if both are used. Use manual UTM parameters only: `utm_source=bing&utm_medium=cpc&utm_campaign={Campaign}&utm_content={AdGroup}`. Disable Microsoft auto-tagging in account settings if using GA4 for cross-channel attribution.

**5. Smart Campaigns vs. Expert Mode**
New accounts default to "Smart Campaigns" (Bing's simplified mode). Always switch to Expert Mode before importing from Google. Smart Campaigns do not support full campaign controls.
