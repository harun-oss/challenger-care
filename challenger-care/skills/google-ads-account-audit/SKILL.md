---
name: google-ads-account-audit
description: 'Full diagnostic of a Google Ads account · conversion tracking, campaign performance, competitive landscape, strategic gaps. For account takeovers or stale-account reactivation. MANDATORY TRIGGER: any mention of "audit Google Ads account", "Google Ads health check", "diagnose Google Ads", "Google Ads account review", "review Google Ads", "take over Google account". Do NOT use for: Building new campaigns (use `google-ads-campaign-build`). Pre-launch QA (use `google-ads-prelaunch-qa`).'
---

> **Permission tier:** generate · **Tools/context:** assets/goals-targets.md, assets/unit-economics.md, assets/team-roles.md, CONFIG.md


# Google Ads Account Audit

## What this skill does

This skill walks an Ads AM through a complete diagnostic of a Google Ads account before any campaign work begins. It covers conversion tracking health, existing campaign performance, competitive positioning, and strategic gaps — producing a clear picture of what's working, what's broken, and what to prioritize.

Use this skill when:
- Taking over an existing client account
- Starting a new client who has a pre-existing Google Ads account
- Diagnosing unexplained performance drops
- Running a quarterly health check on an active account

Output options:
- **Audit Report (DOCX)** — full written audit covering all dimensions, best for client-facing review or internal brief
- **Structured text** — plain text summary for Notion or Slack sharing
- **Something else** — confirm with user

---

## Phase 1 — Context & Scope

Before opening the account, establish the audit scope and what the operator already knows.

**Ask the following:**

1. **Client name and vertical:** Who is this, and are they eCommerce or lead gen?
2. **Account history:** How long has this account been running? Roughly what's the monthly spend?
3. **Why the audit:** New account takeover, performance drop, quarterly check, or something else?
4. **Known issues:** Are there any specific problems Challenger or previous AM flagged?
5. **Success metrics:** What does success look like for this client — leads, purchases, ROAS, CPA target?
6. **Access confirmed:** Is the operator already in the account, or is access still being granted?

**Blocker rule:** If access to Google Ads, GA4, or GTM is not yet confirmed, stop here. Do not proceed until access is granted. Log the outstanding request with date in Challenger's Google Ads Workbook.

---

## Phase 2 — Conversion Tracking Audit

Conversion tracking is the highest-priority item in every audit. Everything else depends on it.

**Step 1 — Check Google Ads Conversions tab**

In Google Ads → Tools → Conversions:
- Are any conversion actions set up?
- What is the tracking status of each? Look for: "Recording conversions", "No recent conversions", "Tag inactive", or "Unverified"
- When did each conversion action last record a conversion? A gap of more than 14 days on an active account is a red flag.
- Are conversion actions set to the correct "Count" setting? (Lead gen: One per click. eCommerce: Every.)
- Is conversion value being passed correctly? (eCommerce should pass dynamic transaction value, not a fixed amount)

**Step 2 — Check GA4 linkage**

In Google Ads → Tools → Linked Accounts → Google Analytics:
- Is GA4 linked and showing Status: Active?
- Are GA4 conversions being imported into Google Ads?
- Cross-reference: do GA4 goal completions roughly match Google Ads conversion counts? Large discrepancies signal tag or attribution issues.

**Optional Composio verification (if `google_analytics` is connected):** the "GA4 link Active" status in Google Ads only confirms the link exists — not that events are actually flowing. To verify the real picture, pull GA4 conversion event counts for the past 30 days directly via Composio (see the live MCP connectors) and compare to the Google Ads-reported number. A material gap (>20%) means events are not making it from GA4 to Google Ads — investigate the import config before any optimisation. If Composio is not connected, fall back to manually opening GA4 → Reports → Engagement → Conversions and comparing.

**Step 3 — GTM tag verification**

Using Google Tag Assistant (Chrome extension) on Challenger's live site:
- Is the Google Tag (AW-XXXXXXXXX) firing on all pages?
- Is the Conversion Tracking tag firing on the correct trigger (Thank You page, form submit, purchase confirmation)?
- Are there any tag errors or warnings?

