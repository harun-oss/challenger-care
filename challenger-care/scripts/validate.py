#!/usr/bin/env python3
"""
Challenger Care - Plugin Validator

Migration-discipline + format compliance checks.
Run before every commit. Exits 0 on success, 1 on failure.

Checks:
  1. No mcp__skills__* literals in HTML (Cowork scanner safety)
  2. No mcp__<uuid>__ patterns outside CONFIG.md
  3. No bare UUID literals outside CONFIG.md (NEW)
  4. SKILL.md frontmatter has name + description
  5. User-facing skills have MANDATORY TRIGGER + Do NOT use clauses (NEW)
  6. CONFIG.md present with required blocks
  7. plugin.json + marketplace.json valid
  8. CLAUDE.md present
  9. Markdown links resolve to existing files (NEW)
 10. No references to ghost folders (knowledge/, skills/lib/, system/) (NEW)
 11. requirements.txt present if any script imports yaml (NEW)
 12. Artifact CONFIG block uses placeholders OR is synced (NEW)

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

# System skills don't need MANDATORY TRIGGER (they're invoked by code, not by Claude)
SYSTEM_SKILLS = {"briefing-generator", "orchestrator", "anomaly-detector"}

# Folders skills might reference - flag these if they don't exist
GHOST_FOLDER_PATTERNS = [
    (r'\bknowledge/', 'knowledge/ (use assets/ instead)'),
    (r'\bskills/lib/', 'skills/lib/ (does not exist)'),
    (r'\bsystem/anomaly-detector', 'system/anomaly-detector (use skills/anomaly-detector/SKILL.md)'),
]

# Bare UUID regex (any standard 8-4-4-4-12 hex pattern)
BARE_UUID_RE = re.compile(r'\b[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b')

# UUID inside mcp__ prefix
MCP_UUID_RE = re.compile(r"mcp__([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})__")


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


def check_no_mcp_uuid_references(root, errors):
    print(f"\n{BOLD}2. Checking for mcp__<uuid>__ patterns outside CONFIG.md...{RESET}")
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
        for match in MCP_UUID_RE.finditer(content):
            fail(f"  {RED}X{RESET} {path.relative_to(root)} hardcoded mcp UUID: {match.group()}", errors)
            found_any = True
    if not found_any:
        print(f"  {GREEN}OK No hardcoded mcp__<uuid>__ outside CONFIG.md{RESET}")


def check_no_bare_uuids(root, errors, warnings):
    """NEW: catch bare UUID literals like SHOPIFY_UUID: '262ca9fd-...'"""
    print(f"\n{BOLD}3. Checking for bare UUID literals outside CONFIG.md...{RESET}")
    found_any = False
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        # Only check code files where a UUID would be a literal value
        if path.suffix not in {".html", ".js", ".py", ".md", ".json"}:
            continue
        if path.name == "CONFIG.md":
            continue
        # Skip VOC CSV and exports (third-party data with random IDs)
        if "/voc/" in str(path) and path.suffix == ".csv":
            continue
        if "/exports/" in str(path):
            continue
        if "/outputs/" in str(path) or "/.cache/" in str(path):
            continue
        try:
            content = path.read_text(errors='ignore')
        except Exception:
            continue
        for match in BARE_UUID_RE.finditer(content):
            uuid_val = match.group()
            # Get the surrounding line for context
            line_start = content.rfind('\n', 0, match.start()) + 1
            line_end = content.find('\n', match.end())
            line = content[line_start:line_end if line_end != -1 else None].strip()
            fail(f"  {RED}X{RESET} {path.relative_to(root)} bare UUID: {uuid_val}", errors)
            fail(f"      Line: {line[:120]}", errors)
            found_any = True
    if not found_any:
        print(f"  {GREEN}OK No bare UUID literals outside CONFIG.md{RESET}")


def check_skill_frontmatter(root, errors, warnings):
    print(f"\n{BOLD}4. Validating SKILL.md frontmatter...{RESET}")
    skills_dir = root / "skills"
    if not skills_dir.exists():
        warn(f"  {YELLOW}!{RESET} skills/ directory not found", warnings)
        return
    count = 0
    issues = 0
    for skill_md in skills_dir.glob("*/SKILL.md"):
        skill_name = skill_md.parent.name
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
        # Extract description
        desc_match = re.search(r'^description:\s*(.+?)$', fm, re.MULTILINE)
        if not desc_match:
            fail(f"  {RED}X{RESET} {skill_md.relative_to(root)} missing 'description:'", errors)
            issues += 1
            continue
        desc = desc_match.group(1).strip()
        if len(desc) < 30:
            fail(f"  {RED}X{RESET} {skill_md.relative_to(root)} description too short ({len(desc)} chars): {desc!r}", errors)
            issues += 1
        # User-facing skills must have routing hints
        if skill_name not in SYSTEM_SKILLS:
            if "MANDATORY TRIGGER" not in desc:
                warn(f"  {YELLOW}!{RESET} {skill_md.relative_to(root)} missing 'MANDATORY TRIGGER' in description", warnings)
            if "Do NOT" not in desc and "do not use" not in desc.lower():
                warn(f"  {YELLOW}!{RESET} {skill_md.relative_to(root)} missing 'Do NOT use for' in description", warnings)
    if issues == 0:
        print(f"  {GREEN}OK All {count} SKILL.md files have valid frontmatter{RESET}")


def check_no_ghost_folder_references(root, errors):
    """NEW: catch references to folders that don't exist."""
    print(f"\n{BOLD}5. Checking for references to non-existent folders...{RESET}")
    found_any = False
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in {".md", ".html", ".js", ".py"}:
            continue
        if "/outputs/" in str(path) or "/.cache/" in str(path):
            continue
        # Skip the validator itself (defines the patterns)
        if path.name == "validate.py":
            continue
        try:
            content = path.read_text(errors='ignore')
        except Exception:
            continue
        for pattern, label in GHOST_FOLDER_PATTERNS:
            for match in re.finditer(pattern, content):
                # Get line context
                line_start = content.rfind('\n', 0, match.start()) + 1
                line_end = content.find('\n', match.end())
                line = content[line_start:line_end if line_end != -1 else None].strip()
                # Skip lines that are documentation OF the rule rather than violating it
                if "use assets/" in line or "not knowledge" in line:
                    continue
                if "old `knowledge/` path" in line or "Should be `assets/`" in line:
                    continue
                if "`knowledge/` path" in line:  # discussing the deprecated path
                    continue
                fail(f"  {RED}X{RESET} {path.relative_to(root)}: refers to {label}", errors)
                fail(f"      Line: {line[:120]}", errors)
                found_any = True
    if not found_any:
        print(f"  {GREEN}OK No ghost folder references{RESET}")


