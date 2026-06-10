---
name: google-ads-campaign-build
description: 'Builds RSA + PMAX campaigns from scratch · account setup, branded vs non-branded split, ad copy (55-headline system), bid strategy, PMAX eligibility, extensions, change log. MANDATORY TRIGGER: any mention of "build Google Ads campaign", "set up Google Ads", "stand up Google", "create RSA campaign", "create PMAX", "build ad groups", "write Google Ads copy". Do NOT use for: Account audit (use `google-ads-account-audit`). Pre-launch QA (use `google-ads-prelaunch-qa`).'
---

> **Permission tier:** execute · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/unit-economics.md, assets/team-roles.md, CONFIG.md


# Google Ads Campaign Build

## What this skill does

This skill guides an Ads AM through the full campaign build process — from account-level settings through RSA and PMAX campaign creation, ad copy writing, bid strategy selection, and extension setup. It is designed to be used after keyword research is complete and client-approved.

**Prerequisites before running this skill:**
- Conversion tracking confirmed working (from google-ads-account-audit or setup)
- Keyword list approved by client (from google-ads-keyword-research)
- Campaign structure and ad group themes defined
- Access to Google Ads account, GA4, and GTM confirmed

Use this skill when:
- Building the first campaigns for a new Google Ads client
- Adding a new campaign type (e.g., adding PMAX to an account that only runs RSA)
- Rebuilding campaigns after a major restructure
- Launching a new service or product campaign

Output options:
- **Campaign Build Summary (DOCX)** — full written brief covering account structure, campaign settings, ad copy rationale, and bid strategy plan, best for client review or internal handoff
- **Structured text** — plain text campaign build checklist for Notion or Slack
- **Something else** — confirm with user

---

## Phase 1 — Pre-Build Confirmation

Before touching Google Ads, confirm the inputs are in place.

**Confirm the following are ready:**

1. **Conversion tracking:** Is at least one conversion action confirmed recording in Google Ads? (Status: "Recording conversions") — if not, stop and resolve via google-ads-account-audit before building
2. **Keyword list:** Is the keyword list approved and ad group structure finalized?
3. **Campaign types to build:** RSA only, or RSA + PMAX? (See PMAX eligibility check below)
4. **Budget:** What is the confirmed monthly budget, and how should it be allocated across campaigns?
5. **Brand campaign:** Will a branded search campaign be built now, or does one already exist?
6. **Extensions/assets ready:** Images, logo, sitelink URLs — are these available?
7. **Client Google Ads Workbook:** Is the workbook open and the change log tab ready?

**PMAX eligibility check:**

PMAX requires all of the following to be true before building:

| Requirement | Check |
|-------------|-------|
| Account has 30+ conversions in last 30 days | Confirm in Google Ads → Conversions |
| Monthly ad budget ≥ $1,000–$2,000 | Confirm with client |
| Account is NOT brand new | Must have existing conversion history |
| eCommerce: GMC product feed approved | Check Merchant Center — Status: Approved |
| Website remarketing audience ≥ 100 users | Check Google Ads → Tools → Audience Manager |

If any requirement is not met: build RSA campaigns only. Flag PMAX for reassessment at the 30-day mark.

---

## Phase 2 — Account-Level Setup

These settings apply to the entire account. Configure them once before building any campaigns.

### 2A. Extensions / Assets (account level)

Set at the account level so they apply to all campaigns by default. Individual campaigns can override with more specific extensions.

| Extension type | Minimum required | Best practice notes |
|---------------|-----------------|---------------------|
| Sitelinks | 4 | Link to: Contact/Quote page, a specific service page, About or Case Studies, Pricing or FAQ. Do not use the homepage for sitelinks — every sitelink should go to a specific, relevant page |
| Callouts | 6 | 25-character benefit statements. Examples: "No Long-Term Contracts", "Free Consultation", "Certified Technicians", "Same-Day Service". Avoid generic filler like "High Quality Service" |
| Images | 4 minimum | Use real brand photography — avoid stock photos. Mix: product images, team/office photos, lifestyle images of the product in use |
| Brand logo | 1 | Square format (1:1 ratio), PNG with transparent background recommended |
| Structured snippets | 1 | Use for: Services offered, product categories, or location list. Header options: Services, Products, Destinations, Courses, Brands |

