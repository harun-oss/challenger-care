---
name: test-price-claim
description: Designs an A/B test for a price point or product claim — variants, segment, duration, success metric — stages it for review. MANDATORY TRIGGER: any mention of "Should we test $50 vs $65 for the 3-pack?", "Test fragrance-free vs unscented as the hero claim", "I want to A/B the PDP hero image". Do NOT use this for: Email subject line tests inside Klaviyo (that's a Klaviyo-internal test, handled in `launch-sale-promo` or flow workflows). Multi-variable experiments (each variable should be its own test).
---

> **Permission tier:** stage · **Time:** 3min · **Tools/context:** assets/unit-economics.md, assets/claim-library.md

# Test a price point or claim

## When to use this workflow

You want to validate a hypothesis without committing — does $50 outperform $45 for the 3-pack? Does "fragrance-free" beat "unscented" as a hero claim?

## What you need

- The variable you're testing (price, headline, hero image, claim)
- 2–3 variants
- A hypothesis you want to confirm or kill (e.g., "I think $50 will hold AOV without hurting CVR")

## What this produces

1. **Test plan brief** with:
   - Variable + variants
   - Hypothesis
   - Success metric (CVR? AOV? Revenue per visitor?)
   - Sample size needed for statistical confidence
   - Duration estimate (based on current traffic from Shopify)
   - Audience segment (who sees the test)
   - Cleanup logic (winner promoted, loser archived)
2. **Variant copy/spec** — each variant fully defined
3. **Tracking plan** — how to read results when test concludes
4. **Decision tree** — when to ship winner, when to keep running, when to kill

Lands in `Drive/tests/[test-name]/`.

## How Claude runs it

1. Pull current Shopify session volume (from MCP) to size sample
2. Pull AOV / CVR baseline from last 30d
3. Validate variants against `../../assets/claim-library.md` (no banned claims)
4. If pricing test: validate against `../../assets/unit-economics.md` (no margin-killers)
5. Calculate required sample size + duration based on baseline + expected effect size
6. Build the test brief
7. Define the cleanup/decision rules

## Permission tier

**Stage** — Builds the test plan. the {{roles.execute_tier_approver}} reviews. The actual A/B implementation happens in Shopify / Pagefly / Klaviyo by the {{roles.marketing_coordinator}} or the {{roles.founder}}.

## Example prompts that trigger this

- "Should we test $50 vs $65 for the 3-pack?"
- "Test fragrance-free vs unscented as the hero claim"
- "I want to A/B the PDP hero image"

## Don't use this for

- Email subject line tests inside Klaviyo (that's a Klaviyo-internal test, handled in `launch-sale-promo` or flow workflows)
- Multi-variable experiments (each variable should be its own test)
