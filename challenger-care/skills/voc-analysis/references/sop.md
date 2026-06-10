# Voice of Customer Analysis — Full SOP Reference

Version 1.0 | Purpose: Consistent, high-quality exit-intent analysis and PPT output

---

## 1. Definition of Done

A great exit-intent analysis is a decision aid, not a loose summary of comments. Final deliverables must include:

- A clean, reviewable analysis dataset (raw preserved + coded copy)
- Sentiment split with counts and percentages (Positive / Neutral / Negative / Unknown)
- CRO-actionable theme coding with a defined codebook, counts, and shares
- Key VoC verbatims supporting each major theme
- Term frequency summary and a word cloud to triangulate patterns
- A presentable slide deck that tells a tight story and ends with a prioritized action plan

---

## 2. Standard Theme Families for Exit-Intent Surveys

These are the most common exit-intent themes observed across clients. Use these as the
starting codebook and add client-specific themes as needed.

| Theme Family | What It Captures |
|-------------|-----------------|
| Price and perceived cost | Too expensive, sticker shock, can't afford, comparing prices |
| Shipping and delivery concerns | Shipping costs, delivery time, no free shipping threshold |
| Trust and credibility | Site doesn't feel trustworthy, unfamiliar brand, no reviews visible |
| Product information gaps | Not enough info, can't find specs, unclear what's included |
| Comparison and decision uncertainty | Still shopping, checking alternatives, not ready to decide |
| UX or technical issues | Site bugs, broken features, confusing navigation |
| Payment/checkout friction | Limited payment options, checkout too long, forced account creation |
| Policy concerns (returns/warranty) | Unclear return policy, no warranty info, risky purchase |
| Timing intent (not ready) | Will come back later, just browsing, need to think about it |
| Availability/stock | Out of stock, wrong size/variant, limited options |
| Support needs | Had a question, couldn't find help, needed to contact support |
| Offer/promo expectations | Looking for a coupon, expected a discount, promo didn't apply |
| Account/login friction | Forced to create account, forgot password, login issues |
| International/region constraints | Doesn't ship to my country, pricing not in my currency |

**Coding rules:**
- Allow multi-label coding: one response can map to multiple themes
- Assign a primary theme (main blocker) and optional secondary themes (supporting blockers)
- If the response is vague, use Unknown/Vague — do not force a theme
- Unknown/Vague is a data quality signal, not a failure

**Price theme note**: If price dominates, always separate "cannot afford" from "not worth it":
- "Cannot afford" → points to offer/pricing strategy interventions
- "Not worth it" → points to value communication and proof interventions

---

## 3. Sentiment Classification Rules

Use four labels only. Keep labels stable across the entire dataset using these rules.

| Label | Definition | Examples |
|-------|-----------|---------|
| Positive | Satisfaction or success state — user found what they needed, completed their goal | 'found what I needed', 'already bought', 'great site', 'perfect product' |
| Negative | Blocker or frustration preventing progression | 'too expensive', 'shipping is high', 'doesn't trust', 'can't find what I need' |
| Neutral | Informational without clear positive/negative intent | 'checking prices', 'comparing options', 'just browsing', 'need to think' |
| Unknown | Too vague to classify, or blank/invalid | 'idk', emoji only, '-', single random word |

**Classification rule**: Classify based on intent to proceed, not tone. "I love the products but they're
too expensive" = Negative (purchase blocked by price). Tone is positive; intent signal is blocked.

**Required output**: Counts and percentages for each class, plus 2–3 representative verbatim
quotes per class for the deck.

---

## 4. Data Preparation Standards

### 4.1 Preserve Raw + Create Analysis Copy
Never overwrite the raw export. Create a separate analysis dataset where cleaning and coding occur.
This enables re-runs, QA, and auditing.

### 4.2 Canonical Cleaning Rules
- Normalize whitespace: trim leading/trailing spaces; collapse multiple spaces
- Standardize casing for analysis fields while preserving the original text in a separate raw_response column
- Move truly empty responses (blank, '-', 'na', 'none', '.') into an empty/invalid bucket. Do not delete them; report them
- Deduplicate only when you are confident the exact same response is repeated by the same user/session; otherwise, treat as separate signals

