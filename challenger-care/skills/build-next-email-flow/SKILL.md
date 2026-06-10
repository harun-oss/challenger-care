---
name: build-next-email-flow
description: 'Drafts a complete Klaviyo flow in Challenger voice — welcome series, browse abandonment, post-purchase, winback, or sunset. Uses the live abandoned cart flow as the template baseline. MANDATORY TRIGGER: any mention of "Build the welcome flow", "Set up browse abandonment in Klaviyo", "Build a winback series for lapsed customers", "Rebuild the [flow name] in brand voice". Do NOT use this for: Subscription welcome (use `onboard-new-subscribers`). One-time campaign sends (use `launch-sale-promo`). Fixing an existing underperforming flow (use `fix-broken-flow` — different process).'
---

> **Permission tier:** stage · **Time:** 5min · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/customer-archetypes.md, voc/quote-library.md, mcp:klaviyo, CONFIG.md

# Build the next email flow

## When to use this workflow

You're building a new Klaviyo flow that doesn't exist yet (or rebuilding one of the 34 dormant drafts in the {{roles.founder}}'s account). Most-needed: Welcome Series · Browse Abandonment · Post-Purchase · Winback · Sunset Unengaged.

## What you need

- Which flow to build (welcome · browse abandonment · post-purchase · winback · sunset)
- Which customer archetype this should lead with (Preparer · Switcher · Sensitive Buyer · etc.)
- (Optional) Discount strategy if relevant (welcome offer, winback incentive)

## What this produces

All in `/outputs/flows/[flow-name]/`:

1. **`flow-architecture.md`** — Steps · delays · branches · exit criteria · segment definition
2. **`email-XX-[step-name].html`** — Klaviyo-ready HTML for each step (typically 3–5 emails)
3. **`subject-lines.md`** — 3 variants per email for A/B testing
4. **`klaviyo-setup-notes.md`** — Trigger config · suppression · smart send time · tracking
5. **`metrics-targets.md`** — Expected open rate, CTR, conversion rate based on Klaviyo benchmarks + the {{roles.founder}}'s past flow performance

## How Claude runs it

1. Load `brand-strategy.md` — voice rules, applicable messaging pillar for the flow type
2. Load `claim-library.md` — what we can/can't say
3. Load `customer-archetypes.md` — pick the lead archetype for this flow
4. Search `../../assets/voc/quote-library.md` for theme matches (e.g., welcome = hold + first-time-buyer themes · winback = repeat-buyer themes)
5. Pull existing abandoned cart flow from Klaviyo as the structural template (it's the proven-working baseline)
6. Design the flow architecture (trigger, steps, timing, branches)
7. Write each email anchored to the right pillar:
   - **Welcome** → Preparation pillar ("Take the minute. Walk out ready.")
   - **Browse abandonment** → Performance pillar ("Hold that doesn't quit at lunch")
   - **Post-purchase** → Performance + Challenge ("You picked the standard. Now use it.")
   - **Winback** → Challenge ("Most guys go back to grease. Will you?")
   - **Sunset** → respectful, low-pressure, clear opt-out
8. Subject lines: short, specific, dare-flavored (per brand book email rules)
9. CTA: "Accept the challenge" at brand layers · "Shop the routine" / "Find your hold" at conversion layers

## Voice check

Apply the brand book quick checklist to every email:
- Leads with a result, not an ingredient
- Time investment anchored somewhere
- Sounds peer-to-peer
- One of the 3 pillars clearly present
- Beauty-brand test passed

## Permission tier

**Stage** — Flows get drafted in Klaviyo but stay paused until the {{roles.execute_tier_approver}} approves. Email content is reversible (can edit/pause), but going live touches real customers.

## Example prompts that trigger this

- "Build the welcome flow"
- "Set up browse abandonment in Klaviyo"
- "Build a winback series for lapsed customers"
- "Rebuild the [flow name] in brand voice"

## Don't use this for

- Subscription welcome (use `onboard-new-subscribers`)
- One-time campaign sends (use `launch-sale-promo`)
- Fixing an existing underperforming flow (use `fix-broken-flow` — different process)

## Reference flow benchmarks (industry + the {{roles.founder}}'s data)

| Flow | Open rate target | CTR target | Revenue per recipient |
|---|---|---|---|
| Welcome | 35–50% | 8–12% | $1.50–$3.00 |
| Browse abandonment | 30–45% | 6–10% | $0.40–$1.20 |
| Post-purchase | 40–55% | 5–9% | $0.30–$0.80 (cross-sell) |
| Winback | 20–30% | 3–6% | $0.50–$1.50 (depends on time since last order) |

These get refined as the {{roles.founder}}'s flow performance data accumulates.
