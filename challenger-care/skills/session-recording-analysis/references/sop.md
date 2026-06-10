# Session Recording Analysis — SOP Reference v1.0

## Table of Contents
1. Overview & Purpose
2. Where This Fits in the CRO Process
3. Tools & Access
4. Pre-Analysis Setup
5. Recording Prioritization & Filtering Strategy
6. Behavioral Signal Reference Guide
7. Desktop vs. Mobile Analysis
8. Evidence Standard
9. Figma Deliverable Structure
10. QA Checklist
11. Post-Delivery Checklist

---

## 1. Overview & Purpose

Session recording analysis is Challenger's primary qualitative research method for understanding
how real users behave on a client's website. Heatmaps show aggregate patterns; session recordings
explain the story behind those patterns — the moments of hesitation, confusion, frustration, and
success that explain why users convert or don't.

**You are the brain and the pen. The analyst is the eyes.**
Claude guides the analyst on what to filter for and what to look for, then transforms raw
observations into structured, deliverable-ready findings.

---

## 2. Where This Fits in the CRO Process

| Step | Research Type |
|------|--------------|
| Step 1 | Heuristic / UX Audit |
| Step 2 | Heatmap & Scroll Map Analysis |
| **Step 3 (this SOP)** | **Session Recording Analysis** |
| Step 4 | Exit-Intent Polls & VoC Survey Analysis |
| Step 5 | Hypothesis Development & Test Roadmap |

Always request prior heuristic and heatmap findings before starting. Recordings validate,
challenge, or add nuance to what aggregate data showed.

---

## 3. Tools & Access

**Default:** Hotjar. Login at hotjar.com, select client site, go to Recordings.

| Tool | Key Notes |
|------|-----------|
| Hotjar | Multi-page journey tracking, rage/dead click tagging, good device segmentation |
| Microsoft Clarity | Free, integrates with GA4, good frustration signals |
| FullStory | Enterprise, automated frustration detection, excellent filtering |
| Mouseflow | Friction score, strong form analytics |
| Lucky Orange | Intuitive UI, real-time view |

**Access check:** Confirm recordings are actively captured and sufficient volume exists
(minimum 20 recordings per key page in the date range). Flag low-traffic pages before starting.

---

## 4. Pre-Analysis Setup

Before watching any recordings:

1. Pull heuristic analysis findings for this client
2. Pull heatmap analysis findings
3. Pull analytics: highest exit rate pages, lowest conversion pages
4. Define 2–3 specific hypotheses to test (e.g. "Do users struggle with the pricing section?")
5. Define which pages to analyze (from heuristic audit key pages)
6. Set date range: last 2–4 weeks default; extend to 30–60 days for low-traffic sites

**Scope guidance:** Depth on 3–5 key pages beats shallow coverage of 10 pages.

---

## 5. Recording Prioritization & Filtering Strategy

### Always segment by device first
Split into two separate filter queues before applying any other filters:
- Desktop / laptop
- Mobile (treat tablet separately if volume warrants)

Never mix device types. Mobile and desktop users behave very differently.

### Priority filter stack (apply in this order, per device)

| Priority | Filter |
|----------|--------|
| 1 — Highest | Rage clicks on key pages |
| 2 | Exit sessions from primary conversion page |
| 3 | Long sessions with no conversion |
| 4 | Dead clicks |
| 5 | Form abandonment |
| 6 | New visitors only |
| 7 | Quick backs (immediate exit via back button) |
| 8 — Baseline | Sessions that did convert |

### How many recordings to watch
- Minimum per page per device: 20
- Standard: 30–50 for key conversion pages
- Stop when: same friction patterns repeat across 5+ sessions without new issues emerging
- Flag if fewer than 20 exist: note in findings as low-confidence

---

## 6. Behavioral Signal Reference Guide

