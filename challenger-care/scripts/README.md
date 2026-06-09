# Scripts

Operational tooling for the Challenger Care plugin.

## Install

```bash
pip3 install -r scripts/requirements.txt
```

## Scripts

### `validate.py`
Migration discipline + format checks. Run before every commit.

```bash
python3 scripts/validate.py
```

Fails the run if anything violates discipline: hardcoded UUIDs, broken markdown links, ghost folder references, missing SKILL.md frontmatter, etc.

### `sync-html-config.py`
Pushes values from `CONFIG.md` into the dashboard HTML.

```bash
python3 scripts/sync-html-config.py            # apply CONFIG.md to dashboard
python3 scripts/sync-html-config.py --reset    # restore placeholders (run before commit)
```

The committed state of `artifact/command.html` always holds placeholders (`__SHOPIFY_UUID__`). Each teammate runs the script locally after pulling to wire up their MCPs.

### `voc-processor.py`
Processes a new JudgeMe CSV export from `assets/voc/exports/` into the structured outputs (`reviews-processed.json`, `theme-counts.json`, `quote-library.md`, etc.).

```bash
python3 scripts/voc-processor.py
```

Run when a fresh review export is dropped in.
