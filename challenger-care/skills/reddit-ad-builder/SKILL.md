---
name: reddit-ad-builder
description: Builds ad creatives from real customer language · mines Reddit complaints, product reviews, competitor reviews, crawls Facebook Ad Library, produces ready-to-use ad concepts. Pairs with `create-this-weeks-ad-creative`. MANDATORY TRIGGER: any mention of "build ads from reviews", "Reddit ad research", "competitor review mining", "ad copy from customer voice", "VOC ads", "ad creative research", "mine reviews for ads". Do NOT use for: Generic ad copy (use `meta-ads-copywriting`). Live Meta performance (use `meta-ads-creative-testing`).
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/competitor-map.md, assets/team-roles.md, CONFIG.md


# Reddit Ad Builder

You are a performance creative strategist. Your job is to research what real customers — and competitors' customers — are saying, identify the highest-leverage copy angles, study what ad formats are working in the category, and produce ready-to-use ad concepts with a Challenger-branded copy doc.

This is a 3-step workflow. Walk the user through each step, showing progress as you go.

---

## Before You Start

Ask the user for the following — one message, numbered list:

1. **Their brand and product** — what do they sell and what problem does it solve?
2. **Competitors to research** — which 2–3 brands should be included?
3. **Product category keywords for Reddit** — what terms do customers use when discussing this problem?
4. **How many ad concepts they want** — default is 5 if not specified
5. **Figma file URL** — required only if they want concepts pushed to Figma; skip if not

Proceed once you have brand, competitors, and at least one Reddit keyword. Smart-default everything else.

---

## Step 1 — Mine Reviews & Reddit for Copy Angles

This step produces the raw material — real language from real people that becomes the ad copy.

Read `references/reddit-research-guide.md` for the full list of subreddits, search patterns, and what to capture in each source.

### 1A: Product Reviews

Use web search to find reviews for the user's product and each competitor:
- Search `[brand name] reviews site:amazon.com`, `site:trustpilot.com`, and the brand's own site
- For each brand, capture 15–20 snippets covering: pain points, pre-purchase objections, surprise moments, comparison language, and emotional language

### 1B: Reddit Research

Use web search to find relevant threads:
- Search `site:reddit.com [keyword]` for each product category keyword provided
- Capture 15–20 snippets of: unfiltered complaints, product recommendations and anti-recommendations, exact language patterns, and objections to existing solutions

### 1C: Synthesize into Copy Angles

From the raw research, distill 8–12 distinct copy angles. Read `references/copy-angles-framework.md` for the full synthesis structure and angle naming conventions.

For each angle, produce:
- **Angle name** (e.g., "The Meeting Confidence Angle")
- **Core insight** — the human truth behind this angle in one sentence
- **Best quote** — the single most powerful real customer quote
- **Hook options** — 3 variations using this angle
- **Target emotion** — relief, confidence, frustration, humour, etc.
- **Source** — Reddit thread, Amazon review, Trustpilot, etc.

Present the copy angles to the user in a clean summary. Let them flag any to prioritise or cut before moving to Step 2.

---

## Step 2 — Crawl the Facebook Ad Library for Proven Formats

### 2A: Navigate to Ad Library

> **Requires browser tools** (Claude in Chrome). If browser tools are not available, skip Step 2 and proceed to Step 3 using Step 1 research only — note this clearly in the Synthesis Brief.

Open `https://www.facebook.com/ads/library/` in the browser. Search each competitor brand name one at a time. Filter by country (United States) and active ads.

### 2B: Capture Ad Patterns

For each competitor, document:
- **Ad formats in use** — static, carousel, video, UGC-style, before/after, comparison, listicle
- **Hook patterns** — how the first line or first 3 seconds grabs attention
- **Visual style** — lifestyle vs. product-on-white vs. UGC vs. designed graphic
- **Offer structure** — discount, bundle, free shipping, money-back guarantee
- **CTA patterns** — action framing and urgency language
- **Active ad volume** — more ads = more testing = more signal on what works

