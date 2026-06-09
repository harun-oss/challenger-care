# Skill Catalog · Complete Reference

Every skill in the Challenger Care plugin · what it does, what it needs, what it produces, who can run it, how long it takes.

Use this as a lookup when you're not sure which workflow fits the job at hand.

---

## Orchestration skills (3)

These are the background skills that run automatically or behind the command bar.

### orchestrator
**Purpose:** Routes free-form command bar input to the right workflow OR builds a custom skill chain.
**When it runs:** Every time you type something into the command bar.
**Tier:** Varies (matches the underlying workflow it routes to)
**Time:** Depends on the routed workflow
**Inputs:** Free-form text from the command bar
**Outputs:** Whatever the routed workflow produces, plus a transparency summary of what ran.

### briefing-generator
**Purpose:** Produces the daily Morning Briefing on the dashboard.
**When it runs:** Daily at 6:00 AM PT (scheduled).
**Tier:** Generate
**Time:** ~90 seconds
**Inputs:** Live Shopify, Klaviyo, GA4 data; anomaly-detector output
**Outputs:** `outputs/briefing-feed.json` consumed by the dashboard

### anomaly-detector
**Purpose:** Surfaces alerts in the "On your plate" queue.
**When it runs:** Every 4 hours (scheduled).
**Tier:** Generate
**Time:** ~30 seconds
**Inputs:** Live MCP data + thresholds from `CONFIG.md`
**Outputs:** `outputs/anomaly-feed.json` consumed by the dashboard

---

## Launch & Test (6 workflows)

For shipping new things into the world.

### launch-new-product · ~5 min · Generate
**Use when:** A new SKU is about to launch and you need every asset built in Challenger voice.
**Produces:** Positioning · PDP (Shopify + Amazon) · 3 ad concepts · launch email · Reddit post · TikTok scripts · Asana launch checklist
**Don't use for:** Existing product refreshes (use `refresh-underperforming-pdp`)

### launch-new-bundle-or-offer · ~4 min · Stage
**Use when:** Launching a bundle, value pack, gift set — especially the 3-pack as default offer (the AOV unlock).
**Produces:** Bundle math validation · PDP hero · cart upsell module · offer landing page · promo email · 3 ad concepts · first-week organic content
**Don't use for:** Discount-led promos (use `launch-sale-promo`)

### launch-sale-promo · ~3 min · Stage
**Use when:** Running a percentage-off campaign, BFCM, flash sale, or limited-time offer.
**Produces:** Site banner · email + SMS · 2 social posts · Klaviyo segment definition · start/end logic
**Don't use for:** Permanent new SKUs or bundles

### test-price-claim · ~3 min · Stage
**Use when:** You want to A/B test a price point or a hero claim.
**Produces:** Test plan · variant copy · tracking plan · decision tree
**Don't use for:** Email subject line tests (handled inside Klaviyo)

### onboard-new-subscribers · ~6 min · Stage
**Use when:** Building (or rebuilding) the welcome flow for new Recharge subscribers.
**Produces:** 4-email welcome flow architecture · all email HTMLs · subject line variants · Klaviyo setup notes
**Don't use for:** General Welcome Series for non-subscribers (use `build-next-email-flow`)

### build-next-email-flow · ~5 min · Stage
**Use when:** Building a new Klaviyo flow (welcome · browse abandonment · post-purchase · winback · sunset).
**Produces:** Flow architecture · all email HTMLs · subject line variants · Klaviyo setup notes · metrics targets
**Don't use for:** Subscriber-specific welcome (use `onboard-new-subscribers`) or campaigns (use `launch-sale-promo`)

---

## Grow (4 workflows)

The weekly recurring work.

### create-this-weeks-ad-creative · ~4 min · Generate
**Use when:** Producing the weekly batch of ad concepts for Meta / TikTok / Reddit.
**Produces:** 5–8 ad concepts (hook + body + CTA + visual brief) · designer handoff · TikTok scripts · Reddit cuts in founder voice
**Don't use for:** One-off ads (this is for batches)

### create-this-weeks-content · ~3 min · Generate
**Use when:** Producing weekly organic content for TikTok (Implicit) · Reddit (founder voice) · Instagram.
**Produces:** TikTok scripts · Reddit posts · Instagram captions · content calendar
**Don't use for:** Paid ad creative (use `create-this-weeks-ad-creative`)

### refresh-underperforming-pdp · ~5 min · Stage
**Use when:** A product page is converting badly or hasn't been updated.
**Produces:** Current-state audit · full PDP rewrite · 3 hero variants · FAQ block · A/B test plan
**Don't use for:** New product launches (use `launch-new-product`)

### creator-outreach · ~4 min · Generate
**Use when:** Building an influencer/creator prospect list and outreach.
**Produces:** 10–25 prospect list with handles, fit notes · personalized outreach drafts · deal structure · tracking plan
**Don't use for:** Paid Meta influencer ads (different workflow)

---

## Listen (5 workflows)

Before you decide.

