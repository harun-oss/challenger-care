# Port Manifest · Canonical Skill Inventory

**Source of truth for every skill in the Challenger Care plugin.**

This file is read by:
- `scripts/validate.py` (checks repo state matches manifest)
- `scripts/sync-workflows.py` (regenerates dashboard Library tab)
- `skills/orchestrator/SKILL.md` (knows what to route across)
- The 90-day cut/keep review (which skills are pulling their weight)

When a skill is added, removed, or changes status, edit this file first. Everything else follows from it.

---

## Status legend

- **kept** · existing Challenger skill · stays as-is after name → CONFIG substitution
- **kept-better** · existing Challenger skill that beats the GrowthHit equivalent · keep, port GH as a paired twin
- **kept-paired** · existing Challenger skill paired with 1-2 GH skills for depth
- **port** · GrowthHit skill being brought in
- **net-new** · created from scratch for Challenger
- **system** · invoked by code/schedule, not by users

## Tier legend

- **generate** · drafts only, no live changes
- **stage** · pre-loads into a tool, awaits approval
- **execute** · live customer-facing change OR money out

## Library-visible flag

- **entry** · appears as a card in the Library tab (15 total)
- **spoke** · hidden in Library · reachable via orchestrator or named chains

---

## The 15 entry cards

| # | Card title | Bound spokes |
|---|---|---|
| 1 | Launch something new | launch-new-product · launch-new-bundle-or-offer · launch-sale-promo · onboard-new-subscribers · subscription-migration-amazon-to-shopify · tiktok-shop-launch-prep |
| 2 | Fix something broken | fix-broken-flow · diagnose-checkout-funnel · refresh-underperforming-pdp · copy-messaging-audit · heuristic-analysis |
| 3 | Why did X drop? | why-sales-dropped · diagnose-checkout-funnel |
| 4 | Where to focus this month? | highest-leverage · leverage-point-assessment · whats-working-to-scale · model-unit-economics · unit-economics-ecom |
| 5 | Make this week's creative | create-this-weeks-ad-creative · reddit-ad-builder · meta-ads-copywriting · ugc-creator-kit · creator-outreach |
| 6 | Make this week's content | create-this-weeks-content · reddit-founder-post |
| 7 | Run the email machine | build-next-email-flow · klaviyo-flows · klaviyo-campaigns · email-copywriting · email-program-audit · email-strategy |
| 8 | Handle this customer | reply-to-customer-issue · respond-to-negative-review |
| 9 | Check the competition | whats-the-competitor-doing · competitive-analysis · meta-ads-competitive-ad-audit |
| 10 | Prep a paid campaign | meta-ads-campaign-build · meta-ads-tracking-audit · meta-ads-audience-research · meta-ads-creative-testing · meta-ads-experiment-tracker · meta-ads-reporting · meta-ads-value-prop-exercise · google-ads-account-audit · google-ads-campaign-build · google-ads-keyword-research · google-ads-optimization · google-ads-prelaunch-qa · google-ads-reporting · bing-ads · reddit-ads · ab-test-reporting · test-price-claim · testing-roadmap |
| 11 | Amazon ops | amazon-listing-refresh · inventory-restock |
| 12 | Weekly review | weekly-business-review |
| 13 | Listen to customers | customer-voice · voc-analysis |
| 14 | CRO deep dive | heatmap-scrollmap-analysis · session-recording-analysis · user-testing · exit-intent-poll · quantitative-analysis |
| 15 | SEO + content | seo-audit · keyword-research · content-brief · seo-content-writing · ecommerce-seo |

---

## The named chains

| Chain | Sequence |
|---|---|
| 3-pack launch | launch-new-bundle-or-offer → meta-ads-copywriting → email-copywriting → klaviyo-campaigns |
| Meta reactivation | meta-ads-tracking-audit → meta-ads-audience-research → meta-ads-campaign-build → meta-ads-creative-testing → meta-ads-reporting |
| Subscription migration | subscription-migration-amazon-to-shopify → email-copywriting → klaviyo-campaigns → onboard-new-subscribers |
| Email program restart | email-program-audit → email-strategy → klaviyo-flows |
| Quarterly review | leverage-point-assessment → testing-roadmap → competitive-analysis |
| PDP refresh | copy-messaging-audit → heuristic-analysis → refresh-underperforming-pdp → test-price-claim → ab-test-reporting |

