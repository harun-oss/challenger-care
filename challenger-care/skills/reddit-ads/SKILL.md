---
name: reddit-ads
description: Reddit advertising · campaign setup, subreddit + interest targeting, Reddit-native creative tone, pixel + conversion tracking, weekly performance, subreddit-level optimisation. MANDATORY TRIGGER: any mention of "Reddit Ads", "Reddit campaign", "Reddit advertising", "Reddit targeting", "subreddit targeting", "Reddit promoted post", "Reddit pixel", "advertise on Reddit". Do NOT use for: Organic Reddit posts (use `reddit-founder-post`). Reddit ad concepts from customer language (use `reddit-ad-builder`).
---

> **Permission tier:** execute · **Tools/context:** assets/brand-strategy.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/team-roles.md, CONFIG.md


# Reddit Ads

## What this skill does

Covers the Reddit Ads workflow for clients: campaign setup, subreddit targeting, creative strategy, pixel and conversion tracking, weekly reporting, and monthly subreddit-level optimisation.

Reddit is a fundamentally different platform from Meta and Google. The audience is opt-in communities — they chose to be in specific subreddits because they care deeply about the topic. They are sceptical of obvious advertising and respond to value-first, authentic content. Getting the creative tone wrong on Reddit is worse than not running at all.

Use this skill when:
- Setting up Reddit Ads for a client (currently: Arda Cards)
- Writing the weekly Reddit performance update
- Optimising subreddit targeting and creative rotation
- An AM asks how Reddit differs from Meta or Google in strategy

---

## Phase 1 — Context

Ask one question at a time:

1. **Client name** — who is this for?
2. **What's needed?** — new campaign setup, weekly report, monthly optimisation, or a creative/targeting question?
3. **Vertical** — B2B/SaaS, eCommerce, or Lead Gen? (Reddit works best for B2B/SaaS and niche eCommerce — avoid for mass consumer goods with no community angle)
4. **Campaign objective** — what action are we driving? (Demo bookings / Free trial signups / Purchases / App installs / Awareness)
5. **Has the Reddit pixel been installed?** — if not, this is the first step before any campaign goes live.

---

## Phase 2 — Platform Fundamentals

Before any setup, make sure the operator understands how Reddit is different. This shapes every decision.

**What makes Reddit different:**

- **Community-first.** Users are in subreddits because of a shared, often intense interest. They will engage with relevant ads and destroy irrelevant ones (downvotes, negative comments).
- **No feed algorithm.** Reddit users see content chronologically within subreddits. Ads appear as promoted posts in feeds. If the ad looks out of place for that community, it gets flagged or ignored.
- **Text-heavy performs.** Unlike Meta where visuals dominate, Reddit users often engage with ads that have substantive copy. Long captions and headlines that explain the value clearly outperform pure visual shock.
- **Comments are live.** Reddit users comment on ads. This is a double-edged sword: genuine comments are social proof, hostile comments are visible to everyone. Monitor comments and respond.
- **Lower CPMs, lower intent.** Reddit CPMs are cheaper than Meta but conversion intent is lower. Best used for awareness and middle-funnel engagement, not direct last-click conversion.

**When Reddit works well:**

- B2B/SaaS targeting a professional community with a niche tool
- eCommerce with a strong hobbyist/enthusiast angle (golf, fitness, board games, specialty food)
- Lead gen for services that map to a specific subreddit community
- Retargeting engaged Reddit users who have visited the site

**When Reddit doesn't work well:**

