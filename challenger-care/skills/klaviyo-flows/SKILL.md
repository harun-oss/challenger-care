---
name: klaviyo-flows
description: 'Consulting-grade Klaviyo flow build · welcome, abandoned cart, browse abandonment, post-purchase, winback, sunset · with precise timing, discount logic, segmentation, deliverability rules. Deeper than `build-next-email-flow` which is the Challenger-tuned production version. MANDATORY TRIGGER: any mention of "build a deep Klaviyo flow", "consulting-grade Klaviyo flow", "optimise the abandoned cart flow", "Klaviyo flow with deliverability rules", "rebuild the welcome flow from scratch". Do NOT use for: Quick Challenger-tuned flow builds (use `build-next-email-flow`). One-time campaign sends (use `klaviyo-campaigns`). Email strategy (use `email-strategy`).'
---

> **Permission tier:** stage · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/unit-economics.md, assets/team-roles.md, CONFIG.md, mcp:klaviyo


# Klaviyo Flows

## What this skill does

Covers the complete Klaviyo flow build process for eCommerce clients — from account and list setup through building every essential flow with the correct timing, filters, discount logic, and A/B test structure. Also covers flow analytics interpretation and monthly optimisation.

Automated flows generate 30× more revenue per recipient than campaigns ($3.65 vs $0.11). Getting them built correctly is the highest-leverage email work on any eCommerce account.

Use this skill when:
- Building flows for a new Klaviyo client
- Rebuilding or optimising underperforming flows
- Adding a specific flow (e.g., post-purchase, winback) to an existing account
- Reviewing flow analytics and deciding what to change

---

## Reference Files

This skill uses reference materials. When running inside an orchestrated workflow, the orchestrator will locate and load these automatically via Glob.

- `assets/brand-strategy.md` — Full discount decision framework, welcome copy templates, abandoned cart dynamic block setup, winback segment build, sunset suppression steps, predictive analytics segments, and full analytics interpretation guide. Read during Phases 3–8.

---

## Phase 1 — Context

Ask one question at a time:

1. **Client name and what they sell** — product category matters for flow strategy
2. **Which flows are needed?** — all essential flows, or a specific one?
3. **What does the audit show?** — if `email-program-audit` has been run, pull the findings. If not, ask for a quick summary: what flows exist, what's missing, list size
4. **List size and monthly order volume** — needed for predictive analytics eligibility and winback timing
5. **Does Challenger use Shopify?** — Klaviyo's Shopify integration enables specific triggers (Checkout Started, Order Placed, etc.)
6. **Do we have admin or editor access to the Klaviyo account?**

> If the account is brand new (no prior flows, no purchase data), start with Phase 2 (account setup) and build in priority order: Welcome → Abandoned Cart → Browse Abandonment → Post-Purchase → Winback → Sunset.

---

## Phase 2 — Account and List Setup

Before building any flows, confirm the account foundations are correct. Flows built on a broken foundation will underperform.

**Master list setup:**
- One primary email list for all marketing subscribers (e.g., "Newsletter" or "All Subscribers")
- All signup forms point to this list
- Suppression list active (hard bounces, spam complaints auto-suppressed)

**Sending domain:**
- Custom sending domain configured (not @klaviyomail.com)
- SPF, DKIM, DMARC all verified in Klaviyo Settings → Email → Sending Domains
- If not configured: fix before launching any flow — Gmail/Yahoo 2024 requirements mandate authentication for bulk senders

**Smart Sending:**
- Default: 16 hours between any two emails to the same contact
- This is a safety net, not a strategy. Flows should be designed so Smart Sending rarely fires.
- Check: Klaviyo Settings → Account → Smart Sending

**Quiet Hours:**
- Enable for SMS flows: default 8 PM–11 AM local time
- Email quiet hours optional but recommended for high-frequency sends

**One-click unsubscribe:**
- Required by Gmail/Yahoo for bulk senders as of June 2024
- Klaviyo adds the List-Unsubscribe header automatically for marketing emails — verify it is enabled in account settings

> For full deliverability setup and verification steps, read `assets/brand-strategy.md` → Deliverability Setup.

---

## Phase 3 — Welcome Series

The welcome series has the highest revenue-per-recipient of any non-cart flow: average $2.65 RPR, top performers $3.34+ for higher-AOV brands. It generates 320% more revenue than promotional emails.

