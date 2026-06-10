---
name: google-ads-reporting
description: 'Weekly + monthly Google Ads performance reporting · markdown output (not PPTX). Spend, key metrics, bid strategy progression notes, narrative framing. MANDATORY TRIGGER: any mention of "Google Ads weekly update", "Google Ads monthly report", "Google Ads performance update", "weekly Google update", "monthly Google report", "Google Ads results". Do NOT use for: Account audit (use `google-ads-account-audit`). Optimization tasks (use `google-ads-optimization`).'
---

> **Permission tier:** generate · **Tools/context:** assets/goals-targets.md, assets/team-roles.md, CONFIG.md


# Google Ads Reporting

## What this skill does

This skill walks an Ads AM through the full Google Ads reporting workflow — from a quick weekly Slack update to a full monthly client-facing report. It covers RSA and PMAX campaigns, bid strategy status, and the narrative framing that explains performance in plain language.

Use this skill when:
- Writing the weekly Slack performance update for a Google Ads client
- Updating the eCommerce or Lead Gen Spend Tracker
- Producing the monthly Google Ads Insights deck or DOCX report
- Summarizing performance after a major campaign launch or bid strategy change

Output options:
- **Weekly Slack update** — formatted Slack message, ready to post to Challenger's internal channel
- **Spend Tracker update** — values to enter into the eCommerce or Lead Spend Tracker
- **Monthly report (DOCX or PPTX)** — full client-facing monthly insights report
- **All three** — complete reporting package for the month

---

## Phase 1 — Context

Before pulling any data, establish which reporting deliverable is needed and what period to cover.

**Ask:**

1. **Client name and vertical:** Who is this, and are they eCommerce or lead gen?
2. **Reporting period:** What week or month are we covering?
3. **What's needed:** Weekly Slack update only, Spend Tracker update only, full monthly report, or all three?
4. **CPA / ROAS target:** What is this client's agreed target? (Needed to frame performance as on-target / below / above)
5. **Key context:** Any external factors this week/month? (Seasonality, promo, budget change, new campaign launch, bid strategy change)

---

## Phase 2 — Weekly Slack Update

Pull from Google Ads → Campaigns → last 7 days. Cover all active campaigns.

**Data to pull (last 7 days vs prior 7 days):**

| Metric | This Week | Last Week | % Change |
|--------|-----------|-----------|----------|
| Spend | | | |
| Clicks | | | |
| Conversions | | | |
| CPA (Lead) or ROAS (eComm) | | | |
| Conv. Rate | | | |
| Impressions | | | |

**Read `references/reporting-templates.md` → Weekly Slack Update section** for the exact message format, emoji usage rules, and narrative framing guidance.

**Weekly Slack update structure:**

```
📊 *[Client Name] — Google Ads Weekly Update | [Date Range]*

*This Week:*
Spend: $X | Conversions: X | CPA: $X / ROAS: X.Xx

*vs Last Week:*
[One sentence: better / worse / flat, and the key reason]

*What's working:*
[1–2 specific observations — best-performing campaign, keyword, or ad]

*Watch list:*
[1 item to keep an eye on — a campaign approaching budget cap, a keyword with rising CPA, a stale ad group]

*Bid Strategy Status:*
[Current strategy + where client is in the progression, e.g. "Maximize Conversions — 22/30 conversions needed to graduate to tCPA"]

*Next 7 days:*
[1 planned action, e.g. "Launching new RSA variant for non-branded campaign", "Reviewing search terms for negative keyword additions"]
```

**Bid strategy graduation thresholds (for the Bid Strategy Status line):**

| Campaign type | Current → Next | Threshold | Notes |
|---------------|---------------|-----------|-------|
| RSA (new account) | Maximize Clicks → Maximize Conversions | 30 conversions in 30 days | Switch when threshold is stable, not one-off |
| RSA (scaled) | Maximize Conversions → tCPA | 30 conversions/month, stable CPA over 30 days | Set tCPA at last-30-day actual CPA, not the target |
| eCommerce PMAX | Maximize Conv. Value → Target ROAS | 30 conversions/month, stable ROAS | Set tROAS slightly below actual ROAS to avoid underspend |