### 4.3 Helper Columns for Repeatability
- **response_length**: word count or character count
- **response_type**: single word, short phrase, sentence, multi-sentence
- **normalized_response**: used for coding and term frequency
- **segment fields**: device/source/page/etc., if present

### 4.4 Data Quality Report (Required)
Before beginning analysis, report to the user:
- Total rows in raw export
- Empty/invalid response count and percentage
- Usable response count
- Date range (if timestamp present)
- Whether segmentation columns are present

---

## 5. Quantification Standards

### 5.1 Two Quantification Methods

**Response share**: percent of (usable) responses mentioning the theme.
- Use this as the primary metric
- Required for every theme in the codebook

**Mentions share**: percent of all theme mentions (useful when multi-labeling is common).
- Use this as a secondary metric when multi-labeling rate is high (>30% of responses have 2+ themes)

### 5.2 Insight Prioritization Model

Prioritize insights using three dimensions:
- **Volume**: response share — how many people mentioned this?
- **Severity**: does it block purchase, or is it a preference?
- **Ease/clarity of fix**: information gap, reassurance gap, or UX change required?

Write each insight as:
> "Because [users do/feel X] → so they leave → therefore we should [action]."
> Evidence: [count, share, 2–3 verbatims]

---

## 6. Segmentation Standard

### When to Segment
If device/source/page/country/new-vs-returning exists, run at least one segmentation pass.
Pick 1–3 segments tied to the business question. Avoid slicing everything.

### Recommended Default Cuts
- Mobile vs. Desktop
- Paid vs. Organic
- New vs. Returning
- Top landing pages vs. others

### Segmentation Rules
- Show a small comparison table of top themes by segment in the deck
- Flag themes that are 1.5x–2.0x higher in a segment as priority leads
- Always report segment sample sizes — only interpret segments with sufficient sample size (minimum 100 responses per segment for defensible results; below 100 = label as directional, note the limitation)
- Never make claims about tiny segments

---

## 7. Term Frequency and Word Cloud Standard

Use term frequency as triangulation, not primary proof. It confirms coded themes and surfaces missed patterns.

**Process:**
1. Build tokens from normalized_response text
2. Remove standard stopwords (the, a, is, it, etc.)
3. Optionally merge obvious synonyms (cost/expensive/price → price_theme)
4. Count frequency of remaining terms

**Deliverable requirements:**
- Top 15–30 terms table (term, frequency, % of responses)
- Word cloud image (or description of one)
- Narrative tie-back: does the term frequency confirm your coded themes? Does it surface any new patterns not captured in coding?

---

## 8. Recommendations and Experiment Mapping

For each top theme (typically 5–8), propose actions in three layers:

**Layer 1 — Immediate copy/UX fixes (low lift)**
Changes that can be implemented in 1–3 days without dev work.
Examples: updating copy, adding a callout, showing existing trust badges more prominently.

**Layer 2 — Medium-lift modules (1–2 weeks)**
Examples: comparison table, shipping calculator, sticky reassurance banner, improved social proof section.

**Layer 3 — Experiments (A/B tests)**
For each proposed experiment, include:
- **Hypothesis**: If we [change X], then [metric Y] will improve because [reason Z]
- **Primary metric**: form submit, add to cart, checkout start, purchase
- **Guardrails**: bounce rate, engagement time, other metrics to watch
- **Traffic note**: If traffic is low, include validation alternatives (session replays, on-page polls, user interviews)

---

## 9. Operating Notes for Difficult Data Cases

**Extremely short responses** ('no', 'idk', single words):
Treat as a data quality signal, not a theme. Report the count separately. Common causes: survey fatigue, weak question framing, or low-intent traffic. Do not force themes onto these responses.

**Price domination**:
Always separate "cannot afford" from "not worth it":
- Cannot afford → interventions: pricing strategy, payment plans, bundle offers
- Not worth it → interventions: value communication, social proof, benefit framing, comparison content

