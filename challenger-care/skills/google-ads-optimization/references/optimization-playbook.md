# Google Ads Optimization Playbook

Reference for the google-ads-optimization skill. Read the relevant section during the phase indicated.

---

## Search Term Decision Framework

### Full decision criteria

**Tier 1 — Add as exact match negative immediately:**
- Searched for a competitor's brand name (e.g., "Klaviyo" on a Salesforce client) — protects budget from wrong-intent clicks
- Contains words that indicate zero purchase intent: "free", "DIY", "how to", "definition", "what is", "salary", "job", "review" (unless the account specifically targets those intents)
- Spent more than 3× the CPA target in 7 days with zero conversions
- Irrelevant industry entirely (e.g., "plumber" appearing on a SaaS account)
- Branded term in a non-branded campaign — add to the non-branded campaign's negative list as exact match

**Tier 2 — Add as phrase match negative:**
- Contains a problematic qualifier that doesn't apply universally (e.g., "cheap", "used", "second hand" on a premium brand)
- Indicates wrong geography (e.g., "London plumber" on a US-only account) — use [location + service] as phrase match
- Professional/trade intent where Challenger only wants consumer purchases (e.g., "wholesale" or "bulk" on a DTC eCommerce account)

**Tier 3 — Monitor before deciding:**
- 1–3 conversions in 30 days but at 2× CPA target — too early to pause; watch for another 14 days
- Brand-adjacent query (e.g., "similar to [client brand]") — could indicate discovery intent; watch click-through rate on landing page

**Do not add as negative:**
- Any search term that has generated 1+ conversions at target CPA in the last 30 days — even if it looks odd
- Branded terms in the branded RSA campaign — these are the campaign's purpose
- Search terms running for fewer than 7 days — insufficient data

### Edge cases

**"Best [product category]" queries:**
Usually high intent. Do not add as negative unless they've spent significantly with zero conversions. Consider adding the converting versions as positive keywords.

**Question queries ("how to use X", "is X worth it"):**
These can convert for some products (especially considered purchases). Check CTR and conversion rate before deciding. If CTR is high but conversions are zero, the landing page may not be answering the query — a content problem, not an ads problem.

**Location modifiers:**
If an account targets a specific region and a location modifier outside that region appears, add "[other location] + service" as a phrase match negative. But be careful — some location queries are from people *researching* moving to or visiting the target area and may still be valid.

---

## RSA Rotation Cadence

### Monthly variant launch process

**Step 1: Identify the target ad group**
Priority order for which ad group gets the new variant:
1. Ad groups with CTR below 2% on Search (headlines not resonating)
2. Ad groups with CPA above target by >25% for 30+ days
3. Ad groups that haven't had a new variant in 90+ days

**Step 2: Write the new RSA**

Use at least 8 distinct headlines (never repeat the same phrase across multiple headlines):
- 2 keyword-specific headlines (pin one to Headline 1)
- 2 benefit headlines (outcome-focused: "Cut Your CPA in Half")
- 2 trust/proof headlines ("Trusted by 500+ Brands", "4.9★ on Google")
- 2 urgency/CTA headlines ("Get Your Free Audit", "Start in 24 Hours")

Use 4 descriptions:
- 1 pain-point → solution format
- 1 proof/social validation format
- 1 feature → benefit format
- 1 CTA-focused format

**Step 3: Label the RSA**
Name format: `[CampaignCode]-RSA-[VariantLetter] [Month Year]`
Example: `NB-RSA-C Apr 2026`

This makes it possible to track which variant launched when without reading the ad copy itself.

**Step 4: Check the 3-RSA rule**
If the ad group already has 3 RSAs:
- Pull the last 30-day performance for all three
- Pause the one with the lowest CTR AND lowest conversion rate
- Then launch the new RSA

**Step 5: Log the launch**
In the Change Log: date, ad group, RSA label, variant letter, hypothesis for why this new angle might outperform.

**Step 6: 30-day review**
After 30 days, compare CTR, conversion rate, and CPA for the new variant vs the existing control. If the new variant is underperforming on all three, pause it and note what didn't work. If it's outperforming, it becomes the new control.

---

