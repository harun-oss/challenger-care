---
name: testing-roadmap
description: Builds and maintains a prioritized test backlog using ICE scoring (Impact x Confidence x Ease). Applies 40/40/20 portfolio rule (Quick Wins / Core Tests / Big Swings). Pairs with `test-price-claim` (single-test designer). MANDATORY TRIGGER: any mention of "ICE score", "test prioritization", "testing roadmap", "test backlog", "sprint planning for CRO", "which tests to run next", "rank test hypotheses". Do NOT use for: Reporting A/B test results (use `ab-test-reporting`). Designing a single test (use `test-price-claim`). User testing (use `user-testing`).
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/voc/quote-library.md, assets/goals-targets.md, assets/team-roles.md, CONFIG.md


# Testing Roadmap & Prioritization Skill

## What this skill does

This skill helps PMs build, score, and maintain a prioritized test backlog for any CRO client. It takes test ideas from any source — heuristic audits, VoC survey data, heatmaps, analytics, copy audits, competitive analysis — applies ICE scoring, ensures portfolio balance, and outputs a roadmap organized for client calls and sprint planning.

Output options:
- **Roadmap table** — structured text or XLSX with test IDs, ICE scores, funnel stage, and status
- **Deck-ready roadmap slide** — formatted for the Test Update Deck opening section (see ab-test-reporting skill)
- **Sprint plan** — prioritized list of what to launch next with rationale

---

## The research-to-roadmap pipeline

Test ideas never come from gut instinct alone. Every item on the roadmap should be traceable to a research source:

| Research source | What it identifies | Priority |
|-----------------|-------------------|----------|
| Heuristic analysis (Baymard) | UX friction, hierarchy failures, trust gaps | High — directly observable |
| VoC / exit-intent survey | Language, objections, confusion points | High — customer voice |
| Heatmap / scroll map | Attention drop-off, ignored CTAs, rage clicks | High — behavioral proof |
| Form abandonment analytics | Specific friction points in conversion flow | High — quantified drop |
| Competitive analysis | Missing trust signals, copy angles, offer structures | Medium |
| Analytics / GA4 | High-traffic/low-converting pages, device splits | Medium |
| Copy/messaging audit | Weak copy, missing proof, vague CTAs | Medium |
| Team brainstorm / intuition | Untested hypotheses | Low — must be validated by research |

**rule:** Every test hypothesis must reference at least one research source. No research, no test.

---

## ICE scoring

ICE = **Impact × Confidence × Ease** — each scored 1–10.

### Scoring definitions

**Impact (1–10): How much will this test move the needle if it wins?**

| Score | Definition |
|-------|-----------|
| 9–10 | Affects the highest-traffic page / primary conversion action / sitewide element |
| 7–8 | Affects a key page or goal with significant traffic |
| 5–6 | Affects a secondary page or micro-conversion |
| 3–4 | Affects a low-traffic page or minor element |
| 1–2 | Minimal traffic or very small element change |

Consider: monthly sessions on the target page × estimated CVR delta × business value per conversion.

**Confidence (1–10): How strongly does research support this hypothesis?**

| Score | Definition |
|-------|-----------|
| 9–10 | Multiple research sources align; direct customer language available; proven pattern in competitive analysis |
| 7–8 | At least 2 research sources support it; clear behavioral signal (heatmap + VoC) |
| 5–6 | Single research source; directional signal but not conclusive |
| 3–4 | Team observation or analyst hypothesis; no direct user data |
| 1–2 | Pure speculation or gut feel |

**Ease (1–10): How easy is this to design and build?**

| Score | Definition |
|-------|-----------|
| 9–10 | Copy change only — no design or dev needed |
| 7–8 | Design change only — minor dev (CSS/JS tweak) |
| 5–6 | New component or section — standard dev work |
| 3–4 | Significant dev work — new page template, new functionality |
| 1–2 | Major dev work — multi-system integration, back-end changes |

### ICE calculation

```
ICE Score = Impact × Confidence × Ease
```

