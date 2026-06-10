---
name: google-ads-optimization
description: 'Weekly + monthly Google Ads ongoing optimization - search term pruning, negative keyword management, ad rotation, bid strategy graduation, device/placement bid adjustments, asset group optimization. MANDATORY TRIGGER: any mention of "optimize Google Ads", "Google Ads weekly optimization", "search term review", "Google Ads negative keywords", "RSA optimization", "PMAX optimization", "Google Ads weekly tasks". Do NOT use for: Account audit (use `google-ads-account-audit`). Reporting (use `google-ads-reporting`).'
---

> **Permission tier:** stage · **Tools/context:** assets/goals-targets.md, assets/team-roles.md, CONFIG.md


# Google Ads Optimization

## What this skill does

This skill guides an Ads AM through the recurring optimization work on live Google Ads accounts — the weekly and monthly tasks that keep RSA and PMAX campaigns healthy, spending efficiently, and improving over time.

Use this skill when:
- Running the weekly optimization check on a client's account
- Deciding whether to graduate a campaign to the next bid strategy
- Reviewing search terms and adding negatives
- Launching a new RSA or PMAX variant (monthly cadence)
- Investigating a sudden performance drop or spend anomaly

Output options:
- **Optimization summary (text)** — plain text list of changes made and rationale, for logging in the Google Ads Workbook Change Log
- **Optimization brief (DOCX)** — formatted document if Challenger or senior AM needs a written record
- **Change log entry only** — just the formatted text to paste into the Workbook Change Log tab

---

## Phase 1 — Context

Before touching the account, establish the optimization scope and what's already happened recently.

**Ask:**

1. **Client name and vertical:** Who is this, eCommerce or lead gen?
2. **Campaign types running:** RSA only, RSA + PMAX, or something else?
3. **Weekly or monthly check?** Weekly = search terms, search terms → negatives, spend review, bid adjustments. Monthly = add the ad variant launch and bid strategy graduation assessment.
4. **Last optimization date:** When was the account last optimized? Flag if more than 14 days have passed — stale accounts accumulate wasted spend quickly.
5. **Any open issues from last week?** Anything flagged in the previous Slack update that needs following up?
6. **Date range to use:** For weekly reviews, use the last 7 days. For monthly, use the last 30 days.

**Composio diagnostic note:** for the **performance collapse** scenario (ROAS or CPA suddenly degrading), tracking issues are always rule-out #1. If `google_analytics` is connected via Composio (see the live MCP connectors), pull GA4 conversion event counts for the affected campaign's landing pages over the past 7 days and compare to Google Ads-reported conversions. A widening gap usually means tracking broke — investigate before changing any campaign settings. Without Composio, manually compare in GA4 → Engagement → Conversions.

---

## Phase 2 — Search Term Review

Search term review is the highest-frequency, highest-impact ongoing task. Run this every week.

**Steps:**

1. In Google Ads → Keywords → Search Terms, filter to the last 7 days.
2. Sort by Spend descending.
3. Work through the list with this decision framework:

**Read `references/optimization-playbook.md` → Search Term Decision Framework** for the full criteria and edge cases.

**Quick decision rules:**

| Search term type | Action |
|-----------------|--------|
| High spend, zero conversions (>7 days, >$30 spend) | Add as negative — exact match |
| Irrelevant to the business entirely | Add as negative — exact match |
| Relevant but wrong intent (e.g., "DIY" on a professional services account) | Add as negative — phrase match |
| Highly relevant, multiple conversions | Consider adding as a positive keyword |
| Branded term showing in non-branded campaign | Add as negative — exact match in non-branded campaign |

4. **Minimum batch size:** Add at least 5 negatives per weekly review if the account has been running for 30+ days. Fewer than 5 means the search term report is either too narrow or hasn't been reviewed in a while.

5. **Log all additions** in the Google Ads Workbook → Change Log tab: Date, Campaign, Action, Keyword Added/Removed, Reason.

---

## Phase 3 — Keyword Performance Review

Monthly: review the full keyword list to pause underperformers and protect budget.

**Pull:** Keywords tab → last 30 days → sort by Cost descending.

**Pause criteria (any one of these):**

- Spent >3× the CPA target with zero conversions in 30 days
- Quality Score ≤ 3 AND Cost Per Click above the campaign average by >50%
- Impression Share <10% AND the keyword has been running for 60+ days (likely too competitive or too broad for the budget)

