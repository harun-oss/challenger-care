# Team Training Session · 90-minute Walkthrough

Used during the live handoff session with Hayden, Emanuel, and Ivey. Records to Drive for future team onboarding.

**Format:** Live demo · screen-share · pause for questions every 15 min
**Duration:** 90 min · 60 min content + 30 min Q&A
**Tools needed:** Hayden's Cowork (signed in) · the installed Challenger Care plugin · the dashboard artifact

---

## Pre-session checklist

- [ ] Plugin installed in Hayden's Cowork · all 24 skills visible in Plugin Directory
- [ ] All MCPs authorized (Shopify, Klaviyo, Drive, Asana)
- [ ] CONFIG.md updated with Hayden's connector UUIDs
- [ ] Dashboard share link generated · in pinned Slack message
- [ ] All knowledge files visible in `assets/`
- [ ] Validator passes clean (`python3 scripts/validate.py`)
- [ ] Test workflow run completed (e.g., `customer-voice` against the VOC corpus)
- [ ] Recording started

---

## Section 1 · What this is (5 min)

**Open with the story:**

*"Hayden, you told us in the kickoff that the AI system wall was context — having to re-explain who you are, what the brand is, every session. We built this so that's never a problem again.*

*Everything you'd need to tell an agency, a fractional CMO, or a new hire is now in this plugin. Claude reads it every session. You can edit it. Your team can edit it. It evolves as the business evolves.*

*Today I'll show you:*
*1. The dashboard you'll open every morning*
*2. The command bar — type anything you want done*
*3. The 21 workflows — the muscle memory of the system*
*4. How to edit anything — because this is a living thing"*

---

## Section 2 · The dashboard tour (15 min)

**Open the dashboard.**

Walk through top-to-bottom:

1. **Header + greeting** — "Your week so far" · the date · MTD pacing
2. **Context strip** — the chips show what Claude has loaded · click "Edit context →" to update brand book, claims, etc.
3. **Morning Briefing** — explain it's cached daily at 6 AM · regenerates on schedule · narrates the state of the business in Challenger voice
4. **Performance KPIs** — Revenue · AOV · CVR · Customers · all live from Shopify
5. **Funnel section** — sessions → ATC → checkout → completed · with abandonment + bundle attach
6. **Top SKUs** — units, sell-through, days stock · color-coded status (Hero, Healthy, Overstocked, Restock Now)
7. **On your plate** — alerts derived from real data · each one with permission tier + contract
8. **Workflows section** — the 21 workflows · click any tile to run
9. **Competitor Watch** — Sunday scan results
10. **Channels strip** — live data per channel · pending sections clearly marked
11. **In flight** — projects from Asana

**Demo:** Click on one alert → walk through the contract → click "Run" → show the output landing in the chat.

**Pause for questions.**

---

## Section 3 · The command bar (10 min)

**Show the command bar in action with 3 examples:**

1. *"Launch the 3-pack as the new default offer"* → orchestrator routes to `launch-new-bundle-or-offer`
2. *"Why did mobile CVR drop Tuesday?"* → routes to `diagnose-checkout-funnel`
3. *"What are customers saying about humidity?"* → routes to `customer-voice` with a theme filter

**Explain:** The orchestrator picks the right workflow based on what you say. You don't need to know the workflow name — describe the outcome, Claude figures it out.

**For custom requests:** If no workflow fits, the orchestrator builds a custom chain — picks 2-3 workflows + runs them in sequence.

---

## Section 4 · The 21 workflows (15 min)

**Quick tour grouped by intent:**

- **Launch & Test** (6 workflows): for shipping new things
- **Grow** (4 workflows): weekly recurring work
- **Listen** (5 workflows): before deciding
- **Fix** (4 workflows): reactive operational work
- **Plan** (2 workflows): strategic work

**Demo 2 in full:**
1. **launch-new-product** — show what files get generated
2. **customer-voice** — show real VOC output

**Mention the catalog:** `docs/skill-catalog.md` has the full reference.

---

## Section 5 · Permission tiers (5 min)

**The three tiers:**

| Tier | Example | Who runs it |
|---|---|---|
| **Generate** | Draft a customer reply, generate ad concepts | Anyone |
| **Stage** | Pre-load a Klaviyo flow but don't publish | Ivey + Hayden |
| **Execute** | Send a campaign, publish a PDP, place a PO | Hayden only |

**Show the team-roles file** · explain how to add a future CMO + give them permissions.

---

## Section 6 · How to edit · the editability deep dive (15 min)

**This is the part Hayden cares most about. Spend time here.**

### Edit a goal
*Open CONFIG.md in GitHub web UI* · change AOV target from $50 to $55 · click commit · explain how everything reads from this file.

### Edit brand voice
*Open `assets/brand-strategy.md`* · show how voice rules are defined · imagine adding a new approved word.

### Edit a workflow
*Open `skills/launch-new-product/SKILL.md`* · show the format · explain how to tweak the output list.

### Add a new workflow
*Open `skills/_template/SKILL.md`* · explain the copy-and-rename pattern · run validate.py to confirm it works.

### Edit via Claude
*"Hayden, update CONFIG.md to set AOV target to $55"* — show Claude opening the file, making the change, committing. Easier than the web UI for most edits.

### Refresh VOC with new reviews
*Show* dropping a CSV into `assets/voc/exports/` · running `scripts/voc-processor.py` · outputs regenerate.

---

## Section 7 · When things break (5 min)

Walk through `docs/connector-troubleshooting.md`.

The main escalation path:
1. Run validate.py
2. Check the troubleshooting doc
3. GitHub issue
4. harun@growthhit.com

---

## Section 8 · What's next (5 min)

**Setup for ongoing:**
- Hayden runs the dashboard every morning
- Ivey can run Generate + Stage workflows
- Updates to brand voice / goals / thresholds happen via CONFIG.md and assets/
- GrowthHit pushes plugin updates via PR · Hayden reviews + merges

**30-day retro scheduled** · we'll review usage, surface what's working, refine what isn't.

---

## Section 9 · Q&A (30 min)

Open it up. Common questions to expect:

- *"How do I know my changes are working?"* → run validator + open dashboard
- *"What if I break something?"* → revert the commit · we can roll back any change
- *"Can my future CMO use this?"* → yes · add them as a GitHub contributor · give them a Cowork seat
- *"What if I want to add a new channel (TikTok Shop)?"* → we add it to CONFIG · build new workflows · same pattern
- *"What happens at engagement end?"* → repo transfers to your GitHub · you fully own it · we provide ongoing support if needed

---

## Post-session checklist

- [ ] Recording saved to Drive
- [ ] Q&A transcript captured
- [ ] Any commitments noted (new workflows requested, edits needed, etc.)
- [ ] Follow-up scheduled (30-day retro)
- [ ] Hayden has bookmark to dashboard
- [ ] Ivey has bookmark + permissions confirmed