Maximum possible: 10 × 10 × 10 = 1,000
typical range: 50–700

### Scoring best practices

- **Score independently before comparing** — don't adjust scores to achieve a predetermined ranking
- **Score with the team when possible** — PM + Strategist + Designer/Dev each score independently, then average
- **Reassess regularly** — scores change as research evolves, traffic shifts, or earlier tests provide new data
- **Don't treat ICE as the only filter** — use it to sort, then apply portfolio balance (see below)

---

## Portfolio balance

A pure ICE ranking produces a roadmap full of similar, medium-complexity tests. explicitly balances the test portfolio across three categories:

| Category | Target mix | Description |
|----------|-----------|-------------|
| **Quick Wins** | ~40% of roadmap | High Ease (7–10), low dev burden, fast to launch — copy changes, CTA tests, trust signal additions |
| **Core Tests** | ~40% of roadmap | Medium complexity, moderate Impact + Confidence — the bulk of the learning agenda |
| **Big Swings** | ~20% of roadmap | Lower Ease (1–4), high Impact — full page redesigns, flow changes, new offer structures. These take longer but produce the biggest learnings |

**Why 20% big swings?** Quick wins and core tests optimize within the current UX paradigm. Big swings challenge the paradigm itself. Clients who only run quick wins plateau.

---

## Test roadmap structure

### Funnel stage tagging

Every test must be tagged to its funnel stage:

| Stage | Description | Examples |
|-------|-------------|---------|
| **Awareness / Landing** | First impression, hero, headline, above-fold | Homepage, ad landing pages |
| **Consideration / Information** | Value prop, product detail, social proof | PDP, About, Features pages |
| **Intent / Conversion** | CTA, form, checkout | CTA button, form fields, pricing |
| **Trust** | Reviews, testimonials, trust badges | Any page element |
| **Retention / Post-conversion** | Thank you page, onboarding | Post-submit pages |

### Test hypothesis format

Every test hypothesis follows this structure:

```
If we [specific change],
then [specific user behavior / metric],
because [research-backed reason].
```

Good example: *"If we replace the generic 'Submit' button with 'Get My Free Quote', then Clicks Yes will increase because VoC data shows users associate 'Submit' with junk mail and generic forms."*

Bad example: *"If we change the CTA button, then conversions will go up because our button doesn't look good."*

### Roadmap item fields

| Field | Description |
|-------|-------------|
| Test ID | Client prefix + sequential number (e.g. NBC020, RISE009) |
| Test Name | Short descriptive name (e.g. "Hero CTA Copy — Benefit Forward") |
| Funnel Stage | From the stage taxonomy above |
| Hypothesis | Full if/then/because sentence |
| Research Sources | Which research inputs support this idea |
| URL Targeting | Page(s) to target |
| Primary Goal | The one metric this test is designed to move |
| Guardrail Goals | Metrics to watch for negative effects |
| Category | Quick Win / Core Test / Big Swing |
| Impact (1–10) | |
| Confidence (1–10) | |
| Ease (1–10) | |
| ICE Score | Impact × Confidence × Ease |
| Status | Ideation / Planning / Design / Dev / Ready / Live / Paused / Winner / Archive |
| Notes | Dependencies, blockers, open questions |

---

## roadmap slide format (for Test Update Deck)

The roadmap opening slide in the Test Update Deck uses status-grouped bullets:

```
🟢 Pushing Live Today: [Test Name] — [one-line description]
🔵 Dev: [Test Name]
🎨 Design: [Test Name]
📋 Planning: [Test Name]
💡 Ideation: [Test Name]
⏸  On Hold: [Test Name] — [reason: awaiting client asset / dependency / seasonal]
```

Top 3 tests in each active status (Dev, Design, Planning) should be ranked by ICE score.

---

## Phases

### Phase 1 — Client context

