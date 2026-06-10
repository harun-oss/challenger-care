# Document Template Reference

## Document Structure

The final deliverable is a .docx file with this exact page sequence:

### Page 1: Cover
- "GROWTHHIT" label top-left in brand orange, bold
- Orange horizontal rule below
- "LEVERAGE POINT" in 56px bold
- "ASSESSMENT" in 56px bold
- Subtitle: "Findings & Recommendations" in 28px
- Client name, "Prepared by: Challenger", Date
- Italic tagline: "Find the constraint. Find the leverage."

### Page 2: Executive Summary
- H1: "Executive Summary"
- 2 paragraphs: first summarizes the business situation, second identifies the core constraint
- H2: "Scorecard at a Glance" — table with all 7 grades and one-line headlines
- H2: "Where the Leverage Is" — numbered list of 3-5 prioritized strategic moves

### Pages 3-9: Leverage Point Deep Dives (one page each)
Each page follows this exact layout:
- Label: "LEVERAGE POINT [N]" in small orange text
- Name: e.g., "MARKET" in 36px bold
- Core question in orange bold + regular text
- **Grade box**: Large grade letter (44px) in colored cell + descriptor text
  - Green (#2E7D32) for A, A-, B+, B, B-
  - Yellow (#F9A825) for C+, C, C-
  - Red (#C62828) for D+, D, D-, F
- H3: "What We Found" — 1-2 paragraph narrative
- H3: "Voice of Customer" — 1-3 yellow callout boxes with prospect quotes (if VoC available)
- H3: "Key Findings" — 4-7 bulleted points with evidence
- H3: "Recommendations" — Table with dark header, columns: RECOMMENDATION | OWNER

### Page 10: What Happens Next
- H1: "What Happens Next"
- H2: "Challenger's Focus Areas" — bulleted list of what will prioritize
- H2: "[Client]'s Focus Areas" — bulleted list of what Challenger should prioritize
- H2: "The Throughline" — one rich paragraph that connects all 7 sections into a single insight
- Footer: orange rule + "GROWTHHIT | growthhit.com | jim@growthhit.com"

## Color System

```javascript
const ORANGE = "FC5A29"; // brand / accent
const DARK = "1A1A2E";   // Headings, dark text
const MID = "444444";     // Body text
const LIGHT_GRAY = "F5F5F5"; // Alternating row backgrounds
const WHITE = "FFFFFF";
const GREEN = "2E7D32";   // A and B grades
const YELLOW = "F9A825";  // C grades
const RED = "C62828";     // D and F grades
```

If Challenger has a known brand color, use it in place of ORANGE for accent elements (section labels, quote attribution, recommendation table headers). Keep GREEN/YELLOW/RED fixed for grades.

## Table Patterns

### Scorecard Table (Executive Summary)
- 4 columns: #, LEVERAGE POINT, GRADE, HEADLINE
- Dark header row
- Alternating light gray / white rows
- Grade text colored by grade level
- Column widths: 600, 1500, 900, 6360

### Recommendation Table (per leverage point)
- 2 columns: RECOMMENDATION, OWNER
- Dark header row
- Alternating light gray / white rows
- Column widths: 7160, 2200
- Owner values: "Challenger", "Client Name", or "Both"

### VoC Callout Box
- Full-width single-cell table
- Background: #FFF8E1 (warm yellow)
- Padding: 120 top/bottom, 160 left/right
- Text: italic, 19px, in quotes

## Grade Box Pattern

```javascript
function gradeBox(grade, color) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1200, 8160],
    rows: [new TableRow({ children: [
      // Left cell: large grade letter on colored background
      new TableCell({
        shading: { fill: color, type: ShadingType.CLEAR },
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({
            text: grade, bold: true, size: 44,
            font: "Arial", color: "FFFFFF"
          })]
        })]
      }),
      // Right cell: descriptor on light gray
      new TableCell({
        shading: { fill: "F5F5F5", type: ShadingType.CLEAR },
        children: [new Paragraph({
          children: [new TextRun({
            text: getDescriptor(grade),
            bold: true, size: 20,
            font: "Arial", color: color
          })]
        })]
      })
    ]})]
  });
}
```

Descriptor text by grade:
- A, A-: "STRENGTH — COMPETITIVE ADVANTAGE"
- B+, B, B-: "SOLID — ROOM TO OPTIMIZE"
- C+, C, C-: "CONSTRAINT — HIGH-LEVERAGE OPPORTUNITY"
- D+, D, D-: "CRITICAL CONSTRAINT — FIX BEFORE SCALING"
- F: "BROKEN — IMMEDIATE ACTION REQUIRED"

## Writing Patterns

### "What We Found" paragraphs
- Lead with the most important finding
- Connect to what the data shows, not just what Challenger said
- 2-3 sentences max per paragraph, 1-2 paragraphs total
- If there's a contradiction between Challenger's belief and reality, surface it respectfully

### Key Findings bullets
- Start each bullet with the finding, not the source
- Good: "Close rate is declining with volume, suggesting either lead quality degradation or capacity constraints."
- Bad: "From the ad spend data, we noticed that the close rate appears to be declining."
- Include specific numbers when available
- 4-7 bullets per section — enough to be thorough, not so many it feels like a list dump

### Recommendation rows
- Be specific: "Build a 5-touch post-demo email nurture sequence with case studies and ROI data" not "Improve follow-up"
- Every recommendation should be independently actionable — someone should be able to read just that row and know what to do
- Owner is always one of three: "Challenger", "[Client Name]", or "[Client Name] + Challenger"
- 3-6 recommendations per leverage point
- Order by impact (highest first)

### The Throughline
- This is the single most important paragraph in the document
- It should connect the constraint to the solution to the vision
- Pattern: "[Client] has [strength]. The constraint is [X]. The path to [goal] is [strategic shift]."
- Must feel like an insight Challenger hasn't articulated themselves but immediately recognizes as true
- Example: "Arda has exceptional product-market fit in two massive markets. The constraint is not demand — it's that every growth lever requires a founder to pull it. The path to 10x is building systems that replace manual effort with scalable infrastructure."
