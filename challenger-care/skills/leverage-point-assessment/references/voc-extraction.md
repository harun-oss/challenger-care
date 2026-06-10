# Voice of Customer Extraction Framework

## Purpose

VoC extraction transforms raw sales conversations and stakeholder interviews into organized intelligence that strengthens every section of the Leverage Point Assessment. The goal is to capture the exact words prospects and customers use — not to paraphrase them.

## Source Classification

Before extracting, classify each transcript:

| Source Type | What to Extract | Reliability |
|---|---|---|
| **Sales demo (won)** | Aha moments, value language, close triggers, objections overcome | High — this is what works |
| **Sales demo (lost/stalled)** | Objection language, friction points, competitive mentions, stall patterns | High — this is what doesn't work |
| **Stakeholder interview** | Founder's view of each leverage point, contradictions with data, emotional energy | Medium — filter for optimism bias |
| **Internal team sync** | Operational reality, churn details, financial constraints, product status | Very high — unfiltered truth |
| **Customer success call** | Retention signals, expansion opportunities, product feedback, usage patterns | High |

## Extraction Categories

For each transcript, extract quotes into these 6 buckets:

### 1. Pain Language
What prospects say BEFORE buying. How they describe their current situation.
- "Our procurement is substandard"
- "Back of the napkin"
- "Everything feels so antiquated"

**Use in assessment:** MARKET (validates the problem), POSITION (messaging language), REACH (ad copy)

### 2. Value Language
What customers say DURING or AFTER the demo/purchase. How they describe the product's value.
- "It's a really simple solution"
- "The email generation alone makes it worthwhile"
- "It makes purchasing super easy"

**Use in assessment:** PRODUCT (what to protect), POSITION (what to emphasize), CONVERT (what to front-load in demos)

### 3. Objection Language
What stalls or kills deals. The words that signal resistance.
- "I need cost approval"
- "Give me a week or two to socialize this"
- "It feels like one of about four components we need"

**Use in assessment:** CONVERT (friction to remove), MONEY (pricing sensitivity), POSITION (narrative to reframe)

### 4. Aha Moments
The specific point in a conversation where a prospect shifts from skeptical to interested. Often accompanied by "oh" or "that's cool" or a visible energy change.
- The first time they see a card scanned
- When they realize it replaces their broken Excel sheet
- When they hear a case study with specific numbers

**Use in assessment:** PRODUCT (what to engineer into self-serve), CONVERT (what to front-load), REACH (what to feature in ads)

### 5. Close Triggers
What finally gets someone to say yes. The specific moment or argument that overcomes the last objection.
- ROI math ("it pays for itself in 2 hours of purchasing time saved")
- Competitive displacement ("this replaces the $1,000/month of broken software you're already paying for")
- Risk removal ("7-day free trial, no commitment")

**Use in assessment:** MONEY (pricing framing), CONVERT (what to emphasize in follow-up), REACH (ad hooks)

### 6. Competitive Context
Who else prospects mention, what they're comparing against, and what language they use to describe alternatives.
- "We're currently using [X]"
- "We looked at [Y] but it was too expensive / complex / limited"
- "Our current system is [description]"

**Use in assessment:** MARKET (competitive landscape), POSITION (differentiation), REACH (targeting)

## How to Map Quotes to Leverage Points

Every quote should be tagged to 1-2 leverage points. Use this decision tree:

1. **Is it about the size/nature of the opportunity?** → MARKET
2. **Is it about the product experience?** → PRODUCT
3. **Is it about pricing, margins, or cash flow?** → MONEY
4. **Is it about differentiation or brand?** → POSITION
5. **Is it about how they found us or awareness?** → REACH
6. **Is it about the sales process or buying experience?** → CONVERT
7. **Is it about team, systems, or scaling?** → EXPAND

Some quotes map to multiple. A prospect saying "we're spending $1,000/month on software that doesn't work" is both MONEY (pricing context) and MARKET (validates the pain).

## Output Format for the Assessment

VoC quotes appear in the assessment as yellow callout boxes:

```
"Exact prospect words go here in quotes and italics."
— Attribution (Name, Company or Role)
```

Rules:
- Use EXACT words from the transcript. Don't clean up grammar or paraphrase.
- Attribute to the person and company (or role if company is sensitive)
- 1-3 quotes per leverage point section (don't overdo it)
- Choose quotes that are specific and vivid, not generic
- The best quotes make the reader feel the pain or excitement

## Handling Internal Syncs and Team Meetings

Internal team meetings are gold mines of unfiltered truth. They contain:

- **Real churn data** — who left and why (not the PR version)
- **Financial reality** — cash constraints, burn rate, what they can't afford
- **Product truth** — what's actually broken vs. what the marketing says
- **Team dynamics** — who's stretched thin, where communication breaks down
- **Fundraising status** — what investors are actually saying

Extract this intelligence but DO NOT put internal quotes in Challenger-facing deliverable. Instead, use internal data to:
1. Validate or challenge what the founder told you
2. Inform your grades (if the founder says "low churn" but the sprint review shows 15 churned accounts, adjust accordingly)
3. Understand constraints that affect your recommendations (if they can't afford a new hire, don't recommend one)

## Red Flags to Watch For

- **Founder optimism bias:** If the founder says everything is great but the data shows otherwise, trust the data.
- **"We're about to..." syndrome:** Plans that haven't shipped yet don't count as current state. Grade on what IS, not what's planned.
- **Vanity metrics:** Large social followings or website traffic that doesn't convert is a REACH problem, not a strength.
- **Revenue concentration:** If one customer is >30% of revenue, that's a MARKET and EXPAND risk.
- **Churn buried in growth:** If they're adding customers but also losing them at a similar rate, net growth is flat. Look at gross churn, not just net.
