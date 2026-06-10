---
name: google-ads-keyword-research
description: 'Full Google Ads keyword research - seed terms, intent classification (Info/Trans/Nav + Top/Mid/Bottom funnel), semantic ad groups, brand/competitor/negative lists, import-ready output. MANDATORY TRIGGER: any mention of "Google Ads keyword research", "Google Ads keyword list", "Google Keyword Planner", "find keywords for Google Ads", "ad group keyword research", "keyword intent classification". Do NOT use for: SEO keyword research (use `keyword-research`). Meta or Reddit targeting.'
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/competitor-map.md, assets/customer-archetypes.md, assets/team-roles.md, CONFIG.md


# Google Ads Keyword Research

## What this skill does

This skill walks an Ads AM through Challenger's structured keyword research process — from understanding Challenger and defining seed terms, through Keyword Planner discovery, filtering, intent classification, semantic ad group formation, and building brand/competitor/negative lists — ending with a client-approved, import-ready keyword set.

Use this skill when:
- Setting up keyword research for a new Google Ads client
- Expanding keyword coverage for an existing account
- Rebuilding keyword structure after a campaign restructure
- Adding a new service or product to an existing account

Output options:
- **Keyword Research Document (DOCX)** — full written summary covering keyword strategy, ad group structure, and import plan, best for client review or internal sign-off
- **Structured text / table** — formatted keyword list with ad group assignments and intent tags, best for Notion or direct import prep
- **Something else** — confirm with user

---

## Phase 1 — Context & Scope

Before opening Keyword Planner, understand Challenger and what this research needs to achieve.

**Ask the following:**

