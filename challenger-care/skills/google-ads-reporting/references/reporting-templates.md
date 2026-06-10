# Google Ads Reporting Templates

Reference for the google-ads-reporting skill. Read the relevant section during the phase indicated.

---

## Weekly Slack Update

### Formatting rules

- Use Slack markdown: `*bold*`, backticks for numbers, line breaks between sections
- Include the emoji header line — it signals a performance update vs a question/comment
- Keep it under 250 words — if the account has nothing notable to say, say so briefly
- Always include the Bid Strategy Status line — this is a key differentiator from a basic report

### Full template

```
📊 *[Client Name] — Google Ads Weekly Update | [Week of MM/DD–MM/DD]*

*Performance (Last 7 Days):*
Spend: $X | Clicks: X | Conversions: X | CPA: $X (target: $X)
[For eCommerce]: Spend: $X | Revenue: $X | ROAS: X.Xx (target: X.Xx)

*vs Prior 7 Days:*
Spend [+/-X%] | Conversions [+/-X%] | CPA [+/-X%]

*What's working:*
[Specific example — e.g., "The Non-Brand campaign hit a 4.2% Conv. Rate this week, best in 30 days, driven by the new RSA variant we launched Monday."]

*Watch list:*
[One item — e.g., "Branded campaign is at 85% of its weekly budget cap by Thursday — may need a budget increase if branded search volume holds."]

*Bid Strategy Status:*
[Campaign name]: [Current strategy] — [X] conversions in the last 30 days. [Next step: e.g., "Target is 30 to graduate to Maximize Conversions — on track for graduation in ~2 weeks."]

*This Week's Focus:*
[One specific action — e.g., "Adding 15 new negatives from last week's search term report to cut irrelevant traffic."]
```

### Narrative framing by performance type

**When performance is above target:**
Lead with the win, then explain why — algorithm learning? Better intent keywords? New RSA? Give the team something specific to replicate.
> "We hit our lowest CPA in 6 weeks this week ($42 vs $55 target). The new Non-Brand RSA launched on Monday is outperforming the prior control by 60% on CTR, and it's pulling the account average up."

**When performance is below target:**
Name the cause before the number — don't lead with bad news without context.
> "CPA came in at $78 this week vs our $55 target. The spike is expected — we graduated to tCPA on Monday and the algorithm is in its learning phase (typically 1–2 weeks of volatility). We're watching daily and will not make further changes until the algorithm stabilizes."

**When performance is flat:**
Flat is a signal too — explain what it means and what's being done.
> "Performance held steady this week — no major swings. This is the plateau we typically see before we graduate bid strategies. We're at 26/30 conversions needed for Maximize Conversions. Expect the next report to show the strategy shift."

---

## Spend Tracker

The Spend Tracker (separate versions for eCommerce and Lead Gen) is updated weekly to track cumulative spend and performance against the monthly budget and target.

### When to update

Update at the end of each week (Friday or Monday covering the prior week). Also update at month-end to close out the month's record.

### Column-by-column entry guide

**eCommerce Spend Tracker columns:**

| Column | What to enter |
|--------|--------------|
| Week Ending | Last day of the reporting week (e.g., "Apr 6") |
| Weekly Spend | Total spend from Google Ads this week (all campaigns combined) |
| MTD Spend | Cumulative spend from day 1 of the month through this week |
| Weekly Revenue | Total conversion value from Google Ads this week |
| MTD Revenue | Cumulative conversion value month-to-date |
| Weekly ROAS | Weekly Revenue ÷ Weekly Spend |
| MTD ROAS | MTD Revenue ÷ MTD Spend |
| Monthly Budget | Agreed monthly budget for this client (fixed, carry forward each week) |
| Budget Remaining | Monthly Budget minus MTD Spend |
| Projected Month-End | (MTD Spend ÷ days elapsed) × days in month |
| Notes | Campaign changes, bid strategy shifts, budget changes, promo periods |

**Lead Gen Spend Tracker columns:**

| Column | What to enter |
|--------|--------------|
| Week Ending | Last day of the reporting week |
| Weekly Spend | Total spend from Google Ads this week |
| MTD Spend | Cumulative spend month-to-date |
| Weekly Leads | Total conversions from Google Ads this week |
| MTD Leads | Cumulative conversions month-to-date |
| Weekly CPA | Weekly Spend ÷ Weekly Leads |
| MTD CPA | MTD Spend ÷ MTD Leads |
| Monthly Budget | Agreed monthly budget (carry forward) |
| Budget Remaining | Monthly Budget minus MTD Spend |
| Projected Month-End | (MTD Spend ÷ days elapsed) × days in month |
| Notes | Campaign changes, tracking issues, seasonality flags |

