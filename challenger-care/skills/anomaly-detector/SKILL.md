---
name: anomaly-detector
description: System skill · runs on schedule to detect anomalies in live Shopify/Klaviyo data. Produces the 'On your plate' alert feed read by the dashboard. Not invoked by users directly. Invoked by scheduled task every 4 hours.
---

> **Permission tier:** n/a (system skill · invoked by scheduled task) · **Tools/context:** assets/goals-targets.md, assets/team-roles.md, assets/unit-economics.md, CONFIG.md, mcp:shopify, mcp:klaviyo

# Anomaly Detector — Logic & Thresholds

The rules that produce "On your plate" alerts in the dashboard. Run on a schedule (every 4 hours, ideally) against live data from connected MCPs. Output a JSON list of alerts that the artifact reads.

---

## How it works

1. Pull current data from connected MCPs (Shopify, Klaviyo when available, GA4 when available)
2. Compare against thresholds + baselines (defined below)
3. Generate a list of alerts, each with: severity, tier, title, description, contract, suggested action
4. Write to a cached output file (Drive: `dashboard/anomaly-feed.json`)
5. Artifact reads this on load

---

## Severity tiers

| Severity | Color | When to use |
|---|---|---|
| **high** | red | Action needed within 24 hours or revenue at risk now |
| **med** | amber | Worth addressing this week |
| **win** | black | Positive signal worth doubling down on |
| **info** | grey | Useful to know, no urgency |

## Action tiers (workflow side, not severity)

Every alert ships with an action button tagged:
- **Generate** (no risk, no commit) — drafts only
- **Stage** (medium risk, reversible) — pre-loads into a tool, requires Execute approval
- **Execute** (high risk, may not be reversible) — live changes or money out

---

## Alert rules · Shopify-driven (live today)

### 1. Inventory restock — `inventory_low`
- **Trigger:** Any SKU with `days_stock_remaining < 25 AND lead_time_days > days_stock_remaining`
- **Severity:** high (if < 14 days), med (14–25 days)
- **Tier:** execute (drafts email to the {{roles.inventory_owner}} + Asana task)
- **Title pattern:** "Reorder [SKU] to avoid stockout"
- **Description:** Include current units, velocity, lead time, recommended order qty
- **Calculation:** `days_stock = (ending_inventory * 30) / units_sold_30d`

### 2. Inventory tracking error — `inventory_tracking_error`
- **Trigger:** Any SKU with `ending_inventory ≤ 0 AND units_sold_30d > 0`
- **Severity:** high
- **Tier:** execute
- **Title pattern:** "[SKU] inventory at [N] — restock + fix tracking"
- **Description:** Bestseller flying off shelves; inventory system shows negative

### 3. AOV gap — `aov_below_target`
- **Trigger:** `avg_aov_7d < (aov_target * 0.7)`
- **Severity:** med (< 70%), high (< 50%)
- **Tier:** generate
- **Title pattern:** "AOV well below target — run the 3-pack reshape"
- **Action prompt:** Fires the "Launch a new bundle or offer" workflow

### 4. Monthly pacing — `monthly_pacing_low`
- **Trigger:** `mtd_revenue < (monthly_goal * (day_of_month / 30) * 0.7)`  
  *(i.e., behind by 30% on prorated pace)*
- **Severity:** med
- **Tier:** generate
- **Action prompt:** "Why did sales drop?" workflow

### 5. Desktop CVR break — `device_cvr_break`
- **Trigger:** `desktop_cvr < (mobile_cvr - 1.0%) AND desktop_sessions > 50`
- **Severity:** high (when desktop near 0%)
- **Tier:** generate
- **Action prompt:** Investigate desktop funnel + propose fixes

### 6. Cart abandonment — `cart_abandonment`
- **Trigger:** `cart_abandonment_rate > 70%`
- **Severity:** med
- **Tier:** generate
- **Action prompt:** Diagnose cart-to-checkout friction

### 7. Checkout abandonment — `checkout_abandonment`
- **Trigger:** `checkout_abandonment_rate > 70%`
- **Severity:** high (> 80%), med (70–80%)
- **Tier:** generate
- **Action prompt:** Diagnose checkout step (shipping, payment, trust)

### 8. Return rate elevated — `return_rate_high`
- **Trigger:** `return_rate_30d > 8%`
- **Severity:** high (> 15%), med (8–15%)
- **Tier:** generate
- **Action prompt:** Cluster refund reasons + propose product/PDP fixes

### 9. Dead / slow-moving SKU — `slow_sku`
- **Trigger:** `units_sold_30d ≤ 2 AND ending_inventory > 500`
- **Severity:** info
- **Tier:** generate
- **Title pattern:** "[N] slow-moving SKUs sitting on inventory"
- **Action prompt:** Recommend bundle / promote / discontinue per SKU
- **Grouping rule:** Combine all qualifying SKUs into one alert when count ≥ 2

### 10. Bundle attach win — `bundle_attach_win`
- **Trigger:** `bundle_attach_rate >= 12% AND < 30%`
- **Severity:** win
- **Tier:** generate
- **Action prompt:** "The 3-pack is working — draft a plan to push attach to 30%+"

### 11. Revenue week-over-week win — `revenue_growth`
- **Trigger:** `revenue_7d > revenue_prev_7d * 1.2`
- **Severity:** win
- **Tier:** generate
- **Action prompt:** "What's driving the growth? Identify + double down."

### 12. Top SKU concentration — `sku_concentration_risk`
- **Trigger:** Top SKU = `> 40%` of weekly revenue AND velocity uneven across SKUs
- **Severity:** info
- **Tier:** generate
- **Action prompt:** Propose bundle ideas that ladder around the hero SKU

