# DCT / Flexible Ads Build Guide

## What DCT / Flexible Ads Is

Dynamic Creative Testing (now called Flexible Ads in Meta's UI) automatically creates and tests combinations of your creative assets. You upload multiple headlines, primary texts, and images/videos — Meta finds the best-performing combinations for different audience segments.

## Step-by-Step Build Process

### In Ads Manager:

1. **Create a new ad set** inside your main campaign
2. Name the ad set: `[Client] | Meta Experiment #[N] | [Month] | [Type]`
3. Set conversion event: Purchase or Lead (matches campaign objective)
4. Set audience: Advantage+ Audience (broad) or your defined interest audience
5. Set placement: Advantage+ Placements (automatic)
6. Set budget: minimum $10/day (recommended $15-25/day for faster data)

7. **Create the ad** inside the ad set:
   - Format: Select "Flexible format" or "Dynamic Creative"
   - Upload all images/videos (3-5 assets)
   - Enter all headlines (up to 5 possible, aim for 3)
   - Enter all primary texts (up to 5 possible, aim for 3)
   - Enter destination URL
   - Select CTA button

8. **Check permutation count** before publishing:
   - Permutations = Headlines × Primary Texts × Media assets
   - If over 20: reduce media assets first (remove the weakest 1-2)

---

## Creative Specifications

### Image Specs

| Placement | Recommended Size | Aspect Ratio | Max File Size |
|---|---|---|---|
| Feed (Facebook + Instagram) | 1080 × 1080px | 1:1 (square) | 30MB |
| Stories/Reels | 1080 × 1920px | 9:16 | 30MB |
| Right column (desktop) | 1200 × 628px | 1.91:1 | 30MB |

**Best practice:** Create in 1:1 first. Meta will auto-crop for other placements. If Reels/Stories performance matters, create a 9:16 version manually.

**Text-on-image rule:** Keep text under 20% of the image area. Heavy text overlay can reduce delivery.

### Video Specs

| Placement | Recommended Length | Format | Aspect Ratio |
|---|---|---|---|
| Feed | 15–30 seconds | MP4/MOV | 1:1 or 4:5 |
| Stories/Reels | 15–30 seconds | MP4/MOV | 9:16 |
| In-stream | 5–15 seconds | MP4/MOV | 16:9 |

**First 3 seconds rule:** The hook must be in the first 3 seconds. Most viewers skip after 3 seconds if not hooked.

**Captions:** Always add captions. ~85% of Facebook video is watched without sound.

---

## Writing Strong DCT Components

### Headlines (under 40 characters)

The headline appears below the image in feed placements. It's not the primary hook — the image/video hook is more important. But the headline reinforces the message.

**Formulas that work:**
- Outcome statement: "Get [result] in [timeframe]"
- Question: "Is [pain] slowing you down?"
- Social proof: "[Number] [personas] trust [Brand]"
- Offer: "[X]% off your first order"

**What to avoid:**
- Your brand name as the headline (waste of a primary position)
- Vague descriptors ("High quality", "The best")
- Duplicate of the primary text first line

### Primary Text (the body copy)

The primary text appears above the image. This is where the main persuasion happens.

**Structure that works:**
1. Hook (first line — must stop the scroll)
2. Problem or context (1–2 lines)
3. Solution and key benefit (1–2 lines)
4. Social proof or credibility signal (1 line)
5. CTA (1 line — tell them exactly what to do)

**Length:** 100–150 words is typically the sweet spot. Longer copy can work for high-ticket or high-consideration products. Shorter for impulse purchases.

**First line is everything:** The first line is what shows before "See more" — write it as if it's the only line that will be read.

---

## Permutation Calculation Examples

**Example 1 — Under limit:**
- 3 headlines × 3 primary texts × 2 images = 18 permutations ✓

**Example 2 — Over limit:**
- 3 headlines × 3 primary texts × 3 images = 27 permutations ✗
- Fix: Reduce to 2 images → 3 × 3 × 2 = 18 ✓

**Example 3 — Pushing the limit:**
- 3 headlines × 3 primary texts × 2 videos = 18 permutations ✓
- 5 headlines × 2 primary texts × 2 images = 20 permutations ✓ (exactly at limit)

---

## Naming Convention Reference

**Ad set naming:** `[Client] | Meta Experiment #[N] | [Month] | [Type]`
**Examples:**
- `Oaktree | Meta Experiment #1 | April | Ads Variety`
- `LeadFlow | Meta Experiment #2 | May | Copy Test`
- `Petal | Meta Experiment #3 | June | Video vs Static`

**Ad naming (inside the ad set):** `[Client] | [Short creative description]`
**Examples:**
- `Oaktree | Lifestyle hero image set`
- `LeadFlow | Problem-solution copy v1`
