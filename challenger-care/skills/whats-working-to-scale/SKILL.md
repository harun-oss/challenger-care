---
name: whats-working-to-scale
description: 'Finds the top-performing creative, email, landing page, and SKU - recommends where to put more weight. MANDATORY TRIGGER: any mention of "What''s working that I should double down on?", "Where should I put more attention this quarter?", "Find the wins from last 30 days". Do NOT use this for: Diagnosing what''s broken (use `why-sales-dropped`). Setting up new tests (use `test-price-claim`). Strategic positioning decisions (use `highest-leverage`).'
---

> **Permission tier:** generate · **Time:** 3min · **Tools/context:** mcp:shopify, mcp:klaviyo (optional), assets/unit-economics.md

# What's working that I can scale?

## When to use this workflow

You have working channels / SKUs / campaigns and want to identify where doubling down would pay off — vs. spreading attention thin across underperformers.

## What you need

- Time frame (last 30 days, last quarter, etc.)
- (Optional) Specific dimension to focus on (creative, email, SKU, channel)

## What this produces

1. **Top performers identified** in each dimension:
   - Top SKU by revenue + by sell-through
   - Top email (flow or campaign) by revenue per send
   - Top landing page by CVR
   - Top traffic source by revenue per session
   - Top customer segment (if data available)
2. **Why it's working** — 1–2 sentence diagnosis per winner
3. **Scale recommendations** — what to amplify, where to put more budget / effort / time
4. **Risks** — what could break if scaled (concentration risk, cannibalization, etc.)

Lands in `Drive/scale-analysis/[date].md`.

## How Claude runs it

1. Pull 30d sales by SKU from Shopify · rank by revenue, sell-through, AOV contribution
2. Pull traffic source revenue from Shopify (or GA4 when connected) · rank
3. If Klaviyo connected: pull flow + campaign revenue per send · rank
4. Identify clear winners (statistically meaningful, not noise)
5. Diagnose why each winner is working
6. Recommend scale moves (e.g., "the 3-pack is 14% attach — push to 30% with hero placement")
7. Flag concentration risks (e.g., "if Clean Pomade 3oz is 40% of revenue, diversification matters")

## Permission tier

**Generate** — analysis only, no changes. Output informs decisions about budget, hero placement, content focus.

## Example prompts that trigger this

- "What's working that I should double down on?"
- "Where should I put more attention this quarter?"
- "Find the wins from last 30 days"

## Don't use this for

- Diagnosing what's broken (use `why-sales-dropped`)
- Setting up new tests (use `test-price-claim`)
- Strategic positioning decisions (use `highest-leverage`)
