# Quantitative Analysis — Design System Reference

## Section 1: HTML Preview CSS Classes

Use these exact class names and styles when building the Visualizer preview.
The preview must match the PPTX layout faithfully — same card structure, same colors.

```css
.deck          { display: flex; flex-direction: column; gap: 24px; font-family: Calibri, sans-serif; }
.slide         { background: #E6ECF5; border-radius: 8px; padding: 22px 26px;
                 aspect-ratio: 16/9; position: relative; overflow: hidden; }
.slide-num     { position: absolute; top: 10px; right: 10px; color: #888; font-size: 9px; }
.slide-title   { font-size: 15px; font-weight: bold; color: #1A1A1A; margin-bottom: 10px; }
.slide-title::before { content: "— "; color: #4285F4; }
.badge         { display: inline-flex; align-items: center; justify-content: center;
                 width: 22px; height: 22px; border-radius: 50%;
                 background: #1A1A1A; color: #fff; font-size: 10px; font-weight: bold; }
.card          { background: #fff; border-radius: 6px; padding: 10px 12px; }
.card-orange   { border-left: 3px solid #ED6C30; }
.card-green    { border-left: 3px solid #34A853; }
.card-blue     { border-left: 3px solid #4285F4; }
.card-red      { border-left: 3px solid #EA4335; }
.card-gray     { border-left: 3px solid #888888; }
.card-black    { border-left: 3px solid #1A1A1A; }
.card-top-orange { border-top: 3px solid #ED6C30; }
.card-top-green  { border-top: 3px solid #34A853; }
.card-top-blue   { border-top: 3px solid #4285F4; }
.card-top-black  { border-top: 3px solid #1A1A1A; }
.stat-big      { font-size: 22px; font-weight: bold; color: #1A1A1A; }
.stat-med      { font-size: 17px; font-weight: bold; color: #1A1A1A; }
.stat-label    { font-size: 9px; color: #666; }
.stat-sub      { font-size: 8px; color: #999; }
.grid-3        { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
.grid-4        { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
.section-label { font-size: 9px; color: #4285F4; font-weight: bold; text-transform: uppercase; }
.tag-red       { background: #FDECEA; color: #EA4335; font-size: 8px;
                 padding: 2px 5px; border-radius: 3px; display: inline-block; }
.tag-green     { background: #E6F4EA; color: #34A853; font-size: 8px;
                 padding: 2px 5px; border-radius: 3px; display: inline-block; }
.title-slide   { background: #1A1A1A !important; display: flex;
                 flex-direction: column; justify-content: center; padding: 40px; }
.finding-row   { display: flex; align-items: flex-start; gap: 8px; margin-bottom: 6px; }
.table-header  { display: flex; align-items: center; gap: 8px;
                 font-size: 8px; color: #666; font-weight: bold;
                 padding: 4px 8px; background: #f5f5f5; border-radius: 4px; }
.table-row     { display: flex; align-items: center; gap: 8px;
                 padding: 5px 8px; background: #fff; border-radius: 4px; margin-bottom: 3px; }
```

---

## Section 2: PPTX Color Constants

```javascript
const C = {
  bg:         "E6ECF5",   // Slide background
  blue:       "4285F4",   // Primary accent
  black:      "1A1A1A",   // Text, badges
  orange:     "ED6C30",   // Secondary accent
  green:      "34A853",   // Positive/success
  red:        "EA4335",   // Negative/critical
  white:      "FFFFFF",
  gray:       "888888",
  darkGray:   "555555",
  cardBg:     "FFFFFF",
  greenBg:    "E6F4EA",   // Light green background
  redBg:      "FDECEA",   // Light red background
  orangeBg:   "FEF3E8",   // Light orange background
  heatRed:    "F09595",   // Heatmap red cell
  heatRedDark:"f7c1c1",   // Heatmap light red cell
  heatOrange: "f5c4b3",   // Heatmap orange cell
  heatGreen:  "C0DD97",   // Heatmap green cell
};
const FONT = "Calibri";
```

---

## Section 3: PPTX Helper Functions

Implement these helper functions exactly. They must produce consistent output across all slides.