- Mass consumer products with no community angle
- Very broad audiences (Reddit's strength is specificity)
- Pure direct-response with a hard-sell approach — Reddit users will roast the ad

---

## Phase 3 — Reddit Pixel Setup

Install before launching any campaign. No pixel = no conversion tracking = no ability to optimise.

**Setup steps:**

1. Reddit Ads Manager → Tools → Reddit Pixel
2. Copy the base pixel code
3. Install via Google Tag Manager:
   - Add a Custom HTML tag with the Reddit pixel base code
   - Trigger: All Pages
4. Create conversion events:
   - **Purchase** (eCommerce): trigger on order confirmation page — pass `value` and `currency` parameters
   - **Lead / Sign Up** (B2B/SaaS): trigger on thank-you page after form submission
   - **Add to Cart** (eCommerce): trigger on add-to-cart button click
5. Verify via Reddit Pixel Helper (Chrome extension) — confirm all events fire correctly before launching

**Reddit pixel + Meta pixel:** Both can fire on the same pages. They don't conflict.

---

## Phase 4 — Campaign Setup

### Campaign Objective

Select based on what Challenger is optimising for:

| Objective | Use when |
|-----------|----------|
| Conversions | Pixel installed, 50+ conversions/month expected — best for lead gen and eCommerce |
| Traffic | New accounts without pixel data, or driving blog/content traffic |
| Video Views | Brand awareness with video creative |
| App Installs | Mobile apps |
| Brand Awareness | Impression-based, no conversion optimisation |

Start with **Conversions** if the pixel is installed. If conversion volume will be low (<20/month), use **Traffic** until volume builds.

### Ad Group — Targeting

Reddit offers three targeting approaches. Use them as separate ad groups — not stacked.

**1. Subreddit Targeting (primary — use first)**

Target specific subreddit communities whose members match the ideal customer.

Process:
1. List 10–20 subreddits where the ideal customer is active
2. In Reddit Ads Manager, search for each subreddit to confirm it's targetable (some private/small subreddits are not)
3. Check estimated audience size — target subreddits with 50K+ members; below this, reach is too limited
4. Group similar subreddits into one ad group (3–8 subreddits per group)
5. Create separate ad groups for distinct audience clusters

> For subreddit research methodology and vetted subreddit lists by vertical, read `references/reddit-playbook.md`.

**2. Interest Targeting (secondary)**

Reddit's interest categories are broader than subreddits. Use as a secondary test after subreddit targeting is established.

Select 1–3 interest categories that match the customer profile. Avoid stacking more than 3 — the audience gets too broad and loses community relevance.

**3. Keyword Targeting**

Target users based on keywords they've searched or engaged with on Reddit. Useful for catching users mid-research (e.g., targeting "project management software" for a B2B tool).

Use phrase and exact match keywords. Avoid broad — Reddit keyword broad match casts too wide a net.

### Ad Group — Budget & Bidding

- Minimum daily budget: $10/day per ad group (below this, insufficient delivery)
- Recommended starting budget: $20–30/day per ad group
- Bid strategy: start with **Automated bid** (Reddit optimises for the selected objective)
- After 14 days of data, review CPM and adjust if overpaying

---

## Phase 5 — Creative Strategy

**The most important section of this skill.** Creative on Reddit is make-or-break. An ad that feels like an ad gets downvoted and commented on negatively.

### The Reddit Creative Rules

**Rule 1: Sound like a Redditor, not a brand.**
Reddit users can smell corporate copy instantly. Write in plain, conversational English. No exclamation points. No "game-changing" or "revolutionary." No stock photo energy.

**Rule 2: Lead with value, not product.**
The best Reddit ads lead with something genuinely useful or interesting — a stat, a counterintuitive insight, a relatable problem — before mentioning the product. Users engage with content that respects their intelligence.

**Rule 3: Be specific to the subreddit.**
The creative should feel like it belongs in the subreddit it's targeting. An ad in r/projectmanagement should acknowledge project management problems. An ad in r/golf should speak golf. Generic ads that could run anywhere perform worst on Reddit.

**Rule 4: Acknowledge you're advertising.**
Reddit users respect honesty. "We made a tool for this problem, and we think [specific subreddit] would actually find it useful" outperforms a hard sell. Transparency about the commercial intent paradoxically builds trust.

**Rule 5: Watch the comments and respond.**
Enable comments on ads. Monitor daily, especially in the first week. Respond to legitimate questions. Do not engage with hostile comments defensively — acknowledge and move on.

### Ad Formats

| Format | Best use | Notes |
|--------|----------|-------|
| Promoted Post (text + image) | B2B, SaaS, niche eCommerce | Most common. Headline + body copy + image. Feels most native. |
| Promoted Post (text only) | B2B thought leadership, discussion-starter | Pure copy. Works in subreddits with strong text culture (r/entrepreneur, r/startups) |
| Video | Product demos, before/after, "how it works" | Autoplay muted. Subtitles mandatory. |
| Carousel | eCommerce with multiple products | Less common on Reddit; use sparingly |
| Conversation Ad | Driving direct replies — used for lead capture | Users reply to the ad in Reddit DM style |

### Headline and Copy Length

- **Headline:** 60–90 characters. State the value or problem clearly. No clickbait.
- **Body copy:** Reddit allows long-form copy. 150–300 words often outperforms short copy. Use it to explain, not just tease.
- **Call to action:** Soft CTAs outperform hard ones on Reddit. "See how it works" > "Buy now". "Try it free" > "Get 50% off today only".

> For Reddit copy templates, headline frameworks, and subreddit-specific tone adjustments, read `references/reddit-playbook.md`.

---

## Phase 6 — Weekly Reporting

**Metrics to pull from Reddit Ads Manager (last 7 days):**

| Metric | Where to find |
|--------|--------------|
| Spend | Campaign overview |
| Impressions | Campaign overview |
| Clicks | Campaign overview |
| CTR | Clicks ÷ Impressions |
| Conversions | Conversions column (if pixel active) |
| CPA | Cost ÷ Conversions |
| CPM | Cost per 1,000 impressions |
| Comments | Ad-level — check for tone (positive / neutral / negative) |

**Weekly update format (Reddit section):**

```
Reddit Ads Performance
• Last 7 Days: [N] [Leads/Purchases] / $[X] CPA / $[X] spend / [X] CPM
• Last 30 Days: [N] [Leads/Purchases] / $[X] CPA / $[X] spend
• Top subreddit this week: r/[name] — [N] conversions at $[X] CPA
• Comment sentiment: [Positive / Neutral / Mixed — flag if negative]
```

Add Reddit as a row in the Spend Tracker. If conversion volume is low (<10/month), report on Traffic and CTR as the primary efficiency metric while conversion data builds.

---

## Phase 7 — Monthly Optimisation

### Subreddit Performance Analysis

Pull a subreddit-level breakdown (Ad Group → breakdown by subreddit if available, or review by ad group):

- Which subreddits are generating conversions?
- Which subreddits have high CTR but zero conversions? (Traffic without intent — pause or reduce budget)
- Which subreddits have low CTR but low CPM? (May be worth keeping for awareness volume)

**Action rules:**

| Subreddit performance | Action |
|----------------------|--------|
| CPA within target, conversions > 5/month | Scale — increase budget 20% |
| High CTR, zero conversions, 14+ days | Pause — traffic without intent |
| Low CTR (<0.3%), low conversions | Replace with a new subreddit from the research list |
| Negative comments, any CPA | Review ad creative — may need tone adjustment |

### Creative Rotation

Reddit creative fatigues quickly in niche subreddits (small communities see the same ad repeatedly). Rotate creative every 4–6 weeks per subreddit group.

Signs of fatigue:
- CTR declining week-over-week with stable impressions
- Increase in negative comments
- CPM rising as Reddit reduces ad score

Rotation approach: keep the subreddit targeting constant, swap the creative. Test a new headline angle and new image/video with the same audience before changing targeting.

### Comment Review

Check the comments on all active ads monthly. If negative comment threads have 5+ replies:
- Review whether the comments identify a legitimate product objection (address in the next creative)
- Consider disabling comments on that specific ad if they're hostile with no resolution
- Do not delete individual comments — Reddit users notice and it worsens sentiment

---

## Synthesis Brief

Before building the final deliverable, write a plain-text summary of key findings for orchestrator handoff.

**Reddit Ads Key Findings:**
- Subreddits targeted (list of 5-20 primary subreddits by audience cluster, estimated audience size per subreddit, confidence of targeting match to ideal customer)
- Ad format used (Promoted Post text+image, text-only, Video, or Conversation Ad; justification for format selection based on subreddit culture)
- Creative angle deployed (headline, key value proposition stated, Reddit-native tone positioning, and how it differs from Meta/Google approach)
- Weekly ROAS or CPA performance (conversions this week, spend, CPM, subreddit performance breakdown showing top and bottom performers)
- Next test hypothesis (new creative angle to test, new subreddit audience cluster, comment sentiment observation, or bid strategy adjustment planned)

**Priority for downstream skills:** If campaign is live and performing, route to ongoing weekly optimization and subreddit performance monitoring. If conversion volume is sufficient (>5/month per subreddit), route to subreddit rebalancing and creative rotation decisions. If comments indicate creative tone misalignment or negative sentiment, flag for creative angle iteration.

*If running standalone, share this summary with the operator or client team before the full deliverable.*

---

## QA Gate

Before launching or delivering any report:

- [ ] Reddit pixel installed and all conversion events verified firing
- [ ] Subreddits confirmed targetable in Ads Manager (not all subreddits are available)
- [ ] Creative tone reviewed against Reddit rules: no corporate speak, value-first, subreddit-specific
- [ ] Comments enabled and monitoring plan confirmed (check daily for first 2 weeks)
- [ ] UTM parameters added to all URLs: `utm_source=reddit&utm_medium=cpc&utm_campaign=[name]`
- [ ] CPA target set before launch — know what "working" looks like before evaluating results
- [ ] 14-day minimum evaluation window before pausing underperforming subreddits

---

## Reference Files

This skill uses reference materials. The orchestrator will locate and load these automatically via Glob.

- `references/reddit-playbook.md` — Subreddit research methodology and vetted subreddit lists by vertical; Reddit copy templates and headline frameworks by objective. Needed during Phases 4 and 5.
