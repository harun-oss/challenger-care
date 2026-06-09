---
name: fix-broken-flow
description: Pauses an underperforming email or ad, audits why, builds the replacement, stages for review. MANDATORY TRIGGER: any mention of "Welcome flow email 2 is underperforming, fix it", "The post-purchase flow CTR dropped — rebuild it", "Pause the browse abandonment flow until we have a replacement". Do NOT use this for: New flows (use `build-next-email-flow`). Single campaign sends (use `launch-sale-promo`). Flow performance reporting (handled by the briefing / anomaly detector).
---

> **Permission tier:** stage · **Time:** 5min · **Tools/context:** mcp:klaviyo (when connected), skills/lib/klaviyo-audit, skills/lib/email-copywriting, knowledge/claim-library.md

# Pause and rebuild a broken flow

## When to use this workflow

A Klaviyo flow (welcome email 2, abandoned cart sequence, post-purchase nudge) is underperforming benchmarks — CTR dropped, revenue per send declined, open rate fell. You want to pause, diagnose, replace.

## What you need

- The flow + step that's underperforming (e.g., "welcome flow email 2")
- (Optional) Suspected cause ("I think the CTA copy is dated")
- (Optional) Performance target ("I want CTR back above 8%")

## What this produces

1. **Audit summary** — what the current flow is doing, where it's failing
2. **Diagnosis** — most likely 1–2 reasons for the drop (copy, CTA, send time, segment, deliverability)
3. **Pause action** — staged in Klaviyo, awaits Hayden's approval before going live
4. **3 rewrite variants** — each with subject line, preview, body, CTA in brand voice
5. **A/B test plan** — how to run the 3 variants against the underperformer
6. **Decision rule** — when to ship the winner

Lands in `Drive/flow-fixes/[flow-name]/`.

## How Claude runs it

1. Pull the flow's last 30 days of performance from Klaviyo (CTR, open rate, revenue per send)
2. Compare against Klaviyo industry benchmarks AND past performance of this same flow
3. Identify which step is underperforming
4. Audit the copy against `../../assets/claim-library.md` and brand voice rules
5. Stage a pause in Klaviyo (awaits approval)
6. Draft 3 rewrite variants
7. Build the A/B test plan
8. Define the success metric + decision rule

## Permission tier

**Stage** — pause is staged but not live until Hayden approves. Rewrites are drafts. The A/B implementation requires explicit "ship" from Hayden.

## Example prompts that trigger this

- "Welcome flow email 2 is underperforming, fix it"
- "The post-purchase flow CTR dropped — rebuild it"
- "Pause the browse abandonment flow until we have a replacement"

## Don't use this for

- New flows (use `build-next-email-flow`)
- Single campaign sends (use `launch-sale-promo`)
- Flow performance reporting (handled by the briefing / anomaly detector)
