---
name: highest-leverage
description: Grades the business across 7 leverage points (Market, Product, Money, Position, Reach, Convert, Expand) and recommends focus. MANDATORY TRIGGER: any mention of "Where should I focus this month?", "Run a leverage point assessment", "What's the highest-leverage thing I could be doing?", "Grade the business". Do NOT use this for: Tactical daily decisions (use the dashboard's "On your plate" alerts). Specific workflow recommendations (this surfaces priorities, then point to specific workflows). Forecasting or modeling (use `model-unit-economics`).
---

> **Permission tier:** generate · **Time:** 6min · **Tools/context:** mcp:shopify, assets/unit-economics.md, assets/goals-targets.md, assets/competitor-map.md

# Where's my highest leverage this month?

## When to use this workflow

Start of month, start of quarter, or when feeling overwhelmed by competing priorities. Answers: where should I put my finite time and budget to move the needle most?

## What you need

Nothing required — Claude pulls current state from Shopify + knowledge files.

Optional inputs:
- Specific constraint to factor in (cash flow tight · Hayden capacity tight · Q3 push)
- Time horizon (this month · this quarter · next 90 days)

## What this produces

A **Leverage Point Assessment** scoring Challenger Care across 7 dimensions, each on an A–F scale:

1. **Market** — Are we in a growing space? Right segment?
2. **Product** — Does the product hold up? Repeat behavior? Reviews?
3. **Money** — Unit economics, margins, cash position
4. **Position** — Brand clarity, differentiation
5. **Reach** — Traffic sources, channel mix
6. **Convert** — Funnel, AOV, CVR
7. **Expand** — Retention, subscription, LTV

For each: grade · evidence · top 1–2 actions to raise the grade.

Then a **prioritization recommendation** — which 2 leverage points to focus on this month, and which 5 to maintain or defer.

Lands in `Drive/strategy/[date]-leverage-assessment.md`.

## How Claude runs it

1. Pull current performance metrics from Shopify (revenue, AOV, CVR, returning rate, sell-through, etc.)
2. Reference `../../assets/unit-economics.md` for the financial spine
3. Reference `../../assets/goals-targets.md` for the goals to score against
4. Reference `../../assets/competitor-map.md` for market + position grading
5. Use the leverage-points framework (from GrowthHit `leverage-point-assessment` skill)
6. Score each of the 7 dimensions
7. Surface evidence per grade
8. Recommend the 2 highest-leverage focuses for the period
9. Identify what to defer / maintain

## Permission tier

**Generate** — strategic analysis only. Output informs the next 30–90 days of work but doesn't change anything live.

## Example prompts that trigger this

- "Where should I focus this month?"
- "Run a leverage point assessment"
- "What's the highest-leverage thing I could be doing?"
- "Grade the business"

## Don't use this for

- Tactical daily decisions (use the dashboard's "On your plate" alerts)
- Specific workflow recommendations (this surfaces priorities, then point to specific workflows)
- Forecasting or modeling (use `model-unit-economics`)
