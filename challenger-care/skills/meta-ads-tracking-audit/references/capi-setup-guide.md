# Conversions API (CAPI) Setup Guide

## Why CAPI Is Now Required

iOS 14.5+ App Tracking Transparency and browser-level ad blocking mean that browser-only pixel tracking misses 20–40% of actual conversions for most advertisers. The Conversions API sends conversion signals directly from the server, bypassing browser restrictions.

CAPI + browser pixel together (with deduplication) is the current gold standard. Using one without the other leaves significant data gaps.

---

## Event Match Quality (EMQ)

EMQ is Meta's score (0–10) for how well your events match to real people. It directly impacts:
- Ad delivery quality (Meta favours advertisers with better signal quality)
- Retargeting accuracy
- Lookalike audience quality

| EMQ Score | Quality | Action |
|---|---|---|
| 8–10 | Excellent | No action needed |
| 6–7 | Good | Minor improvements possible |
| 4–5 | Fair | Add more customer data parameters |
| Below 4 | Poor | CAPI setup likely needed; missing key data |

**How to check:** Events Manager → Data Sources → select Dataset → Event Match Quality tab.

---

## CAPI Setup by Platform

### Shopify (Easiest — Native Integration)

1. Shopify Admin → Sales Channels → Facebook & Instagram
2. Under "Pixels", ensure your Pixel ID is connected
3. Under "Data sharing", set to **Maximum** (this enables CAPI)
4. Shopify automatically handles:
   - Server-side event sending
   - Event deduplication via shared `event_id`
   - Customer data matching (email, phone, address)

**Time to set up:** ~5 minutes
**No developer needed**

### WooCommerce

**Option A: Plugin (recommended)**
- Use **PixelYourSite Pro** (paid) or **Facebook for WooCommerce** (free)
- Both plugins have a native CAPI option — enable it in the plugin settings
- Requires a Meta System User token (generate in Business Manager → System Users)

**Option B: Manual / Agency server-side**
- Use Meta's Marketing API to send events server-side
- Requires developer work — scope with client before recommending

**Time to set up:** 30–60 minutes with plugin; 1–3 days with custom code

### Custom / Headless Sites

1. In Events Manager → Settings → Conversions API → Connect a new integration
2. Choose "Manual" setup
3. Generate a CAPI Access Token
4. Share the token with the developer
5. Developer implements server-side POST to `https://graph.facebook.com/v18.0/{PIXEL_ID}/events`

**Required fields for each CAPI event:**
- `event_name` (must match browser pixel event name exactly)
- `event_time` (Unix timestamp)
- `user_data` (at minimum: `em` hashed email)
- `event_id` (unique ID shared with browser event for deduplication)
- `action_source` (set to "website")

**Time to set up:** 1–5 days developer effort depending on complexity

---

## Deduplication Setup

Without deduplication, if both browser pixel and CAPI fire for the same conversion, Meta counts it twice. This inflates conversion numbers and misleads optimisation.

**How deduplication works:**
Both the browser pixel and the CAPI call must send the same unique `event_id` for the same event. Meta then de-duplicates them into a single counted conversion.

**Implementation:**
1. Generate a unique ID for each event occurrence (e.g., UUID or order ID for Purchase)
2. Pass this ID as `eventID` in the browser pixel: `fbq('track', 'Purchase', {value: 50, currency: 'USD'}, {eventID: 'order_12345'})`
3. Pass the same ID as `event_id` in the CAPI payload

**Verify deduplication is working:** In Events Manager, look at the "Deduplication" column — it should show the percentage of events being deduplicated. A non-zero percentage confirms it's active.

---

## Common CAPI Issues

| Issue | Cause | Fix |
|---|---|---|
| Events duplicating (count doubled) | CAPI sending but no deduplication | Add matching `event_id` to both pixel and CAPI |
| Low EMQ despite CAPI | Not passing customer data (email, phone) | Pass `em` (hashed email) in `user_data` |
| CAPI events delayed | Server processing lag | Normal if under 1 hour; escalate if over 24 hours |
| CAPI connected but low data volume | Event triggers not matching | Compare CAPI event count vs browser event count in Events Manager |
| Access token expired | Token not refreshed | Regenerate system user token in Business Manager |
