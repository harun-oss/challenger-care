# Exit-Intent Poll — Methodology Reference

## Section 1: Question Type Reference

uses exactly one of two survey questions per poll. The question type determines
how themes are labeled, how the deliverable is framed, and what the CRO implications sound like.

| Question | Framing | Theme style | Deliverable title |
|---|---|---|---|
| "What's missing from this page that will help you make a purchase decision?" | Improvements | Needs / gaps | "[Client] — [Page] Exit-Poll Insights" |
| "What, if anything, prevented you from purchasing today?" | Barriers | Objections / blockers | "[Client] — [Page] Purchase Barrier Analysis" |

**Never mix the two.** If a client has run both surveys, produce two separate analyses.

---

## Section 2: Data Cleaning Rules

### Invalid Response Criteria (remove)
- Spam/gibberish: random characters, nonsense strings, repeated letters
- Test entries: "test", "testing", "asdf", "123"
- Zero-signal responses: blank, "n/a", "nothing", "no", "fine", "good"
- True duplicates: exact same text from the same session ID (if available)
- Off-topic: responses that clearly don't address the survey question
  (e.g., "I love your products!" in response to a "what's missing?" question)

### Borderline Responses (keep with caution)
- Short but meaningful ("too expensive", "no video") — keep, these are clear signals
- Generic but directional ("more info needed") — keep, but don't let these dominate themes
- Non-English responses — keep if the meaning is clear; note the language

### Device Segmentation (if available in export)
Hotjar CSV exports sometimes include device type (mobile/desktop/tablet).
If available:
- Segment analysis by device before coding — mobile users often request different things
  (delivery time, trust signals, simpler UX) than desktop users (detailed specs, comparisons)
- If device split is 80%+ one device type, do a combined analysis with a device note
- If 50/50+ split, consider presenting two sub-analyses within the same deliverable

### Minimum Response Thresholds
| Clean responses | Guidance |
|---|---|
| < 20 | Flag as low confidence. Findings are directional only. |
| 20–49 | Reasonable for directional insights. Caveat % precision. |
| 50–99 | Solid for reliable category percentages. |
| 100+ | Statistically robust. Consider secondary segmentation (device, page variant). |

---

## Section 3: Category Coding Conventions

### Theme Label Style by Question Type

**Improvements framing ("What's missing?"):**
- Label themes as content/feature gaps the visitor wants
- Use noun phrases: "Product Comparison", "How-To Video", "Delivery Information"
- Do NOT use negative framing ("Lack of comparison") — use the positive want

**Barriers framing ("What prevented you?"):**
- Label themes as the objection or blocker
- Use noun phrases: "Price Concern", "Shipping Uncertainty", "Size / Fit Anxiety"
- Reflect what stopped them, not what they want added

### Common Theme Patterns by Question Type

**"What's missing?" — frequent themes across DTC clients:**
| Theme | What it includes |
|---|---|
| Price / Discount | Requests for promo codes, sales, lower price, bundle deals |
| Product Comparison | Requests to compare variants, models, sizes against each other |
| How-To / Usage Content | Requests for video, GIF, demo, instructions on how to use/wear/set up |
| Delivery / Shipping Info | Delivery timelines, shipping costs, next-day availability, location-specific ETA |
| Product Details | Materials, dimensions, weight, specs, construction, origin |
| Social Proof / Reviews | More reviews, star ratings, before/after, UGC photos |
| Size / Fit Guide | Sizing charts, fit videos, measurement guidance |
| Other | Catch-all for themes < 3% |

**"What prevented you?" — frequent themes across DTC clients:**
| Theme | What it includes |
|---|---|
| Price Concern | Too expensive, looking for a deal, will wait for a sale |
| Shipping Uncertainty | Cost of shipping, delivery time unclear, international shipping |
| Product Clarity | Unsure how it works, unclear specs, confused by variants |
| Trust / Social Proof | Not enough reviews, unfamiliar brand, need more evidence |
| Just Browsing | Not ready to buy, researching, comparing options |
| Size / Fit Uncertainty | Unsure if it will fit, no size chart, no returns info |
| Other | Themes < 3% |

### Merging Rules
- Merge if two themes share the same root cause (even if worded differently by visitors)
- Do NOT merge themes that have the same volume if they represent clearly different concerns
- Maximum 8 themes in the final analysis — combine the smallest into "Other" to stay clean
- "Other" should never exceed 10% — if it does, check if a hidden theme exists

