# How to use Challenger Care · 1-pager

A no-jargon guide to the dashboard, command bar, workflows, and how to edit the system. Read this before your first session.

---

## What the system does

You open the **Challenger Care Command** dashboard each morning. It shows:

1. **A briefing** — what happened overnight, what needs your attention, what Claude did for you in the last 24 hours
2. **Live performance** — Shopify revenue, AOV, CVR, customers, with goal tracking
3. **The funnel** — sessions → cart → checkout → completed, with abandonment alerts
4. **Top SKUs** — units sold, sell-through, stock days remaining
5. **On your plate** — prioritized alerts with one-click actions
6. **Workflows** — 21 owner-facing actions you can launch (or type something custom into the command bar)

It also runs in the background:
- **Daily briefing** regenerates at 6 AM PT
- **Anomaly detector** runs every 4 hours
- **Competitor scan** runs Sunday mornings (when configured)

---

## The command bar

Type anything you want Claude to do. The orchestrator routes to the right workflow or builds a custom chain.

**Examples:**
- *"Launch the 3-pack as the new default offer"*
- *"Why did mobile CVR drop Tuesday?"*
- *"Compare our PDP to Hanz De Fuko"*
- *"Draft a Reddit post for r/malegrooming"*
- *"What are customers saying lately?"*

If you don't know which workflow to use, just describe what you want. Claude figures out the right one.

---

## The 21 workflows · what they do

Grouped by intent. See `docs/skill-catalog.md` for full reference.

| Group | When to use |
|---|---|
| **Launch & Test** | Shipping something new (product, bundle, sale, price test, email flow) |
| **Grow** | Weekly recurring work (ad creative, content, PDP refresh, creator outreach) |
| **Listen** | Before deciding (customer voice, competitor scan, sales drop diagnostic) |
| **Fix** | Reactive operational work (customer reply, negative review, broken flow, restock) |
| **Plan** | Periodic strategic work (leverage points, unit economics, checkout funnel diagnostic) |

---

## Permission tiers · who can do what

Every workflow declares one of three tiers:

| Tier | What it means | Who runs it |
|---|---|---|
| **Generate** | Drafts only · no live changes · nothing to reverse | Anyone on the team |
| **Stage** | Pre-loads into a connected tool (Klaviyo, Shopify) but doesn't publish yet | Ivey + Hayden |
| **Execute** | Live customer-facing change OR money out | Hayden only by default |

If you're not sure, the safer move is to run as Generate, review the output, then ask Hayden to Stage or Execute.

See `assets/team-roles.md` for the full matrix.

---

## How to edit the system

### Change a goal or threshold
Edit `CONFIG.md` → commit. That's it. Everything reads from CONFIG.md.

Examples:
- Change AOV target from $50 to $55 → edit `goal.aov_target` in CONFIG.md
- Change inventory warning threshold → edit `threshold.inventory_days_warning`
- Add Hayden's authorized GA4 UUID → edit `connector.ga4_uuid`

### Change brand voice or a claim
Edit the relevant file in `assets/`:
- `assets/brand-strategy.md` — voice rules, pillars, taglines
- `assets/claim-library.md` — approved + banned language
- `assets/customer-archetypes.md` — who we write to

GitHub web UI works fine for these. No code needed.

### Tweak a workflow
Edit `skills/<workflow-name>/SKILL.md`. Update the body content. Commit. Done.

### Add a brand-new workflow
1. Copy the template from `docs/skill-template.md`
2. Rename to your workflow name in kebab-case (e.g., `launch-black-friday`)
3. Fill in every section of the SKILL.md
4. Run `python3 scripts/validate.py` to confirm it's correct
5. Commit + push

### Edit via Claude instead
You can just tell Claude: *"Update CONFIG.md to set AOV target to $55"* — Claude opens the file, makes the change, commits. Even easier than the web UI for most edits.

---

## Daily routine (recommended)

**Morning · 5 minutes:**
1. Open the dashboard
2. Scan the briefing — anything to act on?
3. Scan "On your plate" — pick the top alert · click "Run" or "Send"
4. Note anything for later

**During the week · as needed:**
- Run workflows when you have a question or need to ship something
- Edit knowledge files when business state changes
- Update CONFIG.md when goals shift

**Weekly · 15 minutes:**
- Sunday: competitor scan results land
- Review the week's revenue / AOV / email performance
- Plan next week's content + ad creative via the workflows

---

## When something breaks

1. **Dashboard not loading?** → check `docs/connector-troubleshooting.md`
2. **Workflow producing weird output?** → ask Claude to re-run it · usually a context issue
3. **Validation failing on commit?** → run `python3 scripts/validate.py` to see what's wrong
4. **MCP authorization expired?** → re-authorize in your Cowork connector settings
5. **Anything else?** → open a GitHub issue or message harun@growthhit.com

---

## What you DON'T need to worry about

- **Plugin updates** — GrowthHit pushes them via PR · you review + merge
- **Token costs** — already optimized · Haiku for routine work, Sonnet for creative
- **Connector UUIDs** — set in CONFIG.md once, never touched again
- **Skill format** — `docs/skill-template.md` shows the pattern · validator catches errors

---

## Quick reference

| Want to... | Do this |
|---|---|
| Run a workflow | Click the workflow tile on the dashboard OR type into the command bar |
| Change a number | Edit `CONFIG.md` |
| Update brand voice | Edit `assets/brand-strategy.md` |
| Add a claim | Edit `assets/claim-library.md` |
| Add a workflow | See `docs/skill-template.md` |
| Refresh VOC | Drop new CSV in `assets/voc/exports/` · run `scripts/voc-processor.py` |
| Validate before commit | Run `python3 scripts/validate.py` |
| Get help | harun@growthhit.com |
