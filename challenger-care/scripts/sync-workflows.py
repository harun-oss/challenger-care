#!/usr/bin/env python3
"""
Sync the WORKFLOWS array in artifact/command.html from skills/*/SKILL.md frontmatter.

Reads each user-facing SKILL.md, extracts:
  - name (frontmatter)
  - description (frontmatter, first sentence used for tile label)
  - tier (parsed from preamble line, defaults to 'generate')

Groups workflows by intent buckets (Launch & Test, Grow, Listen, Fix, Plan) — buckets
are derived from skill name patterns. Regenerates the WORKFLOWS JS array in the dashboard.

Run from plugin root:
    python3 scripts/sync-workflows.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DASHBOARD = ROOT / "artifact" / "command.html"

# System skills · not user-facing workflows · excluded from tiles
SYSTEM_SKILLS = {"briefing-generator", "orchestrator", "anomaly-detector"}

# Map skill name → bucket. Order within bucket is the order skills will appear.
BUCKETS = {
    "Launch & Test": [
        "launch-new-product",
        "launch-new-bundle-or-offer",
        "launch-sale-promo",
        "test-price-claim",
        "onboard-new-subscribers",
        "build-next-email-flow",
    ],
    "Grow": [
        "create-this-weeks-ad-creative",
        "create-this-weeks-content",
        "refresh-underperforming-pdp",
        "creator-outreach",
    ],
    "Listen": [
        "customer-voice",
        "diagnose-checkout-funnel",
        "whats-the-competitor-doing",
        "why-sales-dropped",
        "whats-working-to-scale",
    ],
    "Fix": [
        "reply-to-customer-issue",
        "respond-to-negative-review",
        "fix-broken-flow",
        "inventory-restock",
    ],
    "Plan": [
        "highest-leverage",
        "model-unit-economics",
    ],
}

BUCKET_TAGLINES = {
    "Launch & Test": "when you're shipping something new",
    "Grow": "the weekly recurring work",
    "Listen": "before you decide",
    "Fix": "reactive operational work",
    "Plan": "periodic strategic work",
}

# Default which buckets start open
BUCKET_OPEN = {"Launch & Test": True, "Grow": True, "Listen": False, "Fix": False, "Plan": False}


def parse_skill(skill_md: Path) -> dict | None:
    """Pull name, short description, tier from a SKILL.md file."""
    try:
        content = skill_md.read_text(errors='ignore')
    except Exception:
        return None
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---\n", 4)
    if end == -1:
        return None
    fm = content[4:end]
    body = content[end + 5:]

    name = None
    description = None
    for line in fm.splitlines():
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip()
        elif line.startswith("description:"):
            description = line.split(":", 1)[1].strip()

    if not name or not description:
        return None

    # Tier: parse "Permission tier:** generate" from preamble line
    tier = "generate"
    tier_m = re.search(r"\*\*Permission tier:\*\*\s*(\w+)", body)
    if tier_m:
        tier = tier_m.group(1).lower()

    # Tile description: take the first sentence of the SKILL description
    # (before any MANDATORY TRIGGER · keep punchy)
    tile_desc = description
    # Strip MANDATORY TRIGGER + everything after
    tile_desc = re.split(r"(?i)mandatory trigger", tile_desc)[0].strip()
    # Strip trailing period
    tile_desc = tile_desc.rstrip(".").rstrip()
    # If too long, truncate at first period after 60 chars
    if len(tile_desc) > 180:
        cut = tile_desc.find(".", 100)
        if cut > 0:
            tile_desc = tile_desc[:cut]

    return {"name": name, "description": tile_desc, "tier": tier}


def main():
    if not SKILLS_DIR.exists():
        sys.exit("skills/ directory not found")
    if not DASHBOARD.exists():
        sys.exit("artifact/command.html not found")

    # Read all skills
    skills_by_name = {}
    for skill_md in SKILLS_DIR.glob("*/SKILL.md"):
        skill_name = skill_md.parent.name
        if skill_name in SYSTEM_SKILLS:
            continue
        data = parse_skill(skill_md)
        if data:
            skills_by_name[skill_name] = data

    print(f"Found {len(skills_by_name)} user-facing skills")

    # Build the JS WORKFLOWS array, grouped by bucket
    groups_js = []
    seen = set()
    for bucket_name, skill_order in BUCKETS.items():
        items_js = []
        for sk_name in skill_order:
            if sk_name in skills_by_name:
                s = skills_by_name[sk_name]
                seen.add(sk_name)
                # Escape backticks/single-quotes in description
                desc_escaped = s["description"].replace("'", "\\'").replace("\n", " ")
                # Title-case from kebab (with manual overrides for short connectors)
                title = ' '.join(w.capitalize() if w not in {"a", "the", "to", "of", "an", "in", "for", "on"} else w for w in sk_name.replace("-", " ").split())
                # Fix capitalization for "this weeks" and a few patterns
                title = title.replace("This Weeks", "this week's").replace("Pdp", "PDP")
                # Escape single quotes in title for JS single-quoted string literal
                title_escaped = title.replace("\\", "\\\\").replace("'", "\\'")
                items_js.append(
                    f"    {{ title: '{title_escaped}', explain: '{desc_escaped}', tier: '{s['tier']}', skill: '{sk_name}' }}"
                )
        if items_js:
            tagline = BUCKET_TAGLINES.get(bucket_name, "")
            is_open = "true" if BUCKET_OPEN.get(bucket_name, False) else "false"
            groups_js.append(
                f"  {{ group: '{bucket_name}', tagline: \"{tagline}\", open: {is_open}, items: [\n"
                + ",\n".join(items_js)
                + "\n  ] }"
            )

    # Warn about any skills that aren't in a bucket
    unbucketed = set(skills_by_name.keys()) - seen
    if unbucketed:
        print(f"WARNING: skills not in any bucket: {sorted(unbucketed)}")
        print("Add them to BUCKETS dict at top of this script.")

    workflows_js = "const WORKFLOWS = [\n" + ",\n".join(groups_js) + "\n];"

    # Replace existing WORKFLOWS array in HTML
    html = DASHBOARD.read_text()
    pattern = re.compile(r"// Static workflow catalog\nconst WORKFLOWS = \[.*?\n\];", re.DOTALL)
    if not pattern.search(html):
        # Try without comment
        pattern = re.compile(r"const WORKFLOWS = \[.*?\n\];", re.DOTALL)
        if not pattern.search(html):
            sys.exit("ERROR: Could not find WORKFLOWS array in dashboard HTML")

    new_block = "// Workflow catalog · generated by scripts/sync-workflows.py · do not hand-edit\n" + workflows_js
    new_html = pattern.sub(new_block, html, count=1)
    DASHBOARD.write_text(new_html)

    print(f"OK Dashboard WORKFLOWS array regenerated · {sum(len(BUCKETS[b]) for b in BUCKETS)} tiles across {len(groups_js)} groups")


if __name__ == "__main__":
    main()
