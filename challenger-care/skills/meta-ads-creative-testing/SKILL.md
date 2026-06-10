---
name: meta-ads-creative-testing
description: 'Weekly creative testing cadence · 1 DCT experiment per month, 7-day pause rules, move non-performers to ASC+/ADV+, maintain legacy library. MANDATORY TRIGGER: any mention of "launch a Meta experiment", "run a Meta DCT", "weekly creative testing", "Meta DCT", "launch new ads on Meta", "weekly Meta creative cadence", "Flexible Ads experiment". Do NOT use for: Initial campaign setup (use `meta-ads-campaign-build`). Scaling decisions. The kickoff methodology deck (not in our port).'
---

> **Permission tier:** execute · **Tools/context:** assets/brand-strategy.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/team-roles.md, CONFIG.md


# Meta Ads Creative Testing

**Owner:** the operator
**Cadence:** Monthly experiment launch + weekly performance monitoring
**Prerequisite:** Campaign built, pixel verified, at least one prior experiment for control data (or strong benchmark creative from value prop exercise)

---

## Phase 1: Experiment Planning

Before launching a new experiment, define:

1. **Experiment number and type:** What are we testing this month?
   - Ads Variety (new images/videos — most common for early months)
   - Copy Test (new headlines/primary texts — keep creative constant)
   - Format Test (static vs. video vs. carousel)
   - Angle Test (new messaging angle vs. control)

2. **Control elements:** What is the current best-performing headline and primary text?
   - Pull from the main campaign's top-performing ad in the last 30 days
   - If month 1 (no control data): use the strongest hook from the value prop exercise

3. **New elements to test:** What are we introducing this month?
   - 4–5 new images or videos
   - 2 new headlines (+ 1 control)
   - 2 new primary texts (+ 1 control)

4. **Permutation check:**
   - Headlines × Primary Texts × Images/Videos ≤ 20
   - If over: reduce image/video count first

Naming convention: `[Client] | Meta Experiment #[N] | [Month] | [Type]`

---

## Phase 2: Creative Preparation

> For asset specifications, naming conventions, and the Canva workflow, read `references/creative-testing-workflow.md`.