| Signal | Definition + CRO Implication |
|--------|------------------------------|
| Rage Click | 3+ rapid clicks on same element. User frustration — broken link, unresponsive element, or misleading affordance. High priority. |
| Dead Click | Click on non-interactive element. User expected it to be clickable. Design affordance problem. |
| Quick Back | Immediate exit via back button. Page did not match expectation from referring link/ad. |
| Hesitation | Cursor/scroll stops 3+ seconds on element. Uncertainty or anxiety — notable before CTAs, pricing, form fields. |
| U-Turn Scroll | Scroll down then back up. User didn't find expected content or missed key information. |
| Form Re-entry | User deletes and re-types in a form field. Format confusion, validation error, or privacy hesitation. |
| Tab Switch | Opens new tab mid-session. Comparison shopping or looking for info the page didn't provide. |
| Scroll Depth Short | Exits well before bottom. Content at exit point not compelling enough to continue. |
| Repeated Navigation | Visits same page/section multiple times. Information architecture is confusing. |
| Successful Flow | Completes goal smoothly. Note what guided them — replicate for other users. |

### Mobile-specific signals

| Signal | Definition |
|--------|-----------|
| Pinch-to-Zoom | Content not readable at default scale. Text too small or images inadequate. |
| Tap Misses | Multiple taps near but not on a target. Touch target too small or too close to others. |
| Horizontal Scroll | Content extends off screen. Responsive layout issue. |
| Keyboard Obscures Content | Mobile keyboard covers active field or submit button. |

---

## 7. Desktop vs. Mobile Analysis

Always document separately. Key differences:

| Dimension | Desktop | Mobile |
|-----------|---------|--------|
| Navigation | Hover states, dropdown menus | Hamburger menus, swipe gestures |
| CTAs | Mouse-click sized | Thumb reach — primary CTA in lower third |
| Forms | Tab key navigation | Correct keyboard type per field |
| Content visible | More above-fold | Faster scroll, less text read |
| Load speed | Generally faster | Network variability critical |
| Trust signals | Visible in sidebar | May be hidden below fold |

---

## 8. Evidence Standard

**A finding requires 3+ sessions showing the same pattern.**

- 1 session struggling = anomaly, not a finding
- 3+ sessions with the same friction on the same element = finding
- Every finding needs at least 1 video link; key findings need 2+
- Technical issues (JS errors, broken forms, WebSocket failures) = flag to dev team separately
  — they are bugs, not UX findings

**What to note for each recording:**
- What the user was successfully doing
- Where they got stuck (element name, step in flow)
- Which behavioral signal revealed it
- Recording ID for examples (note 1–2 IDs per pattern)

---

## 9. Figma Deliverable Structure

### Page setup
- Create new Figma page titled: `Sessions — [Month Year]`
- Use existing client Figma file (reference prior sessions pages for layout)

### Per-page section structure

**Header banner (blue):**
`[Page Name] Sessions (Desktop: XX recordings / Mobile: XX recordings | [Date Range])`

**Then for each device (Desktop first, then Mobile):**

**Successful Achievements**
What users are doing well. Specific behaviors, named elements, video links.

**Unsuccessful Attempts**
Where users are failing. Specific friction, named element, behavioral signal, video links.

**Key Takeaways**
Specific actionable recommendations. One per Unsuccessful Attempt. Video link where helpful.

### Writing standards
- Plain language — write for a client who hasn't watched the recordings
- Specific — name the element, section, or step
- Evidence-based — only patterns observed in multiple recordings
- Quantify where possible — "15 of 61 mobile sessions showed rage clicks on Subscribe"
- Video links inline with the relevant finding

---

## 10. QA Checklist

Before delivering:
- [ ] All agreed pages covered
- [ ] Desktop and mobile documented separately for each page
- [ ] Recording count and date range noted per page
- [ ] Every finding supported by 3+ sessions
- [ ] Every Unsuccessful Attempt has at least 1 video link
- [ ] Key findings have 2+ video links
- [ ] Key Takeaways are specific recommendations, not problem restatements
- [ ] Technical bugs flagged separately (not buried in UX findings)
- [ ] No speculation presented as fact
- [ ] Figma page titled correctly: `Sessions — [Month Year]`
- [ ] Section layout follows format

---

## 11. Post-Delivery Checklist

- Share Figma link with PM; note any low-sample-size pages
- Flag technical bugs to dev team immediately
- Feed every Unsuccessful Attempt into the test hypothesis backlog
- Note pages needing more recordings for future rounds
- Archive Figma page name and date in client research log
