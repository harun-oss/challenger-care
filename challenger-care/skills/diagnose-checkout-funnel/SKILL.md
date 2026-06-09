---
name: diagnose-checkout-funnel
description: Investigates a specific funnel-stage problem — cart abandonment, checkout drop-off, device-specific CVR issues — surfaces top causes with evidence. MANDATORY TRIGGER: any mention of "Why is checkout abandonment at 77%?", "Desktop converting at 0% — what's broken?", "Diagnose the cart-to-checkout drop", "Where are we leaking customers?". Do NOT use this for: Generic "sales dropped" (use `why-sales-dropped` — broader). Email funnel issues (use `fix-broken-flow`). Product-page-specific issues with no funnel data context (use `refresh-pdp` once it's available).
---

> **Permission tier:** generate · **Time:** 3min · **Tools/context:** mcp:shopify, mcp:ga4 (optional), knowledge/unit-economics.md

# Diagnose the checkout funnel

## When to use this workflow

The dashboard flags a funnel issue (high cart abandonment, high checkout abandonment, device-specific CVR break) and you want a deeper diagnosis with specific fix recommendations.

## What you need

- The specific issue to investigate (e.g., "desktop CVR is 0%" or "checkout abandonment at 77%")
- (Optional) Time window (default last 30 days)

## What this produces

1. **Stage-by-stage funnel map** — sessions → ATC → checkout → completed, with conversion rate at each step
2. **Device + source segmentation** — where the problem concentrates (mobile · desktop · which traffic source)
3. **Correlation analysis** — what changed when the problem started (recent PDP edits, page speed shifts, traffic source changes, payment method changes)
4. **Top 3 likely root causes** ranked by evidence strength:
   - e.g., "PDP image change on Tuesday correlates with mobile load time +1.4s and 18% CVR drop"
5. **Fix recommendations** — specific, prioritized by impact × ease
6. **Reversal test plan** — if you ship a fix, how to confirm it worked

Lands in `Drive/diagnostics/[issue-name]-[date].md`.

## How Claude runs it

1. Pull full Shopify funnel data — sessions, cart additions, checkout reached, completed — for current + baseline period
2. Pull device split + traffic source split
3. Pull page-level CVR if accessible
4. Check for correlations with recent site changes (Shopify edit history if available)
5. Rank likely causes by evidence
6. Recommend specific fixes (e.g., "audit PDP load time" · "review shipping cost display" · "test payment options")
7. Define the test to validate any fix

## Permission tier

**Generate** — diagnostic only. Recommends actions, doesn't execute them. Subsequent workflows (PDP refresh, test setup) handle implementation.

## Example prompts that trigger this

- "Why is checkout abandonment at 77%?"
- "Desktop converting at 0% — what's broken?"
- "Diagnose the cart-to-checkout drop"
- "Where are we leaking customers?"

## Don't use this for

- Generic "sales dropped" (use `why-sales-dropped` — broader)
- Email funnel issues (use `fix-broken-flow`)
- Product-page-specific issues with no funnel data context (use `refresh-pdp` once it's available)
