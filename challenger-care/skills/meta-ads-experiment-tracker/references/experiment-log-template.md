# Experiment Log — Templates & Structure

## Google Sheets Experiment Log

Each client should have an experiment log tab in their Spend Tracker spreadsheet (or a standalone sheet). The column structure below is the standard format.

### Column Structure

| Col | Field | Type | Notes |
|-----|-------|------|-------|
| A | Experiment # | Number | Sequential per client. Never reuse. |
| B | Launch Date | Date | Date the DCT went live in Ads Manager |
| C | Review Date | Date | 7-day review date (launch + 7 days) |
| D | Status | Text | Pre-launch / Active / Concluded / Inconclusive |
| E | What Was Tested | Text | The variable. One thing only. |
| F | Control Element | Text | What stayed constant across all variations |
| G | Hypothesis | Text | "We believe [X] will outperform [Y] because [Z]" |
| H | # of Variations | Number | Total ad permutations in the DCT |
| I | Success Metric | Text | CPA < $X / ROAS > X / CTR > X% |
| J | Winner | Text | Variation name, or "Inconclusive" |
| K | Winner CPA / ROAS | Number | Winning variation's key metric |
| L | Loser CPA / ROAS | Number | Losing variation's key metric (or worst performer) |
| M | Action Taken | Text | Promoted to legacy / Paused / Moved to ADV+ / Still running |
| N | Audience Learning | Text | What this result revealed about the audience (full sentence) |
| O | Next Hypothesis | Text | What to test next, based on this result |
| P | Notes | Text | Any anomalies, seasonality, budget changes, or context that affected results |

---

## Pre-Launch Entry Format

When logging a new experiment before it goes live, produce values for columns A–I. Leave J–O blank — those are filled after the experiment concludes.

```
Experiment Log Entry — PRE-LAUNCH

Client: [Client Name]
Experiment #: [N]
Launch Date: [Date]
Review Date: [Launch Date + 7 days]
Status: Pre-launch

What Was Tested: [The variable — one thing. e.g., "Hook angle: curiosity vs. pain-point"]
Control Element: [What stays constant. e.g., "Same product images, same primary text, same offer ($30 off)"]
Hypothesis: "We believe [X] will outperform [Y] because [Z]."
# of Variations: [N]
Success Metric: [CPA below $X / ROAS above X / CTR above X%]
```

---

## Post-Experiment Entry Format

When logging results after the 7-day review, complete columns J–O.

```
Experiment Log Entry — RESULT

Client: [Client Name]
Experiment #: [N]
Status: Concluded [or Inconclusive]

Winner: [Variation name or "Inconclusive — insufficient data"]
Winner [CPA / ROAS]: [$X / X]
Loser [CPA / ROAS]: [$X / X] (worst performer)
Account average [CPA / ROAS] same period: [$X / X] (for context)

Action Taken: [Promoted to legacy ad set / Paused / Moved to ADV+ / Continuing — needs more data]

Audience Learning:
[One full sentence that goes beyond the result. Not: "Curiosity hook won."
Instead: "Our audience responds to curiosity hooks more than pain-point hooks, suggesting they are not yet actively searching for a solution — they need to be interrupted and made aware of the problem before the product can be sold."]

Next Hypothesis:
[Specific and testable. Not: "Test more UGC."
Instead: "Test whether founder-led UGC using the curiosity hook outperforms the winning static variation when using the identical hook line."]

Notes:
[Anything that may have affected results: "CPMs spiked mid-week due to a competitor promotion." / "Client paused the account for 2 days." / "Seasonality: Black Friday weekend overlap."]
```

---

## Learning Quality Guide

The audience learning is the most important field in the log. Push past surface-level results.

**Weak learning (result statement):** "The before/after static image won."
**Strong learning (audience insight):** "Transformation-focused creative consistently outperforms product-focused creative for this audience — they need to see the outcome they're buying, not the product itself. This suggests a low-awareness audience that hasn't yet connected the product to their desired result."