### 13. Returning customer rate strength — `retention_strong`
- **Trigger:** `returning_customer_rate_30d >= 30%`
- **Severity:** win
- **Tier:** generate
- **Title pattern:** "Retention is your strongest signal — [N]% returning"
- **Action prompt:** Recommend subscription program emphasis

### 14. Reddit mention spike — `reddit_mention_spike`
- **Trigger:** Reddit mentions in tracked subs `> baseline_weekly * 1.5`
- **Severity:** info (positive) or med (negative sentiment)
- **Tier:** generate
- **Action prompt:** Pull mentions, summarize sentiment, propose response

---

## Alert rules · Klaviyo-driven (activates when connected)

### 15. Flow underperforming — `flow_ctr_drop`
- **Trigger:** Any flow with `ctr_30d < benchmark * 0.7`
- **Severity:** med
- **Tier:** stage (drafts rewrites, stages A/B test)
- **Action prompt:** "Pause + rebuild a broken flow" workflow

### 16. Campaign performance dropped — `campaign_drop`
- **Trigger:** Last campaign's `open_rate < trailing_average * 0.7`
- **Severity:** med
- **Tier:** generate
- **Action prompt:** Diagnose subject line / send time / list health

### 17. Email revenue pacing — `email_revenue_low`
- **Trigger:** `mtd_email_revenue < (monthly_email_goal * (day_of_month / 30) * 0.6)`
- **Severity:** med
- **Tier:** generate
- **Action prompt:** Identify which flow is underdelivering

### 18. List health decline — `list_health`
- **Trigger:** `bounce_rate > 2% OR unsubscribe_rate > 1%`
- **Severity:** high
- **Tier:** execute
- **Action prompt:** Pause sending to bad segments + cleanup

---

## Alert rules · GA4-driven (activates when connected)

### 19. Traffic source shift — `traffic_shift`
- **Trigger:** Any source's `share_of_sessions` shifts `> 30% week-over-week`
- **Severity:** info
- **Tier:** generate
- **Action prompt:** Diagnose source change, identify cause

### 20. Attribution gap — `attribution_gap`
- **Trigger:** `direct_traffic_share > 50%` (suggests UTM tagging missing)
- **Severity:** info
- **Tier:** generate
- **Action prompt:** Recommend UTM tagging setup

---

## Alert rules · cross-tool (multi-MCP)

### 21. Subscriber churn — `subscriber_churn`
- **Trigger:** `subscriber_cancellations_7d > baseline * 1.5`
- **Severity:** high
- **Tier:** generate
- **Action prompt:** Pull cancellation reasons, propose winback

### 22. Voice of customer pattern — `voc_emerging_theme`
- **Trigger:** Same theme mentioned in `≥ 3 reviews/comments in 14 days` (new vs baseline)
- **Severity:** info
- **Tier:** generate
- **Action prompt:** Review the pattern + propose product or PDP change

---

## Output schema

Each alert is one object in a JSON array:

```json
{
  "id": "inventory_low_pomade_4oz"
  "rule": "inventory_low"
  "severity": "high"
  "tier": "execute"
  "title": "Reorder Pomade 4oz to avoid stockout"
  "description": "18 days remaining · 21-day lead time · ~$3,800 wholesale per past PO"
  "contract": "→ Sends drafted email to the {{roles.inventory_owner}} · creates Asana task · no funds move until the {{roles.inventory_owner}} confirms PO"
  "actions": [
    {
      "label": "Send"
      "primary": true
      "prompt": "Draft a restock email to the {{roles.inventory_owner}} for Pomade 4oz. Reference current inventory, velocity, and lead time. Recommend reorder quantity based on historical PO."
    }
    {
      "label": "Wait"
      "primary": false
      "prompt": null
    }
  ]
  "data_source": "shopify.inventory + shopify.sales"
  "generated_at": "2026-06-08T06:14:00Z"
}
```

---

## How Claude reads the rules

When the scheduled task fires:

1. Pull all required data via MCP calls (parallel)
2. Iterate through every rule above
3. For each rule, check if trigger condition is met
4. If met, generate the alert object using the template
5. Write the full array to `dashboard/anomaly-feed.json` in Drive
6. The dashboard reads this file on load and renders "On your plate"

---

## Calibration notes

- **Inventory rules:** Lead times vary by SKU. Pomade lead time = 21 days per past PO. Update per SKU as data accumulates.
- **AOV target = $50** per [unit-economics.md](../../assets/unit-economics.md). When that target shifts, update the multipliers here.
- **Klaviyo benchmarks** by flow type are documented inside the the operating team email skills. Pull from there at runtime.
- **Baselines for traffic, Reddit mentions, etc.** are rolling 30-day averages. Recalculate weekly.

---

## What NOT to alert on

To prevent alert fatigue:

- Don't alert on `revenue_below_average` for individual days — only week trends
- Don't alert on `cvr_drop` for sub-50-session days (statistical noise)
- Don't repeat the same alert within 48 hours unless severity escalates
- Don't surface info-tier alerts when 3+ med/high alerts already in queue (overload)

---

## Future rules to add

- **Subscription cancellations spike** — when Recharge MCP comes online
- **NPS drop** — when survey tool is wired
- **Competitor activity** — handled by separate competitor scan task
- **Ad performance anomalies** — when Meta + Google MCPs come online

---

## When to update this doc

- Add new rules as new data sources come online
- Adjust thresholds when calibration shows noise (too many false positives) or misses
- Document new alert categories that emerge from team feedback
- Quarterly review with the {{roles.founder}} to confirm the rules still match priorities
