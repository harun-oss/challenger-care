---
name: create-this-weeks-ad-creative
description: Pulls real customer language from VOC + brand voice rules to generate 5–8 ad concepts (static + video) with hooks, copy, and design briefs. Ready for the designer or Implicit agency. MANDATORY TRIGGER: any mention of "Create this week's ad creative", "I need ads for the 3-pack push", "Generate fresh ad concepts focused on sensitive skin", "Build the ad batch for next month's Meta reactivation". Do NOT use this for: Single one-off ads (this workflow is designed for batches). Email creative (use `build-next-email-flow` or `launch-sale-promo`). Specific creative briefs handed to the designer (use the simpler `creative-brief` skill if exists).
---

> **Permission tier:** generate · **Time:** 4min · **Tools/context:** knowledge/brand-strategy.md, knowledge/claim-library.md, knowledge/customer-archetypes.md, knowledge/competitor-map.md, voc/quote-library.md

# Create this week's ad creative

## When to use this workflow

Weekly cadence — produces a batch of ad concepts the team can ship to designers / Implicit / direct-publish on social.

## What you need

- (Optional) This week's theme or focus (the 3-pack · sensitive skin · humidity · etc.)
- (Optional) Target archetype (Preparer · Switcher · Sensitive Buyer · etc.)
- (Optional) Channel mix (Meta static · TikTok video · Reddit native · Instagram carousel)

If nothing specified, default to: 3-pack focus · Preparer archetype · Meta static (since paid Meta is the priority once BM cleanup is done).

## What this produces

All in `/outputs/ads/[week-of-date]/`:

1. **`ad-concepts.md`** — 5–8 concepts, each with:
   - Hook (1-line scroll-stopper)
   - Body copy (3–5 lines)
   - CTA ("Accept the challenge" at brand layers · "Find your hold" / "Shop the routine" at conversion)
   - Visual brief (what the designer should make)
   - Messaging pillar (Preparation · Performance · Challenge)
   - Campaign territory (The Minute · No Midday Failures · Clean Control · Ready Is a Standard)
   - Source quote(s) from VOC that inspired it
   - Target archetype
2. **`designer-handoff.md`** — Ready-to-send brief: dimensions, color palette, image directions, copy lockup
3. **`tiktok-scripts.md`** (if video) — 3 short scripts (Hook 3s · Body 30s · CTA 3s)
4. **`reddit-versions.md`** — Same concepts re-cut for Reddit founder voice (NOT brand voice)

## How Claude runs it

1. Load `brand-strategy.md` — pillars, campaign territories, voice rules, headline formulas
2. Load `claim-library.md` — banned/approved language
3. Load `customer-archetypes.md` — pick 2–3 archetypes to cover
4. Load `../../assets/voc/quote-library.md` — pull 8–12 verbatim quotes around relevant themes
5. Load `competitor-map.md` — make sure we're saying things competitors aren't
6. Generate 5–8 concepts:
   - 2 concepts per pillar (Preparation, Performance, Challenge) — aim for coverage
   - At least 1 concept per primary archetype
   - At least 1 anchored to a specific VOC quote (the "wet dog" anecdote, "pomade acne," etc. are gold)
   - Mix dare frames + result-restriction frames + time-payoff frames per brand book headline formulas
7. Designer brief: anchor to the visual references in the brand book (Jack Henry style — minimal, premium, performance-led)
8. Reddit cuts: NOT brand voice — Hayden-as-founder voice

## Voice check on every concept

- Lead with the result or the challenge — never the product
- Use specific language ("9 to 12 hour hold" beats "long-lasting")
- Show the result in the room (meetings, handshakes, arrivals) — not just in the mirror
- "Accept the challenge" at brand layers · specific conversion CTAs at retargeting layers
- Beauty-brand test on every line — if a beauty brand could publish unchanged, rewrite

## Permission tier

**Generate** — all concepts are drafts. Hayden + Ivey + designer review before anything ships to Meta / Implicit.

## Example prompts that trigger this

- "Create this week's ad creative"
- "I need ads for the 3-pack push"
- "Generate fresh ad concepts focused on sensitive skin"
- "Build the ad batch for next month's Meta reactivation"

## Don't use this for

- Single one-off ads (this workflow is designed for batches)
- Email creative (use `build-next-email-flow` or `launch-sale-promo`)
- Specific creative briefs handed to the designer (use the simpler `creative-brief` skill if exists)

## Notes on channel

- **Meta (when reactivated):** static + video both work · 1080×1080 + 1080×1920
- **TikTok via Implicit:** vertical video · scroll-stopper hook in first 3 seconds · authentic feel
- **Reddit:** founder voice ONLY · no ad-looking content · contributes to community first

## Inspirational angles from VOC (use any of these)

- *"Pomade acne"* — direct address of a problem competitors cause (highest underused acquisition hook)
- *"Wet dog"* anecdote — the unscented promise made vivid
- *"15 years of pomades"* — switcher-narrative authority
- *"100 days of mornings"* — bundle math reframed as benefit
- *"For the man who reacts to everything else"* — sensitive-skin niche
