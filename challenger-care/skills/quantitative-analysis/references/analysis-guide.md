# Quantitative Analysis — Analysis Guide & Guardrails

## Section 1: Dataset Validation

Validate each CSV as it arrives. Do not proceed without all five.

### Landing Page CSV
Expected columns: Landing page URL, Total users, Add to carts, Checkouts, Purchases,
Purchase revenue, Average purchase revenue.
- Check for Grand Total row — this is your site-wide baseline for all calculations
- Confirm date range (ask user if not in filename or headers)
- Count data rows (excluding Grand Total)
- Flag any rows with "web-pixels" in the URL — these are noise, exclude from page analysis

### Session Source/Medium CSV
Expected columns: Session source/medium, Total users, Add to carts, Checkouts, Purchases,
Purchase revenue, Average purchase revenue.
- Grand Total users should match Landing Page Grand Total ±2%
- If discrepancy >2%, flag before proceeding

### Device Category CSV
Expected columns: Device category, Total users, Add to carts, Checkouts, Purchases,
Purchase revenue, Average purchase revenue.
- Sum of all device rows should match Grand Total ±2% (GA4 sampling variance is normal)
- Expected categories: mobile, desktop, tablet (smart tv is rare but valid)

### New vs Returning Users CSV
Expected columns: New/established segment, Total users, Add to carts, Checkouts, Purchases,
Purchase revenue, Average purchase revenue.
- Sum of New + Established (+ "not set" if present) should match Grand Total ±2%

### Funnel Screenshots
- Minimum: one screenshot (PDP-start funnel)
- Ideal: three (Homepage-start, Collections-start, PDP-start)
- Each screenshot must show: step names, active users per step, % of Step 1, abandonment rate
- Note: funnel data is NOT derivable from landing page CSV — these are different measurements

---

## Section 2: Calculation Formulas

### Site-Wide Metrics (from Landing Page Grand Total row)
```
ATC Rate    = Add to Carts / Total Users
CO Rate     = Checkouts / Total Users
CVR         = Purchases / Total Users
AOV         = Purchase Revenue / Purchases
Rev/User    = Purchase Revenue / Total Users
```

### Funnel Drop-off (from Grand Total row)
```
Users → ATC drop     = (Users - Add to Carts) / Users
ATC → CO drop        = (Add to Carts - Checkouts) / Add to Carts
CO → Purchase drop   = (Checkouts - Purchases) / Checkouts
```

### Device Analysis
```
Mobile CVR               = Mobile Purchases / Mobile Users
Desktop CVR              = Desktop Purchases / Desktop Users
CVR Gap                  = Desktop CVR − Mobile CVR
AOV Gap                  = Desktop AOV − Mobile AOV
Rev/User Gap             = Desktop Rev/User − Mobile Rev/User

Incremental Revenue Opportunity:
= (Desktop CVR − Mobile CVR) × Mobile Users × Mobile AOV
```

### New vs Returning
```
CVR Advantage Multiplier     = Established CVR / New CVR
Rev/User Advantage Multiplier = Established Rev/User / New Rev/User
Revenue Concentration        = Established Revenue / Total Revenue
Traffic Share                = Established Users / Total Users
```

### Page-Level Analysis
```
Page ATC Rate  = Page Add to Carts / Page Users
Page CVR       = Page Purchases / Page Users
Page AOV       = Page Revenue / Page Purchases
```

High-traffic low-conversion threshold: >500 users AND <1% CVR
(Exclude web-pixel noise rows)

---

## Section 3: Channel Grouping Rules

When parsing Session Source/Medium CSV, assign each row to exactly one channel.
Apply rules in this order — first match wins.

| Channel | Match Rule |
|---|---|
| Paid Search | Contains "/ cpc", "/ ppc", or "pmax" |
| Direct | Contains "(direct)" or "/ (none)" |
| Organic Search | Contains "/ organic" |
| Email | Contains "email", "klaviyo", "listrak", "mailchimp", "bronto", or "sailthru" |
| SMS | Contains "/ sms" |
| Paid Social | Contains ("facebook" OR "instagram" OR "meta") AND ("paid" OR "cpc" OR "cpm") |
| Organic Social | Contains "facebook", "instagram", "pinterest", "twitter", "tiktok", "youtube" (not already matched as Paid Social) |
| Display/Programmatic | Contains "criteo", "display", "hivewyre", "programmatic", "gdn", "ctv", or "dv360" |
| Referral | Contains "/ referral" |
| Affiliate | Contains "affiliate", "impact", "shareasale", "rakuten", or "cj" |
| Other | Everything else |

