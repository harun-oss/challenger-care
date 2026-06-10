# Heatmap & Scroll Map Analysis — SOP Reference

Version 3.0 | Read this file when you need step-by-step detail on any phase.

---

## Guardrails — Anti-Hallucination Rules (NON-NEGOTIABLE)

### Data Integrity

**1. Never invent or round numbers.**
Every figure must trace to the uploaded CSV. Use exact values: "464 taps (3.98%)" — never "~460 taps".

**2. Classify CSS selectors dynamically — never from a template.**
Read raw selectors from the CSV. Split on `>` and `.` to extract fragments. Group by shared keywords.
- ✅ Analyze keyword patterns: "close", "submit", "cart", "accordion", "klaviyo", "privy"
- ❌ Never assume "klaviyo" = popup — confirm from selector analysis
- ❌ Never copy classifications from a previous client's analysis

**3. Map scroll sections dynamically — never assume positions.**
Use the scroll PNG overlay + full-page screenshot (if available) to identify what content sits at each depth.
- ✅ Label each mapping: "Visually confirmed" or "Estimated — please confirm"
- ❌ Never use "0–5% = header, 5–10% = product image" as a starting template

**4. Never fabricate Baymard guidelines.**
Web-search every citation during the session. Never invent guideline IDs or statistics.
- ✅ "Baymard's large-scale usability testing shows that…" + cite public article URL
- ❌ Never write "Baymard Guideline #742 states…" unless retrieved from web search

**5. Never invent conversion rates or revenue impact.**
Use qualitative labels only: Critical / High / Medium / Low.
- ❌ Never write "This change could increase CR by 15%"

### Interpretation

**6. Correlation ≠ causation.** A popup co-located with a scroll cliff doesn't prove the popup causes it.
Write: "The popup is the most probable contributor" — not "The popup causes users to leave."

**7. Always state data limitations.** Every deliverable must include: data source, date range, page views,
device type, and any missing context (traffic sources, CR data, prior tests).

**8. Don't over-interpret low-signal elements.** Below 0.5% of total taps = aggregate into categories,
don't analyze individually.

**9. Flag missing context every time.** If traffic source, CR data, or device comparison is missing,
call it out explicitly in the deliverable.

---

## Step-by-Step Detail

### Step 1: Parse CSV Data

**Heatmap CSV:**
1. Extract from header: project name, date range, URL, total page views, total taps
2. Parse element table: Rank, CSS Selector, Tap Count, % of Total Taps (store ALL rows)
3. Sanity check: sum of element taps should match header total (±5% tolerance). Flag discrepancies.

**Scroll Map CSV:**
1. Extract from header: project name, date range, URL, total page views
2. Parse depth table: Scroll Depth %, Visitors, Cumulative Drop-off %
3. Calculate interval drop-off: `delta = current_cumulative – previous_cumulative` for each 5% step
4. Calculate % of total visitors at each depth: `visitors_at_depth / total_page_views × 100`
5. Sanity check: visitor counts must decrease monotonically. Flag anomalies.

⚠️ After parsing, verify 3 random rows from each CSV match the raw file before proceeding.

---

### Step 2: Classify Elements (Dynamic)

1. Extract all unique class names and IDs from CSS selectors (split on `>`, `.`, `#`)
2. Identify keyword clusters: form, submit, button, nav, drawer, cart, product, media, image,
   gallery, price, bundle, variant, accordion, faq, popup, modal, overlay, close, dismiss
3. Cross-reference with heatmap PNG: heat spots correspond to ranked elements
4. Cross-reference with live URL if provided (resolves ambiguous selectors definitively)
5. Assign human-readable name + functional category to each element
6. Flag unidentifiable elements as "Unidentified Element (Rank #X)" — show raw selector, ask user

After classifying: aggregate taps by category, rank descending.
⚠️ Verify sum of classified taps equals header total.

---

### Step 3: Map Scroll Depth to Sections (Dynamic)

1. Examine scroll PNG: identify content visible at each color-transition zone
2. If full-page screenshot available: use as primary source — measure section positions as % of total height
3. If live URL available: fetch page, capture full viewport, measure precisely
4. Create mapping table: depth range | section name | confidence | visitors reaching | drop-off
5. If sections unclear: state explicitly — "Section at 30–40% depth unclear from overlay alone"

**Zone Classification (universal — based on drop-off math, not page content):**

| Zone | Delta Drop-off | Interpretation |
|------|---------------|----------------|
| CLIFF | >10% in one 5% interval | Critical. Investigate immediately. |
| SLIDE | 3–10% per interval | Significant. Often around the buy box. |
| TAPER | 1–3% per interval | Gradual attrition through content. |
| PLATEAU | <1% per interval | Highly engaged users. |
| FOOTER DROP | Increased drop in final 5–10% | Normal. Only a concern if unusually large. |

---

### Step 4: Behavioral Analysis

**Tap data — ask:**
- What dominates attention? (top 3 category clusters)
- Is there interaction fragmentation? (many elements in same functional area = UI confusion)
- What is the ATC tap rate? (compare to total taps AND to visitors who reached ATC zone)
- What are users seeking? (accordion/FAQ taps = unmet information needs)
- Are there friction signals? (close/dismiss taps, excessive variant switching)