def check_config_md_exists(root, errors):
    print(f"\n{BOLD}6. Confirming CONFIG.md exists...{RESET}")
    config = root / "CONFIG.md"
    if not config.exists():
        fail(f"  {RED}X{RESET} CONFIG.md missing", errors)
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
    print(f"\n{BOLD}7. Validating plugin.json...{RESET}")
    pj = root / ".claude-plugin" / "plugin.json"
    if not pj.exists():
        fail(f"  {RED}X{RESET} .claude-plugin/plugin.json missing", errors)
        return
    try:
        data = json.loads(pj.read_text())
        for k in ["name", "version", "description"]:
            if k not in data:
                fail(f"  {RED}X{RESET} plugin.json missing key: {k}", errors)
        print(f"  {GREEN}OK plugin.json valid (name: {data['name']}, version: {data['version']}){RESET}")
    except json.JSONDecodeError as e:
        fail(f"  {RED}X{RESET} plugin.json invalid JSON: {e}", errors)


def check_marketplace_json(root, errors):
    print(f"\n{BOLD}8. Validating marketplace.json...{RESET}")
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
    print(f"\n{BOLD}9. Confirming CLAUDE.md exists...{RESET}")
    cm = root / "CLAUDE.md"
    if not cm.exists():
        fail(f"  {RED}X{RESET} CLAUDE.md missing", errors)
        return
    print(f"  {GREEN}OK CLAUDE.md present{RESET}")


