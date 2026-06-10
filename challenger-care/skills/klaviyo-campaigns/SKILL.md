---
name: klaviyo-campaigns
description: Builds, schedules, segments, and optimises one-time Klaviyo campaign sends · newsletters, promotional campaigns, product launches, BFCM, SMS campaigns. Covers A/B testing, Smart Send Time, send-time analytics. MANDATORY TRIGGER: any mention of "Klaviyo campaign", "send a campaign", "Klaviyo newsletter", "Klaviyo promotional email", "BFCM campaign", "Klaviyo SMS", "schedule a Klaviyo email", "Klaviyo broadcast", "subject line test Klaviyo". Do NOT use for: Klaviyo flows or automations (use `klaviyo-flows` or `build-next-email-flow`). Email strategy (use `email-strategy`).
---

> **Permission tier:** stage · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/team-roles.md, CONFIG.md, mcp:klaviyo


# Klaviyo Campaigns

## What this skill does

Covers the campaign side of Klaviyo — one-time and recurring sends to lists and segments. Flows run automatically when a contact does something; campaigns are intentional sends the team schedules to a defined audience. Both channels are required for a healthy email programme. Neither replaces the other.

Most eCommerce email revenue comes from flows (30–50% of total email revenue despite a fraction of the send volume). Campaigns do a different job: they maintain the relationship between purchase events, drive repeat purchase from existing customers, and create the promotional moments (BFCM, launches, flash sales) that flows cannot replicate.

Use this skill when:
- Sending the weekly or bi-weekly newsletter
- Planning a promotional campaign (sale, product launch, flash event)
- Building the BFCM campaign sequence
- Setting up A/B tests on campaign subject lines or content
- Planning SMS campaign sends
- Reviewing campaign analytics and improving performance

---

## Reference Files

This skill uses reference materials. When running inside an orchestrated workflow, the orchestrator will locate and load these automatically via Glob.

- `assets/brand-strategy.md` — Full segmentation recipes, BFCM campaign calendar and content angles, A/B testing examples, newsletter content framework, MPP reporting setup, and SMS compliance reference. Read during Phases 4–9.

---

## Phase 1 — Context

Ask one question at a time:

1. **What type of campaign?** — newsletter, promotional/sale, product launch, BFCM, re-engagement, or SMS?
2. **Who is the audience?** — entire list, engaged segment, VIP customers, new subscribers?
3. **How large is the sendable list?** — this determines which send time and A/B test options apply
4. **What is the sending history?** — new domain, recently reactivated, or established 30+ day history?
5. **SMS included?** — if yes, confirm opt-in status and TCPA compliance before proceeding

---

## Phase 2 — Campaigns vs Flows: The Distinction

Getting this wrong wastes build time. The wrong tool for the job produces worse results even with perfect copy.

| | **Campaigns** | **Flows** |
|---|---|---|
| **Trigger** | Manually scheduled, one-time send | Automated, triggered by contact action or date |
| **Audience** | Defined at send time (list or segment snapshot) | Enrolled individually as trigger fires |
| **Timing** | Everyone receives it on the same day | Each contact receives it at their own moment |
| **Revenue role** | Relationship maintenance, promotions, repeat purchase | High-intent capture (cart, browse, welcome) |
| **Revenue share** | ~50–70% of email sends, lower RPR | ~30–50% of email revenue from fewer sends |
| **Best for** | Newsletters, sales events, product launches, BFCM | Welcome, abandoned cart, post-purchase, winback |

**Rule:** If the email should go to everyone at the same time in response to a business event (a sale, a launch, a newsletter date) → Campaign. If the email should reach each contact at a specific moment in their journey → Flow.

---

## Phase 3 — Campaign Types

### Newsletter
Frequency: 1–2× per week for engaged eCommerce lists. Content: education, product stories, brand voice, user-generated content. No heavy promotional pressure — the newsletter builds the relationship that makes promotions convert.

**Audience:** 90-day engaged segment. Never send newsletters to unengaged contacts — damaged reputation harms all future sends.