```javascript
// Fresh shadow object — use for all cards
function makeShadow() {
  return { type: "outer", blur: 4, offset: 1, angle: 135, opacity: 0.08, color: "000000" };
}

// White card with optional left border
function addCard(sl, x, y, w, h, borderColor = null) {
  const opts = {
    x, y, w, h,
    fill: { color: C.cardBg },
    line: borderColor ? { color: borderColor, width: 2 } : { color: "DDDDDD", width: 0.5 },
    shadow: makeShadow(),
    rectRadius: 0.05,
  };
  if (borderColor) {
    // Simulate left border with a thin filled rectangle
    sl.addShape(pptx.ShapeType.rect, {
      x, y, w: 0.04, h,
      fill: { color: borderColor },
      line: { color: borderColor, width: 0 },
    });
  }
  sl.addShape(pptx.ShapeType.rect, { ...opts, x: x + (borderColor ? 0.04 : 0), w: w - (borderColor ? 0.04 : 0) });
}

// White card with top border
function addCardTop(sl, x, y, w, h, borderColor = null) {
  if (borderColor) {
    sl.addShape(pptx.ShapeType.rect, {
      x, y, w, h: 0.04,
      fill: { color: borderColor },
      line: { color: borderColor, width: 0 },
    });
  }
  sl.addShape(pptx.ShapeType.rect, {
    x, y: y + (borderColor ? 0.04 : 0), w, h: h - (borderColor ? 0.04 : 0),
    fill: { color: C.cardBg },
    line: { color: "DDDDDD", width: 0.5 },
    shadow: makeShadow(),
    rectRadius: 0.05,
  });
}

// Big number + label centered in a card
function addMetric(sl, x, y, w, val, lbl, clr = C.black, sz = 22) {
  sl.addText(String(val), {
    x, y: y + 0.05, w, h: 0.3,
    fontSize: sz, bold: true, color: clr, align: "center", fontFace: FONT,
  });
  sl.addText(lbl, {
    x, y: y + 0.32, w, h: 0.15,
    fontSize: 8, color: C.gray, align: "center", fontFace: FONT,
  });
}

// Small gray sub-text below a metric
function addSubText(sl, x, y, w, txt) {
  sl.addText(txt, {
    x, y, w, h: 0.12,
    fontSize: 7, color: C.gray, align: "center", fontFace: FONT,
  });
}

// Black circle with white number
function addBadge(sl, x, y, num) {
  sl.addShape(pptx.ShapeType.ellipse, {
    x, y, w: 0.22, h: 0.22,
    fill: { color: C.black },
    line: { color: C.black, width: 0 },
  });
  sl.addText(String(num), {
    x: x - 0.01, y: y + 0.02, w: 0.24, h: 0.18,
    fontSize: 9, bold: true, color: C.white, align: "center", fontFace: FONT,
  });
}

// Blue uppercase section header
function addSectionLabel(sl, x, y, w, txt) {
  sl.addText(txt, {
    x, y, w, h: 0.15,
    fontSize: 8, bold: true, color: C.blue,
    align: "left", fontFace: FONT, charSpacing: 1,
  });
}

// Slide title with blue "— " prefix
function slideTitle(sl, txt) {
  sl.addText([
    { text: "— ", options: { color: C.blue } },
    { text: txt, options: { color: C.black } },
  ], {
    x: 0.3, y: 0.1, w: 9, h: 0.3,
    fontSize: 14, bold: true, fontFace: FONT,
  });
}
```

---

## Section 4: Slide-by-Slide Build Specifications

All slides are 10" × 5.63" (standard 16:9). Slide number shown top-right at 9px gray.

### Slide 1: Title (background #1A1A1A)
- Brand name: 36pt bold white, `x:0.5, y:1.5`, left-aligned
- Blue accent line: rectangle `x:0.5, y:2.05, w:1.2, h:0.04`, fill `#4285F4`
- Subtitle "Quantitative Site Analysis": 16pt `#888888`, `x:0.5, y:2.2`
- URL: 12pt light gray `#666666`, `x:0.5, y:2.55`
- Date range + " · GA4 Data": 10pt `#555555`, `x:0.5, y:4.9` (bottom-left)

### Slide 2: Executive Summary
- Title: `slideTitle(sl, "Executive summary")`
- Row 1 (y:0.55): Three metric cards with left borders — Users (blue), Revenue (green), Purchases (orange)
  - Each card: `x: [0.3, 3.5, 6.7], w:3.0, h:0.85`
- Row 2 (y:1.55): Four secondary cards with top borders — CVR (blue), AOV (orange), ATC Rate (green), Rev/User (gray)
  - Each card: `x: [0.3, 2.8, 5.3, 7.8], w:2.3, h:0.75`
- Section label "KEY FINDINGS" at `y:2.5`
- 5 finding rows with black badges starting at `y:2.75`, each row `h:0.35`

