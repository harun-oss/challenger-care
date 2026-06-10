---
name: reddit-founder-post
description: 'Drafts a single founder-voice reply to a Reddit thread · for r/malegrooming, r/SkincareAddiction, r/wicked_edge, and adjacent subs. Single-post motion, not a batch. Reads like a person, not a brand. MANDATORY TRIGGER: any mention of "draft a Reddit reply", "respond to this Reddit thread", "founder voice on Reddit", "this thread asks about pomade · what should I say", "Reddit founder post". Do NOT use this for: Weekly batch organic content (use `create-this-weeks-content`). Paid Reddit ads (use `reddit-ads`). Customer support replies (use `reply-to-customer-issue`).'
---

> **Permission tier:** generate · **Time:** 1min · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/voc/quote-library.md, assets/customer-archetypes.md, assets/team-roles.md, CONFIG.md

# Draft a single Reddit reply (founder voice)

## When to use this workflow

The founder voice on Reddit is one of the brand's strongest unpaid acquisition channels. The motion is high-frequency · 2-5 replies per week across r/malegrooming, r/SkincareAddiction, r/wicked_edge, r/Hair, r/AskMen, and product-specific threads. The existing `create-this-weeks-content` skill is batch-shaped (3-5 posts at once) · this skill handles the single high-leverage reply that comes from spotting a relevant thread in the moment.

## What you need

- (Required) The Reddit thread URL or pasted text
- (Optional) Specific angle you want to take · e.g., "share the routine", "answer the pomade question", "be helpful without selling"
- (Optional) Whether to mention Challenger explicitly · default: no (the rule is help first, mention only when directly asked)

## What this produces

A single drafted Reddit reply, output to `/outputs/reddit/[date]-[thread-slug].md`:

1. **The reply itself** · ready to paste · in founder voice
2. **Notes** · why this angle, what to do if downvoted, follow-up moves
3. **Disclosure check** · if the reply mentions Challenger, does it need an `[I make X]` disclosure per Reddit's rules?

## How Claude runs it

1. Read the thread context · what's the actual question · what's the sentiment · what's the OP asking for
2. Load `brand-strategy.md` · the {{roles.founder}} voice rules section (which is *different* from brand voice · more personal, opinion-led, willing to recommend competitors when honest)
3. Load `customer-archetypes.md` · most Reddit replies hit the Reddit Discoverer archetype (community-driven, founder-voice receptive)
4. Load `claim-library.md` · the same banned-claim rules apply (no "cures", no medical claims) but Reddit allows more direct competitor mentions than ad copy
5. Load `voc/quote-library.md` · if a real customer has already said something relevant, riff on it rather than inventing
6. Draft the reply with these constraints:
   - Helpful before promotional
   - Specific, not generic ("I've found X works because Y" not "moisturizing is important")
   - Opinion-led, not balanced ("I think X" not "some say X and others say Y")
   - Names competitors when honest ("Hanz De Fuko's matte clay works but feels stiffer" beats vague hand-waving)
   - 100-300 words · longer reads as a sales pitch
   - No marketing language · zero
   - Mentions Challenger only if directly asked or if it's the obviously correct answer to the question
   - If mentioning Challenger, includes `[I make Challenger Care · take with grain of salt]` disclosure
7. Generate the notes block · why this angle, alternative angles, what to do if it doesn't land
8. Generate the disclosure check (yes/no + why)

## Voice rules · founder mode (loaded from brand-strategy.md)

Different from brand voice. Read the relevant section in `brand-strategy.md` for the full rules. Quick reminder:

- First-person · "I", "my", "I've found", "in my experience"
- Opinion-led · "I think", "I've come to believe", not "research shows" or "experts say"
- Will recommend competitors when honest about their strengths
- Specific product comparisons OK · "I prefer X because Y" beats "everything's a personal preference"
- The `$5 jar drop` pattern is a proven Reddit motion · surface it when natural (e.g., "happy to ship anyone curious a sample for $5")
- Never copy-paste from marketing materials · if a phrase exists in a Klaviyo email, don't put it on Reddit

## What gets cut from a Reddit reply

Things that flag as inauthentic and tank the post:

- "We at Challenger Care believe..." · founder voice, not corporate
- "Our research shows..." · whose research, posted by whom
- Marketing taglines ("Show up sharper.") · works on Instagram, fails on Reddit
- Excessive enthusiasm ("Absolutely love this question!")
- Hedge words that suggest legal review ("may help with", "could potentially")
- More than one link in the reply
- More than 300 words

## Permission tier

**Generate** · drafts only · the `roles.reddit_voice_owner` (per CONFIG.md · currently the {{roles.founder}}) personally posts.

This skill never auto-posts. Reddit's API + founder voice both require the human in the loop.

## Example prompts that trigger this

- "Draft a Reddit reply for [thread URL]"
- "Someone in r/malegrooming asked about hair pomades · what should I post?"
- "This Reddit thread is about acne · founder voice reply please"
- "What would the {{roles.founder}} post in this thread?" (where the {{roles.founder}} = `roles.reddit_voice_owner`)

## Don't use this for

- Weekly batch of organic content (use `create-this-weeks-content`)
- Paid Reddit ads (use `reddit-ads`)
- Customer DMs from Reddit (use `reply-to-customer-issue`)
- Reddit posts in *brand voice* (Challenger Care commenting as itself · rare · use `create-this-weeks-content`)

## Notes

- High-frequency · this skill runs 2-5×/week, much higher than most skills
- The `$5 jar drop` mechanic is documented in `brand-strategy.md` · surface it when natural
- Reading the OP's full post + the top 3 comments is mandatory before drafting · context matters
- If the thread is contentious or has a hostile sentiment, the right answer is often "don't engage" · flag this to the {{roles.founder}} rather than drafting

