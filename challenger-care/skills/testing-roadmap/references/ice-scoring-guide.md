# ICE Scoring Framework — Full Guide

## Origins

ICE scoring was popularized by Sean Ellis (the "growth hacking" practitioner who coined the term). It's widely used in CRO, product growth, and marketing experimentation because it's fast, collaborative, and forces prioritization on three dimensions simultaneously.

uses ICE as the backbone of the testing roadmap, customized with:
- funnel stage tagging
- Research source requirement (no research = low Confidence cap)
- Portfolio balance overlay (40/40/20 rule)
- Reassessment cadence (after every completed test)

---

## Scoring dimension deep-dives

### Impact — "How much does this matter if it wins?"

The key question is: what's the realistic upside if this test produces a winner?

**Factors that increase Impact:**
- High traffic to the target page (>10,000 sessions/month = strong)
- High-stakes conversion action (form submit, purchase, phone call)
- Sitewide or high-frequency element (navigation, hero, primary CTA)
- Target page has a known conversion problem (high drop-off rate)
- Estimated CVR delta is meaningful (even a 0.5% lift on 50K sessions = 250 extra conversions)

**Factors that decrease Impact:**
- Low-traffic page (<500 sessions/month)
- Secondary or micro-conversion (email sign-up for blog, breadcrumb click)
- Element that most users never see (below-fold on mobile, hidden tab)

**Worked example:**
NBC Step 1 page: 15,000 monthly sessions. Current CVR to Step 2 = 32%. A 3% relative lift = 144 more completions/month. At $45 CPL value, that's $6,480/month. → Impact: 9

NBC Thank You page: 400 monthly sessions, no tracked goal. → Impact: 2

### Confidence — "How sure are we this will work?"

Confidence is entirely about the strength and quantity of your evidence. It is not about how much you like the idea.

**Evidence hierarchy (highest to lowest Confidence):**

| Evidence type | Max Confidence score |
|---------------|---------------------|
| Multiple aligned research sources (VoC + heatmap + heuristic all pointing to same issue) | 9–10 |
| Two aligned sources (VoC + analytics, or heatmap + form abandonment) | 7–8 |
| Single strong source (VoC with direct customer language) | 6–7 |
| Single moderate source (heuristic observation, analyst note) | 4–6 |
| Competitive inspiration only (competitor does it, no user data) | 3–4 |
| Team gut feel / "it looks bad" | 1–3 |

**Worked examples:**
VoC shows 23% of respondents mention "not sure about fees" → heatmap shows users rage-clicking the pricing section → analytics shows 40% exit from pricing page. Three aligned signals. Confidence: 9.

PM thinks the hero image "doesn't look modern enough." No data. Confidence: 2.

### Ease — "How hard is this to build?"

Ease is about the combined design + development effort. Get input from the designer and developer when scoring this — PMs tend to underestimate dev effort.

**Calibrated Ease scale:**

| Score | Effort | Examples |
|-------|--------|---------|
| 10 | <1 hour — copy change in CMS | Headline swap, button text, meta description |
| 9 | 1–4 hours — minor content edit | New headline + subhead, swap one image, reorder list items |
| 8 | Half day — small design change | New CTA button color/size, add trust badge, show/hide element |
| 7 | 1 day — design + light dev | New above-fold layout with existing components |
| 6 | 2–3 days — new component | Add testimonial carousel, social proof bar, sticky CTA |
| 5 | 3–5 days — new section | New hero design, restructured form, new product grid |
| 4 | 1 week — page section overhaul | Full above-fold redesign, new checkout step, new modal |
| 3 | 2 weeks — new page template | Full page redesign with new content strategy |
| 2 | 1 month — complex build | New checkout flow, new onboarding sequence |
| 1 | 2+ months — major system change | Full site architecture change, back-end integration |

---

## ICE in practice: worked examples

### Example 1: B2C lead-gen (NBC-style)