1. **Client name and vertical:** eCommerce or lead gen? B2B or B2C?
2. **Core products or services to advertise:** What specifically needs to appear in Google Ads? (Not everything the business does — what are the priority campaigns?)
3. **Target geography:** National, regional, or specific cities/states? (This affects search volume significantly — a keyword with 5,000 national searches may have only 200 in a target city)
4. **New or existing account:** New accounts start with exact match only. Existing accounts with 30+ days of data can introduce phrase match.
5. **Brand campaign included?** Brand keywords (client's own name) always go in a separate campaign — confirm whether this research covers non-branded only, or also branded terms.
6. **Known competitors:** Who are the main competitors? Needed for the competitor keyword list.
7. **Any services/products to explicitly exclude?** Things Challenger no longer offers, doesn't want to advertise, or where budget is too thin.

---

## Phase 2 — Seed Term Definition

Seed terms are the starting point for Keyword Planner discovery. Getting these right determines the quality of the output.

**What makes a good seed term:**
- Written from the customer's perspective, not Challenger's internal language
- Specific enough to return relevant results, not so broad it floods with irrelevant terms
- Non-branded — client's brand name is not a seed term (goes in the brand keyword list)
- Includes geographic modifier if Challenger is local (e.g., "plumber Minneapolis" not just "plumber")

**Common mistakes to avoid:**
- Too broad: "cleaning" instead of "commercial cleaning services"
- Too internal: "facility maintenance solutions" instead of "office cleaning company"
- Too long-tail at seed stage: "emergency HVAC repair for multi-unit residential buildings" — start broader, Keyword Planner will surface the long-tail variants

**Seed term formula:** [Core service/product] + [Target customer type or use case] + [Geographic modifier if local]

**Examples by vertical:**

| Vertical | Too broad | Too narrow (for seed) | Good seed terms |
|----------|-----------|----------------------|----------------|
| Commercial HVAC | "heating" | "emergency HVAC for commercial buildings Minneapolis" | "commercial HVAC Minneapolis", "HVAC maintenance contract", "commercial AC repair" |
| Personal injury law | "lawyer" | "car accident attorney settlement negotiation" | "personal injury lawyer", "car accident attorney", "injury claim attorney" |
| Shopify app (SaaS) | "software" | "inventory management for Shopify stores with 3PL" | "Shopify inventory app", "ecommerce inventory software", "Shopify stock management" |
| Wedding photography | "photography" | "candid documentary wedding photographer" | "wedding photographer [city]", "wedding photography packages", "wedding photographer near me" |

**Target:** 5–15 seed terms covering the full range of what needs to be advertised. Too few = limited discovery. Too many = noisy, overlapping results.

**Optional seed source — GSC organic queries (via Composio):**

For clients with existing organic presence and `google_search_console` connected via Composio (see the live MCP connectors), pull GSC top non-branded queries by clicks for the past 90 days. These are queries Google has already confirmed lead users to the site — they are battle-tested seed terms with proven intent. Use case: *"pull GSC top non-branded queries by clicks for site {url}, last 90 days"*.

Skip this step if: (a) Composio is not connected, (b) Challenger has no organic presence (new site / never indexed), or (c) GSC site permission isn't available. The original seed-term formula above stands on its own — this is purely an enrichment when the data is there.

Document seed terms in the Google Ads Workbook (Keywords tab) before running Keyword Planner.

---

## Phase 3 — Keyword Planner Discovery

**Tool:** Google Ads → Tools → Keyword Planner → Discover new keywords

**uses Google Keyword Planner as the only tool for keyword volume data.** SEMrush can supplement for competitive analysis, but it estimates search volume from panel data, which diverges from Google's own figures — especially for niche, local, or B2B terms.

**Step-by-step:**

1. Open Keyword Planner → **Discover new keywords**
2. Enter seed terms (one per line or comma-separated — do not mix different themes in a single run; run separately for each major service theme if Challenger has multiple)
3. Set location to Challenger's target geography (be specific — not "United States" if Challenger only serves Minnesota)
4. Set language to English (or client's target language)
5. Click **Get results**
6. Review the results page — note the columns: Avg. monthly searches, Competition (ad competition, not SEO), Top of page bid low range, Top of page bid high range
7. Apply the volume filter: **Avg. monthly searches ≥ 30**
8. Export the filtered list to CSV → open in Google Ads Workbook (Keywords tab)

**Alternative — AI-generated keyword list (when Keyword Planner access is unavailable):**

If the operator cannot access Keyword Planner at this stage, generate 30 keywords directly using knowledge of Challenger's industry, product, and target audience. Apply the same seed term logic — customer-perspective language, geographic modifiers if local, no brand terms.

Output the 30 keywords in the structured table format (see Phase 4 — this applies to both Keyword Planner results and AI-generated lists). Focus specifically on **Commercial** and **Transactional** intent terms that imply readiness to buy — not research or informational queries.

This AI-generated list is a starting point only. Validate with Keyword Planner before final import to confirm search volume and bid estimates.

**Interpreting volume for niche or B2B clients:**

The 30 searches/month threshold is a guideline, not a hard rule. For high-value B2B or specialty markets, a keyword with 10–20 monthly searches may represent $50,000+ in potential revenue per conversion. Use judgment — if the top-of-page bid is very high (indicating advertisers find it profitable), consider including even low-volume terms. Flag these and discuss with the team lead.

---

## Phase 4 — Intent Classification & Filtering

After exporting (or generating), classify each keyword across three dimensions. All three columns must be completed — they serve different purposes and together produce a keyword list Challenger can review and understand.

**Sort by: Top of Page Bid (High Range) — descending**

Top-of-page bid high range is the best available proxy for commercial intent. Advertisers pay more to show for keywords where users convert — so high bid = high-intent audience.

### Dimension 1: Action Tag

Determines whether to include or exclude the keyword from campaigns:

| Tag | What it means | Signals | Action |
|-----|--------------|---------|--------|
| **High** | User is ready to act — buy, hire, call, or request a quote today | Contains: near me, [city], pricing, cost, quote, hire, buy, order, get, best [service] | Include in initial campaigns |
| **Mid** | User is comparing or evaluating options | Contains: best, reviews, vs, comparison, options, top, alternatives | Include in Phase 2 expansion after launch data |
| **Low** | User is researching or learning — unlikely to convert | Contains: how to, DIY, what is, free, guide, tutorial, template | Exclude; add to negative keyword list |
| **Exclude** | Job seekers, competitors, or irrelevant intent | Contains: jobs, careers, salary, hiring, [unrelated industry] | Add to negative keyword list |

### Dimension 2: Search Intent

Classifies the type of search intent — used in Challenger-facing keyword table and for copy strategy:

| Search Intent | Definition | Examples |
|--------------|-----------|---------|
| **Transactional** | User intends to take an action — buy, book, hire, sign up | "emergency plumber Minneapolis", "buy Shopify inventory app", "hire personal injury lawyer" |
| **Navigational** | User is looking for a specific brand or website | "[Brand name]", "[Brand] login", "[Brand] pricing page" |
| **Informational** | User wants to learn or research | "how to fix a leaky faucet", "what is inventory management software", "personal injury lawsuit process" |

**For Google Ads campaigns, prioritise Transactional intent.** Informational keywords belong in the negative list unless Challenger has specific educational content goals.

### Dimension 3: Funnel Stage

Maps where the keyword sits in the buyer journey — informs bidding priority and copy angle:

| Funnel Stage | What it means | Examples |
|-------------|--------------|---------|
| **Bottom** | High purchase intent — near the decision point | "emergency HVAC repair near me", "personal injury lawyer free consultation", "Shopify inventory app free trial" |
| **Middle** | Comparing options, evaluating providers | "best commercial cleaning company Minneapolis", "top inventory apps for Shopify", "personal injury lawyer reviews" |
| **Top** | Awareness stage — broad research | "how to choose an HVAC company", "what is inventory management", "personal injury claim process" |

**Bottom-of-funnel keywords get the highest bids and the most ad copy testing attention.** Top-of-funnel keywords are almost always excluded or added to the negative list for Search campaigns.

### Standard Keyword Output Table

Every keyword in the list must be documented in this format before client review:

| Keyword | Avg. Monthly Volume | Search Intent | Funnel Stage | GH Action Tag | Ad Group | Match Type | Rationale |
|---------|---------------------|--------------|-------------|---------------|----------|-----------|-----------|
| emergency plumber Minneapolis | 320 | Transactional | Bottom | High | Emergency Plumbing Mpls | [Exact] | High-volume, clear emergency intent — user needs to call now; top-of-page bid indicates strong advertiser competition = proven conversion keyword |
| best plumber Minneapolis | 110 | Transactional | Middle | Mid | — (Phase 2) | — | Comparison intent — worth monitoring via Search Terms from Bottom-of-funnel campaigns first before bidding directly |
| how to fix a leaky faucet | 1,900 | Informational | Top | Exclude | — | — | Research intent, DIY signal — zero purchase intent; add to negative list |

**Rationale column:** Write one sentence per keyword explaining why it is or isn't included. This is not optional — it is the primary tool for client education during the sign-off conversation. Clients often question specific keyword inclusions or exclusions; the rationale column provides the answer before they ask.

**Document all classifications in the Google Ads Workbook (Keywords tab).** Do not skip this step — it is the decision point that separates budget-efficient campaigns from ones that bleed spend on low-quality clicks.

---

## Phase 5 — Semantic Ad Group Formation

Group keywords into ad groups based on the rule: **if the same RSA headline can serve every keyword in the group, they belong together.**

If writing the Headline 1 would need to change significantly between two keywords, they need separate ad groups.

**The grouping test — ask for each pair of keywords:**
> "Can I write one headline that's equally relevant and compelling for both of these keywords?"

If yes → same ad group. If no → separate ad groups.

**Ad group size limit:** Maximum 15–20 keywords per ad group. Beyond 20, the keyword-to-ad relevance drops, Quality Score suffers, and the ad group becomes harder to manage.

**Naming convention:** Ad group names should describe the keyword theme, not be generic.
- Good: "Emergency HVAC Repair Minneapolis", "Commercial AC Installation", "HVAC Maintenance Contracts"
- Bad: "Ad Group 1", "Keywords - Group A", "HVAC"

**Example grouping — commercial cleaning client:**

```
Campaign: Non-Branded — Office Cleaning
  Ad Group: Office Cleaning Services
    - office cleaning services minneapolis
    - commercial office cleaning
    - professional office cleaners
    - office janitorial services

  Ad Group: Daily Office Cleaning
    - daily office cleaning
    - recurring office cleaning service
    - weekly office cleaning minneapolis

Campaign: Non-Branded — Post-Construction Cleaning
  Ad Group: Post-Construction Cleanup
    - post construction cleaning minneapolis
    - construction cleanup services
    - after renovation cleaning
```

Why split Office Cleaning from Post-Construction into separate campaigns: the audience and copy are different enough that budget control and bidding at the campaign level makes sense.

Document ad group assignments in the Google Ads Workbook.

---

## Phase 6 — Brand, Competitor & Negative Keyword Lists

Build three lists in parallel. These are applied at account or campaign level before launch.

### Brand keyword list

All variations of Challenger's own business name:
- Exact brand name (and common misspellings)
- Brand + service/product: "[Brand] pricing", "[Brand] reviews", "[Brand] [service]", "[Brand] near me"
- Brand + location if local: "[Brand] [city]"

**These keywords go in a dedicated Branded Search campaign only — never in non-branded campaigns.**

Why this matters: Brand keywords have naturally high Quality Scores and low CPCs. Mixing them into non-branded campaigns inflates average Quality Score, masks CVR, and makes it impossible to accurately evaluate non-branded performance.

Add all brand name variations to the **negative keyword list of every non-branded campaign** to prevent brand queries from triggering non-branded ads at higher bids.

### Competitor keyword list (requires execute_tier_approver approval)

If Challenger wants to run competitor campaigns:
- Competitor brand names (exact + phrase match)
- Competitor + comparison: "[Competitor] alternative", "[Competitor] vs [Client Brand]"
- Competitor + product/service: "[Competitor] [service] [city]"

**Always get explicit execute_tier_approver approval before building competitor campaigns.** Some clients are uncomfortable with the tactic; others have legal restrictions on comparative advertising. Document the approval in the change log.

### Negative keyword list

Built in layers:

**Account-level negatives (apply to all campaigns):**
Add these as a Negative Keyword List at the account level — they automatically apply to current and future campaigns.

Standard negative categories:
- Employment: jobs, careers, salary, hire, hiring, employment, intern, internship, apprenticeship, vacancy, job openings
- Free/DIY: free, DIY, how to, tutorial, guide, template, checklist, sample, example (unless client offers educational content)
- Research-only: what is, definition, meaning, history, news, statistics
- Negative sentiment: complaints, scam, lawsuit, fraud, problems, bad reviews
- Price-only: cheapest, free quote (distinguish from "get a quote"), no cost

**Campaign-level negatives:**
- Branded campaign: add all non-branded service keywords as negatives (to prevent bleed from non-branded campaign getting rerouted)
- Non-branded campaigns: add all brand name variations as negatives
- PMAX: add brand name variations + competitor brand names + account-level negatives

**Build the negative list before any campaign goes live** — adding negatives after launch means budget has already been wasted on irrelevant clicks.

For a more complete list of industry-specific negatives, see `references/negative-keyword-library.md`.

---

## Phase 7 — Match Type Assignment

After intent classification and grouping, assign match types before import.

**Rule: new accounts use exact match only.**

Exact match (`[keyword]`) ensures Google only shows the ad when the query is equivalent to the target keyword. This gives maximum control while conversion data is being established, prevents irrelevant spend, and makes the Search Terms report clean and actionable.

**Match type progression:**

| Account stage | Match types | Rationale |
|--------------|-------------|-----------|
| 0–30 days (new) | Exact match only | Maximum control; build clean baseline |
| 30–90 days | Add phrase match for keywords with relevant Search Terms variants | Keyword Planner won't catch every valuable variant; phrase match expands coverage safely |
| 90+ days | Consider broad match with strong negative lists for specific campaigns | Only when there's enough data to catch irrelevant queries quickly |

**Match type format:**
- Exact: `[keyword]` — e.g., `[emergency HVAC repair Minneapolis]`
- Phrase: `"keyword"` — e.g., `"emergency HVAC repair Minneapolis"`
- Broad: `keyword` — e.g., `emergency HVAC repair Minneapolis` (no brackets or quotes)

**Never use broad match on a new account without a well-built negative keyword list.** Without negatives, broad match will trigger irrelevant queries from day one and waste budget before there's data to diagnose it.

---

## Phase 8 — Client Approval

Before importing any keywords into Google Ads, send the keyword list for review.

**What to send:**
- Export the Google Ads Workbook Keywords tab as CSV or share the Google Sheet link
- Include all classification columns: keyword, search intent, funnel stage, GH action tag, ad group assignment, match type, avg. monthly volume, rationale

**The approval message:**
> "Here is the keyword list for [Client Name] covering [X] ad groups across [Y] campaigns. Please review and let me know: (1) any keywords to remove, (2) any important terms we've missed, (3) any services/products that should not be advertised. I'll hold on import until you confirm."

**Do not import until approval is received.** This step prevents advertising for services Challenger no longer offers, including competitor terms Challenger is uncomfortable with, and missing priority terms Challenger knows but that didn't appear in Keyword Planner.

Document the approval in the change log: date, who approved, any changes requested.

---

## Phase 9 — Import & Documentation

Once approved, import the keyword list into Google Ads.

**Manual import (small lists):**
1. Google Ads → Campaign → Ad Groups → select the correct ad group
2. Keywords tab → + New keyword
3. Enter each keyword in correct match type format

**Bulk import via CSV (larger lists):**
1. Prepare a CSV with columns: Campaign, Ad Group, Keyword, Match Type, Final URL (optional), Max CPC (optional)
2. Google Ads → Tools → Uploads → Upload → Keywords
3. Review the preview for errors before confirming
4. Confirm import completed with no errors

**After import:**
- Verify all keywords are in the correct ad groups
- Verify match types are set correctly
- Log the import in the change log: date, number of keywords, campaigns affected, AM name

---

## Phase 10 — Synthesis Brief

Before building the deliverable, write a brief summary for orchestrator handoff.

**Keyword Research Key Findings**
Extract and summarize:
- Priority keyword clusters (high-volume, high-intent terms grouped by semantic theme; search volume totals per cluster)
- Intent distribution (percentage of Transactional vs Navigational vs Informational keywords; bottom-funnel percentage)
- Negative keyword strategy (account-level negatives to apply; campaign-level negatives by theme; competitor brand exclusions if applicable)
- Match type roadmap (starting with exact match for new accounts; recommended phase 2 transition timeline to phrase match at 30-day mark)

**Priority for downstream skills:** google-ads-campaign-build should focus on semantic ad group structure that mirrors the keyword clusters; ensuring Headline 1 pinning aligns with the keyword themes; confirming match type rollout timeline in the bid strategy plan.

*If running standalone, share this with the operator before the full deliverable.*

---

## Phase 11 — Confirm Output Format + Branding

Before building the deliverable, ask two questions:

> "Keyword research is complete and approved. What format would you like the output in?
>
> 1. **Keyword Research Document (DOCX)** — Full written brief covering keyword strategy, ad group structure, intent rationale, and import plan. Best for client review or internal sign-off before campaign build.
> 2. **Structured text / table** — Formatted keyword list with ad group assignments, match types, and intent tags. Best for Notion or as a reference during campaign build.
> 3. **Something else** — Just tell me."

Wait for the answer. Then ask:

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colors, fonts, and layout rules before building.

Build based on chosen format:
- **Keyword Research Document** → invoke the docx skill; apply or client branding
- **Structured text / table** → output as plain text or Markdown; no skill needed

---

## Error Handling

**Keyword Planner returns very low volume for all seed terms:** Broaden the seed terms and expand the geography first. If national volume is still below 30 for all terms, the niche may not have meaningful Google search demand — flag to the team lead before building campaigns. Spending budget on keywords with no search volume results in ads that rarely show.

**Client requests a keyword that appears low-intent or irrelevant:** Include it with a note flagging the concern. The client knows their business better than the keyword data does — sometimes niche terms convert well despite low Keyword Planner signals. Mark for early review in the Search Terms report (30 days post-launch) to validate or remove.

**Keyword Planner shows no data for specific local terms:** Some hyper-local queries don't appear in Keyword Planner because volume is below the display threshold (usually <10/month). These terms can still be added as exact match — if the search doesn't happen, the keyword simply won't trigger. Include them if Challenger confirms the query pattern exists.

**Client delays approving the keyword list:** Do not import without approval. Send one follow-up with a clear deadline ("I'll hold the import until [date] to keep us on schedule"). If approval isn't received by the launch date, launch without those keywords and add them in the first week once approved.

---

## QA Gate

Before delivering the keyword research output, verify:

- [ ] Seed terms documented and reviewed
- [ ] Keyword Planner run with correct geography and language settings
- [ ] Volume filter applied (≥ 30 average monthly searches, with exceptions noted)
- [ ] All keywords tagged with: GH action tag (High/Mid/Low/Exclude) + Search Intent (Transactional/Navigational/Informational) + Funnel Stage (Bottom/Middle/Top) + Rationale
- [ ] Keywords grouped into semantic ad groups (max 20 per group)
- [ ] Brand keywords isolated to brand list (not mixed into non-branded ad groups)
- [ ] Competitor keyword list created and execute_tier_approver approval documented (if running competitor campaigns)
- [ ] Negative keyword list built at account level
- [ ] Match types assigned (exact match for new accounts)
- [ ] Client sign-off received and documented in change log
- [ ] Import completed and verified in Google Ads

---

## References

Read these files when the relevant phase is reached:

- **[Negative Keyword Library](references/negative-keyword-library.md)** — Read during Phase 6 when building the negative keyword list. Contains industry-specific negative keyword sets by vertical (legal, home services, SaaS, eCommerce, healthcare, financial services) plus universal negatives that apply to all accounts.
- **[Keyword Research Process — Detailed Walkthrough](references/keyword-research-process.md)** — Read at the start of Phase 3 for the full step-by-step Keyword Planner workflow, including how to handle niche markets, multiple service themes, and the transition from exact to phrase to broad match over time.