**Trigger:** Added to list (signup form submission, checkout opt-in)

**Flow filters:**
- Exclude: Placed Order in last 30 days (don't welcome someone who already bought)

**Timing and sequence:**

| Email | Send time | Purpose | Discount? |
|-------|-----------|---------|-----------|
| 1 | Immediately | Deliver promised offer/lead magnet. Brand intro. One clear CTA. | Yes — deliver the signup offer here, not later |
| 2 | Day 2 | Brand story + bestsellers. Why customers love you. Social proof. | No |
| 3 | Day 4 | Product education / "how it works". Address top objection. | No |
| 4 | Day 6 | Urgency / final push. "Your discount expires in 24 hours." | Remind of Email 1 offer |

**Critical rule:** Deliver the promised signup offer immediately in Email 1. Delaying it — even by one hour — causes a measurable drop in conversion. If no offer was made at signup, Email 1 is a warm welcome + brand story.

**Conditional split after Email 1:**
- Branch: Has placed order since flow started?
  - YES → exit flow (don't continue sending welcome series to buyers)
  - NO → continue to Email 2

Apply the same purchased split after each subsequent email.

**A/B test opportunities:**
- Email 1: Subject line (curiosity vs. offer-forward vs. personal tone)
- Email 4: Discount amount (10% vs. free shipping vs. no discount)

> For subject line formulas and copy frameworks for each welcome email, read `assets/brand-strategy.md` → Welcome Series Copy.

---

## Phase 4 — Abandoned Cart

Abandoned cart is the single highest-revenue flow: average $3.65 RPR, top 10% achieve $27+ per recipient. Three-email sequences generate 6.5× more revenue than single-email flows.

**Trigger:** Checkout Started (Shopify) or Added to Cart event

**Trigger filter:**
- Has not placed order since starting flow
- Has not been in this flow in the last 7 days (prevent re-entry spam for frequent browsers)

**Flow filter (apply to every email):**
- Has not placed order since flow trigger

**Timing and sequence:**

| Email | Send time | Purpose | Discount? |
|-------|-----------|---------|-----------|
| 1 | 1 hour after trigger | Remind. Show the cart. No discount. Create desire. | NO |
| 2 | 12–24 hours after trigger | Address objection. Social proof, returns policy, reviews. | Conditional (see below) |
| 3 | 48–72 hours after trigger | Final reminder. Soft urgency. Last chance. | Conditional (see below) |

**Discount strategy (critical):**
Never discount Email 1. Offering a discount immediately trains customers to intentionally abandon carts to receive it — this will increase cart abandonment rates over time.

Use a conditional split before Email 2 to control discount eligibility:
- Condition A (gets discount): First-time customer AND cart value above £/$ threshold (set per client — typically 1.5× AOV)
- Condition B (no discount): Repeat customer OR low cart value → send without discount, lean on urgency and social proof

**Note on 1-hour timing:** Klaviyo's sync with Shopify can take 5–15 minutes. Set the first delay to 1 hour 15 minutes minimum to avoid triggering before the purchase completes.

**A/B test priorities:**
1. Email 1 subject line (product name vs. curiosity vs. "you left something")
2. Email 2 timing (12hrs vs. 24hrs)
3. Email 3 discount amount (if offering one)

> For full discount decision framework, dynamic cart block setup, and copy templates by cart value tier, read `assets/brand-strategy.md` → Abandoned Cart.

---

## Phase 5 — Browse Abandonment

Browse abandonment captures product interest before the cart stage. Lower conversion intent than cart abandonment — treat it as a lighter, curiosity-driven touchpoint, not a hard sell.

**Trigger:** Viewed Product (minimum 2 product views, or 1 view of the same product twice — prevents triggering on casual browsers)

**Trigger filter:**
- Has not started checkout in the last 2 hours (don't double-trigger with cart flow)
- Has not been in this flow in the last 14–30 days

**Timing and sequence:**

| Email | Send time | Purpose | Discount? |
|-------|-----------|---------|-----------|
| 1 | 60 minutes after trigger | Show the viewed product. Light CTA. "Still thinking about it?" | No |
| 2 | 24 hours after trigger | Social proof for that product. Reviews, bestseller status. | No (or very soft offer) |

**Key principles:**
- Two emails is optimal for top performers; three with SMS is best practice if SMS is enabled
- Do NOT mirror abandoned cart urgency — the browse visitor hasn't committed to a purchase
- Dynamic product block should show the last-viewed product, not a generic product grid

**Re-entry control:**
14–30 day window prevents chronic browsers from triggering the flow every day. Set based on client's typical purchase cycle — shorter cycle (consumables) = 14 days; longer cycle (apparel, home goods) = 21–30 days.

---

## Phase 6 — Post-Purchase

Post-purchase flows capitalise on peak brand enthusiasm. They produce 217% higher open rates and 500% higher click rates than campaign averages.

**Trigger:** Placed Order

**Timing and sequence:**

| Email | Send time | Purpose |
|-------|-----------|---------|
| 1 | Immediately | Order confirmation (if Klaviyo is handling this — check Shopify isn't sending a duplicate) |
| 2 | 2–3 days after fulfilment | Cross-sell / upsell based on what they bought. Show complementary products. |
| 3 | 7–10 days after estimated delivery | Review request. Keep it simple: one question, direct link to review platform. |
| 4 | 14–21 days after purchase | Replenishment reminder (for consumables/repeat-purchase products only) |

**Cross-sell logic:**
Use Klaviyo's product recommendation blocks (Klaviyo AI) or set up manual cross-sell segments per product category. The goal is to show products that genuinely complement the purchase — not a generic bestsellers list.

**Review request timing:**
7–10 days after estimated delivery is the sweet spot. Too early (before the product arrives) = no review. Too late (30+ days) = lower response rate. Use the order's fulfilment date + estimated transit time if available.

**Conditional split for repeat vs. first-time buyers:**
- First-time buyer → include "welcome to the community" language, longer brand-building content
- Repeat buyer → skip brand intro, go straight to cross-sell and loyalty messaging

**Smart Sending note:**
If Challenger sends frequent promotional campaigns, Smart Sending may delay post-purchase emails. For Email 1 (order confirmation), disable Smart Sending — it must send immediately.

---

## Phase 7 — Winback and Sunset

### Winback

Winback targets customers who were active but have gone quiet. The goal is re-engagement before they're lost permanently.

**Entry trigger:**
Segment-based. Build a segment:
- Has placed at least 1 order (all time)
- Has not placed an order in [X] days — set X at the brand's natural repurchase window × 1.5
  - Example: AOV brand where 60% of repeat customers buy within 90 days → trigger at 135 days
- Is subscribed and can receive email

**Timing and sequence (3 emails maximum):**

| Email | Send time | Angle |
|-------|-----------|-------|
| 1 | Entry into segment | "We miss you." Show 3–6 bestsellers or new arrivals. Value-first. |
| 2 | 7 days later | Social proof + brand credibility. What's changed or new since they last bought. |
| 3 | 7 days later | Final offer + urgency. "Come back, here's X% off — this is the last email we'll send." |

After Email 3 with no purchase: move to Sunset flow.

### Sunset

Sunset is a structured exit — a final attempt to re-engage before suppressing permanently.

**Entry criteria (segment):**
- Can receive email marketing: YES
- Profile created: 180+ days ago
- Received at least 5 emails in the last 72 weeks
- Opened email: 0 times (all time)
- Clicked email: 0 times (all time)
- Active on site: 0 times
- Viewed product: 0 times
- Placed order: 0 times

**Sequence:**
- Email 1: "Are you still interested?" — give them a reason to stay
- Email 2 (7 days later): "This is our last email" — final chance with unsubscribe option front and centre
- If no click or open after Email 2: suppress from all marketing. Do not delete — suppression preserves the record for exclusion from future campaigns without continuing to damage sender reputation.

**Why this matters:**
Sending to chronically unengaged contacts drags down deliverability scores and increases spam complaint rates. Suppressing them protects the deliverability of every other send.

> For full winback segment build instructions and sunset suppression setup in Klaviyo, read `assets/brand-strategy.md` → Winback and Sunset Setup.

---

## Phase 8 — Flow Analytics and Optimisation

### Key metrics per flow (pull from Klaviyo → Flows → select flow → Analytics)

| Metric | What it tells you |
|--------|------------------|
| Revenue per recipient (RPR) | Primary health metric. Compare against benchmarks. |
| Placed order rate | Conversion rate of flow |
| Open rate | Subject line and deliverability health |
| Click rate | Content and CTA relevance |
| Unsubscribe rate | Relevance or frequency issue if above 0.3% |

**Benchmark RPR targets:**
- Abandoned cart: $3.65 avg; flag if below $1.50
- Welcome series: $2.65 avg; flag if below $1.00
- Post-purchase: should exceed campaign RPR by 90%+

### Monthly optimisation checklist

- [ ] Review RPR for each live flow — compare against prior 30 days
- [ ] Check open rate trend — declining OR vs 30 days ago = subject line fatigue
- [ ] Check unsubscribe rate per flow — above 0.3% triggers a copy and targeting review
- [ ] Smart Sending skips: if >15% of recipients are being skipped, the overall send frequency is too high
- [ ] A/B test winner declared (if a test has run 14+ days with sufficient volume): implement winner, set up next test
- [ ] Predictive analytics check: review High Churn Risk segment size — if growing, escalate winback cadence

> For full analytics interpretation guide, predictive CLV and churn risk segment builds, and what to do when each metric declines, read `assets/brand-strategy.md` → Analytics and Optimisation.

---

## QA Gate

Before any flow goes live:

- [ ] Custom sending domain configured and DKIM/SPF/DMARC verified
- [ ] One-click unsubscribe header confirmed active (Klaviyo Settings → Account)
- [ ] Flow trigger and all flow filters set correctly — test with a real profile
- [ ] Smart Sending status confirmed for each email (disabled for order confirmations, enabled for all others)
- [ ] Purchased split conditional applied after Email 1 in every prospecting flow
- [ ] Discount logic in abandoned cart uses conditional split — NOT applied in Email 1
- [ ] Browse abandonment has 14–30 day re-entry filter set
- [ ] UTM parameters on all links: `utm_source=klaviyo&utm_medium=email&utm_campaign=[flow-name]`
- [ ] Test email sent and rendered on mobile and desktop before activating
- [ ] Flow set to LIVE (not draft) — draft flows do not send

---

## Phase 9: Synthesis Brief

Before delivering flow setup, write a brief summary of live flows and performance. This is used by the orchestrator to carry findings forward to the next skill in a multi-skill workflow.

**Klaviyo Flows Key Findings**

Extract and summarise:
- **Flows configured and live:** List all 6 core flows (welcome, abandoned cart, browse abandonment, post-purchase, winback, sunset) with status (live/paused/planned), 30-day RPR for each, and monthly volume enrolled. Highlight which flows are performing above/below benchmark and by how much (e.g., "Welcome $2.87 RPR (benchmark $2.65); Abandoned cart $2.10 RPR (benchmark $3.65 — needs optimisation)").
- **Performance vs benchmarks:** Which flows are underperforming by more than 20% vs category benchmarks, why (subject line fatigue, insufficient emails, discount strategy misaligned), and which flow represents the highest revenue opportunity for improvement (typically abandoned cart if RPR below $2.00).
- **A/B test queue and optimisation priorities:** Next test to run per flow (e.g., cart Email 1 subject line, welcome Email 4 discount amount), sample size per variant, and win condition. Any discount logic or conditional splits that need adjustment based on first-time vs repeat buyer performance.
- **Smart Sending and frequency health:** Current Smart Sending skip rate across all flows, combined flow + campaign send frequency per week, and whether frequency is sustainable or needs throttling to maintain deliverability.

**Priority for downstream skills:** The email-copywriting skill should prioritise rewriting underperforming subject lines (especially for cart and browse flows) and refining discount messaging for cart Email 2 conditional split. Campaign planning should coordinate promotional send frequency with flow send cadence to avoid Smart Sending caps and maintain healthy sender reputation. Audience segmentation (engaged windows, purchased splits) should be audited quarterly to prevent filter creep.

*If running standalone (not in an orchestrated chain), share this summary with the operator before final flow launch.*

---

## References

Read these files when the relevant phase is reached:

- **[Flow Playbook](../../assets/brand-strategy.md)** — Read during Phases 3–8. Full discount decision framework, welcome copy templates, abandoned cart dynamic block setup, winback segment build, sunset suppression steps, predictive analytics segments, and full analytics interpretation guide.
- **[Brand](../../assets/brand-strategy.md)** — Read when producing any branded output (PPTX, DOCX, PDF). Colours, typography, and component patterns.
- **[Klaviyo Campaigns](../klaviyo-campaigns/SKILL.md)** — Use for newsletter, promotional, and BFCM campaign sends. Flows and campaigns work together — both are required for a complete Klaviyo programme.