**Transparency rule:** If a source doesn't fit cleanly, flag it to the user before assigning.
Never silently reclassify.

---

## Section 4: Page Classification Rules

Classify landing page URLs into groups for the summary analysis:

| Group | Rule |
|---|---|
| Homepage | Path exactly equals "/" |
| Collection Pages | Path contains "/collections/" |
| Product Pages (PDPs) | Path contains "/products/" |
| Search | Path exactly equals "/search" |
| Web Pixels / Noise | Path contains "/web-pixels" — EXCLUDE from all analysis |
| Other | Everything else |

For each group, calculate: total users, average ATC rate, average CVR, total revenue,
page count.

---

## Section 5: Funnel Screenshot Extraction

For each funnel screenshot, extract:
- Step names (e.g., "View item", "Add to cart", "Begin checkout", "Purchase")
- Active users at each step
- % of Step 1 (completion relative to entry)
- Step-to-step completion rate: step N users / step (N-1) users
- Abandonment rate: 1 − (step N users / step (N-1) users)

Cross-funnel comparison: identify patterns that appear consistently across all entry
points. Example: "PDP→ATC drop is ~93-95% across all three funnels" is a finding.
A pattern that appears in only one funnel is a single-funnel anomaly, not a site-wide finding.

---

## Section 6: Key Findings Framework (Slide 10)

The Key Findings slide must follow this structure:

**Critical Leaks (left column, 3 findings)**
Each finding must:
1. Name the specific metric and the gap (e.g., "Mobile CVR is 1.8% vs Desktop 4.2% — a 2.4pp gap")
2. Quantify the business impact where possible (e.g., "$X in incremental revenue if closed")
3. Point to the slide where the data lives (e.g., "See Slide 7")

**Opportunities (right column, 3 findings)**
Each finding must:
1. Name what to test or improve and why the data supports it
2. Be specific — not "improve mobile UX" but "mobile checkout completion is 68% vs 81% desktop — investigate form friction on mobile"
3. Connect to a specific dataset finding

Do not include generic CRO advice. Every finding must trace to the uploaded data.

---

## Section 7: Anti-Hallucination Guardrails

**Guardrail 1 — No Data, No Analysis**
Never generate analysis, metrics, recommendations, or any quantitative claims without
the actual CSV or screenshot containing that data.

**Guardrail 2 — Grand Total Is The Source of Truth**
Always extract site-wide totals from the Grand Total row in the CSV.
Never sum page-level rows to derive totals (URL parameter fragmentation causes double-counting).

**Guardrail 3 — Every Number Must Trace to Source**
Every number in the deck must be directly calculable from the uploaded CSVs or funnel
screenshots. If a number cannot be traced, do not include it.

**Guardrail 4 — No Generic Recommendations**
Slide 10 must only contain findings grounded in the actual data. Never include generic CRO
advice like "improve page speed" or "add social proof" unless the data specifically supports it.

**Guardrail 5 — Calculate, Don't Assume**
All derived metrics (CVR, ATC rate, drop-off %, incremental revenue opportunity) must be
calculated from raw numbers, not assumed from industry benchmarks or prior client data.

**Guardrail 6 — Cross-Validate Totals**
Before building the deck, verify that total users across device categories, new/established
segments, and the Grand Total are within ±2%. Flag any significant discrepancies.

**Guardrail 7 — No Cross-Client Contamination**
Never reference data, findings, or patterns from other client analyses. Each analysis is
completely standalone.

**Guardrail 8 — Confirm Before Building**
Never create the PPTX file without explicit user approval of the visual preview.
Always show the full deck preview first and wait for confirmation.

**Guardrail 9 — Channel Grouping Transparency**
When grouping source/medium into channels, show the grouping logic if asked.
Never silently reclassify a source — if it doesn't fit cleanly, flag it.

**Guardrail 10 — Funnel Data From Screenshots Only**
Funnel completion rates and abandonment rates must come from the GA4 funnel screenshots
the user provides — not from calculating ratios from the landing page CSV (which represents
landing page entry data, not in-session funnel behavior).
