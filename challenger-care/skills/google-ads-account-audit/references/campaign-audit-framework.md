# Campaign Audit Framework

Read this at the start of Phase 3 of the Account Audit for detailed criteria and benchmarks used to evaluate existing campaigns.

---

## Quality Score Benchmarks

Quality Score (1–10) measures keyword + ad + landing page relevance. Each of the three components is rated: Above average, Average, or Below average.

| Quality Score | Interpretation | Action |
|--------------|----------------|--------|
| 8–10 | Excellent — performing at full efficiency | Monitor; maintain keyword-ad alignment as copy evolves |
| 6–7 | Good — minor inefficiencies | Review landing page alignment; test improved headlines |
| 4–5 | Below average — CPC penalty active | Audit ad relevance (keyword in Headline 1?) and landing page match |
| 1–3 | Poor — significant CPC penalty and position suppression | Immediate action: rewrite ad copy, fix landing page, or pause keyword |

**benchmark:** Accounts with "Above average" landing page experience and ad relevance show 750% better CVR and 36% lower CPC compared to "Below average" accounts. Quality Score is not a vanity metric — it directly affects profitability.

**Flag for action:** Any keyword with Quality Score ≤ 4 on a top-spend keyword is a priority fix.

---

## CTR Benchmarks by Vertical

CTR varies significantly by industry and intent level. Use these as orientation, not absolute rules:

| Vertical | Average Search CTR | Strong Search CTR |
|----------|-------------------|------------------|
| Legal | 2–3% | 4–6% |
| Home services | 3–5% | 6–8% |
| B2B SaaS | 2–4% | 5–7% |
| eCommerce | 2–4% | 5–8% |
| Healthcare | 2–3% | 4–5% |
| Financial services | 2–4% | 5–7% |

**Flag for action:** Any RSA with CTR below 1% on Search for 90+ days. Low CTR indicates the ad copy doesn't match the searcher's intent — the headline isn't relevant enough to earn a click.

---

## Wasted Spend Identification

Pull the keyword performance report filtered to the last 90 days. Sort by Cost (descending).

**Identify:**

1. **Keywords with high spend and zero conversions:**
   - Threshold: any keyword that has spent >20% of the monthly budget with zero conversions in 90 days
   - Action: pause the keyword; check if it's due to poor landing page alignment, wrong match type triggering irrelevant queries, or a genuine lack of commercial intent for this keyword

2. **Keywords with high spend and very high CPA (2–3x target):**
   - These are converting, but at unsustainable cost
   - Check: Quality Score (low QS = high CPC), landing page alignment, ad group keyword theme

3. **Search Terms report — irrelevant queries:**
   - Filter the Search Terms report to "Not added" keywords (queries that triggered ads but aren't in the keyword list)
   - Identify irrelevant queries — these are bleeding budget on zero-intent traffic
   - Add as negatives immediately

---

## Ad Group Structure Red Flags

| Red flag | Why it matters | Fix |
|----------|---------------|-----|
| More than 20 keywords per ad group | Ad-to-keyword relevance drops; copy can't be specific enough for all terms | Break into smaller, tighter ad groups |
| Single RSA per ad group | No A/B testing possible; algorithm can't optimize | Add a second RSA with different headline angles |
| More than 3 active RSAs per ad group | Testing signal diluted across too many variants | Pause the weakest-performing RSA |
| Headline 1 not pinned | Generic headlines rotating into Headline 1 position, hurting ad relevance | Pin keyword-specific headline to position 1 |
| Branded and non-branded keywords in same campaign | Performance data distorted; optimization decisions unreliable | Separate into dedicated campaigns |

---

## Bid Strategy Assessment Criteria

**When to flag Maximize Clicks as overdue for graduation:**
- Account has been running for 60+ days
- 30+ conversions recorded in the last 30 days
- Bid strategy is still Maximize Clicks
- Recommendation: graduate to Maximize Conversions

**When to flag tCPA as misconfigured:**
- The tCPA target is more than 30% below the actual CPA from the last 90 days
- Campaign is consistently underspending (impression share is low despite adequate budget)
- Conversion volume drops sharply after tCPA is applied
- Recommendation: raise tCPA to within 20% of actual CPA; let algorithm stabilize over 30 days before tightening

**When to flag Maximize Conversions as ready for tCPA:**
- Account has been on Maximize Conversions for 60+ days
- CPA has been stable within ±15% for 4+ consecutive weeks
- 30+ conversions per month consistently
- Recommendation: introduce tCPA at actual CPA + 20%; tighten by $5–10 every 2 weeks

---

## Budget Utilization Assessment

**Throttling (hitting daily budget cap):**
- The campaign has reached its daily budget limit before the day ends
- Impression share lost to budget: check in the Auction Insights or Campaign column
- Interpretation: demand exists for this campaign but budget is limiting reach
- Options: increase budget, reduce bids to stretch budget further, or apply ad scheduling to focus spend on highest-conversion time windows

**Underspending:**
- Campaign consistently spends <70% of its daily budget
- Interpretation: either the tCPA/tROAS target is too aggressive (algorithm can't find qualifying traffic within the target), Quality Score is too low (low impression share from rank), or keyword volume is too limited for the budget
- Fix: check bid strategy target vs actual performance; check impression share lost to rank vs lost to budget; consider expanding keyword coverage

---

## PMAX Audit Checklist

When an existing account is running PMAX:

| Check | Pass criteria |
|-------|--------------|
| Eligibility at time of launch | Was PMAX appropriate when it was built? (30+ conversions/month, adequate budget) |
| Audience signals | Customer Match + website visitors + custom intent all present |
| Search themes | At least 10 themes populated; up to 50 is the limit (2025) |
| Campaign-level negatives | Account-level list + brand names added (2025 supports up to 10,000) |
| Asset groups | One per product/service category, not one generic group for everything |
| Video assets | Real video present — no auto-generated video |
| Brand name exclusion | Client brand name is in PMAX negatives to keep branded traffic in branded RSA campaign |
| RSA cannibalization | RSA impression share trends since PMAX launch — should not have dropped >20% |

---

## Competitive Positioning Assessment

From the Auction Insights report:

| Metric | What it tells you |
|--------|------------------|
| Impression Share | % of auctions where your ads showed vs total eligible auctions |
| Overlap Rate | How often a competitor's ad showed when yours did |
| Outranking Share | How often your ad ranked higher than a competitor's |
| Top of Page Rate | How often your ad appeared above organic results |
| Absolute Top Rate | How often your ad was the first ad (position #1) |

**Flags:**
- Impression Share below 40%: budget-constrained or Quality Score-constrained. Check which.
- Overlap Rate with a specific competitor above 80%: you're in direct, frequent competition. Review their ad copy (Ads Transparency Center) to differentiate.
- A competitor consistently Outranking you with high frequency: they may be bidding more aggressively, or their Quality Score is higher. Improving QS is the more sustainable response vs increasing bids.
