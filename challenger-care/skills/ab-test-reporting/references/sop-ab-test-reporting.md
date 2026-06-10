# A/B Test Reporting — SOP & Observed Patterns

## Original SOP

Challenger's A/B test reporting process centers on the **Test Update Deck** — a PPTX/Figma presentation delivered on client calls to communicate test status, results, and recommendations. The deck is updated for each team review (typically bi-weekly or monthly).

The original SOP had no formal written guide beyond the deck template itself. This document codifies the patterns observed across real Test Update Decks.

---

## Observed patterns from NBC and RiseCommercial decks

### NBC (National Bankcard) — Lead-gen B2C, frequentist stats

**Platform:** Convert.com (P-value / frequentist)
**Client type:** B2C lead generation (payment processing sign-ups)
**Funnel:** Multi-step CPL form (Name → Phone → Email → Summary Page)
**Deck length:** ~133 slides for an active testing program (~16+ tests)

**Structural observations:**
- Strong "Lessons from N Tests" opening slide that categorizes wins by theme (Messaging, Creative, CTA, Progress Meter)
- Roadmap slides organized per funnel step (Step 1, Step 2, etc.) with specific test ideas and copy angles (e.g. "Tired of Square's 2.6%?")
- Form abandonment slide showing step-by-step drop-off rates with specific % at each field
- LIVE tests have 4 variants with results broken out per goal (one results slide per goal)
- Results table format: P-Value in black box (left panel) · Significance Yes/No · Table columns: Experiment Sessions / Experiment Conversion / C.V.R. / Uplift or Decline
- Observation bullets appear in a bordered text box below the data table
- Test IDs use client prefix + sequential number: NBC015, NBC016A, NBC016B, etc. (iteration suffixes used for test series)

**Unique patterns:**
- Some tests have many variants (NBC019 had 4 variants, each with their own P-value)
- Iteration series (NBC016, 016A, 016B, 016C, 016D) show progressive copy/design refinement
- DESIGN and DEV slides show Control + Variant screenshots but no results (pending launch)
- FLAT section is used for tests that produced no meaningful signal and are being retired without full archive treatment

### RiseCommercial — Lead-gen B2B, Bayesian stats

**Platform:** VWO (Bayesian / Decision Probabilities)
**Client type:** B2B lead generation (commercial real estate space leasing)
**Funnel:** Multi-page site (Homepage → Location Pages → Book A Tour page → form submit / phone click)
**Deck length:** ~57 slides for an active program (~8 live/recent tests)

**Structural observations:**
- Spring Roadmap slide as opening context (status labels: Pushing Live Today / Dev / Adjusting Copy / Planning / Ideation / On Hold / priority-ranked items)
- LIVE tests use VWO screenshot for goal data rather than a custom-built table (data embedded from tool)
- An additional "Leads Overall — Klaviyo + Phone Clicks" summary slide uses the standard black-panel table (P-Value · Significance · Sessions/CVR) to consolidate the multi-source lead data
- Klaviyo form data is reported separately from VWO engagement/click data (because Klaviyo tracks actual submissions while VWO tracks upstream clicks)
- Heatmap Analysis embedded within an individual LIVE test slide (RISE008) showing Control vs. Variant heatmap side-by-side with device behavior notes
- Form Abandonment slide for the "Commercial Space Form" using Klaviyo step completion data (Page visits → Visible on screen → Interacted → Submitted)
- RISE001 (oldest test) used a different visual template (blue blob backgrounds, older style) — visual inconsistency vs. current standard

**Unique VWO patterns:**
- Control often shows "No data yet" when a previous variant (e.g. "002 Variant") is serving as the baseline — must be documented explicitly
- VWO Decision Probabilities bar shows red (probability of worse) vs. green (probability of better) — color-coded
- MDE, ROPE, Power, FPR shown in VWO UI and visible in screenshots (useful context for Challenger)
- VWO 30-day data loss: Tests running >30 days lose visitor assignment data — RISE005 and RISE007 both affected

**Test status variety observed in RISE deck:**
- LIVE (black label, standard)
- Paused (full blue slide divider — different from standard light-bg section dividers)
- Design (light background, plain text divider)
- Dev (light background, plain text divider)
- Ready to go Live (light background, plain text divider)
- Winner (light background, plain text divider)
- Archive content uses an older template style

---

## Two-platform stat format reference

### NBC-style table (Frequentist — Convert)

```
┌─────────────────┬─────────────────────┬───────────────────────┬─────────┬──────────────────┐
│ P-Value         │ Experiment Sessions │ Experiment Conversion │ C.V.R.  │ Uplift / Decline │
│ [X.XXXX]        ├─────────────────────┼───────────────────────┼─────────┼──────────────────┤
│                 │ Control: [X]        │ Control: [X]          │ [X.XX%] │ —                │
│ Significance    ├─────────────────────┼───────────────────────┼─────────┼──────────────────┤
│ Yes / No        │ Variant N: [X]      │ Variant N: [X]        │ [X.XX%] │ [+/-X.XX%]       │
└─────────────────┴─────────────────────┴───────────────────────┴─────────┴──────────────────┘
```

### RISE-style (Bayesian — VWO)

Data comes directly from VWO UI screenshots embedded in slides. Key columns:
- Variations (Control / Variant labels + Baseline tag)
- Unique Conversions / Visitors
- Expected Conversion Rate
- Expected Improvement % (with confidence interval bar)
- Decision Probabilities (MDE · ROPE · Power · FPR settings visible)

A consolidated "Leads Overall" summary table uses the NBC-style format to aggregate multi-source data (Klaviyo form submits + phone clicks).

---

## Client types and their goal structures

| Client type | PRIMARY goals | Typical GUARDRAIL goals |
|-------------|--------------|------------------------|
| Lead-gen B2C (NBC) | Clicks Yes, Form Step Completions, Summary Page visits | Clicks No (should not increase), Page Exit |
| Lead-gen B2B (RISE) | Sign Ups (Klaviyo form submits), Phone Clicks | CTA Clicks (high-level engagement should stay stable), Bounce Rate |
| eComm | Add to Cart, Purchase, Revenue per Session | Bounce Rate, Return Rate |

---

## Edge cases encountered

### Data anomaly: Tracking error mid-test
*RISE010 (Get a Quote)* — Tracking was broken on the variant mid-test, contaminating results. Reported with a note about data quality. Test needs relaunch.

### Data anomaly: GA4 tracking broken
*RISE Archive (Book A Tour Key Events)* — GA4 showed -100% key events, indicating tracking was completely broken. Reported in Archive section with GA4 comparison screenshot.

### Data anomaly: VWO 30-day data loss
*RISE005 (All Location Pages) and RISE007 (15 Minute Space Planning Call)* — Both tests running >30 days lost visitor assignment data due to VWO policy. Notes added: "Due to data loss stemming from VWO policies, the Control group has outperformed the Variant over the last 30 days."

### Multi-source lead aggregation (RISE)
RISE tracks leads from two sources: Klaviyo form submits AND phone clicks. The "Leads Overall" summary table combines both into a single CVR (total conversions from both sources / total experiment sessions). This produces a composite lead rate that better represents true business impact.

### Paused test with strong engagement but low downstream conversion (RISE007)
RISE007 (15 Minute Space Planning Call popup) showed significantly higher engagement (29.55% lift, 100% Decision Probability) but overall form submissions were lower on the variant. Recommendation was to pause until the landing page is updated — engagement wins don't matter if the destination page can't convert.
