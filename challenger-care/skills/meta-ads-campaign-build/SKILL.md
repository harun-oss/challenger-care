---
name: meta-ads-campaign-build
description: 'Stands up the Meta Ads account structure - 1-2 campaigns, DCT/Flexible Ads ad sets, DPA retargeting, ADV+ setup, pixel training, Canva creative workflow, ad creative overview for review. MANDATORY TRIGGER: any mention of "build Meta Ads campaign", "set up Meta Ads", "stand up Meta", "DCT setup", "Meta campaign structure", "first Meta campaign". Do NOT use for: Account onboarding/BM access (one-time, done). Weekly creative testing cadence (use `meta-ads-creative-testing`). Scaling decisions (no skill - single rule).'
---

> **Permission tier:** execute · **Tools/context:** assets/brand-strategy.md, assets/claim-library.md, assets/customer-archetypes.md, assets/voc/quote-library.md, assets/unit-economics.md, assets/team-roles.md, CONFIG.md


# Meta Ads Campaign Build

**Owner:** the operator
**Timeline:** Week 2–3, after kickoff deliverables are complete and pixel is verified
**Prerequisite:** Tracking audit complete, pixel verified, value prop exercise complete (messaging angles available)

---

## Phase 1: Pre-Build Confirmation

Before building anything, confirm:

