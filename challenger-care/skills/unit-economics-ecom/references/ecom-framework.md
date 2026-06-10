# E-Commerce Unit Economics Framework

## Table of Contents

1. [Core Formulas: The CM Stack](#1-core-formulas-the-cm-stack)
2. [Variable Cost Benchmarks](#2-variable-cost-benchmarks)
3. [AOV and Blended AOV](#3-aov-and-blended-aov)
4. [LTV Models](#4-ltv-models)
5. [LTV Benchmarks by Category](#5-ltv-benchmarks-by-category)
6. [Scenario Calculations](#6-scenario-calculations)
7. [Break-Even ROAS](#7-break-even-roas)
8. [Client Intake Questions](#8-client-intake-questions)
9. [Gross Margin Benchmarks by Category](#9-gross-margin-benchmarks-by-category)
10. [Common Mistakes and Red Flags](#10-common-mistakes-and-red-flags)

---

## 1. Core Formulas: The CM Stack

### CM1 — Gross Margin Per Order
```
CM1 = AOV × Gross Margin %
```
Gross Margin % = (Revenue − COGS) ÷ Revenue
COGS includes: product cost, inbound freight, duties/tariffs, packaging

### CM2 — Pre-Marketing Contribution Margin
```
CM2 = CM1 − Variable Fulfillment Costs
```
Variable Fulfillment Costs include:
- Outbound shipping (if not charged to customer)
- Payment processing fees (typically 2–3.5% of AOV)
- Returns reserve (category-dependent, see benchmarks)
- Warehouse pick/pack fees (if 3PL)
- Customer service allocation (optional, improves accuracy)

### CM3 — Post-Acquisition Contribution Margin
```
CM3 = CM2 − CPA
```
This is the per-order profit or loss after paying to acquire the customer.

- CM3 > 0: first-purchase profitable
- CM3 = 0: break-even on order 1
- CM3 < 0: loss leader — requires LTV to justify spend

### Net Profit Per Order (with overhead allocation)
```
Net Profit = CM3 − (Fixed Overhead ÷ Monthly Orders)
```
Optional — only include if Challenger wants fully-loaded profitability.

---

## 2. Variable Cost Benchmarks

Use these when Challenger cannot provide actuals. Label all benchmark-derived
figures `[benchmark]` in the output.

| Cost Item | Typical Range | Notes |
|---|---|---|
| Outbound shipping | 8–12% of AOV | Higher for heavy/bulky products |
| Payment processing | 2–3.5% of AOV | Stripe/Shopify Payments ~2.9% + $0.30 |
| Returns reserve | 2–6% of revenue | Apparel higher (8–12%), supplements lower (2–3%) |
| 3PL pick/pack | $3–8 per order | Depends on item count and 3PL |
| Customer service | 1–3% of revenue | For brands with high inbound volume |

**Typical total variable fulfillment cost: 15–25% of AOV**

For a quick estimate when no data is available:
- Low-return category (supplements, consumables): use 15% of AOV
- Moderate-return category (home goods, electronics accessories): use 20% of AOV
- High-return category (apparel, footwear): use 25–30% of AOV

---

## 3. AOV and Blended AOV

### What to use
Always use **blended AOV** — the average across all orders, not the hero product price.

```
Blended AOV = Total Revenue ÷ Total Orders (trailing 90 days)
```

### AOV red flags
- Client reports AOV = single product price on a multi-SKU store → ask for Shopify analytics
- AOV is very high relative to product price → likely includes bundles or upsells; confirm
- AOV has changed significantly in the last 90 days → use the current period, not LTM

### AOV-lift opportunity
When modeling Scenario A, note if a $10–15 AOV lift (bundle, upsell, or threshold-based free
shipping) would move them from Scenario B into Scenario A territory. This is often the highest-
leverage CRO opportunity.

---

## 4. LTV Models

### Model 1: Simple Formula (use when no cohort data exists)
```
LTV = AOV × Purchase Frequency (per year) × Customer Lifespan (years)
```
Label output `[projected — formula-based, not validated by cohort data]`

### Model 2: Cohort-Based (preferred when data is available)
```
LTV at N days = AOV × (1 + Repeat Purchase Rate at N days)
```
More accurate. Requires cohort data from Klaviyo, Triple Whale, or Northbeam.

Example:
- AOV = $80
- 90-day repeat rate = 18%
- 180-day repeat rate = 31%
- 365-day repeat rate = 48%

LTV at 90d  = $80 × (1 + 0.18) = $94.40
LTV at 180d = $80 × (1 + 0.31) = $104.80
LTV at 365d = $80 × (1 + 0.48) = $118.40

### Model 3: Subscription/Replenishment
```
LTV = AOV × (1 ÷ Monthly Churn Rate)
```
Use for subscription boxes, auto-replenishment, or membership models.

---

## 5. LTV Benchmarks by Category

Use when Challenger has no cohort data. Label all figures `[benchmark]`.

| Category | 90-Day Repeat Rate | 180-Day Repeat Rate | 365-Day Repeat Rate |
|---|---|---|---|
| Supplements / consumables | 25–35% | 40–55% | 55–70% |
| Beauty / skincare | 20–30% | 35–50% | 50–65% |
| Apparel / fashion | 15–25% | 25–40% | 35–55% |
| Home goods / decor | 10–18% | 18–28% | 25–40% |
| Food & beverage | 30–45% | 50–65% | 65–80% |
| Pet products | 25–40% | 45–60% | 60–75% |

Source: Triple Whale industry benchmarks, 2024–2025; Klaviyo Email Benchmarks 2025

---

## 6. Scenario Calculations

### Scenario A — First-Purchase Profitable
```
Max CPA (Scenario A) = CM2 − Target Profit Margin

Where Target Profit Margin = CM2 × Desired Profit %
```
If no target profit is specified, use 20% of CM2 as a conservative default.

Example:
- AOV = $120, GM = 60% → CM1 = $72
- Variable costs = 20% of AOV = $24 → CM2 = $48
- Target profit = 20% of CM2 = $9.60
- Max CPA (A) = $48 − $9.60 = **$38.40**

### Scenario B — Break-Even on Order 1
```
Max CPA (Scenario B) = CM2
```
This is the maximum CPA before the brand loses money on every order.

Example (continued): Max CPA (B) = **$48.00**

### Scenario C — Loss Leader with LTV Upside
```
Max CPA (Scenario C, N-day horizon) = CM2 + (LTV at N days − AOV) × GM%
```
The second term represents the gross margin from repeat purchases.

Simplified version:
```
Max CPA (C) = LTV at N days × GM% − Variable Costs
```

Example:
- LTV at 90d = $94.40 (from Model 2 above)
- GM% = 60%, Variable costs = $24
- Max CPA (C, 90d) = ($94.40 × 0.60) − $24 = $56.64 − $24 = **$32.64**

Wait — this is lower than Scenario B in this example. That's correct when
the 90-day LTV uplift is modest. The insight: Scenario C only makes sense
when LTV at the target horizon meaningfully exceeds the first-order AOV.

Repeat for 180d and 365d horizons.

---

## 7. Break-Even ROAS

```
Break-Even ROAS = 1 ÷ Gross Margin %
```

| Gross Margin | Break-Even ROAS |
|---|---|
| 70% | 1.43× |
| 65% | 1.54× |
| 60% | 1.67× |
| 55% | 1.82× |
| 50% | 2.00× |
| 45% | 2.22× |
| 40% | 2.50× |
| 35% | 2.86× |
| 30% | 3.33× |

**Important:** Break-even ROAS assumes no variable fulfillment costs beyond
COGS. When fulfillment costs are significant, the real break-even ROAS is
higher. Adjust: `Break-Even ROAS = 1 ÷ (GM% − Variable Fulfillment % of revenue)`

---

## 8. Client Intake Questions

### Must-have (minimum viable model)
1. What is your average order value (AOV)? If you have multiple products,
   what is your blended AOV across all orders in the last 90 days?
2. What is your gross margin %? (Revenue minus cost of goods, as a % of revenue)
3. What is your current average CPA (cost per acquisition of a new customer)?

### High-value additions
4. What are your outbound shipping costs per order? (Or does the customer pay shipping?)
5. What payment processor do you use? (Used to estimate processing fees)
6. What is your return rate?
7. Do you have a 3PL? What do they charge per order for pick/pack?
8. Do you have cohort data showing repeat purchase rates at 90/180/365 days?
   (Can pull from Klaviyo, Triple Whale, or Northbeam)
9. Do you have an email/SMS flow for post-purchase retention?
10. What is your target ROAS or target CPA currently?

---

## 9. Gross Margin Benchmarks by Category

Use when Challenger cannot provide gross margin. Label as `[benchmark]`.

| Category | Typical GM Range | Notes |
|---|---|---|
| Supplements / vitamins | 60–75% | Higher for private label |
| Beauty / skincare | 60–75% | Lower with heavy influencer cost |
| Apparel / fashion | 45–65% | Lower end for volume plays |
| Food & beverage | 35–55% | Heavily dependent on COGS and shipping weight |
| Home goods / decor | 40–60% | Wide range; furniture lower |
| Pet products | 50–65% | Premium pet brands higher |
| Electronics accessories | 40–60% | Margin compressed by competition |
| Jewelry / accessories | 55–70% | Higher for handmade/artisan |

Source: Shopify industry data 2024; BeProfit DTC benchmark report 2025

---

## 10. Common Mistakes and Red Flags

### Mistake 1: Using blended CPA instead of new-customer CPA
Blended CPA mixes new and returning customers. The unit economics model
should use **new customer CPA only**. Returning customers don't require
acquisition spend. Ask: "Is this CPA for new customers only, or blended?"

### Mistake 2: Excluding returns from COGS
Many brands calculate gross margin before returns. Returns reduce effective
GM by 2–12% depending on category. If returns are not in COGS, add a
returns reserve to variable fulfillment costs.

### Mistake 3: Mixing subscription and one-time revenue in AOV
If the brand sells both subscription and one-time, run two separate models.
Subscription LTV is calculated differently (churn-based, not cohort-based).

### Mistake 4: Treating Scenario C as the default recommendation
Scenario C requires validated retention infrastructure. For brands without
active email flows, high repeat purchase rates, or subscription models,
the LTV assumption is speculative. Scenario B is often the right starting
point.

### Mistake 5: Ignoring CAC payback on working capital
A high Scenario C CPA may be mathematically correct but operationally
unviable if the brand doesn't have the working capital to fund 180 days
of customer acquisition before recovering the cost. Always note the payback
period and flag if it exceeds Challenger's likely runway.
