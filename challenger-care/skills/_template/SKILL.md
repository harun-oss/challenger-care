---
name: skill-name-in-kebab-case
description: One sentence describing what this skill does for the Challenger Care team. MANDATORY TRIGGER any mention of [list 3-5 phrases]. Do NOT use for [list scenarios that should route to a different skill].
---

# Skill Title in Title Case

<!--
HOW TO USE THIS TEMPLATE:
1. Copy this folder · rename to your skill name in kebab-case
2. Replace every <placeholder> with real content
3. Run python3 ../../scripts/validate.py
4. Commit + push · skill installs on next Cowork sync

Migration discipline reminders:
- Never reference MCP UUIDs directly · pull from CONFIG.md
- Never write mcp__skills__* anywhere · breaks artifact import
- Reference knowledge files via relative paths · ../../assets/file.md
- Declare permission tier explicitly · drives who can run this
-->

## When to use this workflow

Describe the scenario where this skill should fire. Be specific. The orchestrator uses this to route requests.

## What you need

List the inputs the team should provide. Be explicit about optional vs required.

- Required input 1
- Optional input 2 — defaults to X if not provided

## What this produces

List every output file or artifact this skill creates.

1. **`output-1.md`** — Description
2. **`output-2.html`** — Description

All outputs land in `/outputs/<workflow-name>/` unless specified otherwise.

## How Claude runs it

Step-by-step what Claude actually does when this skill fires.

1. Load `../../assets/brand-strategy.md` for voice rules
2. Load `../../assets/claim-library.md` for what we can/can't say
3. Pull data from MCP tool (if applicable)
4. Generate output
5. Save to /outputs/

## Permission tier

**Generate / Stage / Execute** — pick one.

- **Generate** — drafts only, no live changes, anyone can run
- **Stage** — pre-loads into a tool, awaits approval
- **Execute** — live customer-facing OR money out · Hayden-only

Explain the contract: what changes, what's reversible.

## Example prompts that trigger this

- "Run the [skill name] workflow"
- "Typical phrasing the team would use"
- "Another phrasing"

## Don't use this for

- Scenario 1 → use `other-skill-name`
- Scenario 2 → use `other-skill-name`

## When to update this skill

- When brand voice evolves
- When a connected tool changes what's possible
- When team feedback surfaces a gap in the output
