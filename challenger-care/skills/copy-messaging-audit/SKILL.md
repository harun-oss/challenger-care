---
name: copy-messaging-audit
description: 'Audits website copy using Joanna Wiebe Seven Sweeps (Clarity - Voice - So What - Proof - Specificity - Emotion - Zero Risk). Pairs with `refresh-underperforming-pdp` as the diagnosis layer before rewriting. MANDATORY TRIGGER: any mention of "copy audit", "messaging audit", "Seven Sweeps", "audit my copy", "audit a page''s copy", "value proposition review", "CTA copy audit", "review this PDP copy". Do NOT use for: Writing the rewrite itself (use `refresh-underperforming-pdp`). Ad copy (use `meta-ads-copywriting`). Email copy (use `email-copywriting`).'
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/voc/quote-library.md, assets/customer-archetypes.md, assets/team-roles.md, CONFIG.md


# Copy & Messaging Audit Skill

## What this skill does

This skill audits website copy and messaging using a structured, dual-layer framework:

1. **Joanna Wiebe's Seven Sweeps** — a proven copy audit methodology that tests copy from seven distinct angles, each catching a different class of failure
2. **Messaging Principles** — Challenger-specific standards for value proposition clarity, customer voice alignment, and conversion-focused copywriting

For each page audited, the skill outputs:
- Findings per sweep (what's wrong and why)
- Priority level (High / Medium / Low)
- A CRO test hypothesis for each finding (ready for the testing roadmap)
- Recommended copy rewrite or direction

Input: page URL to fetch, or paste raw copy directly. Works for any page type: homepage, PDP, landing page, form page, pricing, about, location pages.

Output options:
- **Audit report** — structured findings document (Markdown or DOCX)
- **Annotated copy** — original copy with inline comments and rewrites
- **Test hypotheses** — formatted ICE-ready items for the testing roadmap skill

---

## Framework 1: Joanna Wiebe's Seven Sweeps

Run every page through all seven sweeps in order. Each sweep catches a different class of copy failure.

### Sweep 1 — Clarity

**The question:** Can a stranger understand exactly what this page is about and what it wants them to do within 5 seconds?

**What to look for:**
- Vague or jargon-heavy headlines that don't state the offer
- Body copy that assumes prior knowledge
- Missing "who this is for" signal
- CTAs that don't say what happens next (e.g. "Submit" vs. "Get My Free Quote")
- Page structure that buries the value prop below the fold

**Test for it:** Read only the headline and the first CTA. Without any other context, do you know what you'll get and who this is for?

**standard:** The hero headline should communicate the primary benefit + who it's for within 8–12 words. The sub-headline adds specificity. The CTA states the action outcome.

---

### Sweep 2 — Voice and Tone

**The question:** Does this copy sound like the brand, or does it sound like a corporate press release?

**What to look for:**
- Copy that's formal and distant when the brand should be approachable
- Copy that's casual when the brand serves a professional audience
- Inconsistent voice across sections (one section conversational, another stiff)
- Passive voice hiding accountability ("results may vary" vs. "most clients see X")
- Generic adjectives with no substance ("innovative," "leading," "best-in-class," "seamless")

**Voice signal:** The brand's email communications, sales calls, or VoC data reveal the natural voice. Copy should match what customers hear from the team directly.

---

### Sweep 3 — The "So What?"

**The question:** Every claim needs to answer "so what?" from the customer's perspective.

**What to look for:**
- Feature lists with no benefits ("24/7 security" with no "so your inventory is always protected")
- Specifications that only engineers care about ("ISO certified" with no explanation)
- Benefit claims that are too abstract ("flexibility" — flexibility to do what, exactly?)
- Proof points that aren't connected to customer outcomes

**How to fix:** For each feature, ask: "So what does that mean for me?" The answer is the actual benefit copy.

**standard:** Every feature claim should have a benefit bridge. Format: "[Feature] so that [customer outcome]."

---

### Sweep 4 — Proof

**The question:** Does the page prove its claims, or just assert them?

**What to look for:**
- Claims with no supporting evidence ("Most trusted provider" — trusted by whom? How many?)
- Testimonials that are vague ("Great service!" adds nothing)
- Social proof that's too generic or unverifiable
- Numbers that lack context ("500+ clients" — in what time period? What size?)
- Missing case study / results data for claims like "our clients see X% improvement"
- Trust badges or certifications that aren't explained

**Proof hierarchy (strongest to weakest):**
1. Specific third-party data with source and date
2. Named customer case study with quantified result
3. Named testimonial with specifics (role, company, specific outcome)
4. Star rating with review count from a recognized platform (Google, G2, Yelp)
5. Unnamed testimonial
6. General claim ("thousands of satisfied customers")

**standard:** Every major claim needs Proof Level 1–4. Levels 5–6 should be supplemented with more specific proof.

---

### Sweep 5 — Specificity

**The question:** Are the claims specific enough to be credible and memorable?

**What to look for:**
- Round numbers that feel made up ("Save 50% of your time" — save 47 minutes per week is more believable)
- Vague benefit claims ("faster," "easier," "better" — faster than what? By how much?)
- Generic superlatives ("the best solution for your business")
- Location claims with no specifics ("serving businesses nationwide" vs. "serving 340+ businesses across Indiana, Ohio, Minnesota, and Wisconsin")

**Specificity test:** Replace the vague claim with a specific version. If the specific version sounds more credible, the vague version needs fixing.

---

### Sweep 6 — Heightened Emotion

**The question:** Does any part of this page make the reader feel something?

**What to look for:**
- Copy that lists features but never connects to the emotional stakes
- Missing loss-framing (what are the costs of NOT solving this problem?)
- Hero copy that describes a product instead of a future state
- No aspiration — copy that talks about what you do, not the life/business transformation it enables
- Missing "I get you" moment — where does the copy show the brand understands the customer's frustration?

**rule for lead-gen:** Show you understand the pain before offering the solution. Lead with empathy, follow with proof, close with action.

**Emotional triggers relevant to clients:**
- B2B: Fear of wasting money, desire for growth certainty, frustration with current provider
- eComm: Desire for belonging/identity, fear of wrong choice, aspiration for an improved version of self
- B2C lead-gen: Fear of being overcharged, desire for simplicity, frustration with complexity

---

### Sweep 7 — Zero Risk

**The question:** Have you removed every possible reason for the reader to hesitate?

**What to look for:**
- No mention of what happens after clicking the CTA (privacy anxiety — "will I get spammed?")
- Missing price-risk reduction ("no contract," "cancel anytime," "free trial")
- Hidden commitment signals (form with too many fields signals high effort; "speak to sales" signals a hard sell)
- Unanswered objections that will prevent conversion (what are the top 3 reasons someone would NOT convert? Are they addressed?)
- No trust signals near the CTA (logo bar, star rating, or proof statement adjacent to the submit button)

**Zero-risk additions:**
- Under CTA: "No credit card required" / "Free, no commitment quote" / "We'll respond in 24 hours"
- Near form: Privacy statement ("We never share your information")
- Adjacent to price: "Cancel anytime" / "30-day money-back guarantee"

---

## Framework 2: Messaging Principles

In addition to the Seven Sweeps, apply these Challenger-specific standards:

### Voice of Customer (VoC) alignment

The most powerful copy comes directly from customers. Before writing or auditing, check whether VoC data exists (survey responses, review mining, sales call transcripts, exit-intent data). Then ask:

- Does the headline language match how customers describe the problem?
- Does the value prop use words customers actually use, or words the brand invented?
- Are customer objections (from VoC) addressed somewhere on the page?

**standard:** If VoC data exists, the headline and primary CTA should use customer vocabulary, not brand vocabulary.

### Value proposition clarity

The value prop answers: *"What do you do, for whom, and why is it better than the alternative?"*

Test the value prop by asking:
1. Can a person outside your industry understand it?
2. Does it say something your top 3 competitors can't also claim?
3. Does it focus on the customer outcome, not the product feature?

**Weak VP:** "All-inclusive commercial spaces with flexible lease terms"
**Strong VP:** "Run your business, not your building — all-inclusive workspace with month-to-month leases so you can grow without the overhead"

### CTA copy standards

| ❌ Weak CTA | ✅ Strong CTA |
|------------|-------------|
| Submit | Get My Free Rate Analysis |
| Learn More | See How It Works |
| Contact Us | Talk to a Space Expert |
| Click Here | Find a Location Near You |
| Get Started | Start Your Free Trial |
| Sign Up | Join 1,200+ Businesses |

CTA copy should state the action AND the outcome. "Get [Outcome]" > "Do [Action]."

### Trust signal placement

Trust signals should appear at the moment of highest hesitation — not just in the footer or About page:
- **Above the fold:** Rating + review count, client count, or featured media logo
- **Adjacent to the CTA:** A single reassurance line (no commitment, privacy, response time)
- **Near the form:** Named testimonial from a similar customer profile
- **Bottom of page:** Awards, certifications, partner logos

---

## Phases

### Phase 1 — Scope the audit

Confirm:
1. Client name and vertical
2. Pages to audit (one page or a full funnel)
3. Primary conversion goal for each page
4. Audience (who is this page trying to convert?)
5. Any VoC data available (survey responses, review data, exit-intent)?
6. Any competitor copy to benchmark against?

**Optional Composio context pull:** if the page is live (URL provided) and `google_analytics` and `google_search_console` are connected via Composio (see the live MCP connectors), pull two things for the target URL: (a) GA4 metrics for the page — sessions, bounce, CVR — to weight sweep priority toward pages that already get traffic; (b) GSC top queries for the URL — to check whether the headline matches the actual queries Google is sending. If Composio is not connected, skip this step and proceed with the copy provided inline.

### Phase 2 — Gather the copy

For each page:
- Fetch the live URL (WebFetch) OR ask the PM to paste the copy
- Extract: headline, subheadline, body copy, CTAs, social proof, trust signals, form fields
- Note what's above the fold vs. below the fold
- Note mobile vs. desktop differences if relevant

### Phase 3 — Run the Seven Sweeps

For each page, run all seven sweeps in sequence. Document:
- **Finding**: What specific copy issue was found
- **Evidence**: Quote the exact copy that's problematic
- **Why it matters**: Which conversion principle it violates
- **Priority**: High (likely killing conversions right now) / Medium (significant friction) / Low (improvement opportunity)
- **Recommended fix**: Specific rewrite direction or example copy

### Phase 4 — Apply Messaging Principles

Overlay the VoC alignment check, value proposition assessment, and CTA copy evaluation. Flag gaps between brand language and customer language.

### Phase 5 — Generate test hypotheses

For every High and Medium priority finding, generate a CRO test hypothesis with skill-specific guidance:

```
If we [specific copy change on X element],
then [metric] will [increase/decrease],
because [VoC finding / Sweep violation / conversion principle].

Research source: [Sweep N — which sweep found it, and supporting evidence]
Category: [Quick Win / Core Test] (most copy tests are Quick Wins; aim for Ease 8–10)
Impact: [Medium-High for above-fold copy; Medium for below-fold]
Confidence: [Rate based on: 1 research source = 4–5, 2+ sources = 7+]
```

Every hypothesis must be grounded in evidence from one of the Seven Sweeps, not speculation.

### Phase 6 — Confirm Output Format + Branding

Ask which format before building:

> "Audit complete — ready to deliver findings. What format would you like?
>
> 1. **Word Document (.docx)** — Full written audit report with findings per sweep and recommended rewrites, best for internal briefs and client delivery
> 2. **Annotated copy** — Original copy with inline [FINDING] and [REWRITE] callouts, best for sharing directly with a copywriter
> 3. **Test hypotheses only** — ICE-ready hypothesis list formatted for the testing-roadmap skill
> 4. **Something else** — Just tell me"

Wait for the user's answer. Then ask about branding:

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colors, fonts, and layout rules before building.

Build based on chosen format:
- **Word doc** → invoke the docx skill; organize findings by page then by sweep, include a priority summary table at the top
- **Annotated copy** → plain text; no skill needed
- **Test hypotheses** → plain text or Markdown table; formatted for the testing-roadmap skill
- **Other** → adapt to the format, confirm approach before building

### Phase 7 — Synthesis Brief

Before finalizing the deliverable, write a plain-text summary of key findings for orchestrator handoff.

**Copy & Messaging Audit Key Findings:**
- High-priority findings count by category (Clarity, Voice/Tone, Proof, Specificity, Zero Risk) with top 2-3 issues per page
- Proof hierarchy assessment: current proof level (1-6 scale) vs. required level for claims made
- VoC alignment gaps: customer language not used in headline or CTA where it should be
- Value proposition clarity assessment: whether page clearly states what, for whom, and why better
- CTA copy status: weak vs. strong format and specific recommendations for each major CTA
- Test hypothesis count: number of High-priority findings converted to CRO test hypotheses ready for roadmap

**Priority for downstream skills:** Route all High-priority test hypotheses to testing-roadmap skill (if not already being tested). Flag any page with underdeveloped copy or missing VoC data as requiring pre-testing research.

*If running standalone, share this summary with the PM or copywriter before executing rewrites.*

---

### Phase 8 — QA gate

Before finalizing:
- [ ] All seven sweeps completed for each page
- [ ] Every High-priority finding has a test hypothesis
- [ ] Rewrites use customer language (not brand jargon)
- [ ] CTA rewrites follow the "[Action] + [Outcome]" format
- [ ] All claims challenged for proof level
- [ ] Zero-risk elements checked at every CTA

---

## Audit output format

### Audit finding format

```
## [Page Name] — Sweep [N]: [Sweep Name]

**Finding (Priority: High / Medium / Low):**
[What the problem is]

**Evidence:**
"[Exact quote from the page copy]"

**Why it matters:**
[Which conversion principle this violates and how it impacts the reader]

**Recommended fix:**
[Specific rewrite or direction]

**Test hypothesis:**
If we [change], then [metric] will [improve], because [reason].
```

---

## Error handling

### URL fetch fails
If WebFetch cannot retrieve the page, do not attempt workarounds (no curl, no Python requests). Inform the user clearly: *"I wasn't able to fetch that URL. Could you paste the page copy directly into the chat? Include the headline, subheadline, body copy, CTAs, and any trust signals."* Proceed with pasted copy once provided.

### Copy is very short or underdeveloped
If the page has minimal copy (e.g., a placeholder or stub page), note this as a top-level finding: *"Page copy is underdeveloped — this is itself a High priority issue."* Audit what exists against all seven sweeps anyway. The absence of copy is a finding, not a blocker.

### No VoC data available
If no VoC research exists for Challenger, audit using heuristic judgment only. Flag every finding that references VoC with: *"No VoC data available — this finding is based on heuristic best practice. Confidence increases significantly once VoC data is collected."* Recommend VoC research as a parallel action item.

### Non-English or mixed-language copy
Flag the language and note: *"Audit conducted on English copy. If the primary audience uses another language, findings apply to structure and proof hierarchy; voice/tone findings require native-language review."* Proceed with structural assessment (Clarity, Proof, Specificity, Zero Risk sweeps) and flag Voice/Tone as requires-native-review.

### Copy has already been partially rewritten
If the user indicates some copy has been recently updated, ask: *"Is there a previous version to compare against, or should I audit the current state only?"* Audit current state unless comparison is explicitly needed.

## Anti-patterns

- **Never rewrite copy without a reason** — every suggested change must tie back to a specific sweep finding or VoC data point
- **Never use brand language as the standard** — always test against customer language; if customers don't use the word, reconsider it
- **Never audit copy in isolation** — copy context is everything; "Book a Tour" means something different above the fold vs. buried in the footer
- **Never over-optimize for cleverness** — clear > clever, always. A clever headline that requires explanation is a weak headline
- **Never treat all pages equally** — prioritize auditing the highest-traffic, highest-drop-off pages first
- **Never skip the zero-risk sweep** — hesitation near the CTA is one of the most common and fixable conversion blockers

---

## Synthesis Brief

Before building the final deliverable, write a plain-text summary of key findings for orchestrator handoff.

**Copy & Messaging Audit Key Findings:**
- Overall copy score or summary (e.g., "3/7 sweeps passed; Clarity and Proof sweeps strongest, Voice/Tone and Zero Risk weakest")
- Top 3 highest-priority copy failures (ranked by conversion impact: specify page + element name + sweep violation type + urgency reason)
- Winning copy angles identified (headlines or CTA language that scored well, value propositions that tested strong, customer language that aligned with VoC)
- Immediate rewrite recommendations (top 3 rewrites by priority — specific before/after copy suggestions for fastest wins; focus on above-fold elements)

**Priority for downstream skills:** Route findings to testing-roadmap (for copy test hypothesis prioritization and ICE scoring), ab-test-reporting (to document any winning copy tests from this audit that have live results), or email-copywriting (if copy angles apply to email campaigns).

*If running standalone, share this summary with the operator or client team before the full deliverable.*

---

## References

- [Seven Sweeps Full Reference](references/seven-sweeps-reference.md) — Full Joanna Wiebe framework with adaptations and worked examples
- [CTA Copy Library](references/cta-copy-library.md) — Proven CTA formulas by vertical and conversion action
