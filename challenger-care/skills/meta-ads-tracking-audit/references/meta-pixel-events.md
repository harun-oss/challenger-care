# Meta Pixel Events — Standard Events by Vertical & Custom Event Guide

## Standard Events Reference

Meta has 17 standard events. These should be used over custom events wherever possible — they're recognised by the algorithm for optimisation and have built-in reporting support.

### eCommerce — Priority Order

| Event | When to Fire | Required Parameters | Optional Parameters |
|---|---|---|---|
| **Purchase** | Order confirmation page | `value`, `currency` | `content_ids`, `content_type`, `num_items` |
| **AddToCart** | Add to Cart button click | `value`, `currency`, `content_ids` | `content_type`, `contents` |
| **InitiateCheckout** | Checkout page load | `num_items`, `value`, `currency` | `content_ids`, `content_type` |
| **ViewContent** | Product page load | `content_ids`, `content_type`, `value` | `currency` |
| **AddToWishlist** | Wishlist/Save button click | `content_ids`, `value`, `currency` | — |
| **Search** | Search results page | `search_string` | — |
| **CompleteRegistration** | Account created confirmation | `currency`, `value` | `status` |

### Lead Gen / B2B — Priority Order

| Event | When to Fire | Required Parameters | Notes |
|---|---|---|---|
| **Lead** | Form submission confirmation | `currency`, `value` | Primary conversion event — value = estimated lead value |
| **CompleteRegistration** | Sign-up confirmation | `status` | For trial or account sign-ups |
| **Contact** | Contact form submission | — | Secondary signal |
| **Schedule** | Booking confirmation page | — | For demo/call booking |
| **ViewContent** | Key landing pages | `content_name` | Blog posts, pricing page, case studies |
| **InitiateCheckout** | Pricing page or plan selection | — | Use if paid conversion funnel exists |
| **SubmitApplication** | Application form confirmation | — | For applications, waitlists |

---

## Customer Data Parameters (Critical for EMQ)

Event Match Quality (EMQ) measures how well Meta can match your events to real people. To achieve EMQ 7+, you must pass customer data parameters (hashed automatically by Meta's pixel).

| Parameter | Field | Format |
|---|---|---|
| `em` | Email address | Lowercase, trimmed, SHA-256 hashed by pixel |
| `ph` | Phone number | E.164 format (e.g. +12125551234) |
| `fn` | First name | Lowercase |
| `ln` | Last name | Lowercase |
| `ct` | City | Lowercase, no spaces |
| `st` | State | 2-letter ISO code (e.g. "ca") |
| `zp` | Zip/postal code | As-is |
| `country` | Country | 2-letter ISO code (e.g. "us") |

**At minimum, pass email (`em`) on all post-login events.** This alone improves EMQ significantly. For Purchase events, pass email + phone + zip.

On Shopify: the Meta Sales Channel handles this automatically when the customer is logged in.
On custom sites: pass via the `userData` object in the pixel base code.

---

## Custom Events Guide

Use custom events only when no standard event fits. Custom events cannot be used for standard campaign optimisation objectives — only for tracking/reporting.

**Good uses for custom events:**
- Tracking a specific micro-conversion that doesn't map to standard events (e.g., "WatchedDemoVideo", "DownloadedPricingPDF")
- Tracking engagement milestones (e.g., "ScrolledTo50Percent", "StayedOnPageOver2Min")

**Bad uses for custom events:**
- Using "Purchase_Confirmed" instead of "Purchase" — this breaks algorithm optimisation
- Using custom events for primary conversion goals — Meta cannot optimise toward them

**Naming convention for custom events:**
- PascalCase: `VideoPlayed`, `QuizCompleted`, `ChatInitiated`
- No spaces, no special characters
- Keep names under 40 characters
- Document all custom events in the Tracking Audit deck

---

## Attribution Window Settings

Check the Ad Account's attribution window settings under: Business Settings → Data Sources → Pixels → Settings.

**Recommended settings:**

| Setting | Recommended | Notes |
|---|---|---|
| Click attribution window | 7-day click | Standard; use 1-day for impulse-purchase eCommerce |
| View attribution window | 1-day view | Avoids over-crediting view-through conversions |
| Advanced matching | On | Improves EMQ — enables customer data hashing |

**Warning:** If the attribution window was recently changed, historical data will look inconsistent. Document the change date in the audit.
