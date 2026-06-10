---
name: launch-new-product
description: Turns a product idea into a complete launch package in Challenger voice — positioning, PDP copy, ad concepts, launch email, social briefs, Reddit post, Asana checklist. MANDATORY TRIGGER: any mention of "Launch [product name]", "Let's launch the new shower bar in 2 weeks", "I want to ship [product] — give me everything". Do NOT use this for: Existing product refreshes (use `refresh-underperforming-pdp` instead). Bundle launches specifically (use `launch-new-bundle-or-offer` — bundle math is different). Sale/promo campaigns (use `launch-sale-promo`).
---

> **Permission tier:** generate · **Time:** 5min · **Tools/context:** assets/brand-strategy.md, assets/unit-economics.md, assets/claim-library.md, assets/customer-archetypes.md, voc/quote-library.md

# Launch a new product

## When to use this workflow

You have a new SKU about to ship and need every asset built in Challenger voice — consistently, in one pass.

## What you need

- Product name + 1-line description
- Key product proof points (hold level, finish, fragrance posture, etc.)
- Target launch date
- (Optional) Primary archetype to lead with — Preparer, Switcher, Sensitive Buyer, etc.

## What this produces

All in `/outputs/launches/[product-name]/`:

1. **`positioning.md`** — One-paragraph positioning statement using the brand book pillars (Preparation · Performance · Challenge)
2. **`pdp-shopify.md`** — Full Shopify PDP per the brand book template (hero benefit · who it's for · why it's different · how to use · what to pair with · review proof · routine CTA)
3. **`pdp-amazon.md`** — Amazon A+ content (hero · problem/solution · benefit stack · how-to · comparison · bundle recommendation · review quote module)
4. **`ad-concepts.md`** — 3 ad concepts (one per messaging pillar) with hook + body + CTA
5. **`launch-email.html`** — Klaviyo-ready HTML for the announcement send
6. **`reddit-post.md`** — Founder-voice Reddit post (not brand voice) for r/malegrooming
7. **`tiktok-scripts.md`** — 3 short TikTok scripts (hook + body + CTA) for the Implicit agency
8. **`asana-launch-checklist.md`** — Launch task list with owners and dates

## How Claude runs it

1. Load `brand-strategy.md` — voice rules, 3 pillars, campaign territories
2. Load `claim-library.md` — what we can and can't say
3. Load `unit-economics.md` — pricing validation, bundle math if relevant
4. Load `customer-archetypes.md` — pick the lead archetype
5. Search `../../assets/voc/quote-library.md` for the closest theme matches (e.g., new pomade → pull from hold + fragrance-free + grease-free themes)
6. Generate positioning anchored to one of the 3 pillars
7. Build the Shopify PDP using the brand book template (hero benefit → who → why different → how to use → pair with → proof → CTA)
8. Build the Amazon listing using product-benefit-first hierarchy
9. Generate 3 ad concepts — one per pillar (Preparation · Performance · Challenge)
10. Write launch email — subject line "dare-flavored," hero copy anchors to Preparation pillar
11. Write Reddit post in **founder voice** (first person, opinion-led, NOT brand voice)
12. Write 3 TikTok scripts — scroll-stoppers using the Challenge or Performance pillar
13. Build Asana checklist with realistic dates

## Voice check before output

Run every customer-facing draft through the brand book quick checklist:
- Leads with a result, not an ingredient
- Anchors to time investment somewhere
- Sounds like a man with standards, not trying to prove something
- At least one of the 3 pillars present
- Approved words used freely · max one "use carefully" word · zero "banned" words
- Beauty-brand test: if a beauty brand could publish this unchanged, rewrite

## Permission tier

**Generate** — all drafts, no live changes. the {{roles.founder}} + the {{roles.marketing_coordinator}} review before anything ships.

## Example prompts that trigger this

- "Launch [product name]"
- "Let's launch the new shower bar in 2 weeks"
- "I want to ship [product] — give me everything"

## Don't use this for

- Existing product refreshes (use `refresh-underperforming-pdp` instead)
- Bundle launches specifically (use `launch-new-bundle-or-offer` — bundle math is different)
- Sale/promo campaigns (use `launch-sale-promo`)