**Missing segmentation data**:
Proceed with the analysis but explicitly state in the deck: "Segment-level insights were not possible due to missing [column name] data. We recommend adding [field] to the survey export for future analyses."

**Small sample sizes** (under 100 usable responses):
Note in the methodology slide. Treat all findings as directional, not statistically significant. Recommend validation before acting.

---

## 10. Slide Deck Blueprint

Typical deck length: 8–14 slides. Keep one key message per slide and support each claim with numbers and/or VoC.

| Slide # | Title | Content Requirements |
|---------|-------|---------------------|
| 1 | Title Slide | Site name, date range, sample size, survey question |
| 2 | Executive Summary | 3–5 headline insights |
| 3 | Data Overview & Methodology | Cleaning + coding approach, response quality stats |
| 4 | Sentiment Split | Counts + percentages + implications per class |
| 5 | Theme Distribution | Top themes with response share (chart or table) |
| 6 | Theme Deep Dive #1 | Meaning, evidence (verbatims), fixes/tests |
| 7 | Theme Deep Dive #2 | Meaning, evidence, fixes/tests |
| 8 | Theme Deep Dive #3 | Meaning, evidence, fixes/tests |
| 9 | Segment Comparison | If available: small comparison table of top themes by segment |
| 10 | VoC Verbatims Wall | Grouped by theme; key quotes highlighted |
| 11 | Word Cloud + Top Terms Table | Top 15–30 terms; narrative tie-back |
| 12 | Prioritized CRO Action Plan | Quick wins vs. experiments vs. research; prioritized |
| 13 | Draft Test Hypotheses | 3–6 tests with success metrics (optional) |
| 14 | Appendix | Full codebook + notes on Unknown/Vague |

Design rules: consistent spacing and typography; avoid text walls; group quotes; show counts and
percentages wherever you make a claim.

---

## 11. QA Checklist (Must Run Before Delivering Deck)

- [ ] Sample size matches raw export; empty/invalid count is reported
- [ ] Sentiment totals add up to 100%
- [ ] Theme tables include counts and percentages (response share; mentions share if multi-label)
- [ ] At least 2 verbatims per top theme
- [ ] Unknown/Vague is handled transparently (no forced coding)
- [ ] Segmentation claims are supported by sufficient segment sample size
- [ ] Deck numbers match the analysis dataset (no mismatches between slides and tables)

---

## 12. Three-Step Workflow (Confirmation Before Deck)

1. **Request analysis only**: Provide the CSV and survey question(s). Require analysis confirmation first; do not generate the deck until confirmed.
2. **Review**: Request changes to themes, prioritization, or segmentation if needed.
3. **Generate deck**: After confirmation, create slides using the blueprint above.

**Always hold**: Do not create the PPT until the analysis is confirmed by the user.

---

## 13. Post-Analysis Checklist

Share this at the end of every analysis. It is part of the deliverable.

| # | Request | Why It Matters |
|---|---------|---------------|
| 1 | Add device/source/page columns to survey export | Enables meaningful segmentation without re-running the survey |
| 2 | Tighten the survey question if >30% responses are vague | Short/vague responses signal question fatigue or ambiguity |
| 3 | Set up comparison periods | Repeat the same survey quarterly to track theme movement over time |
| 4 | Validate top themes with session recordings | Confirm that the stated blocker matches actual behavior on-site |
| 5 | Run a follow-up micro-survey on the #1 theme | Vague price/trust signals need a second-pass question to get actionable detail |
| 6 | Share conversion rate data | Enables quantified impact estimates per recommendation |
| 7 | Run A/B test on top P0 recommendation | VoC shows the problem; a test confirms the fix |

---

## 14. Brand Fallback (if growthit-brand plugin is not accessible)

| Element | Value |
|---------|-------|
| Background | #F5F7F9 (off-white blue-gray) |
| Primary accent | #4677F7 (Blue) |
| Cover/badge fill | #000000 (black) |
| Title font | Poppins Bold |
| Body font | Mulish Regular |
| Footer | Progress dots bottom-left \| GROWTHHIT logo bottom-right ("GROWTH" black, "HIT" blue) |

Always confirm branding with the user before applying.
