# Meta Pixel Health Checklist — Diagnostic & Fix Guide

## Tools You'll Need

- **Meta Pixel Helper** (Chrome extension) — real-time view of pixel fires on any page
- **Meta Events Manager** — canonical view of all events flowing to the account
- **Test Events tool** (inside Events Manager) — simulate and verify specific event triggers
- **GTM Preview mode** — if GTM is being used, verify tags are firing as expected

---

## Step-by-Step Diagnostic Process

### Step 1: Verify the Pixel ID

1. Open Events Manager → Data Sources → select the Dataset
2. Note the Pixel ID (format: a 15-17 digit number)
3. Open Challenger's website with Pixel Helper active
4. Confirm Pixel Helper shows the **same Pixel ID** — if it shows a different ID, the pixel on the site belongs to a different account

**Common cause of ID mismatch:** The client or a previous agency installed a pixel from a different Business Manager. Fix: Replace the pixel code on the site with the correct ID from the current account.

### Step 2: Check for Duplicate Fires

1. Open any page on Challenger's site with Pixel Helper
2. Look at the PageView event count — it should fire exactly once per page load
3. If PageView fires 2+ times, a duplicate pixel installation exists

**Common causes:**
- Pixel installed in both GTM and directly in the site theme/header
- Two separate GTM tags both firing the Meta pixel
- Shopify: Meta Sales Channel pixel + manually installed pixel

**Fix:** Remove one of the duplicate installations. Keep the GTM-managed one if GTM is in use; keep the Sales Channel one for Shopify.

### Step 3: Test Purchase Event

1. In Events Manager, go to Test Events → enter the site URL
2. Complete a test purchase (use a $0 test product or Shopify's test payment mode)
3. Verify the Purchase event appears in Test Events with:
   - Correct `value` parameter (matches order total)
   - Correct `currency` parameter (e.g., USD)
   - `event_id` present (required for CAPI deduplication)

**Common failure modes:**

| Symptom | Likely Cause | Fix |
|---|---|---|
| Purchase fires but no value | Value parameter missing from event code | Add `{value: checkout.total}` to event code |
| Purchase fires on wrong page | Trigger is set to all pages or wrong URL | Set trigger to thank-you / order confirmation URL only |
| Purchase fires but duplicates | Browser + CAPI both firing without dedup | Configure event_id deduplication |
| Purchase never fires | Thank-you page URL changed or not matching | Update GTM trigger URL to match current confirmation page |
| Purchase fires on add to cart | Wrong event name on wrong trigger | Rename event or reassign trigger |

### Step 4: Verify ViewContent and Cart Events

1. Visit a product page — ViewContent should fire
2. Click Add to Cart — AddToCart should fire
3. Go to checkout — InitiateCheckout should fire

**For Shopify:** These events are usually auto-fired by the Meta Sales Channel. Verify they're not being duplicated by a separate GTM setup.

### Step 5: Check Events Manager Signal Health

1. Go to Events Manager → Overview tab
2. Check "Activity" — should show events in the last 7 days for a live site
3. Look at "Event Match Quality" for each event — target 6/10 or higher
4. Check for any warnings or flags under each event

**Warning flags to investigate:**
- "No recent activity" on a live, high-traffic site → pixel is broken or blocked
- Low EMQ scores (below 6) → customer data parameters (email, phone) not being passed → CAPI fix needed
- "Redundant standard events" warning → duplicate fires detected by Meta itself

---

## Platform-Specific Notes

### Shopify

- Use the native **Meta Sales Channel** for pixel and CAPI — it handles most standard events automatically
- Check under Shopify Admin → Sales Channels → Facebook & Instagram → Pixels
- If a manually-installed pixel also exists: remove it to avoid duplication
- Customer data matching: ensure customer email and phone are passed via the Sales Channel (this improves EMQ)

### WooCommerce

- Use the **PixelYourSite** or **Facebook for WooCommerce** plugin for standard events
- Verify the plugin is updated to the latest version (old versions miss iOS 14+ event parameters)
- Manual GTM implementation: ensure dataLayer pushes are correctly formatted

### Custom / Headless

- Standard pixel implementation via GTM is preferred for maintainability
- Single Page Applications (SPAs): standard PageView won't fire on route changes — requires History Change trigger in GTM
- Server-Side tracking (CAPI) is especially important for SPAs where client-side events are less reliable

---

## Escalation Criteria

Escalate to a developer when:
- Pixel fires with incorrect Pixel ID and requires code-level changes
- Purchase event is missing value parameter and the fix requires code changes to the checkout page
- SPA requires custom event listeners for route changes
- CAPI implementation requires server-side code changes on a custom platform