**For eCommerce accounts additionally:**
- Link Google Merchant Center product feed for Shopping extensions
- Price extensions (optional) — list specific products with prices; useful for competitive price positioning

### 2B. Disable auto-applied recommendations

Go to: Google Ads → Recommendations → Auto-apply

Turn OFF every toggle. Google's auto-apply settings can silently make changes including:
- Adding broad match keywords
- Adjusting bids or switching bid strategies
- Adding or pausing ads based on performance predictions

Challenger's operating principle: every change to a client account is intentional, reviewed, and documented in the change log. Auto-apply violates this. Disable it on every account immediately upon gaining access.

### 2C. Audience setup (account level)

Before building campaigns, set up audience lists for use as observation segments and PMAX signals:

- **All website visitors** — Google Ads → Tools → Audience Manager → Website Visitors → All visitors (last 30 days). If below 100, it won't meet PMAX threshold but can still be used for observation.
- **Customer Match** — upload client's customer email list as a CSV (Google Ads → Tools → Audience Manager → Customer Lists). This is required for PMAX and is best practice for RSA remarketing.
- Add both lists to all Search campaigns in **Observation** mode (not Targeting) — this lets you see performance data by audience segment without restricting who sees the ads.

---

## Phase 3 — Campaign Structure

### 3A. Branded vs. non-branded separation — always required

**Rule: branded and non-branded keywords must always be in separate campaigns.**

This is not a preference — it is a structural requirement for every Google Ads account.

Why:
1. **Quality Score contamination:** Brand keywords have naturally high Quality Scores (often 7–10). Mixed with non-branded keywords, they make the account's average QS appear artificially strong, hiding real problems.
2. **CVR distortion:** Brand searchers are already aware of Challenger and convert at much higher rates. A mixed campaign makes non-branded CVR look stronger than it actually is, leading to incorrect bidding decisions.
3. **Budget control:** Branded campaigns generally need lower bids. Mixing makes budget management imprecise — you can't control how much goes to brand vs non-branded.
4. **Reporting clarity:** The client needs to know how well they perform with people who don't already know them. Mixed campaigns make this impossible to report.

**Cross-exclusion (required):**
- Add all brand name variations as **negatives** in every non-branded campaign
- Add all non-branded campaign keywords as **negatives** in the branded campaign (to prevent non-branded queries triggering branded ads)

### 3B. Standard campaign structure template

```
[Client] — Branded Search
  └── Ad Group: Brand Core
        Keywords: [brand name], [brand name + city], [brand misspellings]
  └── Ad Group: Brand + Service
        Keywords: [brand name + service], [brand name + product]

[Client] — Non-Branded — [Service Theme 1]
  └── Ad Group: [Primary Keyword Cluster]
  └── Ad Group: [Secondary Keyword Cluster]

[Client] — Non-Branded — [Service Theme 2] (if distinct enough)
  └── Ad Group: [Keyword Cluster]

[Client] — Competitor (optional — requires execute_tier_approver approval)
  └── Ad Group: [Competitor Name]

[Client] — PMAX (eligible accounts only)
```

---

## Phase 4 — RSA Campaign Build

### 4A. Campaign settings

For each RSA campaign, configure:

