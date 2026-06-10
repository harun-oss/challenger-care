---
name: meta-ads-tracking-audit
description: Maps the conversion funnel, audits Meta Pixel health, documents standard + custom events, assesses Conversions API (CAPI) setup for iOS 14+ compliance. Critical for Meta BM recovery. MANDATORY TRIGGER: any mention of "Meta tracking audit", "Meta Pixel audit", "pixel health check", "Meta conversion events", "CAPI setup", "Meta Pixel events", "iOS 14 tracking". Do NOT use for: Account onboarding (one-time). Campaign builds (use `meta-ads-campaign-build`).
---

> **Permission tier:** stage · **Tools/context:** assets/brand-strategy.md, assets/team-roles.md, CONFIG.md


# Meta Ads Tracking Audit

**Owner:** the operator
**Timeline:** Week 2 — kickoff deliverable #1
**Outcome:** Client funnel mapped, all conversion events documented and verified, Pixel + CAPI health confirmed, Tracking Audit deck delivered to client.

---

## Phase 1: Context

Ask the operator:
1. **Client name** — who is this audit for?
2. **Business type** — eCommerce or Lead Gen/B2B?
3. **Pixel status** — does an existing Meta Pixel exist on the site, or are we starting fresh?
4. **Website platform** — Shopify, WooCommerce, custom, or something else?

> Why it matters: eCommerce and Lead Gen have different priority events. Shopify has native Meta integration; custom sites usually need manual GTM setup. This shapes the entire audit.

If a pixel already exists: the audit starts with a health check (Phase 3). If there is no pixel yet: jump to Phase 4 to define the event plan first, then Phase 5 for CAPI guidance.

---

## Phase 2: Funnel Mapping

Map Challenger's funnel before touching Pixel settings. This creates the strategic framework that determines which events to track and how to weight them.

Ask the operator to walk through:
- **Top of funnel:** What pages do new visitors land on? (Homepage, blog, landing pages?)
- **Middle of funnel:** What actions signal consideration? (Product views, category browsing, pricing page, content downloads?)
- **Bottom of funnel:** What is the primary conversion? (Purchase, lead form, demo booking, phone call?)
- **Post-conversion:** Is there a repeat purchase cycle? Subscription upsell? Referral?

Document the funnel as a simple map:

```
Awareness → [Traffic source] → [Landing page]
Consideration → [Key pages / actions]
Conversion → [Primary event] + [Secondary events]
Post-conversion → [Upsell / retention events]
```

Confirm the funnel map with the operator before moving to event selection. If the funnel is unclear, pull from the Client Workbook or ask the operator for clarity.

---

## Phase 3: Pixel Health Check

*Skip this phase if no pixel exists yet.*

> Before running the health check, read `references/pixel-health-checklist.md` for the full diagnostic steps, common failure modes, and fix instructions by platform.

Check the following:

| Check | Tool | Pass Condition |
|---|---|---|
| Pixel fires on all key pages | Meta Pixel Helper (Chrome) | Green checkmark, correct Pixel ID |
| Correct Pixel ID | Meta Events Manager | Matches the Ad Account's Dataset |
| No duplicate pixel fires | Pixel Helper | Only 1 PageView event per page load |
| Purchase event fires on confirmation page | Test Events tool | Event received with correct value + currency |
| No mismatched events | Events Manager | Event names match standard or agreed custom names |
| Pixel data flowing within last 7 days | Events Manager > Overview | Active signal, no "No recent activity" warning |

**Flag immediately if:**
- Pixel fires with a different ID than the Ad Account's Dataset — this means conversions are being reported to the wrong account
- Duplicate PageView fires — inflates metrics and confuses the algorithm
- Purchase event missing value parameter — ROAS reporting will be broken
- No data in last 7 days on a live site — pixel may be blocked or broken

---

## References

- **[Pixel Health Checklist](references/pixel-health-checklist.md)** — Full diagnostic steps, common failure modes by platform, fix instructions, and verification procedures. Read during Phase 3 before running the health check.
- **[Meta Pixel Events](references/meta-pixel-events.md)** — Standard event list by vertical, custom event creation guidance, naming conventions, and value parameter specifications. Read during Phase 4 when documenting and auditing events.
- **[CAPI Setup Guide](references/capi-setup-guide.md)** — Conversions API configuration, iOS 14+ compliance setup, event deduplication, and server-side tracking implementation. Read during Phase 5 before setting up CAPI.

---

## Phase 4: Event Audit & Documentation

> For the full standard event list by vertical and custom event guidance, read `references/meta-pixel-events.md` before completing this phase.

Map which events exist (or need to be created) against the funnel:

### eCommerce Priority Events (in order of importance)

| Event | Status | Notes |
|---|---|---|
| Purchase | ✓ / ✗ / Needs fix | Include value + currency parameters |
| AddToCart | ✓ / ✗ / Needs fix | Fire on Add to Cart button click |
| InitiateCheckout | ✓ / ✗ / Needs fix | Fire on checkout page load |
| ViewContent | ✓ / ✗ / Needs fix | Fire on product page load |
| CompleteRegistration | ✓ / ✗ / Needs fix | If account creation is a goal |

### Lead Gen Priority Events (in order of importance)