## PMAX Optimization Protocol

### Month 1 (first 30 days): Observe only

Do not make significant changes to a PMAX campaign in its first 30 days. The algorithm is in a learning and calibration phase. Changes reset the learning clock.

What to do in Month 1:
- Monitor spend pacing (is it spending the full budget or throttling?)
- Check for disapproved assets (fix immediately — disapprovals suppress the entire asset group)
- Confirm audience signals are present (Customer Match + website visitors)
- Ensure search-specific exclusions are active (brand terms excluded from PMAX if a separate branded RSA campaign exists)
- Log observations in the Change Log even if making no changes

### Month 2 (31–60 days): First optimization pass

By 60 days, PMAX has enough data to make meaningful asset performance assessments.

**Asset performance audit:**
- Pull Asset Groups → View Details → Performance column
- Remove any asset rated "Low" that has 30+ days of data (images, headlines, descriptions, videos)
- Before removing a Low asset: confirm there are at least 3 other assets of that type remaining — PMAX needs variety
- Add 2–3 fresh assets in each category where performance is weak

**Search theme review:**
- Which search themes are generating conversions vs which are generating impressions only?
- Themes with 30+ days and zero conversions: remove and replace with themes closer to high-converting search terms found in the search terms report

**Audience signal update:**
- Has Challenger's Customer Match list been refreshed with new purchasers? If not, update it
- Consider adding a similar audiences signal based on the Customer Match list

### Month 3+ (ongoing, monthly cadence):

- Asset performance: remove Low performers, add new creative monthly
- Budget: If PMAX is spending efficiently (ROAS at/above target), consider increasing its budget allocation vs RSA. PMAX scales better than RSA when conversion data is strong.
- ROAS target: Tighten by 5–10% if the campaign has held its ROAS target for 30+ consecutive days
- Asset groups: At 90 days, evaluate adding a second asset group for a distinct product line or seasonal promotion

---

## Performance Collapse Diagnosis

Use this flow when CPA spikes to 2× target or ROAS drops 50%+ for 3+ consecutive days.

### Step 1: Rule out tracking issues first

Before blaming performance, verify the data is real:
- Go to Google Ads → Tools → Conversions → check all conversion actions for "Tag inactive" or "No recent conversions" status
- Cross-reference: is the dip in Google Ads also showing in GA4? If GA4 shows normal traffic but Google Ads shows fewer conversions, it's a tracking issue, not a performance issue.
- Has Challenger's website changed recently? New checkout flow, new thank-you page URL, or plugin update can break the conversion tag.

### Step 2: Check for account-level changes

- Was there a bid strategy change in the last 14 days? (Expected volatility — wait it out)
- Were any auto-applied recommendations accidentally enabled? (Tools → Recommendations → Auto-apply — check all toggles)
- Did Google auto-upgrade any keywords to broad match? (Filters → "Match type: was changed")
- Did a new campaign launch and drain budget from existing campaigns?

### Step 3: Check external factors

- Is the landing page loading correctly? Test the top 3 ad landing pages manually.
- Is there a seasonal or market reason? Check Google Trends for the core keywords — is search volume down industry-wide?
- Did a competitor change their offer? (Check Auction Insights for Outranking Share changes)
- Did Challenger run a promotion or price change that affected conversion intent?

### Step 4: Document findings

After the diagnosis, record findings in the Change Log and next Slack update:
- Root cause (if identified)
- Actions taken or not taken (and why)
- Expected timeline for recovery or next assessment point

### Common root causes and fixes:

| Root cause | Fix |
|-----------|-----|
| Conversion tag broke (website change) | Re-install tag via GTM, verify with Tag Assistant |
| Auto-applied recommendation changed keywords to broad | Revert in Change History; disable auto-apply |
| tCPA set too low after graduation | Increase tCPA to actual 30-day average; allow 14-day re-learning |
| Budget drained by PMAX cannibalizing RSA | Add PMAX campaign-level negative for brand terms; check impression share split |
| Seasonal demand drop | Lower budgets proportionally; do not change bid strategy during seasonal troughs |
| Landing page broken or slow | Fix the page; do not pause campaigns — pausing then relaunching restarts the learning phase |
