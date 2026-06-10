# Bid Strategy Guide

Read this during Phase 4C of the Campaign Build skill for the full bid strategy decision framework.

---

## The Bid Strategy Progression Ladder

Google Ads bid strategies are not interchangeable. Each one requires a specific condition to work effectively. Jumping ahead causes poor performance; staying too long on an early-stage strategy leaves efficiency on the table.

```
Maximize Clicks
      ↓ (when: 30+ conversions in account)
Maximize Conversions
      ↓ (when: CPA stable over 60+ days, 30+ conversions/month)
Target CPA (tCPA)
      ↓ (eCommerce only: when revenue data is clean and ROAS stable)
Target ROAS (tROAS)
```

---

## Stage 1: Maximize Clicks

**Use when:** New account, or account with fewer than 30 total conversions.

**What it does:** Maximizes the number of clicks within the daily budget. Google adjusts bids in real time to get as many clicks as possible at the lowest available cost.

**Why start here:** Google's smart bidding strategies (Maximize Conversions, tCPA, tROAS) require conversion data to calibrate. On a new account with no conversion history, smart bidding has nothing to optimize toward. Maximize Clicks builds traffic volume and generates the first conversion data that smart bidding needs.

**Set a max CPC bid cap (optional but recommended):** In Maximize Clicks settings, you can set a maximum CPC. Without a cap, Google can bid very high for competitive keywords. Setting a cap prevents runaway spend on individual clicks. A reasonable starting cap: 2–3x the top-of-page bid high range for the most competitive keyword in the account.

**When to graduate:** When the account records 30+ conversions over a 30-day period. Don't wait for 30 in the current month — 30 total in the account is the threshold.

---

## Stage 2: Maximize Conversions

**Use when:** Account has 30+ conversions recorded; conversion tracking is confirmed working.

**What it does:** Uses machine learning to maximize the number of conversions within the daily budget. Google sets bids automatically for each auction based on the likelihood of conversion given the user's signals (device, location, time of day, search query, browsing behavior, etc.).

**Why this stage:** The algorithm now has enough data to understand what "a converting user" looks like for this specific account. It can start differentiating between high-probability and low-probability conversion traffic and bid accordingly.

**Transition process:**
1. Change bid strategy from Maximize Clicks to Maximize Conversions
2. Log the change in the change log with date and reason
3. Monitor closely for 2 weeks: impression share, conversion volume, CPA
4. Expected behavior: CPC may increase (algorithm is targeting higher-value clicks), but CPL/CPA should improve. If conversion volume drops significantly (>30% in the first week), check that conversion tracking is still recording correctly.

**When to graduate:** When CPA has been stable within ±15% for 4+ consecutive weeks and the account maintains 30+ conversions per month.

---

## Stage 3: Target CPA (tCPA)

**Use when:** Account has been on Maximize Conversions for 60+ days with stable CPA; 30+ conversions per month consistently.

**What it does:** Tells Google to optimize bids with the goal of achieving a specific cost per acquisition. The algorithm will adjust bids to get as many conversions as possible at or below the tCPA target.

**Setting the initial tCPA:**
- Pull the actual CPA from the last 60–90 days on Maximize Conversions
- Set tCPA at **actual CPA + 20%** — not at the aspirational target CPA Challenger wants
- Example: if actual CPA = $85, set initial tCPA = $102

**Why start at 120% of actual CPA:** If you set tCPA exactly at (or below) actual CPA immediately, the algorithm will restrict bids aggressively, causing impression share to drop and conversion volume to fall. A "safe" starting point gives the algorithm room to maintain volume while optimizing toward the target.

**Tightening process:**
- After 2 weeks at initial tCPA: if conversion volume is stable (within ±15%), reduce tCPA by $5–10
- Continue reducing every 2 weeks toward the target CPA
- If conversion volume drops >20% after a reduction: pause the reduction. Hold at current tCPA for 2 more weeks before trying again.

**Warning signs that tCPA is set too aggressively:**
- Impression share drops significantly (>20%) after switching to tCPA
- Campaign consistently underspends (spending <60% of daily budget)
- Conversion volume falls off sharply (the algorithm can't find qualifying traffic at the target CPC)

**Fix for over-aggressive tCPA:** Raise the target by $10–20. Log in change log. Monitor for 7 days.

---

## Stage 4: Target ROAS (tROAS) — eCommerce Only

**Use when:** eCommerce account with accurate purchase revenue tracking; ROAS has been stable over 60+ days on Maximize Conversion Value.

**What it does:** Optimizes bids to achieve a target return on ad spend (revenue ÷ ad spend × 100). The algorithm focuses on high-revenue transactions, not just conversion volume.

**Prerequisite:** Revenue must be passing correctly as conversion value in Google Ads. If the account is recording conversions with a fixed placeholder value (e.g., $1 per lead), tROAS cannot work — it needs real revenue data.

**Setting the initial tROAS:**
- Pull actual ROAS from the last 60–90 days
- Set tROAS at **actual ROAS × 80%** (20% below actual) — same principle as tCPA: give the algorithm room to maintain volume before tightening
- Example: if actual ROAS = 500%, set initial tROAS = 400%

**Tightening process:** Increase tROAS target by 10–20% every 2–3 weeks toward Challenger's goal, as long as revenue volume remains stable.

---

## Troubleshooting Common Bid Strategy Problems

### "My Maximize Conversions campaign is underspending"
- Check conversion tracking — is it recording correctly? Maximize Conversions without valid conversion data may restrict spend
- Check if tCPA is set within the campaign settings (some accounts accidentally set tCPA inside Maximize Conversions) — remove any CPA targets if the goal is pure volume

### "I switched to tCPA and conversion volume collapsed"
1. Check: is conversion tracking still working? Sometimes a GTM publish or site change breaks tracking simultaneously with a bid strategy change
2. If tracking is working: the tCPA target is too aggressive. Raise by 30% immediately. Log the change.
3. If raising tCPA doesn't restore volume within 7 days: revert to Maximize Conversions and rebuild conversion history

### "tCPA is set but the campaign is overspending the target"
- tCPA is a target, not a cap. Google guarantees it will try to hit the target on average, not on every individual conversion. If actual CPA is running 10–20% above target: normal fluctuation. If running >30% above target consistently: the target may be unachievable with current keyword set, landing page, and bid competition.
- Check: is the tCPA target below the absolute floor (minimum CPC × required click volume to generate a conversion)? If so, the math doesn't work and the target needs to be raised.

### "Smart bidding is working but I want to reduce budget — will it break?"
Reducing budget on a smart bidding campaign by >30% in a single change can trigger a "learning period" — the algorithm recalibrates to the new budget constraint, temporarily reducing performance. If budget cuts are necessary:
- Reduce in steps: no more than 20–30% reduction per week
- Log each reduction in the change log
- Monitor conversion volume for 2 weeks after each reduction