**Step 4 — End-to-end test (if tracking is in doubt)**

Complete the conversion action manually (submit a test lead form, or use a test purchase if sandbox is available). Check whether the conversion appears in Google Ads → Conversions within 24 hours.

**If tracking is broken:** Read `references/conversion-tracking-diagnosis.md` for the full GTM repair walkthrough. Do not proceed to Phase 3 until tracking is confirmed working — every subsequent audit finding is unreliable without valid conversion data.

**Tracking audit summary to document:**

| Conversion Action | Status | Last Recorded | Count Setting | Value Passing | Notes |
|------------------|--------|--------------|---------------|---------------|-------|
| [Name] | [Status] | [Date] | [One/Every] | [Yes/No/Dynamic] | |

---

## Phase 3 — Existing Campaign Performance Review

Review every active campaign systematically. Work through these dimensions:

### 3A. Campaign and ad group structure

- What campaigns exist? List them: Branded, Non-Branded, Competitor, PMAX, Display, etc.
- Are branded and non-branded keywords in **separate campaigns**? If not, flag immediately — this is a structural issue that distorts all performance data.
- Are branded keywords added as negatives in non-branded campaigns?
- How many ad groups per campaign? More than 20 in a single campaign often signals poor structure.
- Are ad group themes tight (same headline can serve all keywords) or mixed (multiple unrelated intents)?

### 3B. Keyword health

- Pull the keyword report filtered to the last 90 days.
- Flag: any keywords with **significant spend and zero conversions** — likely wasted budget.
- Flag: any keywords with Quality Score ≤ 4 — these are dragging down ad position and driving up CPC.
- Flag: any keywords with impression share below 30% — either budget-constrained or Quality Score issue.
- Review the **Search Terms report** — are there irrelevant queries triggering ads? These should become negatives.
- Is the match type strategy appropriate for the account's maturity? New accounts should be exact match; broad match without strong negatives on any account is a risk.

### 3C. Ad copy performance

- Pull the ads report for the last 90 days.
- RSA ad strength: are any ads rated "Poor"? These need rewriting.
- CTR by ad: any RSAs with CTR below 1% for Search? Low CTR usually means the ad copy doesn't match the keyword intent.
- Are there at least 2 RSAs per ad group? Single-ad groups can't A/B test.
- Are there more than 3 active RSAs per ad group? This dilutes testing signal.
- Is Headline 1 pinned to the keyword-specific headline? Unpinned Headline 1 lets Google rotate in generic copy, hurting ad relevance.

### 3D. Bid strategy assessment

Review the current bid strategy for each campaign:

| Bid Strategy | Appropriate if... | Red flag if... |
|-------------|------------------|----------------|
| Maximize Clicks | Account is new, fewer than 30 conversions | Account has 6+ months and 30+ monthly conversions — should have graduated |
| Maximize Conversions | 30+ conversions recorded, stable volume | Conversion tracking was recently broken — machine learning is poisoned by bad data |
| Target CPA (tCPA) | Stable CPA over 60+ days, 30+ monthly conversions | Set too aggressively (way below actual CPA) — causes underspend or poor targeting |
| Target ROAS | eCommerce with strong revenue data | ROAS target too high — causes underspend; too low — overspending on low-value orders |

- Is the tCPA or tROAS target achievable? Compare target vs actual CPA/ROAS over the last 90 days.

### 3E. Budget utilization

- Is each campaign spending its full daily budget, or is it throttling?
- Campaigns consistently hitting budget cap = either increase budget or reduce bids; they're leaving clicks on the table.
- Campaigns consistently underspending = likely tCPA/tROAS set too aggressively, or Quality Score issues limiting impression share.

### 3F. PMAX (if running)

- Is PMAX eligible for this account? (30+ monthly conversions, budget ≥ $1k/month, existing data)
- Are audience signals present? (Customer Match + website visitors + custom intent)
- Are search themes populated? (Up to 50, 2025 update)
- Are campaign-level negatives applied? (Up to 10,000, 2025 update) — especially: are branded terms excluded so branded traffic stays in the branded RSA campaign?
- Is there at least one approved video asset per asset group, or is Google auto-generating video?
- Is PMAX cannibalizing RSA impression share? (Check RSA impression share trends since PMAX was added)

