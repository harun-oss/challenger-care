---
name: create-this-weeks-content
description: Generates this week's organic content batch — TikTok scripts, Reddit-ready posts (founder voice), Instagram captions — aligned to current themes from VOC + dashboard signals. MANDATORY TRIGGER: any mention of "Create this week's content", "Generate the content batch for next week", "I need a Reddit post for r/malegrooming about [topic]", "TikTok scripts for the humidity push". Do NOT use this for: Paid ad creative (use `create-this-weeks-ad-creative`). Email content (use `build-next-email-flow` or `launch-sale-promo`). One-off founder posts where context is highly specific (just write directly with Hayden).
---

> **Permission tier:** generate · **Time:** 3min · **Tools/context:** knowledge/brand-strategy.md, knowledge/customer-archetypes.md, voc/quote-library.md, voc/voc-analysis-report.md

# Create this week's content

## When to use this workflow

Weekly cadence for owned channels — TikTok (via Implicit), Reddit (founder voice), Instagram organic. Generates a batch in one pass so the team can publish through the week.

## What you need

- (Optional) This week's theme or angle (e.g., 3-pack push · pomade acne · humidity)
- (Optional) Specific products to feature
- (Optional) Channel emphasis (mostly Reddit · mostly TikTok · etc.)

Default: balanced batch across all channels · pick the strongest VOC theme of the week.

## What this produces

All in `/outputs/content/[week-of-date]/`:

1. **`tiktok-scripts.md`** — 3–5 short scripts:
   - Hook (3 seconds, scroll-stopper)
   - Body (20–30 seconds, the substance)
   - CTA (3 seconds, *"Accept the challenge"* or product-specific)
   - Suggested visual direction for the creator
2. **`reddit-posts.md`** — 2–3 founder-voice posts for r/malegrooming + related subs:
   - Title
   - Body (Hayden voice · first-person · opinion-led · NOT brand voice)
   - Suggested timing + sub
3. **`instagram-captions.md`** — 4–5 captions:
   - Short caption (Stories, single-image posts)
   - Longer caption (carousels, education content)
4. **`content-calendar.md`** — Suggested posting cadence + which channel for which piece

## How Claude runs it

1. Load `brand-strategy.md` — for IG + TikTok, use brand voice. For Reddit, use founder voice (different rules).
2. Load `customer-archetypes.md` — TikTok skews Reddit Discoverer + The Switcher · Reddit specifically skews the Reddit Discoverer + Sensitive Buyer · IG skews mixed
3. Load `../../assets/voc/quote-library.md` — find the strongest 4–6 quotes for this week's theme
4. Load `../../assets/voc/voc-analysis-report.md` — check the emerging themes section for what's currently trending in customer voice
5. Generate content per channel:
   - **TikTok:** dare-flavored hooks, scroll-stoppers, performance results shown in real settings
   - **Reddit:** founder voice (NEVER brand voice) — useful, peer-to-peer, contributes to the community before pitching
   - **Instagram:** mix of preparation (brand pillar) + product education
6. Tie each piece to a specific archetype so the team knows who it's for

## Voice rules per channel

### TikTok (brand voice)
- Direct, confident, peer-to-peer
- Hook first · pillar second · CTA third
- The challenge frame is most powerful here (per brand book)

### Reddit (founder voice, NOT brand voice)
- First-person Hayden voice
- Opinion-led: *"I think..."*, *"In my experience..."*
- Helpful before promotional
- Specific product comparisons OK (Hayden's brand is the brand book context, but on Reddit he can be more direct about competitors)
- Never copy-paste marketing language
- $5 jar drops are a proven pattern — surface this when natural

### Instagram (brand voice)
- Mix of pillars across the week
- Carousels work for product education (how-to + result + proof)
- Captions: short and dare-flavored OR medium-length and result-oriented

## Permission tier

**Generate** — all drafts. Hayden runs the Reddit posts personally (founder voice requires founder posting). Ivey can publish IG. Implicit handles TikTok.

## Example prompts that trigger this

- "Create this week's content"
- "Generate the content batch for next week"
- "I need a Reddit post for r/malegrooming about [topic]"
- "TikTok scripts for the humidity push"

## Don't use this for

- Paid ad creative (use `create-this-weeks-ad-creative`)
- Email content (use `build-next-email-flow` or `launch-sale-promo`)
- One-off founder posts where context is highly specific (just write directly with Hayden)

## Notes

- **Reddit voice is the trickiest.** It must NOT sound like marketing. If a Reddit post could be cut-and-pasted into an IG caption, rewrite it.
- **Hayden's $5 jar drop pattern** is a proven Reddit play — surface it as an option when natural
- **The Pomade Acne hook** plays beautifully on Reddit — high-intent, real conversation territory
- **Implicit handles TikTok execution**, but the scripts feed their content engine
