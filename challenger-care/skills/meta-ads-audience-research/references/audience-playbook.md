# Meta Ads Audience Playbook

## Customer Profile Framework

The more precisely you understand who the customer is, the better your interest selection and the sharper your creative brief. This framework produces a one-page customer profile that feeds directly into Phase 3 (interest selection) and the meta-ads-creative-brief skill.

### Full Customer Profile Questions

Work through these with the operator. One question at a time — don't present the full list.

**The problem and trigger:**
- What specific problem does this product solve, or what desire does it fulfill?
- What happens in the customer's life right before they would buy this product? (The trigger moment)
- How aware are they that this product exists before they see the ad? (Unaware / problem-aware / solution-aware / product-aware)

**Who they are:**
- Age range and life stage? (Student / young professional / parent / retiree)
- What's their relationship with money? (Value-focused / convenience-focused / quality-focused / status-focused)
- Urban, suburban, or rural?

**What else they buy:**
- Name 3 other brands this customer likely buys from. Why those brands?
- What subscription services might they use? (Amazon Prime / Headspace / Peloton / etc.)
- What do they spend discretionary income on?

**Where they spend time:**
- What media do they consume? (Podcasts, YouTube channels, Instagram accounts, newsletters)
- What communities are they part of? (Online forums, Facebook groups, associations, gyms)
- What apps are on their phone besides social?

**What moves them:**
- Price vs. outcome vs. identity: Do they buy based on cost, on the result they'll get, or on who it makes them feel like?
- What would make them trust this brand enough to buy without a review?
- What objection would stop them from buying?

---

## Interest Selection — Vetting Process

After the customer profile is complete, generate 6–10 interest candidates. Then vet them using this process before finalising.

### Step 1: Generate Candidates

From the customer profile, identify:
- **Direct category interests:** The product category itself and adjacent categories
- **Brand interests:** Competitor brands and complementary brands the customer buys
- **Lifestyle interests:** What the customer does, reads, watches, or belongs to
- **Aspirational interests:** Who they want to be or how they want to be seen

### Step 2: Vet in Ads Manager

For each candidate interest:
1. Search the interest in Ads Manager → Ad Set → Audiences
2. Check estimated reach (targeting US only): aim for 3–10M
3. Note the interest size — very large interests (30M+) may be too diffuse; very small ones (<500K) are too narrow
4. Check if the interest exists at all — many intuitive interests don't exist in Meta's library

### Step 3: Select 2–3 Finalists

Pick one from each category:
- 1 broad lifestyle or direct category interest (your baseline)
- 1 brand or community interest (more specific signal)
- 1 aspirational or adjacent interest (for testing)

These become three separate ad sets — one interest per ad set. Do not combine them.

### Step 4: Prioritise if Budget is Tight

If only one ad set is possible (budget under $20/day), choose the interest that:
- Best matches the customer's primary motivation (not their demographics)
- Has a reach of 3–8M
- Is a lifestyle or behaviour signal rather than a direct category (the algorithm narrows from lifestyle better than from category)

---

## Common Interest Mistakes by Vertical

### eCommerce — Apparel / Fashion
❌ "Clothing" — too broad, includes everyone
❌ Brand interest matching Challenger's own brand — you're already targeting people who know them
✅ Complementary brands at similar price point
✅ Lifestyle signals: "Sustainable fashion", "Outdoor lifestyle", "Yoga"

### eCommerce — Health / Wellness / Supplements
❌ "Health and wellness" — 50M+ reach, no signal
❌ "Vitamins and supplements" — Meta audience is too broad
✅ Specific condition or goal: "Running", "Weight training", "Gut health" (if exists)
✅ Media the customer reads: "Men's Health", "Women's Health", "Healthline"
✅ Adjacent brands: specific supplement or fitness brands

### eCommerce — Home Goods
❌ "Home decor" — too broad
✅ Complementary retailers: "West Elm", "Crate and Barrel", "Article"
✅ Life stage trigger: "New homeowner", "Interior design"
✅ Lifestyle: "Minimalism", "Sustainable living"

