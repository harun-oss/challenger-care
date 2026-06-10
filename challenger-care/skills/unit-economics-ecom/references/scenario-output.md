# E-Commerce Scenario Output Template

Use this exact structure for every unit economics deliverable. The output
should be passable directly to Challenger without editing.

---

## Output Template

```
# Unit Economics Analysis — [Brand Name]
Prepared by | [Date]

---

## INPUTS USED

| Input | Value | Source |
|---|---|---|
| Average Order Value (AOV) | $[X] | [Client-provided / Benchmark] |
| Gross Margin % | [X]% | [Client-provided / Benchmark — category: X] |
| Variable Fulfillment Costs | $[X] ([X]% of AOV) | [Client-provided / Benchmark] |
| Contribution Margin 2 (CM2) | $[X] | Calculated |
| Current CPA | $[X] | [Client-provided] |
| Current ROAS | [X]× | [Client-provided / Calculated from CPA + AOV] |

---

## CURRENT STATE DIAGNOSTIC

**Where you are today:**

Your contribution margin stack breaks down as follows:

- CM1 (Gross Margin per order): $[X]
  Formula: $[AOV] × [GM]% = $[CM1]

- CM2 (Pre-marketing margin, after fulfillment): $[X]
  Formula: $[CM1] − $[variable costs] = $[CM2]

- CM3 (Post-acquisition margin at current CPA): $[X]
  Formula: $[CM2] − $[CPA] = $[CM3]

**You are currently operating in:** [Scenario A / B / C]

[One sentence plain-language interpretation of what CM3 means for them]

**Break-even ROAS:** [X]× (formula: 1 ÷ [GM]%)
**Your current ROAS:** [X]×
**Gap:** [above / below] break-even by [X]×

---

## THREE SCENARIO MODEL

### Scenario A — First-Purchase Profitable
**Max allowable CPA: $[X]**

Formula: CM2 ($[X]) − target profit ($[X] at [X]% of CM2) = $[X]

At this CPA:
- Implied minimum ROAS: [X]×
- You generate $[X] of margin per order after acquisition cost
- [Feasibility note: Is this achievable? Reference category/channel benchmarks]

### Scenario B — Break-Even on Order 1
**Max allowable CPA: $[X]**

Formula: CM2 = $[X] (100% of pre-marketing margin allocated to acquisition)

At this CPA:
- You neither profit nor lose on the first order
- No LTV assumption required — sustainable without a retention program
- Implied minimum ROAS: [X]×

### Scenario C — Loss Leader with LTV Upside

| Horizon | LTV | Max CPA | LTV Basis | Required Repeat Rate |
|---|---|---|---|---|
| 90 days | $[X] | $[X] | [Validated / Projected] | [X]% |
| 180 days | $[X] | $[X] | [Validated / Projected] | [X]% |
| 365 days | $[X] | $[X] | [Validated / Projected] | [X]% |

LTV formula: AOV × (1 + repeat rate at N days)
Max CPA formula: (LTV × GM%) − variable fulfillment costs

[INCLUDE THIS BLOCK IF COHORT DATA IS ABSENT:]
⚠️ **Cohort data warning:** The LTV figures above are projected from category
benchmarks, not validated by actual cohort data. Before operating in Scenario
C territory, we recommend pulling 90-day and 180-day cohort reports from
[Klaviyo / Triple Whale / Northbeam] to validate repeat purchase rates.
Running at Scenario C CPAs without validated LTV is a speculative bet.

[INCLUDE THIS BLOCK IF NO RETENTION INFRASTRUCTURE:]
⚠️ **Retention infrastructure warning:** Scenario C requires customers to
return and repurchase. Without active post-purchase email flows and/or SMS,
the projected repeat rates above are unlikely to materialise. We recommend
building retention infrastructure before targeting Scenario C CPAs.

---

## GROWTHHIT RECOMMENDATION

**Recommended scenario: [A / B / C at X-day horizon]**
**Recommended max CPA: $[X]**
**Recommended min ROAS: [X]×**

**Why this scenario:**
[2–3 sentences explaining the specific reasoning for this brand — not generic.
Reference their actual data, their retention infrastructure status, their
category, and their capital position if relevant.]

**What has to be true for this to hold:**
1. [Specific condition — e.g., "Email flows must be generating at least X% repeat purchase rate"]
2. [Specific condition — e.g., "AOV must remain above $X; a drop changes the break-even"]
3. [Specific condition — e.g., "CPA must be measured on new customers only, not blended"]

---

## HOW TO UPDATE THIS MODEL

If any of these inputs change, update the model before changing bid targets:
- AOV changes (pricing, bundle changes, product mix shift)
- Gross margin changes (supplier costs, new product lines)
- Variable costs change (new 3PL, shipping rate changes, returns policy)
- You get 90-day cohort data — this unlocks Scenario C validation
```

---

## Formatting Rules

- Show every formula in plain English alongside the result
- Label every benchmark-derived figure as `[benchmark]`
- Label every projected LTV figure as `[projected]` or `[validated]`
- Use dollar amounts and percentages, not fractions
- Scenario C warning blocks are mandatory when cohort data is absent — never omit them
- The recommendation section must name a specific CPA target, not a range
- Write for a non-financial founder, not an accountant
