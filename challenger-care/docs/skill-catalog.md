# Skill Catalog · v3.1 (Hub + Spoke)

Complete reference for every skill in the Challenger Care plugin.

**Architecture:** 15 Library entry cards (Jobs-To-Be-Done) bind to ~55 spoke skills. Spokes are invoked via their entry card OR directly via a chain. The orchestrator picks the right route based on user input.

**Canonical source:** `docs/port-manifest.md` is the single source of truth. This catalog is the human-readable reference. If they disagree, the manifest wins.

---

## How to find what you need

**You know what you want to do:** scan the 15 entry cards below. Pick the one that matches the job. Click any spoke under it to fire that skill.

**You don't know the right skill:** just type the request into the command bar in plain English. The orchestrator routes to the right entry card and its primary spoke.

**You want depth on a specific topic:** scan the spoke list under each card. Each spoke has its own SKILL.md you can open in GitHub for the full instructions.

---

## The 15 entry cards

### 1 · Launch something new

When you're shipping a product, bundle, sale, or subscription.

| Spoke | What it does | Tier |
|---|---|---|
| launch-new-product | Full new-SKU launch package · positioning, PDP, ads, email, social, Reddit, Asana checklist | generate |
| launch-new-bundle-or-offer | Bundle math + hero copy + cart upsell + offer page + promo email + first-week ads | stage |
| launch-sale-promo | Banner, email, SMS, social, Klaviyo segment + start/end logic | stage |
| onboard-new-subscribers | Welcome flow for new Recharge subs · first jar email, retention nudge, winback if cancel | stage |
| subscription-migration-amazon-to-shopify | The Amazon S&S → Shopify migration play (stage 1 model · stage 2 execute) | stage→execute |
| tiktok-shop-launch-prep | Catalog + content angles + success metrics · briefs Implicit, doesn't run TikTok Shop | generate |

### 2 · Fix something broken

When a flow, funnel, page, or copy is underperforming.

| Spoke | What it does | Tier |
|---|---|---|
| fix-broken-flow | Pauses underperformer · audits why · builds replacement | stage |
| diagnose-checkout-funnel | Investigates a specific funnel-stage problem · top causes with evidence | generate |
| refresh-underperforming-pdp | Diagnoses then rebuilds hero/benefits/FAQ/CTAs in Challenger voice | stage |
| copy-messaging-audit | Joanna Wiebe Seven Sweeps on website copy | generate |
| heuristic-analysis | Conversion + UX friction audit · scored on Clarity/Trust/CTA/Persuasion/UX | generate |

### 3 · Why did X drop?

When revenue, traffic, conversion, or another metric is below expectation.

| Spoke | What it does | Tier |
|---|---|---|
| why-sales-dropped | Pulls Shopify + GA4 + Klaviyo · diagnoses funnel break · 3 likely causes with evidence | generate |
| diagnose-checkout-funnel | Funnel-stage investigation · cart, checkout, device-specific issues | generate |

### 4 · Where to focus this month?

When you need strategic prioritization · what's the highest leverage right now.

| Spoke | What it does | Tier |
|---|---|---|
| highest-leverage | Grades 7 leverage points (Market/Product/Money/Position/Reach/Convert/Expand) · monthly | generate |
| leverage-point-assessment | Quarterly consulting-grade LPA · same framework, deeper output | generate |
| whats-working-to-scale | Top creative, email, page, SKU · where to put more weight | generate |
| model-unit-economics | CM stack, LTV, max CPA scenarios · Challenger-tuned | generate |
| unit-economics-ecom | Consulting-grade CM1/CM2/CM3 + LTV at 90/180/365 + 3 CPA scenarios | generate |

### 5 · Make this week's creative

When you need ads or ad concepts.

| Spoke | What it does | Tier |
|---|---|---|
| create-this-weeks-ad-creative | 5-8 ad concepts from VOC + brand voice rules | generate |
| reddit-ad-builder | Mines Reddit + reviews + Ad Library to produce ad concepts | generate |
| meta-ads-copywriting | Meta primary text (12 frameworks) + headlines (12 options) + video scripts | generate |
| ugc-creator-kit | Brief doc for external UGC creators · specs, key messages, dos/donts | generate |
| creator-outreach | Find creators · TikTok + Instagram prospects + personalized outreach drafts | generate |

### 6 · Make this week's content

When you need TikTok scripts, Reddit posts, IG captions.

| Spoke | What it does | Tier |
|---|---|---|
| create-this-weeks-content | Weekly batch · TikTok scripts + Reddit posts + IG captions | generate |
| reddit-founder-post | Single founder-voice Reddit reply (high-frequency motion) | generate |

### 7 · Run the email machine

When you're building, sending, auditing, or writing email.

| Spoke | What it does | Tier |
|---|---|---|
| build-next-email-flow | Challenger-tuned Klaviyo flow (welcome, cart, browse, post-purchase, winback) | stage |
| klaviyo-flows | Consulting-grade flow build · deeper than build-next-email-flow | stage |
| klaviyo-campaigns | One-time sends · newsletter, BFCM, promo · A/B testing, segmentation | stage |
| email-copywriting | Any email writing in brand voice · subject lines, preview, body, CTAs | generate |
| email-program-audit | Diagnose current Klaviyo state · gaps · build plan | generate |
| email-strategy | Annual roadmap · flows + segments + cadence + attribution | generate |

### 8 · Handle this customer

When a support ticket or negative review comes in.

| Spoke | What it does | Tier |
|---|---|---|
| reply-to-customer-issue | Brand-voice support reply · specific, useful, doesn't grovel | generate |
| respond-to-negative-review | Public response on Amazon/JudgeMe that protects rating | stage |

### 9 · Check the competition

