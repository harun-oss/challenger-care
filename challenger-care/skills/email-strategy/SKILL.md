---
name: email-strategy
description: Defines the full email architecture for Challenger · which flows, what segments, what cadence, attribution setup. The strategic layer between the audit and the build skills. MANDATORY TRIGGER: any mention of "email strategy", "email plan", "what flows should we build", "email roadmap", "email cadence", "plan the email program", "what should we prioritise for email". Do NOT use for: Building specific flows (use `klaviyo-flows`). Diagnosing existing program (use `email-program-audit`). Writing copy (use `email-copywriting`).
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/unit-economics.md, assets/goals-targets.md, assets/team-roles.md, CONFIG.md, mcp:klaviyo


# Email Strategy

## What this skill does

Defines the complete email strategy for a client before any execution begins — the flow architecture, segmentation model, campaign cadence, and revenue attribution setup. Works for any platform.

The strategy answers three questions: What to build, in what order, and how to measure success. Platform-specific skills handle the how.

Use this skill when:
- Starting email work with a new client after the audit
- The audit has surfaced gaps and we need a structured plan before building
- A client asks "what should our email programme look like?"
- Setting expectations with a client on scope and timeline

---

## Phase 1 — Context

Ask one question at a time:

1. **Client name, vertical, and ESP** — pull from the audit if it's been run
2. **What did the audit find?** — which flows are missing, what are the list health issues, is there a deliverability problem?
3. **Monthly order or lead volume** — determines which flows are worth building vs. which are too low-volume to justify
4. **Revenue target for email** — what % of revenue should email drive in 6 months? (eCommerce baseline: 20–30%)
5. **Resources available** — does Challenger have a designer for HTML emails? Do they have copy? Are we writing everything?
6. **Timeline constraints** — is there a product launch or promo coming up that affects prioritisation?

If the audit has not been run, run `email-program-audit` first. Strategy without audit is guesswork.

---

## Phase 2 — Deliverability First

Before defining any strategy, confirm the foundation is clean. A strategy built on a broken foundation fails silently.

**Non-negotiable prerequisites:**
- [ ] Custom sending domain configured
- [ ] SPF + DKIM + DMARC verified
- [ ] Spam complaint rate below 0.1% (or unknown — if unknown, treat as a risk)
- [ ] List engagement composition known: what % is engaged (opened/clicked in 90 days)?

**If deliverability issues exist:**
Deliverability remediation is Tier 0 — it comes before any new builds. A great welcome series sent to a domain with a spam reputation problem will not convert.

Deliverability fix first: suppress unengaged contacts, reduce send frequency to engaged-only segments, run a list validation service (NeverBounce, ZeroBounce) if hard bounces are elevated.

---

## Phase 3 — Flow Architecture

### eCommerce Flow Priority Order

Build in this order. Each tier builds on the last.

**Tier 1 — Revenue foundations (build first, highest RPR):**

| Flow | Why first | RPR benchmark |
|------|-----------|--------------|
| Welcome series | 48% of flow revenue; $2.65 avg RPR; captures buyers at peak intent | $2.65 |
| Abandoned cart | Highest single-flow RPR; $3.65 avg; 6.5× uplift from 3-email vs 1-email | $3.65 |

**Tier 2 — Revenue accelerators (build after Tier 1 is live and performing):**

| Flow | Why second |
|------|------------|
| Browse abandonment | High volume, lower intent than cart — captures early-funnel interest |
| Post-purchase | Cross-sell and review generation; 500% higher CTR than campaigns |
| Winback | Recovers lapsed buyers; low incremental cost once built |

**Tier 3 — Programme maturity (build once Tier 1 and 2 are optimised):**

| Flow | When it's worth building |
|------|--------------------------|
| Sunset | When list health metrics show deliverability drag from unengaged contacts |
| Back-in-stock | When out-of-stock is a frequent customer problem |
| Price drop | When conversion barrier is price, not awareness |
| VIP / loyalty | When repeat purchase rate is above 30% and a loyalty programme exists |
| Review request | If post-purchase flow doesn't already include it |

### Lead Gen / B2B / SaaS Flow Priority Order

**Tier 1 — Foundation:**

| Flow | Why first |
|------|-----------|
| Welcome / lead magnet delivery | First touch; sets the entire relationship |
| Lead nurture (problem → solution → product) | Moves cold leads to sales-ready; without this, inbound leads die |
| Trial onboarding (SaaS) | Activation is the biggest driver of retention; without onboarding, trials churn silently |

**Tier 2 — Conversion and retention:**

| Flow | Why second |
|------|------------|
| Trial expiry / upgrade nudge | Direct revenue from expiring trials |
| Demo confirmation + reminder | Reduces no-shows; highest-intent sequence |
| Post-demo follow-up | Keeps momentum after sales conversation |