---

## Full skill inventory

Columns: name · source · status · tier · entry card · twin pair · trigger event

### System skills (3 · not user-facing · invoked by code/schedule)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| orchestrator | challenger | system | n/a | n/a | n/a | every chat message |
| anomaly-detector | challenger | system | n/a | n/a | n/a | every 4 hours |
| briefing-generator | challenger | system | n/a | n/a | n/a | daily 6am PT |

### Entry-card skills (15 · Library-visible)

These are the 15 user-facing entry cards. Each has bound spokes (see table above). The card itself is also a skill that the orchestrator can route to directly.

Note: entry cards are *meta-skills* that delegate to spokes. They're not implemented as separate SKILL.md files — they're the orchestrator's routing rules. The 15 cards above map to existing or about-to-be-built skills.

### Existing Challenger skills · kept (14 · need name → CONFIG substitution)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| fix-broken-flow | challenger | kept | stage | 2 · Fix something broken | - | underperforming flow detected |
| onboard-new-subscribers | challenger | kept | stage | 1 · Launch | - | first Recharge sub of period |
| diagnose-checkout-funnel | challenger | kept | generate | 2 · Fix · also 3 · Why drop | - | checkout abandonment >70% |
| reply-to-customer-issue | challenger | kept | generate | 8 · Handle customer | - | inbound support ticket |
| respond-to-negative-review | challenger | kept | stage | 8 · Handle customer | - | ≤3-star review on Amazon/JudgeMe |
| inventory-restock | challenger | kept | execute | 11 · Amazon ops | - | days-of-stock <25 |
| launch-new-product | challenger | kept | generate | 1 · Launch | - | new SKU ready |
| launch-new-bundle-or-offer | challenger | kept | stage | 1 · Launch | - | bundle math validated |
| launch-sale-promo | challenger | kept | stage | 1 · Launch | - | calendar promo event |
| creator-outreach | challenger | kept | generate | 5 · Creative | ugc-creator-kit | gifting campaign |
| create-this-weeks-content | challenger | kept | generate | 6 · Content | - | weekly content batch |
| why-sales-dropped | challenger | kept | generate | 3 · Why drop | - | revenue <70% of pace |
| whats-working-to-scale | challenger | kept | generate | 4 · Focus | - | end of month |
| create-this-weeks-ad-creative | challenger | kept | generate | 5 · Creative | reddit-ad-builder | weekly ad batch |

### Existing Challenger skills · kept-better (5 · GH equivalent ports as paired twin)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| build-next-email-flow | challenger | kept-better | stage | 7 · Email | klaviyo-flows | new flow needed |
| customer-voice | challenger | kept-better | generate | 13 · Listen | voc-analysis | monthly VOC scan |
| model-unit-economics | challenger | kept-better | generate | 4 · Focus | unit-economics-ecom | pricing decision |
| highest-leverage | challenger | kept-better | generate | 4 · Focus | leverage-point-assessment | monthly priority |
| whats-the-competitor-doing | challenger | kept-better | generate | 9 · Competition | competitive-analysis | weekly scan |

