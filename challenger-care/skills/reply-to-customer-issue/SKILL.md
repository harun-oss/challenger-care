---
name: reply-to-customer-issue
description: Drafts a brand-voice reply to a customer support ticket. Specific, useful, doesn't grovel. Ivey reviews and sends. MANDATORY TRIGGER: any mention of "Reply to this customer email: [paste]", "Draft a response to this support ticket", "Customer is asking about [issue] — what do I say?". Do NOT use this for: Negative reviews on Amazon / JudgeMe (use `respond-to-negative-review` — public-facing has different stakes). Reddit replies (Hayden does these in founder voice). General brand inbox triage (this is per-message).
---

> **Permission tier:** generate · **Time:** 1min · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/team-roles.md, CONFIG.md

# Reply to a customer issue

## When to use this workflow

A customer has emailed or DM'd with a question, complaint, or issue. You need a brand-voice response ready for the {{roles.marketing_coordinator}} or the {{roles.founder}} to send.

## What you need

- The customer's original message (paste it in)
- (Optional) Order number or product they're referencing
- (Optional) Tone direction — neutral, apologetic, firm

## What this produces

A drafted reply (saved to `/outputs/support/[date]-[topic].md`) including:

1. **Subject line** (if email)
2. **Greeting** — first-name basis · no "Dear valued customer"
3. **Acknowledgment** — restate the issue so they know you heard them (without parroting)
4. **The actual answer or fix** — direct, specific, no hedging
5. **What happens next** — concrete next step or expectation
6. **Sign-off** — the {{roles.marketing_coordinator}} · the {{roles.founder}} · or "The Challenger team" depending on context

## How Claude runs it

1. Read the customer's message carefully — what are they actually asking for? (Sometimes the surface complaint isn't the real ask.)
2. Load `brand-strategy.md` — voice rules. Customer support skews slightly warmer than ad copy but stays direct.
3. Load `claim-library.md` — confirm any claims in the reply are approved
4. Classify the issue:
   - **Product question** ("How long does it last?" · "Is it safe for sensitive skin?") → answer with specifics from claim-library
   - **Shipping/delivery** ("Where's my order?") → check Shopify if possible · offer concrete update
   - **Refund / return** → follow company policy · don't promise things outside the {{roles.founder}}'s authority
   - **Quality issue** ("Came damaged") → apologize once, fix it, move on
   - **Compliment** → thank them briefly, invite them to share (review, Reddit, etc.)
5. Draft the reply in 4–6 sentences. Long replies signal defensiveness.

## Voice rules for support replies

- **Direct** — no "we sincerely apologize for the inconvenience" boilerplate
- **Specific** — never "we'll look into this" without saying when and what
- **Confident** — own the brand · don't apologize for being a small team
- **No beauty-coded language** — never tell them "we're sorry your wellness journey was interrupted"
- **No fratty masculinity** — never end with "stay sharp, bro"
- **No over-promising** — don't offer refunds or replacements you can't deliver

## On-brand vs off-brand examples

**On-brand reply to "my order hasn't shipped":**
> *"Hey Mike — your order shipped this morning · tracking number 1Z9...XYZ · should land Friday. Ping us if it doesn't. — the {{roles.marketing_coordinator}}, Challenger"*

**Off-brand (rewrite):**
> *"Dear valued customer, we sincerely apologize for the delay in your wellness routine. We are working diligently to ensure your products arrive at the earliest possible moment to support your self-care journey."*

## Permission tier

**Generate** — the {{roles.email_reviewer}} reviews and sends. the {{roles.execute_tier_approver}} reviews anything that:
- Mentions refunds or returns outside standard policy
- Comes from a reviewer with a public following
- Touches a quality / safety issue
- Mentions an allergic reaction (per `claim-library.md` — escalate immediately)

## Example prompts that trigger this

- "Reply to this customer email: [paste]"
- "Draft a response to this support ticket"
- "Customer is asking about [issue] — what do I say?"

## Don't use this for

- Negative reviews on Amazon / JudgeMe (use `respond-to-negative-review` — public-facing has different stakes)
- Reddit replies (the {{roles.reddit_voice_owner}} handles these in founder voice)
- General brand inbox triage (this is per-message)

## Special escalation rules

Per `claim-library.md` and `team-roles.md`:

1. **Allergic reaction mention** → escalate to the {{roles.execute_tier_approver}} immediately. Do NOT auto-reply.
2. **Legal threat / dispute language** → escalate to the {{roles.execute_tier_approver}}.
3. **Press / media inquiry** → escalate to the {{roles.execute_tier_approver}}.
4. **Influencer / large-follower-account complaint** → escalate to the {{roles.execute_tier_approver}}.
5. **Refund request outside standard policy** → flag to the {{roles.execute_tier_approver}} before sending.

For everything else: the {{roles.marketing_coordinator}} can run independently with this workflow's drafts.