- **Campaign type:** Search (not Search + Display — Display Network must be OFF)
- **Networks:** Search Network only. Disable: Display Network, Search Partners (turn on Search Partners after 30 days of data if performance warrants)
- **Location:** Client's target geography. Targeting setting: **Presence** (people in the target location) — NOT "Presence or Interest" (which includes people outside the geography who are interested in it)
- **Language:** English (or client's target language)
- **Budget:** Daily budget = monthly budget ÷ 30.4 (Google's average days/month). If spreading across multiple campaigns, allocate based on priority — typically: non-branded (60–70%), branded (20–30%), PMAX if running (remaining)
- **Ad schedule:** If lead gen client with specific business hours, set an ad schedule. If eCommerce (sales happen 24/7), leave default (all hours)
- **Bid strategy:** See Phase 4C

### 4B. Ad group and RSA creation

> For headline formulas by vertical, description structures, and strong vs weak copy examples, read [`references/rsa-ad-copy-framework.md`](references/rsa-ad-copy-framework.md) before writing any ad copy.

**For each ad group:**

Create a minimum of 2 RSAs per ad group. This allows performance comparison — Google will optimize toward the better-performing ad.

Maximum 3 active RSAs per ad group. More than 3 dilutes the testing signal — the algorithm doesn't have enough impressions per variant to learn effectively.

**RSA headline strategy (15 headlines maximum):**

| Position | Content | Rule |
|----------|---------|------|
| Headline 1 (PIN) | Exact keyword or close variant | Pin this position — Headline 1 is the most visible; it must always contain the target keyword for ad relevance |
| Headline 2 | Primary benefit or value proposition | What does Challenger do better than anyone else? |
| Headline 3 | Location, CTA, or social proof | "Serving Minneapolis Since 2010", "Free Consultation", "500+ 5-Star Reviews" |
| Headlines 4–15 | Benefit statements, urgency, proof points, offer details | Vary: emotional appeal, rational benefit, trust signal, offer, guarantee |

**Why pin Headline 1:** If not pinned, Google can rotate any headline into the most prominent position — including generic ones that hurt ad relevance score. Ad relevance is one of three Quality Score components; "Below average" here means higher CPC and lower position.

**RSA description strategy (4 descriptions maximum):**

- Lead with the problem Challenger solves
- Follow with the solution and primary differentiator
- Include at least one proof element (years in business, number of clients served, ratings)
- End with a clear, specific call to action — not "Learn More" but "Get Your Free Quote Today" or "Call Now for Same-Day Service"

**Ad strength:** Aim for "Excellent" — but do not sacrifice keyword relevance for strength score. A "Good" RSA with pinned keyword-specific Headline 1 will outperform an "Excellent" RSA with generic rotating headlines.

### 4C. Bid strategy — progression ladder

| Stage | Condition | Bid strategy | When to move to next stage |
|-------|-----------|-------------|--------------------------|
| **Stage 1** | New account or <30 conversions | **Maximize Clicks** | When 30+ conversions recorded in the account |
| **Stage 2** | 30+ conversions recorded | **Maximize Conversions** | When CPA has stabilized over 60+ days |
| **Stage 3** | Stable CPA over 60+ days | **Target CPA (tCPA)** | Set tCPA at ~20% above current actual CPA; tighten by $5–10 every 2 weeks toward target |

**Never launch with tCPA.** The algorithm requires a minimum of 30 conversions to calibrate. Launching tCPA on a new account with no data results in either severe underspend (can't find clicks that meet the target) or poor quality traffic (lowers threshold to spend budget).

**When to use Target ROAS (tROAS):** eCommerce accounts only, when revenue data is passing correctly and ROAS has stabilized over 60+ days. Set tROAS at ~20% below current actual ROAS and tighten over time.

For detailed bid strategy decision criteria and troubleshooting, see `references/bid-strategy-guide.md`.

### 4D. RSA Copy Generation — Structured System

Use this section when writing ad copy from scratch for a new RSA campaign. The structured system below ensures full headline variety and adherence to Google's character limits.

**One question at a time — never ask two questions in the same message.**

**Step 1 — Brand research:** Ask for Challenger's website URL. Then research the site for: all products/services, brand history, value proposition, key benefits, problems solved, and competitive advantages. Summarise findings internally before writing — do not show this to the user.

**Step 2 — Focus:** Ask whether to focus on a specific product/service or the business as a whole.

**Step 3 — Keywords:** Ask the operator to provide the keywords for this ad group/campaign (or confirm from the keyword research already completed).

**Step 4 — Copy type:** Ask which type of copy is needed:
- **Headline** — 20–30 characters (hard limit: 30 characters maximum)
- **Long Headline** — 80–90 characters (for PMAX asset groups)
- **Description** — 80–90 characters
- **All three** — full copy package for this campaign

**Step 5 — Generate structured output:**

For **Headlines** (generate all 55 — operators select the 15 best for the RSA):

| Category | Quantity | Focus |
|----------|----------|-------|
| Keyword Headlines | 5 | Contain the exact or close-variant target keyword; these are the candidates for Headline 1 pin |
| Angle / Features / Benefits | 20 | Value proposition, product benefits, differentiators — mix emotional and rational |
| Pre-Qualification / Location | 10 | Filter for the right audience (location, business type, budget level, professional vs. consumer) |
| Price / Promotion / Offer / Guarantee | 10 | Specific offers, pricing signals, guarantees, free trials |
| Call to Action | 10 | Action-specific CTAs — not "Learn More" but "Get a Free Quote", "Start Free Today", "Book Same-Day" |

**Character counting rule:** Count every character including spaces. 30 characters maximum per headline — if a headline is 31 characters, rewrite it. Verify before presenting.

For **Long Headlines** (PMAX asset groups, 80–90 chars): Generate 5, each with a distinct angle. These can read more like a full benefit sentence.

For **Descriptions** (RSA or PMAX, 80–90 chars): Generate 4 descriptions following the Problem→Solution / Proof+CTA / Offer / Feature List structure from `references/rsa-ad-copy-framework.md`.

**Read `references/rsa-ad-copy-framework.md` → Structured Copy Generation** for category-by-category formula examples and vertical-specific patterns.

---

## Phase 5 — PMAX Campaign Build

Only proceed with PMAX if all eligibility requirements from Phase 1 are confirmed met.

> Before building the PMAX campaign, read [`references/pmax-standards-2025.md`](references/pmax-standards-2025.md) for the complete setup requirements, 2025 feature updates, asset group structure guidance, and coexistence monitoring detail.

### 5A. PMAX campaign settings

- **Budget:** Separate budget from RSA campaigns. PMAX competes across all Google surfaces (Search, Shopping, YouTube, Display, Gmail, Maps). Start at 30–40% of total account budget.
- **Bid strategy:** Maximize Conversions (or Maximize Conversion Value for eCommerce with revenue tracking). Do not use tCPA or tROAS on PMAX launch — same principle as RSA: algorithm needs data first.
- **Location and language:** Match RSA campaign settings

### 5B. Audience signals — required

Audience signals tell PMAX what kind of users to target. Without them, the algorithm starts from scratch and learns slowly. With them, it has a baseline to work from immediately.

All three signal types should be applied:

1. **Customer Match list** — upload Challenger's existing customer or lead email list (Google Ads → Tools → Audience Manager → Customer Lists). This is the strongest signal — it shows Google exactly who has already bought from or engaged with Challenger.
2. **Website visitors** — All website visitors (last 30 days). Must have ≥ 100 users. If below threshold, this signal can't be used yet.
3. **Custom intent audience** — Create a custom audience in Audience Manager based on: target keyword URLs (e.g., Google SERPs for the top 5–10 target keywords), and relevant apps or websites the target customer uses.

### 5C. Search themes (2025 update)

Search themes are keyword-like signals that guide PMAX toward specific search queries. They are not the same as keywords — PMAX doesn't use keywords in the traditional sense — but search themes shape where it focuses on the Search surface.

- Add up to 50 search themes
- Source: use the high-intent keywords from the approved keyword list (from google-ads-keyword-research)
- Do not add branded terms to PMAX search themes — branded traffic should be captured by the Branded RSA campaign, not PMAX

### 5D. Campaign-level negative keywords (2025 update)

PMAX now supports up to 10,000 campaign-level negative keywords.

At minimum, add:
- The account-level negative keyword list
- All client brand name variations (to keep branded traffic in the Branded RSA campaign)
- Competitor brand names (if not running competitor campaigns — otherwise PMAX will bid on competitor terms)
- Any irrelevant service/product terms specific to this PMAX campaign

### 5E. Asset groups

Create one asset group per major product or service category. Do not use one generic asset group for all products — PMAX targets different audiences per asset group and can't differentiate what you're promoting if everything is mixed.

**Required assets per asset group:**

| Asset type | Minimum | Best practice |
|------------|---------|--------------|
| Images | 3 | 5–10, mix of square (1:1) and landscape (1.91:1) |
| Logo | 1 | Square format, PNG transparent background |
| Video | 1 | Minimum 10 seconds. **Provide a real video — do not let Google auto-generate.** Auto-generated videos are low quality and often misrepresent the brand. |
| Headlines | 3 | Up to 5 — keyword-relevant, benefit-forward |
| Long headlines | 1 | Up to 5 — 90-character extended headlines |
| Descriptions | 2 | Up to 5 — problem → solution → CTA |
| Final URL | 1 | Must be specific to the asset group theme, not the homepage |

**Video — critical note:** If no video is provided, Google will auto-generate one from the images and headlines. Auto-generated videos are typically poor quality and can reflect badly on Challenger's brand. Always request video assets from Challenger before building PMAX. If unavailable: create a simple slideshow-style video using the available images and brand colors. A basic branded video is significantly better than auto-generation.

### 5F. PMAX and RSA coexistence

When PMAX and RSA Search campaigns run simultaneously, PMAX takes priority for queries it determines it can win on Search. This can cannibalize RSA impression share.

Monitor weekly for the first 30 days after PMAX launch:
- RSA campaigns: check Impression Share — has it dropped since PMAX went live?
- If RSA impression share drops >20% after PMAX launch, investigate: are PMAX search themes overlapping with RSA keyword themes?
- Adjustments: tighten PMAX search themes, add RSA core keywords to PMAX negative list, or adjust budget allocation

---

## Phase 6 — Change Log Setup

Before any campaign goes live, create and populate the change log.

**Why:** Every change to a Google Ads account must be documented. Without a change log, performance shifts become impossible to diagnose, multiple operators conflict with each other's changes, and account history is lost during transitions.

**Location:** Google Ads Workbook → Change Log tab

**Format:**

| Date | Change Made | Campaign / Ad Group | Changed By | Reason |
|------|-------------|---------------------|------------|--------|
| 2026-04-06 | Disabled auto-applied recommendations | Account level | [AM Name] | standard — all changes must be intentional |
| 2026-04-06 | Added 4 sitelinks, 6 callouts, brand logo at account level | Account level | [AM Name] | Required extensions before launch |
| 2026-04-06 | Created Branded Search campaign | [Client] — Branded | [AM Name] | Separate brand traffic from non-branded; protect brand impression share |
| 2026-04-06 | Launched Non-Branded RSA — Theme 1 | [Client] — NB Theme 1 | [AM Name] | First go-live; Maximize Clicks bid strategy |

**Log every action taken during the build session.** The change log is not optional — it is part of the deliverable.

---

## Phase 7 — Synthesis Brief

Before building the deliverable, write a brief summary for orchestrator handoff.

**Campaign Build Key Findings**
Extract and summarize:
- Campaign structure created (account-level settings finalized; branded campaign isolated; non-branded campaigns organized by theme; RSA vs PMAX split)
- Budget allocations set (daily budgets confirmed; total monthly allocation verified; percentage split between branded/non-branded/PMAX)
- Targeting parameters confirmed (location targeting set to Presence; language set correctly; ad schedules applied; network settings locked to Search only)

**Priority for downstream skills:** google-ads-prelaunch-qa should verify: conversion tracking is still recording (critical gate); all extensions are deployed and approved by Google (approval timing); Quality Score signals are healthy on top ad groups; change log is fully populated before launch; 24-hour post-launch monitoring checklist is ready.

*If running standalone, share this with the operator before the full deliverable.*

---

## Phase 8 — Confirm Output Format + Branding

Before building the deliverable, ask two questions:

> "Campaign build is complete. What format would you like the output in?
>
> 1. **Campaign Build Summary (DOCX)** — Full written brief covering account structure, campaign settings, ad copy rationale, bid strategy plan, and PMAX setup (if applicable). Best for client review or internal handoff.
> 2. **Structured text** — Plain text checklist of what was built and key settings. Best for Notion or Slack.
> 3. **Something else** — Just tell me."

Wait for the answer. Then ask:

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colors, fonts, and layout rules before building.

Build based on chosen format:
- **Campaign Build Summary** → invoke the docx skill; apply or client branding
- **Structured text** → output as plain text or Markdown; no skill needed

---

## Error Handling

**Conversion tracking not working:** Do not proceed with the campaign build. Redirect to google-ads-account-audit to resolve tracking first. Campaigns launched without working conversion tracking cannot be optimized and will waste budget.

**Keyword list not yet approved:** Do not import keywords or create ad groups without execute_tier_approver sign-off. Use placeholder ad group structure if needed but clearly mark as pending import. Complete the approval step via google-ads-keyword-research before finalizing.

**PMAX eligibility requirements not met:** Build RSA campaigns only. Add a note in the Google Ads Workbook flagging PMAX for reassessment: "Reassess PMAX eligibility at [date] when account reaches 30 conversions/month."

**Client cannot provide video assets for PMAX:** Do not launch PMAX with auto-generated video. Options: (1) delay PMAX launch until video is provided, (2) create a simple branded slideshow video using static images and brand colors, (3) launch PMAX with video format disabled (Google Ads → PMAX → Asset Group → Video → disable video ad format). Document the decision in the change log.

**Customer Match list unavailable:** PMAX can still be built using website visitors and custom intent as audience signals, but learning will be slower. Note the limitation in the Google Ads Workbook and revisit once Challenger can provide a list.

---

## QA Gate

Before handing off to the pre-launch QA skill, verify:

- [ ] Auto-applied recommendations disabled at account level
- [ ] Minimum extensions set at account level (4 sitelinks, 6 callouts, brand logo, 4 images)
- [ ] Branded campaign fully separated from non-branded campaigns
- [ ] Brand keywords added as negatives in all non-branded campaigns
- [ ] Non-branded keywords added as negatives in branded campaign
- [ ] Each RSA ad group: minimum 2 RSAs, maximum 3 active
- [ ] Headline 1 pinned to keyword-specific headline in every RSA
- [ ] Bid strategy set correctly per account stage (Maximize Clicks for new accounts)
- [ ] PMAX eligibility confirmed before building (if applicable)
- [ ] PMAX audience signals all present: Customer Match + website visitors + custom intent
- [ ] PMAX search themes populated (min 10, max 50)
- [ ] PMAX campaign-level negatives applied
- [ ] Video assets provided for PMAX (no auto-generated video)
- [ ] Change log created and all build actions logged
- [ ] All campaign budgets set and total = confirmed monthly budget

---

## References

Read these files when the relevant phase is reached:

- **[Bid Strategy Guide](references/bid-strategy-guide.md)** — Read during Phase 4C for the full bid strategy decision framework, including how to identify when an account is ready to graduate between stages, how to troubleshoot underspend on tCPA, and how to set realistic tROAS targets for eCommerce.
- **[PMAX Standards 2025](references/pmax-standards-2025.md)** — Read at the start of Phase 5 for the complete PMAX setup requirements, 2025 feature updates (campaign-level negatives, search themes), asset group best practices, and coexistence monitoring guidance.
- **[RSA Ad Copy Framework](references/rsa-ad-copy-framework.md)** — Read during Phase 4B and 4D. Phase 4B: structural rules, pinning guidance, ad strength vs. relevance. Phase 4D: structured copy generation — category-by-category formula examples (keyword, feature/benefit, pre-qualification, price/offer, CTA), vertical quick reference, and character counting guide.
