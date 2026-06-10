---
name: bing-ads
description: Microsoft Advertising setup, reporting, optimisation · Search, Shopping, PMAX-equivalent · Google Ads import + Bing-specific bid adjustments + LinkedIn profile targeting. Import from Google after Google launches. MANDATORY TRIGGER: any mention of "Bing Ads", "Microsoft Advertising", "Bing campaign", "Bing search ads", "Bing Shopping", "set up Bing", "import to Bing", "Bing optimisation". Do NOT use for: Google Ads campaigns. Meta Ads. Reporting only.
---

> **Permission tier:** execute · **Tools/context:** assets/goals-targets.md, assets/team-roles.md, CONFIG.md


# Bing Ads (Microsoft Advertising)

## What this skill does

Covers the full Bing Ads workflow for clients: importing campaigns from Google Ads, applying Bing-specific adjustments, reporting weekly performance, and running the monthly search term and bid optimisation review.

Bing is almost always run alongside Google — not instead of it. The workflow assumes Google campaigns already exist and Bing is the secondary channel.

Use this skill when:
- Launching Bing Ads for a client who already has Google Ads running
- Writing the weekly Bing performance update or Spend Tracker entry
- Running the monthly Bing search term review and optimisation
- The AM asks about Bing-specific differences in audience, performance, or setup

---

## Phase 1 — Context

Ask one question at a time:

1. **Client name** — who are we setting up or reporting on?
2. **What's needed?** — new account setup, weekly report, monthly optimisation, or a general Bing question?
3. **What's running on Google?** — which campaign types are live? (RSA Search, Shopping, PMAX) Bing setup mirrors Google.
4. **Has a Microsoft Advertising account been created yet?** — if not, start with account creation before importing.

---

## Phase 2 — Account Setup & Google Import

The fastest path to a working Bing account is importing directly from Google Ads. This takes 15–20 minutes and copies campaigns, ad groups, keywords, and ads with minor adjustments needed.

### Step 1: Create the Microsoft Advertising Account