**Do not pause:**
- Brand keywords — ever, regardless of CPA (brand defense)
- Any keyword that converted at target CPA in the last 30 days (even if it's had slow patches before)
- Keywords running for fewer than 14 days (insufficient data)

**Adding new keywords:**

If the search term review reveals high-converting queries that aren't in the keyword list, add them as exact match or phrase match. Start with a low manual CPC bid and monitor for 14 days before letting Smart Bidding take over.

---

## Phase 4 — Ad Copy Rotation (Monthly)

The SOP cadence: launch one new RSA variant per month, max 3 active RSAs per ad group.

**Steps:**

1. Check the current RSA count per ad group. If any ad group has 3 active RSAs, pause the lowest performer before launching the new one.

2. **Identify which ad group needs a new variant:** Prioritize ad groups with the lowest CTR or highest CPA.

3. **RSA rotation rules:**
   - Never run more than 3 RSAs simultaneously in one ad group — signal gets diluted
   - Label each RSA with the variant letter and launch date (e.g., "RSA-B — Apr 2026") for easy tracking
   - A/B test should run for at least 30 days before drawing conclusions
   - Pin Headline 1 to the keyword-specific headline — do not leave it unpinned

4. **Write the new RSA:** Use the same headline and description formulas from the `google-ads-campaign-build` skill for RSA copywriting. Reference the highest-converting search terms from Phase 2 as inspiration for new headline angles.

**Read `references/optimization-playbook.md` → RSA Rotation Cadence** for the full launch checklist and copy formula reference.

---

## Phase 5 — PMAX Optimization (Monthly, if running)

PMAX optimization follows a distinct cadence from RSA. Read this section only if PMAX is active in the account.

**Read `references/optimization-playbook.md` → PMAX Optimization Protocol** for the full month-by-month guidance.

**Monthly PMAX checklist:**

- [ ] **Asset performance:** In the PMAX campaign → Asset Groups → View Details → check asset performance ratings. Remove any asset rated "Low" that has had 30+ days of data. Add a replacement asset before removing the low-performer.
- [ ] **Asset group expansion:** If a single asset group has been live for 60+ days and is performing at or above target, consider adding a second asset group targeting a different product category, audience segment, or seasonal theme. Max 3 asset groups per PMAX campaign.
- [ ] **Search themes:** Review the current search themes list (up to 50 allowed). Add themes based on high-converting search terms from Phase 2. Remove themes that have generated zero conversions in 60+ days.
- [ ] **Negative keywords:** Confirm campaign-level negatives are still accurate. Add any new negatives identified in Phase 2 (especially branded terms — make sure they're excluded from PMAX if there's a separate branded RSA campaign).
- [ ] **Audience signals:** Are Customer Match lists still current? If Challenger has added new purchasers to their CRM in the last 30 days, update the Customer Match audience.
- [ ] **ROAS / CPA target:** Is PMAX's Target ROAS or tCPA still aligned with the current account performance? Compare last 30 days actual vs target. If actual ROAS is consistently 30%+ above the PMAX target, tighten the target upward to concentrate spend on higher-value conversions.

---

## Phase 6 — Bid Strategy Graduation

Assess monthly whether any campaign is ready to move up the bid strategy ladder.

**Bid strategy ladder:**

| Stage | Strategy | Graduation criteria |
|-------|----------|-------------------|
| New campaign | Maximize Clicks | Accumulate 30 conversions in any 30-day window |
| Learning phase | Maximize Conversions | Stable CPA over 30+ days AND 30+ monthly conversions |
| Mature campaign | Target CPA | Set at last-30-day actual CPA; reduce 5–10% every 2 weeks if stable |
| eCommerce PMAX | Maximize Conv. Value | 30 conversions in 30 days |
| eCommerce mature | Target ROAS | Set slightly below actual ROAS; tighten every 2–4 weeks if holding |

**Graduation rules:**
- Only graduate **one campaign at a time** — graduating multiple campaigns simultaneously makes it impossible to attribute performance changes
- After graduation, **do not change anything else** in the account for 14 days — let the algorithm re-learn without interference
- Log the graduation in the Change Log with the date, old strategy, and new strategy
- Alert in the Slack update the week of graduation — clients need to know why there may be short-term performance volatility

**Demotion rule:**
If a campaign was recently graduated to tCPA or tROAS and is now severely underspending (spending <50% of its budget) after 14 days of learning, the target is set too aggressively. Move the target to the actual 30-day average and allow another 14 days. Do not demote the bid strategy — adjust the target first.

---

## Phase 7 — Device & Placement Review (Monthly)

Quick monthly check — catches hidden budget drains.

**Device review:**
In Google Ads → Campaigns → Segment → Device:
- Which device has the worst CPA or lowest ROAS?
- If a device (usually Tablet or TV Screens) has generated >10 conversions at significantly above-target CPA, add a negative bid modifier (–30% is a starting point, –100% excludes the device entirely)
- Never add a negative modifier to Mobile without a strong reason — mobile traffic is dominant for most clients

**Placement review (Display / PMAX):**
In Google Ads → Campaigns → select PMAX → Where Ads Showed:
- Review YouTube placements and app placements
- Any placement category with significant spend and zero conversions after 30 days? Add a placement exclusion
- Children's apps are a common waste in PMAX — add "Mobile App Categories → Games for Kids / Apps for Kids" as exclusions if they appear

---

## Phase 8 — Synthesis Brief

Before logging and delivering output, write a brief summary for orchestrator handoff.

**Optimization Key Findings**
Extract and summarize:
- Bid changes made (search term negatives added, quantity and rationale; keywords paused for poor performance; new high-converting keywords added as positives)
- Budget reallocations (campaigns throttling and needing budget increase; campaigns underspending and needing strategy adjustment; spend redistribution across active performers)
- Performance deltas (CPA/ROAS before and after changes; bid strategy graduation progress toward next threshold; conversion velocity trending up/down week-over-week)

**Priority for downstream skills:** google-ads-reporting should highlight performance volatility if a bid strategy change occurred this week (algorithm learning phase is expected to show 1–2 weeks of flux); feature newly optimized high-performers; call out which accounts are approaching graduation readiness so reporting can set client expectations for the next phase.

*If running standalone, share this with the operator before building the optimization report.*

---

## Phase 9 — Log Changes & Output

Every optimization session must be logged. No changes without a Change Log entry.

**Change Log format (for Google Ads Workbook → Change Log tab):**

```
Date: [YYYY-MM-DD]
Campaign: [Campaign name]
Change type: [Search term negative / Keyword paused / RSA variant launched / Bid strategy change / Device modifier / PMAX asset added-removed / Search theme added-removed]
Specific change: [Exact keyword, asset name, or strategy name]
Reason: [1 sentence — why this change was made, what data drove it]
```

**Before building the output, confirm format:**

> "What would you like as the output for this optimization session?
>
> 1. **Change log entry** — formatted text to paste into the Google Ads Workbook
> 2. **Optimization summary (text)** — brief plain-text summary of all changes made, suitable for Notion or internal Slack
> 3. **Optimization brief (DOCX)** — full written record with context, suitable for senior AM review or client transparency
> 4. **Something else** — just tell me"

If DOCX is selected:
> "branding, or client-specific? If Challenger, I'll pull from the brand file."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` before building.

---

## Error Handling

**Performance spike or collapse (CPA 2× target or ROAS 50% below target):** Before making any changes, diagnose the cause. Read `references/optimization-playbook.md` → Performance Collapse Diagnosis for the step-by-step investigation flow. Do not make blind optimizations when performance is off — the root cause must be identified first.

**Account inactive for >14 days (no recent optimization logged):** Flag this before anything else. Stale accounts accumulate search term waste and may have had auto-applied recommendations silently enabled. Start with the Phase 4 audit checklist in `google-ads-account-audit` to verify account-level settings before running the optimization routine.

**Bid strategy in learning phase:** If any campaign's Status column shows "Learning" (visible in the Campaign Status column), do not make any bid, budget, or targeting changes to that campaign. Wait until the learning phase resolves (typically 7–14 days). Making changes during learning resets the clock and extends volatility. Log this in the Change Log as "No changes — in learning phase" so the record stays current.

**Google Ads Workbook not found / Change Log tab missing:** Do not skip logging. If the Workbook link isn't in Challenger's Rolling Agenda, ask the operator for it before proceeding. Unlogged changes are the root cause of most "we don't know what changed" investigations.

---

## QA Gate

Before delivering the output:

- [ ] Search terms reviewed for the last 7 days — at least 5 negatives added (if account is 30+ days old)
- [ ] Any keyword with >3× target CPA and zero conversions in 30 days — paused or flagged
- [ ] No more than 3 RSAs active per ad group
- [ ] PMAX asset ratings checked — "Low" assets flagged or removed
- [ ] Bid strategy graduation assessed — conversion count vs threshold noted
- [ ] Device and placement review done (monthly only)
- [ ] Every change logged in the Change Log with date, campaign, change type, and reason
- [ ] No changes made to campaigns in active learning phase

---

## References

Read these files when the relevant phase is reached:

- **[Optimization Playbook](references/optimization-playbook.md)** — Read during Phases 2, 4, 5, and for error handling. Contains: the full Search Term Decision Framework with edge cases, RSA rotation cadence and launch checklist, PMAX month-by-month optimization protocol, and the Performance Collapse Diagnosis flow.