### Lead Gen — B2B / SaaS
❌ Job titles as interests — Meta interest targeting ≠ LinkedIn. Job titles on Meta are unreliable.
✅ Software brands the prospect uses: "Klaviyo", "Salesforce", "Slack"
✅ Business media: "Inc.", "Entrepreneur", "Fast Company"
✅ Industry associations or events if they exist in Meta's library

### Lead Gen — Local Services
❌ Geographic interest (use geo targeting at the campaign level instead)
✅ Trigger life event: "Recently moved", "New homeowner" (if applicable)
✅ Problem signal: if the service is for a specific life situation
✅ Keep the interest very broad — rely on geography as the primary constraint

### Lead Gen — Health / Wellness Services
✅ Condition-specific if the service addresses a specific condition (approach carefully — Meta health-related targeting restrictions apply)
✅ Life stage: "Parents of young children", "Retired persons"
✅ Lifestyle: what the ideal patient or client does outside of the health context

---

## Lookalike Audience — Seed Quality Guide

| Seed | Recommended size | Quality notes |
|------|-----------------|---------------|
| Purchasers — last 90 days | 500–5,000 ideal | Freshest signal. Prioritise this. |
| Purchasers — all time | 5,000+ | Good for large accounts. Can dilute with old buyers. |
| High-LTV purchasers (top 25%) | 200+ | Needs segmentation from CRM or Klaviyo export |
| Email list — all customers | 500+ matched | Match rate typically 40–60%. Upload as CSV. |
| Email list — VIP / repeat buyers | 200+ matched | Higher quality than full list |
| Add-to-cart, no purchase (180 days) | 1,000+ | Intent signal but noisy. Use only if purchase data is thin. |
| All website visitors (180 days) | 10,000+ | Weakest. Use only at early stage with no other option. |

**Minimum seed size for a reliable LAL:** 100 matched users. Below this, Meta will still create the LAL but quality degrades significantly.

**Refresh cadence:** Rebuild lookalikes every 90 days using the most recent cohort. Stale seeds (purchasers from 12+ months ago) produce lower-quality LALs as customer profiles shift.

---

## Exclusion Audience Setup — Step by Step

### 1. Recent Purchasers (Pixel)
- In Ads Manager: Audiences → Create Audience → Custom Audience → Website
- Event: Purchase
- Time window: Last 30 days
- Name: `[Client] | Purchasers | Last 30 Days`
- Apply as exclusion to: All prospecting campaigns

### 2. Customer Email List
- In Ads Manager: Audiences → Create Audience → Custom Audience → Customer List
- Upload: CSV with email column
- Name: `[Client] | Customer List | [Upload Date]`
- Note: Update this list every 90 days. Old lists go stale.
- Apply as exclusion to: All prospecting campaigns

### 3. Retargeting Overlap
- If running a separate DPA or retargeting campaign:
  - Create: Website visitors, last 30 days
  - Name: `[Client] | Website Visitors | Last 30D`
  - Apply as exclusion to: Prospecting campaign
  - Apply as inclusion to: Retargeting campaign

### 4. Engaged Non-Converters (Optional)
- For accounts with high traffic but lower conversion rate: build a custom audience of engaged non-buyers (add-to-cart + no purchase, last 30 days) and use as a separate retargeting ad set with a specific offer or objection-handling creative.

---

## Audience Saturation Diagnosis

When performance declines, distinguish creative fatigue from audience saturation before making any changes:

| Symptom | More likely cause | First action |
|---------|-----------------|-------------|
| CTR declining, CPA rising, reach stable | Creative fatigue | New creative first |
| Frequency above 3.5, reach declining | Audience saturation | Expand or refresh audience |
| CPA rising, frequency normal, reach normal | Creative fatigue or offer issue | Test new offer or hook |
| All metrics declining suddenly | Algorithm disruption | Check for tracking issues, budget changes, or platform events |

**Rule:** Always rule out creative fatigue before changing the audience. They look identical. The test: launch a completely new creative with the same audience. If the new creative performs well, it was fatigue. If it still underperforms, it's the audience.
