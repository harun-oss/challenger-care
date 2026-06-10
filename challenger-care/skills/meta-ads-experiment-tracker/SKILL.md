---
name: meta-ads-experiment-tracker
description: Logs experiment hypotheses before launch, records results + audience learnings after, synthesises patterns. Reads/writes to assets/experiment-log.md. MANDATORY TRIGGER: any mention of "log an experiment", "experiment log", "record experiment results", "what experiments have we run", "experiment learnings", "Meta experiment history". Do NOT use for: Launching experiments (use `meta-ads-creative-testing`). Writing copy (use `meta-ads-copywriting`).
---

> **Permission tier:** generate · **Tools/context:** assets/voc/quote-library.md, assets/team-roles.md, assets/experiment-log.md, CONFIG.md


# Meta Ads Experiment Tracker

## What this skill does

This skill logs experiment hypotheses before launch and records audience learnings after each experiment concludes — building a structured knowledge base for each client that compounds over time.

The Change Log inside `meta-ads-creative-testing` records **actions** (pause, promote, move to ADV+). This skill records **learnings** — what each experiment revealed about the audience, and how that shapes what to test next.

Use this skill when:
- About to launch a new experiment and want to formally record the hypothesis
- An experiment has concluded and you want to log the result and learning
- Planning the next experiment and want to pull up what's already been learned
- Producing the creative learnings section for the monthly report

---

## Phase 1 — What Are We Doing?

Ask:

> "Are you logging a new experiment before launch, recording the results of a completed experiment, or pulling up the experiment history for a client?"

Route to the appropriate phase based on the answer.

---

## Phase 2 — Pre-Launch Hypothesis Log

Run this before a new experiment goes live. It takes 2 minutes and creates the anchor for the post-experiment learning.

Ask one question at a time:

1. **Client name**
2. **Experiment number** — what number is this? (Check the history: if no prior log exists for this client, this is Experiment #1)
3. **What are we testing?** — the variable. One thing only. (e.g., Hook angle: curiosity vs. pain-point / Format: static vs. video / Talent: founder vs. customer testimonial)
4. **What are we holding constant?** — the control elements. (e.g., Same product, same primary text, same offer)
5. **Hypothesis** — finish this sentence: "We believe that [variation] will outperform [control] because [reason based on audience insight or prior data]."
6. **Success metric** — what does winning look like? (e.g., CPA below $X / ROAS above X / CTR above X%)
7. **Launch date and planned 7-day review date**
8. **Number of variations**

Produce the pre-launch log entry. Read `references/experiment-log-template.md` for the exact format.

After logging: "Pre-launch log saved. When the 7-day review is complete, come back to log the result — one sentence about what the audience told us."

---

## Phase 3 — Post-Experiment Results Log

Run this after the 7-day review (or when the experiment is fully concluded). Pair it with whatever decisions were made in `meta-ads-creative-testing`.

Ask one question at a time:

1. **Client and experiment number** — which experiment are we closing out?
2. **Winner** — which variation won, or was it inconclusive?
3. **Key metrics for each variation** — CPA or ROAS per variation (not the whole account — this specific DCT ad set)
4. **Action taken** — promoted to legacy / paused / moved to ADV+ / still running
5. **The learning** — the most important question: *what did this experiment tell us about the audience?*

   Push the operator past surface-level answers. "The curiosity hook won" is not a learning. "Our audience responds to curiosity hooks because they don't yet know [product] exists — they need to be pulled into awareness before we can sell" is a learning. If the operator can't articulate it, offer a draft based on the result and ask them to confirm or correct.
   
   Audience insights to look for: awareness level, primary motivation (price/outcome/identity/status), objection type, creative fatigue signals, persona shift, seasonality patterns.

6. **Hypothesis for next experiment** — what does this result suggest we should test next?

Produce the post-experiment log entry. Read `references/experiment-log-template.md` for the exact format.

---

## Phase 4 — Pattern Synthesis (3+ Experiments)

After 3 or more experiments have been logged for a client, this phase synthesises what's been learned into strategic patterns.

Run this when:
- An AM asks "what have we learned from our experiments so far?"
- Preparing the creative strategy section of the monthly deck
- Planning what to test in month 4+

Ask: **"Share the results from your last [N] experiments — either from the log or from memory."**

Then identify patterns across the data:

**Format patterns:** Does static or video consistently outperform? Is one format always inconclusive?

**Hook angle patterns:** Which hook types have won (pain-point / curiosity / social proof / aspirational)? Which have consistently underperformed?

**Audience signal:** What do the cumulative results tell us about the customer's awareness level and primary motivation? Are they price-driven, outcome-driven, identity-driven?

**Fatigue signals:** Which creative elements have run for 90+ days and are due for rotation?

**Next experiment recommendation:** Based on the pattern, what's the single highest-value hypothesis to test next?

Read `references/experiment-log-template.md` → Pattern Synthesis section for the structured output format.

---

## Phase 5 — Output Format + Branding (if DOCX)

First, ask:

> "Log ready. How would you like it delivered?
>
> 1. **Google Sheets row** — values formatted to paste into the experiment log spreadsheet
> 2. **Notion entry** — structured entry for a client Notion knowledge base
> 3. **DOCX** — written experiment summary (useful for monthly report or client handoff)
> 4. **Slack update** — brief learning summary formatted for Challenger's internal channel"

For **Google Sheets row**: produce the values in column order per `references/experiment-log-template.md`. The AM pastes these directly into the next empty row of the experiment log.

For **DOCX**:
- Ask: "branding or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."
- If branding confirmed: read `../../../growthit-brand/assets/growthit-brand.md` before invoking the docx skill.
- Structure as: Experiment Overview → Result → Learning → Next Hypothesis.

For **Slack**: one short paragraph. State what was tested, what won, and the single most important thing learned. Max 4 lines.

For **Pattern Synthesis output** (Phase 4): always produce as a structured written summary — Hook Patterns → Format Patterns → Audience Signal → Next Experiment Recommendation. Can be DOCX or pasted into the monthly deck. If DOCX: ask format and branding the same way.

---

## Synthesis Brief

Before building the final deliverable, write a plain-text summary of key findings for orchestrator handoff.

**Meta Ads Experiment Tracker Key Findings:**
- Experiments logged: [Total experiment count to date, list experiment numbers / names — pre-launch hypotheses recorded, post-experiment results recorded]
- Win/loss record: [Breakdown of passed vs. failed experiments: X won (promoted to legacy), Y inconclusive (still running), Z failed (paused/moved to ADV+) — success rate and trend]
- Key learning per experiment: [For each logged experiment, the audience insight revealed — NOT just "curiosity hooks won" but WHY (e.g., "audience needs awareness pull before selling" / "price-sensitive personas respond to urgency" / "founder authority builds trust with new buyers")]
- Pattern emerging across tests (if 3+ experiments): [Hook angles that consistently win / Format preferences / Audience awareness/motivation signal / Creative fatigue timeline — each pattern grounded in 2+ experiments]
- Hypothesis validation track record: [Which pre-launch hypotheses were correct / wrong — confidence level for next hypothesis]
- Next highest-value experiment recommended: [Specific single test to run based on pattern synthesis — variable, control, and hypothesis grounded in learnings from prior experiments]

**Priority for downstream skills:** Next: Validated hypotheses → meta-ads-creative-brief (brief asset creation for next month's test) → meta-ads-creative-testing (launch confirmed hypothesis) → Cycle back for 7-day review and post-experiment logging

*If running standalone (not in an orchestrated chain), share experiment history and pattern synthesis with AM to build strategic momentum for future testing — learnings compound across months.*

---

## QA Gate

Before delivering any log entry:

- [ ] Hypothesis is a full sentence: "We believe [X] will outperform [Y] because [Z]" — not just "testing curiosity hooks"
- [ ] Learning is an audience insight, not just a result statement — "curiosity hooks won" ≠ a learning
- [ ] Post-experiment entry includes the action taken (promoted / paused / ADV+) — connects back to the Change Log
- [ ] Next hypothesis is specific — not "test more UGC" but "test founder-led UGC against customer testimonial UGC using the same hook line"
- [ ] Pattern synthesis (Phase 4): each pattern is supported by at least 2 data points — no pattern from a single experiment

---

## Reference Files

This skill uses reference materials. The orchestrator will locate and load these automatically via Glob.

- `references/experiment-log-template.md` — Google Sheets column structure, pre-launch and post-experiment entry format, pattern synthesis output template. Needed during Phases 2, 3, and 4.
- `references/copy-frameworks.md` (from meta-ads-copywriting) — Hook angle table and video script frameworks help ground the next hypothesis in a specific creative approach. Needed during Phase 4 when recommending the next experiment.
