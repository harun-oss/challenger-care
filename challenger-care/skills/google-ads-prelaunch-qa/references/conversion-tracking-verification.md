# Conversion Tracking Verification & Repair (Pre-Launch)

Read this during Phase 2 of the Pre-Launch QA skill when any conversion tracking item fails. This guide covers diagnosis and repair before a campaign goes live.

---

## Quick Diagnosis Flowchart

```
Is there a conversion action in Google Ads → Tools → Conversions?
    NO → Create one (see: Creating a conversion action)
    YES ↓

What is the status?
    "Recording conversions" → ✅ Pass Phase 2A
    "No recent conversions" → Check last recorded date
        Last recorded <30 days ago → Could be genuine low traffic; proceed cautiously
        Last recorded >30 days ago, or never recorded → GTM tag investigation needed
    "Tag inactive" → GTM tag removed or broken → Tag repair needed
    "Unverified" → Tag exists but never fired → Test conversion needed

Is the Google Tag (AW-XXXXXXXXX) firing on all pages?
    Check with Tag Assistant (see below)
    NO → Install or repair Google Tag in GTM
    YES ↓

Is the Conversion Tracking tag firing on the correct trigger?
    NO → Fix trigger in GTM
    YES ↓

Submit a test conversion → Does it appear in Google Ads within 24h?
    NO → Re-diagnose from Step 3 (tag firing check)
    YES → ✅ Conversion tracking verified
```

---

## Creating a Conversion Action

If no conversion action exists yet:

1. Google Ads → Tools → Conversions → + New conversion action
2. Select: **Website**
3. Configure:
   - **Category:** Lead (lead gen) / Purchase (eCommerce)
   - **Name:** Descriptive — "Contact Form Submit", "Free Quote Request", "Purchase"
   - **Value:**
     - Lead gen: use a fixed value (estimated average lead value) or $1 as a placeholder
     - eCommerce: select "Use the transaction value" to capture dynamic revenue
   - **Count:**
     - Lead gen: **One** — count only the first conversion per user session
     - eCommerce: **Every** — count each purchase separately
   - **Click-through conversion window:** 30 days (default — appropriate for most clients)
   - **View-through window:** 1 day (default)
4. Save and note the **Conversion ID** (AW-XXXXXXXXX) and **Conversion Label** from the tag setup screen

---

## Installing the Google Tag in GTM

The Google Tag must fire on every page before conversion tracking can work.

1. In GTM → Tags → New
2. Tag type: **Google Tag**
3. Tag ID: `AW-XXXXXXXXX` (Conversion ID from step above)
4. Trigger: **Initialization - All Pages** (important: use Initialization trigger, not Page View — this ensures the tag fires before other tags)
5. Name: "Google Ads — Google Tag [AW-XXXXXXXXX]"
6. Save

---

## Installing the Conversion Tracking Tag in GTM

1. GTM → Tags → New
2. Tag type: **Google Ads Conversion Tracking**
3. **Conversion ID:** AW-XXXXXXXXX
4. **Conversion Label:** [the label from Google Ads conversion setup]
5. **Conversion Value:** Leave blank for fixed value (Google pulls from conversion action settings). For dynamic eCommerce revenue: set to a DataLayer variable `{{dlv - revenue}}` or equivalent
6. Set trigger (see below)

---

## Setting the Correct Trigger

### Option A: Thank You page (most reliable for lead gen)

1. GTM → Triggers → New
2. Trigger type: **Page View**
3. This trigger fires on: **Some Page Views**
4. Condition: Page URL → **contains** → `/thank-you` (or whatever the confirmation page URL is — ask the developer if unsure)
5. Test: does this URL appear in the browser after a form is submitted? Verify by submitting a test form.

**Common issue — URL changed after website redesign:**
Check the current confirmation page URL by submitting the form in a test environment. Update the trigger URL condition to match the current URL.

### Option B: Form submission event (when no Thank You page exists)

1. GTM → Triggers → New
2. Trigger type: **Form Submission**
3. Enable: **Wait for Tags** (500ms) and **Check Validation** (ensures form was submitted successfully, not just clicked)
4. This trigger fires on: **Some Forms**
5. Condition: Form ID → equals → [the form's HTML id attribute] (inspect the form element to find this)
6. Test thoroughly — form submission triggers are more fragile than page view triggers

**If the form uses an iFrame or third-party widget (e.g., Gravity Forms, Typeform, JotForm):**
Standard GTM Form Submission triggers often don't fire across iFrames. Solutions:
- Check if the form provider has native GTM integration documentation
- Some providers offer a "postMessage" listener that GTM can detect — custom JavaScript may be needed
- Escalate to developer if standard form triggers don't fire

### Option C: eCommerce purchase confirmation page

1. Trigger type: **Page View**
2. Condition: Page URL → contains → `/order-confirmation` or `/checkout/success` (varies by eCommerce platform)
3. For Shopify: `/thank_you` is the standard post-purchase URL

---

## Testing with GTM Preview Mode

1. GTM → Preview → enter the live website URL → Connect
2. The Tag Assistant panel opens in a new window showing all tag activity
3. Navigate through the conversion flow:
   - Fill out the lead form → submit → navigate to Thank You page
   - Or: complete a test purchase → navigate to order confirmation
4. In the Tag Assistant panel, verify:
   - **Google Tag (AW-XXXXXXXXX):** should show "Fired" on every page
   - **Conversion Tracking tag:** should show "Fired" only on the conversion page, not on other pages

**What "Not Fired" means:** The trigger conditions weren't met. Check the trigger URL or form conditions.
**What "Fired with errors" means:** The tag fired but Google returned an error — check the Conversion ID and Label are correct.

---

## Verifying in Google Ads

After a successful GTM Preview test:

1. Submit a real test conversion (submit the form, or use a test order in Shopify)
2. In Google Ads → Tools → Conversions → find the conversion action
3. The **Tracking status** should update from "Unverified" or "No recent conversions" to **"Recording conversions"** within 24 hours
4. The **Last conversion** date should reflect today or yesterday

**If status doesn't update after 24 hours:**
- Return to GTM Preview and re-test — confirm the Conversion Tracking tag fired (not just the Google Tag)
- Test with an incognito browser window and no Chrome extensions (some ad blockers or privacy extensions interfere with tag firing even during testing)
- Check: is the Google Ads account in the same Google account as the GTM container? Mismatched accounts can cause reporting delays.

---

## Cross-Check with GA4

After confirming Google Ads conversion tracking is verified:

1. GA4 → Reports → Engagement → Events — confirm the key event is appearing (e.g., `form_submit`, `generate_lead`, `purchase`)
2. Check the event count over the last 7 days — does it roughly match the expected volume?
3. GA4 → Conversions — confirm the event is marked as a conversion in GA4 (if Challenger tracks it as a GA4 conversion)
4. Google Ads → Tools → Linked Accounts → Google Analytics — confirm GA4 is linked with Status: Active

**Expected discrepancy between GA4 and Google Ads conversion counts:**
- Google Ads uses a 30-day click-through window (default)
- GA4 uses a 7-day click attribution by default
- Structural difference: 10–30% variation in reported conversions is normal — this is attribution window difference, not a tracking error
- If the discrepancy is >50%: investigate further — may indicate a tag firing inconsistency or cross-device tracking gap