**Weak learning:** "Video outperformed static."
**Strong learning:** "Video outperforms static when it shows the product being used in a realistic setting. This audience needs to see themselves in the scenario, not just see the product. Demo-style video works; talking-head testimonial without product demo does not."

**Weak learning:** "Inconclusive — not enough data."
**Strong learning (even from inconclusive results):** "The experiment ran for 7 days with a $15/day budget and generated 3 purchases total — insufficient to draw conclusions. This signals the test budget needs to be at least $25/day to get 7+ conversions per variation within the review window. Adjust test budget for Experiment #[N+1]."

**Rule:** If you can't answer "what does this tell us about the customer?", the learning isn't done yet.

---

## Next Hypothesis Guide

Every experiment should inform the next one. The next hypothesis should follow logically from the current result.

**If the experiment was conclusive (clear winner):**
→ Test a variation of the winning element to understand why it won.

Example: Curiosity hook won. Next: Test 3 different curiosity hooks against each other to find the strongest specific angle within curiosity.

**If the experiment was inconclusive:**
→ Either increase the test budget, extend the run time, or test a more dramatic variable that creates clearer signal.

Example: Static vs. video was inconclusive. Next: Test the same concept using radically different creative — founder UGC vs. polished studio video — to get a stronger signal.

**If the experiment lost badly (control clearly better):**
→ Understand why it failed. Was the hook wrong? The visual? The audience expectation?

Example: Aspirational lifestyle images dramatically underperformed the product hero images. Next: Test another aspirational angle (social proof / outcome-driven copy overlay) to determine if aspirational framing itself is the issue, or just the specific execution.

---

## Pattern Synthesis Output Format

Use this format when producing the synthesis after 3+ experiments.

```
EXPERIMENT PATTERN SYNTHESIS
Client: [Client Name]
Experiments covered: #[N] through #[N]
Prepared: [Date]

─────────────────────────────────────
FORMAT PATTERNS
─────────────────────────────────────
[What the data shows about static vs. video vs. UGC performance. Minimum 2 experiments to support a pattern.]

Example: "Static images have outperformed video in 3 of 4 experiments (Exp #1, #2, #4). The one exception (Exp #3) used UGC-style video, which outperformed the control static. Pattern: polished produced video underperforms; raw or product-focused static and UGC-style video both work."

─────────────────────────────────────
HOOK ANGLE PATTERNS
─────────────────────────────────────
[Which hook types have won, which have consistently lost.]

Example: "Pain-point hooks have won 2 of 2 tests (Exp #1, #3). Aspirational/lifestyle hooks have lost in both experiments where tested (Exp #2, #4). Pattern: this audience is pain-aware and responds to acknowledgment of their problem before being shown the solution."

─────────────────────────────────────
AUDIENCE SIGNAL
─────────────────────────────────────
[What the cumulative learnings reveal about who this customer is and what motivates them.]

Example: "This audience is in the middle of the funnel — they are aware of the problem but haven't committed to a solution. They respond to pain acknowledgment + a specific, credible outcome. They do not respond to lifestyle aspiration or identity-based messaging. Price sensitivity appears low: the offer test (Exp #5) showed minimal performance difference between $20-off and full-price ads."

─────────────────────────────────────
CREATIVE ELEMENTS DUE FOR ROTATION
─────────────────────────────────────
[Any legacy ads that have been running 90+ days with declining CTR or rising CPA.]

─────────────────────────────────────
RECOMMENDED NEXT EXPERIMENT
─────────────────────────────────────
Hypothesis: "[Full hypothesis sentence]"
Rationale: "[Why this is the highest-value test based on the pattern data above]"
Variable to test: "[Specific variable]"
Control: "[What stays constant]"
Suggested format: [Static / UGC / Video]
Suggested number of variations: [N]
```
