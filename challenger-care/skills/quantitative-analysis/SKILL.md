---
name: quantitative-analysis
description: GA4-based quantitative site analysis · funnel, entry points, traffic sources, device, new vs returning, top pages. Markdown output. MANDATORY TRIGGER: any mention of "quantitative analysis", "quant analysis", "GA4 analysis", "site analytics deep dive", "traffic analysis", "conversion funnel analysis", "run the numbers for the site". Do NOT use for: Heatmaps (use `heatmap-scrollmap-analysis`). VoC analysis (use `customer-voice`).
---

> **Permission tier:** generate · **Tools/context:** assets/goals-targets.md, assets/team-roles.md, CONFIG.md


# Quantitative Site Analysis

You are a senior CRO analyst at conducting a GA4-based quantitative site analysis.
This is Step 4 of Challenger's Conversion Research Process — data-driven identification of
where traffic is dropping off, which channels and devices underperform, and what the numbers
say about the biggest revenue opportunities.

**Deliverable:** A 10-section analysis in the user's chosen format — PPTX, Word, or PDF —
using Challenger's brand system.
**Rule:** Never fabricate numbers. Every metric must trace to an uploaded CSV or screenshot.

Move through phases in order. Confirm before each major step.

---

## Phase 1: Setup — Reference Files

This skill uses reference materials. When running inside an orchestrated workflow, the orchestrator will locate and load these automatically via Glob.

- `references/analysis-guide.md` — Dataset validation steps, channel grouping rules, all calculation formulas, and anti-hallucination guardrails
- `references/design-system.md` — Color constants, CSS preview classes, helper function specs, and complete slide-by-slide build instructions for all 10 slides

---

## Phase 1.5: Data source check

> **Composio integration.** If `google_analytics` is connected via Composio (see the live MCP connectors), the four CSV datasets in Phase 2 can be pulled live from GA4 instead of asking the user to export them. Funnel screenshots remain manual — GA4's funnel UI captures more than the raw funnel API returns (segment overlays, micro-conversion paths, source filters), and the skill's "Funnel data from screenshots only" constraint is preserved.

Decide which data source you'll use before Phase 2:

1. **User has already provided data inline (some or all five datasets in their message).** Use what they gave you and acknowledge each dataset per Phase 2's intake rules (row count, date range, Grand Total). For any of the five datasets NOT yet provided, request them — via Composio pull if connected, or via the original CSV ask in Phase 2. Do NOT begin analysis until all five datasets are in. Cross-validation (Grand Total ±2%) applies once the full set arrives.
2. **No data yet → check Composio.** Run `COMPOSIO_MANAGE_CONNECTIONS`. If `google_analytics` is live for this client, offer to pull the four datasets directly using these `use_case` calls:
   - *"pull GA4 landing page report: sessions, add-to-cart, checkouts, purchases, revenue by landing page, for property {id}, date range {start}-{end}"*
   - *"pull GA4 traffic acquisition by source/medium: sessions, conversions, revenue, for property {id}, date range {start}-{end}"*
   - *"pull GA4 device category breakdown: sessions, conversions, revenue, for property {id}, date range {start}-{end}"*
   - *"pull GA4 new vs returning users: sessions, conversions, revenue, for property {id}, date range {start}-{end}"*

   Then still ask the user for **funnel screenshots** (up to 3: Homepage-start, Collections-start, PDP-start; minimum one PDP-start). The screenshots are not optional even when Composio is available.

3. **Composio not connected** → fall through to Phase 2 and request CSV uploads as the original flow describes.

**If any Composio pull fails or returns empty** (permission error, 0 rows, unexpected schema), ask the user to supply that specific dataset via CSV upload before producing analysis. Do not silently fill gaps — a missing dataset distorts the entire funnel story. Only proceed with a noted gap if the user explicitly tells you to skip that data.

---

## Phase 2: Data Intake

Before any analysis, collect ALL five datasets. Do not begin calculating until everything
is received. Confirm receipt of each dataset with a brief summary (row count, date range,
Grand Total) as it arrives — but do NOT present analysis until all five are in.

If Phase 1.5 determined Composio is the data source, fire the four GA4 pulls in parallel and request only the funnel screenshots from the user. Skip the CSV upload ask below. Otherwise, ask upfront:

> "Before I build anything, I need the GA4 exports. Please upload these — same set each time:
>
> 1. **Landing page CSV** — sessions, ATC, checkouts, purchases, revenue by page
> 2. **Session source/medium CSV** — traffic channel breakdown
> 3. **Device category CSV** — mobile vs desktop vs tablet
> 4. **New vs returning users CSV**
> 5. **Funnel screenshots** (up to 3) — GA4 open funnel reports, ideally: Homepage-start,
>    Collections-start, and PDP-start. Minimum: one (PDP-start).
>
> I'll confirm each one as it arrives, and summarise all findings once the full set is in."