When you need a competitor scan or positioning analysis.

| Spoke | What it does | Tier |
|---|---|---|
| whats-the-competitor-doing | Recurring scan · Based / Hanz De Fuko / Paul Mitchell · pricing, ads, sentiment | generate |
| competitive-analysis | Quarterly deep · Bain Elements of Value + UX audit | generate |
| meta-ads-competitive-ad-audit | Meta Ad Library + TikTok Ads Library · creative format/hook/copy analysis | generate |

### 10 · Prep a paid campaign

When standing up, tuning, or reporting on paid ad accounts.

**Meta (9):** meta-ads-campaign-build · meta-ads-tracking-audit · meta-ads-audience-research · meta-ads-creative-testing · meta-ads-experiment-tracker · meta-ads-reporting · meta-ads-value-prop-exercise

**Google (6):** google-ads-account-audit · google-ads-campaign-build · google-ads-keyword-research · google-ads-optimization · google-ads-prelaunch-qa · google-ads-reporting

**Other (4):** bing-ads · reddit-ads · test-price-claim · testing-roadmap · ab-test-reporting

(Hidden by default · invoked via the orchestrator or named chains.)

### 11 · Amazon ops

When the cash engine needs attention.

| Spoke | What it does | Tier |
|---|---|---|
| amazon-listing-refresh | Quarterly listing refresh · copy + A+ content + image stack + pricing | stage |
| inventory-restock | Reorder timing from velocity · email to inventory_owner · Asana task | execute |

### 12 · Weekly review

The Friday synthesis.

| Spoke | What it does | Tier |
|---|---|---|
| weekly-business-review | Reads briefing cache + experiment log + Klaviyo + Shopify · 5-section retrospective + next-week plan | generate |

### 13 · Listen to customers

When you want themes from reviews or surveys.

| Spoke | What it does | Tier |
|---|---|---|
| customer-voice | Review mining · 30-day reviews from JudgeMe + Amazon · themes + ad-ready quotes | generate |
| voc-analysis | Open-ended survey response analysis (exit poll, NPS open-ends, post-purchase) | generate |

### 14 · CRO deep dive

When the dashboard isn't enough · diagnostic tools.

| Spoke | What it does | Tier |
|---|---|---|
| heatmap-scrollmap-analysis | Hotjar / Clarity / Lucky Orange heatmap analysis (when tool installed) | generate |
| session-recording-analysis | Structured session replay analysis · Successful/Unsuccessful/Takeaways | generate |
| user-testing | Lyssna preference + design survey tests (when subscription active) | generate |
| exit-intent-poll | Single-question exit poll response analysis | generate |
| quantitative-analysis | GA4-based site analysis · funnel + entry points + top pages | generate |

### 15 · SEO + content

When organic search becomes a priority.

| Spoke | What it does | Tier |
|---|---|---|
| seo-audit | Full technical + on-page + content SEO audit | generate |
| keyword-research | SEO keyword discovery · intent classification · topical authority | generate |
| content-brief | Keyword → writer brief (SERP, structure, E-E-A-T, schema) | generate |
| seo-content-writing | Articles, guides, comparison pages, SEO PDP copy | generate |
| ecommerce-seo | Shopify-specific SEO execution · canonical, faceted nav, product schema | stage |

---

## The 6 named chains

The orchestrator runs these in sequence when the request matches:

| Chain | When | Sequence |
|---|---|---|
| **3-pack launch** | Push the 3-pack as default offer | launch-new-bundle-or-offer → meta-ads-copywriting → email-copywriting → klaviyo-campaigns |
| **Meta reactivation** | Turn Meta back on after BM recovery | meta-ads-tracking-audit → meta-ads-audience-research → meta-ads-campaign-build → meta-ads-creative-testing → meta-ads-reporting |
| **Subscription migration** | Move Amazon S&S subs to Shopify | subscription-migration-amazon-to-shopify → email-copywriting → klaviyo-campaigns → onboard-new-subscribers |
| **Email program restart** | Get Klaviyo running | email-program-audit → email-strategy → klaviyo-flows × N |
| **Quarterly review** | Big-picture strategic review | leverage-point-assessment → testing-roadmap → competitive-analysis |
| **PDP refresh** | Fix an underperforming product page | copy-messaging-audit → heuristic-analysis → refresh-underperforming-pdp → test-price-claim → ab-test-reporting |

---

## System skills (background · not user-invoked)

| Skill | What it does | When it runs |
|---|---|---|
| orchestrator | Routes free-form input to the right entry card / spoke / chain | Every chat message |
| anomaly-detector | Produces "On your plate" alerts for the dashboard | Every 4 hours (scheduled) |
| briefing-generator | Daily Morning Briefing on the dashboard | Daily 6am PT (scheduled) |

---

## Permission tiers

Every skill has one of three tiers:

| Tier | What it means | Who can run |
|---|---|---|
| **generate** | Drafts only · no live changes · no money out · fully reversible | Anyone |
| **stage** | Pre-loads into a tool (Klaviyo, Shopify, Asana) but doesn't publish | marketing_coordinator + above |
| **execute** | Live customer-facing change OR money out | execute_tier_approver only (per CONFIG.md) |

The orchestrator stops on Execute-tier work and confirms approval before any live action.

---

## How this catalog stays current

`docs/port-manifest.md` is the canonical source. When a skill is added, removed, or changes status:

1. Edit `docs/port-manifest.md` first
2. Run `python3 scripts/sync-workflows.py` (regenerates dashboard Library)
3. This catalog gets regenerated (or manually updated) to match
4. Validator (check #21) confirms `skills/` matches the manifest

Quarterly: 90-day cut/keep review. Skills used <2×/month by non-GrowthHit roles get archived.
