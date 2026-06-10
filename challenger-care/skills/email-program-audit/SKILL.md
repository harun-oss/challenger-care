---
name: email-program-audit
description: Audit the Klaviyo email program end-to-end. Maps existing flows + campaigns, benchmarks list health and deliverability, identifies revenue gaps, produces a prioritised build plan. Run once during program revival; outputs become assets. MANDATORY TRIGGER: any mention of "audit our email program", "diagnose Klaviyo", "what email do we have running", "email program review", "what flows are live", "Klaviyo health check". Do NOT use for: building a specific flow (use `klaviyo-flows` or `build-next-email-flow`). Writing copy (use `email-copywriting`). Email strategy decisions (use `email-strategy`).
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/goals-targets.md, assets/team-roles.md, CONFIG.md, mcp:klaviyo


# Email Program Audit

## What this skill does

Maps a client's existing email program, benchmarks it against what a healthy program looks like for their vertical, identifies what's missing and what it's costing them, and produces a prioritised build plan.

This skill is platform-agnostic. It works the same way whether Challenger is on Klaviyo, Klaviyo, ActiveCampaign, Mailchimp, Omnisend, or anything else. Platform-specific execution skills are invoked after this audit defines what to build.

Use this skill when:
- Starting email work with a new client
- Auditing an existing client's email before proposing expanded scope
- An AM needs to understand the current state before building anything
- Determining which platform-specific skills to use next

---

## Reference Files

This skill uses reference materials. When running inside an orchestrated workflow, the orchestrator will locate and load these automatically via Glob.

- `assets/brand-strategy.md` — List health benchmarks by vertical and platform, flow quality checklist, deliverability diagnosis and remediation, and revenue gap estimation benchmarks. Read during Phases 3–7.

---

## Phase 1 — Context

Ask one question at a time:

1. **Client name and what they sell** — who is this for?
2. **Vertical** — eCommerce (Shopify/DTC) or Lead Gen/B2B/SaaS?
3. **Email platform** — which ESP are they on? (Klaviyo / Klaviyo / ActiveCampaign / Mailchimp / Omnisend / Other / Unknown)
4. **Do we have admin access?** — can we log in to their ESP, or are we working from screenshots/exports Challenger has shared?
5. **List size** — approximately how many contacts/subscribers?
6. **Current email revenue** — for eCommerce: what % of total revenue is attributed to email? For Lead Gen: are they tracking email-sourced leads or pipeline?

If Challenger's platform is unknown, ask: "What tool do they use to send emails — do you know?" If still unknown, proceed to Phase 2 and flag platform identification as the first action.

---

## Phase 2 — Platform & Access Inventory

Before auditing performance, confirm what we're working with.

**Platform identification (if not confirmed):**

| Platform | Typical indicators |
|----------|-------------------|
| Klaviyo | Shopify-integrated, eCommerce DTC, "flows" terminology |
| Klaviyo | B2B, CRM-integrated, "workflows" and "sequences" |
| ActiveCampaign | SMB B2B or service businesses, "automations" and "deals" |
| Mailchimp | Smaller lists, less sophisticated automation, "journeys" |
| Omnisend | eCommerce, competes with Klaviyo, SMS-integrated |
| Drip | eCommerce, "workflows", Shopify-integrated |
| Brevo | European clients, lower cost, mixed B2B/eCommerce |

**Access checklist:**

- [ ] Admin or editor access to ESP confirmed
- [ ] Domain authentication status visible (SPF, DKIM, DMARC) — check in ESP settings or ask client
- [ ] Sending domain confirmed (e.g., hello@brand.com or noreply@brand.com)
- [ ] Integration confirmed: ESP ↔ eCommerce platform (Shopify, WooCommerce, etc.) or CRM (Klaviyo, Salesforce)
- [ ] Unsubscribe and suppression lists accessible

If access is not yet granted, note what's needed before the audit can be completed and continue with whatever Challenger or AM can share.

---

## Phase 3 — List Health Audit

Pull or ask for the following metrics. Compare against benchmarks in `assets/brand-strategy.md`.

**List composition:**
- Total contacts / subscribers
- Active (engaged) subscribers: opened or clicked in last 90 days
- Unengaged: no open or click in 90–180 days
- Suppressed / unsubscribed count

