---
name: creator-outreach
description: 'Builds a prospect list of creators / influencers across TikTok + Instagram, drafts personalized outreach for each. MANDATORY TRIGGER: any mention of "Find 10 micro-influencers in men''s grooming", "I want to do a gifting campaign for the 3-pack - who should we contact?", "Find creators on TikTok who post barbershop content". Do NOT use this for: Paid Meta influencer ads (that''s a different workflow once Meta is reactivated). Customer-as-creator UGC programs (use `ugc-creator-kit` for that). Press outreach to publications (different audience and approach).'
---

> **Permission tier:** generate · **Time:** 4min · **Tools/context:** assets/claim-library.md, assets/team-roles.md, CONFIG.md

# Reach out to creators or influencers

## When to use this workflow

You want creator partnerships for content, gifting, affiliate, or paid sponsorships. Either targeted (specific creator names) or discovery-based (find creators in our niche).

## What you need

- The goal of outreach (gifting · affiliate · paid · UGC)
- The vibe / niche you want (men's grooming · barbershop culture · fitness · Reddit-credible · TikTok-native)
- Budget range (free product, paid flat fee, % affiliate)
- Volume — how many creators do you want?

## What this produces

1. **Prospect list** — 10–25 creators with:
   - Handle + platform
   - Follower count + engagement estimate
   - Niche fit notes
   - Why they're a fit for Challenger
2. **Outreach drafts** — one personalized message per creator
3. **Deal structure** — what we're offering each tier (nano · micro · mid)
4. **Tracking plan** — UTMs, codes, attribution

Lands in `Drive/outreach/[campaign-name]/`.

## How Claude runs it

1. Use the influencer-prospector skill to crawl TikTok + Instagram + creator directories
2. Filter for niche fit (men's grooming · clean ingredients · everyman vibe)
3. Filter out obvious mismatches (bro-energy, fragrance-heavy, sponsored-to-death)
4. For each prospect, draft personalized outreach (reference their specific content)
5. Use brand-voice rules from `../../assets/claim-library.md`
6. Suggest the deal tier per creator (gifting for nano, paid for higher reach)

## Permission tier

**Generate** — all drafts, no sends. the {{roles.founder}} or the {{roles.email_reviewer}} reviews and sends manually (or via outreach tool).

## Example prompts that trigger this

- "Find 10 micro-influencers in men's grooming"
- "I want to do a gifting campaign for the 3-pack — who should we contact?"
- "Find creators on TikTok who post barbershop content"

## Don't use this for

- Paid Meta influencer ads (that's a different workflow once Meta is reactivated)
- Customer-as-creator UGC programs (use `ugc-creator-kit` for that)
- Press outreach to publications (different audience and approach)
