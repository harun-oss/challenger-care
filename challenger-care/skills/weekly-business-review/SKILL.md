---
name: weekly-business-review
description: Synthesizes the week. What shipped, what tested, what won, what to do next week. Reads the briefing cache + experiment log + Klaviyo flow performance + Shopify + Amazon. The cadence between daily briefing and monthly leverage assessment. MANDATORY TRIGGER: any mention of "weekly review", "WBR", "this week's review", "what happened this week", "what should we do next week", "Friday review". Do NOT use this for: Daily briefing (briefing-generator runs that). Monthly strategic review (use `leverage-point-assessment` or `highest-leverage`). Specific diagnostic on a single metric (use `why-sales-dropped` or `diagnose-checkout-funnel`).
---

> **Permission tier:** generate · **Time:** 3min · **Tools/context:** assets/brand-strategy.md, assets/goals-targets.md, assets/team-roles.md, assets/usage-log.md, assets/experiment-log.md, assets/promo-calendar.md, CONFIG.md, mcp:shopify, mcp:klaviyo

# Weekly Business Review

## When to use this workflow

Runs every Friday (or scheduled task). The cadence between the daily briefing and the monthly leverage assessment.

The daily briefing tells you what's happening *today*. The monthly LPA tells you *where to focus*. The weekly review is the retrospective + planning step in between: what shipped, what tested, what we learned, what's queued.

The marketing coordinator runs this most weeks; the {{roles.founder}} reads it Monday morning.

## What you need

Nothing required · this skill is the closest thing to a fully automated retrospective.

Optional inputs:
- Specific area to focus on ("just give me email this week")
- Specific decisions you want the review to include ("should we run the promo Friday or wait?")

## What this produces

In `/outputs/weekly-review/[week-of-date]/`:

1. **`week-summary.md`** — The 5-section retrospective:

   ### Headline
   One sentence on what defined the week. Loads voice rules from `brand-strategy.md` · direct, not corporate.
   
   ### What shipped
   - PDPs updated · ads launched · emails sent · creators reached out to · etc.
   - Pulled from Shopify analytics + Klaviyo send log + Asana (if available)
   - Tagged with the skill that produced it (read from `usage-log.md`)
   
   ### What tested
   - Active A/B tests · their day-N reading · ship/kill/keep-running call
   - Reads `experiment-log.md` for the running tests
   - Calls out tests that need a decision this week
   
   ### What won, what lost
   - Top performer of the week (creative, email, page, SKU) with the number
   - Worst performer of the week with the number
   - Both with a one-sentence "why" if the data supports it
   - Cross-references `goals-targets.md` to flag what's pacing vs not pacing
   
   ### What to do next week
   - 3-5 specific things, each tagged with the role responsible (per `team-roles.md` + `roles.*` in CONFIG)
   - Reads `promo-calendar.md` for upcoming events worth prepping for
   - Surfaces skill suggestions ("Run `customer-voice` · last run was 14 days ago and you've had 12 new reviews")

2. **`metrics-snapshot.md`** — The numbers behind the summary:
   - Shopify · revenue · orders · AOV · CVR · 7-day delta
   - Klaviyo · flow revenue · campaign revenue · list growth
   - Subscription · net adds (Shopify) · manual entry for Amazon S&S
   - Asset freshness · any `assets/*.md` not updated in >90 days (flag for review)

3. **`decisions-needed.md`** — Things waiting on the `roles.execute_tier_approver` (per CONFIG):
   - A/B tests pending ship/kill decision
   - Stage-tier work pending approval (staged Klaviyo flows · staged Shopify changes)
   - Promo calendar items needing sign-off

## How Claude runs it

1. Load `goals-targets.md` for the targets to compare against
2. Load `usage-log.md` (the running log every skill appends to) · count this week's skill invocations
3. Load `experiment-log.md` if it exists · pull active tests and their day-N stats
4. Load `promo-calendar.md` · what's coming up in the next 14 days
5. Load `assets/team-roles.md` for role responsibilities · resolve names via `roles.*` keys in CONFIG.md
6. Pull Shopify metrics for the last 7 days (revenue · orders · AOV · CVR · funnel)
7. Pull Klaviyo metrics for the last 7 days (flow rev · campaign rev · list growth)
8. Generate the headline (one sentence · direct · brand voice)
9. Section by section · synthesize what shipped from usage-log, what tested from experiment-log, what won/lost from Shopify/Klaviyo
10. Generate the 3-5 "next week" items · each tagged with role
11. Generate the metrics snapshot
12. Generate the decisions-needed list
13. Output all 3 docs · notify the team

## What this skill explicitly DOES NOT do

- Deep root-cause analysis (that's `why-sales-dropped` or `diagnose-checkout-funnel`)
- Strategic prioritization (that's `highest-leverage` or `leverage-point-assessment`)
- Specific workflow execution (the review surfaces what should run, doesn't run it)
- Replace the daily briefing (that's `briefing-generator` · runs every morning)
- Replace the monthly leverage review (that's quarterly territory)

## Permission tier

**Generate** · the review is a read-only synthesis · safe for anyone to run.

The decisions surfaced *inside* it may need execute_tier_approver attention · those route to their own skills.

## Example prompts that trigger this

- "Run the weekly review"
- "What happened this week?"
- "Friday review"
- "What should we do next week?"
- "WBR please"

## Don't use this for

- Daily check (briefing-generator runs that)
- Strategic prioritization (highest-leverage / leverage-point-assessment)
- Single-metric diagnostics (why-sales-dropped · diagnose-checkout-funnel)
- One-off campaign builds (launch-sale-promo · launch-new-bundle-or-offer)

## Notes

- Reads the `usage-log.md` which every skill appends to via the orchestrator · if skills aren't appending, the "what shipped" section is empty (validator should warn)
- The promo calendar is `assets/promo-calendar.md` (markdown table) · the team edits it directly via GitHub web UI
- Designed to run as a Friday afternoon scheduled task · output ready for Monday morning read