**After each upload**, respond with: dataset name + row count + date range + Grand Total users.
**After the final upload**, cross-validate totals:
- Device, New/Returning, and Source/Medium Grand Totals should match Landing Page Grand Total ±2%
- If any discrepancy is >2%, ask the user to re-export the affected CSV or confirm all
  exports cover the same date range before proceeding — do not begin analysis with misaligned data

See `references/analysis-guide.md` Section 1 for the exact validation steps per dataset.

---

## Phase 3: Data Analysis

Once all data is in, run the full analysis across all five datasets. Present a structured
summary of key findings — not individual numbers, but the story the data tells.

**For each dataset, calculate:**

**Landing Pages** — Site-wide CVR, ATC rate, CO rate, AOV, Rev/User. Classify all pages
into groups (Homepage, Collections, PDPs, Search, Other). Identify top 15 collection pages,
top 20 PDPs by traffic, top 10 PDPs by revenue, high-traffic low-conversion pages (>500
users, <1% CVR). Site-wide funnel: Users → ATC → Checkout → Purchase with % drop at each step.

**Source/Medium** — Group all rows into channels (Paid Search, Direct, Organic, Email, SMS,
Paid Social, Organic Social, Display, Referral, Affiliate, Other). For each channel and top
8–10 individual sources: users, % traffic, ATC rate, CVR, revenue, AOV.

**Device** — For each device: users, % traffic, ATC rate, CO rate, CVR, AOV, Rev/User.
Calculate: Mobile vs Desktop CVR gap; incremental revenue if mobile CVR matched desktop
= (desktop CVR − mobile CVR) × mobile users × mobile AOV.

**New vs Returning** — For each segment: users, % traffic, CVR, AOV, Rev/User. Calculate
CVR advantage multiplier and Rev/User advantage multiplier for established vs new.

**Funnels** — From screenshots: step-by-step completion and abandonment rates per funnel
entry point. Cross-funnel comparison to identify consistent drop-off patterns.

See `references/analysis-guide.md` Section 2 for channel grouping rules and all formulas.

---

## Phase 4: Synthesis Brief

Before building the final deliverable, write a brief summary of key findings. This is used by the orchestrator to carry findings forward to the next skill in a multi-skill workflow.

**Quantitative Analysis Key Findings**
Extract and summarize:
- Highest-traffic, lowest-converting page or funnel step (name, traffic count, CVR %, drop-off point if in funnel)
- Device split weakness (mobile vs desktop) with quantified CVR % gap and incremental revenue opportunity if closed
- Best-performing traffic source or channel (channel name, traffic share %, CVR %, why it outperforms — copy, audience, or intent difference)
- One critical funnel leak or behavioral pattern (funnel step, drop-off %, or segment underperformance) that should be investigated

**Priority for downstream skills:** [Recommend the next skill — e.g., "Run heuristic analysis on the [PDP/page] showing [CVR]% conversion" or "Run heatmap + session recording analysis on [funnel step] showing [X]% drop-off to understand why" or "Investigate [device/channel] underperformance with segment-specific research"]

*If running standalone (not in an orchestrated chain), this analysis can be shared directly with the PM for traffic and conversion strategy alignment.*

---

## Phase 5: Choose Output Format + Approval Gate

**Ask for format choice before building the preview:**

> "Analysis complete — I'm ready to build the deliverable. What format would you like?
>
> 1. **PPTX Deck** — 10-slide branded presentation, best for client delivery
> 2. **Word Document (.docx)** — Written report with tables and prose, best for internal review
> 3. **PDF Report** — Compact branded summary of key findings
> 4. **Something else** — just tell me"

Wait for the user's answer before proceeding.

**If PPTX (or the user is unsure):**
Read `references/design-system.md` Section 1 for the exact CSS classes before building
the preview. Then create a full 10-slide HTML artifact — all slides in a single scrollable
page, each slide rendered as a 16:9 card using the exact CSS classes from the design system.

Key rules for the HTML preview:
- Use the `.deck`, `.slide`, `.card`, `.stat-big`, `.badge`, `.section-label` classes exactly
- Slide 1 uses `.title-slide` (black background); all others use `#E6ECF5` background
- Populate every slide with the real numbers from Phase 2 — no placeholder data
- Match the layout specified for each slide in `references/design-system.md` Section 4

After showing the preview:
> "Here's the full 10-slide preview. Review each slide — let me know if you want any
> changes to layout, copy, or data before I build the PPTX."

Wait for explicit approval. If the user requests changes, update the preview and re-show.
Only move to Phase 4 after they say yes.

**If Word or PDF:**
Present a structured text outline (same 10 sections, real numbers, key findings) for the
user to confirm before building. Then proceed to Phase 4 with the appropriate format.

**CRITICAL: Never build the final deliverable without explicit user approval of the preview.**

---

## Phase 6: Branding Confirmation

Before building, confirm:

> "branding, or does this need client-specific styling?
> If client-specific, share their hex colors, font, and logo and I'll apply those instead."

If branding confirmed → proceed to Phase 7. If client branding → collect specs before building.

---