| Event | Status | Notes |
|---|---|---|
| Lead | ✓ / ✗ / Needs fix | Fire on form submission confirmation |
| CompleteRegistration | ✓ / ✗ / Needs fix | For sign-up flows |
| Contact | ✓ / ✗ / Needs fix | For contact form submissions |
| ViewContent | ✓ / ✗ / Needs fix | For key landing pages |
| Schedule | ✓ / ✗ / Needs fix | If demo/call booking is a goal |

For each event with issues: document what's wrong and what needs to be fixed. If this is a new pixel: this table becomes the implementation spec for the developer or client.

---

## Phase 5: Conversions API (CAPI) Assessment

CAPI is no longer optional — iOS 14+ privacy changes mean browser-only tracking misses 20–40% of conversions for many accounts. Ask:

1. **Is CAPI already set up?** Check Events Manager → Settings → Conversions API.
2. **What's the Event Match Quality (EMQ) score?** A score below 6/10 means poor data quality — ad delivery and optimization will suffer.
3. **Is deduplication active?** Browser events + CAPI events must share the same `event_id` to prevent double-counting.

> For platform-specific CAPI setup instructions (Shopify, WooCommerce, custom), read `references/capi-setup-guide.md`.

**CAPI status summary:**

| Item | Status |
|---|---|
| CAPI connected | Yes / No / Partial |
| Event Match Quality score | [X/10] |
| Deduplication configured | Yes / No |
| Recommendation | [Action needed] |

If CAPI is not set up: add this as a priority recommendation in the audit deck. For Shopify clients, CAPI can be enabled in minutes via the native Meta Sales Channel integration.

---

## Phase 6: Tracking Plan Documentation

Compile everything into the tracking plan — this is what goes into the Tracking Audit deck slide:

```
Client: [Name]
Platform: [Shopify / WooCommerce / Custom]
Pixel ID: [AW-XXXXXXX]
Dataset ID: [Same as Pixel ID in most cases]

Conversion Events:
  Primary: [e.g., Purchase — value + currency]
  Secondary: [e.g., AddToCart, InitiateCheckout]

Pixel Health: [✓ Clean / ⚠ Issues found — list them]

CAPI Status: [Connected / Not connected]
EMQ Score: [X/10]
Deduplication: [Active / Not configured]

Open Issues:
  1. [Issue + recommended fix]
  2. [Issue + recommended fix]

Priority Actions Before Launch:
  - [Highest priority fix]
  - [Second priority fix]
```

Before moving to output, confirm the tracking plan with the operator: "Does this match what you've observed in Events Manager?"

---

## Phase 7: Synthesis Brief

Before delivering the final audit, write a brief summary of key findings. This is used by the orchestrator to carry findings forward to the next skill in a multi-skill workflow.

**[Client Name] Tracking Audit Key Findings**
- Top finding 1 — specific pixel health status. Example: "Pixel is clean and firing correctly on all priority events. Purchase event includes value + currency parameters. EMQ score is 8/10 — excellent data quality for optimization"
- Top finding 2 — specific CAPI status. Example: "CAPI is connected with deduplication active. Browser + server-side tracking provides 95%+ conversion attribution visibility"
- Top finding 3 — specific issue or blocker. Example: "No critical issues. One minor fix needed: InitiateCheckout event should fire on cart page; currently fires on checkout only"

**Priority for downstream skills:** What the next skill should focus on. Example: "Tracking is reliable and ready for campaign launch. Next skill can confidently optimize for Purchase event with full conversion visibility. CAPI setup means iOS tracking gaps are minimal."

*If running standalone (not in an orchestrated chain), share this summary with the operator before the full deliverable.*

---

## Phase 8: Output Format + Branding

> "Tracking audit complete. What format would you like for the deliverable?
>
> 1. **DOCX Report** — full written audit with funnel map, event table, CAPI assessment, and priority action list. For internal records or client handoff.
> 2. **Slide brief** — structured notes to populate the [Tracking Audit template deck](https://docs.google.com/presentation/d/1Yx2dXdOM_fEACvo7CUfdFbyCr0uaJzvS6J7-Nta3SeU/edit) — first slide + event table + issues list
> 3. **Verbal summary** — I'll walk through findings in this conversation"

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colours, fonts, and layout rules before building output.

Build based on chosen format:
- **DOCX** → invoke the docx skill; apply branding; structure as: funnel map → pixel health → event audit → CAPI → priority actions
- **Slide brief** → output slide-by-slide notes ready to paste into the template deck
- **Verbal** → walk through findings section by section in this conversation

---

## Reference Files

This skill uses reference materials. The orchestrator will locate and load these automatically via Glob.

- `references/pixel-health-checklist.md` — Full diagnostic steps, common failure modes by platform, fix instructions, and verification procedures. Needed during Phase 3 before running the health check.
- `references/meta-pixel-events.md` — Standard event list by vertical, custom event creation guidance, naming conventions, and value parameter specifications. Needed during Phase 4 when documenting and auditing events.
- `references/capi-setup-guide.md` — Conversions API configuration, iOS 14+ compliance setup, event deduplication, and server-side tracking implementation. Needed during Phase 5 before setting up CAPI.

---

## Pre-Delivery QA

Before delivering output:
- [ ] Funnel map confirmed with the operator
- [ ] All priority events audited (status documented for each)
- [ ] Pixel health check completed (or noted as N/A for new pixel)
- [ ] CAPI status assessed and EMQ score noted
- [ ] Open issues listed with recommended fixes
- [ ] Priority actions identified (ranked by impact)
- [ ] Synthesis brief written (if in an orchestrated chain)
- [ ] Output format and branding preference confirmed
