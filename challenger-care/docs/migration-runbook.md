# Migration Runbook · v3.1

How the Challenger Care plugin moves from one Cowork account to another · most importantly the GrowthHit → Hayden handoff at engagement end.

---

## v3.1 quick path (most edits)

Most edits don't require a full migration. They're file edits via GitHub web UI.

### To change a goal or threshold
1. Open `CONFIG.md` in GitHub web UI
2. Edit the value in the `goal:` or `threshold:` block
3. Commit
4. Done · validator runs on the commit · CI confirms · plugin auto-syncs on next reload

### To change a team member's name
1. Open `CONFIG.md` in GitHub web UI
2. Edit the relevant `roles.*` value (e.g. `roles.marketing_coordinator: "New Name"`)
3. Commit
4. Done · every skill that references that role updates automatically · no skill body edits needed

### To add a fractional CMO
1. Open `CONFIG.md` · set `roles.fractional_cmo: "Their Name"`
2. Decide which Execute-tier permissions they get (edit `roles.execute_tier_approver` if applicable)
3. Commit · done

---

## Full migration (handoff to Hayden's account)

When the engagement ends and Hayden takes ownership of the repo + plugin:

### Step 1 · Repo ownership
- Transfer the GitHub repo from `harun-oss/challenger-care` to Hayden's GitHub account (or fork it)
- Hayden becomes the admin · GrowthHit becomes a collaborator if continued support is needed

### Step 2 · Cowork connector authorization
On Hayden's Cowork account, authorize:
- Shopify (required) · note the new UUID
- Klaviyo (required) · note the new UUID
- Google Drive (for competitor scan caching) · note the UUID
- Asana (for "In flight" data) · note the UUID

### Step 3 · Update `CONFIG.md` with new account values
Edit one file, every skill updates:

```yaml
connector:
  shopify_uuid: "<Hayden's new Shopify UUID>"
  klaviyo_uuid: "<Hayden's new Klaviyo UUID>"
  asana_uuid: "<Hayden's new Asana UUID>"
  drive_uuid: "<Hayden's new Drive UUID>"

stack:
  asana_project_gid: "<Hayden's Challenger project GID>"
  drive_dashboard_cache_folder_id: "<Hayden's competitor scan cache folder>"

roles:
  founder: "Hayden Wheatley"
  marketing_coordinator: "Ivey"
  manufacturing_lead: "Emanuel Itzhakian"
  email_reviewer: "Ivey"
  inventory_owner: "Emanuel Itzhakian"
  execute_tier_approver: "Hayden Wheatley"
  customer_support_owner: "Ivey"
  reddit_voice_owner: "Hayden Wheatley"
  fractional_cmo: ""
```

### Step 4 · Sync the dashboard
```bash
cd challenger-care
python3 scripts/sync-html-config.py
python3 scripts/sync-workflows.py
```

### Step 5 · Verify
```bash
python3 scripts/validate.py
```

If validator passes 0 errors, 0 warnings → migration done.

### Step 6 · CI setup (if not already done)
See `docs/ci-setup.md`. Two files in `.github/workflows/` need to land · either:
- Add `workflow` scope to the PAT and push, or
- Copy `validate.yml` + `README.md` into GitHub web UI manually

### Step 7 · Generate fresh share link
- Open the artifact in Hayden's Cowork
- Generate a new share link
- Pin in the team Slack channel

### Step 8 · Test on a second teammate's Cowork
- Install the plugin on Ivey's account
- Run a Generate-tier skill (e.g., `customer-voice`) to verify routing works
- Confirm the dashboard loads with the new UUIDs

---

## Migration discipline (still enforced)

The plugin enforces these rules via `scripts/validate.py` (20 checks):

- No `mcp__skills__*` literals in HTML (Cowork's import scanner blocks them)
- All MCP connector UUIDs live in `CONFIG.md` only
- No bare UUIDs outside `CONFIG.md` (the validator's regex catches them)
- No hardcoded account-specific IDs (file IDs, channel IDs, project gids) outside CONFIG.md
- No raw team names in skill bodies (must use `{{roles.X}}` substitution)
- No GrowthHit voice ("GrowthHit", "the AM", "senior CRO strategist") in skill bodies
- Every user-facing skill declares Permission Tier
- Customer-facing skills load brand-strategy + claim-library
- No Composio cross-plugin path references
- Skills using `{{roles.X}}` must list CONFIG.md in their context-loading line
- Files in `skills/` match `docs/port-manifest.md`

Validator runs on every commit (locally) and every PR (via GitHub Actions). Migration discipline holds across the handoff.

---