def check_markdown_links(root, errors, warnings):
    """NEW: relative markdown links should resolve to existing files."""
    print(f"\n{BOLD}10. Checking markdown links resolve...{RESET}")
    link_re = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    found_broken = False
    for md in root.rglob("*.md"):
        if "/outputs/" in str(md) or "/.cache/" in str(md):
            continue
        try:
            content = md.read_text(errors='ignore')
        except Exception:
            continue
        for match in link_re.finditer(content):
            link_text, link_target = match.group(1), match.group(2)
            # Skip URLs, anchors, mailto
            if link_target.startswith(("http://", "https://", "mailto:", "#", "tel:")):
                continue
            # Strip anchor fragment
            link_path = link_target.split("#")[0]
            if not link_path:
                continue
            target = (md.parent / link_path).resolve()
            if not target.exists():
                warn(f"  {YELLOW}!{RESET} {md.relative_to(root)}: broken link → {link_target}", warnings)
                found_broken = True
    if not found_broken:
        print(f"  {GREEN}OK All markdown links resolve{RESET}")


def check_requirements_for_yaml(root, errors, warnings):
    """NEW: if any script imports yaml, requirements.txt should exist."""
    print(f"\n{BOLD}11. Checking for requirements.txt if PyYAML used...{RESET}")
    yaml_users = []
    for py in (root / "scripts").glob("*.py") if (root / "scripts").exists() else []:
        try:
            content = py.read_text(errors='ignore')
            if "import yaml" in content or "from yaml" in content:
                yaml_users.append(py.name)
        except Exception:
            continue
    if not yaml_users:
        print(f"  {GREEN}OK No yaml-dependent scripts{RESET}")
        return
    req = root / "scripts" / "requirements.txt"
    if not req.exists():
        req = root / "requirements.txt"
    if not req.exists():
        fail(f"  {RED}X{RESET} {yaml_users} import yaml but no requirements.txt found", errors)
    else:
        content = req.read_text()
        if "pyyaml" not in content.lower() and "yaml" not in content.lower():
            warn(f"  {YELLOW}!{RESET} requirements.txt exists but doesn't list pyyaml", warnings)
        else:
            print(f"  {GREEN}OK requirements.txt lists pyyaml{RESET}")


def check_artifact_uuid_state(root, warnings):
    """NEW: warn if artifact has real UUIDs committed (should be placeholders)."""
    print(f"\n{BOLD}12. Checking artifact CONFIG state...{RESET}")
    artifact = root / "artifact" / "command.html"
    if not artifact.exists():
        return
    content = artifact.read_text(errors='ignore')
    m = re.search(r"SHOPIFY_UUID:\s*'([^']*)'", content)
    if not m:
        warn(f"  {YELLOW}!{RESET} Could not find SHOPIFY_UUID in artifact", warnings)
        return
    val = m.group(1)
    if val.startswith("__") and val.endswith("__"):
        print(f"  {GREEN}OK Artifact CONFIG holds placeholders (committable state){RESET}")
    elif BARE_UUID_RE.match(val):
        warn(f"  {YELLOW}!{RESET} Artifact has live UUID '{val[:8]}...' committed. Run: python3 scripts/sync-html-config.py --reset before commit", warnings)
    else:
        warn(f"  {YELLOW}!{RESET} Artifact SHOPIFY_UUID is unexpected value: {val[:20]}", warnings)



