# Challenger Care · AI Operating System

The Claude plugin that powers Challenger Care's daily growth operations.

Built by GrowthHit · maintained by the Challenger Care team post-handoff.

---

## What this is

A self-contained Claude plugin that gives the Challenger Care team:

- **A daily dashboard** with live Shopify + Klaviyo data, anomaly alerts, and one-click workflow launches
- **21 owner-facing workflows** that wrap real ecommerce moves (launch a product, fix a broken flow, refresh a PDP, etc.) in Challenger's brand voice
- **A briefing skill** that runs daily at 6 AM and narrates the state of the business
- **A command bar orchestrator** that routes free-form requests to the right workflow or builds custom chains
- **The full brand knowledge base** — strategy, voice, claims, customer archetypes, VOC corpus from 480+ reviews

Install once, edit forever. No code changes required for day-to-day updates.

---

## Install

1. Connect this repo via the GitHub connector in your Cowork account (one-time auth)
2. Open the Plugin Directory → Organization tab → install **Challenger Care**
3. Authorize the connectors the plugin reads from:
   - Shopify (required)
   - Klaviyo (required once active)
   - Google Drive (optional · for knowledge file storage)
   - Asana (optional · for project tracking)
4. Update `challenger-care/CONFIG.md` with your connector UUIDs
5. Install the Command dashboard artifact from `challenger-care/artifact/command.html`

Detailed walkthrough in `challenger-care/docs/migration-runbook.md`.

---

## How it's organized

```
.claude-plugin/marketplace.json    ← registers the plugin
challenger-care/
├── .claude-plugin/plugin.json     ← plugin manifest
├── CLAUDE.md                      ← project instructions (loaded first)
├── CONFIG.md                      ← all editable values (goals, thresholds, UUIDs)
├── README.md                      ← plugin-level intro
├── assets/                        ← brand knowledge + VOC corpus
├── skills/                        ← 24 skills (21 workflows + 3 orchestration)
│   └── _template/                 ← copy this folder to add a new workflow
├── artifact/command.html          ← the dashboard
├── scripts/                       ← VOC processor, validator
├── docs/                          ← how-to, training, troubleshooting
└── audits/                        ← Klaviyo audit + competitor scans
```

---

## Editing

This system is designed to be edited by the team, not just GrowthHit.

| Want to change... | Edit... |
|---|---|
| A goal or target | `challenger-care/CONFIG.md` |
| Brand voice or claims | `challenger-care/assets/brand-strategy.md` or `claim-library.md` |
| How a workflow works | `challenger-care/skills/<workflow-name>/SKILL.md` |
| Anomaly thresholds | `challenger-care/CONFIG.md` |
| Add a new workflow | Copy `challenger-care/skills/_template/` |

Most edits happen via GitHub's web UI or by asking Claude to make the change.

Run `python3 challenger-care/scripts/validate.py` after edits to catch issues.

---

## Migration discipline

This repo follows strict discipline so it transfers between accounts cleanly:

- Zero `mcp__skills__*` literals in any HTML
- All connector UUIDs in `CONFIG.md` only
- No hardcoded account-specific IDs (file IDs, channel IDs, project gids)
- Validator catches violations before they ship

Details in `challenger-care/docs/migration-runbook.md`.
