---
name: google-ads-prelaunch-qa
description: Pre-launch QA checklist before Google Ads goes live · conversion tracking, campaign settings, keywords + ad groups, extension completeness, Quality Score alignment, PMAX readiness, change log setup. Saves wasted budget from bad launches. MANDATORY TRIGGER: any mention of "Google Ads pre-launch check", "QA Google Ads", "Google Ads launch checklist", "pre-launch Google Ads", "is Google Ads ready to launch", "Google Ads readiness check". Do NOT use for: Auditing live campaigns (use `google-ads-account-audit`). Building campaigns (use `google-ads-campaign-build`).
---

> **Permission tier:** stage · **Tools/context:** assets/team-roles.md, CONFIG.md


# Google Ads Pre-Launch QA

## What this skill does

This skill runs a systematic pre-launch quality assurance review of a Google Ads account before any campaign goes live. It checks every layer — from conversion tracking and campaign settings through keyword health, ad copy, extensions, Quality Score signals, PMAX readiness, and change log setup — producing a documented, signed-off QA record.

**When to use this skill:**
- Final check before a new client's first campaigns go live
- Before adding a new campaign type to an existing account (e.g., launching PMAX for the first time)
- After a major account restructure or rebuild
- Before reactivating paused campaigns that have been idle for 30+ days

**Do not skip pre-launch QA.** Every item on this checklist represents a real failure mode that has caused wasted budget, poor campaign performance, or client trust issues in active accounts.

Output options:
- **QA Report (DOCX)** — full written QA record with pass/fail status, findings, and sign-off, best for internal records or client-facing review
- **Structured checklist** — plain text version for Notion or Slack
- **Something else** — confirm with user

---

## Phase 1 — Scope Confirmation

Before starting the QA, confirm what's being reviewed.

**Ask the following:**

1. **Campaign types launching:** RSA only, RSA + PMAX, or something else?
2. **Client vertical:** eCommerce or lead gen? (Affects which checklist items apply)
3. **New or existing account:** New accounts have a longer QA checklist; existing accounts may have some settings already verified.
4. **Any known issues flagged during build:** Were there any items left unresolved during campaign build that need follow-up?
5. **Target launch date:** Is there a specific date or time the campaigns need to go live? (Important for scheduling and ad approval timing)

---

## Phase 2 — Conversion Tracking Verification

This is the highest-stakes item in the entire QA. Do not pass this section with any doubt.

### 2A. Google Ads Conversions tab check

In Google Ads → Tools → Conversions:

- [ ] At least one conversion action exists and shows status: **"Recording conversions"**
- [ ] Conversion action category is correct: Lead (lead gen) or Purchase (eCommerce)
- [ ] Count setting is correct: One per click (lead gen) or Every (eCommerce)
- [ ] Conversion value is set: fixed value or dynamic (eCommerce must pass dynamic transaction value)
- [ ] Last conversion recorded within the past 7 days (confirms the tag is active on the live site)

**If any item fails:** Do not proceed with launch. Resolve the tracking issue first. Refer to `references/conversion-tracking-verification.md` for the diagnosis and repair process.

### 2B. GA4 linkage check

In Google Ads → Tools → Linked Accounts → Google Analytics:
- [ ] GA4 property is linked, status: **Active**
- [ ] GA4 conversions are importing into Google Ads (verify in the Conversions tab — GA4 source visible)
- [ ] **Events actually arriving in GA4** — the "Active" link status only confirms the connection exists. To confirm events are flowing, either:
  - **Composio path (preferred if connected):** pull GA4 conversion events count for the past 24h via Composio (see the live MCP connectors) — should show test conversions from Step 2D. Use case: *"pull GA4 conversion event count for property {id}, last 24 hours"*.
  - **Manual path:** open GA4 → Reports → Realtime → look for the conversion event firing as you submit the test in Step 2D. A linked-but-empty GA4 property is one of the most common silent-fail patterns at launch.

### 2C. Live tag verification

Using Google Tag Assistant on Challenger's live website:
- [ ] Google Tag (AW-XXXXXXXXX) fires on **all pages** — no errors
- [ ] Conversion Tracking tag fires on the correct trigger only (Thank You page, purchase confirmation, or form submit event)
- [ ] No tag errors or warnings

### 2D. End-to-end test