### Budget pacing flags

Pacing alerts to add to the Notes column and flag in the Slack update:

- **Overpacing (>10% above budget pace):** "(!) Overpacing — projected to spend $X this month vs $X budget. Check daily budgets across all campaigns."
- **Underpacing (>10% below budget pace):** "(!) Underpacing — projected $X vs $X budget. Common causes: tCPA too low, Quality Score drop, impression share loss. Investigate before end of week."
- **On pace (within 10%):** No flag needed — enter a "✓ On pace" note for clarity.

---

## Monthly Report

The monthly Google Ads Insights report is delivered at or just before the monthly strategy call. It gives Challenger a clear picture of what happened, why it happened, and what's coming next.

### Slide/section structure

**Section 1: Performance Scorecard**

One-page summary table:

| Metric | This Month | Last Month | Target | Status |
|--------|-----------|-----------|--------|--------|
| Spend | | | | |
| Clicks | | | | |
| Impressions | | | | |
| Conversions / Revenue | | | | |
| CPA / ROAS | | | | |
| Conv. Rate | | | | |
| Avg. CPC | | | | |

Status column: use ✅ (at or better than target), ⚠️ (within 20% of target), or 🔴 (more than 20% off target).

Headline sentence below the table: one sentence that captures the month. Example: "April was our strongest CPA month in 6 months, driven by the Non-Brand campaign graduating to tCPA on April 2nd."

**Section 2: Campaign Breakdown**

Table: one row per campaign. Columns: Campaign Name, Spend, Conversions/Revenue, CPA/ROAS, vs Target, Status.

Callout box: which campaign drove the most conversions? Which had the highest CPA and why?

**Section 3: Keyword Highlights**

Two columns:
- *Top 5 converting keywords:* keyword, conversions, CPA/ROAS
- *Changes made:* new keywords added, keywords paused, search terms converted to negatives (how many negatives added this month?)

**Section 4: Ad Copy Performance**

RSA performance table: Ad name/label, Ad Strength rating, CTR, Conversions, CPA/ROAS.

Call out: any new variants launched this month? Any underperforming ads paused?

Copy insight: what headline angle or description theme is winning? (e.g., "Pain-point headlines are outperforming benefit headlines 2:1 on CTR in the Non-Brand campaign")

**Section 5: PMAX Insights (if running)**

Only include if PMAX is active. Cover:
- Total spend on PMAX vs RSA this month
- Top-performing asset type (image, video, text)
- Asset groups: performance split if multiple are running
- Search themes: any new themes added or removed?
- Any cannibalisation signals? (RSA impression share declining as PMAX scales)

**Section 6: What Worked / What Didn't / What's Next**

The most important section. Always present all three parts — even if performance was strong, identify one honest limitation.

Format:
> **What worked:** [Specific, attributable win. Not "performance was good" — which campaign, keyword, or copy change drove it and why?]
>
> **What didn't:** [Honest observation. If everything was great, identify one thing that underperformed relative to expectation, even if it was minor.]
>
> **What's next:** [2–3 specific actions with expected timeline. Example: "1. Graduate Non-Brand to tCPA when we hit 30 conversions (projected week of April 14). 2. Launch competitor campaign by April 21 — brief is drafted. 3. Add PMAX asset group for spring collection by April 28."]

**Section 7: Bid Strategy Progression**

Table: one row per campaign. Columns: Campaign, Current Bid Strategy, Conversions (last 30 days), Next Strategy, Threshold to Graduate, Estimated Timeline.

Narrative: explain the progression in plain language — where are we in the account's maturity arc? What will change once the next threshold is reached?

---

## Data Sources in Google Ads

Where to pull each metric:

| Metric | Location in Google Ads |
|--------|------------------------|
| Spend / Clicks / Impressions | Campaigns → Date range filter → Summary row |
| Conversions | Campaigns → Columns → Conversions → Conversions, Cost/conv., Conv. rate |
| Conversion value / ROAS | Campaigns → Columns → Conversions → Conv. value, Value/cost |
| By campaign | Campaigns tab → select campaign → apply date range |
| Keyword performance | Keywords tab → last 30 days |
| Search terms | Keywords → Search terms |
| Ad performance | Ads tab → RSAs and PMAx asset groups |
| Auction Insights | Campaigns → Auction Insights |
| Bid strategy status | Campaigns → Bid strategy column |
