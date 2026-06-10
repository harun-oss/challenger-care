---
name: ab-test-reporting
description: 'Documents A/B test results - per-test setup, statistical interpretation, decision (Ship/Keep Running/Pause/Kill), anomalies, lessons-from-tests synthesis. Markdown output. Pairs with `test-price-claim` and `testing-roadmap`. MANDATORY TRIGGER: any mention of "A/B test report", "test results writeup", "interpret P-values", "VWO Decision Probability", "ship or kill decision", "lessons from tests", "A/B test conclusions". Do NOT use for: Building test roadmap (use `testing-roadmap`). Designing single test (use `test-price-claim`).'
---

> **Permission tier:** generate · **Tools/context:** assets/goals-targets.md, assets/team-roles.md, CONFIG.md, assets/experiment-log.md


# A/B Test Reporting Skill

## What this skill does

This skill helps PMs build and populate the **Test Update Deck** — Challenger's primary deliverable for client CRO calls. It takes raw test data (variant descriptions, goal metrics, P-values or Bayesian probabilities) and outputs structured narrative content: observation bullets, statistical interpretation, decision recommendations, test learnings, and the opening "Lessons from Tests" synthesis.

Output options:
- **Structured text** — slide-by-slide copy ready to paste into the Figma deck template
- **Full PPTX** — invoke the pptx skill with branding (#4677F7, #F5F7F9, #000000 cover, Poppins Bold / Mulish Regular)

Handles both stat formats:
- **Frequentist** (Convert, AB Tasty, Optimizely): P-Value + Significance + Sessions/CVR/Uplift table
- **Bayesian** (VWO): Decision Probabilities + Expected Improvement + Unique Conversions/Visitors

---

## Test Update Deck anatomy

Every deck follows this exact structure. The skill must preserve this order.

### 1. Opening context section

| Slide | Content |
|-------|---------|
| Cover | Client name · "Test Update Deck" · Date |
| Funnel/Campaign Overview | Drop-off % by step (B2B: Klaviyo form step completion; eComm: CPL funnel percentages) |
| Lessons from [N] Tests | Categorized wins by theme — updated every deck |
| Roadmap | Upcoming tests per funnel step, organized by: Pushing Live · Dev · Design · Planning · Ideation · On Hold |

### 2. Status section dividers

Plain, centered-text slides — one per section, in this order:

**LIVE → DESIGN → DEV → Ready to go Live → Winner → PAUSED → FLAT → ARCHIVE**

### 3. Per-test block (one block per test)

**Setup slide** (one per test):
```
Header:   [STATUS LABEL] — [TEST ID]: [Test Name] — Figma
Body:     Test hypothesis (full sentence)
Block 1:  URL TARGETING (black background)
Block 2:  EXPERIMENT GOALS — list each goal tagged [PRIMARY] or [GUARDRAIL]
Block 3:  AUDIENCE TARGETING & TRAFFIC ALLOCATION
Block 4:  TEST PARAMETERS (new — see below)
Visual:   Control + Variant screenshot(s) side by side with Figma link
```

**TEST PARAMETERS block** (required for every LIVE, DESIGN, DEV test):
- Testing Platform (Convert / VWO / AB Tasty / other)
- Start Date
- Planned Duration
- Significance Threshold (e.g. p<0.05 / 95% Decision Probability)
- MDE — Minimum Detectable Effect (e.g. ±15% relative lift)
- Traffic Allocation

**Results slides** (one per goal — LIVE and PAUSED tests only):
```
Header:   [Goal name]
Content:  Statistical data table (format depends on platform — see below)
Footer:   Observation bullets (2–4 per slide)
```

**Decision + Learnings slide** (one per completed / paused test):
```
RECOMMENDATION: [SHIP ✓] [KEEP RUNNING →] [PAUSE & ITERATE ⟳] [KILL ✗]
Rationale: 1–2 sentences
What this test proved: [insight]
What it suggests for the next iteration: [hypothesis evolution]
Revenue/lead impact: [if SHIP recommendation — see calculation below]
```

### 4. Supplemental analytics slides

Include after LIVE section or in ARCHIVE:
- **Form Abandonment** — step completion funnel (Klaviyo or custom tracking data)
- **Heatmap Callouts** — if available, embed within the relevant LIVE test block
- **GA4 / Period Comparisons** — for ARCHIVE section and context slides

---

## Goal labeling: Primary vs. Guardrail

Every experiment goal must be labeled before results are reported.

| Label | Definition | Example goals |
|-------|-----------|---------------|
| **[PRIMARY]** | The core conversion metric you are optimizing for | Form Submits, Clicks Yes, Sign Ups, Add to Cart |
| **[GUARDRAIL]** | A metric you are watching to ensure no harm — you want it flat or positive, never significantly negative | Clicks No, Bounce Rate, Page Depth, Revenue per Session |

A test where the PRIMARY goal wins but a GUARDRAIL metric significantly worsens is **not a clean win** — use PAUSE & ITERATE.

---

## Statistical interpretation

### Frequentist format (Convert, AB Tasty, Optimizely)

Results table format:
```
| P-Value [X]   | Experiment Sessions | Experiment Conversion | C.V.R.  | Uplift / Decline |
| Significance  | Control: [X]        | Control: [X]          | [X.XX%] | —                |
| Yes / No      | Variant: [X]        | Variant: [X]          | [X.XX%] | [+/- X.XX%]      |
```

Interpretation rules:
- P-Value < 0.05 → Significant at 95% confidence → eligible for SHIP
- P-Value 0.05–0.10 → Directionally significant at 90% → "positive directional trend — continue running"
- P-Value > 0.10 → Not significant → report CVR direction only, never quote uplift as confirmed
- Uplift = `(Variant CVR − Control CVR) / Control CVR × 100`
- Minimum viable sample: 500+ sessions per variant before drawing conclusions

**Common errors to flag:**
- **Peeking**: Test stopped early when significance flickered — check if significance has been stable for 7+ days
- **Sample ratio mismatch (SRM)**: Variant sessions >10% different from control — flag and investigate before calling results
- **Novelty effect**: Variant CVR high in week 1 then declining — always check week-over-week trend

### Bayesian format (VWO)

Results shown in VWO UI:
```
Unique Conversions / Visitors · Expected CVR · Expected Improvement % · Decision Probabilities bar
Settings shown: MDE · ROPE · Power · FPR
```

Interpretation rules:
- Decision Probability ≥ 95% → Call winner → eligible for SHIP
- Decision Probability 80–94% → Strong signal → KEEP RUNNING unless business context demands sooner call
- Decision Probability < 80% → Inconclusive → continue running or reassess if traffic is too low
- **ROPE (Region of Practical Equivalence)**: If Expected Improvement falls within ±ROPE, the effect is practically negligible — call it flat even if directional
- **VWO 30-day data loss**: VWO resets visitor data after 30 days. Flag: *"Note: data loss due to VWO 30-day policy — results reflect last 30 days only"*
- **Control showing "No data yet"**: A previous variant is serving as the baseline (not the original control). Document this clearly in observations

---

## Decision framework

Apply this matrix to every test with results:

| Scenario | Recommendation |
|----------|----------------|
| PRIMARY goal significant (≥95% / p<0.05), GUARDRAILs flat or positive | **SHIP ✓** |
| PRIMARY goal 80–94% probability / p<0.10, trend consistent ≥2 weeks | **KEEP RUNNING →** |
| PRIMARY goal positive but a GUARDRAIL metric significantly negative | **PAUSE & ITERATE ⟳** — note the tension explicitly |
| Test running >4 weeks, no signal, traffic too low to reach MDE | **PAUSE & ITERATE ⟳** — redesign hypothesis or increase traffic |
| PRIMARY goal negative at ≥95% significance | **KILL ✗** — extract learnings |
| Data anomaly (tracking error, SRM, VWO data loss) | **PAUSE** — document anomaly, relaunch clean |
| DESIGN or DEV status | No recommendation — show setup only |

---

## Revenue / lead impact calculation

Required for every SHIP recommendation.

**Lead-gen clients (B2B, B2C lead gen):**
```
Monthly Leads Lift = (Variant CVR − Control CVR) × Monthly Sessions
Annual Leads Lift  = Monthly Leads Lift × 12
```

**eComm clients:**
```
Monthly Revenue Lift = (Variant CVR − Control CVR) × Monthly Sessions × AOV
Annual Revenue Lift  = Monthly Revenue Lift × 12
```

Always append: *"Based on current traffic levels. Assumes variant performance holds post-ship."*

---

## Anomaly documentation format

When any data quality issue exists, insert this callout block inside the observation area:

```
⚠️ DATA ANOMALY — [Anomaly Type]
What happened: [brief description of the issue]
Data affected: [which variant / which date range]
Action taken: [excluded from results / test restarted / monitoring closely]
Impact on interpretation: [results should be treated as directional only / test should be relaunched clean]
```

**Anomaly types:** Tracking error · VWO 30-day data loss · Sample ratio mismatch (SRM) · External event interference · Mid-test change · Platform policy reset

---

## Lessons from Tests synthesis

The "Lessons from [N] Tests" opening slide is a living document. Update it every deck with new learnings from any test that concluded or produced a meaningful signal.

**Format per lesson:**
`[Test ID] — [What was tested] → [What we learned]`

**Categories:**

| Category | What belongs here |
|----------|-------------------|
| **Messaging** | Copy angles, value prop framing, headline language that converted |
| **UI/UX** | Layout changes, visual hierarchy, navigation improvements that won |
| **CTA** | Button copy, placement, color, or styling patterns that worked |
| **Trust / Social Proof** | Review formats, testimonials, ratings, trust badges that lifted conversion |
| **Form Optimization** | Field sequence, length reduction, friction removal that improved submit rate |
| **Progress Meter** | Multi-step flow or funnel navigation changes |

---

## Phases

### Phase 1 — Client context

Confirm:
1. Client name and vertical (eComm / Lead-gen B2B / Lead-gen B2C)
2. Testing platform (Convert / VWO / AB Tasty / other)
3. Number of tests to document and their statuses
4. Any notable context for this period (seasonal traffic changes, site redesigns, tracking issues, external events)

### Phase 2 — Per-test data collection

For each test, collect:
- Test ID + test name
- Status (LIVE / DESIGN / DEV / Ready to go Live / Winner / PAUSED / FLAT / ARCHIVE)
- Hypothesis (full sentence — *"If we [change], then [users will] because [reason]"*)
- URL targeting
- Goals — and which is PRIMARY, which are GUARDRAIL
- Audience + traffic allocation
- Start date + planned duration
- Testing platform + significance threshold + MDE
- Variant description (1–2 sentences)
- Results per goal: sessions, conversions, CVR, and P-value or Decision Probability
- Any anomalies or data quality flags

If any required field is missing, ask before proceeding. Do not invent data.

### Phase 3 — Analysis and recommendation

For each test with results:
- Apply the statistical interpretation rules for the correct platform format
- Apply the decision matrix to assign SHIP / KEEP RUNNING / PAUSE & ITERATE / KILL
- Check all GUARDRAIL goals before confirming any positive recommendation
- Write 2–4 observation bullets per goal (specific, quantified, no vague language)
- Write the Decision + Learnings slide content
- Calculate revenue/lead impact for any SHIP recommendation

### Phase 4 — Opening section synthesis

- Update "Lessons from [N] Tests" with any new completed or directional tests
- Update the Roadmap slide to reflect current test statuses

### Phase 5 — Confirm Output Format + Branding

Before generating output, ask which format:

> "Ready to build the Test Update Deck. What format would you like?
>
> 1. **PPTX Deck** — Branded presentation slide-by-slide, best for client delivery
> 2. **Word Document (.docx)** — Written report format, best for internal briefs or async review
> 3. **Structured text** — Slide-by-slide copy labeled for paste into your Figma deck template
> 4. **Something else** — Just tell me"

Wait for the user's answer. Then ask about branding:

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours, font, and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colors, fonts, and layout rules before building.

Build based on chosen format:
- **PPTX** → invoke the pptx skill; follow the Test Update Deck structure above
- **Word doc** → invoke the docx skill; same content as prose + tables, branded
- **Structured text** → label each slide clearly (`--- SLIDE: NBC019 Setup ---`) and output copy in order
- **Other** → adapt to the format, confirm approach with user before building

### Phase 6 — Synthesis Brief

Before finalizing the deliverable, write a plain-text summary of key findings for orchestrator handoff.

**A/B Test Reporting Key Findings:**
- Test results summary: count of tests in each status (LIVE, DESIGN, DEV, PAUSED, FLAT, ARCHIVE) with recommendation distribution (SHIP/KEEP RUNNING/PAUSE & ITERATE/KILL)
- Decision confidence: which tests reached statistical significance (≥95% confidence / p<0.05 or ≥95% Decision Probability) vs. directional signals only
- Revenue/lead impact from shipped winners: total monthly/annual lift if all current SHIP recommendations are implemented
- Data quality flags: anomalies documented (tracking errors, SRM, VWO 30-day reset, external interference) and their impact on interpretation
- Lessons from Tests update: new themes identified (Messaging/CTA/UI/Form/Trust patterns) with winning test examples ready for next test ideation

**Priority for downstream skills:** Route winning test patterns (by category: Messaging, CTA, UI, etc.) to copy-messaging-audit (for broader copy pattern application) and testing-roadmap (for hypothesis iteration building on successful variations). Flag anomalies for technical investigation.

*If running standalone, share this summary with the PM or client before the Test Update Deck presentation.*

---

### Phase 7 — QA gate

Before finalizing, verify:
- [ ] Every test has a full hypothesis sentence
- [ ] Every goal is labeled PRIMARY or GUARDRAIL
- [ ] Every test with results has a RECOMMENDATION from the decision matrix
- [ ] GUARDRAIL goals checked before any SHIP call
- [ ] Revenue/lead impact calculated for every SHIP recommendation
- [ ] Data anomalies documented with the standard callout block
- [ ] "Lessons from Tests" opening slide updated
- [ ] Roadmap reflects current statuses
- [ ] No uplift percentages quoted as confirmed where P-Value > 0.10 or Decision Probability < 95%

---

## Error handling

### Missing or incomplete test data
If the user provides a test without results (status is DESIGN or DEV), document only the setup slide — hypothesis, URL targeting, goals, and variant screenshots. Skip the results and decision slides entirely. Do not prompt for data that doesn't exist yet.

### First deck for a new client
If there is no prior "Lessons from Tests" slide (new client or first deck), create a placeholder with the structure in place. Label it: *"Lessons from [N] Tests — building this as tests conclude."* Populate it with any directional signals from LIVE tests currently running.

### Stats platform unknown or data format unclear
If the user doesn't specify their testing platform, ask before interpreting results. Frequentist and Bayesian numbers look similar but mean completely different things — never assume. Ask: *"Are you using Convert / AB Tasty (P-value format) or VWO (Decision Probability format)?"*

### Incomplete goal data
If results are available for some goals but not others (e.g., one goal is still collecting data), report the available goals and note the missing ones explicitly: *"[Goal name] — data still collecting, will include next update."* Never skip a goal silently.

### Data anomaly without enough context
If the user flags an anomaly but can't explain what caused it, document it with the anomaly callout using the closest applicable type and note: *"Root cause under investigation."* Do not omit the anomaly disclosure just because the cause is unknown.

## Anti-patterns

- **Never call a winner based on sample size alone** — require both significance threshold AND minimum session count
- **Never quote uplift as confirmed if P-Value > 0.10** — use "directional positive trend"
- **Never skip the guardrail check** — a test that wins on PRIMARY but tanks a GUARDRAIL is not a clean win
- **Never omit the anomaly callout** — if data quality is compromised, say so; don't bury it in footnotes
- **Never say "the variant performed better" without quantifying** — always include CVR delta and uplift %
- **Never present VWO Decision Probabilities as P-values** — Bayesian and frequentist are fundamentally different
- **Never invent or estimate missing data** — if a number is not provided, ask

---

## Synthesis Brief

Before building the final deliverable, write a plain-text summary of key findings for orchestrator handoff.

**A/B Test Reporting Key Findings:**
- Test winner or loser designation (test ID, primary goal metric, statistical significance level p<0.05 or Decision Probability %, effect size on primary metric [+/- X.XX%], control vs. variant CVR)
- Effect size on primary metric (absolute lift in conversions, relative % uplift, confidence level, guardrail metric performance check)
- Recommended rollout decision (SHIP ✓, KEEP RUNNING →, PAUSE & ITERATE ⟳, or KILL ✗; rationale in 1-2 sentences)
- Next test hypothesis (what winning or losing insight informs the next test direction; how variant results will evolve into next iteration)
- Learnings for test roadmap (which test category was validated [Messaging/UI/CTA/Trust/Form/Progress], specific insight to carry forward, velocity impact on testing cadence)

**Priority for downstream skills:** Route findings to testing-roadmap (to prioritize next experiments based on learnings, adjust ICE scoring with new data), copy-messaging-audit (if winner was messaging-focused and should inform broader copy audit), or heatmap-scrollmap-analysis (if UX element change won and suggests broader behavioral pattern to investigate).

*If running standalone, share this summary with the operator or client team before the full deliverable.*

---

## References

- [Test Update Deck SOP & Observed Patterns](references/sop-ab-test-reporting.md) — Original SOP + patterns observed across NBC and RiseCommercial decks
- [Statistical Interpretation Guide](references/stat-interpretation-guide.md) — Full guide for both frequentist and Bayesian formats, including edge cases
