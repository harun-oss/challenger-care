---
name: launch-sale-promo
description: 'Builds a complete promo campaign from a single ask — banner copy, email send, SMS, social posts, Klaviyo segment + start/end logic. MANDATORY TRIGGER: any mention of "Run a 20% off promo on the 3-pack from Friday to Sunday", "BFCM campaign — what should we run?", "Free shipping weekend, let''s go". Do NOT use this for: New product launches (use `launch-new-product`). Bundle launches (use `launch-new-bundle`). Ongoing email flows (use `build-next-email-flow`).'
---

> **Permission tier:** stage · **Time:** 3min · **Tools/context:** assets/claim-library.md, assets/unit-economics.md, # Launch a sale or promo, CONFIG.md, assets/brand-strategy.md

## When to use this workflow

You're running a discount, BFCM-style campaign, flash sale, or limited-time offer and need every asset built consistently.

## What you need

- The offer (e.g., "20% off the 3-pack", "free shipping over $40")
- Start + end dates
- Target audience (all customers, lapsed, subscribers, etc.)
- Reason for the offer (optional but useful for copy framing)

## What this produces

1. **Site banner** — 1 line, 2 variants
2. **Email send** — subject + preview + body + CTA in brand voice
3. **SMS message** — 160-character version
4. **2 social posts** — Instagram + Reddit-appropriate (founder voice for Reddit)
5. **Klaviyo segment definition** — who gets the email
6. **Start/end logic** — turn-on date, turn-off date, exclusion list
7. **Discount code** suggestion (the {{roles.founder}} creates in Shopify)

All drafts land in `Drive/promos/[campaign-name]/`.

## How Claude runs it

1. Validate offer math against `../../assets/unit-economics.md` — flag if discount kills margin below 50%
2. Pull brand voice rules from `../../assets/claim-library.md`
3. Generate site banner copy (2 variants)
4. Draft email (subject lines × 3, preview, body, CTA)
5. Draft SMS (160 char hard limit)
6. Draft social posts (IG caption + Reddit post in founder voice)
7. Define Klaviyo segment criteria
8. Compile into one campaign brief

## Permission tier

**Stage** — All drafts go into Klaviyo / Shopify but don't publish. the {{roles.execute_tier_approver}} approves before send.

## Example prompts that trigger this

- "Run a 20% off promo on the 3-pack from Friday to Sunday"
- "BFCM campaign — what should we run?"
- "Free shipping weekend, let's go"

## Don't use this for

- New product launches (use `launch-new-product`)
- Bundle launches (use `launch-new-bundle`)
- Ongoing email flows (use `build-next-email-flow`)
