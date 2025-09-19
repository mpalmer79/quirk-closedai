---
title: NH On Premise Server — Plan
nav_order: 12
---

# NH On Premise Server — Plan

This page is the deployment plan for a New Hampshire regional node that runs the Quirk AI voice gateway **on premise**.

---

## What stays on premise vs. cloud

**On premise (NH node)**
- Caddy reverse proxy (TLS) at `https://voice.quirkcars.com`
- Voice Gateway (FastAPI) bridging Twilio Media Streams ↔ OpenAI Realtime
- Policy/redaction (VIN/email/phone) and minimal, redacted logs
- Optional: private document store (RAG) for SOPs/policies you don’t want off-site

**Cloud/SaaS**
- Twilio phone number + Media Streams
- OpenAI API (Realtime + text)
- Optional: uptime monitors, SIEM/log analytics, off-site backups (non-PII)

---

## Can we replace Cloudflare?

**Yes for DNS.** Options:
- Keep Cloudflare as **DNS-only** (gray cloud) — simple and reliable for pilot.
- Move DNS to registrar or self-hosted authoritative DNS (Bind/NSD/PowerDNS).  
  If you self-host DNS, plan for **2+ name servers**, monitoring, and consider DNSSEC.

**TLS/Proxy:** handled on premise by **Caddy** (Let’s Encrypt).  
**WAF/DDoS/CDN:** Cloudflare adds protections you would need to replace (e.g., Nginx+ModSecurity with OWASP CRS, or an ISP scrubbing service). The voice workflow usually does not need CDN.

---

## Architecture (NH)