| Check | Status |
|---|---|
| Pixel verified and firing correctly | ✓ / ✗ |
| Primary conversion event confirmed (Purchase or Lead) | ✓ / ✗ |
| Value prop exercise complete (messaging angles available) | ✓ / ✗ |
| Monthly budget confirmed | ✓ / ✗ |
| Canva access confirmed (Jim's account) | ✓ / ✗ |

**Hard stop if pixel is not verified.** Do not run campaigns without confirmed conversion tracking — you will waste budget and train the algorithm incorrectly.

Ask the operator:
1. What is Challenger's monthly budget?
2. What is the primary conversion event? (Purchase value? Lead value?)
3. eCommerce or Lead Gen?
4. Do we have initial creative ready (from value prop exercise / brand assets)?

---

## Phase 2: Account Structure Setup

> For the full campaign structure rationale and when to deviate from the standard setup, read `references/campaign-structure-guide.md`.

Challenger's standard structure:

**Main Campaign (always)**
- Objective: Conversions (Purchase or Lead — must match pixel event)
- 1 campaign maximum for the first 90 days (concentrate all signal here)
- Ad sets inside: DCT/Flexible Ads ad sets (one per experiment + legacy winners)

**DPA Campaign (eCommerce only, launch at 30+ days)**
- Objective: Catalogue Sales
- Budget: ~10% of total monthly budget
- Audience: Website visitors (add to cart, view content, all website visitors)
- Requires: Catalogue set up and synced to Ads Manager

**ADV+ Campaign (launch at 60–90 days)**
- Objective: Advantage+ Shopping Campaign
- Budget: ~10–15% of total monthly budget
- Use: Give a second life to DCT creative that underperformed in the main campaign
- Requires: Minimum Pixel data (50+ purchases/month) and a library of tested creative

**What the structure is NOT:**
- No campaign per audience segment
- No campaign per product category (unless completely different KPIs)
- No campaign per geography (use ad set level targeting or reporting breakdown)

---

## Phase 3: Synthesis Brief

Document the campaign structure for the handoff. This is used when handing off to the operator for creative development and for internal reference.

**[Client Name] Campaign Build Summary**
- Account structure: specific structure deployed. Example: "1 main campaign (Conversions objective) + DPA campaign at 30+ days. CBO enabled for optimal budget distribution"
- DCT configuration: specific configuration with permutation count. Example: "4 images × 3 headlines × 2 primary texts = 18 permutations (meets ≤20 limit). Naming: Client | Meta Exp #1 | April | Ads Variety"
- Pixel status: specific pixel health status. Example: "Verified and firing correctly on Purchase event with value + currency parameters"
- Next step: specific next action. Example: "Creative development and execute_tier_approver approval via Ad Creative Overview deck before launch"

*Share this summary with the operator for creative development handoff.*

---

## Phase 5: Main Campaign Build

### Campaign-Level Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Campaign objective | Conversions | Always — do not use Traffic or Reach for performance campaigns |
| Campaign budget optimisation (CBO) | On (Advantage+ budget) | Lets Meta distribute budget across ad sets |
| Budget | Full monthly budget ÷ 30 × daily | Start with daily budget |
| Campaign spending limit | Optional | Set if client has hard monthly cap |
| Special ad categories | Off | Only enable if legally required (housing, credit, employment, social issues) |

### Ad Set-Level Settings

**For each DCT ad set:**

| Setting | Recommended Value |
|---|---|
| Conversion event | Purchase (eCommerce) or Lead (Lead Gen) |
| Targeting | Broad (no detailed interests unless brand new pixel) |
| Placement | Advantage+ Placements (automatic) |
| Optimisation goal | Conversions |
| Attribution window | 7-day click, 1-day view |
| Minimum budget | $10/day per DCT ad set |

**Audience note:** Start with Advantage+ Audience (broad) once the Pixel has 200+ monthly events. For new pixels: use 1–2 broad interest categories as a guide but still keep the audience large (3M+ potential reach).

---

## Phase 6: DCT / Flexible Ads Setup

> Before building the first DCT, read `references/dct-build-guide.md` for the full step-by-step build process, creative specifications, and naming conventions.

DCT (Dynamic Creative Testing) / Flexible Ads lets Meta automatically find the best combinations of headlines, primary texts, and images/videos.

**First DCT — initial launch:**

Components:
- **Images or videos:** 3–5 assets (from value prop exercise or brand assets)
- **Headlines:** 1 control (best known hook or brand tagline) + 2 new options to test
- **Primary texts:** 1 control + 2 new options
- **CTAs:** 1 CTA (keep consistent — usually Shop Now or Learn More)

**Permutation check (critical):**
Permutations = Headlines × Primary Texts × Images/Videos
- Example: 3 headlines × 3 primary texts × 4 images = **36 permutations**
- Maximum allowed: **20 permutations per DCT ad set**
- If over 20: reduce image/video count first, then reduce headline/text options

**Naming convention:**
`[Client] | Meta Experiment #[N] | [Month] | [Type]`
Example: `Oaktree | Meta Experiment #1 | April | Ads Variety`

---

## Phase 7: Creative in Canva

All ad creative is built inside **Canva Pro** on the account (Jim's access).

> For creative specifications by placement type, read `references/dct-build-guide.md`.

**Creative brief to designer:**
Use the Ad Creative Overview deck to brief the designer and present to Challenger for approval before going live.
Template: [[Template] - Ad Creative Overview](https://docs.google.com/presentation/d/1FIZl6mf46S8n-YHtYLPZhbg3RDBKPk0lBpy-STTn_C8/edit)

**Client approval step (required before launching any new creative):**
Never launch new creative without execute_tier_approver sign-off. Send the Ad Creative Overview deck to Challenger and wait for approval. Aim for 48-hour turnaround.

---

## Phase 8: Output Format + Branding

> "Campaign build complete. What format would you like for the setup summary?
>
> 1. **DOCX Report** — written campaign setup summary with account structure, DCT configuration, permutation count, and launch checklist
> 2. **Creative brief** — structured brief for the Ad Creative Overview deck to send to the designer/client for approval
> 3. **Verbal summary** — confirm the setup in this conversation"

> "branding, or client-specific? If Challenger, I'll pull from the brand file. If client-specific, share their colours and logo."

If branding: read `../../../growthit-brand/assets/growthit-brand.md` for exact colours, fonts, and layout rules before building.

Build based on chosen format:
- **DOCX** → invoke the docx skill; apply branding; include: account structure diagram → campaign settings → DCT configuration → permutation count → launch checklist
- **Creative brief** → formatted brief for Ad Creative Overview: campaign context, ad format specs, creative direction notes

---

## Reference Files

This skill uses reference materials. The orchestrator will locate and load these automatically via Glob.

- `references/campaign-structure-guide.md` — Full rationale for the standard campaign structure (main campaign, DPA, ADV+), when to deviate, and tier-specific guidance. Needed during Phase 2 before setting up the account structure.
- `references/dct-build-guide.md` — Complete step-by-step DCT setup process, creative specifications by placement type, naming conventions, and permutation calculations. Needed during Phase 6 before building the first DCT.

---

## Pre-Launch Checklist

Before going live:
- [ ] Pixel verified and firing on the correct conversion event
- [ ] Campaign objective set to Conversions (not Traffic, not Reach)
- [ ] CBO enabled — budget flowing to campaign level
- [ ] DCT permutations ≤ 20 per ad set
- [ ] Naming convention applied correctly
- [ ] Creative reviewed and approved by client via Ad Creative Overview deck
- [ ] Payment method confirmed active in Ad Account
- [ ] Attribution window: 7-day click, 1-day view
- [ ] DPA campaign set up (if eCommerce and catalogue synced)
- [ ] Synthesis brief written (if in an orchestrated chain)