### Promotional / Sale
For flash sales, seasonal promotions, and clearance. Higher frequency acceptable during the event window (2–3 sends over a 48–72hr window). Exclude recent purchasers where possible.

**Audience:** 60-day engaged segment + exclude anyone who already purchased in the last 7 days.

### Product Launch
1–3 emails over the launch window. Email 1: announcement + early access or waitlist. Email 2: launch day. Email 3: last chance / social proof 3–5 days later.

**Audience:** Full engaged list (90-day); VIP segment gets Email 1 a day early.

### BFCM Sequence
The highest-stakes campaign of the year. Requires a full multi-send plan, audience warming 4–6 weeks in advance, and a separate segmentation strategy. See Phase 7 and `assets/brand-strategy.md` → BFCM Campaign Plan.

### Re-engagement Campaign
A one-off campaign to contacts who have gone quiet — distinct from the automated re-engagement *flow*. Used when a list hasn't been sent to in 60+ days, or before BFCM to re-activate dormant contacts safely.

**Audience:** 90–180-day unengaged segment. Limit volume to 20% of your normal weekly send to avoid complaint rate spikes.

---

## Phase 4 — Segmentation for Campaigns

Segmented campaigns return 3× more revenue per recipient than unsegmented sends. The goal is always to send to the most relevant, engaged audience — not the largest one.

### Core Segments to Build

**Engaged (primary campaign audience):**
- Clicked email in last 90 days OR opened email in last 30 days
- Klaviyo provides default 30-, 60-, and 90-day engaged segments — use these as your base
- Filter: "Apple Privacy Open = False" for open-based conditions to exclude MPP-inflated opens

**VIP Customers:**
- Placed 2+ orders AND placed order in last 90 days AND is in top 25% by total spend
- Campaign approach: early access, exclusive offers, loyalty communications

**Recent Subscribers (not yet purchasers):**
- Subscribed in last 30 days AND has never placed an order
- Campaign approach: trust-building, social proof, first-purchase incentive

**Never Engaged:**
- Has never opened or clicked any email
- Never send regular campaigns here; they should be in the re-engagement flow only, and suppressed if they don't re-engage within 90 days

### Suppression Rules

Always exclude from campaign sends:
- Unsubscribed (automatic)
- Hard bounced (automatic)
- Spam complaints (automatic)
- Anyone who received an email in the last 16 hours (Smart Sending handles this if enabled)
- For promotional campaigns: exclude contacts who purchased the promoted item in the last 7 days

### Campaign Deduplication

Klaviyo automatically deduplicates profiles when sending to multiple lists or segments in a single campaign (maximum 15 groups per campaign). A contact included in two segments will only receive the campaign once. Never split the same campaign across separate sends to avoid duplicates — add all groups to one campaign.

> For full segmentation recipes including RFM-based campaign segments and pre-BFCM warming segments, read `assets/brand-strategy.md` → Segmentation Recipes.

---

## Phase 5 — Building a Campaign in Klaviyo

**Path:** Marketing → Campaigns → Create Campaign → Email (or SMS)

### Step-by-step

1. **Name the campaign** using the naming convention: `YYMMDD_email_[type]_[audience]`
   - Example: `250901_email_promo_90day-engaged`
   - Lowercase, underscores between concepts, dashes within phrases

2. **Select audience** — add lists or segments to include; add exclusion segments
   - Include: primary target segment
   - Exclude: recent purchasers, unsubscribers (automatic), any suppression lists

3. **Design the email** — select template or create from scratch
   - Always fill in the plain text version (deliverability + accessibility)
   - Always fill in preview text (never leave blank — ESP pulls first line of email if empty)

4. **Choose send strategy:**

| Strategy | When to use | Key constraint |
|----------|-------------|---------------|
| **Fixed Send Time** | Most campaigns; specific day/time | Send in recipient timezone recommended |
| **Gradual Send** | Very large lists (50,000+); new domain warming | Cannot combine with A/B testing |
| **Smart Send Time** | Large audiences wanting audience-level optimisation | Requires 12,000+ recipients minimum |

