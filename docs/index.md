---
title: Quirk AI — Overview
nav_order: 1
---

<!-- Home-page split layout (main content + right-side info panel) -->
<style>
  /* two-column split only inside the content area */
  .home-split {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 320px; /* main | right panel */
    gap: 2rem;
    align-items: start;
  }
  @media (max-width: 992px) {
    .home-split { grid-template-columns: 1fr; }
    .home-aside { order: 2; }
  }
  .home-aside {
    position: sticky; top: 1rem;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 16px;
    background: #f8fbff; /* light blue card */
  }
  .home-aside h3 { margin-top: 0; }
  .home-aside .meta { color: #6b7280; font-size: .9rem; margin-top: -.25rem; }
  .home-aside ul { margin-top: .5rem; }
  .home-aside .btn { display: inline-block; margin-top: .5rem; }
</style>

<div class="home-split">

<div class="home-main">

# Quirk AI

Quirk AI is our **on premise corporate assistant** that improves speed, consistency, and compliance across the dealer group while **keeping customer data private**.

{: .note }
**Phase-1 focus**: Internal copilots for BDC, Sales, Service Writers, Parts, and Marketing. Read-only adapters to CRM/DMS (e.g., VIN Solutions). Voice pilots via Twilio → OpenAI Realtime.

## Why it matters (business outcomes)

- **Response speed**: cut handling time for common tasks by **30–50%**
- **Consistency**: one brand voice, compliant across **13 OEMs / 20 stores**
- **Quality**: better lead follow-up, clearer repair notes, fewer escalations
- **Privacy**: on premise isolation; PII redaction in logs

## Quick links
[Executive Brief](overview/exec.md){: .btn .btn-primary }
[Architecture](overview/architecture.md){: .btn }
[Security Posture](overview/security.md){: .btn }
[Templates](templates/){: .btn }
[Playbooks](playbooks/){: .btn }

## Where we are today

- ✅ Prompt system + departmental personas  
- ✅ Docs site (playbooks/templates)  
- ✅ Voice gateway & reverse proxy (on premise ready)  
- 🔄 DNS + firewall steps for `voice.quirkcars.com`  
- 🔜 Controlled read-only adapters (CRM/DMS)

## Near-term milestones

- Pilot go-live (1–2 stores), measure handle-time & quality  
- Expand templates (BDC, Service, F&I)  
- Add audit/reporting & change governance

</div>

<aside class="home-aside">
  <h3>NH On Premise Server</h3>
  <div class="meta">Deployment for New Hampshire dealerships</div>
  <p><strong>Goal:</strong> keep voice + CRM context local, with a hardened egress path to Twilio/OpenAI.</p>
  <ul>
    <li><strong>DNS:</strong> keep Cloudflare in <em>DNS-only</em> (gray) for pilot, or move to registrar/self-hosted DNS later.</li>
    <li><strong>TLS/Proxy:</strong> on premise Caddy terminates TLS at <code>https://voice.quirkcars.com</code>.</li>
    <li><strong>Firewall:</strong> inbound <code>80/443</code> → proxy; egress allow-list to Twilio/OpenAI/Let’s Encrypt.</li>
    <li><strong>PII:</strong> redact names/phones/emails in logs; no raw audio stored.</li>
  </ul>
  <p><strong>Replace Cloudflare?</strong> Yes for DNS (registrar or self-host). WAF/DDoS/CDN features require alternatives (Nginx+ModSecurity, ISP scrubbing) or you accept the risk.</p>

  <a class="btn btn-primary" href="infra/nh-on-premise.html">Read the NH plan →</a><br>
  <a class="btn" href="infra/server-install-on-premise.html">On Premise Install guide →</a>
</aside>

</div>
