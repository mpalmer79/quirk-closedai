---
title: Quirk AI — Overview
nav_order: 1
---

<!-- Layout: full-width frame (minus sidebar) with centered main + right-aside -->
<style>
  /* Fallbacks in case these aren't set globally */
  :root{
    --quirk-sidebar-width: 340px;   /* must match your left nav width */
    --quirk-gutter: 24px;           /* page edge padding (match left edge feel) */
  }

  /* Frame spans from the right edge of the sidebar to the right edge of viewport */
  .home-wrap{
    width: calc(100vw - var(--quirk-sidebar-width));
    margin-left: auto;                  /* anchor to the right side of the page */
    padding-right: var(--quirk-gutter); /* equal breathing room at right edge   */
  }

  /* Two columns: centered main (flexible) + fixed-width aside (card) */
  .home-split{
    display: grid;
    grid-template-columns: minmax(0, 1fr) 320px; /* main | aside */
    gap: 2rem;
    align-items: start;
  }

  /* Center the readable main column inside its grid area */
  .home-main{
    max-width: 960px;
    margin-left: auto;
    margin-right: auto;
  }

  /* Sticky right-hand card */
  .home-aside{
    position: sticky; top: 1rem;
    border: 1px solid #e5e7eb; border-radius: 12px;
    padding: 16px; background: #f8fbff;
  }
  .home-aside h3{ margin: .25rem 0 .25rem; }
  .home-aside .meta{ color:#6b7280; font-size:.9rem; margin:-.1rem 0 .5rem; }
  .home-aside .btn{ display:inline-block; margin-top:.5rem; }

  /* Hero/readability */
  .home-hero h1{ margin-top:.25rem; margin-bottom:.25rem; }
  .home-hero .lead{ font-size:1.1rem; color:#374151; }
  .btn-row{ display:flex; flex-wrap:wrap; gap:.5rem; margin:.75rem 0 1rem; }

  /* Mobile: collapse to one column, add side paddings */
  @media (max-width: 992px){
    .home-wrap{
      width: 100vw;
      padding-left: var(--quirk-gutter);
      padding-right: var(--quirk-gutter);
    }
    .home-split{ grid-template-columns: 1fr; }
    .home-aside{ order: 2; } /* show aside after the main on small screens */
  }
</style>

<div class="home-wrap">
  <div class="home-split">

    <!-- markdown="1" ensures headings/links render inside this div -->
    <div class="home-main" markdown="1">

<div class="home-hero">

# Quirk AI

<span class="lead">
Quirk AI is our **on premise corporate assistant** that improves speed, consistency, and compliance across the dealer group while **keeping customer data private**.
</span>

{: .note }
**Phase-1 focus**: Internal copilots for BDC, Sales, Service Writers, Parts, and Marketing. Read-only adapters to CRM/DMS (e.g., VIN Solutions). Voice pilots via Twilio → OpenAI Realtime.
</div>

## Why it matters (business outcomes)

- **Response speed:** cut handling time for common tasks by **30–50%**
- **Consistency:** one brand voice, compliant across **13 OEMs / 20 stores**
- **Quality:** better lead follow-up, clearer repair notes, fewer escalations
- **Privacy:** on premise isolation; PII redaction in logs

## Quick links
<div class="btn-row">
  <a class="btn btn-primary" href="overview/exec.html">Executive Brief</a>
  <a class="btn" href="overview/architecture.html">Architecture</a>
  <a class="btn" href="overview/security.html">Security Posture</a>
  <a class="btn" href="templates/">Templates</a>
  <a class="btn" href="playbooks/">Playbooks</a>
</div>

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

    </div><!-- /home-main -->

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

      <p><strong>Replace Cloudflare?</strong> Yes for DNS (registrar or self-host). WAF/DDoS/CDN require alternatives (Nginx+ModSecurity, ISP scrubbing) or accepting the risk.</p>

      <a class="btn btn-primary" href="infra/nh-on-premise.html">Read the NH plan →</a><br>
      <a class="btn" href="infra/server-install-on-premise.html">On Premise Install guide →</a>
    </aside>

  </div><!-- /home-split -->
</div><!-- /home-wrap -->
