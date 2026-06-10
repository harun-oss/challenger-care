---
name: why-sales-dropped
description: 'Pulls Shopify + GA4 + Klaviyo together, diagnoses where the funnel broke this week, gives 3 most likely causes with evidence. MANDATORY TRIGGER: any mention of "Why is revenue down this week?", "Sales dropped - what happened?", "We''re at 60% of last month''s pace, why?". Do NOT use this for: Single-day anomalies (statistical noise - wait 3 days). Forward-looking forecasts (this is diagnostic, not predictive). Customer feedback diagnostics (use `customer-voice` for that).'
---

> **Permission tier:** generate · **Time:** 3min · **Tools/context:** mcp:shopify, mcp:ga4 (optional), mcp:klaviyo (optional), assets/unit-economics.md

# Why did sales drop?

## When to use this workflow

Revenue this week is lower than last week / last month / expectation, and you want a diagnostic answer fast — not a guess.

## What you need

- Time frame to diagnose (this week, this month, since X date)
- (Optional) Specific suspicion to investigate (e.g., "I think it's a Klaviyo flow break")

## What this produces

1. **Diagnostic summary** — 1 paragraph: what's happening, when it started
2. **Funnel comparison** — current period vs. baseline at each stage (sessions, ATC, checkout, completed)
3. **Channel breakdown** — where the drop is concentrated (which source, which device, which page)
4. **Top 3 likely causes** with evidence (e.g., "Mobile CVR dropped 18% Tuesday — correlates with PDP image change")
5. **Recommended next actions** — 1–3 fixes ranked by impact / effort

Lands in `Drive/diagnostics/[date]-revenue-drop.md`.

## How Claude runs it

1. Pull current period revenue, orders, AOV, CVR from Shopify
2. Pull baseline (prior period, same length) from Shopify
3. If GA4 connected: pull traffic source breakdown for both periods
4. If Klaviyo connected: pull flow + campaign performance for both periods
5. Identify the stage(s) where the drop happened
6. Look for correlating events (PDP changes, paused flows, traffic source shifts, inventory issues)
7. Rank 3 most likely causes by evidence strength
8. Recommend next workflows to run (e.g., `pause-rebuild-flow`, `refresh-pdp`)

## Permission tier

**Generate** — diagnostic only. No changes are made. Recommends next actions but doesn't execute them.

## Example prompts that trigger this

- "Why is revenue down this week?"
- "Sales dropped — what happened?"
- "We're at 60% of last month's pace, why?"

## Don't use this for

- Single-day anomalies (statistical noise — wait 3 days)
- Forward-looking forecasts (this is diagnostic, not predictive)
- Customer feedback diagnostics (use `customer-voice` for that)