Complete a test conversion (submit the form, or place a test order if a sandbox environment is available):
- [ ] Conversion appears in Google Ads → Conversions → "Conversions (last 30 days)" column within 24 hours

**Pass standard:** All four items (2A–2D) must pass before launch is approved.

---

## Phase 3 — Campaign Settings Audit

Run through every active campaign and check these settings:

### 3A. Network settings

- [ ] Campaign type set to **Search** (not Search + Display)
- [ ] **Display Network: OFF** — this is the most common setup error. Search campaigns with Display Network on mix intent-based and impression-based traffic, which distorts performance data and typically wastes budget
- [ ] **Search Partners: OFF** for new campaigns — turn on after 30 days once there's baseline data to evaluate quality

### 3B. Location targeting

- [ ] Target geography is correct (matches client brief)
- [ ] Location targeting option set to **"Presence"** — users physically in the target location
- [ ] NOT set to **"Presence or Interest"** — this would show ads to users outside the target area who are interested in it (e.g., someone in New York searching for "Minneapolis HVAC" would see a Minneapolis HVAC ad if Presence or Interest is enabled)

### 3C. Ad schedule

- [ ] For lead gen clients with specific business hours: ad schedule is set to match operating hours (no point generating leads at 2am if no one answers)
- [ ] For eCommerce clients: no ad schedule restriction (purchases happen 24/7)
- [ ] If an ad schedule was requested by Challenger, verify it's applied to the correct campaigns

### 3D. Budget

- [ ] Daily budget is set at campaign level
- [ ] Total daily budget across all campaigns × 30.4 = confirmed monthly budget (no over- or under-allocation)
- [ ] Budget is not shared across campaigns via a shared budget (unless intentional and documented)

### 3E. Bid strategy

| Campaign type | Expected bid strategy at launch | Pass / Fail |
|--------------|-------------------------------|-------------|
| New account (any campaign) | Maximize Clicks | |
| Existing account, <30 conversions | Maximize Clicks | |
| Existing account, 30+ conversions | Maximize Conversions | |
| Existing account, stable CPA, 60+ days | tCPA (only if set appropriately — ~20% above actual CPA) | |
| PMAX | Maximize Conversions (or Maximize Conversion Value for eCommerce) | |

- [ ] Bid strategy matches the account's conversion history and maturity stage
- [ ] If tCPA is used: the target is within 20% of the actual CPA from the last 90 days — not aspirational, not arbitrary

---

## Phase 4 — Campaign Structure Check

### 4A. Branded vs. non-branded separation

- [ ] Branded keywords are in a **dedicated branded campaign**, not mixed with non-branded campaigns
- [ ] All brand name variations (including misspellings) are added as **negatives in every non-branded campaign**
- [ ] Non-branded keywords are added as **negatives in the branded campaign**

This is a structural requirement. Failure here makes every performance metric unreliable.

### 4B. Ad group health

For every active ad group:
- [ ] Minimum **2 RSAs** per ad group — never launch with a single ad
- [ ] Maximum **3 active RSAs** per ad group — more dilutes testing signal
- [ ] Maximum **15–20 keywords** per ad group — beyond this, ad relevance drops
- [ ] Headline 1 is **pinned** to the keyword-specific headline — not rotating freely

### 4C. Keyword check

- [ ] All keywords from the approved keyword list are imported into the correct ad groups
- [ ] Match types are correctly assigned (exact match for new accounts)
- [ ] Account-level negative keyword list is applied
- [ ] Campaign-level negatives applied where specified (branded negatives in non-branded campaigns)
- [ ] No keywords in status: "Rarely shown due to low Quality Score" on a critical ad group before launch — these need fixing before going live

---

## Phase 5 — Extensions Completeness Check

At account level:
- [ ] Minimum 4 sitelinks — each linking to a specific, relevant page (not the homepage)
- [ ] Minimum 6 callouts — differentiated benefit statements (not generic filler)
- [ ] Brand logo uploaded
- [ ] Minimum 4 images — real brand photography preferred over stock
- [ ] Structured snippets — at least one header with relevant list (Services, Products, or Locations)

For eCommerce:
- [ ] Google Merchant Center product feed linked and status: **Approved** (no disapproved products)

**Note on approval timing:** New extensions and ads require Google review, which typically takes 24–48 hours. Ensure extensions are submitted at least 48 hours before the planned launch date to avoid delays.

