---
name: leverage-point-assessment
description: Grades the business across 7 leverage points (Market · Product · Money · Position · Reach · Convert · Expand) on A-F scale with findings, quotes, recommendations. Pairs with `highest-leverage` (the lighter monthly Challenger version). This is the quarterly deep grade. MANDATORY TRIGGER: any mention of "leverage point assessment", "LPA", "strategic assessment", "growth audit", "grade the business", "quarterly LPA", "7 leverage points". Do NOT use for: Monthly priority check (use `highest-leverage`). Single-metric review. Channel-specific audits.
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/unit-economics.md, assets/goals-targets.md, assets/competitor-map.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/team-roles.md, CONFIG.md


# Leverage Point Assessment

## Overview

The Leverage Point Assessment is Challenger's proprietary strategic diagnostic. It evaluates a client's business across 7 fixed categories, grades each A-F, identifies the biggest constraint, and delivers prioritized recommendations. The output is a polished, client-facing Word document (.docx) ready to present.

**Before starting, read:**
- This SKILL.md (you're here)
- `references/framework.md` — The 7 leverage points, grading rubric, pyramid model, and question bank
- `references/voc-extraction.md` — How to extract and organize voice-of-customer intelligence from transcripts
- `references/docx-template.md` — The document structure and formatting specs for the final deliverable
- Invoke the `docx` skill (anthropic-skills:docx) before generating the .docx file
- Invoke the `brand-kit` skill (assets/brand-strategy.md) to apply Challenger's visual identity standards to the deliverable

## Workflow

The skill operates in either **single-pass** or **phased** mode depending on available inputs.

### Single-Pass Mode
When all inputs are provided at once (transcripts, data, research), produce the complete assessment in one go.

### Phased Mode
When inputs arrive incrementally:
1. **Phase 1 — Hypothesis Draft**: With whatever is available (even just a website URL and basic context), produce initial grades and hypotheses for each leverage point. Flag what data would strengthen or change the assessment.
2. **Phase 2 — Data Integration**: As additional inputs arrive (transcripts, ad data, VoC, etc.), update grades, add findings, and weave in evidence.
3. **Phase 3 — Final Deliverable**: Produce the polished client-facing document.

## Input Processing

### Required (minimum to start)
- Company name and what they do
- At least ONE of: stakeholder interview transcript, client workbook, website URL

### Optional (strengthens the assessment)
- Ad spend / performance data (spreadsheets)
- Keyword research (spreadsheets)
- Sales call transcripts (for VoC extraction)
- Competitor research
- Internal team meeting transcripts
- Previous work product for this client

### How to Process Each Input Type

**Stakeholder interview / call transcript:**
1. Read the full transcript
2. Extract direct quotes organized by leverage point
3. Identify what the founder/CEO said about each of the 7 areas
4. Note contradictions between what they say and what the data shows
5. Capture the emotional energy — what topics did they light up about vs. deflect on?

**Ad spend data:**
1. Calculate monthly totals by channel
2. Identify best/worst performing months and channels
3. Calculate blended CPL/CPD and CPD by channel
4. Flag volatility and trends
5. Map findings to REACH and MONEY sections

**Sales call transcripts (VoC):**
1. Follow the extraction framework in `references/voc-extraction.md`
2. Categorize every meaningful quote by leverage point
3. Organize into: Pain Language, Value Language, Objection Language, Aha Moments, Close Triggers
4. Use exact prospect words — don't paraphrase. These go into the deliverable as VoC callout boxes.

**Keyword research:**
1. Summarize total addressable search volume
2. Identify high-volume, high-intent keyword clusters
3. Flag competition level and CPC ranges
4. Map to REACH section as organic opportunity

**Client workbook / intake form:**
1. Extract business fundamentals: revenue, team size, pricing, ICP
2. Note what they self-identified as strengths vs. challenges
3. Cross-reference with what the data actually shows

## Output Specification

The final deliverable is a `.docx` file with this exact structure:

### Document Structure

1. **Cover Page** — branded, client name, date, subtitle "Findings & Recommendations"
2. **Executive Summary** — 2-paragraph narrative + scorecard table (all 7 grades at a glance) + prioritized "where the leverage is" list
3. **7 Leverage Point Pages** (one per section), each containing:
   - Section header with leverage point number and name
   - Core question for that leverage point
   - **Grade box** — color-coded (green for A/B, yellow for C, red for D/F) with grade and descriptor
   - **"What We Found"** — 1-2 paragraph narrative synthesis
   - **"Voice of Customer"** — 1-3 direct prospect quotes in yellow callout boxes (only if VoC data is available)
   - **"Key Findings"** — 4-7 bulleted evidence points
   - **"Recommendations"** — Table with specific actions and owners (Challenger, Client, or Both)
4. **What Happens Next** — Challenger's focus areas, Client's focus areas, and The Throughline (the one connective insight that ties all 7 together)

### Formatting Specs
- Invoke the `docx` skill (anthropic-skills:docx) before generating the document
- Invoke the `brand-kit` skill (assets/brand-strategy.md) for Challenger's official colors, fonts, and logo usage — use these for the cover page, section labels, header accents, and recommendation table headers
- Use `npm install -g docx` and the docx-js library
- Font: Arial throughout
- Page size: US Letter (12240 x 15840 DXA)
- Colors: Use client's brand color as accent if known, otherwise default to orange (the brand accent color from assets/brand-strategy.md) from the brand-kit
- Grade colors: Green (#2E7D32) for A/B grades, Yellow (#F9A825) for C grades, Red (#C62828) for D/F grades
- VoC quotes: Yellow background (#FFF8E1) callout boxes with italicized text
- Recommendation tables: Dark header row, alternating row shading, two columns (Recommendation | Owner)

## Grading Guidelines

Grades are assigned based on evidence, not gut feel. See `references/framework.md` for the full rubric, but the key principle:

**Grade based on what the EVIDENCE shows, not what Challenger says.** If the founder says "our market is huge" but can't name their TAM, that's a B at best. If they say "our product is great" but churn data shows customers leaving, that's a B- or C. Always cross-reference claims against data.

**The lowest-graded leverage point is always the biggest opportunity.** Frame it that way in the deliverable — not as a weakness, but as the area where improvement will have the most outsized impact.

**Adjacent grades (one above the constraint) are usually affected by the constraint.** If Reach is a D, Convert is probably suppressed too because there's not enough volume to optimize against. Note these dependencies.

## Writing Style

- Direct, no fluff. Every sentence should contain information or insight.
- Use Challenger's language, not marketing jargon. If their prospects say "back of the napkin," use that phrase.
- Findings should feel like observations from a trusted advisor, not a consultant's report.
- Recommendations must be specific and actionable — not "improve your website" but "build a post-demo email nurture sequence: 5-7 touches over 30 days with case studies, ROI data, and re-engagement CTAs."
- Every recommendation needs an owner. If it's scope, say so. If it's Challenger's, say so. If it's both, say so.
- The Throughline at the end should be a single, memorable insight that connects all 7 sections. For Arda it was: "The path to 10x is building systems that replace manual effort with scalable infrastructure."

## Common Patterns by Client Type

### B2B SaaS
- PRODUCT and MONEY tend to be stronger (high margins, recurring revenue)
- REACH and CONVERT tend to be the constraints (CAC, pipeline, sales cycle)
- Look for: churn data, activation metrics, CAC payback, freemium dynamics

### DTC / E-commerce
- PRODUCT and MARKET tend to be stronger (clear demand, physical product)
- MONEY and REACH tend to be constraints (margins, ad costs, CAC)
- Look for: ROAS, contribution margin, repeat purchase rate, AOV trends

### Services Businesses
- MARKET and POSITION tend to be stronger (niche expertise)
- EXPAND and CONVERT tend to be constraints (founder-dependent, proposal-based sales)
- Look for: utilization rates, project profitability, referral rates, pipeline velocity

## Checklist Before Delivering

- [ ] All 7 leverage points graded with evidence
- [ ] Executive summary includes scorecard table and prioritized leverage list
- [ ] VoC quotes are real, attributed, and mapped to the right leverage points
- [ ] Every recommendation has an owner
- [ ] Recommendations are specific and actionable (not vague)
- [ ] The Throughline ties all 7 sections into one insight
- [ ] Document uses brand standards (brand-kit skill applied)
- [ ] File saved to the workspace folder and presented to the user
