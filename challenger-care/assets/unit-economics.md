# Unit Economics — Challenger Care

The numbers Claude (and the team) should know cold before any pricing, bundle, ad spend, or promo decision.

---

## Product economics

| Metric | Value | Source |
|---|---|---|
| Product COGS (per jar, blended) | **$3.45** | Kickoff |
| Gross margin | **~82%** | Kickoff |
| Free shipping threshold | **$35** | Kickoff |
| Shipping cost (per order, variable) | **$5.50–$8.00** | Kickoff — depends on mix |
| Jar duration (subscription cadence) | **~110 days** | Kickoff — natural sub interval |

## AOV math

| Metric | Current | Target |
|---|---|---|
| Shopify AOV | **$25–$30** | **$50** |
| AOV lift required | — | **20%+** |
| Strategy | — | 3-pack as default offer |

## 3-Pack bundle math (the AOV unlock)

| Variable | Value |
|---|---|
| Product cost (3 jars + packaging) | **$11–$12** |
| Target retail (range) | **$50–$89** |
| Contribution at $50 retail | ~$38 after COGS |
| Free shipping | Included (well above $35 threshold) |
| Acquisition headroom | **~$38 CAC room at $50 retail** |
| First-order behavior | Range is wide because Hayden flagged uncertainty on max bundle price for first-time buyers |

**Decision rule:** Test 3-pack at $50, $65, $89 against current single-jar default. Target: ≥30% bundle attach rate.

## Order contribution stack

For a typical single-jar order at $25:
```
Revenue           $25.00
COGS              -$3.45
Shipping cost     -$6.50  (mid-range)
Payment fees      -$0.75  (3%)
─────────────────────────
Contribution      ~$14.30 (~57% per-order margin after fulfillment)
```

For a 3-pack at $50:
```
Revenue           $50.00
COGS              -$11.00
Shipping cost     -$7.50  (slightly higher with bundle weight)
Payment fees      -$1.50  (3%)
─────────────────────────
Contribution      ~$30.00 (~60% per-order margin after fulfillment)
```

The 3-pack roughly **doubles per-order contribution** vs single jar.

## Acquisition economics

| Scenario | Max allowable CPA | Rationale |
|---|---|---|
| First-order profitable | ~$14 (single jar) / ~$30 (3-pack) | Order pays for itself within fulfillment |
| Break-even with 1 reorder | ~$28 (single) / ~$60 (3-pack) | Assumes 1 repeat purchase |
| Loss-leader (LTV-funded) | $40–$60 for 3-pack | Justified if subscription attach >20% |

**Constraint:** Limited Shopify cohort data due to low order volume — LTV figures use Amazon S&S as the proxy (1,318 subs, 110-day cadence). When Shopify scale grows, recalibrate.

## Subscription economics

| Lever | Value |
|---|---|
| Jar duration | ~110 days |
| Implied subscription cadence | Quarterly (~every 110 days) or monthly micro-doses |
| Amazon S&S subscribers | 1,318 |
| Shopify (Recharge) subscribers | 17 |
| Migration opportunity | Move S&S subs to Shopify for owned customer relationship |
| LTV multiplier (sub vs one-time) | ~3–5× over 18 months (industry average for daily-use grooming) |

## Revenue goals

| Channel | Current monthly | Target monthly |
|---|---|---|
| Blended (Amazon + Shopify) | ~$55K | **$60K** |
| Shopify | ~$929 (30d) | **$6,000** (10% of blend) |
| Klaviyo email | ~$214 (MTD) | **$1,000** (25%+ from flows) |

## Cash position context

- Manufacturing payable to Emanuel — **~6 weeks from clearing** as of kickoff (Jun 5, 2026)
- Once cleared: free cash available for growth investment (paid acquisition, inventory expansion)
- Risk tolerance: **high** on Shopify/Klaviyo (low revenue today, easy to test); **controlled** on Meta/Google paid (need spending ceilings)

## Decision rules for Claude

When the team asks pricing / bundle / spend / promo questions, Claude should:

1. **Always reference the AOV target** — $50 is the gate that unlocks profitable paid acquisition
2. **Default to the 3-pack** when proposing offers — it's the only product mix that hits the AOV target
3. **Cap discount logic** — every promo must preserve at least 50% gross margin
4. **Flag any first-order CPA above $30** as risky given current LTV uncertainty
5. **Subscription is the LTV play** — every offer should have a subscription tier
6. **Free shipping is sacred** — orders below $35 lose $5–$8 to shipping, killing margin

## When to update this doc

- After every pricing test (record outcome)
- When COGS changes (new supplier, packaging, formulation)
- When Shopify LTV data becomes statistically meaningful (~6 months of consistent orders)
- When subscription program expands or churns meaningfully
