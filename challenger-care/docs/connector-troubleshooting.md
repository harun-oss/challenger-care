# Connector Troubleshooting

When things break, start here. Common failure modes per tool, with the exact thing to check first.

---

## Shopify

### "Dashboard shows — instead of revenue numbers"
1. Check your Cowork connector settings · is Shopify authorized?
2. Open chat and ask Claude *"What's our 7-day revenue?"* · if that works, the connector is fine — issue is in the artifact
3. If Claude can't pull either: re-authorize the Shopify connector

### "Wrong store data showing"
- Confirm `connector.shopify_uuid` in `CONFIG.md` matches the UUID of your authorized Shopify connector in Cowork
- If you have multiple Shopify connections, you might be hitting the wrong one — update CONFIG.md

### "Sessions or CVR not showing"
- Shopify analytics needs the store to have processed 7+ days of orders before sessions/CVR backfill
- Verify by running `FROM sessions SHOW sessions SINCE -7d` directly in Cowork chat with the Shopify tool

### Migration · post-account-transfer
- Authorize Shopify under Hayden's Cowork account
- Note the new connector UUID (Cowork shows it in connector settings)
- Update `CONFIG.md` → `connector.shopify_uuid`
- Run `python3 scripts/sync-html-config.py` to refresh the dashboard's CONFIG block

---

## Klaviyo

### "Email Revenue KPI shows — instead of a number"
1. Confirm `connector.klaviyo_uuid` is set in `CONFIG.md`
2. Confirm Klaviyo is authorized in Cowork
3. Ask Claude *"List my Klaviyo flows"* · if you see them, the connector works
4. If MTD revenue still doesn't show, the metric ID might need updating — see `assets/stack-inventory.md`

### "Flow performance report is empty"
- The flow may have zero sends in the requested window. Try a longer time range.
- Verify the flow ID by listing flows first · sometimes the dashboard references an outdated ID

### "Can't see new campaigns"
- Klaviyo MCP caches for a few minutes · wait and refresh

### Migration · post-account-transfer
- Same as Shopify: re-authorize · note new UUID · update `CONFIG.md`
- Klaviyo also has an Account ID (`q93EMp` for Challenger) — verify it's correct in `CONFIG.md` → `stack.klaviyo_account_id`

---

## Google Drive

### "Knowledge files not loading in workflows"
1. Confirm Drive is authorized and connected
2. Confirm the plugin is installed (the knowledge files live inside the plugin folder, not in your personal Drive)
3. If you moved knowledge files to a separate Drive folder, update `CONFIG.md` → `stack.drive_client_folder_id`

### "Workflow outputs not appearing in Drive"
- Outputs land in `/outputs/<workflow-name>/` inside the plugin folder by default
- If you want them in your Drive, you'll need to set up a Drive sync · ask Claude for help configuring this

---

## Asana

### "In flight pills not showing on dashboard"
- Asana MCP needs to be connected
- Confirm `connector.asana_uuid` is set in `CONFIG.md`
- Confirm there are tasks tagged for the dashboard to pick up (usually "Challenger Care" project)

---

## GitHub (for editing the system)

### "Validator failing on commit"
1. Run `python3 scripts/validate.py` locally
2. Read each error · they tell you exactly what's wrong
3. Common issues:
   - Missing frontmatter on a new SKILL.md → see `docs/skill-template.md` for the format
   - Hardcoded UUID outside CONFIG.md → move it to CONFIG.md
   - Broken relative link in markdown → fix the path

### "Plugin not appearing in Cowork after push"
- Cowork syncs plugins from GitHub every few minutes
- Try refreshing the Plugin Directory in Cowork
- If still missing, check `.claude-plugin/marketplace.json` syntax is valid JSON

### "Edits not propagating to teammates"
- Plugins sync per-account · each teammate's Cowork pulls fresh on its own schedule
- For immediate updates, they can manually refresh their Plugin Directory

---

## The artifact (dashboard)

### "Artifact prompts to connect a plugin I don't have"
- This is the migration discipline violation we built the validator to prevent
- Run `python3 scripts/validate.py` — it scans for `mcp__skills__*` literals and bare UUIDs and will tell you exactly which file is the culprit
- Generate a fresh share link after fixing (old ones are frozen with old requirements)

### "Numbers in dashboard don't match what's in CONFIG.md"
1. Run `python3 scripts/sync-html-config.py` to sync the dashboard CONFIG block from CONFIG.md
2. Commit + push the regenerated `artifact/command.html`
3. Reload the dashboard in Cowork

### "Dashboard shows old data"
- Cowork artifact has a Reload button · click that
- MCP data caches for the session · close and reopen the artifact for a hard refresh

---

## Permission errors

### "I can't run a Stage-tier workflow"
- Check your assigned permission level in `assets/team-roles.md`
- Ivey: Generate + Stage · Hayden: all tiers
- Future fractional CMO: starts at Generate + Stage, earns Execute over time

### "I tried to Execute and nothing happened"
- Execute-tier actions require explicit Hayden approval
- The workflow may have staged the change in Klaviyo / Shopify but not published yet
- Check the staged action and confirm Hayden's go before proceeding

---

## Share link issues

### "I sent a teammate the dashboard link and they got an error"
- Share links are point-in-time snapshots · old links freeze with old requirements
- Generate a fresh share link after every meaningful update to the artifact
- Document the current share link in your team Slack pinned message

### "My teammate sees different data than I do"
- Both of you need to be authorized to the same MCPs
- Check both your Cowork connector settings · ensure Shopify, Klaviyo, etc. are authorized for both

---

## Escalation path

If none of the above resolves the issue:

1. **Run the validator first** · `python3 scripts/validate.py` · catches most issues
2. **Search GitHub issues** in the challenger-care repo · someone may have hit this before
3. **Open a GitHub issue** with: what you did, what you expected, what happened, screenshots if relevant
4. **Tag harun@growthhit.com** for urgent issues

---

## When to update this doc

- After every new failure mode that requires investigation
- After a migration to a new account (some symptoms only appear post-migration)
- When connectors update their APIs
- Quarterly review even if nothing has broken — keeps it fresh