---

## Phase 4 — Account-Level Settings Audit

Check these settings which apply across all campaigns:

- **Auto-applied recommendations:** Are any enabled? In Recommendations → Auto-apply — all toggles should be OFF. controls all changes; auto-apply can silently undo optimization work.
- **Extensions / Assets:** Are the minimum required extensions active at account level?
  - 4 sitelinks (not just any 4 — are they linking to meaningful, specific pages?)
  - 6 callouts (are they differentiated benefit statements, or generic filler?)
  - Brand logo
  - Images (4 minimum — are they real brand imagery or stock photos?)
  - Structured snippets
- **Location targeting settings:** Are campaigns set to "Presence" (people in the target location) not "Presence or Interest" (people interested in the location)? The latter shows ads to users outside the target geography.
- **Network settings:** Are Search campaigns set to "Search Network only"? Any campaign with Display Network enabled alongside Search is mixing performance data and usually wastes budget.
- **Search partners:** On or off? For established accounts with positive data, search partners may be worthwhile. For accounts with limited data, turn off until there's a baseline.

---

## Phase 5 — Competitive Audit

Understand the competitive environment before drawing conclusions about account performance.

**Step 1 — Google Ads Transparency Center**

Go to `adstransparency.google.com` and search for each of Challenger's top 3–5 competitors:
- What headlines and copy angles are they running? Note: emotional appeals, price points, offers, trust signals.
- How many ads are they running? Frequency suggests what's working.
- Any seasonal or promotional patterns?

**Step 2 — Auction Insights report**

In Google Ads → Campaigns → Auction Insights (run for the last 90 days):
- Who is showing up in the same auctions as this client?
- What is this client's Impression Share vs competitors?
- Who has a higher Outranking Share — meaning they're beating this client's position consistently?

**Step 3 — SEMrush competitive gap**

- Pull Challenger's domain and compare keyword overlap with the top 2–3 competitors.
- Are there high-volume, high-intent keywords where competitors rank but this client doesn't advertise?
- Note any offer angles in competitor ads that seem distinctive (money-back guarantees, free trials, specific turnaround times).

**Step 4 — Manual SERP review**

Google Challenger's top 5 target keywords:
- Is Challenger's ad appearing? At what position?
- How does their ad copy compare visually to competitors — is it benefit-forward, does it stand out?
- Are competitors using extensions Challenger isn't (promotions, prices, callouts)?

**Step 5 — Organic context (optional, via Composio)**

If `google_search_console` is connected via Composio (see the live MCP connectors), pull two things to layer organic visibility into the competitive picture:

- *"pull GSC clicks, impressions, position by query for the past 90 days, segmented brand vs non-brand"* — answers: does Challenger already rank organically for the same keywords they're bidding on? If yes, paid is likely cannibalizing organic clicks and the true paid contribution is overstated.
- *"pull GSC top URLs by clicks for the past 90 days"* — answers: which of Challenger's pages already have organic momentum? Those are the strongest landing-page candidates for the paid campaigns.

If Composio is not connected, this is a manual export from GSC → Performance → Queries (filter to last 90 days, segment by brand vs non-brand via a query contains filter). Skip if no GSC access at all.

Document findings in a competitive matrix in the Google Ads Workbook.

---

## Phase 6 — Strategic Gap Summary

After completing the audit, synthesize findings into a prioritized gap list.

Organize findings into three tiers:

**Tier 1 — Fix before anything else (blockers):**
Issues that make any other optimization meaningless. Conversion tracking broken, branded/non-branded mixed, auto-apply enabled, wrong network settings.

**Tier 2 — Fix within first 30 days (high impact):**
Issues that are actively wasting budget or suppressing performance. Keywords with high spend and zero conversions, ad groups with no RSA variation, Quality Scores ≤ 4, tCPA set far below achievable CPA, PMAX without audience signals.

**Tier 3 — Optimize over 60–90 days (improvements):**
Structural improvements that compound over time. Ad copy testing, extension optimization, search terms → negative keywords, Search partners testing, bid strategy graduation (Maximize Clicks → Maximize Conversions).

