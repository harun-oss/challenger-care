#!/usr/bin/env python3
"""
Challenger Care · Plugin Validator

Runs migration discipline + format compliance checks across the plugin.
Run before every commit. Exits 0 on success, 1 on failure.

Usage:
    python3 scripts/validate.py
    python3 scripts/validate.py --verbose
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"


def find_plugin_root():
    here = Path(__file__).resolve().parent
    if here.name == "scripts":
        return here.parent
    if (here / "skills").exists() and (here / "CLAUDE.md").exists():
        return here
    raise SystemExit("Could not locate plugin root.")


def fail(msg, errors):
    errors.append(msg)


def warn(msg, warnings):
    warnings.append(msg)


def check_no_mcp_skills_references(root, errors):
    print(f"\n{BOLD}1. Checking for mcp__skills__* in HTML files...{RESET}")
    html_files = list(root.glob("**/*.html"))
    found_any = False
    for html in html_files:
        if "/outputs/" in str(html) or "/.cache/" in str(html):
            continue
        content = html.read_text(errors='ignore')
        for match in re.finditer(r"mcp__skills__\w*", content):
            fail(f"  {RED}X{RESET} {html.relative_to(root)} contains literal '{match.group()}' at position {match.start()}", errors)
            found_any = True
    if not found_any:
        print(f"  {GREEN}OK No mcp__skills__* in HTML{RESET}")


def check_no_hardcoded_uuids(root, errors, warnings):
    print(f"\n{BOLD}2. Checking for hardcoded UUIDs outside CONFIG.md...{RESET}")
    uuid_re = re.compile(r"mcp__([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})__")
    found_any = False
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in {".md", ".html", ".js", ".py", ".json"}:
            continue
        if path.name == "CONFIG.md":
            continue
        if "/outputs/" in str(path) or "/.cache/" in str(path):
            continue
        try:
            content = path.read_text(errors='ignore')
        except Exception:
            continue
        for match in uuid_re.finditer(content):
            fail(f"  {RED}X{RESET} {path.relative_to(root)} hardcoded UUID: {match.group()} - move to CONFIG.md", errors)
            found_any = True
    if not found_any:
        print(f"  {GREEN}OK No hardcoded MCP UUIDs outside CONFIG.md{RESET}")


def check_skill_frontmatter(root, errors, warnings):
    print(f"\n{BOLD}3. Validating SKILL.md frontmatter...{RESET}")
    skills_dir = root / "skills"
    if not skills_dir.exists():
        warn(f"  {YELLOW}!{RESET} skills/ directory not found", warnings)
        return
    count = 0
    issues = 0
    for skill_md in skills_dir.glob("*/SKILL.md"):
        if "_template" in str(skill_md):
            continue
        count += 1
        content = skill_md.read_text(errors='ignore')
        if not content.startswith("---\n"):
            fail(f"  {RED}X{RESET} {skill_md.relative_to(root)} missing frontmatter", errors)
            issues += 1
            continue
        end = content.find("\n---\n", 4)
        if end == -1:
            fail(f"  {RED}X{RESET} {skill_md.relative_to(root)} frontmatter not closed", errors)
            issues += 1
            continue
        fm = content[4:end]
        if "name:" not in fm:
            fail(f"  {RED}X{RESET} {skill_md.relative_to(root)} missing 'name:'", errors)
            issues += 1
        if "description:" not in fm:
            fail(f"  {RED}X{RESET} {skill_md.relative_to(root)} missing 'description:'", errors)
            issues += 1
    if issues == 0:
        print(f"  {GREEN}OK All {count} SKILL.md files have valid frontmatter{RESET}")


def check_config_md_exists(root, errors):
    print(f"\n{BOLD}4. Confirming CONFIG.md exists...{RESET}")
    config = root / "CONFIG.md"
    if not config.exists():
        fail(f"  {RED}X{RESET} CONFIG.md missing - required for editability", errors)
        return
    content = config.read_text(errors='ignore')
    required_blocks = ["goal:", "threshold:", "connector:", "team:", "brand:"]
    missing = [b for b in required_blocks if b not in content]
    if missing:
        for block in missing:
            fail(f"  {RED}X{RESET} CONFIG.md missing required block: {block}", errors)
    else:
        print(f"  {GREEN}OK CONFIG.md present with all required blocks{RESET}")


def check_plugin_json(root, errors):
    print(f"\n{BOLD}5. Validating plugin.json...{RESET}")
    pj = root / ".claude-plugin" / "plugin.json"
    if not pj.exists():
        fail(f"  {RED}X{RESET} .claude-plugin/plugin.json missing", errors)
        return
    try:
        data = json.loads(pj.read_text())
        for k in ["name", "version", "description"]:
            if k not in data:
                fail(f"  {RED}X{RESET} plugin.json missing key: {k}", errors)
        if not errors:
            print(f"  {GREEN}OK plugin.json valid (name: {data['name']}, version: {data['version']}){RESET}")
    except json.JSONDecodeError as e:
        fail(f"  {RED}X{RESET} plugin.json invalid JSON: {e}", errors)


def check_marketplace_json(root, errors):
    print(f"\n{BOLD}6. Validating marketplace.json...{RESET}")
    mj = root.parent / ".claude-plugin" / "marketplace.json"
    if not mj.exists():
        fail(f"  {RED}X{RESET} ../.claude-plugin/marketplace.json missing", errors)
        return
    try:
        data = json.loads(mj.read_text())
        if "plugins" not in data:
            fail(f"  {RED}X{RESET} marketplace.json missing 'plugins' array", errors)
            return
        print(f"  {GREEN}OK marketplace.json valid - {len(data['plugins'])} plugin(s) registered{RESET}")
    except json.JSONDecodeError as e:
        fail(f"  {RED}X{RESET} marketplace.json invalid JSON: {e}", errors)


def check_claude_md(root, errors):
    print(f"\n{BOLD}7. Confirming CLAUDE.md exists...{RESET}")
    cm = root / "CLAUDE.md"
    if not cm.exists():
        fail(f"  {RED}X{RESET} CLAUDE.md missing - required project instructions", errors)
        return
    print(f"  {GREEN}OK CLAUDE.md present{RESET}")


def main():
    parser = argparse.ArgumentParser(description="Validate the Challenger Care plugin.")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    root = find_plugin_root()
    print(f"{BOLD}Challenger Care - Plugin Validator{RESET}")
    print(f"Plugin root: {root}")

    errors = []
    warnings = []

    check_no_mcp_skills_references(root, errors)
    check_no_hardcoded_uuids(root, errors, warnings)
    check_skill_frontmatter(root, errors, warnings)
    check_config_md_exists(root, errors)
    check_plugin_json(root, errors)
    check_marketplace_json(root, errors)
    check_claude_md(root, errors)

    print(f"\n{BOLD}Summary{RESET}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")

    if warnings and args.verbose:
        print(f"\n{YELLOW}Warnings:{RESET}")
        for w in warnings:
            print(w)

    if errors:
        print(f"\n{RED}{BOLD}VALIDATION FAILED{RESET}")
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        print(f"\n{GREEN}{BOLD}VALIDATION PASSED{RESET}")
        sys.exit(0)


if __name__ == "__main__":
    main()
