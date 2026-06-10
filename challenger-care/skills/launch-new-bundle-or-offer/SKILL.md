---
name: launch-new-bundle-or-offer
description: Builds a complete bundle/offer launch — validates bundle math, drafts hero + cart upsell + offer landing page + promo email + first-week ad concepts. Tuned for the 3-pack as the AOV anchor. MANDATORY TRIGGER: any mention of "Launch the 3-pack as the new default offer", "Build a starter kit", "Make a Father's Day gift bundle", "Test a $50 vs $65 price point for the 3-pack". Do NOT use this for: Discount-led sales (use `launch-sale-promo`). New individual SKUs (use `launch-new-product`). Subscription onboarding (use `onboard-new-subscribers`).
---

> **Permission tier:** stage · **Time:** 4min · **Tools/context:** assets/brand-strategy.md, assets/unit-economics.md, assets/claim-library.md, assets/customer-archetypes.md, voc/quote-library.md, mcp:shopify, CONFIG.md

# Launch a new bundle or offer

## When to use this workflow

You're launching a new bundle (most importantly the 3-pack as default offer), a value pack, or a structured offer (gift set, starter kit). This is the **highest-leverage AOV move** Challenger can make.

## What you need

- Bundle SKUs (which products are in it)
- Target retail price
- (Optional) Discount vs. buying separately
- Target launch date
- Is this a permanent SKU or a limited-time offer?

## What this produces

All in `/outputs/launches/[bundle-name]/`:

1. **`bundle-math.md`** — Validation against `unit-economics.md`:
   - Bundle COGS · contribution per order
   - AOV impact vs. current
   - CAC headroom unlocked
   - Profitability at the proposed price
   - Recommendation: ship, adjust price, or rethink
2. **`pdp-hero.md`** — Bundle PDP hero · product name · subhead · price reveal · CTA (per brand book template)
3. **`cart-upsell.md`** — Cart-add upsell module copy (when a single jar is in cart, prompt to upgrade)
4. **`offer-landing-page.md`** — Full landing page copy for paid traffic destination
5. **`promo-email.html`** — Klaviyo-ready announcement email
6. **`ad-concepts.md`** — 3 ad concepts using the bundle as the hero — one per messaging pillar
7. **`first-week-content.md`** — Reddit post + 2 TikTok scripts to seed the launch organically

## How Claude runs it

1. Load `unit-economics.md` — calculate bundle math
2. Validate math: contribution margin must stay above 50% per the unit-economics rule
3. If math fails → flag the issue, propose a price adjustment, stop
4. If math passes → proceed
5. Load `brand-strategy.md` + `claim-library.md`
6. Load `customer-archetypes.md` — bundles primarily serve The Preparer + The Wife/Mom archetypes
7. Search `../../assets/voc/quote-library.md` for repeat-buyer + subscription-worthy quotes (these speak to bundle value)
8. Generate PDP hero anchored to brand idea: *"Show up sharper."* · campaign platform: *"One minute. Every room."*
9. Bundle math should be reframed as customer benefit: 3-pack = 100 days of confident mornings, not "3 jars in a bag"
10. Cart upsell uses **dare frame** ("Most guys grab one. Challenger men grab three") OR **value frame** ("100 days for the price of a haircut and a half")
11. Email subject lines test 3 framings: time-payoff · result-restriction · dare
12. Ad concepts: one Preparation-led · one Performance-led · one Challenge-led

## Voice check

Same as `launch-new-product` — run every draft through the brand book quick checklist before output.

**Special bundle framing rule:** Never describe a bundle as just "savings" or "deal." Frame as a **commitment to the standard** — per the brand book, "Prepared is a standard."

## Permission tier

**Stage** — PDP draft + email get staged in Shopify + Klaviyo respectively. Bundle math + ad concepts are Generate-tier. The Stage actions need the {{roles.founder}}'s explicit go before going live.

## Example prompts that trigger this

- "Launch the 3-pack as the new default offer"
- "Build a starter kit"
- "Make a Father's Day gift bundle"
- "Test a $50 vs $65 price point for the 3-pack"

## Don't use this for

- Discount-led sales (use `launch-sale-promo`)
- New individual SKUs (use `launch-new-product`)
- Subscription onboarding (use `onboard-new-subscribers`)

## Special note on the 3-pack

The 3-pack is the **single highest-leverage AOV move** for Challenger right now. When this workflow is used for the 3-pack specifically:
- Position as the **default offer**, not as an upsell
- The 110-day jar math is the hero (100 days of mornings per pack)
- Bundle attach rate is the success metric · target 30%+ within 90 days
- This is the move that unlocks profitable paid acquisition · everything else is downstream