- Go to [ads.microsoft.com](https://ads.microsoft.com) → Create account
- Account name: `[Client Name] — Challenger`
- Time zone: match Challenger's primary market
- Currency: match Challenger's billing currency
- Link Challenger's payment method before importing

### Step 2: Import from Google Ads

Microsoft Advertising → Tools → Import → Import from Google Ads

Import settings to apply:
- ✅ Import campaigns, ad groups, ads, keywords, negative keywords
- ✅ Import bid strategies (Bing will convert to its equivalents)
- ✅ Import ad extensions
- ❌ Do NOT auto-sync — import once and manage separately

After import: pause everything. Review before enabling.

### Step 3: Post-Import Adjustments

Bing is not a 1:1 copy of Google. Apply these adjustments after import:

| Item | Action |
|------|--------|
| Keyword match types | Bing's Broad Match behaves differently — review and tighten where needed |
| URLs | Confirm all final URLs are Bing-tracked (add UTM: `utm_source=bing&utm_medium=cpc`) |
| Bid amounts | Bing CPCs are typically lower — start bids at 80% of Google bids and adjust based on impression share |
| Ad copy | Bing ads copy from Google fine — no changes needed unless Google-specific language was used |
| Extensions | Re-verify all extensions are active — some don't import cleanly |
| Shopping feed | For Shopping campaigns: connect the Microsoft Merchant Center and verify product feed separately |

### Step 4: LinkedIn Profile Targeting (Bing-exclusive)

Bing's most powerful differentiator is LinkedIn profile targeting — unavailable on Google. Use it to layer on top of keyword targeting for B2B or professional audience clients.

Available targeting dimensions: Company, Industry, Job Function

- Add LinkedIn targeting at the ad group level
- Use as an **observation** layer first (bid adjustment, not restriction)
- Typical bid adjustment: +20–30% for high-value LinkedIn segments
- Use for: B2B, SaaS, high-AOV professional products (not for mass consumer eCommerce)

> For which clients should use LinkedIn profile targeting and recommended bid adjustments by segment, read `references/bing-playbook.md`.

---

## Phase 3 — Campaign Types

### Search Campaigns (RSA)

Bing Search works almost identically to Google Search. Key differences:

- **Audience skew:** Bing users are older (35+), higher income, more desktop-heavy. Adjust creative tone accordingly — less urgency, more considered.
- **CPCs:** Typically 20–40% lower than Google for the same keywords. More efficient for some verticals.
- **Match type behaviour:** Bing's broad match is less refined than Google's. Use Phrase and Exact match more aggressively, especially early.
- **Device split:** Bing traffic is significantly more desktop-weighted. Monitor device performance and apply mobile bid adjustments if mobile CPA is poor.

### Shopping Campaigns (eCommerce)

Microsoft Shopping requires a separate setup from Google Shopping:

1. Create a Microsoft Merchant Center account
2. Submit the product feed (can sync from a Google Merchant Center feed — use the Google Import option in Merchant Center)
3. Link Merchant Center to the Ads account
4. Create a Shopping campaign: select the product set, set a daily budget, start with Maximize Clicks bid strategy

> For Merchant Center setup steps and feed troubleshooting, read `references/bing-playbook.md`.

### Performance Max (Microsoft Equivalent)

Microsoft's equivalent to Google PMAX is **Smart Shopping** (for eCommerce) and **Performance Max** campaigns (rolling out). Treat the same as Google PMAX:
- Use after 30 days of regular campaign data
- Provide all asset types (images, headlines, descriptions, logos)
- Monitor asset group performance monthly

---

## Phase 4 — Weekly Reporting

Bing is reported as its own channel in the Spend Tracker, alongside Google and Meta.

**Metrics to pull from Microsoft Advertising (last 7 days):**

| Metric | Where to find |
|--------|--------------|
| Spend | Campaigns overview → Date: Last 7 days |
| Clicks | Same view |
| Conversions | Same view (ensure UET tag is firing correctly) |
| CPA | Cost ÷ Conversions |
| ROAS | Conv. value ÷ Cost (eCommerce only) |
| Impression Share | Competitive metrics column |

**Weekly Slack update format (Bing section):**

```
Bing Ads Performance
• Last 7 Days: [N] Purchases / $[X] CPA / [X] ROAS / $[X] spend
• Last 30 Days: [N] Purchases / $[X] CPA / [X] ROAS / $[X] spend
• Impression Share: [X]% (Lost to rank: [X]% / Lost to budget: [X]%)
```

Add Bing as a row in the Spend Tracker below Google. If Challenger uses the combined weekly Slack report automation (`ads-weekly-slack-report`), add a Bing section to their message template.

---

## Phase 5 — Monthly Optimisation

Run alongside the Google Ads monthly optimisation (`google-ads-optimization`). Cover:

### Search Term Review

Microsoft Advertising → Reports → Search Term Report

Apply the same GH Action Tag system used for Google:
- **High:** Add as exact match keyword
- **Mid:** Monitor for another 30 days
- **Low:** Add as negative keyword
- **Exclude:** Add as negative immediately

> For the full keyword classification system, read the Google Ads keyword research skill references — the same GH Action Tag framework applies.

### Bid Strategy Review

| Stage | Bid strategy | Threshold to advance |
|-------|-------------|---------------------|
| New account | Maximize Clicks | 30 conversions in 30 days |
| Growing | Maximize Conversions | 30 conv/month, stable CPA |
| Scaled | Target CPA | Set at actual CPA, lower gradually |
| eCommerce | Target ROAS | 30 conv/month, set below actual ROAS |

### Device Bid Adjustments

Check desktop vs. mobile vs. tablet CPA split monthly. Apply:
- If mobile CPA is 50%+ worse than desktop: apply -30% to -50% mobile bid adjustment
- If tablet CPA is poor (common on Bing): apply -20% to -40% tablet adjustment
- Bing traffic is desktop-heavy — typically desktop outperforms mobile on Bing

### LinkedIn Profile Targeting Adjustment (if active)

Review which LinkedIn segments are generating conversions vs. spend. Increase bid adjustment for top-converting segments (+25–40%). Remove or reduce underperforming segments.

---

## Phase 6 — Monthly Optimisation (continued)

*[Phases 2–5 completed. This phase concludes the monthly review cycle.]*

---

## Phase 7 — Synthesis Brief

Before delivering any report or completing any optimization review, write a brief summary for orchestrator handoff.

**Bing Ads Key Findings**
- **Account health score:** Impression share % and lost-to-budget/rank split. UET tag verified as active. Bid strategy stage matches account maturity (e.g., "30 conversions achieved — ready to advance to Maximize Conversions"). Note any device imbalance (mobile CPA vs desktop).
- **Performance vs. target:** Current CPA or ROAS with MoM change. Breakdown by campaign type if applicable (Search vs. Shopping vs. Performance Max equivalent). Call out which category is tracking ahead/behind target.
- **Top optimization move:** One specific, quantified action for next month — e.g., "Add 12 negative keywords from search term report (estimated $[X] CPA savings)", "Apply -35% mobile bid adjustment (mobile CPA 60% worse than desktop)", or "Test LinkedIn targeting on top 3 B2B segments (+25% bid adjustment)".

**Priority for downstream skills:** Name the next action: e.g., "Cross-apply Bing negative keywords to Google Search campaigns", "Review Performance Max asset performance if 30+ days live", or "Scale Bing spend by [%] pending next month's bid strategy advancement".

*If running standalone, share this with the operator before the full report.*

---

## Phase 8 — UET Tag Verification

Microsoft's Universal Event Tracking (UET) tag is the equivalent of the Google Ads conversion tag. Verify monthly:

1. Microsoft Advertising → Tools → UET Tags
2. Confirm status: Active
3. Check conversion actions: confirm they match the same events tracked in Google (purchases, leads)
4. If UET shows "Unverified" or "Tag inactive": use the Microsoft UET Helper Chrome extension to diagnose

**Common UET issues:**
- Tag fires on all pages but conversion action is misconfigured (wrong URL match)
- Google Tag Manager container has UET tag but it's not triggering on the conversion page
- Cross-domain tracking issues for multi-page checkouts

---

## Phase 9 — QA Gate

Before delivering any report or completing any setup:

- [ ] All phases completed in sequence
- [ ] UET tag verified as active and tracking conversions correctly
- [ ] All campaign URLs have Bing UTM parameters (`utm_source=bing&utm_medium=cpc`)
- [ ] Shopping feed connected and syncing (eCommerce clients only)
- [ ] Bid strategy matches the account maturity stage (advancement threshold reviewed, not left on Maximize Clicks indefinitely)
- [ ] Mobile and tablet bid adjustments applied if Bing CPA is device-imbalanced (>50% variance documented)
- [ ] LinkedIn profile targeting reviewed and bid adjustments set (B2B clients only)
- [ ] Search term negatives identified and added monthly (with specific keywords logged)
- [ ] Impression share and lost-to-budget/rank split documented
- [ ] Synthesis brief complete: account health score, performance vs. target by campaign type, top optimization move named with expected impact

---

## References

Read these files when the relevant phase is reached:

- **[Bing Playbook](./references/bing-playbook.md)** — Read during Phase 2 (LinkedIn targeting setup and bid adjustment recommendations) and Phase 3 (Merchant Center feed troubleshooting and Shopping campaign setup).