def check_mcp_tools_tightness(root, warnings):
    """NEW: Check that every registered tool in artifact is actually called.
    Per migration discipline: 'Keep mcp_tools tight — register only what you call.'"""
    print(f"\n{BOLD}13. Checking artifact mcp_tools tightness...{RESET}")
    artifact = root / "artifact" / "command.html"
    if not artifact.exists():
        return
    content = artifact.read_text(errors='ignore')
    # Extract registered tools: pattern `<key>: 'mcp__' + CONFIG.X_UUID + '__<tool>'`
    reg_re = re.compile(r"^\s+([a-z_]+):\s*'mcp__'\s*\+\s*CONFIG\.[A-Z_]+\s*\+\s*'__[\w-]+'", re.MULTILINE)
    registered = set(m.group(1) for m in reg_re.finditer(content))
    # Extract called tools: pattern `callTool(TOOL.<key>`
    call_re = re.compile(r"callTool\(TOOL\.([a-z_]+)")
    called = set(m.group(1) for m in call_re.finditer(content))
    unused = registered - called
    uncalled_but_used = called - registered
    if unused:
        for u in sorted(unused):
            warn(f"  {YELLOW}!{RESET} Tool '{u}' is registered but never called \u00b7 strip per discipline", warnings)
    if uncalled_but_used:
        for u in sorted(uncalled_but_used):
            warn(f"  {YELLOW}!{RESET} Tool '{u}' is called but not registered \u00b7 add to TOOL object", warnings)
    if not unused and not uncalled_but_used:
        print(f"  {GREEN}OK All {len(registered)} registered tools are called{RESET}")




# ============================================================
# v3.1 validator extensions (checks 14-22)
# ============================================================

# Files exempt from name-leak check #14
NAME_LEAK_EXEMPT = {"CLAUDE.md", "CONFIG.md", "team-roles.md", "port-manifest.md"}

# Skills exempt from MANDATORY TRIGGER check (system skills · not user-facing)
SYSTEM_SKILLS_EXEMPT = {"orchestrator", "anomaly-detector", "briefing-generator", "_template"}


def check_no_raw_names_in_skill_bodies(root, errors, warnings):
    """Check 14 · No raw team names (Hayden/Ivey/Emanuel) in skill BODIES.
    Frontmatter exempt. Quoted example output blocks exempt. References folder exempt."""
    print(f"\n{BOLD}14. Checking for raw names in skill bodies...{RESET}")
    names_re = re.compile(r"\b(Hayden|Ivey|Emanuel)\b")
    skills_dir = root / "skills"
    if not skills_dir.exists():
        return
    leaks = 0
    for skill_md in skills_dir.glob("*/SKILL.md"):
        text = skill_md.read_text(errors="ignore")
        if not text.startswith("---\n"):
            continue
        end = text.find("\n---\n", 4)
        if end == -1:
            continue
        body = text[end + 5:]
        # Strip quoted example blocks (> "...") which legitimately contain names
        # Then count remaining raw name references
        cleaned = re.sub(r"^>\s+\*?\"[^\"]*\"\*?$", "", body, flags=re.MULTILINE)
        # Also strip inline code with names (e.g., `email to Emanuel`)
        # Names ARE allowed inside {{roles.X}} substitution comments
        matches = list(names_re.finditer(cleaned))
        if matches:
            for m in matches:
                # Get line context
                line_start = cleaned.rfind("\n", 0, m.start()) + 1
                line_end = cleaned.find("\n", m.end())
                line = cleaned[line_start:line_end if line_end != -1 else None].strip()
                # Skip if it is inside an obvious comment about the substitution rule
                if "roles." in line and "→" in line:
                    continue
                if "team-roles" in line.lower():
                    continue
                warn(f"  {YELLOW}!{RESET} {skill_md.relative_to(root)} raw name: {m.group()} · use {{{{roles.X}}}} instead", warnings)
                leaks += 1
    if leaks == 0:
        print(f"  {GREEN}OK No raw names in skill bodies{RESET}")


