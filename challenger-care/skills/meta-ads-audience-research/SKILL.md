---
name: meta-ads-audience-research
description: 'Builds Meta audience strategy - target customer research, interest categories, lookalikes, exclusions, refresh cadence. MANDATORY TRIGGER: any mention of "Meta audience research", "Meta audience strategy", "interest targeting", "build audiences for Meta", "lookalike audience setup", "Meta audience refresh", "targeting strategy Meta". Do NOT use for: Campaign structure (use `meta-ads-campaign-build`). Scaling/budget decisions.'
---

> **Permission tier:** generate · **Tools/context:** assets/brand-strategy.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/team-roles.md, CONFIG.md


# Meta Ads Audience Research

## What this skill does

This skill builds the audience strategy before any campaign goes live — researching who the customer is, selecting the right guide interests for the algorithm's early learning phase, setting up lookalike audiences once pixel data exists, and defining exclusions that protect spend efficiency.

Challenger's philosophy: **the Meta algorithm finds audiences better than manual targeting once it has data.** Audience research here is not about building complex interest stacks — it's about giving the algorithm a sensible starting point and getting out of the way.

Use this skill when:
- Building the initial audience strategy for a new client before campaign launch
- Setting up lookalike audiences after the pixel has accumulated conversion data
- Performance has plateaued and audiences may be saturated — time to refresh
- An AM wants to understand who the customer is before writing copy or creative briefs

---

## Phase 1 — Context

Ask one question at a time:

1. **Client name and product/service** — what are they selling?
2. **Vertical** — eCommerce or Lead Gen?
3. **Where are we in the engagement?** — new client (pre-launch), or existing client refreshing audiences?
4. **Pixel status** — how many monthly conversion events does the pixel currently have? (Under 200 = early stage. 200+ = algorithm can optimise from data.)
5. **Do we have any existing customer data?** — customer email list, purchase history, CRM export? (Needed for lookalike seeds.)
6. **Any audience intel already gathered?** — value prop exercise results, customer interviews, prior ad performance data?

If a value prop exercise has already been done for this client, ask the operator to share the key customer insights from it — those findings directly inform the interest categories and the copy angle for each audience.

---

## Phase 2 — Customer Profile Research

Before touching Ads Manager, build a clear picture of who the customer is. Ask:

> "Describe your best customer in one paragraph. Not demographics — describe their life. What problem do they have? What do they do on a Thursday afternoon? What other brands do they buy? What would make them stop scrolling?"

If the operator can answer this confidently, proceed. If not, run through the rapid customer profile:

**Rapid customer profile (ask one question at a time):**

1. **Primary problem/motivation:** What is the #1 reason someone buys this product? (Not "it's good quality" — the specific problem or desire it resolves.)
2. **Who they are:** Age range, life situation, occupation type? Not for targeting — for writing interests that reflect real people.
3. **What else they buy:** What other brands, categories, or subscriptions does this customer have? (These become interest candidates.)
4. **Where they spend time:** What media do they consume, what apps do they use, what communities are they part of?
5. **Trigger moment:** What happens in their life right before they would search for this product? (Understanding the trigger sharpens creative direction and interest selection.)

Read `references/audience-playbook.md` → Customer Profile section for the full question framework and how to translate answers into interest categories.

---

## Phase 3 — Guide Interest Strategy (New Pixel / Early Stage)

For accounts under 200 monthly conversion events, the algorithm needs a gentle guide — not a narrow constraint.

**The goal:** Select 1–2 interest categories that describe the target customer well enough to tilt the algorithm's initial learning toward the right audience, while keeping the total potential reach above 3 million.

**Interest selection rules:**
- Never stack more than 2–3 interests in one ad set in the early stage
- Prefer **broad category interests** (e.g., "Fitness and wellness") over hyper-specific ones ("CrossFit") — the algorithm will narrow from broad better than it will expand from narrow
- Avoid overlapping interests in the same ad set — overlap fragments the signal
- Use Audience Insights in Meta (if available) or the interest search in Ads Manager to check estimated reach before finalising

**Three types of interests to consider:**

| Type | What it is | Example |
|------|-----------|---------|
| Direct category | The product category itself | "Skin care", "Home improvement" |
| Adjacent brand | Competitor or complementary brand | "Glossier", "Patagonia" |
| Lifestyle signal | What the customer does or reads | "Outdoor recreation", "Health magazine" |

Select one from each type as candidates. Test all three as separate ad sets (not combined) if budget allows. If budget is limited, pick the one that best matches the customer profile — typically the lifestyle signal outperforms the direct category.

**Reach check:** Target 3–10M potential reach for most accounts. Under 1M = too narrow. Over 20M = may be too diffuse for early learning.

Read `references/audience-playbook.md` → Interest Selection section for the full interest vetting process and common mistakes.

---

## Phase 4 — Broad Targeting Transition

Once the pixel hits **200+ monthly conversion events**, switch the main campaign to Advantage+ Audience (broad targeting). This is not optional — it is the standard approach.

**What to tell the operator:**
> "At 200+ monthly conversions, the pixel knows your buyer better than any interest list we could build. Advantage+ Audience gives the algorithm full latitude to find them. Narrow interest stacks at this stage actively reduce performance by constraining the algorithm's search."

**Transition checklist:**
- [ ] Pixel has 200+ conversion events in the last 30 days
- [ ] At least one prior experiment has run (provides creative signal beyond just targeting)
- [ ] Existing interest-targeted ad sets paused (not deleted — keep for comparison reference)
- [ ] Main campaign switched to Advantage+ Audience
- [ ] 7-day monitoring period after transition — flag any CPA/ROAS spike immediately

---

## Phase 5 — Lookalike Audiences

