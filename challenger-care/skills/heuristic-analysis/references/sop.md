# CRO Heuristic Analysis — Full SOP Reference

Version 2.0 | March 2026 | Classification: Internal Reference

---

## Table of Contents

1. What Is a Heuristic Analysis?
2. Scope — All Key Pages
3. How to Identify Key Pages
4. Heuristic Dimensions
5. Per-Page Analysis Format
6. Anti-Hallucination Rules
7. Category-Specific Considerations
8. Summary Table
9. Deck Structure
10. QA Checklist
11. Post-Delivery Checklist
12. Brand Fallback Spec

---

## 1. What Is a Heuristic Analysis?

A heuristic analysis is Step 1 of Challenger's Conversion Research Process. A team of
optimisation experts, analysts, developers, and UX designers collaborate to find initial
high-level testing opportunities and set a roadmap for in-depth research.

The heuristic analysis covers ALL key pages of Challenger's website — not just product pages.
The goal is to give stakeholders a page-by-page picture of what is working, what is creating
friction, and where the highest-leverage research and testing opportunities exist.

This is a qualitative, expert-led audit. Findings are observations from experienced CRO
practitioners, informed by UX research principles (Baymard Institute, Nielsen Norman Group,
CXL), but grounded in what is actually present on Challenger's pages.

**The four steps of Challenger's Conversion Research Process:**

| Step | Name | Description |
|------|------|-------------|
| Step 1 | Heuristic Analysis (this SOP) | Expert review of all key pages; identifies high-level testing opportunities and research roadmap |
| Step 2 | Quantitative Research | Analytics review to pinpoint user segments, isolate behavioral trends, find highest-value funnels |
| Step 3 | Qualitative Research | Exit intent polls, session recordings, interviews, surveys to understand the "why" |
| Step 4 | Hypothesis Development | Data-driven hypotheses from Steps 1–3, proven or disproven through A/B testing |

---

## 2. Scope — All Key Pages

The audit must cover every page that plays a meaningful role in the user's journey from
awareness to conversion.

**Common page types by business model:**

| Business Model | Typical Key Pages to Audit |
|---------------|---------------------------|
| E-commerce | Homepage, Collection/Category page, Product Detail Page (PDP), Cart, Checkout step 1 |
| Lead Gen / B2B / SaaS | Homepage, Features/Product page, Pricing page, About/Team page, Contact or Demo page |
| Booking / Experiences | Homepage, Category/All tours page, Individual tour pages, Booking flow step 1, Blog/content pages |
| Content / Media | Homepage, Category pages, High-traffic articles, Email signup / lead capture page |

Aim for 5–10 pages per audit. Fewer than 5 is too shallow; more than 10 makes the deck unwieldy.

**Always confirm the page list with Challenger before fetching.** Do not guess URL patterns —
ask for the exact URLs.

---

## 3. How to Identify Key Pages

1. Ask Challenger: "Which pages do you consider most important for driving conversions? Which
   pages do users visit before they buy/book/sign up?"
2. Check analytics: Top pages by sessions, pages with highest drop-off, pages in the primary
   conversion funnel.
3. Walk the site: Start from the homepage and follow the most likely conversion path for a
   first-time visitor. Every page you land on is a candidate.

---

## 4. Heuristic Dimensions

Evaluate every page across these five dimensions. These map directly to the Summary Table.

| Dimension | What It Measures | High | Medium | Low |
|-----------|-----------------|------|--------|-----|
| Clarity | How easily a first-time visitor understands the page and what to do next | Clear, focused, no cognitive overload | Mostly clear but some confusion | Confusing or overwhelming |
| Trust | Whether the page builds confidence and reduces perceived risk | Strong trust signals near point of commitment | Some trust signals present | Few or no trust signals |
| CTA Strength | Whether the primary call-to-action is clear, visible, and compelling | Prominent, clear, appropriately repeated | CTA exists but weak or buried | CTA absent, confusing, or competing |
| Persuasion | Whether the page speaks to the user's motivations — emotional and functional | Strong outcome-focused, emotionally resonant messaging | Some benefit language mixed with features | Purely functional/spec-driven |
| Overall UX | The overall user experience — flow, information architecture, mobile experience | Smooth, intuitive experience | Some friction but generally workable | Significant UX issues |