**Tier 3 — Programme maturity:**

| Flow | When to build |
|------|--------------|
| Winback (churned customers) | When MRR churn is a known problem |
| Re-engagement (cold leads) | When lead database is growing but conversion rate is flat |
| Feature adoption (SaaS) | When product analytics show low feature uptake correlates with churn |

---

## Phase 4 — Segmentation Strategy

### Core Principle

Build the minimum segments needed to send the right content to the right person. Complexity without volume is waste — a 50-person segment is not worth maintaining.

### Master List + Engagement Segments (applies to all platforms)

**Master list:** One primary list containing all subscribed marketing contacts. All forms point here. This is the audience for all campaign sends.

**Engagement segments (dynamic):**

| Segment | Definition | Use for |
|---------|------------|---------|
| Highly engaged | Opened or clicked in last 30 days | Highest-priority campaign sends |
| Engaged | Opened or clicked in last 90 days | Primary campaign audience |
| At-risk | No open/click in 90–180 days | Re-engagement campaigns, lower send frequency |
| Unengaged | No open/click in 180+ days | Sunset flow only — no campaign sends |
| Purchasers | Has placed ≥ 1 order | Post-purchase flows, cross-sell, loyalty |
| Non-purchasers | Has not placed an order | Welcome series, nurture, acquisition offers |

**Suppression list:** Hard bounces, spam complaints, unsubscribes — maintained automatically by most ESPs. Verify it's active.

### Campaign Send Rules

Never send campaigns to the full list. Send to: Engaged segment (90-day window) excluding recent purchasers (if promotional) and excluding current retargeting audiences.

This protects deliverability and reduces unsubscribe rates.

### eCommerce Segmentation Additions

Once Tier 1 flows are live and data is accumulating, add:

| Segment | When to build |
|---------|--------------|
| Purchasers by category | When cross-sell strategy requires it (e.g., "bought running shoes → show socks") |
| High AOV buyers | After 500+ orders — use for VIP campaigns |
| Repeat buyers (2+ orders) | For loyalty campaigns and referral asks |
| Lapsed buyers | Winback entry segment (time-based) |

### B2B/SaaS Segmentation Additions

| Segment | When to build |
|---------|--------------|
| By lifecycle stage | Lead → MQL → SQL → Customer → Churned |
| By company size or industry | If ICP has clear firmographic distinctions |
| Trial users → active vs. inactive | Behavior-based; requires product event integration |
| Churned customers | For winback targeting |

---

## Phase 5 — Campaign Cadence

Campaigns are one-time or recurring sends — newsletters, promotions, product launches. They are not flows.

### eCommerce Campaign Cadence

**Recommended starting cadence:**

| Type | Frequency | Sent to |
|------|-----------|---------|
| Product / editorial newsletter | 2× per month | Engaged segment (90 days) |
| Promotional / sale | As needed, max 2× per month | Engaged segment, exclude recent buyers |
| Product launch | Per launch | Full engaged list |
| Seasonal | Per season (BF/CM, Q4, etc.) | Full engaged list with suppression |

**Frequency guardrails:**
- Absolute minimum: 1× per month (below this, list goes cold and deliverability suffers)
- Sweet spot: 4–8× per month (combined flows + campaigns)
- Warning threshold: above 8× per month increases unsubscribe and complaint rates

**Send day and time baseline (test with own audience):**
- Tuesday–Thursday performs best across most consumer brands
- 9–11 AM or 6–8 PM local time for peak engagement
- Avoid Friday afternoon and Monday morning

### B2B/SaaS Campaign Cadence

| Type | Frequency |
|------|-----------|
| Value-first newsletter (tips, insights, case studies) | 1–2× per month |
| Product update / feature announcement | Per release (not every minor update) |
| Promotional / discount | Quarterly max — B2B audiences respond poorly to frequent discounts |
| Re-engagement campaign | 1× per quarter to at-risk segment |

**B2B frequency guardrails:**
- Maximum 2 marketing emails per contact per week
- Above this, unsubscribe rates spike and sales sequence open rates drop

---

## Phase 6 — Revenue Attribution Setup

Agreed attribution must be set before any performance review. Disagreeing on attribution after the fact creates client trust problems.

### eCommerce Attribution

Standard: **5-day click, 1-day open** attribution window in Klaviyo (industry standard for eCommerce).

| Window | What it means |
|--------|--------------|
| 5-day click | A purchase within 5 days of clicking an email is attributed to email |
| 1-day open | A purchase within 1 day of opening (but not clicking) is attributed to email |

Do NOT use 30-day attribution windows — they over-credit email and will create inflated expectations.