Before building the DCT in Ads Manager:
- Build or source all creative assets in Canva Pro (account, Jim's access)
- Prepare the Ad Creative Overview deck to present assets to Challenger for approval
- Template: [[Template] - Ad Creative Overview](https://docs.google.com/presentation/d/1FIZl6mf46S8n-YHtYLPZhbg3RDBKPk0lBpy-STTn_C8/edit)
- Get execute_tier_approver approval before uploading to Ads Manager

**Do not launch any new creative without execute_tier_approver sign-off.**

---

## Phase 3: DCT Launch

1. Create a new ad set inside the main campaign
2. Name it per the naming convention
3. Set budget: minimum $10/day, recommended $15–25/day for faster data
4. Upload all creative assets
5. Enter all headlines and primary texts
6. Verify permutation count ≤ 20
7. Set destination URL + CTA
8. Review and publish

**Timing:** Launch the experiment at the beginning of the week (Monday or Tuesday) so the 7-day review falls on the same day the following week.

---

## Phase 4: 7-Day Performance Review

**After 7 days,** check each experiment DCT and apply the decision rules:

### Pause Rules

**Pause the DCT if:**
- Zero purchases (or zero leads) generated in 7 days
- CPA or ROAS is 2× worse than the account average over the same period

**Keep running the DCT if:**
- CPA/ROAS is within 2× of the account average — more data needed
- The DCT is within first 3 days — too early to evaluate

**Promote to legacy if:**
- CPA or ROAS is better than the account average — move winning creative to the main campaign's evergreen ad set

### ASC+ / ADV+ Handoff

Creative that gets paused doesn't disappear. Move it to the ADV+ campaign for a second chance:
- Creative that generated no purchases in the main campaign sometimes finds an audience in ADV+
- Only move to ADV+ if the account is 60+ days old and ADV+ is already set up
- Document what was moved and when in the Change Log

### Change Log Update

Update the account Change Log after every experiment review:

| Date | Action | Campaign/Ad Set | Reason |
|---|---|---|---|
| [Date] | Paused | Experiment #2 — Lifestyle images | 7 days, 0 purchases |
| [Date] | Promoted | Headline "Stop wasting time on X" | 40% below account CPA |
| [Date] | Moved to ADV+ | Experiment #1 paused creative | Second chance on broader audience |

---

## Phase 5: Legacy Ad Library Management

The main campaign's evergreen ad set (legacy) accumulates winning creative over time. Manage it actively:

**Add to legacy when:**
- A DCT headline, primary text, or image outperforms the account average by 20%+
- A creative element has run for 30+ days and maintained performance

**Remove from legacy when:**
- A creative has been running for 90+ days with declining CTR (creative fatigue)
- CPA has risen 30%+ over the past 30-day rolling average for that specific creative

**Target: 3–8 active legacy ads** in the evergreen set. Too few = limited coverage. Too many = budget fragmentation.

---

## Phase 6: Reference Files

This skill uses reference materials. The orchestrator will locate and load these automatically via Glob.

- `references/creative-testing-workflow.md` — Asset specifications, naming conventions, Canva Pro workflow, execute_tier_approver approval processes, and Ad Creative Overview brief structure. Needed during Phase 2 before preparing creative.

---

## Phase 7: Output Format + Branding

> "Experiment ready [or experiment reviewed]. What format would you like for the output?
>
> 1. **DOCX Report** — written experiment summary: what was launched/paused/promoted, performance vs. account average, next steps
> 2. **Slack update** — brief formatted summary ready to share in Challenger's internal channel
> 3. **Verbal summary** — confirm experiment status in this conversation"

> "branding, or client-specific? If Challenger, I'll pull from the brand file."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colours, fonts, and layout rules before building output.

Build based on chosen format:
- **DOCX** → invoke the docx skill; apply branding; structure as: experiment overview → 7-day results → decisions made → legacy updates → next month plan
- **Slack update** → brief status with creative decisions and next experiment plan
- **Verbal** → walk through decisions in this conversation

---

## Synthesis Brief

Before building the final deliverable, write a plain-text summary of key findings for orchestrator handoff.

**Meta Ads Creative Testing Key Findings:**
- Winning creative identified: [Specific creative element(s) that won — headline ID/text, primary text ID/text, image/video ID or angle name — with metric improvement (CPA/ROAS % vs. account average)]
- Fatigue alerts triggered: [Any creative elements running 90+ days with declining CTR or CPA rise 30%+ — rotation candidates for legacy ad set / next experiment]
- Next creative directions recommended: [Based on 7-day results, recommend what to test in next experiment — specific hook angle, format, or audience angle to pursue]
- Budget implications noted: [Scaling recommendations (if winner ready to scale, budget increase suggestion) / Pausing recommendations (which DCTs to pause, which budget to reallocate)]
- Experiment performance vs. benchmarks: [How this month's winners compare to account average — X% below CPA / X% above ROAS — confidence level for promotion to legacy]
- Change Log updated and legacy inventory reviewed: [All actions logged (Paused / Promoted / Moved to ADV+) with dates and rationale — current active legacy count noted]

**Priority for downstream skills:** Next: meta-ads-experiment-tracker (log post-experiment learning and audience insights if experiment complete) → Plan Month N+1 experiment hypothesis based on winning angles → Prepare next month's meta-ads-creative-brief if new assets needed

*If running standalone (not in an orchestrated chain), communicate 7-day review decisions, winning creative elements, and recommended next hypothesis to AM/client immediately before planning next experiment.*

---

## QA Gate

Before delivering:
- [ ] Experiment name follows naming convention
- [ ] Permutation count ≤ 20 confirmed
- [ ] Client creative approval obtained before launch (or documented as pending)
- [ ] 7-day review applied decision rules (pause / keep / promote)
- [ ] Paused creative moved to ADV+ (if ADV+ is set up)
- [ ] Change Log updated with all actions taken
- [ ] Legacy ad set reviewed for fatigue
