---
name: email-copywriting
description: Writes, critiques, and optimises email copy for every type of email · welcome flows, abandoned cart, nurture sequences, re-engagement, promotional campaigns, transactional. Subject lines, preview text, body, CTAs. MANDATORY TRIGGER: any mention of "write email copy", "write a subject line", "preview text", "email CTA", "write this email", "improve this email", "abandoned cart copy", "welcome email copy", "winback email", "promotional email copy". Do NOT use for: ESP setup or flow configuration (use `klaviyo-flows` or `klaviyo-campaigns`). Email strategy (use `email-strategy`).
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/team-roles.md, CONFIG.md


# Email Copywriting

## What this skill does

Writes, critiques, and optimises email copy — subject lines, preview text, body, and CTA — for any email type and any ESP. The principles here apply whether Challenger is on Klaviyo, Klaviyo, ActiveCampaign, or anything else.

Good email copy has one job: advance the relationship. In an eCommerce welcome email, that means delivering the offer and establishing the brand voice. In an abandoned cart email, it means removing the objection that stopped the purchase. In a B2B nurture email, it means building enough trust that the contact moves one step closer to a conversation. Copy that doesn't serve that job is wasted.

Use this skill when:
- Writing flow emails (welcome, cart, winback, post-purchase)
- Writing campaign copy (promotional, newsletter, product launch)
- Critiquing or rewriting existing email copy
- Producing full sequences (3–7 emails with consistent arc)
- Setting subject line strategy and A/B test plans

---

## Reference Files

This skill uses reference materials. When running inside an orchestrated workflow, the orchestrator will locate and load these automatically via Glob.

- `assets/brand-strategy.md` — Subject line formulas by email type, worked body copy templates (welcome, cart, winback, nurture, B2B), A/B testing framework, and copy critique checklist. Read during Phases 2–7.

---

## Phase 1 — Context

Ask one question at a time:

1. **What type of email?** — welcome, abandoned cart, browse abandonment, post-purchase, winback, nurture, promotional campaign, re-engagement, or transactional?
2. **Brand voice and audience** — who is the sender, who is the recipient, and what is the brand tone? (Formal/conversational/playful/authoritative?)
3. **What is the goal of this specific email?** — open the relationship, recover a purchase, drive a click, book a call, get an upgrade?
4. **Any existing copy to critique or improve?** — if yes, get it before writing
5. **Platform and format** — HTML branded template or plain text? From the brand or from a named person?

---

## Phase 2 — Subject Lines

The subject line is the email. If it fails, nothing else matters. 43% of people decide to open based on subject line alone.

### Length

| Goal | Target length | Why |
|------|--------------|-----|
| Maximum open rate | 61–70 characters | Highest average open rate (43.38%) |
| Maximum click rate | 41–50 characters | Highest CTR per send |
| Mobile preview (no cutoff) | Under 50 characters | Most mobile clients show ~46 chars |

**Rule:** Write the 61-70 char version first, then create a shorter variant for A/B testing.

### High-performing formulas

**Curiosity gap:**
`You forgot something → [Cart recovery]`
`The mistake most [audience] make → [Nurture]`
`We almost didn't send this → [Re-engagement]`

**Specificity (numbers beat vague):**
`Your cart total: $127.00` outperforms `Don't forget your cart`
`3 customers asked us the same question this week` outperforms `Important update`

**Direct personal:**
`Quick question, [Firstname]`
`Your trial ends Friday — here's what you lose`

**Urgency (use sparingly — overuse collapses credibility):**
`Last chance: 48 hours left` [only true if true]
`Only 4 left in your size`

**Social proof:**
`Why 12,000 customers reorder every 90 days`
`The product your neighbours are ordering`

### Modifiers that lift open rates

| Modifier | Lift | When to use |
|----------|------|-------------|
| First name personalisation | +26% average | Nurture, re-engagement — not promotional |
| Urgency language | +22% average | Expiry, flash sale, cart — when genuinely urgent |
| Emojis | +56% average | DTC/consumer brands; test before scaling |
| Question format | Varies | Best for curiosity and nurture |
| Number in subject | +15–20% | Lists, countdowns, stats |

**Emoji rules:** Use maximum 1 emoji per subject line. Place at the beginning or end, never mid-sentence. Avoid for B2B SaaS — test first with the specific audience.

