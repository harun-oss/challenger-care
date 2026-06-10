# Conversion Tracking Diagnosis & GTM Repair

Read this when Phase 2 of the Account Audit finds any conversion tracking status other than "Recording conversions."

---

## Step 1 — Identify the Failure Mode

In Google Ads → Tools → Conversions, note the status of each conversion action:

| Status | What it means |
|--------|--------------|
| Recording conversions | ✅ Working correctly |
| No recent conversions | ⚠️ Tag may be working but no one has converted recently — or tag may have stopped firing. Check the last recorded conversion date. |
| Tag inactive | 🔴 The tag is not firing at all. GTM issue or tag was removed. |
| Unverified | ⚠️ Tag was set up but has never recorded a conversion. Tag may be on the wrong page or not yet triggered. |
| Tracking status unknown | ⚠️ Google can't confirm the tag is working. GTM container may not be installed on the site. |

---

## Step 2 — Check GTM Container Installation

Open Challenger's live website in Chrome. Open DevTools (F12) → Sources tab → search for the GTM container ID (e.g., `GTM-XXXXXXX`).

If the GTM container ID is not found in the page source: the GTM snippet was removed from the site. This is the most common issue after a website redesign or CMS migration.

**Fix:** Re-install the GTM snippet. Challenger's developer needs to add the GTM container code to the `<head>` and `<body>` of every page:

```html
<!-- In <head> -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>

<!-- Immediately after opening <body> -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

After re-installation, proceed to Step 3.

---

## Step 3 — Verify Google Tag (AW-XXXXXXXXX) is Firing

Install the Google Tag Assistant Chrome extension if not already installed.

1. Open Tag Assistant → Connect to Challenger's site
2. Navigate to any page on the site
3. Look for the Google Tag (`AW-XXXXXXXXX`) — it should show status: **Fired** on every page

**If the Google Tag is not firing:**
1. In GTM → Tags → find the "Google Tag" (or "Google Ads - Google Tag")
2. Confirm: Tag ID = `AW-XXXXXXXXX` (exact conversion ID)
3. Confirm: Trigger = All Pages (Initialization - All Pages, not Page View)
4. Check: is the tag paused? Look for a pause icon in GTM
5. Has the GTM container been published after any recent changes? In GTM → Submit → confirm the latest version is published

**If the Google Tag is missing entirely from GTM:**
Create a new tag:
- Tag type: Google Tag
- Tag ID: `AW-XXXXXXXXX` (the Conversion ID from Google Ads → Tools → Conversions → [conversion action] → Tag setup)
- Trigger: All Pages (Initialization trigger)
- Name: "Google Ads — Google Tag"
- Save and publish

---

## Step 4 — Verify Conversion Tracking Tag is Firing on the Right Trigger

In Tag Assistant, complete the conversion action (submit the lead form, or visit the Thank You page):

1. Does the Conversion Tracking tag fire?
2. Does it fire on the correct trigger only (not on every page)?
3. Check the tag details: Conversion ID and Label — do they match the values in Google Ads?

**Common failure modes:**

### A. Thank You page URL changed after website redesign

Most common issue. The old site's Thank You page was `/thank-you`. The new site uses `/contact/success` or `/confirmation`.

**Fix in GTM:**
1. GTM → Triggers → find the Thank You page trigger
2. Update the Page Path condition to match the new URL
3. Test in GTM Preview → navigate to the new confirmation page → confirm Conversion Tracking tag fires
4. Publish

### B. Form plugin changed (e.g., Contact Form 7 → Gravity Forms)

Different form plugins emit different events that GTM listens for. A trigger set up for Contact Form 7 won't fire on a Gravity Forms submission.

**Fix:**
1. Check what form plugin the new site uses
2. In GTM → Triggers → update the Form Submission trigger:
   - For most modern plugins: use Form Submission trigger type, confirm "Check Validation" is enabled, and select the correct form via ID, class, or URL condition
   - Some plugins require a custom event listener — check the plugin documentation for GTM integration
3. Test end-to-end in GTM Preview

### C. Single-page application (SPA) — no page reload on form submit

If the site is built on React, Vue, or Angular, submitting a form may not trigger a page reload. Standard Page View triggers won't work.

**Fix:**
- The site needs to push a custom event to the GTM dataLayer on form success:
  ```javascript
  dataLayer.push({ event: 'form_submit_success' });
  ```
- Create a Custom Event trigger in GTM listening for this event: `form_submit_success`
- This requires developer involvement — escalate to Challenger's dev team

### D. Conversion tracking tag has wrong Conversion ID or Label

**Fix:** In Google Ads → Tools → Conversions → [conversion action] → Tag setup → copy the exact Conversion ID and Label. Compare to what's in the GTM tag. Update if different.

---

## Step 5 — Submit a Test Conversion

After verifying tags in GTM Preview:

1. Submit a real test form or complete a real test purchase (use a test order/coupon if available)
2. Wait up to 24 hours
3. Check Google Ads → Tools → Conversions — the conversion action status should update to "Recording conversions" and show a recent conversion date

If the status doesn't update after 24 hours: return to Step 3 and re-check the tag firing. The most common remaining issue is the tag firing on the wrong page or event.

---

## Step 6 — Cross-Check with GA4

After confirming Google Ads conversion tracking is working:

1. In GA4 → Reports → Engagement → Events — confirm the key event (e.g., `form_submit`, `purchase`) is firing
2. In Google Ads → Tools → Linked Accounts → Google Analytics — confirm the GA4 link is Active
3. Compare conversion counts: Google Ads conversions vs GA4 conversions for the same time period. A 10–30% difference is normal (attribution window differences). A >50% difference suggests a persistent tracking issue.

**Note on attribution:** Google Ads defaults to a 30-day click-through conversion window. GA4 defaults to a 7-day click attribution. This causes structural differences in reported conversion numbers — it doesn't necessarily mean tracking is broken.

---

## When to Escalate

Escalate to a tracking specialist when:
- The GTM container is installed and all tags appear to be firing correctly in Preview, but conversions still don't appear in Google Ads after 48 hours
- The site is a SPA and the development team is unavailable to add dataLayer pushes
- The conversion action is a phone call (requires call tracking setup, which is outside standard GTM configuration)
- Server-side GTM is in use (non-standard setup requiring specialist knowledge)