5. **Smart Sending (16hr frequency cap)** — leave enabled for all regular campaigns. During BFCM window (Black Friday through Cyber Monday), disable it — buyer intent is high and multiple sends per day are expected.

6. **Review and schedule** — send test email to yourself first; check mobile preview in Klaviyo's preview tool; confirm recipient count is as expected.

---

## Phase 6 — A/B Testing Campaigns

Every campaign is a learning opportunity. Run a structured A/B test whenever the audience is large enough.

### What to test (priority order)
1. **Subject line** — highest leverage; affects every recipient; test first
2. **From name** — "[Brand]" vs "[First name] from [Brand]" — especially impactful for B2B-adjacent sends
3. **Email content** — hero image vs no image; long copy vs short copy; one CTA vs two
4. **Send time** — only when subject line and content are already optimised

### Minimum requirements for valid results

| Requirement | Threshold |
|-------------|-----------|
| Recipients per variant | 50 minimum; 1,000+ recommended |
| Win probability | 90%+ = statistically significant; 75–89% = "Promising" (not conclusive) |
| Test variants | Maximum 4 |

**Cannot A/B test with Gradual Send** — the variable distribution across time confounds results. Choose one.

### Winner determination
- **Automatic:** Klaviyo selects winner in real-time based on chosen metric (open rate, click rate, or revenue per recipient)
- **Manual:** Review results yourself and select the winner to send to remaining audience
- **Recommended metric:** Revenue per recipient if audience is large enough; click rate otherwise. Avoid using open rate as the primary winner metric — Apple MPP inflates opens for a significant portion of most audiences.

### Document every test

Follow the A/B test template in `email-copywriting`'s references — hypothesis, variable changed, win condition defined before send. Results with no documentation produce data, not learning.

> For worked A/B test examples specific to campaigns, read `assets/brand-strategy.md` → A/B Testing.

---

## Phase 7 — BFCM Campaign Planning

BFCM is the highest-revenue email event of the year. It requires a plan, not improvisation.

**Minimum lead time: 6 weeks before Black Friday**

### Audience warming (4–6 weeks before BFCM)

The goal is to reactivate as many contacts as safely possible before high-volume promotional sends begin. Sending cold to a large unengaged list immediately before BFCM destroys sender reputation exactly when it matters most.

1. **Week 6–5:** Send to 30-day engaged segment only. Confirm deliverability is clean.
2. **Week 4–3:** Expand to 60-day engaged. Monitor complaint rate (must stay below 0.1%).
3. **Week 2–1:** Expand to 90-day engaged. Run a re-engagement campaign for 90–180-day contacts — only those who re-engage get added to the BFCM list.
4. **Never send BFCM campaigns to 180+ day unengaged contacts** — spam trap and complaint risk; these contacts should be in the sunset flow.

### Smart Sending during BFCM

Disable Smart Sending for BFCM promotional campaigns. Buyer intent during BFCM is at its peak; the 16-hour frequency cap will suppress sends that should go out. Re-enable after Cyber Monday.

### Campaign sequence (minimum)

| Timing | Send | Audience |
|--------|------|----------|
| 1 week before | VIP early access announcement | VIP segment only |
| 2–3 days before | Offer preview / "coming soon" | 90-day engaged |
| Black Friday AM | Full launch | 90-day engaged |
| Black Friday PM | Reminder (non-openers/non-clickers) | Non-openers from AM send |
| Saturday | "Extended" or social proof | Clickers who haven't purchased |
| Sunday | Final weekend reminder | Non-purchasers from Friday |
| Cyber Monday AM | Cyber Monday offer (new or extended) | 90-day engaged minus recent purchasers |
| Cyber Monday PM | Last chance | Non-purchasers |

> For the full BFCM calendar, content angles, and SMS integration plan, read `assets/brand-strategy.md` → BFCM Campaign Plan.

---

## Phase 8 — SMS Campaigns