### What kills open rates

- ALL CAPS (reads as spam)
- Excessive punctuation `!!!`
- Misleading subject lines (high open, low click, high unsubscribe)
- "FWD:" or "RE:" tricks — B2C audiences recognise them; damages trust
- Spam trigger words in subject: "free", "guaranteed", "winner", "cash" — test deliverability if needed

### Preview text rules

Preview text is the second line of the subject. It is the most underused subject-line asset in email.

- Optimal length: 40–100 characters (30 minimum before it gets cut)
- **Never repeat the subject line** — it wastes the second impression
- Treat it as a tagline to the subject: subject = headline, preview = subhead
- If left blank, ESPs pull the first line of the email (often an unsubscribe link or header text — always fill it manually)

**Formula:**
`[Subject]: Your cart is waiting → [Preview]: Free shipping expires at midnight`
`[Subject]: Quick question, Sarah → [Preview]: Takes 30 seconds to answer`
`[Subject]: Your trial ends Friday → [Preview]: Here's everything you'd lose access to`

> For full subject line formulas by email type and worked examples, read `assets/brand-strategy.md` → Subject Lines by Email Type.

---

## Phase 3 — Body Copy

### Length by email type

| Email type | Target word count | Notes |
|------------|------------------|-------|
| Promotional / campaign | 50–125 words | Short wins; cut every sentence that doesn't earn its place |
| Welcome email 1 | 100–200 words | Deliver the offer + set expectations. No walls of text. |
| Abandoned cart email 1 | 50–100 words | Fast, punchy. Remind + CTA. |
| Abandoned cart email 2 | 75–150 words | Add social proof or address the most common objection |
| Winback | 75–150 words | Direct, no fluff, one compelling reason to return |
| Nurture email | 150–250 words | Progressive — earlier emails shorter, later emails deeper |
| Plain text B2B | 75–200 words | Reads like a human sent it. No bullet points in the email body. |
| Post-purchase | 100–175 words | Reassure + educate + next step |
| Re-engagement | 75–125 words | One value prop, one question, one CTA |

**Rule:** If you can say it in fewer words, say it in fewer words. Every additional sentence adds a reason to stop reading.

### Structure

Every email body should follow this skeleton — adapt length to type:

```
1. LEAD (1-2 sentences)
   Acknowledge the context: what just happened, or why you're writing.
   "You added something to your cart and got pulled away."
   "Your trial started 5 days ago — we wanted to check in."

2. BRIDGE (1-3 sentences)
   Connect the context to the value. What does the reader want? What stands in their way?
   "Most people get stuck at [specific step]. Here's the fastest path through it."

3. PROOF (optional, 1-2 sentences)
   Social proof, stat, or example that makes the bridge credible.
   "Over 8,000 customers have completed this step — the ones who do are 3× more likely to stick around."

4. CTA
   One action only. See Phase 4.
```

### Voice guidelines

