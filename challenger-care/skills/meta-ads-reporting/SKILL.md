---
name: meta-ads-reporting
description: Weekly + monthly Meta Ads performance reporting · key metrics, creative winners, what to test next. Markdown output (not PPTX). MANDATORY TRIGGER: any mention of "Meta Ads weekly report", "Meta monthly report", "Meta performance update", "weekly Meta performance", "monthly Meta report", "Meta Ads results". Do NOT use for: Scaling decisions. Creative testing decisions (use `meta-ads-creative-testing`). Account onboarding.
---

> **Permission tier:** generate · **Tools/context:** assets/goals-targets.md, assets/team-roles.md, CONFIG.md


# Meta Ads Reporting

**Owner:** the operator / AM
**Cadence:** Weekly Slack update + monthly Ad Insights report
**Prerequisite:** Access to Ads Manager, Spend Tracker template, and client's Slack channel

---

## Phase 1: Context

Ask the operator / AM one question at a time:
1. **Client name** — who is this report for?
2. **Report type** — weekly Slack update, spend tracker update, or monthly report?
3. **Reporting period** — what dates does this cover?
4. **Target CPA or ROAS** — what is the agreed performance target?
5. **Monthly budget** — total budgeted vs. actual spend this month so far?

---

## Phase 2: Reference Files

This skill uses reference materials. The orchestrator will locate and load these automatically via Glob.

- `references/reporting-templates.md` — Slack update templates, Spend Tracker structure, monthly report formats, and data field definitions. Needed during Phases 3, 4, and 5 before composing updates and reports.

---

## Phase 4: Weekly Slack Update

The weekly Slack update is a brief, scannable performance summary posted to Challenger's internal Slack channel (or shared with the operator for review before posting).

**Gather this data from Ads Manager (last 7 days):**
- Total spend
- Impressions and reach
- Clicks (link clicks)
- CTR
- CPA (cost per purchase or lead)
- ROAS (if eCommerce)
- Number of purchases or leads
- Top-performing ad or creative (by CPA or ROAS)

**Format the update:**

```
📊 Meta Ads Weekly Update — [Client Name]
Period: [Mon DD] – [Mon DD]

Spend: $[X] of $[monthly budget] budget used ($[X] remaining)
Purchases/Leads: [N] at avg CPA of $[X] (target: $[X])
ROAS: [X.X] (target: [X.X]) [eCommerce only]

🏆 Top performing creative: [Ad name or description] — $[CPA] CPA
⚠️ Flagged: [Any issue — creative fatigue, pixel issue, budget pacing off]

Next 7 days: [Brief note — new experiment launching, scaling, monitoring]
```

Keep it to 6–8 lines maximum. Clients scan these — not read them.

---

## Phase 5: Spend Tracker Update

The Spend Tracker is the shared Google Sheet that tracks channel-level spend and performance over time.

Template: [[Template] E-commerce Spend Tracker](https://docs.google.com/spreadsheets/d/1Fu4qdoac1LoJffnd3JNOHcxE1bE9AzweVeuLt_OTr7c/edit)

**Weekly update:**
- Add the week's spend to the Meta Ads column
- Update the conversion column (purchases or leads)
- Calculate CPA for the week
- Add any notes (new experiment, budget change, seasonality flag)

**If multi-channel:** The Spend Tracker tracks all channels (Meta, Google, email, direct). Update Meta columns only — leave other channels to their respective managers.

---

## Phase 6: Monthly Ad Insights Report

The monthly report is the comprehensive performance review delivered to Challenger. It covers the full month's performance, experiment results, and the plan for next month.

Template: [[Template]: Ad Insights deck](https://docs.google.com/presentation/d/1IK7uqLs_XrL3nOrknppb_2pasZNVotFRO4L_LPkFqu4/edit)

**Gather this data from Ads Manager (last 30 days):**
- Total spend vs. budget
- Total purchases or leads
- Avg CPA and ROAS (vs. prior month and vs. target)
- Impression share and reach
- Top 3 performing ads / creative (with names or descriptions)
- Bottom 3 performing ads (what was paused and why)
- Experiment results (what was tested, what won, what was phased out)
- Change Log summary (all major actions taken in the month)

**Monthly report sections:**

| Section | Content |
|---|---|
| Performance Summary | Spend, CPA, ROAS vs. target and prior month |
| Creative Performance | Top and bottom performers with key learning |
| Experiment Results | What Experiment #N tested, what won, what was moved to ADV+ |
| Scaling & Budget | Budget changes made and rationale |
| Next Month Plan | Next experiment type, scaling intentions, any structural changes |

**Preparing the narrative:**
The numbers tell what happened. The narrative tells why and what's next. Always include:
- One "what worked well and why" observation
- One "what we'll do differently" observation
- One "what we're testing next" commitment

---

## Phase 7: Output Format + Branding

> "Report content ready. What format would you like?
>
> 1. **DOCX Report** — full written monthly performance report with narrative, tables, and recommendations
> 2. **Slide brief** — structured notes to populate the Ad Insights deck template slide by slide
> 3. **Slack update** — weekly update formatted for Slack
> 4. **Spend Tracker update** — summary of what to enter into the weekly tracker"

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colours, fonts, and layout rules before building output.

Build based on chosen format:
- **DOCX** → invoke the docx skill; apply branding; include: performance summary → creative performance → experiment results → next month plan
- **Slide brief** → section-by-section notes for the Ad Insights deck
- **Slack update** → formatted per the weekly update template
- **Spend Tracker** → data table showing what to input for the week

---

## Synthesis Brief

Before building the final deliverable, write a plain-text summary of key findings for orchestrator handoff.

**Meta Ads Reporting Key Findings:**
- ROAS by campaign (weekly and monthly avg, vs. target, direction and % variance)
- CPM trends (week-over-week change, seasonality impact, platform inflation notes)
- Top creatives by CTR (top 3 performers, CTR %, link clicks, engagement signal)
- Recommended budget shifts (increase/decrease amount and rationale based on CPA/ROAS performance)
- Spend pacing vs. budget (current month spend rate, projected month-end position, pace trajectory)

**Priority for downstream skills:** Route findings to meta-ads-scaling (if budget pacing requires adjustment or CPA/ROAS trend warrants scaling decision), meta-ads-creative-testing (if underperforming or fatigued creative identified), or hold for manual AM review if performance meets target and no action needed.

*If running standalone, share this summary with the operator or client team before the full deliverable.*

---

## Phase 8: Pre-Delivery QA

Before delivering:
- [ ] Reporting period confirmed (correct date range pulled from Ads Manager)
- [ ] Performance vs. target clearly stated (not just raw numbers — always vs. target)
- [ ] Weekly updates: spend, leads/purchases, CPA, top performer, and flagged issues included
- [ ] For monthly reports: experiment results summarised with winner/loser and action taken
- [ ] For spend tracker: Meta channel data only (don't overwrite other channels)
- [ ] Next steps or next month plan included
- [ ] Output format and branding preference confirmed
