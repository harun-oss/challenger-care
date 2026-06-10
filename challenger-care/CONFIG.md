# Challenger Care · CONFIG

**This file holds every value the dashboard, workflows, and scripts reference. Edit here · the whole system updates.**

Last updated: 2026-06-09
Version: 0.1.0-alpha

---

## How to use this file

- **Editing:** Open in GitHub web UI · click pencil icon · change the value in the YAML block · commit.
- **No code changes needed** for any update in this file.
- After editing, run `python3 scripts/validate.py` to confirm the value is picked up correctly.
- The dashboard reads this on every load. Workflows reference it when they run.

Every value below is grouped by purpose. When you edit, leave the keys + structure intact — only change the values.

---

## Goals

The targets every workflow and alert evaluates against. Update quarterly or when strategy shifts.

```yaml
goal:
  monthly_revenue_blended: 60000     # USD · Amazon + Shopify combined · VERIFY against actuals on first run
  monthly_revenue_shopify: 6000      # USD · Shopify-only target (10% of blended)
  monthly_email_revenue: 1000        # USD · Klaviyo target
  email_flow_share_pct: 25           # % of email revenue from automated flows
  aov_target: 50                     # USD · unlocks profitable paid acquisition
  shopify_subscribers_target: 50     # 90-day target for Recharge subscribers
  shopify_subscribers_baseline: 17   # VERIFY against Recharge dashboard · last set 2026-06-09
  amazon_ss_subscribers: 1318        # Manual entry · update from Amazon Seller Central monthly
```

---

## Anomaly thresholds

Drives "On your plate" alerts. Tune as you learn what fires too often or rarely.

```yaml
threshold:
  # Inventory
  inventory_days_critical: 20       # Below = high-severity
  inventory_days_warning: 25        # Below = med-severity
  inventory_default_lead_time_days: 21

  # Funnel
  cart_abandonment_pct: 70
  checkout_abandonment_pct: 70
  device_cvr_gap_min_sessions: 50
  device_cvr_gap_threshold: 1.0     # % point gap mobile-vs-desktop

  # Revenue health
  monthly_pacing_warning_pct: 70
  return_rate_warning_pct: 8
  return_rate_critical_pct: 15
  aov_gap_critical_ratio: 0.7
  aov_gap_warning_ratio: 0.85

  # Email (Klaviyo)
  flow_ctr_drop_pct: 30
  campaign_open_drop_pct: 30

  # Retention
  returning_customer_rate_strong: 30  # Above = "strong retention" win
  returning_customer_rate_weak: 15

  # Bundle attach
  bundle_attach_target_pct: 30
  bundle_attach_floor_pct: 12
```

---

## Unit economics defaults

Used by `model-unit-economics` and bundle math workflows.

```yaml
unit_economics:
  cogs_per_jar_usd: 3.45
  gross_margin_pct: 82
  free_shipping_threshold_usd: 35
  shipping_cost_min_usd: 5.50
  shipping_cost_max_usd: 8.00
  payment_fee_pct: 3.0
  jar_duration_days: 110

  # Bundle (3-pack)
  bundle_3pack_cogs_min_usd: 11
  bundle_3pack_cogs_max_usd: 12
  bundle_3pack_target_price_min_usd: 50
  bundle_3pack_target_price_max_usd: 89
```

---

## Connector UUIDs

The MCP connector identifiers used by the dashboard and workflows. The ONLY UUIDs that should appear anywhere in this repo.

**On migration to a new account, only this section needs updating.**

```yaml
connector:
  shopify_uuid: "262ca9fd-3fa1-4803-a458-2822030a8dd0"      # Update on migration
  klaviyo_uuid: "cf072fd6-c3c4-48ec-af2a-2f4d5457c59d"      # Update on migration

  # Optional — enable when authorized
  drive_uuid: "c4ef2caa-2184-45db-a8b9-048fd7fb7cdc"        # Google Drive MCP UUID (per Cowork connector authorization)
  asana_uuid: "074a94e7-815b-4b26-9a9e-172d35a7ce08"       # Asana MCP UUID (per Cowork connector authorization)
  ga4_uuid: ""
  slack_uuid: ""
```

---

## Stack references

Account-specific resources. Updated at migration.

```yaml
stack:
  shopify_shop_domain: "challengercare.com"
  klaviyo_account_id: "q93EMp"
  klaviyo_sender_email: "Info@challengercare.com"
  drive_client_folder_id: ""        # Add when Drive is connected
  slack_internal_channel_id: ""     # Add if useful
  asana_project_gid: "1189315776295965"  # DUMMY · "Client Onboarding & Tool Setup" · Hayden: replace with real Challenger Care project GID after creating it in his Asana
  drive_dashboard_cache_folder_id: "1wUAhjeUVd6hncbub_-HbY9lk6BrmA057"  # Drive folder where scan outputs live · Hayden: create folder + paste ID
```

---

## Team contacts

Editable as the team changes. Workflows reference these for routing.

```yaml
team:
  founder_email: "hayden@challengercare.com"
  manufacturing_email: "emanuel@amrlabs.com"
  marketing_coord_name: "Ivey"
  growthhit_email_alias: "info@growthhit.com"
```

---

## Roles (substitution layer)

Every skill references roles via `roles.*` keys, never raw names. Edit one value here, every skill that mentions that role updates automatically. Adding a fractional CMO is one edit.

```yaml
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

---

## Brand reference values

Single source of truth for brand identifiers.

```yaml
brand:
  brand_idea: "Show up sharper."
  campaign_platform: "One minute. Every room."
  primary_cta: "Accept the challenge."
  hold_claim_validated: "All-day hold (9-12 hours)"
  positioning_pillar_lead: "Preparation"
```

---

## Schedule / cadence

```yaml
schedule:
  briefing_time_pt: "06:00"
  anomaly_check_interval_hours: 4
  competitor_scan_day: "Sunday"
  competitor_scan_time_pt: "09:00"
```

---

## Model tiers

```yaml
model:
  briefing: "haiku"
  anomaly_detector: "haiku"
  orchestrator_routing: "haiku"
  workflow_execution: "sonnet"
  voc_themes: "haiku"
```

---

## Version control

```yaml
config:
  version: "0.1.0-alpha"
  last_edited: "2026-06-09"
  schema_version: 1
```

---

## When to update this doc

- Any time a goal, threshold, or target shifts
- When a new connector is added
- At migration to a new account (update `connector.*` + `stack.*`)
- When the team grows or contacts change
- Quarterly review minimum