**Test idea:** Replace "Submit" button copy with "Get My Free Rate Analysis"
- Impact: 8 (Step 1 is highest-traffic page; CTA clicks are primary goal)
- Confidence: 8 (VoC shows "Submit" feels generic; heuristic identified low CTA specificity)
- Ease: 10 (copy change in CMS)
- **ICE: 640** → Quick Win, launch immediately

**Test idea:** Full Step 1 page redesign with new hero layout and progressive disclosure form
- Impact: 9 (primary conversion page)
- Confidence: 6 (heuristic supports hierarchy change, but no direct user language for the new layout)
- Ease: 3 (2-week dev effort for new template)
- **ICE: 162** → Big Swing, schedule for later sprint

**Test idea:** Add favicon to browser tab
- Impact: 1 (no conversion impact)
- Confidence: 1
- Ease: 10
- **ICE: 10** → Remove from roadmap entirely

### Example 2: B2B lead-gen (RISE-style)

**Test idea:** Add "Spaces Available Near You" location-aware headline on homepage
- Impact: 7 (homepage gets 12K sessions/month)
- Confidence: 7 (heatmap shows users first look at location section; VoC mentions "is there one near me?")
- Ease: 5 (location API integration needed)
- **ICE: 245** → Core Test

**Test idea:** Social proof bar with "1,200+ businesses call RISE home"
- Impact: 7 (sitewide element, high visibility)
- Confidence: 8 (heuristic analysis identified missing quantified social proof; competitor benchmarking shows this pattern converts)
- Ease: 8 (design + light CSS)
- **ICE: 448** → Quick Win / Core Test boundary

---

## Portfolio balance worked example

After ICE scoring 20 test ideas, the ranked list might look like:

| Rank | ICE | Category | Status |
|------|-----|---------|--------|
| 1 | 640 | Quick Win | → Launch |
| 2 | 560 | Quick Win | → Launch |
| 3 | 490 | Core Test | → Design |
| 4 | 448 | Quick Win | → Design |
| 5 | 380 | Core Test | → Planning |
| 6 | 320 | Core Test | → Planning |
| 7 | 280 | Quick Win | → Backlog |
| 8 | 245 | Core Test | → Backlog |
| 9 | 200 | Big Swing | → Backlog |
| 10 | 180 | Big Swing | → Backlog |
...

The top 8 are all Quick Wins or Core Tests. Portfolio check: need 2 Big Swings in the active design/planning pipeline. Bump items 9 and 10 up even though ICE is lower — they challenge the paradigm and create compounding learnings.

---

## Reassessment triggers

Reassess ICE scores whenever:
- A related test concludes (learnings may increase or decrease Confidence on other items)
- Traffic changes significantly on target pages (affects Impact)
- New research is completed (heuristic, VoC, heatmap — affects Confidence)
- Dev or design capacity changes (affects Ease)
- A competitor launches a significant site change (may affect Confidence for competitive-inspired tests)
- A test has been in the backlog for >3 months without launching (ask: is this still the right thing to test?)

---

## Common ICE scoring debates

**"This feels like it should be higher Impact" — but the traffic is low**
ICE is honest about traffic. If the page only gets 300 sessions/month, even a 50% CVR lift produces almost nothing at scale. Score it accurately and park it unless traffic increases.

**"We have no user research" — client pushed back on research investment**
Cap Confidence at 4 for any idea without direct user data. Explain to Challenger: low-Confidence tests produce more inconclusive results, wasting test cycles. The research investment pays for itself by increasing test win rate.

**"This is so easy and we're sure it'll work — why isn't it higher priority?"**
Check Impact. If it's a sitewide change on a high-traffic page, it should be high priority. If it's on a low-traffic page with a micro-conversion, Ease 10 × Confidence 10 × Impact 2 = 200. That's still backlog material.

**"Big Swings always score lower in ICE"**
Yes, because Ease is low. That's intentional. Use the 20% portfolio rule to override pure ICE ranking for Big Swings. ICE is a starting point, not a dictator.
