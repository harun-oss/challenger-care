#!/usr/bin/env python3
"""
Sync the CONFIG block in artifact/command.html with CONFIG.md values.

Reads CONFIG.md, extracts YAML blocks, regenerates the JS CONFIG object
in command.html so the dashboard always reflects CONFIG.md.

Run after every CONFIG.md edit.
"""

import re
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_MD = ROOT / "CONFIG.md"
DASHBOARD = ROOT / "artifact" / "command.html"


def extract_yaml_blocks(md_content):
    """Pull all ```yaml ... ``` blocks from CONFIG.md and merge."""
    merged = {}
    for match in re.finditer(r"```yaml\n((?:.|\n)*?)```", md_content):
        block = match.group(1)
        try:
            data = yaml.safe_load(block) or {}
            merged.update(data)
        except yaml.YAMLError as e:
            print(f"WARNING: could not parse YAML block: {e}")
    return merged


def main():
    if not CONFIG_MD.exists():
        print("CONFIG.md not found")
        return
    if not DASHBOARD.exists():
        print("artifact/command.html not found")
        return

    config = extract_yaml_blocks(CONFIG_MD.read_text())
    print(f"Loaded config keys: {list(config.keys())}")

    # Build the new JS CONFIG object
    goals = config.get("goal", {})
    thresholds = config.get("threshold", {})
    connector = config.get("connector", {})

    new_block = f"""const CONFIG = {{
  goals: {{
    monthly_revenue: {goals.get('monthly_revenue_shopify', 6000)},
    aov_target: {goals.get('aov_target', 50)},
    monthly_email_revenue: {goals.get('monthly_email_revenue', 1000)},
  }},
  thresholds: {{
    cart_abandonment: {thresholds.get('cart_abandonment_pct', 70)},
    checkout_abandonment: {thresholds.get('checkout_abandonment_pct', 70)},
    return_rate: {thresholds.get('return_rate_warning_pct', 8)},
  }},
  SHOPIFY_UUID: '{connector.get('shopify_uuid', '')}',
  KLAVIYO_UUID: '{connector.get('klaviyo_uuid', '')}',
}};"""

    html = DASHBOARD.read_text()
    # Replace the existing const CONFIG = {...}; block
    pattern = re.compile(r"const CONFIG = \{.*?\};", re.DOTALL)
    if pattern.search(html):
        html_new = pattern.sub(new_block, html, count=1)
        DASHBOARD.write_text(html_new)
        print("✓ Dashboard CONFIG block synced from CONFIG.md")
    else:
        print("Could not find CONFIG block in dashboard HTML")


if __name__ == "__main__":
    main()
