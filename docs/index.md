---
title: Quirk AI — Overview
nav_order: 1
---

<!-- Page-only layout overrides (works without any global include) -->
<style>
  /* Sidebar width you want (tweak 320–420px to taste) */
  :root { --quirk-sidebar-width: 360px; }

  /* On desktop, override the theme's grid to widen the sidebar
     and position the main area as the second column. */
  @media (min-width: 992px) {
    /* The two-column grid container used by Just the Docs */
    .page {
      display: grid !important;
      grid-template-columns: var(--quirk-sidebar-width) minmax(0, 1fr) !important;
      column-gap: 0 !important;
    }

    /* Sidebar column */
    .side-bar {
      width: var(--quirk-sidebar-width) !important;
      max-width: var(--quirk-sidebar-width) !important;
      flex: 0 0 var(--quirk-sidebar-width) !important;
    }

    /* Main column is placed by the grid; remove any left margin hacks */
    .main { margin-left: 0 !important; }
  }

  /* Center the header/search row and the readable content column */
  .main .main-header,
  .main .main-content {
    max-width: 960px;      /* readable line length */
    margin-left: auto;
    margin-right: auto;
    padding-left: 1rem;
    padding-right: 1rem;
  }

  /* Optional: slightly tighter space under the header on this page */
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