**Engagement metrics (last 30 days of sends):**
- Average open rate
- Average click rate
- Unsubscribe rate per campaign
- Bounce rate (hard + soft)
- Spam complaint rate

**List growth:**
- How is the list being built? (Pop-up / checkout capture / lead magnet / manual import)
- Approximate monthly net growth rate

> For benchmark comparisons by vertical and platform, and for what each metric indicates, read `assets/brand-strategy.md` → List Health Benchmarks section.

---

## Phase 4 — Flow / Automation Inventory

Map every automated flow or sequence that is currently live. Then compare against the essential flow set for their vertical.

For each flow found, record:
- Flow name
- Status: Live / Paused / Draft
- Trigger
- Number of emails in the sequence
- Last edited date (if visible)

**Essential flows by vertical:**

### eCommerce — Essential Flows

| Flow | Priority | Status to capture |
|------|----------|------------------|
| Welcome series (email capture → first purchase) | Critical | Live / Paused / Missing |
| Abandoned cart | Critical | Live / Paused / Missing |
| Browse abandonment | High | Live / Paused / Missing |
| Post-purchase (thank you + cross-sell) | High | Live / Paused / Missing |
| Winback / re-engagement | High | Live / Paused / Missing |
| Sunset (suppression of chronically unengaged) | Medium | Live / Paused / Missing |
| Back-in-stock | Medium | Live / Paused / Missing |
| Price drop alert | Low | Live / Paused / Missing |
| Review request | Medium | Live / Paused / Missing |
| VIP / loyalty | Low | Live / Paused / Missing |

### Lead Gen / B2B / SaaS — Essential Flows

| Flow | Priority | Status to capture |
|------|----------|------------------|
| Welcome / lead magnet delivery | Critical | Live / Paused / Missing |
| Lead nurture (problem-aware to solution-aware) | Critical | Live / Paused / Missing |
| Demo / call booking confirmation + reminder | Critical | Live / Paused / Missing |
| Post-demo follow-up | High | Live / Paused / Missing |
| Trial onboarding (SaaS) | Critical | Live / Paused / Missing |
| Trial expiry / conversion | High | Live / Paused / Missing |
| Winback (churned customers) | Medium | Live / Paused / Missing |
| Re-engagement (cold leads) | Medium | Live / Paused / Missing |

