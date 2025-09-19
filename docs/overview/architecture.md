---
title: Architecture (At a Glance)
parent: Quirk AI — Corporate Overview
nav_order: 3
---

# Architecture (At a Glance)

**Goal:** keep customer data private while enabling fast, consistent assistance.

PSTN/Cell
│
▼
Twilio Phone Number
│ (TwiML: <Connect><Stream/>)
▼
Twilio Media Streams ⇄ WSS
│
▼
[Caddy TLS Proxy] — https://voice.quirkcars.com

│ (TLS, WS upgrade)
▼
[Voice Gateway (FastAPI/UVicorn)]
├─ Policy / Redaction (VIN/email/phone)
├─ Logging (minimal, redacted)
├─ Read-only Adapters: CRM/DMS (VIN Solutions, DMS, inventory)
└─ OpenAI Realtime (secure outbound)


**Key properties**
- **On-premises** reverse proxy and gateway; no inbound to model providers  
- **Least-privilege** adapters (read-only in P1)  
- **Auditability**: prompt governance + minimal redacted logs  
- **Replaceable**: proxy/gateway are standard Docker services

**Runbooks & install**
- Infra install: `docs/infra/server-install.md`  
- Ops runbook: hidden page for operators