**DTC / eCommerce (conversational, brand-forward):**
- Contractions: always (it's, you're, we've)
- Sentence length: short and varied — mix 5-word and 15-word sentences
- Avoid: corporate language, passive voice, "utilise"
- OK to: start sentences with "And", "But", "Because"

**B2B SaaS (professional, human):**
- Plain text format or minimal HTML — avoid decorative design
- No slang, no emoji, no urgency tricks
- First-person from a named person: "I wanted to reach out" > "We wanted to reach out"
- Address the reader's professional context: their role, their goal, their pain
- Avoid: buzzwords ("synergy", "leverage", "holistic"), excessive exclamation marks

**Platform vs. person voice:**
- Welcome, promotional, post-purchase → brand voice, HTML, from the brand
- Nurture email 4–5 (bottom of sequence), re-engagement, trial check-in → personal voice, plain text, from a named person

### Common body copy mistakes

| Mistake | Why it fails | Fix |
|---------|-------------|-----|
| Starting with "We" | Centres the brand, not the reader | Start with "You" or address their situation |
| Long paragraphs | Readers scan, not read; walls of text are abandoned | Max 3 sentences per paragraph |
| Multiple topics in one email | Dilutes attention; reader doesn't know what to do | One email, one message, one CTA |
| Generic social proof | "Thousands of customers love us" means nothing | Use specific numbers, names, review excerpts |
| Burying the CTA | Reader loses interest before reaching it | CTA within the first 200 words AND at the bottom |
| Passive voice | Weak and distant | Active: "Get your report" not "Your report can be accessed" |
| Telling, not showing | Abstract benefit claims | Concrete: "Ship in 2 days" not "Fast shipping" |

> For worked email copy examples by type (welcome, cart, winback, nurture, B2B outreach), read `assets/brand-strategy.md` → Copy Templates.

---

## Phase 4 — CTAs

The CTA is the only thing that matters at the end of reading. Everything else has been building toward it.

### CTA copy rules

- **2–4 words maximum** — "Shop now", "Get your discount", "Book a call", "Start your free trial"
- **Action verb first** — "Download", "Get", "Book", "See", "Start", "Try", "Claim"
- **Specific, not generic** — "See the GolfRoots Pro Set" beats "Click here"
- **One CTA per email** — two CTAs split attention and reduce total click rate; if you need two, make one visually dominant

### CTA button design (for HTML emails)

- Minimum size: **44×44px** (Apple HIG and WCAG 2.1 touch target standard)
- Recommended: 48px height, full-width on mobile
- Contrast: button colour must pass WCAG AA (4.5:1 contrast ratio against background)
- White space: minimum 20px above and below the CTA — white space increases conversion by up to 232%
- Text: white or high-contrast on coloured button; never black on dark button

### CTA placement

- **Flow emails:** CTA above the fold (within first scroll) AND repeated at the bottom
- **Promotional campaigns:** CTA at the end of each content section if multiple sections exist
- **Plain text B2B:** Hyperlinked text CTA, no button — "Book a 20-minute call here: [link]"

### Anchor text for plain text emails

The link text should describe the destination or action:
- `Book a call → [calendly link]` ✓
- `Click here → [calendly link]` ✗
- `See the full case study → [link]` ✓
- `Read more → [link]` ✗

---

## Phase 5 — Plain Text vs HTML

The format decision affects deliverability, open rates, and perceived sender identity.

| Situation | Recommended format | Why |
|-----------|-------------------|-----|
| B2B nurture / SDR-type emails | Plain text | +23% open rate vs HTML in B2B contexts; feels personal |
| eCommerce promotional / campaign | HTML (branded template) | Brand experience, visual product presentation |
| eCommerce flow emails (cart, welcome) | HTML with plain text fallback | Visual impact + deliverability safety |
| Trial onboarding (Day 1 check-in) | Plain text | Feels like a colleague checking in, not an email blast |
| Re-engagement / winback | Plain text preferred | Higher deliverability to cold contacts; less likely to land in Promotions |
| Transactional (receipts, confirmations) | HTML | Functional clarity; tables, order summaries |

**Multipart MIME (always recommended):**
Every HTML email should also include a plain text version. Most ESPs do this automatically if you fill in the plain text tab. Plain text version: skip formatting, strip links (replace with full URLs), remove images. Benefits: deliverability, accessibility, compatibility with older email clients.

**Apple Mail Privacy Protection (MPP) note:**
Since 2021, Apple Mail prefetches all emails and records an open — even if the real reader never opens it. This inflates open rates for any audience with significant Apple Mail usage. Do not optimise purely for open rate — click rate and conversion rate are more reliable performance signals.

---

## Phase 6 — Mobile Optimisation

60%+ of emails are opened on mobile. Copy and formatting must work at mobile width first.

### Typography

- Body font: minimum **14px** (16–17px preferred on mobile)
- Heading font: minimum **22px**
- Line height: **1.4–1.6×** the font size (tight line height makes text hard to scan)
- Line length: maximum **65 characters per line** at desktop; on mobile, text will reflow

### Layout

- Single column always — multi-column breaks on mobile
- CTAs: full width on mobile (100% width button, not fixed-width)
- Images: max-width 600px with `width: 100%` styling so they scale down
- Padding: minimum 20px on left and right so text doesn't touch screen edges

### Copy considerations

- Front-load the value in subject line and preview — mobile previews are short
- Lead sentence carries more weight on mobile (reader decides to scroll or not)
- Bullet points render well on mobile for feature lists; avoid for flowing paragraphs

---

## Phase 7 — A/B Testing

Never A/B test without a hypothesis. "Let's try two subject lines" is not a test — it generates data, not learning.

### What to test first (priority order)

1. **Subject line** — highest leverage; affects 100% of recipients
2. **CTA copy** — "Get 15% off" vs "Claim your discount" vs "Shop now"
3. **Email length** — 75 words vs 175 words (especially for cart and nurture)
4. **Plain text vs HTML** — for any audience that skews B2B or enterprise
5. **From name** — "[First name] from [Brand]" vs "[Brand]" vs "[First name] [Last name]"
6. **Send time** — 10 AM vs 2 PM in contact's timezone

### Test rules

- **One variable per test** — never change subject line AND from name AND send time simultaneously
- **Minimum sample size:** 500 contacts per variant for statistical significance (1,000+ preferred)
- **Run duration:** long enough for 80% of opens to register — typically 4 hours for automated flows, 24 hours for campaigns
- **Win condition:** define before the test — "Winner = higher click rate if open rate is within 5% of each other; otherwise winner = higher open rate"
- **Apply the winner** — document the result and update the live email; never let test results sit unactioned

### What not to test

- Formatting only (colour of button, image choice) when copy is untested — fix copy first
- Small lists — 200 per variant is not significant; wait until list size supports it
- Seasonal campaigns — external factors (holidays, news) contaminate results

> For worked A/B test examples and a copy critique framework, read `assets/brand-strategy.md` → A/B Testing and Copy Review.

---

## Phase 8: Synthesis Brief

Before delivering the final copy, write a brief summary of key recommendations. This is used by the orchestrator to carry findings forward to the next skill in a multi-skill workflow.

**Email Copywriting Key Findings**

Extract and summarise:
- **Subject line strategy:** The high-performing formula used for this email type (e.g., for cart: specificity + urgency; for nurture: curiosity gap + personal tone), character count target, and preview text approach. Expected open rate lift based on formula vs control.
- **Copy tone and length:** Recommended word count for this email type, voice (conversational vs formal, DTC vs B2B), whether plain text or HTML is optimal, and any audience-specific adaptations (first-time buyer vs repeat customer)
- **CTA and conversion path:** Single CTA copy (2–4 words, action verb first), button design requirements if HTML, placement strategy (above fold + bottom), and whether this CTA fits into the broader flow/campaign sequence
- **A/B test priorities:** Subject line variant to test first (e.g., curiosity vs offer-forward), minimum sample size, win condition (open rate vs click rate vs revenue), and any secondary tests queued (from name, send time, content length)

**Priority for downstream skills:** The platform-specific execution skills (klaviyo-flows, Klaviyo-email) should build the email exactly as written here and queue the A/B test structure with the subject line variant and win condition defined. Campaign planning should coordinate promotional copy frequency to avoid messaging fatigue across multiple sends.

*If running standalone (not in an orchestrated chain), share this summary with the operator before the full deliverable.*

---

## QA Gate

Before delivering any email copy:

- [ ] Subject line: under 70 characters, tested for mobile cutoff at 46 chars
- [ ] Preview text: filled, under 100 chars, does not repeat subject line
- [ ] Lead sentence: starts with reader context, not "We" or the brand name
- [ ] One email, one CTA — no competing actions
- [ ] CTA copy: 2–4 words, action verb first, specific destination
- [ ] No passive voice, no corporate language
- [ ] Paragraphs: max 3 sentences each
- [ ] Plain text version drafted (even if just a note to the operator to complete it)
- [ ] Word count matches email type target
- [ ] Personalisation tokens verified: `{{ contact.firstname | default: 'there' }}` — always include a fallback

---

## References

- **[Copy Playbook](../../assets/brand-strategy.md)** — Subject line formulas by email type, worked body copy templates (welcome, cart, winback, nurture, B2B), A/B testing framework, and copy critique checklist.
- **[Brand](../../assets/brand-strategy.md)** — Read when Challenger's brand voice is unknown or when producing any branded output. Colours, typography, and tone guidelines.
- **[Klaviyo Campaigns](../klaviyo-campaigns/SKILL.md)** — Use when copy is being written for a campaign send (newsletter, promotional, BFCM) rather than a flow.
