# Research Sources — Mapping to Test Opportunities

## How to use this reference

Each research source surfaces a different class of CRO problem. When building a roadmap, identify which research sources are available for a client, then map findings to the test opportunity categories below. This ensures every roadmap item has at least one evidence-backed research source, which is required for Confidence scoring above 4.

---

## Research source map

### Heuristic Analysis (Baymard Institute framework)

**What it surfaces:**
- UX friction points (navigation, form design, hierarchy failures)
- Trust signal gaps (missing reviews, weak social proof, no credentials)
- Layout and visual hierarchy problems
- Mobile-specific UX issues
- Information architecture failures

**Test opportunities it generates:**
- Layout and page structure tests (Core Test / Big Swing)
- Trust signal placement and format tests (Quick Win / Core Test)
- Navigation and CTA clarity tests (Quick Win)
- Mobile-specific UX improvements (Core Test)
- Form optimization tests (Quick Win / Core Test)

**Confidence contribution:** Single strong source — supports Confidence 6–7 on its own. Combine with VoC or behavioral data for 8+.

---

### VoC / Exit-Intent Survey Data

**What it surfaces:**
- The exact words customers use to describe their problem and your product
- Objections that prevent conversion ("I'm not sure about the price" / "I couldn't find X")
- Confusion points ("I didn't understand what all-inclusive meant")
- What almost stopped them from buying/converting
- What they wish they'd known sooner

**Test opportunities it generates:**
- Messaging and headline copy tests (Quick Win — highest-leverage VoC application)
- Objection-handling copy additions (Quick Win)
- FAQ and information architecture tests (Core Test)
- Social proof format tests (Quick Win / Core Test)
- Value proposition clarity tests (Quick Win)

**Confidence contribution:** Strongest source for copy and messaging tests — supports Confidence 8–9 for headline/copy tests when customer language is directly available. Also boosts Confidence for any trust signal or information gap test.

**Note:** VoC is the only source that gives you *customer vocabulary* — words you can put directly into test copy without inventing language.

---

### Heatmap & Scroll Map Analysis

**What it surfaces:**
- Where users actually look and click vs. where you expect them to
- Ignored CTAs or sections with high impressions but low interaction
- Rage clicks (users clicking on non-clickable elements, signaling confusion)
- Scroll depth drop-off (content below a certain fold is never seen)
- Mobile vs. desktop attention differences

**Test opportunities it generates:**
- CTA placement tests — move CTAs to where attention actually is (Core Test)
- Above-fold content prioritization tests (Core Test / Big Swing)
- Removing or de-emphasizing ignored sections (Quick Win / Core Test)
- Element clarity tests — what are users trying to click that isn't clickable? (Quick Win)
- Section reordering tests based on attention patterns (Core Test)

**Confidence contribution:** Strong behavioral signal — supports Confidence 7–8 for attention and placement tests. Combine with VoC for 9+.

---

### Form Abandonment Analytics

**What it surfaces:**
- Exactly which form field or step has the highest drop-off
- Time spent per field (long time = confusion or hesitation)
- Fields with high error rate (format mismatch or unclear expectations)
- Step-level completion rates in multi-step forms

**Test opportunities it generates:**
- Field removal or simplification tests (Quick Win — highest-leverage form optimization)
- Field label and placeholder copy tests (Quick Win)
- Field sequence reordering tests (Core Test)
- Progress indicator tests for multi-step forms (Quick Win / Core Test)
- Form length reduction tests — collect less upfront (Core Test)

**Confidence contribution:** Highly specific — supports Confidence 8–9 for the specific form step or field identified. The most quantified of all research sources (exact drop-off % by field).

---

### Analytics / GA4

**What it surfaces:**
- High-traffic, low-converting pages (where Impact is highest)
- Device type split (mobile vs. desktop CVR differences)
- Traffic source breakdown (organic vs. paid vs. direct behave differently)
- Exit pages (where users leave the funnel)
- Page speed issues (Time to First Byte, Core Web Vitals)
- Returning vs. new visitor conversion rate differences

**Test opportunities it generates:**
- Page-level conversion optimization (Impact scoring — which pages deserve tests most)
- Device-specific UX improvements (mobile vs. desktop separate test variants)
- Traffic-source-specific landing page tests (Core Test)
- Page speed and technical performance improvements (Core Test / Big Swing)
- Return visitor personalization (Big Swing)

**Confidence contribution:** Medium — supports Confidence 5–6 as a standalone source. GA4 tells you *where* the problem is but not *why*. Combine with heatmaps or VoC for higher Confidence.

---

### Competitive Analysis

**What it surfaces:**
- Trust signals, proof formats, or social proof volumes that competitors have and you don't
- Copy angles and value propositions competitors use that resonate
- Offer structures (pricing, bundles, guarantees) that competitors use
- UX patterns common in the space that users may now expect
- Missing features or information compared to competitive alternatives

**Test opportunities it generates:**
- Trust signal gap tests (Quick Win — add what competitors have)
- Offer/guarantee structure tests (Core Test)
- Messaging angle tests inspired by competitive positioning (Quick Win / Core Test)
- Feature comparison or differentiation copy tests (Quick Win)

**Confidence contribution:** Low-Medium — supports Confidence 4–6. Competitive inspiration needs user data validation. "Competitors do it" is not proof it will work for your audience — treat as a hypothesis generator, not a validation tool.

---

### Copy/Messaging Audit (Seven Sweeps)

**What it surfaces:**
- Clarity failures in headlines and CTAs
- Missing or weak proof
- Generic features with no benefit bridges
- Emotional disconnects in the copy
- Zero-risk signals missing near CTAs
- Voice/tone inconsistencies

**Test opportunities it generates:**
- CTA copy tests (Quick Win — almost always Ease 9–10)
- Headline/hero copy tests (Quick Win / Core Test)
- Trust and proof addition tests (Quick Win)
- Feature-to-benefit copy rewrites (Quick Win)
- Zero-risk element addition tests (Quick Win)

**Confidence contribution:** Medium — supports Confidence 5–7 for copy tests. Combine with VoC data (actual customer language) to reach 8+. A copy audit without VoC data identifies structural problems; VoC data tells you what to replace the bad copy with.

---

## Research source combinations and their Confidence impact

| Sources combined | Confidence range | Notes |
|-----------------|-----------------|-------|
| VoC + Heatmap | 8–9 | Behavioral + attitudinal — strongest combination |
| VoC + Form Abandonment | 8–9 | Best for form optimization tests |
| Heuristic + VoC | 7–9 | UX gap confirmed by customer voice |
| Heuristic + Heatmap | 7–8 | UX gap confirmed by behavior |
| VoC only | 6–8 | Strong for copy; medium for UX |
| Heatmap + Form Abandonment | 7–8 | Best for funnel and engagement tests |
| Analytics only | 4–6 | Quantifies the problem but not the cause |
| Competitive only | 3–5 | Hypothesis generator, not validation |
| Team brainstorm only | 1–3 | Cap Confidence here until research confirms |