Lookalike audiences are built from a seed — a list of existing customers or high-value website visitors. They are most useful for:
- Scaling into a new audience segment after broad targeting is established
- Testing against the broad Advantage+ baseline
- Multi-market expansion (building lookalikes from the US base to test in AU, UK, CA)

**When to build lookalikes:**
- Pixel has at least 1,000 purchase events (for purchase lookalikes)
- Or: a customer email list with at least 500 matched users exists

**Seed options (in order of quality):**

| Seed | Quality | Notes |
|------|---------|-------|
| Purchasers (pixel events) | ★★★★★ | Best signal — actual buyers |
| High-value purchasers (top 25% LTV) | ★★★★★ | Best for premium scaling |
| Customer email list | ★★★★ | Upload to Custom Audience first |
| Add-to-cart (no purchase) | ★★★ | Intent signal — lower quality than purchasers |
| All website visitors | ★★ | Too broad — use only if purchase data is very limited |

**LAL percentage tiers:**
- 1% LAL — most similar to seed. Use first. Highest quality, smallest reach.
- 2–3% LAL — slightly broader. Use after 1% is at scale.
- 5–10% LAL — broad. Useful for awareness campaigns; lower conversion intent.

**Testing LALs vs. broad:**
Run the LAL as a separate ad set alongside the Advantage+ broad campaign. Do not replace broad with LAL — test them side by side. The broad campaign often outperforms LAL by month 3+.

---

## Phase 6 — Exclusions

Exclusions protect spend efficiency. Always apply:

**Standard exclusions (apply to all campaigns):**

| Exclusion | How to create | Why |
|-----------|--------------|-----|
| Recent purchasers (last 30 days) | Pixel event: Purchase | Don't serve acquisition ads to people who just bought |
| Email list (existing customers) | Custom Audience upload | Suppress from acquisition campaigns; use for retention separately |
| Current retargeting audience | Website visitors (last 30 days) | If running a separate DPA retargeting campaign, exclude them from the main prospecting campaign |

**When to review exclusions:**
- At 90 days: check if the excluded audience is large enough to run a dedicated winback or upsell campaign
- After any large promotion: add promo buyers to exclusion list for 30 days to avoid post-purchase ad fatigue

---

## Phase 7 — Audience Refresh (Existing Clients)

Symptoms that the audience needs refreshing:
- Frequency above 3.5 in the last 7 days (shown in Ads Manager)
- CTR declining while spend holds steady
- CPA rising despite no creative or offer changes
- Reach declining week-over-week for same budget

**Refresh options (in order of disruption):**

1. **Add new creative first** — audience saturation and creative fatigue look identical. Before changing the audience, test new creative. If new creative doesn't help, then it's an audience issue.

2. **Expand the interest category** — if on a guided interest, widen to a broader parent category or add one adjacent interest.

3. **Shift to Advantage+ Audience** — if not already on broad, this is the next step.

4. **New LAL seed** — build a fresh lookalike from the most recent 90-day purchaser cohort.

5. **Geo expansion** — if the account is US-only, test adding CA or UK as incremental audiences. Multi-market clients have this built into their structure already.

---

## Phase 8 — Synthesis Brief

Before delivering the final audience strategy, write a brief summary of key findings. This is used by the orchestrator to carry findings forward to the next skill in a multi-skill workflow.

**[Client Name] Audience Strategy Key Findings**
- Top finding 1 — specific audience segment with supporting data. Example: "ICP is price-sensitive wellness professionals aged 28–42 in metro areas, who engage with fitness content and complementary wellness brands"
- Top finding 2 — specific lookalike or exclusion insight. Example: "Lookalike seed quality: 1,200+ purchase events provide strong signal; 1% LAL outperforms broad targeting in early stage"
- Top finding 3 — specific exclusion or refresh trigger. Example: "Recent purchasers (30-day exclusion) represent 15% of audience size; exclusion gap is large enough to warrant separate winback campaign at month 3"

**Priority for downstream skills:** What the next skill should focus on — be specific to the Meta Ads workflow context. Example: "Use these audience segments and exclusion rules when building the campaign structure. Primary creative angle should appeal to the price-sensitivity signal identified."

*If running standalone (not in an orchestrated chain), share this summary with the operator before the full deliverable.*

---

## Phase 9 — Output Format

> "Audience strategy ready. How would you like it delivered?
>
> 1. **Audience brief** — written document covering customer profile, guide interests, lookalike setup, and exclusions — ready to hand off to the campaign builder
> 2. **Slide deck addition** — audience strategy slide to add to the Meta Strategy Deck or monthly deck
> 3. **Verbal summary** — confirm the strategy in this conversation before building in Ads Manager"

For **audience brief** (DOCX): invoke the docx skill. Read `../../../growthit-brand/assets/growthit-brand.md` for branding. Structure as: Customer Profile → Guide Interests → Lookalike Setup → Exclusions → Refresh Triggers.

---

## Reference Files

This skill uses reference materials. The orchestrator will locate and load these automatically via Glob.

- `references/audience-playbook.md` — Full customer profile question framework, interest selection vetting process, common interest mistakes by vertical, and lookalike seed quality guide. Needed during Phases 2 and 3.

---

## QA Gate

Before delivering:

- [ ] Customer profile is grounded in real customer insight — not assumptions
- [ ] Interests selected are from different categories (not three near-identical options)
- [ ] Potential reach for each interest checked in Ads Manager (3–10M target)
- [ ] Lookalike seed quality confirmed — purchasers preferred over visitors
- [ ] Standard exclusions defined (recent purchasers, email list, retargeting overlap)
- [ ] Transition trigger noted: "Switch to Advantage+ Audience at 200 monthly conversion events"
- [ ] Refresh triggers documented so AM knows when to come back
- [ ] Synthesis brief written (if in an orchestrated chain)
