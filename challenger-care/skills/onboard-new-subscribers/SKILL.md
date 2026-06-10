---
name: onboard-new-subscribers
description: 'Builds the welcome flow for new Recharge subscribers - first jar email, retention nudge before second shipment, win-back if they cancel. Anchored to the Preparation pillar. MANDATORY TRIGGER: any mention of "Build the subscriber welcome flow", "Set up onboarding for new Recharge subscribers", "Create a winback for subscription cancellations". Do NOT use this for: General email Welcome Series for non-subscribers (use `build-next-email-flow` and select welcome). One-time promotional sends (use `launch-sale-promo`). Reactivating lapsed customers (different flow - use `build-next-email-flow` and select winback).'
---

> **Permission tier:** stage · **Time:** 6min · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/unit-economics.md, assets/customer-archetypes.md, voc/quote-library.md, mcp:klaviyo, CONFIG.md

# Onboard new subscribers

## When to use this workflow

You're building (or rebuilding) the subscriber welcome flow on Recharge. New subscribers get an automated email sequence that locks in the relationship and reduces early churn.

## What you need

- Confirmation Recharge is connected and the subscription event fires into Klaviyo
- (Optional) Specific products to feature in the flow
- (Optional) Desired flow length (3 emails default · up to 5)

## What this produces

All in `/outputs/flows/subscriber-onboarding/`:

1. **`flow-architecture.md`** — Step-by-step flow design:
   - Trigger: New Recharge subscription event
   - Delay timing between emails
   - Conditional branches (cancellation, second order, etc.)
   - Exit criteria
2. **`email-01-welcome.html`** — Day 0 · "You're in"
3. **`email-02-first-jar.html`** — Day 3 · "What to expect" (the 110-day jar education)
4. **`email-03-retention-nudge.html`** — Day 90 · "Your next jar ships in 10 days" + soft upsell to 3-pack
5. **`email-04-winback.html`** — Triggers on cancellation · respectful, doesn't beg, opens the door
6. **`subject-lines.md`** — 3 variants per email for A/B testing
7. **`klaviyo-setup-notes.md`** — Setup instructions: segment definition, send timing, smart-send-time toggle, suppression list, tracking parameters

## How Claude runs it

1. Load `brand-strategy.md` — Preparation pillar leads ("One minute. Every room.")
2. Load `claim-library.md` — confirm we don't make subscription/savings claims we can't back
3. Load `unit-economics.md` — the 110-day jar math is the structural anchor
4. Search `../../assets/voc/quote-library.md` for subscriber-language quotes ("on my third container," "won't try anything else")
5. Email 1 (Welcome): tone is **direct + welcoming peer** — "You took the minute. Here's what you get."
6. Email 2 (First jar education): teach the 110-day math · how to use · what to expect at day 30 / 60 / 90
7. Email 3 (Retention nudge): time-flexed to send 10 days before second shipment · upsell path to 3-pack ("100 days at a time, not 30")
8. Email 4 (Winback): NO discount-as-default · respect their decision · ask one question (why) · open the door without begging

## Voice check

Subscriber emails skew warmer than ad copy — these customers have already opted in. Still:
- No beauty-coded language ("your wellness journey")
- No fratty masculinity ("you're crushing it")
- Direct, peer-to-peer, useful
- The Challenge pillar appears subtly: "Most guys won't keep up with this. You did. Here's what's next."

## Permission tier

**Stage** — All 4 emails get drafted in Klaviyo as a flow but stay paused until the {{roles.founder}}'s explicit approval. Klaviyo setup notes are Generate-tier reference.

**Why Stage:** A subscriber welcome flow is live customer-facing the moment it's unpaused. Reversible (can be paused again) but worth the {{roles.execute_tier_approver}}'s approval before going live.

## Example prompts that trigger this

- "Build the subscriber welcome flow"
- "Set up onboarding for new Recharge subscribers"
- "Create a winback for subscription cancellations"

## Don't use this for

- General email Welcome Series for non-subscribers (use `build-next-email-flow` and select welcome)
- One-time promotional sends (use `launch-sale-promo`)
- Reactivating lapsed customers (different flow — use `build-next-email-flow` and select winback)

## Special note on subscriber LTV

Per `unit-economics.md`, subscribers are 3–5× LTV vs. one-time buyers. Per `customer-archetypes.md`, the Sensitive Buyer and Switcher archetypes have the highest subscription propensity. Lean copy toward those archetypes where appropriate.
