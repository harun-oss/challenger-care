---
name: refresh-underperforming-pdp
description: Diagnoses why a PDP isn't converting, then rebuilds the hero + benefits + FAQ + CTAs in Challenger voice anchored to real VOC quotes. MANDATORY TRIGGER: any mention of "Refresh the Clean Cream Pomade PDP", "Rebuild the Matte 3oz PDP — it's converting badly", "Update the Body Wash PDP — it's a slow mover". Do NOT use this for: A new product (use `launch-new-product`). Collection / category pages (PDP only). General website copy refresh (different scope).
---

> **Permission tier:** stage · **Time:** 5min · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/customer-archetypes.md, voc/quote-library.md, mcp:shopify, CONFIG.md

# Refresh an underperforming PDP

## When to use this workflow

A product page isn't converting well — CVR below site average, high bounce, or just hasn't been updated since 2024. This rebuilds it from the ground up in Challenger voice.

## What you need

- Product URL or product handle (e.g., `challenger-clean-hair-pomade-3oz`)
- (Optional) Suspected issue ("hero is too generic" · "no proof points" · "CTA is weak")

## What this produces

All in `/outputs/pdps/[product-handle]/`:

1. **`current-state-audit.md`** — What's there now (pulled from Shopify), what's missing per the brand book template, what's off-voice
2. **`pdp-rewrite-full.md`** — Complete rewrite using the brand book Shopify PDP template:
   - Hero benefit (one-sentence result claim)
   - Who it's for (specific Challenger-man use case)
   - Why it's different (vs. petroleum / fragrance-heavy / heavy-shine alternatives)
   - How to use (precise routine with time investment)
   - What to pair with (2 routine cross-sells)
   - Review proof (2 verbatim quotes from VOC)
   - Routine CTA
3. **`hero-variants.md`** — 3 alternative hero copy options for A/B testing
4. **`faq-block.md`** — 6–8 FAQ entries based on real customer questions from VOC + likely objections
5. **`a-b-test-plan.md`** — How to test the rewrite vs. the current PDP (segment, duration, success metric)

## How Claude runs it

1. Pull current PDP content from Shopify (`get-product` with the handle)
2. Pull last 30 days of Shopify performance for that product (sessions, ATC, completed, CVR)
3. Load `brand-strategy.md` — Shopify PDP template + voice rules
4. Load `claim-library.md` — confirm every claim is approved · flag any banned language in the current PDP
5. Load `customer-archetypes.md` — identify the primary archetype this product serves
6. Search `../../assets/voc/quote-library.md` for the strongest quotes on themes relevant to this product:
   - Pomade → hold + fragrance-free + grease-free + acne
   - Shampoo → cleansing + scalp + scent posture + value
   - Body wash → cleansing + scent posture + skin
7. Audit the current state against the brand book template — what's missing, what's off-voice
8. Rewrite using the template structure
9. Generate 3 hero variants using different brand book headline formulas:
   - Result + restriction
   - Time + payoff
   - Dare frame (for the bolder test)
10. Build FAQ from real customer questions in VOC + objections worth addressing
11. Design the A/B test (which variants, segment, sample size, duration)

## Voice check on every section

- Hero must lead with a **result**, not an ingredient
- Time investment anchored somewhere
- "Who it's for" should specify a real use case (the morning before the client meeting, the gym before work, the cologne already on)
- Review proof — use 2 specific results-led quotes · NOT "I love it" generic praise
- CTA at brand layer = "Accept the challenge" · at conversion layer = "Shop the routine" / "Find your hold"

## Permission tier

**Stage** — Rewrite gets staged in Shopify (or Pagefly) but stays unpublished. Hero variants ready for A/B test setup. the {{roles.execute_tier_approver}} approves before going live.

## Example prompts that trigger this

- "Refresh the Clean Cream Pomade PDP"
- "Rebuild the Matte 3oz PDP — it's converting badly"
- "Update the Body Wash PDP — it's a slow mover"

## Don't use this for

- A new product (use `launch-new-product`)
- Collection / category pages (PDP only)
- General website copy refresh (different scope)

## Special note on slow movers (Body Wash · Tea Tree Shampoo)

Per VOC + dashboard data, these SKUs are barely moving (2 units/month). When this workflow runs on them, suggest a SKU-strategy review BEFORE rewriting:
- Could they be bundled with the hero pomade?
- Could they be re-positioned as part of "the complete routine"?
- Is the SKU worth keeping vs. discontinuing?

A new PDP doesn't fix a SKU-mix problem. Flag this to the {{roles.founder}} if the PDP rewrite isn't the right intervention.