Klaviyo supports email and SMS campaigns from the same platform. SMS campaigns have different rules, compliance requirements, and performance benchmarks.

### Compliance requirements (non-negotiable)

- **Only send to currently opted-in subscribers** — prior opt-in from another channel does not carry over
- **Separate opt-in from email** — SMS and email must have separate consent checkboxes; a combined checkbox violates compliance
- **Double opt-in strongly recommended** — required by many carriers, especially for abandoned cart SMS
- **Include opt-out language** in every US SMS message; carriers recommend explicit opt-out at minimum every 5th message
- **Quiet hours (TCPA, US):** 8 AM – 9 PM in the recipient's timezone; state-specific rules may apply (e.g., Florida: 8 AM – 8 PM)

### Character limits

| Format | Limit | Note |
|--------|-------|------|
| SMS (no emoji) | 160 characters | Single segment |
| SMS (with emoji or special characters) | 70 characters | Single segment |
| 2-segment SMS | 306 characters | Header uses 14 chars |
| MMS | 1,600 characters | Image or GIF included |

**Best practice:** Keep all SMS under 160 characters. Longer messages are broken into multiple segments by carriers, which increases cost and reduces readability.

### SMS campaign strategy

SMS is the highest-urgency channel — it sits next to personal texts and is opened within minutes. Use it for:
- Flash sale announcements (time-sensitive, 24hr window)
- BFCM early access to VIP subscribers
- Limited stock alerts
- Event reminders

Do not use SMS for: newsletters, content-heavy educational messages, or anything that doesn't create immediate action.

---

## Phase 9 — Send Time Strategy

Three send time approaches in Klaviyo campaigns — choose based on audience size and campaign type.

| Approach | How it works | Minimum audience | Best for |
|----------|-------------|-----------------|----------|
| **Fixed Send Time** | Sends at a specific time to all recipients | Any size | Most campaigns |
| **Personalized Send Time** | Klaviyo sends each contact at their individually predicted best time, within a window you set | Any size (AI needs data per profile) | Newsletters, evergreen content |
| **Smart Send Time** | Klaviyo runs two exploratory phases to find ONE optimal time for the whole audience | 12,000+ recipients | High-volume promotional sends |

**Personalized Send Time** is distinct from Smart Send Time — it optimises per individual (different send time per person), not per audience. It requires no minimum audience size and is the better default for most campaigns where the content is not urgently time-sensitive.

**Fixed Send Time baseline** (when no AI send time available): 10–11 AM or 2–3 PM in the contact's timezone. Tuesday, Wednesday, and Thursday outperform Monday and Friday for B2B-adjacent audiences; day of week matters less for high-frequency DTC.

**Do not use Personalized or Smart Send Time for:**
- Time-sensitive campaigns where the framing references a specific time ("Tonight only", "Ends at midnight")
- BFCM sends where urgency requires simultaneous arrival

---

## Phase 10 — Analytics and Optimisation

### Key campaign metrics (Klaviyo → Campaigns → select campaign)

| Metric | Healthy benchmark | Flag if |
|--------|------------------|---------|
| Open rate (MPP-adjusted) | 25–40% | Below 15% |
| Click rate | 2–5% | Below 1% |
| Unsubscribe rate | Below 0.3% | Above 0.3% |
| Spam complaint rate | Below 0.01% | Above 0.1% (Gmail blocks at 0.3%) |
| Revenue per recipient (RPR) | $0.08–$0.20 for campaigns | Below $0.05 |

### Apple MPP — accurate open rate reporting

Apple Mail prefetches tracking pixels, inflating open rates by 15–30% for most eCommerce audiences. Do not make segment or suppression decisions based on raw open rate.

**To get accurate data:**
- In Klaviyo custom reports: filter "Apple Privacy Open = False" to see true human opens
- Or switch the attribution model to "opened or clicked email (excluding Apple privacy opens)"
- Always use **click rate as the primary engagement signal** for campaign decisions, not open rate

### Monthly campaign optimisation checklist

