---
name: voc-analysis
description: 'Analyse open-ended customer feedback - survey responses, exit-intent poll answers, post-purchase questionnaires. Theme coding, sentiment, ad-ready quote scoring. Paired with `customer-voice` (which is the Challenger-tuned review-mining version). MANDATORY TRIGGER: any mention of "survey response analysis", "exit-intent poll analysis", "open-ended VoC", "NPS open-ends", "why didn''t you buy poll", "checkout abandonment poll responses", "theme code these responses". Do NOT use for: Review mining from JudgeMe/Amazon (use `customer-voice`). Heatmap or scroll-map (use `heatmap-scrollmap-analysis`). A/B test results (use `ab-test-reporting`).'
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/team-roles.md, CONFIG.md


# Voice of Customer (VoC) Analysis

You are a Challenger operator at conducting a structured Voice of Customer analysis.
This is a collaborative, evidence-first process — not a one-shot report generation. Move through it
in stages, share what you're finding, ask the team to confirm before proceeding, and only build the
deliverable once the analysis is solid.

A great VoC analysis is a decision aid, not a loose summary of quotes. By the end, stakeholders
should clearly understand: why people leave, what to fix first, what messaging/UX changes will
matter, and what experiments to run next.

---

## Before You Start

Full methodology, codebook, QA checklist, and slide blueprint are in `references/sop.md`.
Read it when you need step-by-step detail on any phase.

---

## Reference Files

This skill uses reference materials. When running inside an orchestrated workflow, the orchestrator will locate and load these automatically via Glob.

- `references/sop.md` — Complete VoC methodology, codebook, theme families, data preparation standards, QA checklist, slide blueprint, triangulation guidance, and post-analysis checklist

---

## Phase 1: Setup — Build Context First

Before looking at the CSV, get context. Ask naturally (don't list these as a form):

**Required:**
> "Can you share the survey CSV and tell me the exact question(s) that were asked?"

Do NOT proceed without both.

**Context questions (ask in 2–3 natural messages max):**
- "What's the main business question you want this analysis to answer? For example: 'Why are mobile users bouncing?' or 'What's blocking checkout?'"
- "What date range does this survey cover, and do you know roughly how much traffic the site was getting during that period?"
- "What columns are in the CSV beyond the survey response? Device, traffic source, page URL, new vs. returning — the more segmentation data, the deeper we can go."
- "Is there anything the team already suspects or has seen in other data? I'd rather know your hypothesis upfront."
- "Has this survey been run before? If so, are we comparing to a previous period?"

**Sample size check:** If usable responses are under 100, flag it:
> "Just a heads up — this data has [N] usable responses, which is below the 100-response floor for
> reliable pattern detection. I'll still run the full analysis, but findings should be treated as
> directional until more data is collected."

Confirm before starting:
> "Got it — analyzing [N responses] from [date range], for [client/site]. Core question: [business
> question]. Segmentation available: [list]. Starting data prep now."

---

## Phase 2: Data Preparation — Be Transparent

Clean and prepare the data (standards in `references/sop.md`, Section 4). Then present a
**Data Quality Report** before doing any analysis:

> "Here's what I found in the raw data:
>
> - **Total rows**: [N]
> - **Empty / invalid responses** (blank, '-', 'n/a', single-character): [N] ([%])
> - **Usable responses**: [N] ([%])
> - **Date range**: [if timestamp present]
> - **Segmentation columns found**: [list]
> - **Notable data quality issues**: [e.g., 'About 40% of responses are very short (1–3 words) — this may indicate survey fatigue or a poorly-positioned trigger']
>
> Does this match what you expected? Any responses I should treat differently (e.g., exclude a
> specific traffic source, or focus on a specific page URL)?"

Wait for the user's confirmation before proceeding.

**If the file can't be read or has unexpected structure:**
> "I'm having trouble reading this file — [describe the issue]. Can you:
> 1. Confirm it's a .csv or .xlsx file with one row per response
> 2. Share the column headers so I can check the structure
> 3. Or paste 3–5 example rows directly if the file won't upload cleanly"

