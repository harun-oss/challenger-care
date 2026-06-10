---
name: subscription-migration-amazon-to-shopify
description: 'Models the economics of migrating Amazon Subscribe & Save customers to Shopify subscriptions, drafts the migration offer for owner approval, then executes the comms once approved. MANDATORY TRIGGER: any mention of "migrate Amazon subscribers to Shopify", "move S&S to Recharge", "win subscribers off Amazon", "subscription migration play". Do NOT use this for: New subscriber acquisition (use `onboard-new-subscribers`). General subscription program review (use `whats-working-to-scale`). One-off campaign sends (use `launch-sale-promo`).'
---

> **Permission tier:** stage (stage 1 model) → execute (stage 2 comms · execute_tier_approver only) · **Time:** 5min model + 8min comms · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/unit-economics.md, assets/goals-targets.md, assets/team-roles.md, assets/voc/quote-library.md, CONFIG.md, mcp:klaviyo, mcp:shopify

# Migrate Amazon subscribers to Shopify

## When to use this workflow

The single biggest known LTV unlock in the business. The brand has 1,318 Amazon Subscribe & Save subscribers paying the platform's terms, with limited customer data and no direct relationship. Moving even 10% to Shopify subscriptions (currently 17 subs · 90-day target 50) doubles the subscription base and gives the brand a direct CRM line.

This is also the highest-risk move in the playbook · Amazon S&S subscribers cancel within Amazon's UI, and pushing migration too aggressively can trigger Amazon's rank-suppression for "customer manipulation." Two-stage by design: stage 1 produces a model + offer for review, stage 2 executes only after the {{roles.execute_tier_approver}} signs off.

## What you need

- (Optional) Target migration rate (default: 10% over 90 days)
- (Optional) Incentive budget ceiling (default: pull from CONFIG.md · `goal.monthly_revenue_shopify`)
- (Optional) Specific subscriber cohort to target (default: all 1,318)

## What this produces

### Stage 1 (Model + Offer · stage tier)

In `/outputs/subscription-migration/[date]-stage1/`:

1. **`economics-model.md`** — The math:
   - Current state: 1,318 Amazon S&S subs · estimated AOV per ship · estimated lifetime value
   - Migration scenarios: 5% / 10% / 20% migrated · LTV delta · platform fee savings (Amazon takes ~15%)
   - Break-even incentive cost · maximum spend per migrated subscriber that still produces positive contribution
   - Risk model: Amazon rank impact if we push too hard
2. **`migration-offer.md`** — The proposal customers see:
   - Headline (in Challenger voice · loads `brand-strategy.md`)
   - Incentive structure (free first jar · % off lifetime · bundle bonus · etc.)
   - Friction reduction (Recharge account setup · payment migration · shipping address transfer)
   - The "why" message (why moving is better for them · NOT why it's better for the brand)
3. **`klaviyo-segment-spec.md`** — The audience definition for the comms send:
   - Who's eligible (active S&S subs · activity threshold · purchase history)
   - Who's excluded (recent purchasers · recently cancelled · damaged-product complaints)
4. **`approval-checklist.md`** — Decisions the {{roles.execute_tier_approver}} makes before stage 2:
   - Approve / modify / kill incentive structure
   - Approve / modify segment scope
   - Set launch window
   - Confirm Amazon rank tolerance

### Stage 2 (Comms execution · execute tier · execute_tier_approver only)

Triggers ONLY after `approval-checklist.md` is signed off. In `/outputs/subscription-migration/[date]-stage2/`:

1. **`klaviyo-flow-built.md`** — The 3-email migration sequence drafted in Klaviyo (paired with `klaviyo-flows`):
   - Email 1: the offer (loads `voc/quote-library.md` for social proof)
   - Email 2: how to do it (Recharge setup walkthrough · 110-day cadence explanation)
   - Email 3: deadline reminder (urgency · scarcity · last call)
2. **`tracking-setup.md`** — How we measure migration success:
   - UTMs on every link
   - Shopify subscription cohort tagging
   - Conversion attribution back to the Klaviyo segment
3. **`week-1-checkpoint.md`** — What to check on day 7:
   - Migration rate vs target
   - Amazon rank impact (if any)
   - Cancellation reasons from non-converters
   - Decision: continue · adjust · pause

## How Claude runs it

### Stage 1

1. Load `unit-economics.md` for COGS, margin, jar duration (110 days = natural sub cadence)
2. Load `goals-targets.md` for `shopify_subscribers_target`
3. Load `brand-strategy.md` for voice rules + `claim-library.md` for banned language
4. Pull current Shopify subscription count from `mcp:shopify` (currently 17 per CONFIG)
5. Read manual Amazon S&S subscriber count from CONFIG.md → `goal.amazon_ss_subscribers` (currently 1,318)
6. Model 3 scenarios (5% / 10% / 20% migrated) with break-even incentive analysis
7. Draft the migration offer in Challenger voice · pull 2-3 ad-ready quotes from `voc/quote-library.md`
8. Define Klaviyo segment based on Recharge eligibility + Amazon-buyer-data-we-have
9. Generate the approval checklist
10. STOP. Output all 4 docs to `/outputs/subscription-migration/[date]-stage1/`. Notify execute_tier_approver (per `team-roles.md` → `roles.execute_tier_approver` per CONFIG.md). Wait for sign-off.

### Stage 2 (only after sign-off)

11. Read the signed-off `approval-checklist.md`
12. Chain into `klaviyo-flows` (paired skill) to build the 3-email sequence
13. Build the tracking setup
14. Schedule the day-7 checkpoint as a follow-up task

## Voice + claim rules (loaded from CONFIG)

- Loads voice rules from `assets/brand-strategy.md` · the dare-frame works here ("Own your routine. Skip the middleman.")
- Loads claim rules from `assets/claim-library.md` · cannot make claims about Amazon's terms or pricing changes
- Loads archetypes from `assets/customer-archetypes.md` · primary target is the Preparer + Switcher archetypes (highest LTV migration candidates)

## Permission tier

**Stage 1: stage tier** · drafts the model + offer. Anyone with stage access can run.
**Stage 2: execute tier** · live customer-facing comms sent · requires `roles.execute_tier_approver` sign-off (per CONFIG.md).

Why two tiers: a subscription-migration push is the single highest-risk move in the playbook. The economics need to be modelled before the comms ship. Decoupling them prevents accidental over-commit.

## Example prompts that trigger this

- "Run the subscription migration play"
- "Model what it would take to move Amazon subs to Shopify"
- "Build the Amazon → Shopify migration offer"
- "What if we tried to win 10% of S&S to Shopify?"

## Don't use this for

- General subscription onboarding for new Recharge subs (use `onboard-new-subscribers`)
- Sub program performance review (use `whats-working-to-scale`)
- One-off promo campaigns (use `launch-sale-promo`)
- New customer acquisition flows (use `build-next-email-flow` → welcome flow)

## Notes

- This is a *campaign*, not a one-time skill. After stage 2 ships, the migration runs over 4-6 weeks. Check progress via the dashboard's Shopify subscriber count vs Amazon S&S count.
- The 110-day jar duration is the natural retention window · target migration windows around that cadence so the next jar shipment is the Shopify one.
- Pulls from `assets/competitor-map.md` only if competitors have similar migration plays worth borrowing or beating.