- [ ] Review average campaign RPR — compare to previous month and 90-day trend
- [ ] Check if any campaign had unsubscribe rate above 0.3% — investigate content or audience mismatch
- [ ] Confirm engaged segment size is growing (or stable) — declining engagement = deliverability risk
- [ ] Review any A/B test results and apply learnings to next campaign
- [ ] Check Klaviyo deliverability tab for any domain or inbox placement flags
- [ ] Review SMS opt-in rate if applicable — declining opt-ins signal friction in signup flow

---

## QA Gate

Before any campaign goes live:

- [ ] Campaign named using convention: `YYMMDD_email_[type]_[audience]`
- [ ] Audience: engaged segment selected, unengaged excluded, recent purchasers excluded where relevant
- [ ] Plain text version filled in (not left blank)
- [ ] Preview text filled in (does not repeat subject line)
- [ ] Test email sent and reviewed on mobile and desktop
- [ ] Recipient count confirmed — cross-check against expected segment size
- [ ] Smart Sending setting confirmed (on for regular sends; off for BFCM)
- [ ] A/B test win condition defined before send (if running a test)
- [ ] For SMS: quiet hours enabled, opt-out language included, character count confirmed
- [ ] Unsubscribe link present in footer (Klaviyo includes automatically for opted-in lists — verify template hasn't stripped it)

---

## Phase 11: Synthesis Brief

Before campaign delivery, write a brief summary of campaign performance and learnings. This is used by the orchestrator to carry findings forward to the next skill in a multi-skill workflow.

**Klaviyo Campaigns Key Findings**

Extract and summarise:
- **Campaign cadence and schedule:** Weekly or bi-weekly newsletter send frequency and audience (e.g., "2 newsletters/week to 90-day engaged segment, size 42K and growing"). Promotional calendar for next quarter with scheduled sends (e.g., "3 flash promotions in January, BFCM sequence in November"). Any seasonal or event-driven sends planned. Note any frequency risks (total sends per week combined with flow sends).
- **Segmentation strategy and audience health:** Primary audiences used (90-day engaged, 60-day engaged, VIP, recent subscribers). Exclusion rules applied (recent purchasers, unsubscribes, suppressions). Engaged segment size trend (growing, stable, declining) and what it signals for deliverability. VIP segment characteristics and treatment (early access, exclusive offers).
- **A/B test results and subject line winners:** Most recent campaign A/B test winner and lift (e.g., "Curiosity gap subject line outperformed offer-forward by 3.2% open rate; apply to next 5 campaigns"). Secondary test queued (from name, send time, content length). Any subject line patterns emerging across successful campaigns (e.g., personalisation + specificity consistently wins).
- **BFCM readiness (if applicable):** Audience warming plan 6 weeks before Black Friday, re-engagement sequence planned for 90–180-day contacts, BFCM campaign sequence drafted, and expected frequency during BFCM window (Smart Sending disabled, daily sends possible).

**Priority for downstream skills:** Flow optimisation should monitor Smart Sending skip rates weekly — if campaign volume + flow sends exceed capacity, campaign frequency may need throttling. Email copywriting should iterate on highest-performing subject line formula and apply to future campaigns. Lead scoring/audience segmentation should validate that engaged segment definition is correctly filtering out unengaged contacts to protect sender reputation.

*If running standalone (not in an orchestrated chain), share this summary with the operator before campaign launch.*

---

## References

- **[Campaign Playbook](../../assets/brand-strategy.md)** — Read during Phases 4–9. Full segmentation recipes, BFCM campaign calendar and content angles, A/B testing examples, newsletter content framework, MPP reporting setup, and SMS compliance reference.
- **[Brand](../../assets/brand-strategy.md)** — Read when producing any branded output. Colours, typography, and component patterns.
- **[Email Copywriting](../email-copywriting/SKILL.md)** — Use for subject lines, preview text, and body copy for any campaign type.
- **[Klaviyo Flows](../klaviyo-flows/SKILL.md)** — Use for automated triggered sequences (welcome, cart, post-purchase, winback).