---

## 5. Per-Page Analysis Format

Every page uses the same two-part structure:

### What Works
Identify 2–4 specific things the page does well. Be concrete — reference actual page elements,
copy, or design choices.

- Name the specific element (exact copy or structural feature observed)
- Explain why it works (which dimension it serves)
- Add a "Heuristics Notes" sub-point for nuance or caveats if relevant

**Good example:**
> **Strong social proof** — TripAdvisor #1 rating with 4,600+ reviews and Yelp 5-star with
> 1,600+ reviews are prominently placed, building trust early and reducing perceived risk for
> first-time visitors.
> - Heuristics Notes: Trust and clarity are strong. Cognitive load increases as users scroll
>   due to dense content blocks further down the page.

**Bad example (too generic):**
> Good design — the page looks professional and well-branded.

### Research Opportunities
Identify 2–4 specific friction points or gaps. Each must be actionable.

- Name the specific problem (referencing the actual element or its absence)
- Explain the impact (why it creates friction or reduces conversion)
- Suggest the direction (what to test or change)

**Good example:**
> **Improve CTA hierarchy** — Multiple CTAs compete for attention (header "Buy Tickets",
> individual tour CTAs, newsletter signup). Prioritising one primary action supported by
> secondary actions would reduce decision fatigue.

**Bad example (too generic):**
> The page lacks urgency — consider adding urgency signals.

---

## 6. Anti-Hallucination Rules