Present the gap summary in the Google Ads Workbook (Audit tab) before taking any action. No changes should be made to the account until the operator and client agree on priorities.

---

## Phase 7 — Synthesis Brief

Before building the deliverable, write a brief summary for orchestrator handoff.

**Account Audit Key Findings**
Extract and summarize:
- Wasted spend percentage (high-spend, zero-conversion keywords; paused keywords; irrelevant search terms)
- Quality Score distribution (how many keywords at each QS level; any ≤ 4 dragging performance)
- Campaign structure gaps (branded/non-branded separation status; ad group theme coherence; keyword-to-ad relevance issues)
- Budget allocation issues (throttling campaigns; underspending campaigns; mismatch between budget and performance)

**Priority for downstream skills:** google-ads-keyword-research should focus on identifying high-intent keyword gaps that complement the existing structure gaps; google-ads-optimization should prioritize removing the wasted spend sources identified in the audit and fixing Quality Score issues before scaling budget.

*If running standalone, share this with the operator before the full deliverable.*

---

## Phase 8 — Confirm Output Format + Branding

Before building the deliverable, ask two questions:

> "Audit complete. What format would you like the output in?
>
> 1. **Audit Report (DOCX)** — Full written audit covering all dimensions: tracking health, campaign performance, competitive landscape, and prioritized recommendations. Best for client-facing review or internal brief.
> 2. **Structured text** — Plain text summary, best for Notion or Slack.
> 3. **Something else** — Just tell me."

Wait for the answer. Then ask:

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colors, fonts, and layout rules before building.

Build based on chosen format:
- **Audit Report** → invoke the docx skill; apply or client branding
- **Structured text** → output as plain text or Markdown; no skill needed

---

## Error Handling

**Access not yet granted:** Stop at Phase 1. Log the outstanding access request with the date. Revisit when access is confirmed — do not attempt a partial audit without full account access.

**Conversion tracking broken — GTM tags missing from new website:** Read `references/conversion-tracking-diagnosis.md` for the full repair walkthrough. This is the most common issue after a website redesign.

**No Auction Insights data:** Auction Insights requires the campaign to have been running long enough to accumulate impression data. If the account is very new or campaigns were recently paused, skip this step and note it in the audit.

**GA4 and Google Ads conversion counts diverge significantly:** This is usually a tag firing issue (Google Ads tag fires, GA4 tag doesn't, or vice versa), attribution window mismatch (Google Ads default 30-day click window vs GA4's 7-day), or a cross-device tracking gap. Document the discrepancy and flag for tracking specialist review before trusting either data source for optimization.

**Account has no historical data (new account):** Skip Phases 3 and 5 (campaign review and Auction Insights — there's nothing to review). Focus on Phase 2 (ensure tracking is installed correctly before launch) and Phase 4 (account-level settings). The output becomes a launch readiness check rather than a performance audit.

---

## QA Gate

Before delivering the audit output, verify:

- [ ] Conversion tracking status confirmed (Recording / Broken / Missing) and documented
- [ ] GA4 link verified
- [ ] All active campaigns reviewed and documented in the Workbook
- [ ] Branded and non-branded keyword separation checked
- [ ] Quality Score flags identified (any ≤ 4)
- [ ] Budget utilization checked (throttling vs underspending)
- [ ] Auto-applied recommendations status checked
- [ ] Competitive audit completed (Transparency Center + Auction Insights)
- [ ] Gap summary organized into Tier 1 / Tier 2 / Tier 3
- [ ] No changes made to the account during the audit phase

---

## References

Read these files when the relevant phase is reached:

- **[Conversion Tracking Diagnosis & GTM Repair](references/conversion-tracking-diagnosis.md)** — Read during Phase 2 whenever tracking shows any status other than "Recording conversions." Covers the full GTM diagnosis workflow, common failure modes (website redesign, URL changes, form plugin changes), and step-by-step repair instructions.
- **[Campaign Audit Framework](references/campaign-audit-framework.md)** — Read at the start of Phase 3 for the detailed criteria and benchmarks used to evaluate existing campaigns: Quality Score thresholds, CTR benchmarks by industry, wasted spend identification, and bid strategy assessment rules.
