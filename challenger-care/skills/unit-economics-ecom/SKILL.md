---
name: unit-economics-ecom
description: 'Builds the full acquisition economics model - CM1/CM2/CM3 stack, LTV at 90/180/365 days, max CPA scenarios. Pairs with `model-unit-economics` (the Challenger-tuned production version). This is the consulting-grade deep dive. MANDATORY TRIGGER: any mention of "consulting-grade unit economics", "full CM stack", "deep unit economics", "max allowable CPA", "MACPA", "break-even ROAS", "contribution margin stack", "consulting-grade LTV model". Do NOT use for: Quick Challenger-tuned unit economics (use `model-unit-economics`). B2B / lead gen (different math). Ad performance reporting.'
---

> **Permission tier:** generate · **Tools/context:** assets/unit-economics.md, assets/goals-targets.md, assets/team-roles.md, CONFIG.md


# Unit Economics — E-Commerce / DTC

Builds a complete acquisition economics model for a DTC or e-commerce brand.
Produces a formatted report the operator can share directly with Challenger.

Read `references/ecom-framework.md` for all formulas, benchmarks, and intake
questions before running the model. Read `references/scenario-output.md` for
the exact output format before writing the deliverable.

---

## Workflow

### Step 1 — Collect Client Inputs

Read `references/ecom-framework.md` → Section: Client Intake for the full
question set. Minimum viable inputs are: **AOV, gross margin %, current CPA**.
Everything else sharpens accuracy but is not blocking.

**Intake principles:**
- Accept approximate values ("roughly 60%") and flag them with "~" in output
- If a data point is missing, use category benchmarks from
  `references/ecom-framework.md` → Gross Margin Benchmarks and label them
  `[benchmark]`
- Never skip gross margin — it is the foundation of every downstream number

**Flag and stop if:**
- Gross margin reported as 0% or >90% — almost always markup vs. margin
  confusion, or COGS missing freight/duties. Clarify before proceeding.
- AOV equals the single product price on a multi-SKU store — this is likely
  single-product thinking, not blended AOV. Ask for clarification.

---

### Step 2 — Run the Diagnostic

Before modeling scenarios, show Challenger where they stand today. This earns
credibility and sets the baseline.

1. Calculate CM1: `AOV × Gross Margin %`
2. Subtract variable fulfillment costs (shipping, payment fees, returns
   reserve) → CM2. Use benchmarks from `references/ecom-framework.md` →
   Variable Cost Benchmarks if actuals are not provided.
3. Subtract current CPA → CM3
4. Identify their current scenario:
   - CM3 > 0: first-purchase profitable
   - CM3 ≈ 0: break-even
   - CM3 < 0: loss leader (intentional or not)
5. Calculate break-even ROAS: `1 ÷ Gross Margin %`

Present this as "Here is where you are today" before moving to scenarios.

---

### Step 3 — Model the Three Scenarios

Read `references/ecom-framework.md` → Section: Scenario Calculations for
the exact formulas. Calculate and present all three:

**Scenario A — First-Purchase Profitable**
Maximum CPA to generate profit on order 1. Calculate implied minimum ROAS.
Flag if this CPA is achievable given category and channel benchmarks.

**Scenario B — Break-Even on Order 1**
Maximum CPA to break even without any LTV assumption. This is the floor for
sustainable spend.

**Scenario C — Loss Leader with LTV Upside**
Calculate for 90-day, 180-day, and 365-day horizons:
- LTV-adjusted max CPA at each horizon
- Repeat purchase rate required to justify this CPA
- Retention infrastructure required (email flows, SMS, subscription)

**Decision gate for Scenario C — flag clearly if:**
- No cohort data exists → label all LTV figures `[projected, not validated]`
- No retention infrastructure in place (email flows, subscription, loyalty)
- Payback period exceeds client's capital runway

---

### Step 4 — LTV Horizon Projections

Model 90d, 180d, and 365d cumulative LTV using Challenger's actual repeat
purchase rates or benchmarks from `references/ecom-framework.md` → LTV
Benchmarks. Show how the economics improve (or don't) over each horizon.

Always label clearly:
- **Validated** — based on Challenger's actual cohort data
- **Projected** — based on category benchmarks or formula

---

### Step 5 — Deliver the Output

Read `references/scenario-output.md` for the exact template before writing.

**Before delivering, run this QA check:**
1. Every metric shows its formula, not just the number
2. Every benchmark-derived input is labeled `[benchmark]`
3. Scenario C includes the warning block if cohort data or retention
   infrastructure is absent
4. The recommended scenario has a specific rationale — not a default to C
5. Output reads cleanly for a client — no internal notes or jargon

Write in plain language. Avoid agency jargon. Use Challenger's own language
where possible. The output should be passable directly to Challenger.

---

## Quality Rules

- **Never invent a gross margin.** Use the category benchmark and label it.
  A wrong gross margin invalidates every number downstream.
- **Scenario C always needs a warning block** if cohort data is absent.
  Do not present it as a clean recommendation without this.
- **Show the math.** Every calculated figure includes the plain-English
  formula so Challenger can verify and update with their own numbers.
- **The recommendation is not always C.** For brands without email
  automation or repeat purchase history, Scenario A or B is the right
  call even if C looks attractive on paper.

---

## Files in This Skill

```
unit-economics-ecom/
├── SKILL.md                 ← this file
└── references/
    ├── ecom-framework.md    ← formulas, benchmarks, intake, scenario calcs
    └── scenario-output.md   ← exact output format and client-ready template
```
