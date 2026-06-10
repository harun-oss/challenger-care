---
name: inventory-restock
description: 'Calculates reorder timing from real velocity, drafts the email to Emanuel, opens the Asana task. MANDATORY TRIGGER: any mention of "Reorder Pomade 4oz", "Check our inventory — anything need restocking?", "Time to reorder anything?". Do NOT use this for: New product launches (use `launch-new-product`). General inventory health review (run the dashboard''s "Top SKUs" section). Strategic SKU decisions like discontinue / bundle / promote (use `highest-leverage`).'
---

> **Permission tier:** execute · **Time:** 2min · **Tools/context:** mcp:shopify, mcp:asana (when connected), assets/team-roles.md, assets/unit-economics.md, CONFIG.md

# Handle inventory restock

## When to use this workflow

A SKU is approaching stockout or has crossed the restock threshold. Auto-triggered by the anomaly detector but can also be run manually.

## What you need

- The SKU to restock (or "let me find which ones need it")
- (Optional) Override the reorder quantity calculation

## What this produces

1. **Restock analysis**:
   - Current inventory level
   - 30-day velocity
   - Days of stock remaining
   - Recommended reorder quantity (based on lead time + target stock level)
   - Estimated cost (based on past PO data if available)
2. **Email to the {{roles.inventory_owner}}** — drafted, ready to send, in brand voice
3. **Asana task** — created for tracking the PO through to delivery
4. **Cost estimate** — wholesale cost ballpark for cash flow planning

## How Claude runs it

1. Pull current inventory from Shopify for the target SKU
2. Calculate 30d velocity from Shopify sales
3. Apply lead time (Pomade = 21 days per past data — confirm for other SKUs)
4. Recommend reorder qty = (target stock days × velocity per day) + safety buffer
5. Reference `../../assets/team-roles.md` — the {{roles.inventory_owner}} is the manufacturing handoff
6. Draft email to the {{roles.inventory_owner}} with all the data
7. Open Asana task in the "Inventory" project (when Asana connected)
8. Surface the email for the {{roles.execute_tier_approver}}'s approval before sending

## Permission tier

**Execute** — sends a real email to the {{roles.inventory_owner}} + creates a real Asana task. Funds don't move until the {{roles.inventory_owner}} responds with PO confirmation. Reversible: the email can be retracted within send-delay window; the Asana task can be deleted.

## Example prompts that trigger this

- "Reorder Pomade 4oz"
- "Check our inventory — anything need restocking?"
- "Time to reorder anything?"

## Special handling

- **Combo (3-pack)** — currently shows negative inventory due to a tracking error. This workflow flags the tracking issue separately from the restock decision and asks the {{roles.founder}} to confirm both actions.
- **Dead SKUs** (e.g., Body Wash, Tea Tree Shampoo with high stock + low velocity) — workflow does NOT recommend restock. Instead refers to `highest-leverage` for product mix decisions.

## Don't use this for

- New product launches (use `launch-new-product`)
- General inventory health review (run the dashboard's "Top SKUs" section)
- Strategic SKU decisions like discontinue / bundle / promote (use `highest-leverage`)