Confirm:
1. Client name and vertical
2. Current funnel architecture (what pages / steps exist)
3. Primary conversion goal (what counts as a conversion)
4. Available traffic (sessions/month to key pages)
5. Testing platform and current capacity (how many tests can run simultaneously)
6. Existing test backlog (what's already been tested, what's live, what's coming)

### Phase 2 — Research inventory

Ask: "What research do we have available for this client?"

For each available source, identify the test ideas it suggests:
- Heuristic analysis → friction points and UX gaps
- VoC data → objections, confusion, missing information
- Heatmap/scroll map → attention and click patterns
- Form abandonment → specific step drop-off
- Analytics → high-traffic, low-converting pages
- Copy audit → weak copy, missing proof elements
- Competitive analysis → gaps vs. competitors

If little or no research exists, recommend completing a heuristic analysis or VoC survey before building a roadmap — tests without research backing have lower Confidence scores and higher chance of inconclusive results.

### Phase 3 — Hypothesis generation

For each identified opportunity:
1. Write the full if/then/because hypothesis
2. Assign funnel stage
3. Identify primary and guardrail goals
4. Tag research sources
5. Assign category (Quick Win / Core Test / Big Swing)

### Phase 4 — ICE scoring

Score each item on Impact, Confidence, and Ease (1–10 each). Calculate ICE = I × C × E.

When scoring Impact, use actual traffic data when available:
- **Preferred when available:** pull live GA4 sessions per target page via Composio (see the live MCP connectors) — gives current-month traffic without asking the user to look it up. Fall back to user-provided traffic if Composio is not connected.
- Get monthly sessions to the target page
- Estimate potential CVR delta based on comparable tests
- Estimate business value per conversion (lead value, AOV)

### Phase 5 — Portfolio balance check

After ranking by ICE:
1. Check the mix: is it ~40% Quick Wins / 40% Core / 20% Big Swings?
2. If overweighted toward Quick Wins: flag at least 1–2 Big Swing tests for the roadmap
3. If overweighted toward Big Swings: ensure near-term velocity with Quick Wins
4. Check funnel coverage: are tests distributed across stages, or all concentrated on one page?

### Phase 6 — Synthesis Brief

Before finalizing the roadmap output, write a brief summary of key findings. This is used by the orchestrator to carry insights forward to test execution.

**Testing Roadmap Key Findings**
Extract and summarize:
- Highest-priority test (ID + name) with Impact and Confidence scores, primary research sources, and what it measures
- Highest-confidence test with research sources cited (heuristic analysis, VoC survey, heatmap — name the specific finding)
- Top Quick Win (Ease 7+) that can launch this week and address a key friction point from research
- One Big Swing (Ease ≤4) that maintains portfolio balance and tests a paradigm-shift hypothesis

**Priority for downstream skills:** [Recommend the next phase — e.g., "AB test execution: prioritize tests with 2+ research sources and Confidence ≥7; allocate design capacity for Big Swings simultaneously" or "If roadmap is light on hypotheses, run additional heuristic or VoC research before execution"]

*If running standalone (not in an orchestrated chain), this roadmap can be shared directly with the PM for sprint planning and capacity allocation.*

### Phase 7 — Confirm Output Format + Branding

Ask which format before building:

> "Ready to output the roadmap. What format would you like?
>
> 1. **Roadmap table (XLSX)** — Full scored backlog with all fields, best for ongoing sprint planning
> 2. **Roadmap table (text)** — Same content in plain text, best for Notion or inline sharing
> 3. **Deck-ready roadmap slide** — Formatted for the Test Update Deck opening roadmap section
> 4. **Sprint plan** — Focused view of what to build/launch next and why
> 5. **Something else** — Just tell me"

Wait for the user's answer. Then ask about branding:

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colors, fonts, and layout rules before building.

Build based on chosen format:
- **XLSX** → invoke the xlsx skill; include all roadmap item fields plus a summary tab
- **Text table** → output as Markdown table; no skill needed
- **Deck slide** → format as the roadmap slide (see slide format above); for full PPTX invoke the pptx skill
- **Sprint plan** → plain text or DOCX via the docx skill; confirm with user
- **Other** → adapt to the format, confirm approach before building

---

## QA Gate

Before delivering the final roadmap, verify:
- [ ] **Research traceability:** Every test (Confidence 5+) cites ≥1 research source; Confidence 3–4 items flagged as pending research validation
- [ ] **Confidence defensibility:** Confidence 7+ supported by ≥2 research sources OR direct customer language; Confidence 5–6 backed by single source with observable behavioral signal; Confidence 3–4 are analyst hypotheses pending VoC/heatmap validation
- [ ] **Portfolio balance:** Quick Wins ~40%, Core Tests ~40%, Big Swings ~20% (or documented exception if <5 items total; single Big Swing minimum if 5+)
- [ ] **Funnel coverage:** Tests distributed across ≥2 funnel stages (not all on one page); high-traffic pages have 2+ tests in backlog
- [ ] **Impact calculation verified:** For tests with traffic data, documented as: [monthly sessions] × [estimated CVR delta based on comparable test] = [quantified revenue impact]; estimated impacts flagged clearly
- [ ] **Dependencies explicit:** Conflicting tests (same URL, incompatible changes) noted with "On Hold — dependency on [Test ID]"; sequential dependencies documented in Notes field
- [ ] **Synthesis brief complete:** Key findings extracted with test IDs, Confidence/Impact scores, research sources cited, and downstream priority stated (if in orchestrated chain)
- [ ] **Output format matches request:** Table / Deck slide / Sprint plan delivered in requested format with correct branding

---

## ICE scoring pitfalls to avoid

- **Don't inflate Confidence to justify a pet test** — if there's no research, score it low (3–4) and note what research would increase confidence
- **Don't treat all Ease 10s as equivalent** — a copy tweak on a homepage and a copy tweak on a low-traffic page are both Ease 10 but wildly different Impact
- **Don't stack the roadmap with high-Ease, low-Impact tests** — velocity without learning is just change for change's sake
- **Don't ignore dependencies** — if Test B requires Test A to ship first, note this explicitly
- **Don't let high ICE override common sense** — a test that would confuse Challenger or require a 3-month dev engagement isn't really "Ease 8"
- **Don't set-and-forget the roadmap** — reassess after every test completes; learnings should feed back into scores and new hypotheses

---

## Anti-patterns

- **Never add a test to the roadmap without a research source** — "because it looks good" is not a reason
- **Never build a roadmap of only quick wins** — clients plateau; 20% big swings are non-negotiable for long-term growth
- **Never let the roadmap go stale** — update statuses and scores after every team review
- **Never score the same person's gut feel as "Confidence 8"** — that's a 3 at best, pending research

---

## Error handling

### No research available
If Challenger has no completed research (no heuristic analysis, VoC, heatmaps, or analytics data), do not block the roadmap — instead, cap Confidence scores at 4 for all ideas and add a note to each: *"Confidence capped — no research available yet."* Recommend completing a heuristic analysis or VoC survey as the first action item. Never assign Confidence 7+ to any test that has no user data behind it.

### No traffic data available for Impact scoring
If monthly session counts are unknown, use one of these fallbacks:
- Ask Challenger to check Google Analytics for the target page's monthly sessions
- If unavailable, estimate relative Impact as High/Medium/Low (not a number) and note: *"Impact estimated — verify with GA4 data"*
- Flag the estimate clearly in the roadmap so it gets updated once data is available

### Only 1–2 test ideas
If the PM provides fewer than 3 test ideas, flag the thin backlog explicitly: *"This roadmap is underpopulated. Before sprint planning, recommend completing [research type] to generate more hypotheses."* Still score and rank the available ideas, but note the gap.

### Dependency conflict
If two test ideas cannot run simultaneously (e.g., both target the same URL with conflicting changes), flag the conflict and note which should run first. Mark the blocked test as "On Hold — dependency on [Test ID]."

---

## References

- [ICE Scoring Framework & Best Practices](references/ice-scoring-guide.md) — Full scoring guide with worked examples
- [Research Sources Reference](references/research-sources.md) — How each research type maps to test opportunities