> For flow quality assessment criteria (not just whether a flow exists, but whether it's built well), read `assets/brand-strategy.md` → Flow Quality Checklist.

---

## Phase 5 — Campaign Audit

Campaigns are one-time or recurring sends (newsletters, promos, product launches) — not automated flows.

Ask or pull:
- How often are they sending campaigns? (Weekly / bi-weekly / monthly / ad hoc)
- What types? (Promotional / educational / product launches / seasonal)
- What are recent open and click rates on campaigns?
- Is there a campaign calendar or is sending ad hoc?

**Campaign health signals:**

| Signal | Healthy | Needs attention |
|--------|---------|----------------|
| Send frequency | 1–4x per month | <1x (underutilised) or >8x (fatigue risk) |
| Campaign open rate | Above list average | Declining week-over-week |
| Subject line approach | Varied (curiosity, value, urgency) | All similar format |
| Segmentation | Sends to engaged segments, not full list | All sends to full list |
| A/B testing | Subject lines tested | No testing at all |

---

## Phase 6 — Deliverability Check

Deliverability problems silently kill email performance. Check before building anything new.

**Domain authentication (check in ESP settings or via MXToolbox):**
- [ ] SPF record published and valid
- [ ] DKIM configured for the sending domain
- [ ] DMARC policy set (p=none minimum; p=quarantine or p=reject is better)
- [ ] Custom sending domain set up in ESP (not sending from a shared ESP domain)

**Sending reputation signals:**
- Spam complaint rate: must be below 0.1% (Gmail threshold)
- Hard bounce rate: should be below 2%
- If either is elevated: list hygiene issue — do not add new flows until resolved

> For deliverability diagnosis and remediation steps by issue type, read `assets/brand-strategy.md` → Deliverability section.

---

## Phase 7 — Revenue Gap Analysis

Translate missing flows and programme gaps into estimated monthly revenue impact.

**eCommerce revenue gap formula:**

For each missing critical or high-priority flow:
```
Estimated monthly revenue = (Monthly sessions or orders) × (Flow trigger rate) × (Flow conversion rate) × (AOV)
```

Use conservative estimates. The goal is not a precise number — it's a credible range that makes the build plan feel urgent.

**Example framing for Challenger:**
> "Based on your current monthly order volume and AOV, a working abandoned cart flow alone is estimated to recover $X–$X per month. You currently have no cart flow live."

> For revenue estimation benchmarks by flow type and vertical, read `assets/brand-strategy.md` → Revenue Gap Benchmarks section.

---

## Phase 8 — Output: Prioritised Build Plan

Summarise findings and produce the build plan.

**Build plan structure:**

**Tier 1 — Fix immediately (blocking issues)**
- Deliverability problems (domain auth, complaint rate) — nothing else matters until these are resolved

**Tier 2 — Build first (highest revenue impact)**
- Missing critical flows for the vertical
- List growth mechanism if none exists

**Tier 3 — Build next (high impact)**
- Missing high-priority flows
- Campaign cadence and segmentation improvements

**Tier 4 — Build later (good to have)**
- Medium and low priority flows
- A/B testing programme
- Advanced segmentation

**Platform routing:**
Based on the audit findings, identify which platform-specific skills to use for execution. Note at the bottom of the build plan:
> "Next step: use `[klaviyo-flows / Klaviyo-email / activecampaign-email]` to build Tier 1 and Tier 2 items."

**Output format options:**

> "Audit complete. How would you like the output?
>
> 1. **Written summary** — findings and build plan in this conversation
> 2. **DOCX report** — formatted audit document to share internally or with Challenger
> 3. **Slide deck addition** — audit findings slide to add to a strategy or onboarding deck"

For DOCX: invoke the docx skill. Read `../../assets/brand-strategy.md` for branding.

---

## Phase 9: Synthesis Brief

Before delivering the audit, write a brief summary of key findings. This is used by the orchestrator to carry findings forward to the next skill in a multi-skill workflow.

**Email Program Audit Key Findings**

Extract and summarise:
- **Platform and current flow state:** ESP identified, flows mapped (live/paused/missing) by vertical, total list size, recent send history. For eCommerce: which of the 5 critical flows (welcome, abandoned cart, browse, post-purchase, winback/sunset) are missing. For B2B/SaaS: nurture, trial onboarding, and re-engagement status.
- **List health and deliverability status:** % engaged (90-day window), % unengaged, bounce rate, spam complaint rate. SPF/DKIM/DMARC authentication status. Any immediate deliverability risks flagged — if present, these block new flow build until resolved.
- **Revenue impact of gaps:** Estimated monthly revenue opportunity from missing critical flows (especially abandoned cart and welcome for eCommerce), based on monthly order/session volume and client's AOV. This quantifies the urgency of the build plan.
- **Campaign cadence assessment:** Current send frequency (too low, appropriate, or unsustainable), segmentation quality (sends to full list vs engaged segments), A/B testing maturity.

**Priority for downstream skills:** The email-strategy skill should use these findings to build a prioritised flow roadmap with Tier 1/2/3 sequencing. The platform-specific execution skills (klaviyo-flows or Klaviyo-email) should follow the Tier 1 build order directly and use the list health findings to set flow filters (suppression, engagement windows) correctly from day one.

*If running standalone (not in an orchestrated chain), share this summary with the operator before the full audit report.*

---

## QA Gate

Before delivering the audit:

- [ ] Platform confirmed and access status noted
- [ ] All essential flows checked (not just the ones that exist — gaps documented too)
- [ ] List health metrics compared against benchmarks, not just recorded
- [ ] Deliverability authentication status confirmed — flag if any of SPF/DKIM/DMARC are missing
- [ ] Revenue gap expressed as a number range, not just "you're missing flows"
- [ ] Build plan is tiered and routes to the correct platform-specific skill

---

## References

Read these files when the relevant phase is reached:

- **[Audit Framework](../../assets/brand-strategy.md)** — Read during Phases 3–7. List health benchmarks by vertical and platform, flow quality checklist, deliverability diagnosis and remediation, and revenue gap estimation benchmarks.
- **[Email Strategy](../email-strategy/SKILL.md)** — Use after the audit to define the full flow architecture, segmentation model, and campaign cadence. The audit produces the input; email-strategy produces the plan.
- **[Brand](../../assets/brand-strategy.md)** — Read when producing any branded output (PPTX, DOCX, PDF). Colours, typography, and component patterns.
