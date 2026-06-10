---
name: customer-voice
description: Pulls last 30 days of reviews + survey responses, clusters into themes, surfaces new patterns and ad-ready quotes. MANDATORY TRIGGER: any mention of "What are customers saying lately?", "Run customer voice — anything new emerging?", "Show me reviews about the 3-pack", "Cluster recent feedback by theme". Do NOT use this for: Strategic positioning decisions (use `highest-leverage`). Single-customer support replies (use `reply-to-customer-issue`). A/B test design (use `test-price-claim`).
---

> **Permission tier:** generate · **Time:** 2min · **Tools/context:** assets/customer-archetypes.md, assets/voc/voc-corpus.csv, assets/voc/voc-analysis-report.md, CONFIG.md

# What are customers saying?

## When to use this workflow

You want a current read on customer sentiment — what's positive, what's friction, what new themes are emerging. Useful before any creative work, PDP refresh, or product decision.

## What you need

Nothing required — Claude pulls the latest review data from Drive.

Optional inputs:
- Specific theme to dig into ("complaints about scent" · "feedback on the 3-pack")
- Time window (default last 30 days)
- Source filter (Amazon · JudgeMe · Reddit · survey)

## What this produces

1. **Top 5 themes** in the period · positive + friction · with frequency
2. **Emerging themes** — patterns not previously dominant (e.g., "feels heavy in humidity" appearing across multiple reviews)
3. **Quote library snippets** — 10–15 verbatim quotes tagged by theme + ad-readiness
4. **Sentiment trend** — improving, stable, declining
5. **Recommended actions** — which themes deserve a workflow response (PDP update? new claim? product reformulation?)

Lands in `Drive/voc-reports/[date].md`. Quotes also append to `../../assets/quote-library.md`.

## How Claude runs it

1. Read latest reviews CSV from `Drive/exports/reviews-combined.csv`
2. Filter by date range and source
3. Theme-code each review (positive · friction · new pattern)
4. Sentiment-score
5. Rank themes by frequency
6. Compare against trailing 90-day baseline to surface emerging patterns
7. Pull verbatim quotes per theme — score for ad-readiness (specificity, emotion, novelty)
8. Compile report

## Permission tier

**Generate** — analysis only. The quote library it produces is reused by every customer-voice-driven workflow (ad creative, PDP refresh, email copy).

## Example prompts that trigger this

- "What are customers saying lately?"
- "Run customer voice — anything new emerging?"
- "Show me reviews about the 3-pack"
- "Cluster recent feedback by theme"

## Note on data dependency

**This workflow's output quality depends on the underlying review corpus.** Currently it reads from JudgeMe-only data (724 reviews). Once the {{roles.founder}} delivers the 500 Amazon reviews CSV, the corpus jumps to 1,224 and the analysis gets much more reliable. Until then, results are partial — the workflow runs, just at lower confidence.

## Don't use this for

- Strategic positioning decisions (use `highest-leverage`)
- Single-customer support replies (use `reply-to-customer-issue`)
- A/B test design (use `test-price-claim`)
