---
name: tiktok-shop-launch-prep
description: Preps the catalog, content angles, and success metrics for TikTok Shop launch with the Implicit agency. This skill briefs Implicit and gives the team a hand-off doc · it does NOT run TikTok Shop (that is explicitly out of scope per the engagement SOW · Implicit owns execution). MANDATORY TRIGGER: any mention of "prep TikTok Shop", "TikTok Shop launch", "brief Implicit", "TikTok Shop catalog", "TikTok content angles". Do NOT use this for: Running TikTok Shop campaigns (Implicit owns that). TikTok organic content from Implicit (use `create-this-weeks-content`). Paid TikTok ads (different skill set · not in scope).
---

> **Permission tier:** generate · **Time:** 5min · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/voc/quote-library.md, assets/customer-archetypes.md, assets/unit-economics.md, assets/team-roles.md, CONFIG.md

# TikTok Shop launch prep (brief Implicit)

## When to use this workflow

TikTok Shop launch is in flight with the Implicit agency. They own execution. This skill produces the hand-off package that gives Implicit everything they need to run it well: catalog readiness, content angles from VOC, brand guardrails, success metrics for measurement.

Run once at the start of the engagement. Re-run quarterly as the catalog evolves or the content angles need a refresh.

**Scope guardrail:** TikTok Shop execution is explicitly out of scope per the engagement SOW. This skill produces the brief · Implicit produces the campaigns.

## What you need

- (Required) Confirmation that Implicit is the executing party
- (Optional) Initial catalog scope · default: full hero pomade jar + 3-pack bundle
- (Optional) Specific content angles to push or avoid · default: pull from VOC themes

## What this produces

In `/outputs/tiktok-shop/[date]-launch-brief/`:

1. **`catalog-readiness.md`** — What needs to ship to TikTok Shop on day 1:
   - SKU list with pricing (loaded from CONFIG.md · `unit_economics.cogs_per_jar_usd` and current pricing)
   - Inventory commitment · how many units allocated to TikTok Shop fulfillment
   - Shipping setup · TikTok Shop's fulfillment options vs Shopify pickup
   - Product images requirement · TikTok Shop's specific formats (different from Amazon/Shopify)
   - Compliance check · TikTok Shop bans on certain claim language · cross-reference `claim-library.md`

2. **`content-angles.md`** — The hooks Implicit's creators will pull from:
   - 5-7 hooks loaded from `voc/quote-library.md` · ranked by ad-readiness
   - Each hook with the underlying customer pain it taps
   - Mapped to customer archetypes (loaded from `customer-archetypes.md`) · primarily Reddit Discoverer + Switcher for TikTok
   - Brand voice rules (loaded from `brand-strategy.md`) · what works on TikTok (peer-to-peer, dare-flavored) vs what doesn't (corporate, hedged)
   - Banned language list pulled from `claim-library.md` (medical claims, "cures", etc.)

3. **`success-metrics.md`** — How we measure TikTok Shop performance:
   - North star · monthly TikTok Shop GMV
   - Leading indicators · CTR on creator videos · add-to-cart rate · cart conversion
   - Lagging indicators · 30-day repeat purchase rate from TikTok Shop buyers
   - Attribution setup · UTMs · TikTok Pixel · cross-reference with Shopify cohort tagging
   - Cadence · weekly Slack update from Implicit · monthly performance review
   - The threshold for "this is working" vs "this is a learning experiment"

4. **`brand-guardrails.md`** — What Implicit's creators can and cannot do:
   - Voice rules from `brand-strategy.md` (the full language bank)
   - Banned claims from `claim-library.md` (Amazon-style stricter rules apply for TikTok Shop)
   - Approved comparison points vs competitors (loaded from `competitor-map.md`)
   - When to escalate vs ship · disclosure rules · what needs `roles.execute_tier_approver` approval

5. **`measurement-cadence.md`** — How the brand stays in the loop without owning execution:
   - Weekly Slack update from Implicit (what shipped · what's running · what's queued)
   - Monthly performance call (numbers · learnings · next month plan)
   - Quarterly strategic review · is TikTok Shop pulling its weight · do we expand or pull back

## How Claude runs it

1. Load `brand-strategy.md` · the full voice rules and language bank
2. Load `claim-library.md` · both Challenger's rules and known TikTok Shop platform rules (stricter than Shopify · closer to Amazon)
3. Load `voc/quote-library.md` · pull top 5-7 ad-ready quotes scoring high on TikTok-style hooks (specific results, relatable use cases, peer-to-peer voice)
4. Load `customer-archetypes.md` · TikTok skews Reddit Discoverer + Switcher · note the demographic skew
5. Load `unit-economics.md` · COGS, margin, pricing constraints
6. Load `competitor-map.md` · what Based does on TikTok (heavy TikTok presence per the brand context)
7. Load `team-roles.md` + CONFIG.md · who's the point of contact with Implicit (typically `roles.marketing_coordinator`)
8. Generate the 5 docs in sequence
9. Output to `/outputs/tiktok-shop/[date]-launch-brief/`
10. The hand-off doc gets sent to Implicit · the team keeps the copy

## What this skill explicitly DOES NOT do

- Run TikTok Shop campaigns (Implicit's job · out of scope per SOW)
- Brief individual creators (Implicit's job · the creators come from Implicit's roster)
- Build the TikTok Shop catalog technically (Shopify integration handles that · or Implicit's tech team)
- Produce TikTok content (Implicit produces · this skill briefs)
- Replace `create-this-weeks-content` · that's organic across all channels · this is TikTok Shop specifically

## Permission tier

**Generate** · the brief is a hand-off doc · no live changes · no money out. Safe for anyone on the team to produce.

Final approval of the brief before sending to Implicit goes through `roles.execute_tier_approver` (per CONFIG.md) since it commits brand voice and inventory to a partner agency.

## Example prompts that trigger this

- "Prep the TikTok Shop launch brief for Implicit"
- "Build the TikTok Shop catalog and content brief"
- "What does Implicit need from us for TikTok Shop?"
- "Run the TikTok Shop launch prep"

## Don't use this for

- Running TikTok Shop campaigns (Implicit's job · this skill produces the brief)
- TikTok organic content (use `create-this-weeks-content`)
- Paid TikTok ads (different skill set · not in scope)
- TikTok creator outreach (use `creator-outreach` if the brand is doing direct creator partnerships · Implicit handles their own creators)

## Notes

- The Implicit relationship is the operational reality · this skill respects it · it does not try to do Implicit's work
- The brief gets re-run quarterly to refresh content angles as VOC evolves
- TikTok Shop's platform rules are stricter than Shopify · closer to Amazon · always validate claims against `claim-library.md` before sending the brief
- This skill is the precondition for the success of TikTok Shop · without the brief, Implicit defaults to generic creator content that doesn't carry the brand voice