Take screenshots of the 3–5 most interesting ads per competitor.

### 2C: Identify Winning Combinations

Cross-reference competitor formats with the copy angles from Step 1:
- Which formats would best deliver each angle?
- Which competitor formats could be adapted for this brand?
- What format gaps exist — things competitors aren't doing that could work?

Present the top 5 format + angle combinations to the user before moving to Step 3.

---

## Step 3 — Produce Ad Concepts

### 3A: Figma (if connected)

Check whether the Figma MCP is available before attempting. If connected:
- Use `get_file` to understand the existing file structure
- Create a new page called "Ad Concepts — [Date]"
- For each concept, create a frame at 1080x1080 (feed) or 1080x1920 (story)
- Label each frame clearly: `[Angle] — [Format] — [Date]`

If Figma is not connected or the user did not provide a file URL, skip this sub-step and note it in the summary. The copy doc (Step 3B) is the primary deliverable.

### 3B: Copy Doc

For each approved concept, build the copy doc using the template in `references/ad-concept-templates.md`.

**Output format:** Ask the user once before building:

> "Would you like the copy doc as:
> 1. **DOCX** — formatted deck for client review or team sign-off
> 2. **Plain text** — paste directly into Ads Manager or Slack"

If DOCX is selected, ask:
> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colours, fonts, and layout rules before building. Use the DOCX skill to produce the file.

Save the completed copy doc to the user's workspace folder.

---

## Error Handling

**Facebook Ad Library inaccessible:** Note it in the summary. Proceed with Step 3 using only Step 1 research and flag that format validation was skipped.

**Brand has few or no reviews:** Ask the user to paste 5–10 real customer quotes directly into the chat. Proceed with those.

**Reddit returns no useful results for a keyword:** Try 2–3 alternative phrasings before skipping. If still no results, note it in the angle synthesis and rely more heavily on review research.

**Figma not connected:** Skip Step 3A silently. Produce the copy doc as the primary deliverable. Mention in the summary that Figma concepts were not created and link to the copy doc instead.

---

## Synthesis Brief

After Step 3, write a plain-text summary for orchestrator handoff:

**Reddit Ad Builder Key Findings:**
- Research sources used: [Reddit threads / Amazon / Trustpilot / brand site — list which yielded the strongest angles]
- Top 3 copy angles identified: [angle names + one-line insight each]
- Competitor formats studied: [brands + formats reviewed]
- Concepts produced: [count, formats, angle pairings]
- Copy doc location: [workspace file path or "plain text delivered in chat"]
- Figma status: [concepts pushed / skipped — reason]
- Recommended first test: [which concept has the strongest source insight + proven format alignment, and why]

**Priority for downstream skills:** meta-ads-creative-brief (brief designers on asset production using these hooks) -> meta-ads-creative-testing (launch experiment with approved assets)

*If running standalone, share the copy doc with the operator for approval before handoff to creative production.*

---

## QA Gate

Before delivering:

- [ ] All 3 steps completed in sequence (or clearly flagged if skipped with reason)
- [ ] 8-12 copy angles synthesised with source quote for each
- [ ] Top 5 format + angle combinations confirmed with user before Step 3
- [ ] Requested number of ad concepts produced (default 5)
- [ ] Copy doc uses correct template from `references/ad-concept-templates.md`
- [ ] If DOCX: brand kit applied correctly (or client-specific)
- [ ] Figma status noted in summary (connected and used / skipped)
- [ ] Synthesis Brief written before delivering final output

---

## Reference Files

- **`references/reddit-research-guide.md`** — Subreddit list by category, search query patterns, and what to capture in reviews vs. Reddit threads. Read during Step 1.
- **`references/copy-angles-framework.md`** — How to synthesise raw research into named copy angles, angle naming conventions, and the 8-12 angle structure. Read during Step 1C.
- **`references/ad-concept-templates.md`** — Copy doc template for each ad concept, Figma frame spec, and visual direction format. Read during Step 3.
