# Reporting Templates — Weekly Slack Update & Monthly Ad Insights

## Weekly Slack Update — Full Template

```
📊 Meta Ads Weekly Update — [Client Name]
Period: [Mon DD] – [Sun DD, YYYY]

💰 Spend: $[X] spent | $[X] remaining of $[monthly budget] budget
📦 Results: [N] [purchases/leads] | Avg CPA: $[X] (target: $[X])
📈 ROAS: [X.X]x (target: [X.X]x) ← eCommerce only

🏆 Top creative: [Short description] — $[X] CPA / [X]x ROAS
[Optional: 🥈 Runner-up: [Short description] — $[X] CPA]

[Optional ⚠️ Flag: [Any issue requiring attention — e.g., creative fatigue detected on legacy ad, pixel data delay noticed]]

▶️ This week: [1–2 lines on what's happening — experiment launching, scaling, monitoring only]
```

**Formatting rules:**
- Keep it to 8–10 lines maximum — clients scan these on mobile
- Always compare CPA/ROAS to target (not just raw numbers)
- Highlight one specific creative by name — it makes the update feel specific and trustworthy
- Only flag issues if they're real — don't add ⚠️ to every update
- End with the forward-looking "This week" line — always close with what's next

**When to post:** Every Monday morning (or agreed day). Post in Challenger's internal Slack channel (not in client-facing channels unless the operator confirms this is the right place).

---

## Monthly Ad Insights Deck — Slide-by-Slide Structure

The Ad Insights deck template covers 8–10 slides. Here is the content for each:

### Slide 1: Cover
- Client logo + logo (or client branding only if white-label)
- Month and year
- Prepared by: [the operator name]

### Slide 2: Performance Summary (the most important slide)
- Total spend vs. budget (% used)
- Total results: purchases or leads
- Average CPA vs. target (with trend arrow: ↑ improved, ↓ declined, → stable)
- ROAS vs. target (eCommerce)
- Month-over-month comparison (vs. prior month — same metrics)

**Narrative to include (2–3 sentences):** What drove performance this month. Was it creative, budget, seasonality?

### Slide 3: Budget Pacing
- Daily spend chart (if available from Ads Manager screenshot or export)
- Any scaling actions taken: date, amount changed, and result
- Budget remaining / projected month-end spend

### Slide 4: Creative Performance
- Top 3 ad combinations (headline + image/video): CPA, impressions, spend each
- Bottom 3 ad combinations: CPA, why paused
- **Key insight (1–2 sentences):** What the creative performance tells you about the audience

### Slide 5: Experiment Results
- Experiment name and number
- What was tested: [variable] (images/copy/format/angle)
- Results: Winner → [specific element] at [CPA/ROAS]. Loser → [element] at [CPA/ROAS]
- Actions taken: Winner promoted to legacy. Non-performer moved to ADV+ or paused.
- Next experiment: [what's planned for next month and why]

### Slide 6: Account Activity Log (Change Log Summary)
- Table of all major actions taken in the month
- Format: Date | Action | Reason | Result
- Keep it concise — 5–8 rows max

### Slide 7: Next Month Plan
- Budget plan (maintaining, increasing, or decreasing — and why)
- Next experiment: type, hypothesis, assets needed
- Any structural changes planned
- Any external factors to watch (seasonality, promotions, competitive activity)

### Slide 8: Appendix (Optional)
- Raw data tables from Ads Manager
- Full ad-level performance breakdown
- Experiment permutation list

---

## Narrative Framing Guidance

The monthly report should not just be numbers. It should tell a story that Challenger can understand and act on. For each month, prepare:

**1. What worked (and why):**
> "This month, our lifestyle image creative significantly outperformed product-only images — $14 CPA vs. $28 CPA. This suggests the Oaktree Home audience responds more to aspirational content than feature-led creative. We'll build on this in next month's experiment."

**2. What didn't work (and the learning):**
> "The discount-led copy angle ('20% off today') had above-average CTR but a high bounce rate and no purchases — suggesting price-sensitive clicks that didn't convert. We're not running discount angles in next month's experiment."

**3. What's next (commitment):**
> "Experiment #2 will test three new video hooks against our current best-performing static image. We'll have the creative brief to you by [date] for approval."

---

## Data Sources in Ads Manager

Where to pull each metric for reports:

| Metric | Location in Ads Manager |
|---|---|
| Total spend | Campaign level → Columns → Performance |
| CPA (Cost per result) | Campaign level → Cost per result column |
| ROAS | Campaign level → Purchase ROAS column |
| Impressions / Reach | Add columns → Delivery |
| CTR | Add columns → Performance and Clicks |
| Top performing ad | Ad level view → sort by CPA ascending |
| Frequency | Ad set level → Delivery columns |
| Budget pacing | Campaign level → Daily budget × days elapsed |

**Date range:** Always set to the exact reporting period. The default "Last 7 days" or "Last 30 days" may not match the reporting period exactly.