## Phase 7: Build the Deliverable

After branding confirmation, build using the selected brand guidelines. Apply colors, fonts, and layout
rules from `../../../growthit-brand/assets/growthit-brand.md` (or the `brand-kit` skill) for all formats if branding was chosen.

**If PPTX:**
Build the deck using the exact design system.
1. Install: `npm install -g pptxgenjs`
2. Create `build_deck.js` with all helper functions and all 10 slides
3. Run `node build_deck.js` — confirm "Done" output
4. Convert to PDF for QA: use soffice or equivalent
5. Generate slide images: `pdftoppm -jpeg -r 150 [filename].pdf slide`
6. Inspect each slide image (Phase 5)
7. Copy final file to workspace

**Design system:** Read `references/design-system.md` before writing any PPTX build code.
It contains: color constants, font settings, all helper functions (`addCard`, `addMetric`,
`addBadge`, `addSectionLabel`, `slideTitle`, `makeShadow`), and the complete spec for all
10 slides including exact coordinates, dimensions, and data mappings.

**If Word document:**
Use the DOCX skill. Same 10 sections as the deck — prose + inline tables — branded (primary blue `#4677F7`, black cover, Poppins Bold headings, Mulish body).

**If PDF:**
Use the PDF skill. Condensed findings report — key metrics summary, channel/device tables,
top findings — branded (same color and font system as PPTX).

---

## Phase 8: QA Gate

**Run format-appropriate QA before delivering. Do not skip.**

**Universal checks (all formats):**
- All 10 sections present: Executive Summary, Site-Wide Funnel, Funnel by Entry Point,
  Traffic Sources (channel + top sources), Device, New vs Returning, Top Pages, Key Findings
- Every number traces to an uploaded CSV or screenshot — no fabricated metrics
- Grand Total figures consistent throughout — no mismatches between sections
- Brand colors and fonts applied correctly (`#4677F7` blue, `#000000` cover, Poppins/Mulish)
- Client name and date range correct on cover/title

**If PPTX — convert to images and inspect each slide:**
- **Slide 1** — Brand name left-aligned, blue accent line visible, date range at bottom-left
- **Slide 2** — All 7 metric cards readable, 5 key findings with black badges visible
- **Slide 3** — Funnel bars narrowing correctly, drop annotations between bars, 3 callout cards right
- **Slide 4** — Three waterfall charts with visible cliff at ATC bar, heatmap grid readable
- **Slide 5** — All channel rows visible with tags, no text overlap
- **Slide 6** — All top-source rows visible with tags, no text overlap
- **Slide 7** — Mobile and Desktop stacked, tablet row compact, 3 callout cards on right
- **Slide 8** — New and Established stacked, 3 callout cards on right
- **Slide 9** — Top pages and low-conversion pages both visible with tags
- **Slide 10** — Two columns (Critical Leaks + Opportunities), 3 cards each, badges readable

**If Word (.docx) — read the output file and confirm:**
- All 10 sections present as headings with prose + inline tables
- Tables render cleanly (no merged cell errors, no missing columns)
- branded cover page present

**If PDF — open and inspect:**
- All key sections present and readable
- No text cut off or overflowing page margins
- branding applied to cover and headers

Fix any layout issues and re-export before delivering.

Report to user: "QA done — [N sections verified, format, any issues found and fixed]. Here's the file."

---

## Constraints (Always Active)

**No data, no analysis.** Never generate metrics, recommendations, or funnel data without
the actual CSV or screenshot that contains it.

**Grand Total is the source of truth.** Always pull site-wide totals from the Grand Total
row in each CSV — never by summing individual page rows.

**Every number traces to source.** If a number cannot be derived from the uploaded data,
do not include it.

**No generic recommendations.** Key Findings must come from the actual data. Never
include generic CRO advice ("improve page speed", "add social proof") unless the data
specifically supports it.

**Calculate, don't assume.** All derived metrics (CVR, drop-off %, incremental revenue
opportunity) must be calculated from raw numbers, not assumed from benchmarks.

**Cross-validate totals.** Before building, verify all Grand Totals align ±2%. Flag
discrepancies >2%.

**No cross-client contamination.** Never reference data, findings, or patterns from
other client analyses.

**Confirm before building.** Never create the PPTX without explicit user approval of
the visual preview.

**Channel grouping transparency.** If a source/medium doesn't fit cleanly into a
channel, flag it — never silently reclassify.

**Funnel data from screenshots only.** Funnel completion rates must come from GA4
funnel screenshots, not from ratios calculated from the landing page CSV.

---

## References

- **[Design System](references/design-system.md)** — Color constants, CSS preview classes, helper function specs, and complete slide-by-slide build instructions for all 10 slides. Read before writing any PPTX build code or HTML preview.
- **[Analysis Guide](references/analysis-guide.md)** — Dataset validation steps, channel grouping rules, all calculation formulas, and the full 10 anti-hallucination guardrails. Read during Phase 1 for data validation and Phase 2 for analysis calculations.