### Slide 3: Site-Wide Funnel
- Title: `slideTitle(sl, "Site-wide funnel")`
- Left side (x:0.3, w:5.5): Four trapezoid funnel bars, narrowing proportionally
  - Each bar height: proportional to user count relative to top-of-funnel
  - Bar colors (top to bottom): `#4285F4`, `#5C9CF5`, `#82B4F7`, `#34A853`
  - White bold number centered on bar; step label to the right
  - Drop annotation between bars: "↓ X% drop · Y lost" in `#EA4335`
- Right side (x:6.0, w:3.7): Three callout cards, top-bordered
  - Card 1: ATC→CO drop % (red top border)
  - Card 2: CO→Purchase rate (green top border)
  - Card 3: AOV (blue top border)

### Slide 4: Funnel by Entry Point
- Title: `slideTitle(sl, "Funnel by entry point")`
- Left 70% (x:0.3, w:6.8): Three waterfall column charts side-by-side (HP / CLP / PDP)
  - Each waterfall: colored title, user count subtitle
  - Vertical bars decreasing in height proportional to step completion %
  - ATC bar: red-colored, red % label, "ATC" label below
  - Green "end CVR" badge at bottom of each waterfall
- Right 30% (x:7.3, w:2.5): Heatmap grid card
  - Column headers: HP, CLP, PDP (in their respective accent colors)
  - Row labels: PDP→ATC, ATC→CO, CO→Purch, End CVR
  - Cell colors: red for PDP→ATC row, orange for ATC→CO, green for CO→Purch
  - End CVR row: color by performance (green/orange/red)
- Bottom (y:4.7): Three color-coded insight boxes spanning full width (red, orange, green)

### Slide 5: Traffic Source Breakdown
- Title: `slideTitle(sl, "Traffic source breakdown")`
- Table header row: Channel | Users | % Traffic | CVR | AOV | Revenue
- One white card per channel row, sorted by Users desc
- "Low CVR" tag (red) and "Top CVR" tag (green) on standout rows
- Rows with tags: red left border (Low CVR) or green left border (Top CVR)

### Slide 6: Top Individual Sources
- Title: `slideTitle(sl, "Top individual sources")`
- Same table format as Slide 5
- Columns: Source/Medium | Users | CVR | Purchases | Revenue | AOV
- Top 8 individual sources, tags for standout CVR performers

### Slide 7: Device Category
- Title: `slideTitle(sl, "Device category")`
- Left 65% (x:0.3, w:6.2): Stacked sections
  - Section label "MOBILE · X% OF TRAFFIC" → white card, orange left border
    - 4 metric boxes in 2×2 grid: Users, CVR, AOV, Rev/User (with colored bg)
    - Context line below card (e.g., "Mobile drives X% of traffic but only Y% of revenue")
  - Section label "DESKTOP · X% OF TRAFFIC" → white card, green left border
    - Same 4-metric structure
  - Tablet: compact single-row card, gray left border
- Right 35% (x:6.7, w:3.1): Three callout cards, top-bordered
  - Incremental revenue opportunity (orange top border)
  - Desktop CVR advantage multiplier (blue top border)
  - Desktop CO→Purchase rate (black top border)

### Slide 8: New vs Established Users
- Title: `slideTitle(sl, "New vs established users")`
- Identical layout to Slide 7 but for segments:
  - New users: orange-themed card (orange left border)
  - Established users: green-themed card (green left border)
  - Right callouts: CVR advantage multiplier, Rev/User advantage, Revenue concentration

### Slide 9: Top Landing Pages
- Title: `slideTitle(sl, "Top landing pages")`
- Top section: "TOP PERFORMING PAGES" label → 6–7 best pages
  - Table columns: Page | Users | ATC % | CVR | Revenue | AOV
  - Tags: "Top CVR" (green), "High CVR" (blue) on standout performers
- Bottom section: "HIGH-TRAFFIC LOW-CONVERSION PAGES" label
  - 2–3 worst high-traffic pages (>500 users, <1% CVR)
  - Red left borders, "Low CVR" and "Dead page" tags

### Slide 10: Key Findings & Opportunities
- Title: `slideTitle(sl, "Key findings & opportunities")`
- Two equal columns (x:0.3, w:4.6) and (x:5.2, w:4.6)
- Left column: "CRITICAL LEAKS" label → 3 cards
  - Red/orange left borders, numbered black badges, bold colored titles, gray body text
- Right column: "OPPORTUNITIES" label → 3 cards
  - Green/blue left borders, same structure
- All 6 findings must be grounded in actual data from Phases 1–2
