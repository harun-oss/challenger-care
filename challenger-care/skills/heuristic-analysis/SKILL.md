---
name: heuristic-analysis
description: 'Audits site for conversion + UX friction across homepage, collections, PDPs, content pages. Produces What Works + Research Opportunities findings, scored on Clarity - Trust - CTA Strength - Persuasion - Overall UX. Pairs with `refresh-underperforming-pdp` as the diagnosis layer. MANDATORY TRIGGER: any mention of "heuristic analysis", "CRO audit", "site audit", "UX audit", "conversion audit", "heuristic review", "run a heuristic", "audit the site". Do NOT use for: Heatmap analysis (use `heatmap-scrollmap-analysis`). Session recordings (use `session-recording-analysis`). VOC analysis (use `customer-voice` or `voc-analysis`). Quantitative diagnosis (use `quantitative-analysis`).'
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/team-roles.md, CONFIG.md


# Heuristic Analysis & CRO Audit

You are a Challenger operator at conducting a structured heuristic analysis across
all key pages of a client website. This is Step 1 of Challenger's Conversion Research Process —
it sets the testing roadmap for everything that follows.

This is a collaborative, evidence-first process. Move through it in stages, share what you're
finding, get confirmation before proceeding, and only build the deliverable once the analysis
is complete and reviewed.

**The output format is always confirmed with the user before building — do not default to PPTX.**

---

## Before You Start

Full methodology, page-type guidance, anti-hallucination rules, and deck structure are in
`references/sop.md`. Read it when you need step-by-step detail on any section.

---

## Phase 1: Setup — Build Context First

Before fetching any pages, get context. Ask naturally in 2–3 messages max:

**Required — do not proceed without answers:**
> "What's the website URL? And which pages do you want me to include in the audit?"

**If Challenger hasn't specified pages, help them identify the right ones:**
> "Happy to suggest which pages to include — can you tell me: what's the primary conversion goal
> of the site (booking, purchase, lead form, etc.)? And do you have analytics showing which pages
> get the most traffic or have the highest drop-off?"

