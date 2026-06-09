# Challenger Care Plugin

The full Claude plugin for the Challenger Care team. Installed at the org / project level via the GitHub connector.

---

## What's in this plugin

### Skills (24 total)

**3 orchestration skills:**
- `orchestrator` — routes command bar input to workflows or custom chains
- `briefing-generator` — daily 6am briefing for the dashboard
- `anomaly-detector` — runs anomaly rules every 4 hours, feeds the "On your plate" alert queue

**21 owner-facing workflows:**

| Group | Workflows |
|---|---|
| **Launch & Test** | launch-new-product · launch-new-bundle-or-offer · launch-sale-promo · test-price-claim · onboard-new-subscribers · build-next-email-flow |
| **Grow** | create-this-weeks-ad-creative · create-this-weeks-content · refresh-underperforming-pdp · creator-outreach |
| **Listen** | customer-voice · whats-the-competitor-doing · why-sales-dropped · whats-working-to-scale · diagnose-checkout-funnel |
| **Fix** | reply-to-customer-issue · respond-to-negative-review · fix-broken-flow · inventory-restock |
| **Plan** | highest-leverage · model-unit-economics |

### Assets

**8 knowledge files** in `assets/`:
- `brand-strategy.md` · `unit-economics.md` · `claim-library.md` · `team-roles.md` · `goals-targets.md` · `stack-inventory.md` · `competitor-map.md` · `customer-archetypes.md`

**VOC corpus** in `assets/voc/`:
- 480 published JudgeMe reviews · theme-coded
- Top-50 ad-ready quote library
- Sentiment analysis · emerging themes detection

### Dashboard
`artifact/command.html` — the daily cockpit. Live Shopify + Klaviyo data.

### Scripts
- `scripts/voc-processor.py` — regenerates VOC corpus when new review data lands
- `scripts/validate.py` — pre-commit validator

### Docs
- `docs/how-to-use.md` · `docs/skill-catalog.md` · `docs/connector-troubleshooting.md` · `docs/training-script.md` · `docs/migration-runbook.md`

---

## Connected tools (MCPs)

| Tool | Status | Used by |
|---|---|---|
| **Shopify** | Required | Dashboard · briefing · anomaly-detector · most workflows |
| **Klaviyo** | Required once active | Email-related workflows · briefing · anomaly |
| **Google Drive** | Optional but recommended | Output storage · brand book reference |
| **Asana** | Optional | In-flight project tracking |
| **GA4** | Future | Cross-channel attribution |

UUIDs configured in `CONFIG.md` after first install.

---

## Editability principles

Designed so the team can edit + extend without GrowthHit involvement:

1. **All editable values live in one place** — `CONFIG.md`
2. **Every knowledge file has a "When to update this doc" section**
3. **A `_template/` folder** shows the format for new workflows
4. **`scripts/validate.py`** catches broken edits before they ship
5. **GitHub web UI handles 95% of edits** — no Git knowledge needed for markdown

---

## Permission tiers

Every workflow declares its tier:
- **Generate** — drafts only, no live changes
- **Stage** — pre-loads into a tool but doesn't publish
- **Execute** — live customer-facing change OR money out (Hayden-only by default)

See `assets/team-roles.md` for who can run what.

---

## When to update what

| If this changes... | Edit... |
|---|---|
| Monthly goal | `CONFIG.md` → `goal.monthly_revenue` |
| AOV target | `CONFIG.md` → `goal.aov_target` |
| A claim approval | `assets/claim-library.md` |
| Brand voice | `assets/brand-strategy.md` |
| Team member added | `assets/team-roles.md` |
| Connector UUID | `CONFIG.md` → `connector.<tool>_uuid` |
| Workflow tweak | `skills/<workflow>/SKILL.md` |
| New workflow | Copy `skills/_template/` |
| Dashboard threshold | `CONFIG.md` |
