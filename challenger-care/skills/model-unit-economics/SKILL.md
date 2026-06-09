---
name: model-unit-economics
description: Builds the contribution margin stack, LTV at 90/180/365 days, and max CPA scenarios. MANDATORY TRIGGER: any mention of "What's our max CPA if Meta gets reactivated?", "Model the 3-pack at $65 — is it profitable?", "If subscription attach hits 25%, what changes?", "Run unit economics on the wholesale opportunity". Do NOT use this for: Real-time CPA tracking (that's the ads weekly report when Meta + Google connect). Brand strategy decisions (use `highest-leverage`). Single-promo pricing decisions (use `launch-sale-promo` — references this workflow internally).
---

> **Permission tier:** generate · **Time:** 4min · **Tools/context:** mcp:shopify, assets/unit-economics.md

# Model my unit economics

## When to use this workflow

Before any pricing decision, paid acquisition reactivation, bundle launch, or subscription strategy change. The numbers that decide what's profitable.

## What you need

- The scenario to model (e.g., "if we launch the 3-pack at $65" or "if Meta CPA is $40")
- (Optional) Override default assumptions (LTV horizon, shipping cost, payment fees)

## What this produces

1. **Contribution margin stack** for the scenario:
   - Revenue
   - COGS
   - Shipping
   - Payment fees
   - Contribution per order (dollars + %)
2. **LTV projections** at 3 horizons:
   - 90-day (first cycle)
   - 180-day (second cycle, if subscription)
   - 365-day (full year)
3. **Max CPA scenarios**:
   - First-purchase profitable cap
   - Break-even with 1 repeat
   - Loss-leader with LTV upside (assumes subscription attach rate)
4. **Decision read** — is this profitable, break-even, or LTV-funded?
5. **Sensitivities** — what changes the answer (subscription attach rate, repeat rate, COGS shifts)

Lands in `Drive/financial-models/[scenario].md`.

## How Claude runs it

1. Pull defaults from `../../assets/unit-economics.md` — COGS, margin, AOV, shipping cost, jar duration
2. Pull current Shopify customer behavior — repeat rate, AOV, subscription attach
3. Build the contribution stack for the scenario
4. Project LTV at each horizon using current repeat rate as baseline
5. Calculate max CPA scenarios
6. Surface sensitivities (which inputs change the answer the most)
7. Make the decision recommendation

## Permission tier

**Generate** — modeling only. Output informs decisions but doesn't change anything live.

## Example prompts that trigger this

- "What's our max CPA if Meta gets reactivated?"
- "Model the 3-pack at $65 — is it profitable?"
- "If subscription attach hits 25%, what changes?"
- "Run unit economics on the wholesale opportunity"

## Note on LTV reliability

Shopify cohort data is currently thin (limited order volume). LTV projections use Amazon S&S subscriber behavior as a proxy (1,318 subs, 110-day cadence). Confidence improves as Shopify scale grows. Workflow flags this in the output.

## Don't use this for

- Real-time CPA tracking (that's the ads weekly report when Meta + Google connect)
- Brand strategy decisions (use `highest-leverage`)
- Single-promo pricing decisions (use `launch-sale-promo` — references this workflow internally)