**Scroll data — ask:**
- Where is the cliff? (single largest delta drop-off interval)
- What % reach the buy box / primary CTA?
- What % reach key persuasion content? (trust badges, reviews, comparisons)
- Is there a loyal minority? (users persisting past 90% = highly engaged researchers)
- Content ROI: is valuable content placed below where most visitors drop off?

**Combined (if both datasets):**
- Cross-validate: high taps + high drop-off zone = strong friction signal
- Effective CTA rate: CTA taps ÷ visitors who reach CTA zone
- Content investment mismatch: significant taps from a tiny % of visitors

---

### Step 5: Baymard Cross-Reference

For each finding: (a) identify the UX theme, (b) web-search for the Baymard article,
(c) summarize in your own words with attribution, (d) include article URL if found.

If no Baymard result found: cite general UX research and note the absence. Do not invent.

---

### Step 6: Generate Test Ideas

Quality criteria for each test:
- **Specific:** "Delay popup to 30s+ or exit-intent" — not "improve the popup"
- **Measurable:** one clear primary metric per test
- **Grounded:** traces to a specific data finding AND a Baymard principle
- **Varied:** mix quick wins (config changes) and deeper redesigns

**Prioritization:**

| Priority | Criteria | Examples |
|----------|---------|---------|
| P0 — Immediate | >10% of taps or >20% scroll drop-off. Low effort. | Remove/delay popup, show price above fold |
| P1 — Next Sprint | 5–10% of taps or 10–20% drop-off. Medium effort. | Compress buy box, relocate trust signals |
| P2 — This Quarter | 2–5% of taps or 5–10% drop-off. | Mid-page CTA, image reorder |
| P3 — Backlog | <2% of taps or <5% drop-off, or high effort. | Content reorder, footer redesign |

---

### Step 7: 9-Slide PPTX Structure (when PPTX is chosen)

| # | Slide | Content |
|---|-------|---------|
| 1 | Title Slide | Client name, page, device, data source, date range, page views, total taps |
| 2 | Executive Summary | 3 hero stat cards + Combined Insight callout box |
| 3 | Tap — Top 15 Table | Dynamically classified elements + callout cards |
| 4 | Tap — Category Chart | Horizontal bar chart of aggregated categories + 3 insight cards |
| 5 | Scroll — Drop-Off | Line chart with zone annotations (Cliff, Slide, Taper, Plateau) |
| 6 | Scroll — Content Reach | Section → depth → % visitors reaching each |
| 7 | Combined Insights | 2×2 insight card grid |
| 8 | Recommendations 1/2 | P0 + P1 tests with Baymard references |
| 9 | Recommendations 2/2 | P1, P2, P3 tests with Baymard references |

If only one data type available: reduce to 7 slides (remove the irrelevant data slides).
Note missing data type on the title slide.

---

### Step 8: QA Checklist

**8A — Data Accuracy**
- [ ] Spot-check 5 random elements from top 20 against raw CSV — counts must match exactly
- [ ] Re-calculate delta drop-off for cliff zone + 2 other intervals — any mismatch = rebuild
- [ ] Verify category totals: sum element taps per category = category total in chart
- [ ] Search entire deliverable for every number — each must trace to the CSV

**8B — Classification Accuracy**
- [ ] Re-read top 10 CSS selectors — confirm labels match actual elements (cross-reference PNG)
- [ ] Any "Unidentified" elements? Confirm they're flagged with raw selector shown
- [ ] Scroll section mapping: re-examine PNG, confirm each label matches visible content at that depth

**8C — Baymard Citations**
- [ ] Every citation was web-searched this session OR is a well-known public finding
- [ ] Any unverifiable citation: rephrase as general UX best practice or remove

**8D — Visual / Format QA**
- [ ] PPTX: convert to PDF → slide images → inspect every slide for overlaps, cut-off content, wrong colors
- [ ] Word doc: read .docx output, confirm table formatting and heading hierarchy
- [ ] All formats: brand colors and fonts applied correctly

**8E — Completeness**
- [ ] Title/opening section: client name, page, device, data source, date range, page views, taps
- [ ] All sections present (or reduced if partial data — noted on title slide)
- [ ] Limitations stated: missing context called out explicitly
- [ ] Post-Analysis Improvement Checklist shared with user ← mandatory

---

## Post-Analysis Improvement Checklist

Share this at the end of every analysis. It is part of the deliverable.

| # | Request | Why It Matters |
|---|---------|---------------|
| 1 | Full-page screenshot (no overlay) | Enables precise section-to-depth mapping |
| 2 | Live page URL | Resolves ambiguous CSS selectors definitively |
| 3 | Traffic source breakdown | Cold ad traffic vs. branded search behave very differently |
| 4 | Conversion rate data | Enables quantified impact estimates per recommendation |
| 5 | Desktop heatmap/scroll data | Isolates device-specific issues vs. site-wide problems |
| 6 | Session recordings | Validates hypotheses (is the popup really causing the cliff?) |
| 7 | Prior A/B test results | Prevents recommending already-tested changes |

---

## Brand Fallback (if growthit-brand.md is not accessible)

| Element | Value |
|---------|-------|
| Background | #F5F7F9 (off-white blue-gray) |
| Primary accent | #4677F7 (Blue) |
| Cover/badge fill | #000000 (black) |
| Title font | Poppins Bold |
| Body font | Mulish Regular |
| Footer | Progress dots bottom-left | GROWTHHIT logo bottom-right ("GROWTH" black, "HIT" blue) |

Always confirm branding with the user before applying. Some deliverables need client branding.