**What to track per month:**
- Email-attributed revenue (Klaviyo dashboard → Revenue)
- Revenue breakdown: flows vs. campaigns
- Email revenue as % of total revenue (pull total from Shopify)
- Revenue per recipient by flow (flows → individual flow → RPR metric)

**Reporting cadence:** Weekly Slack update + monthly review deck. Reference the `ads-weekly-slack-report` skill for the cross-platform weekly report format.

### B2B/SaaS Attribution

Email attribution in B2B is last-touch by default in most ESPs, which under-credits email's role in multi-touch journeys.

Recommended approach: track email as an "assist" channel alongside the primary attribution model. In Klaviyo, use the Contacts reports to see which deals have email touchpoints in their history.

**What to track:**
- Email-attributed leads (contact source = email form or email click)
- Email open-to-form-completion rate per campaign
- Workflow completion rates (what % of contacts complete the nurture sequence)
- Trial activation rate for onboarding sequences (requires product event integration)

---

## Reference Files

This skill uses reference materials. When running inside an orchestrated workflow, the orchestrator will locate and load these automatically via Glob.

- `assets/brand-strategy.md` — Flow ROI benchmarks, flow sequencing rationale, advanced segmentation recipes, campaign content calendar templates, and attribution model comparisons. Read during Phases 3–6.

---

## Phase 7 — Output: Strategy Brief

Produce a written strategy brief covering:

1. **Deliverability status** — prerequisites met or outstanding actions
2. **Flow build plan** — tiered list with rationale and estimated timeline
3. **Segmentation model** — master list + engagement segments + platform-specific additions
4. **Campaign cadence** — frequency, types, send rules
5. **Attribution setup** — agreed attribution windows and monthly metrics
6. **Success benchmarks** — what good looks like at 30/60/90 days

> "Strategy ready. How would you like it delivered?
>
> 1. **Written brief** — in this conversation
> 2. **DOCX** — formatted document for internal use or client review
> 3. **Slide deck addition** — strategy slide for a client onboarding or QBR deck"

Wait for format choice. Then, if DOCX is chosen, confirm branding:

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

For DOCX with branding: invoke the docx skill. Read `../../assets/brand-strategy.md` for exact colors, fonts, and layout rules.

---

## Phase 8: Synthesis Brief

Before finalizing the strategy brief, write a synthesis of key findings. This is used by the orchestrator to carry findings forward to the next skill in a multi-skill workflow.

**Email Strategy Key Findings**

Extract and summarise:
- **Deliverability baseline:** SPF/DKIM/DMARC status, spam complaint rate, list health composition (% engaged, % unengaged) — flag any prerequisites that must be fixed before flow build
- **Flow prioritisation:** Tier 1, 2, and 3 flows ranked by revenue impact and estimated monthly recovery/uplift for each critical flow (especially welcome and abandoned cart)
- **Segmentation model:** Master list structure, engagement segments (30/90/180 day windows), suppression rules, and how this differs from current state if audit has been run
- **Attribution window:** Agreed click/open attribution model for this client and platform, with 30/60/90-day revenue reporting benchmarks
- **Timeline:** Phased build plan with estimated weeks to completion for each tier

**Priority for downstream skills:** The email-copywriting skill should prioritise writing copy for Tier 1 flows identified in this strategy, starting with the welcome series and abandoned cart emails. Copy tone and length should reflect the flow type (eCommerce urgency vs. B2B nurture). The platform-specific execution skills (klaviyo-flows or Klaviyo-email) should use the flow prioritisation and segmentation model here as the exact build spec.

*If running standalone (not in an orchestrated chain), share this synthesis with the operator before the full deliverable.*

---

## QA Gate

Before delivering the strategy:

- [ ] Deliverability prerequisites confirmed or flagged as outstanding
- [ ] Flow priority order is vertical-appropriate (eCommerce vs B2B/SaaS) — not a generic list
- [ ] Segmentation model includes suppression of unengaged contacts from campaign sends
- [ ] Campaign cadence has frequency guardrails noted
- [ ] Attribution window explicitly agreed (not left ambiguous)
- [ ] 30/60/90-day benchmarks defined so success is measurable

---

## References

- **[Strategy Playbook](../../assets/brand-strategy.md)** — Read during Phases 3–6. Flow ROI and sequencing rationale, advanced segmentation recipes, campaign content calendar templates, and attribution model comparisons.
- **[Klaviyo Campaigns](../klaviyo-campaigns/SKILL.md)** — Use for newsletter, promotional, and BFCM campaign execution once campaign cadence is defined in the strategy.
- **[Email Copywriting](../email-copywriting/SKILL.md)** — Use this skill to write the actual email copy once the strategy is defined here.
