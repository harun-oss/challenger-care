#!/usr/bin/env python3
"""
Sync the CONFIG block in artifact/command.html with CONFIG.md values.

Workflow:
  1. Edit CONFIG.md (goals, thresholds, connector UUIDs)
  2. Run this script to push values into artifact/command.html
  3. Reload the dashboard

For migration discipline, the COMMITTED state of artifact/command.html holds
placeholders ('__SHOPIFY_UUID__'). Each teammate runs --apply locally after
pulling, so their dashboard wires up to their authorized MCPs.

Usage:
    python3 scripts/sync-html-config.py            # apply CONFIG.md to HTML
    python3 scripts/sync-html-config.py --reset    # restore placeholders (run before committing)
"""

import re
import sys
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit(
        "ERROR: PyYAML not installed. Run:\n"
        "    pip3 install -r scripts/requirements.txt\n"
        "or:\n"
        "    pip3 install pyyaml"
    )

ROOT = Path(__file__).resolve().parent.parent
CONFIG_MD = ROOT / "CONFIG.md"
DASHBOARD = ROOT / "artifact" / "command.html"

PLACEHOLDER_SHOPIFY = "__SHOPIFY_UUID__"
PLACEHOLDER_KLAVIYO = "__KLAVIYO_UUID__"


def extract_yaml_blocks(md_content):
    merged = {}
    for match in re.finditer(r"```yaml\n((?:.|\n)*?)```", md_content):
        block = match.group(1)
        try:
            data = yaml.safe_load(block) or {}
            merged.update(data)
        except yaml.YAMLError as e:
            print(f"WARNING: could not parse YAML block: {e}")
    return merged


def build_config_block(goals, thresholds, shopify_uuid, klaviyo_uuid):
    return f"""const CONFIG = {{
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
  SHOPIFY_UUID: '{shopify_uuid}',
  KLAVIYO_UUID: '{klaviyo_uuid}',
}};"""


def replace_in_html(html, new_block):
    pattern = re.compile(r"const CONFIG = \{.*?\};", re.DOTALL)
    if not pattern.search(html):
        print("ERROR: Could not find CONFIG block in dashboard HTML")
        sys.exit(1)
    return pattern.sub(new_block, html, count=1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true",
                        help="Restore placeholders (run before commit)")
    args = parser.parse_args()

    if not CONFIG_MD.exists():
        sys.exit("CONFIG.md not found")
    if not DASHBOARD.exists():
        sys.exit("artifact/command.html not found")

    config = extract_yaml_blocks(CONFIG_MD.read_text())
    goals = config.get("goal", {})
    thresholds = config.get("threshold", {})
    connector = config.get("connector", {})

    if args.reset:
        shopify, klaviyo = PLACEHOLDER_SHOPIFY, PLACEHOLDER_KLAVIYO
        mode = "RESET (placeholders restored for commit)"
    else:
        shopify = connector.get("shopify_uuid", "") or PLACEHOLDER_SHOPIFY
        klaviyo = connector.get("klaviyo_uuid", "") or PLACEHOLDER_KLAVIYO
        mode = "APPLIED (UUIDs from CONFIG.md written to HTML)"
        if shopify == PLACEHOLDER_SHOPIFY:
            print("WARNING: CONFIG.md has empty shopify_uuid · dashboard will show 'CONFIG not synced'")

    new_block = build_config_block(goals, thresholds, shopify, klaviyo)
    html = DASHBOARD.read_text()
    new_html = replace_in_html(html, new_block)
    DASHBOARD.write_text(new_html)

    print(f"OK Dashboard CONFIG block · {mode}")
    print(f"   shopify_uuid={shopify[:8]}{'...' if len(shopify) > 8 else ''}")
    print(f"   klaviyo_uuid={klaviyo[:8]}{'...' if len(klaviyo) > 8 else ''}")


if __name__ == "__main__":
    main()