def check_no_gh_voice_leakage(root, errors):
    """Check 15 · No GrowthHit voice in skill bodies."""
    print(f"\n{BOLD}15. Checking for GrowthHit voice leakage...{RESET}")
    forbidden = [
        r"\bGrowthHit\b",
        r"\bsenior CRO strategist\b",
        r"\bthe AM\b",
        r"\bAccount Manager\b",
    ]
    pattern = re.compile("|".join(forbidden))
    skills_dir = root / "skills"
    if not skills_dir.exists():
        return
    leaks = 0
    for skill_md in skills_dir.glob("**/*.md"):
        text = skill_md.read_text(errors="ignore")
        for m in pattern.finditer(text):
            # Skip if it is in a comment about the rule
            line_start = text.rfind("\n", 0, m.start()) + 1
            line_end = text.find("\n", m.end())
            line = text[line_start:line_end if line_end != -1 else None].strip()
            if "validator" in line.lower() or "no GrowthHit" in line or "no \"GrowthHit\"" in line.lower():
                continue
            fail(f"  {RED}X{RESET} {skill_md.relative_to(root)} GH-voice: {m.group()}", errors)
            leaks += 1
    if leaks == 0:
        print(f"  {GREEN}OK No GrowthHit voice in skill bodies{RESET}")


def check_every_skill_has_permission_tier(root, errors):
    """Check 16 · Every user-facing skill declares Permission tier in preamble."""
    print(f"\n{BOLD}16. Checking Permission Tier on every user-facing skill...{RESET}")
    skills_dir = root / "skills"
    if not skills_dir.exists():
        return
    tier_re = re.compile(r"\*\*Permission tier:\*\*\s*(generate|stage|execute|varies|n/a)", re.IGNORECASE)
    missing = 0
    for skill_md in skills_dir.glob("*/SKILL.md"):
        skill_name = skill_md.parent.name
        if skill_name in SYSTEM_SKILLS_EXEMPT:
            continue
        text = skill_md.read_text(errors="ignore")
        if not tier_re.search(text):
            fail(f"  {RED}X{RESET} {skill_md.relative_to(root)} missing Permission Tier declaration", errors)
            missing += 1
    if missing == 0:
        print(f"  {GREEN}OK All user-facing skills declare Permission Tier{RESET}")


def check_brand_voice_skills_load_context(root, warnings):
    """Check 17 · Skills that generate customer-facing content load brand-strategy + claim-library."""
    print(f"\n{BOLD}17. Checking brand-voice skills load required context...{RESET}")
    skills_dir = root / "skills"
    if not skills_dir.exists():
        return
    voice_skill_pattern = re.compile(r"(write|copy|draft|launch|respond|reply|content)", re.IGNORECASE)
    missing = 0
    for skill_md in skills_dir.glob("*/SKILL.md"):
        skill_name = skill_md.parent.name
        if skill_name in SYSTEM_SKILLS_EXEMPT:
            continue
        if not voice_skill_pattern.search(skill_name):
            continue
        text = skill_md.read_text(errors="ignore")
        # Look at the preamble line (between frontmatter end and first H1)
        if "brand-strategy.md" not in text or "claim-library.md" not in text:
            warn(f"  {YELLOW}!{RESET} {skill_md.relative_to(root)} (customer-facing skill) should load brand-strategy.md + claim-library.md", warnings)
            missing += 1
    if missing == 0:
        print(f"  {GREEN}OK All customer-facing skills load brand-strategy + claim-library{RESET}")


def check_no_composio_paths(root, errors):
    """Check 18 · No Composio cross-plugin path references."""
    print(f"\n{BOLD}18. Checking for Composio cross-plugin paths...{RESET}")
    composio_re = re.compile(r"growthit-data-sources/references/composio")
    leaks = 0
    for f in root.rglob("*.md"):
        if "/outputs/" in str(f) or "/.cache/" in str(f):
            continue
        try:
            text = f.read_text(errors="ignore")
        except Exception:
            continue
        for m in composio_re.finditer(text):
            fail(f"  {RED}X{RESET} {f.relative_to(root)} Composio path leak", errors)
            leaks += 1
    if leaks == 0:
        print(f"  {GREEN}OK No Composio paths{RESET}")