---

## Section 4: PPTX 3-Slide Build Spec

When the user selects PPTX, build using brand guidelines. Read
`../../../growthit-brand/assets/growthit-brand.md` or reference the `brand-kit` skill for full specs.
Quick reference: primary blue `#4677F7`, background `#F5F7F9`, cover `#000000`,
title font Poppins Bold, body font Mulish Regular. Exact slide structure:

### Slide 1: Cover
- Background: `#000000` (black)
- Client name: `#4677F7` (Blue), Poppins Bold, 18pt, top-left ~x:0.5, y:1.0
- Title: white, Poppins Bold, 42pt — "[Page] Exit-Poll Insights" or "[Page] Purchase
  Barrier Analysis" depending on question type
- Blue accent underline: `#4677F7` rectangle, ~3.5" wide, 0.04" tall, below title
- Month/Year: white, Mulish Regular, 16pt
- "Prepared by" + GROWTHHIT logo: bottom-left — "GROWTH" black-on-white, "HIT" blue
- No progress dots on cover slide

### Slide 2: Executive Summary
- Background: `#F5F7F9`
- Header: label tag "[IMPROVEMENTS]" or "[BARRIERS]" in black filled tag, Poppins Bold
- Title: survey question in italic blue Mulish, ~13pt, below header
- Left column (~55% width): "Executive Summary:" bold heading, bulleted list of themes
  with percentages — highlight the top 3 percentages in Blue
- Right column (~40% width): "VOICE OF VISITORS" section label in `#4677F7` bold uppercase;
  10-15 verbatim quotes in Mulish Regular, ~11pt, light gray quote marks
- Footer: progress dots bottom-left, GROWTHHIT logo bottom-right

### Slide 3: Results
- Background: `#F5F7F9`
- Header: label tag "[RESULTS]" in black filled tag
- Title: "[Page] Exit-Poll Results", Poppins Bold 22pt
- Response count note: "[N] responses collected. Invalid responses removed." Mulish 12pt.
- Left side: data table
  - Header row: `#4677F7` fill, white Poppins Bold — "Categories | Volume | Percentage"
  - Alternating rows: `#DCE6FD` (light blue) for top themes, white for lower themes
  - Row text: Mulish Regular, 12pt, black
- Right side: bar chart
  - Bars: `#4677F7` (Blue), no border
  - X-axis: category names, Mulish 9pt
  - Y-axis: percentages (0% to max+5%), Mulish 9pt
  - Data labels: % shown above each bar, Poppins Bold 10pt
  - No chart border, light gray horizontal gridlines only
- Footer: progress dots, GROWTHHIT logo

---

## Section 5: CRO Hypothesis Templates

For each of the top 3 themes, write one specific testable hypothesis.
Use this structure: "[Theme] suggests testing [specific change] on the [page element]."

**Examples by theme:**
- Price/Discount → "The 37% discount signal suggests testing a visible 'Subscribe & Save'
  or limited-time offer badge on the ATC button."
- How-To/Usage → "The 23% how-to gap suggests testing a product demo video in the first
  media carousel slot above the fold."
- Product Comparison → "The 14% comparison request suggests testing a 'Compare Models'
  interactive table in the product description section."
- Delivery → "The 10% delivery uncertainty suggests testing a dynamic estimated delivery
  date display below the ATC button, localized by visitor IP."
- Social Proof → "The 4% review gap suggests testing an expanded review module showing
  the full review count rather than a capped 10."

**Rules for CRO hypotheses:**
- Always reference the specific % from the analysis — grounds the recommendation in data
- Name the specific page element to change (not just "the PDP")
- One hypothesis per theme — keep it tight
- Never recommend something not supported by the actual response data

---

## Section 6: Multi-Wave Tracking (if prior data exists)

If Challenger has run this poll before and prior analysis exists:
- Compare current % distribution against prior distribution
- Flag: shrinking themes (Challenger may have addressed that gap), growing themes
  (a worsening issue), and stable themes (persistent barriers worth prioritizing for tests)
- Add a "Trend" column to the results table: ↑ / ↓ / → with previous %

Example: "Delivery concerns dropped from 18% to 10% — consistent with the shipping
timeline copy update they made in September."
