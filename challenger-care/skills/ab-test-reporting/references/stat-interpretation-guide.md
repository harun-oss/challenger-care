# Statistical Interpretation Guide — A/B Testing

## The two frameworks in use at clients run tests on different platforms. The two stat frameworks encountered are:

| Framework | Platform examples | Key metric | Decision threshold |
|-----------|------------------|-----------|-------------------|
| **Frequentist** | Convert, AB Tasty, Optimizely | P-Value | p < 0.05 (95% confidence) |
| **Bayesian** | VWO | Decision Probability | ≥95% probability of improvement |

These are not interchangeable. Never describe a Bayesian probability as a "P-value" or vice versa.

---

## Frequentist statistics (Convert, AB Tasty)

### What the numbers mean

**P-Value:** The probability of observing the measured difference (or larger) if the variant had no real effect. Lower = stronger evidence of a real effect.
- p < 0.05 → less than 5% chance the result is due to chance → statistically significant at 95% confidence
- p < 0.10 → 90% confidence → directional signal only, not a clean win

**Significance (Yes/No):** Whether the test has crossed the pre-set threshold (typically p < 0.05).

**C.V.R. (Conversion Rate):** Experiment Conversion / Experiment Sessions

**Uplift / Decline:** `(Variant CVR − Control CVR) / Control CVR × 100`

### Minimum sample size

Never draw conclusions from < 500 sessions per variant. Even with a "significant" P-value, small sample sizes produce unreliable estimates with wide confidence intervals. Always check whether traffic is sufficient before reporting a win.

For tests with multiple variants, each individual variant needs 500+ sessions — not just the total.

### Common errors

**Peeking (stopping too early)**
Checking significance multiple times during a test and stopping when you first see p < 0.05 inflates false positive rate. standard: significance should be stable for ≥7 consecutive days before calling a winner.

**Sample Ratio Mismatch (SRM)**
If you allocate 50/50 but one variant has materially more sessions (>10% imbalance), something is wrong with traffic allocation. Results are unreliable. Flag with the anomaly callout and investigate.

**Novelty effect**
Users interact with a new variant just because it's different, then return to baseline behavior. Always check week-over-week CVR trend. If variant CVR was high week 1 and declining, note this in observations.

**Segment pollution**
If a test targets "All Users" but results differ dramatically between mobile and desktop, the combined number may mask opposite directional signals. Flag for device-level analysis.

---

## Bayesian statistics (VWO)

### What the numbers mean

**Expected Conversion Rate:** The posterior estimate of the true CVR for each variation, based on observed data + prior.

**Expected Improvement %:** The expected lift of the variant over the baseline, expressed as a relative % with a confidence interval bar.

**Decision Probabilities:** The probability that a variant is better than the baseline. Presented as a bar showing red (probability of being worse) and green (probability of being better).
- ≥95% → strong signal → eligible for SHIP
- 80–94% → directional positive → KEEP RUNNING
- <80% → inconclusive → continue or reassess

**MDE (Minimum Detectable Effect):** The smallest lift the test was designed to detect at the given traffic and power settings. If Expected Improvement < MDE, the test likely lacks sufficient traffic to detect the change being tested.

**ROPE (Region of Practical Equivalence):** A range around 0 within which a difference is considered practically negligible (not worth acting on even if real). If Expected Improvement falls within ±ROPE, treat as flat.

**Power:** Probability of detecting a true effect if one exists. VWO default: 80%.

**FPR (False Positive Rate):** Probability of incorrectly declaring a winner when there is none. VWO default: 10%.

### VWO-specific issues

**30-day data loss**
VWO automatically purges visitor assignment data after 30 days. Tests running longer than 30 days will show inflated data for recent visitors (who were re-assigned) vs. historical visitors (whose data was purged). This skews results toward the currently-winning variant. Always flag this with the anomaly callout.

**Control showing "No data yet"**
This happens when a previous variant is serving as the baseline (not the original control). The original control was paused and an iteration was set as the new "baseline." Document explicitly: *"Note: [Variant X] is the baseline for this comparison. Original control is not receiving traffic."*

**Klaviyo vs. VWO data**
VWO tracks click events and page interactions. Klaviyo tracks actual form submissions (which may lag VWO events by minutes or hours if webhook-based). For lead-gen clients, always report both:
1. VWO data for engagement/click goals
2. Klaviyo data for actual form submits
3. A "Leads Overall" summary that combines both

---

## Practical decision guide

### "Should we call this a winner?"

Ask these questions in order:

1. **Is the PRIMARY goal significant?** (p < 0.05 or ≥95% Decision Probability)
2. **Have all GUARDRAIL goals been checked?** No significant negatives?
3. **Is the sample size sufficient?** ≥500 sessions per variant?
4. **Has significance been stable?** At least 7 days of consistent results (frequentist)?
5. **Is there any data quality issue?** SRM, tracking errors, VWO data loss?

If all 5 answers are YES → SHIP. If any is NO → do not call a winner yet.

### "Should we keep running?"

- Directional positive (p 0.05–0.10 or 80–94% Decision Probability) + insufficient sample → KEEP RUNNING
- Positive but <7 days of stability → KEEP RUNNING
- Approaching significance with 2–4 weeks to go → KEEP RUNNING

### "Should we pause and iterate?"

- Test running >4 weeks with no meaningful signal + traffic too low for MDE → redesign hypothesis
- PRIMARY goal positive but GUARDRAIL significantly negative → address the tension
- Upstream dependency broken (e.g., landing page the test drives traffic to was redesigned) → pause until LP updated

### "Should we kill it?"

- PRIMARY goal significantly negative (≥95% confidence or p < 0.05 in the wrong direction)
- Extract the learning: what did users dislike? What assumption was wrong?

---

## Revenue / lead impact worked examples

### Lead-gen example (NBC)
- Control CVR: 12.5%
- Variant CVR: 14.3%
- Monthly sessions: 8,000
- Monthly lift: (0.143 − 0.125) × 8,000 = 144 additional leads/month
- Annual lift: 144 × 12 = 1,728 additional leads/year

### eComm example
- Control CVR: 2.8%
- Variant CVR: 3.2%
- Monthly sessions: 50,000
- AOV: $85
- Monthly revenue lift: (0.032 − 0.028) × 50,000 × $85 = $17,000/month
- Annual revenue lift: $17,000 × 12 = $204,000/year

Always note: *"Based on current traffic levels. Assumes variant performance holds post-ship."*

---

## Language standards

| Situation | Use this language | Avoid |
|-----------|------------------|-------|
| p < 0.05 / ≥95% Decision Probability | "Statistically significant — we recommend shipping" | "This test won" (too casual) |
| p 0.05–0.10 / 80–94% Decision Probability | "Positive directional trend — continuing to collect data" | "Looks like a winner" |
| p > 0.10 / <80% Decision Probability | "No significant signal at this time" | "Flat" alone (too dismissive — still useful data) |
| Negative result | "The variant underperformed the control on [goal]" | "The test failed" |
| Data anomaly | "Results should be treated as directional due to [issue]" | Omitting the issue entirely |
