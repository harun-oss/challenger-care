# Campaign Structure Guide — Full Rationale and Variants

## The Account Structure Philosophy

Challenger's account structure is built around one principle: **concentrate data to accelerate algorithm learning.**

The Meta algorithm learns from conversion events. The more conversions flow through a single campaign structure, the faster and more confidently it can optimise. Fragmented structures (many campaigns, small budgets per campaign) slow this process.

Standard structure:
1. **1 Main Campaign** — all DCT experiments + legacy winners
2. **1 DPA Campaign** (eCommerce only, 30+ days) — ~10% of budget
3. **1 ADV+ Campaign** (60–90+ days) — ~10-15% of budget

---

## When to Deviate from the Standard Structure

### Add a Third Campaign When:
- The client is running a time-limited promotion with a completely different CTA and landing page — isolate it so the algorithm isn't confused by mixed signals
- The client has a clearly distinct product line with separate audience, creative, and conversion event (e.g., B2C retail + B2B wholesale under the same account)

### Never Add a Campaign For:
- "I want to test different audiences" → Use separate ad sets within one campaign. Audience testing belongs at the ad set level.
- "I want to track performance by region" → Use the breakdown report in Ads Manager (Delivery column → Country/Region)
- "My client wants to keep brand and non-brand separate" → Not necessary for Meta (unlike Google Ads). One campaign handles both.
- "I want a separate campaign for Reels" → Use Advantage+ Placements — Meta automatically prioritises the best placement per ad

---

## Campaign Budget Optimisation (CBO) vs. Ad Set Budget Optimisation (ABO)

**Use CBO (Advantage+ Campaign Budget):**
- Standard for all campaigns
- Meta distributes budget across ad sets based on performance signals
- Better for accounts where some DCT ad sets perform and others don't — budget automatically flows to winners

**Use ABO (manual ad set budgets) when:**
- You need to guarantee a minimum spend on a specific ad set (e.g., a brand new DCT that needs time to gather data before CBO might starve it)
- You're running a promotional ad set with a hard daily budget cap
- In the first 7–14 days of a new campaign when you want to ensure each ad set gets equal spend for comparison

**Practical approach:**
Start new campaigns with ABO at $10/day per ad set for the first 7–14 days. Once you have performance data, switch to CBO and let Meta optimise allocation.

---

## DPA Campaign Setup (eCommerce)

DPA (Dynamic Product Ads) are retargeting ads that automatically show the specific products a visitor viewed on Challenger's website.

**Prerequisites:**
- Product catalogue uploaded and synced to Meta (via Shopify Sales Channel or manual upload)
- Pixel firing ViewContent and AddToCart events correctly
- Website has at least 500–1,000 monthly website visitors (otherwise audience is too small)

**Setup:**
- Campaign objective: Catalogue Sales
- Ad set: Retargeting — select "Website visitors" and choose "Viewed or added to cart but not purchased" (last 30 days)
- Creative: Dynamic — Meta auto-populates product images, names, and prices from the catalogue
- Budget: ~10% of total monthly budget
- Frequency cap: 3–5 impressions per person per week to avoid overexposure

**Launch timing:** After 30 days — the Pixel needs to accumulate enough ViewContent and AddToCart events for the retargeting audience to be meaningful.

---

## ADV+ Campaign Setup

ADV+ (Advantage+ Shopping Campaign) is Meta's fully automated campaign type. uses it specifically to give a second life to creative that underperformed in the main campaign.

**Purpose:**
The main campaign's DCT experiments tell us which creative wins with the core audience. Non-winning creative often works for a different audience that narrow DCT targeting misses. ADV+ finds that audience automatically.

**What to put in ADV+:**
- DCT creative that generated at least some engagement but didn't hit CPA/ROAS targets in the main campaign
- NOT: new untested creative (test in main campaign first)
- NOT: the current best-performing creative from the main campaign (don't dilute the signal)

**Setup:**
- Campaign objective: Advantage+ Shopping Campaign
- Budget: 10–15% of total monthly budget
- Creative: Upload the phased-out assets as static ad sets (not DCT)
- Audience: Broad (ADV+ handles targeting automatically)

**Launch timing:** 60–90 days after initial launch, once main campaign has performance history and DCT phase-outs are available.

---

## Common Setup Mistakes to Avoid

| Mistake | Impact | Correct Approach |
|---|---|---|
| Campaign objective set to Traffic | Algorithm optimises for clicks, not conversions — CPA will be terrible | Always use Conversions objective |
| Too many ad sets per campaign | Budget fragmentation, slower learning | Max 3-5 ad sets in main campaign |
| Detailed interest stacking (10+ interests) | Audience too narrow, kills delivery | Broad or 1-2 interests max |
| Placements manually restricted (Facebook only, no Instagram) | Limits algorithm's ability to find best performing placements | Use Advantage+ Placements |
| Auto-applied recommendations left on | Meta will automatically change bids, budgets, creative | Turn off under Campaign Settings → Automation |