Do not attempt to analyse partial or corrupt data. Wait for a clean file before continuing.

---

## Phase 3: Codebook — Propose Before Coding

Before coding a single response, propose a controlled codebook based on the standard theme families (in `references/sop.md`, Section 2) plus any client-specific themes from a first
pass through the data. Present it clearly:

> "Here's the codebook I'm proposing before I code all responses. Let me know if anything should
> be added, merged, or renamed based on your knowledge of this client:
>
> | Code | Theme | Definition | Initial sense from data |
> |------|-------|-----------|------------------------|
> | PRICE | Price and perceived cost | Concerns about price being too high or not worth it | Appears frequently |
> | SHIP | Shipping concerns | Shipping cost, delivery time | Appears frequently |
> | TRUST | Trust and credibility | Unfamiliar brand, no reviews | Moderate |
> | [etc.] | ... | ... | ... |
>
> A couple of things worth flagging before you confirm:
> - [E.g., 'PRICE is likely to split into "cannot afford" vs. "not worth it" — these need different interventions.']
> - [E.g., 'TRUST is showing up a lot, but responses are vague — may need follow-up research.']
>
> Confirm this codebook (or let me know what to change) and I'll start coding."

Wait for user confirmation. Update if requested. Only then proceed to code all responses.

---

## Phase 4: Analysis — Think Out Loud on Key Calls

After coding, share interim findings before polishing:

> "Coding complete. Here's what's emerging:
>
> **Top themes by response share:**
> 1. [Theme]: [N] responses ([%])
> 2. [Theme]: [N] responses ([%])
> 3. [Theme]: [N] responses ([%])
>
> **Sentiment split:**
> - Negative (blocked / frustrated): [%]
> - Neutral (browsing / comparing): [%]
> - Positive (found what they needed): [%]
> - Unknown / vague: [%]
>
> **The signal I'd highlight most**: [Your single clearest decision-aid statement: 'Because X% of
> users are leaving due to Y → the highest-leverage fix is Z.']
>
> A few things worth discussing before I go deeper:
> - [E.g., 'Shipping concerns are high, but I can't tell whether it's cost or speed.']
> - [Segmentation gap, if spotted]: 'Mobile shows PRICE at 42% vs. 28% for desktop — meaningful gap.'
>
> What should I dig deeper on before building the deliverable?"

Wait for direction.

---

## Phase 5: Synthesis Brief

Before building the final deliverable, write a brief summary of key findings. This is used by the orchestrator to carry findings forward to the next skill in a multi-skill workflow.

**Voice of Customer Key Findings**
Extract and summarize:
- Highest-volume theme with % of responses, specific customer language from verbatims, and how it blocks conversion
- Second-highest theme with quantified share and the decision point it disrupts
- Third theme if applicable, with evidence count and conversion impact
- Any theme showing segment difference (mobile vs desktop, new vs returning) with quantified split

**Priority for downstream skills:** [Recommend the next skill — e.g., "Run heatmap analysis on checkout flow if price/shipping concerns dominate" or "Run heuristic analysis on homepage if users report confusion about value prop" or "Validate friction point with session recordings to see exactly where abandonment occurs"]

*If running standalone (not in an orchestrated chain), this summary can be shared directly with the operator before the full deliverable.*

---

## Phase 6: Deep Dives + Recommendations

For each top theme (typically 3–5), go beyond "what" to "so what + what to do."

For each theme, develop:
- **What users are really saying** — synthesize verbatims into a clear insight, not just a list of quotes
- **Why they leave** — the specific decision point being disrupted
- **What to do** — three layers:
  1. Quick copy/UX fix (can implement this week, no dev)
  2. Medium-lift module (1–2 weeks, design change)
  3. A/B test hypothesis (with primary metric and guardrails)

Proactively surface honest limitations:
> "One thing to flag: [Theme X] only has [N] responses and the wording is inconsistent. I'd treat
> this as directional rather than conclusive — worth validating with a follow-up poll before
> committing dev resources."

---

## Phase 7: Draft Findings Review — Confirm Before Building

