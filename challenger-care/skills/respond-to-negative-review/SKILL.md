---
name: respond-to-negative-review
description: Drafts the right response to a negative review on Amazon or JudgeMe. Protects the 84% 5-star moat. Addresses the issue, offers a path forward, doesn't grovel. MANDATORY TRIGGER: any mention of "Negative review just came in on Amazon: [paste]", "1-star JudgeMe review · draft a response", "Reply to this 3-star: [paste]". Do NOT use this for: Positive reviews (different flow — usually a brief thank-you, not a response). Customer support emails / DMs (use `reply-to-customer-issue` — private channel, different stakes). Reddit threads (Hayden in founder voice).
---

> **Permission tier:** stage · **Time:** 1min · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/team-roles.md

# Respond to a negative review

## When to use this workflow

A 3-star-or-below review just landed on Amazon or JudgeMe. You need a response that's public-facing, brand-aligned, and protects rating equity.

## What you need

- The review text (paste it in)
- Star rating
- Platform (Amazon or JudgeMe)
- (Optional) Product the review is on
- (Optional) Whether the reviewer is a verified buyer

## What this produces

A staged response (saved to `/outputs/reviews/[date]-[platform]-[product].md`) including:

1. **Acknowledgment** — show you read the review (not parrot it)
2. **The actual response** — address the specific issue
3. **The offer** — concrete next step or solution
4. **Sign-off** — appropriate to the platform

## How Claude runs it

1. Read the negative review carefully
2. Classify the type:
   - **Quality / product defect** ("Came damaged" · "Didn't hold")
   - **Expectation mismatch** ("Expected more hold" · "Stronger scent than I thought")
   - **Shipping / fulfillment** ("Took forever to arrive" · "Wrong size")
   - **Pricing** ("Overpriced" · "Bottle smaller than expected")
   - **Allergic reaction / sensitivity** ⚠️ **escalate immediately**
   - **Trolling / fake review** → flag to the {{roles.execute_tier_approver}}, don't engage publicly
3. Load `brand-strategy.md` — voice rules. Public responses skew slightly warmer but stay direct.
4. Load `claim-library.md` — confirm no banned language slips into the response · don't make medical claims even when addressing a sensitivity report
5. Draft the response per the type:
   - **Quality / defect:** Acknowledge specifically. Offer replacement or refund. Provide a direct contact (the {{roles.marketing_coordinator}} or support email).
   - **Expectation mismatch:** Don't argue. Acknowledge the gap. Educate gently. Sometimes offer to swap to a different SKU that better fits their need.
   - **Shipping:** Apologize once for the experience. Offer to make it right.
   - **Pricing:** Don't apologize for the price. Reframe the value (110-day jar math, ingredient quality). Thank them for trying.
   - **Allergic reaction:** Escalate. Do NOT publish a response without the {{roles.founder}}'s review.

## Voice rules for public review responses

- **Acknowledge specifically** — don't use "we hear you" boilerplate
- **Own the fix** — never "we'll forward this to our team"
- **Direct but not defensive** — never argue with the reviewer
- **No beauty language** — don't say "your wellness experience"
- **No "we're sorry to hear that" repeatedly** — once is enough
- **End with something forward-looking** — a contact, an offer, an invitation back

## On-brand vs off-brand

**On-brand response to "Pomade didn't hold":**
> *"Sorry to hear it didn't hold for you, Tom. Our Matte gives medium-firm hold and works best applied to damp hair · if you'd like a hold step up, our Strong variant might fit better. Email me at info@challengercare.com and I'll swap it out. — the {{roles.marketing_coordinator}}"*

**Off-brand (rewrite):**
> *"Dear valued customer, we sincerely apologize that your Challenger experience did not meet your expectations. Your feedback is invaluable and we will share it with our team. We hope you'll give us another opportunity to support your daily self-care routine."*

## Permission tier

**Stage** — Response is drafted but stays unpublished until the {{roles.execute_tier_approver}} reviews. Public-facing reviews are too high-stakes for auto-posting.

**Exceptions requiring the {{roles.execute_tier_approver}}'s direct write:**
- Allergic reaction or safety mention
- Legal threat language
- Reviewer is an influencer / has a public following
- Review is going viral or has unusual engagement
- Review accuses Challenger of a specific quality / ingredient claim that would need legal review

## Example prompts that trigger this

- "Negative review just came in on Amazon: [paste]"
- "1-star JudgeMe review · draft a response"
- "Reply to this 3-star: [paste]"

## Don't use this for

- Positive reviews (different flow — usually a brief thank-you, not a response)
- Customer support emails / DMs (use `reply-to-customer-issue` — private channel, different stakes)
- Reddit threads (the {{roles.reddit_voice_owner}} in founder voice)

## Protecting the rating equity

Challenger has 84% 5-star on Amazon · 92.5% positive on JudgeMe · this is a real moat. Every negative review response should:
- Reduce the chance the reviewer escalates further (refund chargeback, social complaint)
- Demonstrate to other potential buyers reading the review that Challenger handles issues well
- Not invite more negative reviews by sounding defensive or robotic

A good response to a 3-star review often results in a rating bump after the issue is resolved. Always offer a concrete way to make it right.
