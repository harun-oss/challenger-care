# Ad Concept Templates

## Copy Doc Template

Use this template for every ad concept. One section per concept in the final document.

```
## [Concept Name]

**Format:** [Static Feed / Story / Carousel / Video / UGC-style]
**Angle:** [Angle name from Step 1]
**Inspired by:** [Which competitor ad or format from Step 2 informed this]

---

**Primary Text (above the fold):**
[Main ad copy — 2–3 sentences max. Write in the customer's voice, not brand voice.]

**Headline:**
[Bold headline — 30–40 characters max]

**Description:**
[Smaller text under headline — optional, 20–30 characters]

**CTA Button:** [Shop Now / Learn More / Get Yours / Try It Free]

---

**Visual Direction:**
[What the image or video should show — be specific. Name the shot type, the setting, the emotion on the person's face, any text overlays.]

**Source Quote:**
"[The real customer quote that inspired this concept — exactly as written]"
```

---

## Figma Frame Spec

When pushing concepts to Figma:

| Format | Canvas size | Notes |
|--------|-------------|-------|
| Feed (static or carousel) | 1080 x 1080px | Square |
| Story / Reels | 1080 x 1920px | Vertical full-screen |
| Banner / DPA | 1200 x 628px | Landscape |

**Frame naming convention:**
`[Angle Short Name] — [Format] — [YYYY-MM-DD]`
Example: `Meeting Confidence — Static Feed — 2025-06-01`

**Required layers in each Figma frame:**
1. Background / hero image placeholder (label: "IMAGE — replace with final asset")
2. Primary text layer (label: "PRIMARY TEXT")
3. Headline layer (label: "HEADLINE")
4. CTA button (label: "CTA")
5. Concept notes layer (locked, non-printing): angle name, source quote, inspired-by reference

---

## DOCX Branding Notes

When producing the copy doc as a DOCX:

- Read `../../../growthit-brand/assets/growthit-brand.md` for the full brand spec
- Cover page: black background (`#000000`), white title "Ad Concepts — [Brand] — [Date]", footer
- Section headers: Poppins Bold, 14pt, `#000000`
- Concept name: Poppins Bold, 12pt, `#4677F7`
- Body / copy text: Mulish Regular, 11pt, `#000000`
- Divider between concepts: thin rule in `#4677F7`
- Footer on every page: "GROWTH" (black) + "HIT" (`#4677F7`), Poppins Bold, right-aligned

Use the DOCX skill to build the file. Pass the brand parameters above directly.