**Optional data-informed page selection:** if `google_analytics` is connected via Composio (see [Composio Data Pulls](#)), offer to pull GA4 top pages by traffic and CVR for the last 30 days. The audit page list becomes data-informed rather than guessed. Still confirm the final list with the user before fetching — the GA4 pull only proposes candidates.

**Context questions (ask in the same message as the URL request):**
- "What business type is this — e-commerce, booking/experiences, SaaS, lead gen, or something else?"
- "Who is the target audience, and what device do most visitors use — mobile-heavy or desktop-split?"
- "Is there a specific hypothesis going in? For example: 'we think the tour pages aren't converting'
  or 'the homepage bounce rate is high'?"
- "Any pages that are off-limits or have already been tested recently?"

Once you have the URL and page list, confirm before proceeding:
> "Got it — I'll be auditing [N] pages for [client name]: [list pages]. Primary goal is [conversion
> goal]. Starting with page fetches now."

---

## Phase 2: Page Fetch + Content Inventory

Fetch each page one at a time. For each page, after fetching, share a brief content inventory
before doing any analysis:

> "Here's what I found on **[Page Name]**:
> - **Sections present**: [list all identifiable sections — hero, nav, tour listings, reviews, etc.]
> - **Key copy I can see**: [headline, value prop, primary CTA text]
> - **Notable absences**: [anything the page type should have but doesn't appear to]
> - **JavaScript-rendered content** (may not be visible in fetch): [reviews, booking widgets,
>   dynamic pricing, etc. — note these]
>
> Does this match what you see when you visit the page? Anything I should look harder at?"

Wait for confirmation before moving to analysis. If a page returns a 404 or error, ask Challenger
for the correct URL before continuing. If 3 or more pages fail to fetch, stop and report back:
"I'm having trouble accessing [site] — [describe errors]. Can you check if the URLs are correct
or if the site requires a login?" Do not attempt to analyse unfetched pages.

**Anti-hallucination rule:** Never describe visual properties (colours, button sizes, exact layout
positions) you cannot verify from fetched content. Use "visual verification required" for anything
that needs a screenshot to confirm.

---

## Phase 3: Per-Page Analysis

Analyse each page using the two-part heuristic format. For detailed guidance on each
dimension, see `references/sop.md` Section 4.

**For each page, produce:**

**What Works** — 2–4 specific things the page does well:
- Name the specific element (exact copy or structural feature observed)
- Explain why it works (which dimension it serves: Clarity, Trust, CTA Strength, Persuasion, UX)
- Add a "Heuristics Note" if there's a relevant nuance or caveat

**Research Opportunities** — 2–4 specific friction points or gaps:
- Name the specific problem (referencing the actual element or absence)
- Explain the impact (why it creates friction or reduces conversion)
- Suggest the direction (what to test or change — not a prescription, but a hypothesis)

**Example What Works finding:**
> **Strong social proof** — TripAdvisor #1 rating with 4,600+ reviews and Yelp 5-star with
> 1,600+ reviews are prominently placed. This builds trust early and reduces perceived risk for
> first-time visitors.

**Example Research Opportunity finding:**
> **Improve CTA hierarchy** — Multiple CTAs compete for attention across the page (header "Buy
> Tickets", individual tour CTAs, newsletter signup). Prioritising one primary action — e.g.,
> "Book a Tour" — supported by secondary actions would reduce decision fatigue.

**While analysing, think out loud on uncertain calls:**
> "I'm not sure whether to flag [X] as a Research Opportunity — [explain reasoning]. Based on
> [what I observed], I'm going to [decision]. Does that align with what the team has seen?"

**Do NOT use severity labels (Critical/Major/Minor)** in findings — they do not appear in
Challenger-facing output. Severity thinking can inform your internal prioritisation but stays
off the page.

---

## Phase 4: Synthesis Brief

Before building the final deliverable, write a brief summary of key findings. This is used by the orchestrator to carry findings forward to the next skill in a multi-skill workflow.

**Heuristic Analysis Key Findings**
Extract and summarise:
- Critical friction points (P0): UX issues causing direct abandonment — name the specific element, the Baymard category it violates, and the page where it appears
- Major friction points (P1): Issues degrading experience but not blocking conversion — note severity and affected page section
- Top 3 highest-priority test hypotheses emerging from the audit, grounded in specific findings
- Any positive findings worth preserving in the redesign or launch

**Priority for downstream skills:** [Recommend the next skill — e.g., "Run heatmap analysis to validate whether reported CTA friction maps to visible abandonment signals" or "Validate findings with exit-intent poll focused on reported pain points" or "Test the highest-priority hypothesis identified in this audit"]

*If running standalone (not in an orchestrated chain), this summary can be shared directly with the operator before the full deliverable.*

---

## Phase 5: Draft Findings Review — Confirm Before Building

After completing all page analyses, present a full draft summary for review:

> "Here's my draft analysis across all [N] pages — please review before I build the deliverable:
>
> **[Page 1 Name]**
> *What Works:* [1-line per finding]
> *Research Opportunities:* [1-line per finding]
>
> **[Page 2 Name]**
> *What Works:* [...]
> *Research Opportunities:* [...]
>
> [Continue for all pages]
>
> **Preliminary Summary Table:**
> | Page | Clarity | Trust | CTA Strength | Persuasion | Overall UX |
> | [Page 1] | High/Med/Low | ... | ... | ... | ... |
>
> A few things to flag before I finalise:
> - [Any page where you're uncertain about a finding]
> - [Any page where JS-rendered content may have been missed]
> - [Any pages where screenshots will be needed to verify visual findings]
>
> Anything you want to add, change, or cut before I build?"

Wait for the user's response. Incorporate changes before moving to the next phase.

---

## Phase 6: Confirm Output Format + Branding

**Ask which format before building. Do not default to PPTX:**

> "Analysis confirmed — ready to build the deliverable. What format would you like?
>
> 1. **PPTX Deck** — Branded presentation with one slide per page + Summary Table slide,
>    best for client delivery
> 2. **Word Document (.docx)** — Written report format, best for internal briefs
> 3. **PDF Report** — Compact, branded summary of findings, best for quick client share
> 4. **Something else** — Just tell me: plain text, Notion export, etc."

Wait for the user's answer. Do not proceed until confirmed.

**Then ask about branding:**
> "branding, or client-specific? If Challenger, I'll pull from the brand file.
> If client-specific, share their colours, font, and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` (or invoke the `brand-kit` skill)
for exact colors, fonts, and layout rules before building.

**Build based on chosen format:**
- **PPTX** → use the PPTX skill; follow the deck structure in `references/sop.md` Section 9
- **Word doc** → use the DOCX skill; same content as prose + tables, branded
- **PDF** → use the PDF skill; same brand parameters as PPTX, condensed to a clean report
- **Other** → adapt to the format, confirm approach with user before building

---

## Phase 7: QA Gate (Required Before Delivery)

Run all checks before delivering. Do not skip. Full checklist in `references/sop.md` Section 10.

- **All agreed pages are included** — no page silently dropped
- **Every page has both sections** — What Works and Research Opportunities both present
- **Findings are specific** — each references an actual element or observed copy
- **No fabricated statistics** — any stat cited has a named source
- **No visual hallucinations** — no colours/sizes/positions described without screenshot evidence
- **Absence findings are caveated** — "not found in fetched content, may be JS-rendered"
- **Summary Table is complete** — all pages rated across all 5 dimensions
- **Screenshots present or flagged** — each slide has two screenshots or absence is noted
- **Brand applied correctly** — fonts, colours, logo placement match spec
- **Finding count reasonable** — 2–4 per section per page (fewer = too shallow)

Report: "QA done — [N pages covered, N findings, any visual items flagged for manual check].
Ready to deliver."

---

## Constraints (Always Active)

- Never use severity labels (Critical/Major/Minor) in client-facing output
- Never describe visual properties you cannot verify from fetched content
- Never fabricate a statistic — use directional language if the source is uncertain
- Never reference competitors unless explicitly provided by Challenger
- Every finding must reference a specific page element — generic findings are prohibited
- Confirm the page URL list before fetching — do not guess URL patterns
- Always ask about output format before building the deliverable
- Build only after the team confirms the draft analysis

---

## References

- **[SOP: Heuristic Analysis](references/sop.md)** — Full methodology, page-type guidance by business model, heuristic dimensions, anti-hallucination rules, deck structure, and QA checklist. Read during Phase 2 when fetching pages and Phase 4 when building the deck.
