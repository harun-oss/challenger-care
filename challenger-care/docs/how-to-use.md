# How to Use the Challenger OS · One-Pager for the Team

For the team operating Challenger Care · founder, marketing coordinator, manufacturing lead, future fractional CMO.

---

## What this is

A Claude plugin that gives you:

- **A daily dashboard** (Challenger OS · the artifact) · live Shopify + Klaviyo + Amazon data + 15 Library entry cards for action
- **~66 skills + 3 system skills** that handle launches, fixes, diagnostics, content, ads, email, SEO, customer voice, and strategy
- **A brand knowledge base** loaded into every skill at runtime · voice, claims, archetypes, VOC, unit economics, goals
- **Migration discipline** baked in · 20 validator checks · CI on every PR · no name leaks · no agency-voice leaks

---

## The 30-second mental model

1. **Open the dashboard.** Read the Daily 3 (revenue, new customers, days of stock). If all green → ship features. If red → that's today's priority.
2. **Need something done?** Click an entry card in the Library OR type the request into the command bar. The orchestrator routes.
3. **Want to change something?** Edit the right file via GitHub web UI · everything updates automatically.

---

## Three things that change a lot · and where to edit each

### Goals + thresholds
Edit `CONFIG.md` → relevant block. Dashboard + briefing + alerts all read from this.

**Examples:**
- AOV target → `goal.aov_target`
- Anomaly thresholds → `threshold.*`
- Subscriber goal → `goal.shopify_subscribers_target`

### Team names
Edit `CONFIG.md` → `roles.*` block. Every skill that mentions a role updates.

**Examples:**
- Ivey leaves → change `roles.marketing_coordinator` and `roles.email_reviewer`
- Hire a fractional CMO → set `roles.fractional_cmo`
- New manufacturing lead → change `roles.manufacturing_lead` and `roles.inventory_owner`

No skill body edits needed. Skills resolve `{{roles.X}}` tokens at runtime.

### Brand voice + claims + archetypes
Edit the relevant file in `assets/`:

| Change | Edit |
|---|---|
| Voice rules · taglines · positioning | `assets/brand-strategy.md` |
| What we can/can't say | `assets/claim-library.md` |
| Customer archetypes | `assets/customer-archetypes.md` |
| Competitor positioning | `assets/competitor-map.md` |
| Unit economics (COGS, margin, etc.) | `assets/unit-economics.md` |
| Goals + targets narrative | `assets/goals-targets.md` |
| VOC corpus | `assets/voc/voc-corpus.csv` + run `scripts/voc-processor.py` |

---

## How to launch work

### From the dashboard
Click any of the 15 entry cards. The card expands to show the spoke skills bound to it. Click a spoke → its trigger phrase drops into the chat input → press Enter.

### From chat
Type in plain English. Examples:
- *"Launch the 3-pack as default offer"* → runs the 3-pack chain
- *"Why did sales drop?"* → runs why-sales-dropped
- *"Build the welcome flow"* → runs build-next-email-flow
- *"Reactivate Meta"* → runs the Meta reactivation chain
- *"Refresh the Pomade PDP"* → runs the PDP refresh chain

The orchestrator picks the right route.

---

## Permission tiers

| Tier | What | Who |
|---|---|---|
| **Generate** | Drafts only, no live changes, no money out | Anyone on the team |
| **Stage** | Pre-loads into Klaviyo/Shopify/Asana but doesn't publish | marketing_coordinator + above |
| **Execute** | Live customer-facing change OR money out | execute_tier_approver only |

When a skill is Execute-tier, it stops and asks the execute_tier_approver (currently set in CONFIG.md → `roles.execute_tier_approver`) for confirmation.

---

## How to add a new workflow

1. Read `docs/skill-template.md`
2. Copy the template into `skills/<your-skill-name>/SKILL.md`
3. Add a row to `docs/port-manifest.md`
4. Run `python3 scripts/validate.py` · fix anything it flags
5. Open a PR · CI runs validator + dashboard sync check
6. Merge

If the new skill should appear in the Library, bind it to one of the 15 entry cards by adding it to that card's "Bound spokes" row in `port-manifest.md`. The dashboard refreshes on next `sync-workflows.py` run.

---

## How to ask Claude to make a change

You don't need to know the file structure. Just ask:

- *"Claude, update CONFIG.md so AOV target is $55"* → Claude opens a PR
- *"Claude, add a competitor called Hims to competitor-map"* → Claude opens a PR
- *"Claude, rewrite the Pomade PDP refresh skill to load brand-strategy explicitly"* → Claude opens a PR

CI runs on the PR. CONFIG/assets PRs auto-merge if validator is green. Skill changes wait for one human approval.

---

## The 6 named chains (multi-skill workflows)

The orchestrator runs these when the request matches:

| Chain | Trigger | Sequence |
|---|---|---|
| 3-pack launch | "Launch the 3-pack as default" | bundle → ads → email → campaign |
| Meta reactivation | "Turn Meta back on" | tracking audit → audience → build → testing → reporting |
| Subscription migration | "Move Amazon subs to Shopify" | model → email → campaign → onboard |
| Email program restart | "Restart Klaviyo" | audit → strategy → flows × N |
| Quarterly review | "Grade the business" | LPA → roadmap → competitive |
| PDP refresh | "Refresh the [SKU] PDP" | copy audit → heuristic → rebuild → test → report |

---

## When things break

| Symptom | Where to look |
|---|---|
| Dashboard not loading data | `docs/connector-troubleshooting.md` |
| Validator failing on commit | Read the error · usually a missing context file or name leak |
| Skill not firing as expected | Check `assets/usage-log.md` · did it route at all? |
| Edit not propagating | Check CI · is the PR merged? |
| MCP connector unhappy | `docs/migration-runbook.md` has connector setup |

---

## What's where (quick reference)

```
challenger-care/
├── CLAUDE.md                    · master project instructions
├── CONFIG.md                    · all editable values (goals, roles, UUIDs)
├── README.md                    · plugin-level intro
├── assets/                      · brand knowledge files
│   ├── brand-strategy.md
│   ├── claim-library.md
│   ├── customer-archetypes.md
│   ├── competitor-map.md
│   ├── unit-economics.md
│   ├── goals-targets.md
│   ├── team-roles.md            · narrative (CONFIG.md is the substitution truth)
│   ├── stack-inventory.md
│   ├── experiment-log.md        · running A/B test log
│   ├── usage-log.md             · per-skill invocation log
│   ├── promo-calendar.md        · annual rhythm
│   └── voc/                     · 480 review corpus + analysis
├── skills/                      · 69 user-facing + 3 system skills
│   └── <skill-name>/SKILL.md
├── artifact/command.html        · the dashboard
├── docs/
│   ├── port-manifest.md         · canonical skill inventory
│   ├── skill-catalog.md         · this catalog
│   ├── how-to-use.md            · this doc
│   ├── migration-runbook.md     · handoff + setup
│   ├── connector-troubleshooting.md
│   ├── ci-setup.md              · GitHub Actions setup
│   └── skill-template.md        · for adding new skills
└── scripts/
    ├── validate.py              · 20 migration checks
    ├── sync-workflows.py        · regen dashboard from manifest
    ├── sync-html-config.py      · regen dashboard from CONFIG.md
    └── voc-processor.py         · refresh VOC corpus
```
