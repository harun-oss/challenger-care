# PMAX Standards 2025

Read this at the start of Phase 5 of the Campaign Build skill for complete PMAX setup requirements, 2025 feature updates, and coexistence monitoring guidance.

---

## What PMAX Is (and Isn't)

Performance Max (PMAX) is a goal-based campaign type that runs across all Google surfaces simultaneously: Search, Shopping, YouTube, Display, Gmail, Discover, and Maps. It uses machine learning to allocate budget and bids across all these surfaces to maximize conversions.

**What PMAX is good for:**
- Accounts with established conversion data that want to extend reach beyond Search
- eCommerce with approved product feeds (Shopping is a major surface for PMAX)
- Clients with strong creative assets (images, video, copy) who want automated multi-channel distribution

**What PMAX is NOT good for:**
- New accounts with no conversion history — the algorithm has nothing to optimize toward
- Accounts with limited budgets (<$1,000–$2,000/month) — insufficient signal for the machine learning to work effectively
- Advertisers who need granular control over where their ads show — PMAX allocates across surfaces autonomously

---

## 2025 Feature Updates

### Campaign-level negative keywords

PMAX now supports up to **10,000 campaign-level negative keywords**.

This was a major gap in earlier PMAX versions — accounts couldn't prevent PMAX from bidding on brand terms, competitor terms, or irrelevant queries at the campaign level.

**Required minimums for every PMAX campaign:**
1. Account-level negative keyword list applied to PMAX
2. All client brand name variations — prevents PMAX from capturing branded search traffic that should stay in the Branded RSA campaign
3. Competitor brand names (if not running competitor campaigns)
4. Industry-specific exclusions from the negative keyword library

**How to apply:** Google Ads → PMAX Campaign → Settings → Campaign negatives → Add keywords

### Search themes

PMAX now accepts up to **50 search themes** per campaign.

Search themes are intent signals that guide PMAX toward specific search queries. They're similar to keywords but aren't keywords — PMAX doesn't do keyword-level bidding. Instead, search themes influence which search queries PMAX considers relevant.

**How to set up search themes:**
- Google Ads → PMAX Campaign → Asset Group → Search themes → Add themes
- Source: use the high-intent keywords from the approved keyword research
- Each theme should be a phrase describing what the customer is searching for (e.g., "commercial HVAC repair Minneapolis", "emergency AC replacement")
- Up to 50 themes per asset group

**Best practice:** Add at least 10 themes. Accounts with no search themes give PMAX no signal about which search queries are relevant — it learns from scratch, which is significantly slower.

**Do NOT add branded terms as search themes.** PMAX will bid on them, pulling branded traffic away from the dedicated Branded RSA campaign where it belongs.

---

## Eligibility Requirements

All of the following must be confirmed before building PMAX:

| Requirement | How to verify | Minimum |
|-------------|--------------|---------|
| Conversion history | Google Ads → Conversions → last 30 days | 30+ conversions |
| Monthly ad budget | Client brief / workbook | $1,000–$2,000/month minimum |
| Account age | Google Ads account creation date | Not a brand-new account |
| GMC feed (eCommerce) | Google Merchant Center → Products → Status | All products Approved |
| Website remarketing audience | Google Ads → Tools → Audience Manager → Website visitors | 100+ users |

If any item fails: do not build PMAX. Document the gap and set a reassessment date.

---

## Audience Signals — Setup Detail

Audience signals are not traditional audience targeting — they're suggestions that guide the algorithm's initial learning. PMAX will expand beyond these audiences if it finds conversion opportunities elsewhere.

### Customer Match

**What it is:** A list of existing customers or leads uploaded as a CSV.
**Why it matters:** The strongest possible signal — you're showing Google exactly who your existing customers are, and PMAX finds similar users.

**How to create:**
1. Client exports their customer email list (CRM, Shopify customers, email list)
2. Format: CSV with column headers — minimum: Email Address. Optional: First Name, Last Name, Phone, Country, Zip Code (more fields = higher match rate)
3. Google Ads → Tools → Audience Manager → + → Customer List → Upload CSV
4. Google hashes the email addresses for privacy before matching
5. Google displays the match rate (typically 30–60%) — a higher match rate means more of the list can be used as a signal
6. Apply the Customer Match list to the PMAX campaign as an audience signal

**Note:** Customer Match requires the account to be in good standing with Google's policies and the account to have spent a certain amount historically. If Customer Match is unavailable: skip this signal and use the other two.

### Website Visitors

**What it is:** A remarketing audience of users who visited Challenger's website.
**Minimum:** 100 users in the last 30 days (required for PMAX audience signal eligibility).

**How to set up:**
1. If the Google Tag (AW-XXXXXXXXX) is installed via GTM on all pages, Google automatically builds a website visitors audience
2. Google Ads → Tools → Audience Manager → Your audiences → Website visitors — confirm the audience size is ≥ 100
3. If below 100: PMAX cannot use this signal yet. Launch PMAX without it and add once threshold is reached.

### Custom Intent Audience

**What it is:** An audience Google builds based on users whose behavior suggests they're actively researching keywords, visiting specific URLs, or using specific apps that indicate purchase intent.

