---
name: amazon-listing-refresh
description: 'Refreshes Amazon listing copy, A+ content, image stack, and pricing strategy based on review data + brand strategy + competitor moves. Covers the cash engine that gets ~92% of revenue with zero current skill coverage. MANDATORY TRIGGER: any mention of "refresh Amazon listing", "update Amazon copy", "redo A+ content", "Amazon SEO", "Amazon listing audit", "fix the Pomade Amazon listing". Do NOT use this for: Shopify PDP work (use `refresh-underperforming-pdp`). Responding to Amazon reviews (use `respond-to-negative-review`). Inventory restocking (use `inventory-restock`).'
---

> **Permission tier:** stage · **Time:** 6min · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/voc/quote-library.md, assets/competitor-map.md, assets/customer-archetypes.md, assets/team-roles.md, CONFIG.md

# Refresh the Amazon listing

## When to use this workflow

Amazon is the cash engine · roughly 92% of revenue per CONFIG.md and ~1,318 active Subscribe & Save subscribers. Yet the listing copy, A+ content, image stack, and pricing have likely not been refreshed in months. This is the single biggest unaddressed surface in the brand.

Run quarterly OR when:
- Reviews are clustering on a new theme (positive or negative) the listing isn't addressing
- A competitor has launched a comparable product at a better price/positioning
- Conversion rate on Amazon (visible in Seller Central · manual) drops 15%+ month-over-month
- New review insights from `customer-voice` surface ad-ready quotes worth elevating
- Amazon launches new A+ modules or listing features we should adopt

## What you need

- (Required) Which listing(s) to refresh · default: the hero pomade jar
- (Optional) Specific concern · pricing · A+ content · image stack · listing copy · all
- (Optional) Latest VOC export · if customer-voice has surfaced new themes worth incorporating

## What this produces

In `/outputs/amazon/[product-handle]-[date]/`:

1. **`current-state-audit.md`** — What's on Amazon now:
   - Listing title + bullet points + description
   - A+ content modules currently live
   - Image stack (hero + lifestyle + comparison + ingredient · whatever is up)
   - Current price + S&S discount
   - 30-day BSR trend (if manually entered in CONFIG.md or pasted)
   - Recent review themes (loads from `voc/quote-library.md`)
2. **`refreshed-listing.md`** — Full rewrite:
   - **Listing title** · keyword-optimized · ≤200 chars per Amazon rules · loads claim library to avoid banned terms ("cures", "treats", etc.)
   - **5 bullet points** · each in Challenger voice · result-led · loads from `voc/quote-library.md` for proof points
   - **Long description** · 2000 chars max · positioning anchor (the brand idea from CONFIG · `brand.brand_idea`)
   - **Backend keywords** · 250 chars · the long-tail search terms not in the title
3. **`a-plus-content-brief.md`** — A+ modules to ship:
   - Module 1 · hero benefit (result-led headline + lifestyle image direction)
   - Module 2 · what we remove (fragrance-free · sulfate-free · etc. · loaded from `brand-strategy.md`)
   - Module 3 · who it's for (specific use cases from `customer-archetypes.md`)
   - Module 4 · how to use (precise routine with time investment)
   - Module 5 · comparison table (vs the dominant competitor per `competitor-map.md`)
   - Module 6 · brand story (founder voice · loaded from `brand-strategy.md`)
4. **`image-stack-direction.md`** — Briefs for new product photography if needed:
   - Hero shot (jar + texture · isolated)
   - Lifestyle (in-use · target archetype context)
   - Comparison (vs competitor · vs petroleum-based · loaded from competitor-map)
   - Ingredient (what's in · what's not · visual)
   - Result (before/after style · subject to claim library limits)
   - Routine (the full routine spread · cross-sell visual)
5. **`pricing-recommendation.md`** — Should the price move? Should S&S discount change?
   - Current price vs competitor matrix (loaded from `competitor-map.md`)
   - Unit economics impact at each price point (loaded from `unit-economics.md`)
   - S&S discount sensitivity model (5% / 10% / 15% scenarios)
   - Recommendation + reasoning
6. **`approval-checklist.md`** — What the `roles.execute_tier_approver` decides before any of this ships to Amazon

## How Claude runs it

1. Load `brand-strategy.md` · voice rules + brand idea + campaign platform
2. Load `claim-library.md` · what we can/can't say on Amazon (Amazon has stricter rules than the brand itself)
3. Load `voc/quote-library.md` · find 5-8 ad-ready quotes that match the current review theme
4. Load `customer-archetypes.md` · primary archetype for this product (typically Preparer + Sensitive Buyer for pomade)
5. Load `competitor-map.md` · pull current state of Based, Hanz De Fuko, Paul Mitchell · what they're claiming · how they're priced
6. Load `unit-economics.md` · COGS, margin, S&S impact
7. Generate current state audit (pull from Seller Central if accessible · otherwise note as manual entry)
8. Rewrite the listing using the Amazon-specific template (title → bullets → long description → backend)
9. Brief A+ content modules per the 6-module structure
10. Brief image stack with shot list
11. Run pricing analysis with the 3 scenarios
12. Generate the approval checklist
13. Output all 6 docs · notify `roles.execute_tier_approver`

## Amazon-specific voice constraints

Amazon is stricter than Shopify:

- No external URLs in listing copy
- No "limited time" or scarcity claims in the listing (only ads)
- No prohibited medical terms (`claim-library.md` has the full list · Amazon also bans "FDA-approved", "cure", "heal" universally)
- No comparison to specific competitor brand names in the listing copy itself (allowed in A+ comparison module)
- Title char limit · 200 max per category
- Bullets · 500 chars max each
- Backend keywords · 250 chars total, no commas, no duplicates from title

Reads `claim-library.md` to verify nothing slips in.

## Permission tier

**Stage** · the refresh is drafted and staged in Seller Central but doesn't go live until `roles.execute_tier_approver` (per CONFIG) signs off.

Why stage and not generate: Amazon listing changes affect 92% of revenue. A bad refresh tanks rank for 6-12 months.

## Example prompts that trigger this

- "Refresh the Pomade Amazon listing"
- "Update Amazon A+ content"
- "Run the Amazon listing audit"
- "The Amazon BSR has dropped · what should the listing do differently?"

## Don't use this for

- Shopify PDP work (use `refresh-underperforming-pdp`)
- Responding to specific Amazon reviews (use `respond-to-negative-review`)
- Restock decisions (use `inventory-restock`)
- General competitor scan (use `whats-the-competitor-doing`)

## Notes

- This skill currently has no live Amazon Seller Central MCP. The state pull is manual until that connector exists. Document the manual paste points in the output.
- The cash engine has zero current skill coverage · running this once per quarter is the floor.
- The 1,318 S&S subscribers depend on this listing staying healthy · a stockout-driven listing suppression cascades to S&S cancellations within Amazon's UI · pair with `inventory-restock` monitoring.

