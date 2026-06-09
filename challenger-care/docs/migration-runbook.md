# Migration Runbook

How to move the Challenger Care plugin from one Cowork account to another. Used when transferring ownership to Hayden at the end of the GrowthHit engagement, and re-usable for any future account move.

---

## Migration discipline · the rules

This plugin is built to migrate cleanly. The rules:

1. **All MCP connector UUIDs live in `CONFIG.md` only.** Nothing else hardcodes them.
2. **No `mcp__skills__*` literals in the artifact HTML.** Cowork's scanner picks these up and prompts users to install plugins they don't have.
3. **No account-specific IDs in code** (file IDs, channel IDs, project gids). Documentation may reference them contextually.
4. **The committed artifact HTML holds placeholders.** Each teammate runs `sync-html-config.py` locally after pulling.
5. **Validator runs clean before every commit.** `python3 scripts/validate.py` must pass.
6. **Generate a fresh artifact share link** after every meaningful update.

---

## One-time setup · new account

### 1. Fork or transfer the GitHub repo

**Option A — Repo transfer (recommended for full handoff)**
- In GitHub, go to `harun-oss/challenger-care` → Settings → Transfer ownership
- Transfer to Hayden's GitHub account
- Hayden's repo becomes the source of truth · GrowthHit can be added as a contributor

**Option B — Fork**
- Hayden forks `harun-oss/challenger-care` to his account
- He owns the fork · we push updates via PR

### 2. Install Cowork's GitHub connector

In Hayden's Cowork:
- Settings → Connectors → GitHub → Authorize
- This lets Cowork pull plugins from his GitHub

### 3. Install the plugin

In Hayden's Cowork:
- Plugin Directory → search "challenger-care"
- Install · this clones the repo into Cowork's plugin cache
- Verify all 24 SKILL.md skills appear in the skill index

### 4. Authorize the MCPs

In Hayden's Cowork → Connectors:
- **Shopify** — authorize against `challengercare.com` (required)
- **Klaviyo** — authorize against account `q93EMp` (required)
- **Google Drive** — authorize (optional · for output sync)
- **Asana** — authorize (optional · for in-flight tracking)

After each authorization, Cowork shows the connector's UUID in its settings.

### 5. Update CONFIG.md with the new UUIDs

In Hayden's local repo clone (or via GitHub web UI):

```yaml
connector:
  shopify_uuid: "<paste-new-uuid-here>"
  klaviyo_uuid: "<paste-new-uuid-here>"
  drive_uuid: "<if-connected>"
  asana_uuid: "<if-connected>"
```

Also update `stack.*` if any account IDs differ (e.g., `klaviyo_account_id`).

### 6. Sync the dashboard HTML

```bash
cd challenger-care
pip3 install -r scripts/requirements.txt    # one-time
python3 scripts/sync-html-config.py
```

This writes Hayden's UUIDs into `artifact/command.html` for his local use. **Don't commit this** — run `--reset` before any commit.

### 7. Validate before committing

```bash
python3 scripts/validate.py
```

Must pass 0 errors. If you committed live UUIDs by accident, the validator will catch it.

### 8. Open the dashboard

In Hayden's Cowork → Artifacts → open `artifact/command.html`. Verify:
- KPIs show real numbers
- Shop name in header
- No "CONFIG not synced" warning
- All workflow tiles render

### 9. Generate fresh share link

Cowork's Artifact view → Share → copy new link. Pin in team Slack. Old links are frozen with old artifact requirements.

### 10. Test on a second teammate's Cowork

Before announcing to the full team, install the plugin on Ivey's (or another teammate's) Cowork, repeat steps 4–8, confirm her view works. This catches per-account permission issues.

---

## Recurring · before every commit

```bash
# 1. Reset artifact placeholders
python3 scripts/sync-html-config.py --reset

# 2. Run validator
python3 scripts/validate.py

# 3. If clean, commit + push
git add -A
git commit -m "..."
git push
```

---

## What lives where

| File | Contains | Edit when |
|---|---|---|
| `CONFIG.md` | All UUIDs, goals, thresholds, team contacts | New account, new goal, threshold tuning |
| `CLAUDE.md` | Master project instructions for Claude | Brand strategy shifts, knowledge file added |
| `assets/*.md` | Knowledge files (brand, voice, claims, archetypes) | When the brand or operations change |
| `assets/voc/` | Customer review corpus + analysis | Fresh JudgeMe export — run `voc-processor.py` |
| `skills/<name>/SKILL.md` | Individual workflow definition | A workflow's behavior changes |
| `artifact/command.html` | Dashboard | Layout / KPI changes (UUIDs come from sync, not here) |
| `scripts/` | Validation + sync tooling | Tooling updates only |

---

## Troubleshooting migration issues

See `docs/connector-troubleshooting.md` for tool-specific failure modes.

Common migration-specific issues:

### "Dashboard shows 'CONFIG not synced'"
You haven't run `python3 scripts/sync-html-config.py` after updating CONFIG.md. Run it.

### "Validator catches a UUID I didn't put there"
The committed file may have been synced and not reset. Run `python3 scripts/sync-html-config.py --reset` and re-commit.

### "Plugin installed but skills not showing"
Cowork's plugin directory caches for a few minutes. Wait and refresh. If still missing, verify `marketplace.json` parses as valid JSON.

### "Workflow runs but can't find knowledge files"
The skill is using the old `knowledge/` path. Should be `assets/`. Run the validator — it catches this now.

### "Hayden's MCPs are different — do I update every skill?"
No. Skills never reference UUIDs. They reference `mcp:shopify`, `mcp:klaviyo`, etc. by tool *name*, and the dashboard wires those names to UUIDs through CONFIG.md. Only CONFIG.md needs updating.

---

## Rollback

To roll back the entire repo to a previous state:

```bash
git log --oneline           # find the commit hash to revert to
git revert <hash>           # reverts a single commit
# OR
git reset --hard <hash>     # nukes everything after that commit (destructive)
git push --force-with-lease # only if you understand what this does
```

Per-commit changes are reviewable on GitHub before merging. Use PRs for anything that affects multiple files.

---

## Versioning

The plugin uses semantic versioning at the manifest level:

- `0.1.x` — alpha · initial GrowthHit build
- `0.2.x` — handoff complete · Hayden owns
- `1.0.x` — first stable production version (after 30-day post-launch retro)

`plugin.json` has the canonical version. Update it when shipping a meaningful change. Git tags follow: `v0.1.0-alpha`, `v0.2.0`, `v1.0.0`.

---

## Sign-off checklist for migration

- [ ] Repo transferred / forked to Hayden's GitHub
- [ ] Cowork GitHub connector authorized for Hayden's account
- [ ] Plugin installed · all 24 skills visible
- [ ] All required MCPs authorized (Shopify + Klaviyo minimum)
- [ ] CONFIG.md updated with new UUIDs
- [ ] `sync-html-config.py` run locally
- [ ] Validator passes 0 errors
- [ ] Dashboard opens · KPIs populate
- [ ] Tested on second teammate's Cowork (Ivey)
- [ ] Fresh share link generated + pinned in Slack
- [ ] Training session held (see `docs/training-script.md`)
- [ ] Handoff doc signed by Hayden
