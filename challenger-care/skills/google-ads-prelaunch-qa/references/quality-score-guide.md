# Quality Score Optimization Guide

Read this during Phase 6 of the Pre-Launch QA skill when any Quality Score component is rated "Below average."

---

## What Quality Score Measures

Quality Score (1–10) is Google's estimate of the relevance and quality of your keyword, ad copy, and landing page, relative to competitors bidding on the same keyword.

It is composed of three components, each rated Above average / Average / Below average:

| Component | Weight | What it measures |
|-----------|--------|-----------------|
| Expected CTR | Highest | Will searchers click your ad when they see it, compared to similar ads? |
| Ad Relevance | Medium | How closely does your ad copy match the intent of the keyword? |
| Landing Page Experience | Highest | How useful and relevant is the landing page to a user who clicked your ad? |

**Why Quality Score matters (quantified):**

benchmark: accounts where both Landing Page Experience and Ad Relevance are "Above average" show:
- **750% better conversion rate** vs accounts with "Below average" on both
- **36% lower CPC** — Google rewards relevance with lower costs

A keyword with Quality Score 10 pays up to 50% less per click than a competitor with Quality Score 5 bidding on the same keyword. Quality Score is a direct cost lever.

---

## Component 1: Expected CTR

**What "Below average" means:** Google predicts that your ad is less likely to get clicked than competitor ads for the same keyword, based on historical CTR data for similar ads.

**Why it happens:**
- Ad copy is too generic — doesn't speak to the specific intent behind the keyword
- No clear value proposition in the headline
- Competitor ads are more compelling, specific, or offer-forward
- The ad shows irrelevant headlines in the top positions (Headline 1 not pinned to keyword)

**How to fix:**

1. **Review competitor ads on the same SERP:** Google the target keyword in an incognito window. What do competitor ads lead with? Is there a stronger offer, a more specific benefit, or a trust signal you're missing?

2. **Make Headline 1 more specific:**
   - Generic: "Professional HVAC Service"
   - Specific: "Emergency HVAC Repair Minneapolis — Same Day"
   The second version immediately signals relevance to someone searching "emergency HVAC repair Minneapolis."

3. **Add a compelling offer to Headline 2:**
   - "Free Estimates", "No Fee Unless You Win", "Free 14-Day Trial" — these improve CTR by reducing the risk of clicking

4. **Pin Headline 1 to the most keyword-specific headline.** If Headline 1 rotates freely, generic phrases may appear in the most prominent position, reducing CTR.

5. **Test a different lead angle:** If "professional + service + city" isn't working, try leading with an outcome or a pain removal headline.

---

## Component 2: Ad Relevance

**What "Below average" means:** The ad copy doesn't closely match the keyword's intent. Google can't see a strong connection between what the user searched and what the ad says.

**Why it happens:**
- Ad group has too many different keyword intents — the ad can't be relevant to all of them
- Headline 1 doesn't contain the target keyword or a close variant
- The ad was written for a related but different ad group and copied over without editing
- The keyword and the ad group theme are misaligned (a keyword snuck into the wrong ad group)

**How to fix:**

1. **Verify Headline 1 contains the target keyword:**
   - If the ad group is "emergency HVAC repair Minneapolis", Headline 1 must say something like "Emergency HVAC Repair Minneapolis" or "Minneapolis Emergency HVAC Repair"
   - Close variants are acceptable: "Emergency AC Repair Minneapolis" for a keyword "emergency HVAC Minneapolis" — Google understands AC = HVAC in this context
   - Pure rewording that drops the keyword is not sufficient

2. **Check the ad group keyword theme:**
   - Run an audit of all keywords in the ad group
   - Are all keywords asking for the same thing? If there are keywords with different intents (e.g., "emergency HVAC repair" and "HVAC maintenance contract" in the same ad group), the ad can't be relevant to both
   - Move mismatched keywords to their own ad group with a dedicated RSA

3. **Review all 15 headlines:**
   - Are most headlines related to the keyword theme?
   - Generic filler headlines (e.g., "High Quality Service", "We're Here to Help") don't contribute to ad relevance
   - Replace with keyword-adjacent headlines: benefit statements, features, or proof points that reinforce the keyword's topic

---

## Component 3: Landing Page Experience

**What "Below average" means:** Google's crawlers and user behavior signals indicate that users who click the ad don't find the landing page useful, relevant, or easy to navigate.

**Why it happens:**
- The landing page doesn't mention the keyword or service in a prominent position
- Ad says "Emergency Plumber" → landing page is the generic homepage with no emergency plumbing content visible
- The landing page is slow to load on mobile
- The landing page doesn't have a clear, accessible CTA matching the ad's promise
- The landing page content is thin, hard to navigate, or appears low-quality to Google's systems

**How to fix:**

1. **Message match — top of page:**
   - The landing page H1 or banner headline should reflect the same language as the ad's Headline 1
   - Ad: "Emergency HVAC Repair Minneapolis" → Landing page H1: "Emergency HVAC Repair in Minneapolis — Available 24/7"
   - The searcher should instantly recognize they're in the right place after clicking

2. **Page speed:**
   - Test with Google PageSpeed Insights (pagespeed.web.dev)
   - Mobile score below 50 is a significant landing page experience signal issue
   - Common fixes: compress images, remove render-blocking scripts, enable caching
   - If the site is slow and Challenger's dev team can't fix it quickly: use a faster dedicated landing page for Google Ads traffic

3. **CTA visibility and alignment:**
   - The CTA on the landing page must be prominent and above the fold on mobile
   - It must match what the ad promised: if the ad says "Get a Free Quote", the landing page needs a visible free quote form, not a generic "Contact Us" link buried at the bottom
   - Users don't scroll — if they can't see a way to convert immediately, they bounce

4. **Content relevance:**
   - The landing page should have substantive content about the specific service advertised
   - Sending a "commercial HVAC repair" ad to a generic homepage with 5 different services mentioned gets flagged as low relevance
   - Dedicated landing pages per major ad group consistently outperform generic homepages for landing page experience scores

5. **Mobile-first design:**
   - Google's primary landing page assessment is mobile
   - Verify the page renders correctly on a smartphone: no overlapping elements, no tiny text, buttons are tappable, forms work on mobile keyboard

---

## Quality Score by Match Type

Quality Score is calculated per keyword, not per ad or per campaign. Exact match keywords typically have higher Quality Scores than phrase or broad match because the intent is more precisely known.

When a keyword has a low QS (≤4), check:
- Is this the right keyword for this ad group?
- Is the exact match version of this keyword performing differently from the phrase match version?
- Has this keyword had enough impressions to generate a real Quality Score, or is it based on limited data?

**Minimum impressions for reliable Quality Score:** Google needs approximately 500+ impressions to calculate a statistically meaningful Quality Score. Newly launched keywords or very low-volume keywords may show a QS based on limited data that doesn't reflect true quality.

---

## Pre-Launch Quality Score Reality Check

Quality Score is not fully available before a campaign launches — it builds up from actual impression and click data. However, you can estimate quality before launch using:

1. **Ad Relevance check:** Does Headline 1 contain the target keyword? (Yes = likely Above average. No = likely Below average.)

2. **Landing Page preview:** Does the landing page H1 or prominent text reflect the keyword? Is the page fast and mobile-friendly? Does it have a clear CTA?

3. **Competitive SERP review:** Search the target keyword in incognito. Is your ad copy (based on what you've written) competitive with what's showing? Would a searcher be drawn to click it?

These three checks give a reasonable pre-launch indication of where QS will land. Flag any ad group where all three checks raise concerns — fix before launch.