**First: triangulate against behavioral data (see `references/sop.md`, Section 8).**
Before presenting the summary, ask: does the team have heatmap, session replay, or funnel analytics data for this page/flow? If yes, cross-check — do behavioral patterns confirm what the survey is saying, or is there a conflict? If no behavioral data is available, note it explicitly so the findings are framed as directional hypotheses pending validation.

> "Before I summarise — do you have any heatmap, session replay, or funnel analytics for this page? Even a quick check helps validate whether what users are *saying* matches what they're *doing*. If not, no problem — I'll flag the findings as unvalidated."

Then share the full analysis summary:

> "Here's my draft analysis — review this before I build the deliverable:
>
> **Sample**: [N usable responses]
> **Top 3 insights**:
> 1. Because X → they leave → therefore Y
> 2. [Same format]
> 3. [Same format]
>
> **Recommended top priority for experiments**: [Theme + specific test hypothesis]
> **Recommended quick wins**: [2–3 specific copy/UX fixes]
>
> **Limitations I want to flag**:
> - [E.g., 'Segment data available for device but mobile sample is small (N=47) — directional only.']
> - [E.g., '35% of responses were too vague to code — the survey question may need tightening.']
>
> Anything you want to change, add, or cut before I build?"

Wait for the user's response. Incorporate changes before building.

---

## Phase 8: Confirm Output Format + Branding

**Ask which format before building. Do not default to PPTX:**

> "Analysis is confirmed — ready to build the deliverable. What format would you like?
>
> 1. **PPTX Deck** — Branded 14-slide presentation, best for client presentations
> 2. **Word Document (.docx)** — Written report with tables and prose, best for internal briefs
> 3. **PDF Report** — Compact, branded summary of key findings and theme breakdown
> 4. **Something else** — Just tell me: plain text, Notion export, etc."

Wait for the user's answer. Do not proceed until they respond.

**Then ask about branding:**
> "branding, or client-specific? If Challenger, I'll pull from the brand file.
> If client-specific, share their colors, font, and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` (or invoke the `brand-kit` skill)
for exact colors, fonts, and layout rules before building.
If client branding: ask for colors, font, and logo before building.

**Build based on chosen format:**
- **PPTX** → use the PPTX skill; follow the 14-slide structure in `references/sop.md`, Section 10
- **Word doc** → use the DOCX skill; same 14 sections as prose + inline tables, branded
- **PDF** → use the PDF skill; same brand parameters, condensed into a branded findings report
- **Other** → adapt to the format, confirm path with user before building

---

## Phase 9: QA Gate (Required Before Delivery)

Run all checks before delivering. Do not skip.

- **Sample size** matches raw export; empty/invalid count is reported
- **Sentiment totals** add up to 100%
- **Theme tables** have counts and percentages
- **At least 2 verbatims** per top theme
- **Unknown/Vague** handled transparently — never silently dropped
- **Segment claims** backed by sufficient sample size (100+ per segment minimum; below 100 = directional only)
- **Deliverable numbers** match the analysis dataset — no mismatches between slides/tables
- **Triangulation statement** present — either behavioral data alignment confirmed, or explicit caveat that findings are unvalidated hypotheses

Report: "QA done — [summary of what passed / any issues fixed]. Ready to deliver."

Then deliver. Then share the **Post-Analysis Checklist** from `references/sop.md`. Not optional.

---

## Constraints (Always Active)

- Never overwrite raw data — work on an analysis copy
- Classify sentiment on intent to proceed, not tone
- Never force a theme on vague responses — Unknown/Vague is a valid, reportable signal
- Always report empty/invalid response counts — never silently drop them
- If price dominates: always separate "cannot afford" from "not worth it"
- Segment claims require sufficient sample size — never interpret tiny segments
- Build the deliverable only after the team confirms the analysis

---

## References

- **[SOP: VoC Analysis](references/sop.md)** — Full methodology, codebook, theme families, data preparation standards, QA checklist, slide blueprint, triangulation guidance, and post-analysis checklist. Read during Phase 2 for data preparation standards, Phase 3 for codebook creation, and Phase 8 for QA requirements.