**How to create:**
1. Google Ads → Tools → Audience Manager → + → Custom Segment → Create custom segment
2. Choose: "People who searched for any of these terms on Google"
3. Enter the top 10–20 high-intent keywords from the keyword research
4. Optionally add: "People who browse types of websites" — enter competitor URLs and relevant industry sites
5. Name the segment clearly (e.g., "Commercial HVAC — High Intent Searchers")
6. Apply to PMAX campaign as an audience signal

---

## Asset Group Structure

### One asset group per product or service category — not one for everything

PMAX uses asset groups to target different audiences across different surfaces. If all your products and services are in one asset group, PMAX can't differentiate what it's promoting and to whom.

**Example for a commercial cleaning company:**

```
PMAX Campaign: [Client] — PMAX
  Asset Group 1: Office Cleaning Services
    Final URL: /office-cleaning
    Images: office interior, cleaning team in office, "before/after" desk area
    Headlines: "Professional Office Cleaning", "Spotless Offices, Guaranteed", "Minneapolis Office Cleaners"

  Asset Group 2: Post-Construction Cleaning
    Final URL: /post-construction-cleaning
    Images: construction site, finished cleaned space, cleaning crew with equipment
    Headlines: "Post-Construction Cleanup", "Fast Construction Site Cleaning", "Certified Construction Cleaners"
```

If both asset groups pointed to the homepage with generic images, PMAX would have no way to surface the right message for the right search intent.

### Required assets per asset group

| Asset type | Required | Notes |
|------------|---------|-------|
| Landscape images (1.91:1) | 3 minimum | Up to 20. Real brand photography only — no stock photos. Show the service in action, team, happy customers. |
| Square images (1:1) | 3 minimum | Up to 20. Same quality standard as landscape. |
| Logo (1:1 square) | 1 required | PNG with transparent background recommended. |
| Video | 1 minimum | Must be 10 seconds minimum. **Do not skip** — auto-generated video will be used if no video is provided. |
| Headlines | 3 minimum | Up to 5. Max 30 characters each. Keyword-relevant and benefit-forward. |
| Long headlines | 1 minimum | Up to 5. Max 90 characters each. |
| Descriptions | 2 minimum | Up to 5. Max 90 characters each. |
| Business name | Required | Official business name as it appears publicly. |
| Final URL | Required | Specific to the asset group theme — not the homepage unless the homepage is the most relevant destination. |

### Video — critical requirement

**Auto-generated video is not acceptable.**

When no video asset is provided, Google will create an automatic video using the provided images and text. These auto-generated videos are typically low quality, poorly branded, and can damage Challenger's brand perception.

**If Challenger has no video:** Options in priority order:
1. Request a short video from Challenger — even a smartphone video of the team or product in action is significantly better than auto-generated
2. Create a simple branded slideshow video using the static images, brand colors, and overlaid text using a tool like Canva or Adobe Express
3. Disable the video ad format for the campaign (Google Ads → PMAX Campaign → Asset Group → Additional formats → uncheck video ads) — this is a last resort as it limits PMAX reach on YouTube and Display

---

## PMAX and RSA Coexistence

When PMAX and RSA campaigns run simultaneously targeting overlapping keywords/searches:

**What happens:** PMAX takes priority on Search auctions it determines it can win. RSA campaigns may see impression share drop.

**This is expected behavior — but it must be monitored.**

**Monitoring schedule (first 30 days after PMAX launch):**

Week 1–4: Check RSA campaign impression share weekly:
- Compare RSA impression share before PMAX launch vs after
- If RSA impression share drops >20% after PMAX launches: investigate overlap

**Diagnosing overlap:**
- Are PMAX search themes similar to the RSA campaign keywords? If yes, PMAX is directly competing with RSA on Search
- Check PMAX Insights tab → Search terms PMAX is showing for — are these the same terms the RSA is targeting?

**Adjustments if overlap is problematic:**
1. Make PMAX search themes more specific (narrower terms that are distinct from core RSA keywords)
2. Add RSA's most important exact match keywords to PMAX campaign-level negatives
3. Adjust budget allocation: reduce PMAX budget slightly and increase RSA budget to compensate

**When RSA impression share drop is acceptable:**
If RSA impression share drops but total conversions and revenue are stable or growing — PMAX is simply fulfilling some of that demand more efficiently. The goal is conversions, not preserving RSA impression share at all costs.

---

## PMAX Reporting and Insights

PMAX provides less granular reporting than RSA campaigns by design. What's available:

- **Asset group performance:** Headlines, descriptions, and images are rated (Learning, Good, Best, Low) — replace "Low" assets
- **Audience insights:** Who is converting (demographics, interests) — useful for informing creative strategy
- **Search term insights:** High-level themes, not individual keywords — less detailed than RSA Search Terms report
- **Attribution:** Conversions attributed to PMAX include all surfaces — difficult to separate Search conversions from Display or YouTube conversions

**Set expectations:** Clients accustomed to keyword-level reporting from RSA will find PMAX reporting frustrating. Frame it as a black-box channel that's evaluated at the campaign level (total conversions, CPA, ROAS) rather than keyword-by-keyword.
