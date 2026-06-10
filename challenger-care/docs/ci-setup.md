# CI Setup · One-Time Manual Step

The plugin includes CI definitions in `.github/workflows/` that must be added
to the repo manually because the GitHub PAT used during the port doesn't have
`workflow` scope.

## Two paths to land CI

### Path A · Add workflow scope to the PAT (5 seconds, recommended)

1. GitHub → Settings → Developer settings → Personal access tokens
2. Find the token used for this repo
3. Edit → check the `workflow` scope checkbox → Save
4. Re-run the push from this session

### Path B · Copy the files via GitHub web UI

Two files need to be added to the repo:

#### `.github/workflows/validate.yml`

Runs on every PR. Three jobs:
1. Validator (all 20 checks)
2. Sync-workflows + dashboard drift check (when skills/manifest change)
3. Path-based merge gate (auto-merge config/assets/docs · require approval on skills/scripts/artifact)

The full YAML is checked into the GrowthHit working session output.

#### `.github/workflows/README.md`

Explains the CI policy + branch protection recommendations.

## Branch protection settings (set in GitHub UI after CI is added)

Settings → Branches → main → Add rule:
- Require pull request before merging
- Require status checks: `validate`, `merge-gate`
- Require approvals: 1 (for PRs that touch skills/scripts/artifact)
