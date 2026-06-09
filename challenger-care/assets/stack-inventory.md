# Connected Stack Inventory — Challenger Care

Every tool that touches the website, marketing, ops, or AI system. What it does · what's connected · who has access · what's pending.

---

## Commerce stack (live)

### Shopify
- **Store:** [challengercare.com](https://challengercare.com)
- **Admin:** [admin.shopify.com](https://admin.shopify.com)
- **Plan:** Basic
- **Currency:** USD · Timezone: PDT · Country: US
- **Access granted:** Collaborator (code: 9550)
- **MCP status:** ✅ Live — pulls sales, inventory, customers, sessions, conversion
- **Apps installed:** Recharge · Klaviyo · Pagefly · JudgeMe · GA4 · Zigpoll

### Recharge
- **Purpose:** Subscription management on Shopify
- **Current subscribers:** 17
- **Goal:** Grow to 50+ within 90 days · migrate Amazon S&S subs over time
- **MCP status:** Not connected yet · accessed via Shopify orders that include subscription metadata

### Klaviyo
- **Purpose:** Email + SMS automation
- **Access:** Granted to info@growthhit.com + developer@growthhit.com
- **Admin status:** Pending — Hayden owes elevated permissions
- **MCP status:** Not connected yet · will connect once admin access is granted
- **Active flows:** Abandoned cart only
- **Pending build:** Welcome · Browse abandonment · Post-purchase · Winback

### Pagefly
- **Purpose:** Landing page builder for Shopify
- **Use case:** Custom PDPs and campaign landing pages
- **Access:** Through Shopify admin

### JudgeMe
- **Purpose:** Review collection + display on Shopify
- **Reviews imported:** 724 (already exported to project folder)
- **MCP status:** No direct MCP · works via CSV exports

### GA4
- **Property:** G-KEQ9SJG71H
- **Access:** Granted
- **MCP status:** Not connected yet · pending for full traffic source analysis
- **Note:** Shopify native analytics covers most of what GA4 would give — GA4 adds attribution + multi-touch detail

### Zigpoll
- **Purpose:** Exit-intent surveys
- **Use case:** Capture friction reasons from cart abandoners
- **MCP status:** No direct MCP · responses pulled via export

### Amazon Seller Central
- **Status:** Active · Hayden owns
- **Volume:** ~92% of total revenue · 1,318 S&S subscribers · 2,500+ reviews · 84% 5-star
- **MCP status:** **No MCP available** · data via manual report exports → Drive
- **Treatment:** Cash engine · maintain, don't optimize

---

## Marketing & content stack

### Meta Business Manager
- **Status:** Partially compromised — recovery in progress
- **MCP status:** Not connected yet
- **Reactivation gate:** BM cleanup complete + AOV ≥ $40 + Shopify CVR ≥ 2.5%
- **Risk tolerance:** Controlled spend with explicit ceilings

### Facebook + Instagram (organic)
- **Status:** Owned channels · minimal activity currently
- **Future:** Active once paid ads reactivate

### TikTok (organic + Shop)
- **Status:** Pending launch
- **Agency:** Implicit (separate engagement)
- **Goal:** Content engine fueling Meta + organic + ad amplification

### Reddit
- **Status:** Active · Hayden organically engaging
- **Subreddits:** r/malegrooming, r/wicked_edge, r/pomade (and related)
- **Tactic:** $5 jar drops every 8–12 weeks · drives 30–50 sustained sessions per drop
- **MCP status:** No direct MCP · web scraping for mentions when needed

### Google Ads
- **Status:** Not active
- **Future:** Brand defense + non-brand search after AOV economics support it

### Bing Ads
- **Status:** Not active

---

## Internal & operational stack

### Figma
- **Purpose:** Design destination for creative outputs
- **Use case:** Where AI-generated briefs and concepts get finalized into production-ready assets
- **MCP status:** Available via GrowthHit org · UUID swaps for client account at migration

### Google Drive
- **Purpose:** File storage · knowledge base host
- **Client folder:** [Drive link](https://drive.google.com/drive/folders/1mee3_Uyo7zSeRXapJ9J63pa5WXop-kuJ)
- **MCP status:** Available · pending Hayden's account connection
- **Use:** Stores all knowledge files, briefing outputs, action ledger artifacts, exports

### Slack
- **Purpose:** Internal team comms
- **GrowthHit channel:** C0B7GTR0ZGR (internal Challenger Care)
- **Client-facing channel:** TBD
- **MCP status:** Available via GrowthHit org

### Asana
- **Purpose:** Project management
- **Status:** In setup — Hayden adopting for the first time
- **MCP status:** Available · pending Hayden's account connection
- **Use:** Workflow tasks, "In flight" projects, manufacturing handoffs

### PandaDoc
- **Purpose:** Contract signing
- **Use case:** GrowthHit contracts already signed via this · May not need ongoing MCP

### Superhuman
- **Purpose:** Hayden's email client
- **Use case:** Email correspondence search — "Challenger Care" or "hayden@challengercare.com"

### Read AI
- **Purpose:** Meeting recording + transcripts
- **MCP status:** Available · client meetings tagged "Challenger Care"
- **Use:** Pull stakeholder interview content, kickoff transcripts, ongoing call insights

---

## AI infrastructure

### Claude (anthropic)
- **Plan:** Claude for Teams · 5 seats
- **Status:** Hayden stood up over a 10-hour weekend before kickoff
- **Walls hit:** Re-explaining context · need better skills, file structure, .md files

### Claude Project — Challenger Care
- **Status:** In build · this engagement's central deliverable

### Claude Code (Hayden's own builds)
- **Status:** Already used by Hayden to build the live abandoned cart email (Claude Code → HTML → Klaviyo)

### MCP Connectors (target state)
| MCP | Use | Status |
|---|---|---|
| Shopify | Orders, sales, inventory, sessions, customers | ✅ Live |
| Klaviyo | Flows, campaigns, metrics | Pending admin access |
| GA4 | Sessions, source, multi-touch | Pending |
| Google Drive | Knowledge files, exports, outputs | Pending |
| Asana | Tasks, projects, ownership | Pending |
| Slack | Team comms surfacing in dashboard | Optional · low priority |
| Read AI | Meeting transcripts | Available via GrowthHit |

### Claude Design
- **Status:** Hayden exploring for emails + brand design
- **Use case:** Brand-aligned visual generation
- **Linked output:** Some emails generated and pushed to Klaviyo via this path

---

## Not yet in stack · future considerations

- **Customer support tool** (Gorgias, Zendesk, etc.) — currently informal · may add as volume grows
- **Influencer outreach tools** (Aspire, Modash, etc.) — for the creator prospecting workflow
- **TikTok Shop seller account** — pending Implicit launch
- **QuickBooks / financial reporting tools** — Hayden flagged interest for AI reporting layer
- **SMS provider for concierge subs** — future retention play

---

## Per-tool access notes for migration

When porting the AI system from GrowthHit's org to Hayden's Claude:

| Tool | Migration action |
|---|---|
| Shopify | Hayden re-authorizes MCP under his Claude · update CONFIG.SHOPIFY_UUID in artifact |
| Klaviyo | Hayden authorizes once admin access granted · add tool to mcp_tools |
| GA4 | Hayden authorizes · add tool to mcp_tools |
| Drive | Hayden authorizes · file IDs stay the same if the folder is shared correctly |
| Asana | Hayden authorizes · project gids will be his own |
| Read AI | Stays in GrowthHit org · meeting transcripts accessible via shared link if needed |

---

## Decision rules for Claude

When workflows reference a tool:

1. **Always check the MCP status** — don't promise data from a tool that isn't connected
2. **Default to Shopify-native when possible** — even for CVR, sessions, sources (Shopify analytics is broader than people assume)
3. **Amazon is read-only via exports** — no live MCP, no real-time data
4. **Drive is the storage layer** — every workflow output lands there (or chat if Drive isn't connected)
5. **Klaviyo writes need approval** — any live email touch needs Hayden's Execute permission

---

## When to update this doc

- Any time a connector is added or removed
- When access status changes (e.g., Klaviyo admin granted)
- When a new tool enters the workflow (e.g., TikTok Shop seller account)
- When migration to Hayden's account happens (update MCP UUIDs)
