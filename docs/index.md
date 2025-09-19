---
title: Quirk AI — Overview
nav_order: 1
---

<!-- Inline overrides so they always load on this page -->
<style>
  /* Adjust how wide you want the light-blue sidebar */
  :root { --quirk-sidebar-width: 360px; } /* tweak 320–400px to taste */

  /* Desktop+ : widen sidebar and shift main area */
  @media (min-width: 992px) {
    .side-bar {
      width: var(--quirk-sidebar-width) !important;
    }
    .main {
      margin-left: var(--quirk-sidebar-width) !important;
    }
  }

  /* Center the main content column and the header/search row */
  .main .main-content,
  .main .main-header {
    max-width: 960px;         /* readable column; adjust if desired */
    margin-left: auto;
    margin-right: auto;
    padding-left: 1rem;
    padding-right: 1rem;
  }

  /* Optional: tighten the top spacing under the header */
  .main .main-content > h1:first-child { margin-top: .5rem; }
</style>

# Quirk AI 

Quirk AI is our **on-prem corporate assistant** that improves speed, consistency, and compliance across the dealer group while **keeping customer data private**.

{: .note }
**Phase-1 focus**: Internal copilots for BDC, Sales, Service Writers, Parts, and Marketing. Read-only adapters to CRM/DMS (e.g., VIN Solutions). Voice pilots via Twilio → OpenAI Realtime.

## Why it matters (business outcomes)

- **Response speed**: cut handling time for common tasks by **30–50%**  
- **Consistency**: one brand voice, compliant across **13 OEMs / 20 stores**  
- **Quality**: better lead follow-up, clearer repair notes, fewer escalations  
- **Privacy**: on-prem isolation; PII redaction in logs

## Quick links
[Executive Brief](overview/exec.md){: .btn .btn-primary }
[Architecture](overview/architecture.md){: .btn }
[Security Posture](overview/security.md){: .btn }
[Templates](templates/){: .btn }
[Playbooks](playbooks/){: .btn }

## Where we are today

- ✅ Prompt system + departmental personas  
- ✅ Docs site (playbooks/templates)  
- ✅ Voice gateway & reverse proxy (on-prem ready)  
- 🔄 DNS + firewall steps for `voice.quirkcars.com`  
- 🔜 Controlled read-only adapters (CRM/DMS)

## Near-term milestones

- Pilot go-live (1–2 stores), measure handle-time & quality  
- Expand templates (BDC, Service, F&I)  
- Add audit/reporting & change governance
