---
title: Quirk AI — Overview
nav_order: 1
---

<!-- Home-page only: center the content text while keeping paragraphs/lists readable -->
<style>
  .home-center { text-align: center; }
  /* Keep blocks readable (left text) but center them as units */
  .home-center > * {
    max-width: 960px;
    margin-left: auto;
    margin-right: auto;
  }
  .home-center p,
  .home-center .note,
  .home-center ul,
  .home-center ol,
  .home-center pre,
  .home-center code,
  .home-center .highlighter-rouge {
    display: inline-block;
    text-align: left;
    width: auto;            /* shrink to content; still capped by max-width above */
  }
  /* Button row centers nicely */
  .home-center .btn { display: inline-block; }
</style>

<div class="home-center">

# Quirk AI

Quirk AI is our **on-premise corporate assistant** that improves speed, consistency, and compliance across the dealer group while **keeping customer data private**.

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

</div>
