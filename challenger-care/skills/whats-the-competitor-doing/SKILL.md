---
name: whats-the-competitor-doing
description: Scans Based, Hanz De Fuko, Paul Mitchell — pulls new ads, pricing changes, recent launches, Reddit sentiment. Flags what to borrow and what to beat. MANDATORY TRIGGER: any mention of "What's the competitor doing?", "Run a competitor scan", "Has Based launched anything new?", "Check Hanz De Fuko's current PDPs". Do NOT use this for: Internal product audits (use `refresh-underperforming-pdp` or `heuristic-analysis`). Customer-voice analysis (use `customer-voice` / VOC workflow). Direct ad copy (use `create-this-weeks-ad-creative` — competitor scan is an input to it).
---

> **Permission tier:** generate · **Time:** 3min · **Tools/context:** knowledge/competitor-map.md, knowledge/brand-strategy.md, browser tool (Claude in Chrome) when available, web fetch for public sources (Meta Ad Library, brand sites)

# What's the competitor doing?

## When to use this workflow

Weekly competitor scan OR ad-hoc deep dive when you need to know what one of the named competitors is up to before a launch / repositioning / paid push.

## What you need

- (Optional) Which competitor(s) to focus on — Based · Hanz De Fuko · Paul Mitchell · or "all three"
- (Optional) What you're trying to learn — pricing · creative · positioning · new launches

Default: scan all three competitors against the baseline in `competitor-map.md`.

## What this produces

In `/outputs/competitor/[scan-date]/`:

1. **`scan-summary.md`** — Executive summary:
   - What changed since last scan
   - The 3 most strategically relevant findings
   - Recommended Challenger responses (if any)
2. **`per-brand-update.md`** — Per competitor:
   - PDP changes (pricing, copy, hero claims)
   - New SKU launches (if any)
   - Current ad creative (from Meta Ad Library)
   - Recent Reddit / community mentions + sentiment
   - Status: Active / Quiet / Aggressive
3. **`positioning-implications.md`** — How findings map to Challenger's position:
   - Gaps competitors are now filling
   - Gaps still open for Challenger
   - Things worth borrowing
   - Things worth beating

## How Claude runs it

1. Load `competitor-map.md` — current baseline state per competitor
2. Load `brand-strategy.md` — for assessing how their positioning compares to ours
3. For each competitor:
   - Pull their homepage + top PDPs via Chrome browser tool (when available) or web fetch
   - Pull active ads from Meta Ad Library (`https://www.facebook.com/ads/library/?search_type=page&q=[brandname]`)
   - Search Reddit for last-30-day mentions (r/malegrooming, r/wicked_edge, r/SkincareAddiction)
   - Compare against baseline in `competitor-map.md`
4. Diff each finding from baseline · flag changes
5. Cross-reference with Hayden's stated read in `competitor-map.md`:
   - Based — Gen Z TikTok hype · weak long-term
   - Hanz De Fuko — premium pomade · not innovating · Challenger Clean is better
   - Paul Mitchell — mass-prestige · coasting since 1987
6. Recommend Challenger responses where relevant:
   - "Based launched a clay pomade at $19 → consider response: highlight Challenger Matte for half the price OR position against clay-formula heaviness"
   - "Hanz De Fuko quiet again — opportunity for direct comparison content"
   - "Paul Mitchell launched seasonal campaign — likely no threat, Challenger's segment is different"

## Permission tier

**Generate** — all research, no live changes. Output informs strategic decisions (PDP refresh, creative shifts, pricing tests) but doesn't trigger them.

## Example prompts that trigger this

- "What's the competitor doing?"
- "Run a competitor scan"
- "Has Based launched anything new?"
- "Check Hanz De Fuko's current PDPs"

## Don't use this for

- Internal product audits (use `refresh-underperforming-pdp` or `heuristic-analysis`)
- Customer-voice analysis (use `customer-voice` / VOC workflow)
- Direct ad copy (use `create-this-weeks-ad-creative` — competitor scan is an input to it)

## Scheduled use

This workflow runs as a **scheduled task every Sunday at 9:00 AM PT**. Output writes to `/outputs/competitor/[scan-date]/scan-summary.md` and feeds the dashboard's Competitor Watch panel.

Manual runs are for ad-hoc deeper dives.

## Reliability notes

- **Meta Ad Library is publicly fetchable** — works reliably
- **Competitor PDPs vary** — some block scraping (Cloudflare, etc.). Chrome browser tool is more reliable than raw web fetch.
- **Reddit mentions** — public, scrapable, sentiment analysis straightforward
- **TikTok / Discord activity** — harder to scrape · note these qualitatively where possible

When a fetch fails, flag it in the output rather than silently skipping. Honesty about data gaps maintains trust in the report.

## Strategic principle from the brand book

We don't engage competitors in formal copy (no naming names in ads). But internally, we know exactly what they're doing. The competitive insight informs our positioning · the formal communication stays on the Challenger story.