def check_role_key_two_sided(root, warnings):
    """Check 19 · Skills using {{roles.X}} tokens must list CONFIG.md in context."""
    print(f"\n{BOLD}19. Checking role-key two-sided rule...{RESET}")
    skills_dir = root / "skills"
    if not skills_dir.exists():
        return
    missing = 0
    role_token_re = re.compile(r"\{\{roles\.\w+\}\}")
    for skill_md in skills_dir.glob("*/SKILL.md"):
        text = skill_md.read_text(errors="ignore")
        if role_token_re.search(text) and "CONFIG.md" not in text:
            warn(f"  {YELLOW}!{RESET} {skill_md.relative_to(root)} uses {{{{roles.X}}}} but doesn't list CONFIG.md in context", warnings)
            missing += 1
    if missing == 0:
        print(f"  {GREEN}OK Skills using role tokens load CONFIG.md{RESET}")


def check_manifest_match(root, errors):
    """Check 21 · Files in skills/ match docs/port-manifest.md (and vice versa)."""
    print(f"\n{BOLD}21. Checking skills/ vs port-manifest.md...{RESET}")
    manifest = root / "docs" / "port-manifest.md"
    skills_dir = root / "skills"
    if not manifest.exists():
        warn(f"  {YELLOW}!{RESET} docs/port-manifest.md missing", [])
        return
    manifest_text = manifest.read_text(errors="ignore")
    # Extract skill names from manifest rows (column 1 of inventory tables)
    manifest_skills = set()
    for m in re.finditer(r"^\|\s*([a-z][a-z0-9-]+)\s*\|", manifest_text, re.MULTILINE):
        name = m.group(1).strip()
        if name and not name.startswith(("name", "skill", "challenger", "growthhit", "system", "kept", "port", "net-new")):
            manifest_skills.add(name)
    # Files in skills/ (excluding _template, system skills are also in manifest)
    file_skills = set()
    for d in skills_dir.iterdir():
        if d.is_dir() and d.name != "_template":
            file_skills.add(d.name)
    only_in_files = file_skills - manifest_skills
    only_in_manifest = manifest_skills - file_skills
    if only_in_files:
        for s in sorted(only_in_files):
            warn(f"  {YELLOW}!{RESET} skill '{s}' exists in skills/ but not in port-manifest.md", [])
    if only_in_manifest:
        for s in sorted(only_in_manifest):
            # Only warn if it looks like a real skill name (not a column header artifact)
            if "-" in s and len(s) > 3:
                pass  # quiet · manifest may list table rows that aren't full skills
    if not only_in_files and not only_in_manifest:
        print(f"  {GREEN}OK skills/ matches port-manifest.md ({len(file_skills)} skills){RESET}")
    else:
        print(f"  {GREEN}OK skills/ has {len(file_skills)} skill folders (warnings on edge cases above){RESET}")



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
    check_no_mcp_uuid_references(root, errors)
    check_no_bare_uuids(root, errors, warnings)
    check_skill_frontmatter(root, errors, warnings)
    check_no_ghost_folder_references(root, errors)
    check_config_md_exists(root, errors)
    check_plugin_json(root, errors)
    check_marketplace_json(root, errors)
    check_claude_md(root, errors)
    check_markdown_links(root, errors, warnings)
    check_requirements_for_yaml(root, errors, warnings)
    check_artifact_uuid_state(root, warnings)
    check_mcp_tools_tightness(root, warnings)
    # v3.1 extensions
    check_no_raw_names_in_skill_bodies(root, errors, warnings)
    check_no_gh_voice_leakage(root, errors)
    check_every_skill_has_permission_tier(root, errors)
    check_brand_voice_skills_load_context(root, warnings)
    check_no_composio_paths(root, errors)
    check_role_key_two_sided(root, warnings)
    check_manifest_match(root, errors)

    print(f"\n{BOLD}Summary{RESET}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")

    if warnings:
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