**Narrative framing rules:**
- Always compare to the prior period — never report a number in isolation
- Use plain language: "We got 12 leads at $48 each" not "Conversion volume was 12 with a CPA of $48.23"
- If performance is below target, name the cause first, then the fix — don't just report the bad number
- If a bid strategy change happened this week, call it out explicitly — algorithm resets cause short-term volatility and Challenger needs to understand why

---

## Phase 3 — Spend Tracker Update

The Spend Tracker (eCommerce or Lead Gen version) tracks cumulative monthly spend and performance vs target. Update this at the end of each week.

**Values to record:**
- Week ending date
- Spend this week
- Cumulative month-to-date spend
- Conversions this week
- Cumulative month-to-date conversions
- CPA or ROAS this week
- Month-to-date CPA or ROAS
- Notes (any significant events: campaign launch, bid strategy change, budget change)

**Read `references/reporting-templates.md` → Spend Tracker section** for column-by-column entry instructions and how to flag budget pacing issues (underpacing or overpacing vs monthly budget).

**Budget pacing check:**
- Calculate: (MTD spend ÷ days elapsed) × days in month = projected month-end spend
- If projected spend is more than 10% above or below the monthly budget, flag immediately in the Tracker notes and in the Slack update
- Common cause of underpacing: tCPA set too low or quality score drop; common cause of overpacing: budget cap not set correctly or a new campaign launched mid-month

---

## Phase 4 — Monthly Report

The monthly Google Ads Insights report is a client-facing document delivered at or just before the monthly strategy call. It covers the full month's performance, what was learned, and what the plan is for the next 30 days.

**Read `references/reporting-templates.md` → Monthly Report section** for the slide-by-slide structure and narrative framing guidance.

**Monthly report structure (7 sections):**

**1. Performance Summary**
High-level scorecard: Spend, Clicks, Impressions, Conversions, CPA/ROAS, Conv. Rate — this month vs last month vs target. One headline sentence.

**2. Campaign Breakdown**
Performance by campaign type (Branded RSA, Non-Branded RSA, PMAX, Competitor if running). Include: spend split, conversions by campaign, CPA/ROAS by campaign. Flag any campaign that is significantly above or below account average.

**3. Keyword Highlights**
Top 5 converting keywords this month. Any keywords paused for poor performance. New keywords added. Search terms added as negatives.

**4. Ad Copy Performance**
RSA performance (ad strength ratings, CTR by ad). Any new variants launched. Winning vs underperforming copy.

**5. PMAX Insights (if running)**
Asset group performance. Top-performing assets (images, headlines, descriptions). Any listing groups paused. Search themes working.

**6. What Worked / What Didn't / What's Next**
The most important narrative section — always present even if performance is flat:
- *What worked:* Specific campaigns, keywords, or copy angles that drove results
- *What didn't:* One honest observation about what fell short and why
- *What's next:* 2–3 concrete actions for next month (not vague — specific: "Launch competitor campaign", "Graduate Non-Brand to tCPA once we hit 30 conversions", "Add PMAX asset group for seasonal collection")

**7. Bid Strategy Progression Update**
Where does each campaign currently sit on the bid strategy ladder?
- Maximize Clicks → Maximize Conversions → tCPA (lead gen)
- Maximize Conversion Value → Target ROAS (eCommerce)

Call out: how many conversions in the last 30 days? What's the next threshold? What's the timeline to the next graduation?

**8. Channel Context (optional, via Composio)**

If `google_analytics` and `google_search_console` are connected via Composio (see the live MCP connectors), add this section to the monthly report:

- **GA4 attribution sanity check:** pull GA4 sessions and revenue/conversions attributed to Paid Search for the same month. Compare to Google Ads-reported numbers. A material gap (>20% in either direction) warrants a one-line note in the report — usually a tracking config drift, sometimes legitimate cross-device attribution differences. Either way, surfacing the gap protects credibility with Challenger.
- **Organic context:** pull GSC clicks and impressions for the same period, segmented brand vs non-brand. Answers two questions clients ask in every monthly review: (a) is paid stimulating organic brand demand (brand impressions up MoM = healthy halo), and (b) is paid cannibalising organic clicks (paid up + non-brand organic down on the same queries = potential cannibalisation worth investigating).

Skip this section entirely if Composio is not connected, or if either app is not active for Challenger. The other 7 sections stand on their own — section 8 is enrichment, not a requirement.

---

## Phase 5 — Synthesis Brief

Before building the deliverable, write a brief summary for orchestrator handoff.

**Reporting Key Findings**
Extract and summarize:
- ROAS delta / CPA delta (performance this period vs last period vs target; percentage improvement/decline; attribution to specific campaigns or bid strategy changes)
- Impression share and budget pacing (which campaigns are hitting budget caps; which are underspending; projected month-end spend vs budget; any off-track signals)
- Top and bottom campaigns (best-performing campaigns by CPA/ROAS; lowest performers requiring intervention; keyword or ad copy wins worth featuring)
- Recommended next actions (3–5 concrete tactics for the next 7/30 days: specific campaigns to launch, optimization priorities, bid strategy graduations to prepare for)

**Priority for orchestrator:** Reporting is the final skill in the Google Ads chain — it synthesizes all findings from account-audit, keyword-research, campaign-build, optimization, and prelaunch-qa into an actionable narrative for client delivery. Close the loop by ensuring weekly updates are delivered to Challenger's Slack channel and monthly reports are presented at strategy calls.

*If running standalone, deliver weekly update to client channel and monthly report at strategy call.*

---

## Phase 6 — Confirm Output Format + Branding

Before building:

> "What format for the report?
>
> 1. **DOCX** — full written report, client-facing, professional formatting
> 2. **PPTX** — slide deck version, best for screen-share on monthly strategy call
> 3. **Slack only** — no formal report, just the weekly updates
> 4. **Something else** — just tell me"

Wait for answer. Then:

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colours, fonts, and layout rules before building.

Build based on chosen format:
- **DOCX** → invoke the docx skill; apply branding
- **PPTX** → invoke the pptx skill; apply branding
- **Slack only** → output formatted Slack message; no file needed

---

## Error Handling

**No conversion data for the period:** If a campaign recorded zero conversions in a 7-day window, do not extrapolate. Report it accurately: "Zero conversions this week. This is [expected due to low volume / unexpected — investigating]." Then check: is the conversion tracking still healthy? Did a tag break?

**Spend higher than monthly budget:** First verify — is a campaign set to a daily budget that would exceed the monthly target? If so, pause and fix immediately. Then report accurately in the Tracker with a note.

**Client asking why ROAS/CPA got worse after a bid strategy change:** This is expected and common. When Google Ads changes from Maximize Clicks to Maximize Conversions, or from Maximize Conversions to tCPA, the algorithm re-enters a learning period (typically 1–2 weeks). Performance volatility during this period is normal. Always pre-empt this in the Slack update when a bid strategy change happens.

**Month is missing data (new client mid-month):** Only report the weeks where campaigns were live. Label the report as "Partial Month" and note the campaign launch date. Do not try to extrapolate to a full month.

---

## QA Gate

Before sending the weekly update or delivering the monthly report:

- [ ] Compared this period to prior period (not just current numbers in isolation)
- [ ] Bid strategy status noted — current strategy + conversions toward next threshold
- [ ] Budget pacing calculated — projected month-end spend vs budget
- [ ] Conversion tracking health verified (still "Recording conversions"?)
- [ ] At least one specific "What's next" action named — not vague
- [ ] Format and branding confirmed before building document

---

## References

Read these files when the relevant phase is reached:

- **[Reporting Templates](references/reporting-templates.md)** — Read during Phases 2–4. Contains the full Weekly Slack Update template with formatting rules, Spend Tracker column-by-column entry guide, and monthly report slide structure with narrative framing examples.