### customer-voice · ~2 min · Generate
**Use when:** You want a current read on what customers are saying.
**Produces:** Top 5 themes · emerging patterns · ad-ready quotes by theme · sentiment trend · recommended actions
**Don't use for:** Strategic positioning (use `highest-leverage`) or single-customer reply (use `reply-to-customer-issue`)

### whats-the-competitor-doing · ~3 min · Generate
**Use when:** Weekly competitor scan or ad-hoc deep dive before a launch.
**Produces:** Scan summary · per-brand update · positioning implications · recommended responses
**Don't use for:** Internal product audits (use `refresh-underperforming-pdp` or `heuristic-analysis`)

### why-sales-dropped · ~3 min · Generate
**Use when:** Revenue is lower than expected and you want a diagnostic fast.
**Produces:** Diagnostic summary · funnel comparison · channel breakdown · top 3 likely causes with evidence · recommended next actions
**Don't use for:** Single-day noise — wait 3 days

### whats-working-to-scale · ~3 min · Generate
**Use when:** You want to identify which channels / SKUs / campaigns to double down on.
**Produces:** Top performers per dimension · diagnosis · scale recommendations · risks
**Don't use for:** Diagnosing what's broken (use `why-sales-dropped`)

### diagnose-checkout-funnel · ~3 min · Generate
**Use when:** A specific funnel stage is broken (cart abandonment, checkout drop, device CVR gap).
**Produces:** Stage-by-stage funnel map · device + source segmentation · correlation analysis · top 3 root causes · fix recommendations · reversal test plan
**Don't use for:** Generic "sales dropped" (use `why-sales-dropped`) or email funnel (use `fix-broken-flow`)

---

## Fix (4 workflows)

Reactive operational work.

### reply-to-customer-issue · ~1 min · Generate
**Use when:** A customer email or DM needs a brand-voice response.
**Produces:** Drafted reply (subject + greeting + answer + next step + sign-off)
**Don't use for:** Public negative reviews (use `respond-to-negative-review`) or Reddit (Hayden in founder voice)

### respond-to-negative-review · ~1 min · Stage
**Use when:** A 3-star-or-below review just landed on Amazon or JudgeMe.
**Produces:** Drafted response staged for Hayden's review · escalation flag for sensitive cases
**Don't use for:** Positive reviews · customer support DMs · Reddit

### fix-broken-flow · ~5 min · Stage
**Use when:** A Klaviyo flow is underperforming benchmarks.
**Produces:** Audit summary · diagnosis · pause action · 3 rewrite variants · A/B test plan · decision rule
**Don't use for:** New flows (use `build-next-email-flow`) or one-time sends (use `launch-sale-promo`)

### inventory-restock · ~2 min · Execute
**Use when:** A SKU is approaching stockout or has crossed the restock threshold.
**Produces:** Restock analysis · email to Emanuel · Asana task · cost estimate
**Don't use for:** New launches · general inventory review (run the dashboard) · strategic SKU decisions (use `highest-leverage`)

---

## Plan (2 workflows)

Periodic strategic work.

### highest-leverage · ~6 min · Generate
**Use when:** Start of month/quarter, or feeling overwhelmed by competing priorities.
**Produces:** Leverage point assessment (7 dimensions A–F) with evidence · top 2 focuses recommendation · what to defer
**Don't use for:** Tactical daily decisions (use the dashboard's alerts)

### model-unit-economics · ~4 min · Generate
**Use when:** Before a pricing decision, paid acquisition reactivation, bundle launch, or subscription change.
**Produces:** Contribution margin stack · LTV projections (90/180/365 day) · max CPA scenarios · decision read · sensitivities
**Don't use for:** Brand strategy decisions (use `highest-leverage`)

---

## Quick decision tree

**Have a customer or rating to respond to?** → `reply-to-customer-issue` (private) or `respond-to-negative-review` (public)

**Inventory or operational alert?** → `inventory-restock` · `fix-broken-flow`

**Launching something new?** → `launch-new-product` (single) · `launch-new-bundle-or-offer` (bundle) · `launch-sale-promo` (sale) · `build-next-email-flow` (new flow)

**Generating creative or content?** → `create-this-weeks-ad-creative` · `create-this-weeks-content` · `creator-outreach`

**Diagnosing a problem?** → `why-sales-dropped` (broad) · `diagnose-checkout-funnel` (specific) · `fix-broken-flow` (email)

**Listening before deciding?** → `customer-voice` · `whats-the-competitor-doing` · `whats-working-to-scale`

**Strategic / planning?** → `highest-leverage` · `model-unit-economics`

**Refreshing existing content?** → `refresh-underperforming-pdp` · `fix-broken-flow`

**Testing an idea?** → `test-price-claim`

---

## How skills find each other

Every skill's frontmatter has a `description` field that includes:
- **MANDATORY TRIGGER:** the phrases that should fire this skill
- **Do NOT use for:** the scenarios that should route elsewhere

The orchestrator reads these on every command bar input and picks the right skill (or chain of skills) automatically.

If you find the orchestrator routing wrong frequently to a skill, edit that skill's `description` — sharpen the triggers, or add a clearer "Do NOT use for" line.