### Net-new Challenger-only skills (5 · ship in phase 2)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| subscription-migration-amazon-to-shopify | net-new | port | stage | 1 · Launch | - | Amazon → Shopify migration push (largest LTV unlock) |
| amazon-listing-refresh | net-new | port | stage | 11 · Amazon ops | - | quarterly Amazon listing review |
| reddit-founder-post | net-new | port | generate | 6 · Content | - | weekly Reddit reply |
| weekly-business-review | net-new | port | generate | 12 · Weekly review | - | every Friday |
| tiktok-shop-launch-prep | net-new | port | generate | 1 · Launch | - | TikTok Shop catalog prep (briefs Implicit, doesn't run) |

### GH ports · Email (5)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| email-program-audit | growthhit | port | generate | 7 · Email | - | initial Klaviyo diagnostic (one-time, output to asset) |
| email-strategy | growthhit | port | generate | 7 · Email | - | annual email roadmap |
| klaviyo-flows | growthhit | port | stage | 7 · Email | build-next-email-flow | consulting-grade flow build |
| klaviyo-campaigns | growthhit | port | stage | 7 · Email | - | one-time campaign send |
| email-copywriting | growthhit | port | generate | 7 · Email | - | any email writing |

### GH ports · Research (2)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| voc-analysis | growthhit | port | generate | 13 · Listen | customer-voice | survey response analysis |
| competitive-analysis | growthhit | port | generate | 9 · Competition | whats-the-competitor-doing | quarterly Bain Elements of Value deep dive |

### GH ports · Website (2)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| copy-messaging-audit | growthhit | port | generate | 2 · Fix | refresh-underperforming-pdp | before PDP rewrite |
| heuristic-analysis | growthhit | port | generate | 2 · Fix | refresh-underperforming-pdp | before CRO test |

### GH ports · Strategy (3)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| testing-roadmap | growthhit | port | generate | 10 · Paid · also 4 · Focus | test-price-claim | quarterly test backlog |
| unit-economics-ecom | growthhit | port | generate | 4 · Focus | model-unit-economics | consulting-grade unit econ |
| leverage-point-assessment | growthhit | port | generate | 4 · Focus | highest-leverage | quarterly LPA |

### GH ports · Meta Ads (9)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| meta-ads-campaign-build | growthhit | port | execute | 10 · Paid | - | day 1 of Meta reactivation |
| meta-ads-copywriting | growthhit | port | generate | 10 · Paid · also 5 · Creative | - | each Meta ad batch |
| meta-ads-creative-testing | growthhit | port | execute | 10 · Paid | - | weekly DCT experiment |
| meta-ads-competitive-ad-audit | growthhit | port | generate | 9 · Competition | - | before each ad batch |
| meta-ads-audience-research | growthhit | port | generate | 10 · Paid | - | refresh targeting |
| meta-ads-tracking-audit | growthhit | port | stage | 10 · Paid | - | Meta BM recovery |
| meta-ads-reporting | growthhit | port | generate | 10 · Paid | - | weekly + monthly Meta review |
| meta-ads-experiment-tracker | growthhit | port | generate | 10 · Paid | - | post-experiment log |
| meta-ads-value-prop-exercise | growthhit | port | generate | 10 · Paid · also 4 · Focus | - | initial Meta brand alignment |

### GH ports · Google Ads (6)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| google-ads-account-audit | growthhit | port | generate | 10 · Paid | - | account takeover |
| google-ads-campaign-build | growthhit | port | execute | 10 · Paid | - | day 1 of Google launch |
| google-ads-keyword-research | growthhit | port | generate | 10 · Paid · also 15 · SEO | - | before Google campaign |
| google-ads-optimization | growthhit | port | stage | 10 · Paid | - | weekly Google tune |
| google-ads-prelaunch-qa | growthhit | port | stage | 10 · Paid | - | before Google goes live |
| google-ads-reporting | growthhit | port | generate | 10 · Paid | - | weekly + monthly Google review |

### GH ports · Bing Ads (1)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| bing-ads | growthhit | port | execute | 10 · Paid | - | after Google launches (import + LinkedIn layer) |

### GH ports · Reddit Ads (1)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| reddit-ads | growthhit | port | execute | 10 · Paid | - | paid Reddit experiment |

### GH ports · Creative (2)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| reddit-ad-builder | growthhit | port | generate | 5 · Creative | create-this-weeks-ad-creative | new ad concepts from real customer language |
| ugc-creator-kit | growthhit | port | generate | 5 · Creative | creator-outreach | each UGC creator brief |

### GH ports · SEO (5)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| seo-audit | growthhit | port | generate | 15 · SEO | - | one-time then quarterly |
| keyword-research | growthhit | port | generate | 15 · SEO | google-ads-keyword-research | before content planning |
| content-brief | growthhit | port | generate | 15 · SEO | - | per article |
| seo-content-writing | growthhit | port | generate | 15 · SEO | - | per article |
| ecommerce-seo | growthhit | port | stage | 15 · SEO | - | Shopify SEO issue |

### GH ports · CRO deep (5)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| heatmap-scrollmap-analysis | growthhit | port | generate | 14 · CRO deep | - | when Hotjar/Clarity installed |
| session-recording-analysis | growthhit | port | generate | 14 · CRO deep | - | same |
| user-testing | growthhit | port | generate | 14 · CRO deep | - | when testing design decision |
| quantitative-analysis | growthhit | port | generate | 14 · CRO deep | - | when dashboard isn't enough |
| exit-intent-poll | growthhit | port | generate | 14 · CRO deep | - | when poll responses come in |

### GH ports · Closures (1)

| name | source | status | tier | entry card | twin | trigger event |
|---|---|---|---|---|---|---|
| ab-test-reporting | growthhit | port | generate | 10 · Paid · also 2 · Fix | - | A/B test concludes |

### Existing Challenger skills · kept-paired (4 · already counted above, listed here for clarity)

These are the same skills as in "kept" or "kept-better" above. The "paired" label means they have an explicit twin in the GH ports list.

| name | twin |
|---|---|
| refresh-underperforming-pdp | copy-messaging-audit + heuristic-analysis |
| test-price-claim | testing-roadmap |
| create-this-weeks-ad-creative | reddit-ad-builder |
| creator-outreach | ugc-creator-kit |

---

## Skill count reconciliation

| Bucket | Count |
|---|---|
| System | 3 |
| Existing Challenger · kept | 14 |
| Existing Challenger · kept-better | 5 |
| Net-new Challenger-only | 5 |
| GH ports | 42 |
| **Total unique skills** | **69** |
| **User-facing (non-system)** | **66** |

The 4 "kept-paired" skills are already counted in "kept" or "kept-better" buckets.

**Visible in Library:** 15 entry cards.
**Hidden, reachable via orchestrator and chains:** 51 spokes.

---

## What's explicitly cut

| Skill | Reason |
|---|---|
| meta-ads-strategy-deck | Client PPTX, agency artifact |
| meta-ads-creative-testing-methodology | Methodology lives in skill body |
| meta-ads-account-onboarding | One-time done |
| brand-kit | GrowthHit's, not Challenger's |
| closing-deck | Sales tool, N/A |
| unit-economics-leadgen | B2B, N/A |
| hubspot-email | B2B, N/A |
| daily-pm-report | Multi-client agency tool |
| web-qa | Removed per request |
| ads-monthly-performance-deck | Agency deliverable |
| ads-weekly-slack-report | Reporting theater |
| seo-reporting | Agency reporting (port if fractional CMO arrives) |
| meta-ads-scaling | Single-decision rule, not workflow |
| meta-ads-creative-brief | Duplicates ugc-creator-kit + create-this-weeks-ad-creative |
| growthit-orchestrator | Keep ours, graft chain directory pattern |

---

## How this file gets used by code

- **`scripts/validate.py`** check #21: every directory in `skills/` corresponds to a row in this manifest, and vice versa. Files outside the manifest fail. Manifest entries without files fail.
- **`scripts/validate.py`** check #20: for every row with a non-empty `twin` column, both skills must have mutually exclusive "Do NOT use for" clauses in their descriptions.
- **`scripts/sync-workflows.py`**: reads this manifest, regenerates the dashboard's `WORKFLOWS` JS array with only the 15 entry cards (Library-visible) and their bound spokes (as data for the orchestrator).
- **`skills/orchestrator/SKILL.md`**: routes free-form user input to the matching entry card (or directly to a spoke if explicit), then dispatches to bound spokes.
- **Manual editing**: when a skill changes status (cut, archived, new), edit this file first. CI validates the change. Other code follows.

---

## Edit log

| Date | Change |
|---|---|
| 2026-06-10 | v3.1 initial manifest created from v3-port-plan.md |