---

## Phase 6 — Quality Score & Landing Page Alignment

Quality Score is Google's real-time assessment of how relevant your keyword, ad, and landing page are to the searcher. Poor Quality Score = higher CPC and lower ad position. This check is preventive — fix issues before launch rather than discovering them after spending budget.

### 6A. Ad relevance check

For the top-priority ad group in each campaign:
- [ ] Does the RSA Headline 1 (pinned) contain the **exact target keyword** or a close variant?
- [ ] Google Ad Preview: does the ad visually stand out from competitor ads on the same SERP? Does it lead with a specific benefit or differentiator?
- [ ] Ad strength rating: Good or Excellent? (Poor = needs rewriting before launch)

**Why ad relevance matters:** "Above average" ad relevance is one of three Quality Score components. Accounts with "Above average" ad relevance and landing page experience show 750% better CVR and 36% lower CPC on average.

### 6B. Landing page alignment check

For each ad group, check the final URL destination:

- [ ] The landing page **headline or H1** mirrors the ad's primary keyword and value proposition — if the ad says "Emergency Plumber Minneapolis — Available 24/7" the landing page should lead with a similar message, not a generic brand homepage
- [ ] The landing page loads quickly on mobile (Google's primary indexing is mobile-first — slow mobile pages = "Below average" landing page experience)
- [ ] The landing page has a clear, prominent CTA that matches the ad's CTA (e.g., if the ad says "Get a Free Quote", the landing page should have a visible quote form, not a "Contact Us" buried at the bottom)
- [ ] The landing page URL is functioning — click through the final URL and confirm the page loads without errors

### 6C. Quality Score flags

If Keyword Planner Quality Score estimates or early indicators show any component rated "Below average":

| Component | Common fix |
|-----------|-----------|
| Expected CTR | Rewrite ad copy to be more benefit-forward and specific; compare with competitor ads in the same SERP |
| Ad relevance | Ensure Headline 1 contains the exact keyword; verify ad group keywords are tightly themed |
| Landing page experience | Match landing page headline to ad copy; improve page load speed; add a clear, visible CTA |

Do not launch an ad group where all three components are "Below average" — it will spend budget at a severe CPC penalty and rank poorly against competitors.

---

## Phase 7 — PMAX Pre-Launch Check (if applicable)

Skip this phase if no PMAX campaign is included in the launch.

- [ ] Eligibility re-confirmed: 30+ conversions/month, budget ≥ $1k, existing account, GMC approved (eCommerce)
- [ ] All three audience signals present:
  - [ ] Customer Match list uploaded and status: Active
  - [ ] Website visitors audience ≥ 100 users
  - [ ] Custom intent audience created
- [ ] Search themes populated: minimum 10, up to 50
- [ ] Campaign-level negatives applied: account-level list + brand name variations + competitor names
- [ ] Asset groups: each has all required assets (images, logo, video, headlines, descriptions, final URL)
- [ ] Video assets: real video provided — **no auto-generated video**
- [ ] Each asset group final URL is live and loading correctly
- [ ] GMC product feed status: Approved with no disapproved products (eCommerce)
- [ ] PMAX budget is set separately from RSA campaigns

---

## Phase 8 — Auto-Applied Recommendations Check

- [ ] Google Ads → Recommendations → Auto-apply: **ALL toggles are OFF**

This must be checked immediately before launch — Google sometimes re-enables auto-apply settings after account changes. A single enabled toggle can silently add broad match keywords or change bids.

---

## Phase 9 — Change Log Verification

- [ ] Change Log tab exists in the Google Ads Workbook
- [ ] All build actions are logged: account setup, extension additions, campaign launches, keyword import, PMAX setup
- [ ] Each log entry includes: date, what changed, campaign/ad group, who made the change, and why

If the change log is missing or incomplete: do not launch until it's populated. An undocumented launch creates an undiagnosable baseline.

---

## Phase 10 — Final Sign-Off

Once all QA items pass:

1. Document QA completion in the change log: "Pre-launch QA completed — all items passed. Ready for go-live. [AM Name], [Date]"
2. Set a reminder to check the account 24 hours after launch for:
   - Are campaigns showing? (Check Impressions — if zero after 24 hours, investigate)
   - Is conversion tracking recording? (Check Conversions tab — at least one test conversion should appear)
   - Are any ads disapproved by Google? (Check Ads tab for status)
3. Deliver the QA report in the agreed format

**If any item fails QA:** Do not launch the affected campaigns. Document what failed, what needs to be fixed, and who is responsible. Launch is blocked until all Tier 1 items pass.

---

## Phase 11 — Synthesis Brief

Before building the deliverable, write a brief summary for orchestrator handoff.

**Pre-Launch QA Key Findings**
Extract and summarize:
- Pass/fail on each checklist category (conversion tracking status: Recording/Broken/Missing; campaign settings locked down; structure validation; extensions deployed and Google approval timing)
- Any blockers to launch (failed conversion tracking is a hard block; PMAX with missing video assets; Quality Score "Below average" on critical ad groups; auto-apply re-enabled)
- Critical follow-ups (24-hour post-launch validation checklist; conversion tracking persistence confirmation; impression/click pacing monitoring)

**Priority for downstream skills:** google-ads-reporting should verify on the first post-launch check (24 hours): conversion tracking is still "Recording conversions"; impressions and clicks are flowing at expected pacing; no ads were disapproved by Google; bid strategy is in learning phase as expected. Flag any anomalies immediately for investigation.

*If running standalone, share this with the operator before launch approval.*

---

## Phase 12 — Confirm Output Format + Branding

Before building the deliverable, ask two questions:

> "QA complete. What format would you like the output in?
>
> 1. **QA Report (DOCX)** — Full written QA record with pass/fail status for every item, findings, and launch sign-off. Best for internal records or client-facing accountability.
> 2. **Structured checklist** — Plain text version with pass/fail marks. Best for Notion or Slack.
> 3. **Something else** — Just tell me."

Wait for the answer. Then ask:

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colors, fonts, and layout rules before building.

Build based on chosen format:
- **QA Report** → invoke the docx skill; apply or client branding
- **Structured checklist** → output as plain text or Markdown; no skill needed

---

## Error Handling

**Conversion tracking fails during QA:** This is a hard block — do not launch any campaigns. Refer to `references/conversion-tracking-verification.md` for the diagnosis workflow. Escalate to a tracking specialist if GTM debugging doesn't resolve within 2 hours.

**Ads pending Google review at launch time:** New ads typically take 24–48 hours to be reviewed. If campaigns go live before ads are approved, the campaigns will show limited or no traffic. Plan: submit all ads at least 48 hours before the planned go-live date. If ads are still pending at launch time, launch anyway — they will begin serving once approved.

**PMAX asset group incomplete:** Do not launch PMAX with an incomplete asset group (missing images, no video, fewer than 3 headlines). A PMAX campaign with poor or missing assets will perform significantly worse than one with complete creative. Better to delay PMAX by a week and launch it properly than launch a low-quality version.

**One campaign fails QA but others pass:** The campaigns that pass can launch on schedule. Clearly document which campaign is blocked and why. Set a specific remediation date. Do not leave failed items open-ended.

**Auto-applied recommendations were re-enabled after build:** Turn them all off immediately and log the change. Review the Recommendations tab to check if any auto-applied changes were made between build and QA — if so, review and reverse any changes that weren't intentional.

---

## QA Gate

This skill's output IS the QA gate. Before delivering the final report:

- [ ] Every item in Phases 2–9 has a documented Pass or Fail status
- [ ] Any failed item has a documented remediation plan and responsible AM
- [ ] No campaigns are set live until all Tier 1 items pass (Phases 2, 3, 4A)
- [ ] Change log includes QA completion entry
- [ ] Post-launch 24-hour check reminder is scheduled

---

## References

Read these files when the relevant phase is reached:

- **[Conversion Tracking Verification & Repair](references/conversion-tracking-verification.md)** — Read during Phase 2 if any tracking item fails. Covers the full Google Tag Assistant diagnosis process, common failure modes (website redesign, URL changes, form plugin compatibility), GTM repair steps, and verification confirmation process.
- **[Quality Score Optimization Guide](references/quality-score-guide.md)** — Read during Phase 6 when any Quality Score component is "Below average." Covers how to improve Expected CTR through ad copy, how to improve Ad Relevance through keyword-to-headline matching, and how to improve Landing Page Experience through message match and page speed.