| Pattern to Avoid | Example | Rule |
|-----------------|---------|------|
| Fabricated statistics | "Research shows 73% of users abandon when trust signals are missing" | Never cite a specific stat without naming the exact source. Use directional language: "UX research consistently shows that trust signals near the CTA reduce hesitation." |
| Visual hallucination | "The red CTA button is undersized at approximately 32px" | Never describe colours, sizes, exact positions, or visual properties you cannot verify from fetched content or a screenshot. |
| Assumed absence | "This page has no reviews section" | Always caveat: "Not found in fetched content — may be present in JavaScript-rendered sections. Verify manually." |
| Generic findings | "The page lacks trust signals" (without citing what is or isn't present) | Every finding must reference a specific element. If it could be copy-pasted to a different client unchanged, it is not specific enough. |
| Invented competitors | "Unlike [competitor brand], this page fails to..." | Never reference competitors unless explicitly provided by Challenger. |
| Overconfident impact claims | "Adding a mid-page CTA will increase conversion by 15–20%" | Never predict specific conversion lifts. Use directional language: "Adding a mid-page CTA is likely to reduce scroll-back friction and may improve booking rate." |

---

## 7. Category-Specific Considerations

Apply these additional checks based on Challenger's business type:

| Business / Page Type | Additional Checks |
|---------------------|-------------------|
| E-commerce PDPs | Price visible without scroll? Variant selector clear? Shipping cost on page? Photo reviews? Return policy easy to find? Mobile sticky Add to Cart? |
| Booking / Experiences | Booking widget or availability calendar on tour page? Pricing clear? Duration, meeting point, group size easy to find? Urgency signals honest? |
| Lead Gen / B2B / SaaS | Form length appropriate? Value proposition above form? Social proof (logos, case studies)? Privacy signals near form? |
| Category / Listing Pages | Can users differentiate between options quickly? Filters or sorting present? "Best for you" recommendation or hierarchy? Key details visible in listing card? |
| Content / Blog Pages | Clear next step for engaged readers (related content, email capture, CTA)? Scannable format? Internal linking to relevant products? |
| Homepage | Primary value proposition above fold? Single dominant CTA? Enough social proof for first-time visitors? Navigation clear without being overwhelming? |

---

## 8. Summary Table

The final content slide of every heuristic analysis deck is a Summary Table rating all pages
across the five dimensions (Clarity / Trust / CTA Strength / Persuasion / Overall UX).

**Rating guidance:**
- Rate each page across all five dimensions using High / Medium / Low
- Ratings should reflect the dominant pattern — one weak element doesn't override four strong ones
- Be consistent: similar pages with similar findings should get similar ratings
- Present the table as the last content slide before any appendix

**Example format:**

| Page | Clarity | Trust | CTA Strength | Persuasion | Overall UX |
|------|---------|-------|--------------|-----------|------------|
| Homepage | High | High | Medium | High | High |
| Category Page | High | Medium | Medium | Medium | Medium |
| Tour Detail Page | High | High | Medium | High | High |
| Blog Page | High | Medium | Medium | High | Medium |

---

## 9. Deck Structure

| Slide # | Title | Content |
|---------|-------|---------|
| 1 | Title Slide | Client logo (top left) + "Heuristic Analysis & CRO Audit" + date (bottom left) + logo (bottom right). Background: light grey (#F5F7F9). |
| 2 | Conversion Research Process | Standard methodology slide: 4-step process with the behavioural/attitudinal research matrix. This slide is the same for every client. |
| 3 to N | One slide per page | Slide title = page name. Left: two screenshots (desktop + mobile/zoomed). Right: "What Works" section (blue button header + findings) and "Research Opportunities" section (blue button header + findings). |
| N+1 | Summary Table | All pages × five dimensions rated High / Medium / Low. No narrative — table speaks for itself. |

**Design rules:**
- Background: #F5F7F9 (light grey) for all slides
- Primary accent: #4677F7 (blue) for button headers and borders
- Fonts: Poppins Bold for titles; Mulish Regular for body
- "What Works" and "Research Opportunities": styled as filled blue button headers (white text)
- Screenshots: left two-thirds of content area; findings on right
- logo: bottom right on every slide
- No severity labels (Critical/Major/Minor) anywhere in the deck

---

## 10. QA Checklist

Run before delivery:

| # | Check | Pass Criteria |
|---|-------|--------------|
| 1 | All agreed pages included | No page silently dropped |
| 2 | Every page has both sections | What Works and Research Opportunities both present |
| 3 | Findings are specific | Each references an actual observed element or copy |
| 4 | No fabricated statistics | Any stat cited has a named source |
| 5 | No visual hallucinations | No colours/sizes/positions without screenshot evidence |
| 6 | Absence findings are caveated | "Not found in fetched content — may be JS-rendered. Verify manually." |
| 7 | Summary Table complete | All pages rated across all 5 dimensions |
| 8 | Screenshots present or flagged | Each slide has two screenshots, or absence noted |
| 9 | Brand applied correctly | Fonts, colours, logo placement match spec |
| 10 | Finding count reasonable | 2–4 per section per page |

---

## 11. Post-Delivery Checklist

Share with Challenger team after delivering the deck:

| # | Action Item | Owner | Timeframe |
|---|-------------|-------|-----------|
| 1 | Review deck with stakeholders (design, dev, marketing) | PM | Within 48 hours |
| 2 | Confirm top 3–5 Research Opportunities to prioritise | PM + Client | Within 5 business days |
| 3 | Check "requires manual verification" findings on real device/browser | Designer or QA | Within 48 hours |
| 4 | Create A/B test tickets for prioritised opportunities | CRO Strategist | Within 5 business days |
| 5 | File deck in client Drive folder under /Audits | PM | Within 24 hours |
| 6 | Feed heuristic findings into quantitative research priorities (Step 2) | CRO Strategist | At next client sync |

---

## 12. Brand Fallback Spec

If the `growthit-brand` plugin is not accessible, use these values:

| Element | Value |
|---------|-------|
| Primary blue | #4677F7 |
| Background grey | #F5F7F9 |
| Black | #000000 |
| Body text | #444444 |
| Title font | Poppins Bold |
| Body font | Mulish Regular |
| Button style | Filled blue (#4677F7), white text, rounded corners |
| Logo position | Bottom right, every slide |
