---
title: Security Posture
parent: Quirk AI — Corporate Overview
nav_order: 4
---

# Security Posture

## Data handling
- P1: **read-only** adapters (CRM/DMS); no direct writes
- No long-term storage of PII; redaction of VIN/email/phone in logs
- Encrypted in transit (TLS); on-prem isolation

## Network
- Cloudflare DNS → `voice.quirkcars.com` → Caddy (TLS) → Gateway
- Inbound ports: 80/443 only; outbound to OpenAI/Twilio APIs
- Role-based OS access; SSH keys only

## Logging & audit
- Minimal application logs; no raw audio persisted
- Prompt changes via PR; changelog + tests prevent drift

## Secrets
- `.env` mounted at runtime; never committed
- Rotation documented in Ops runbook

## Compliance
- OEM brand voice enforcement in prompts
- TCPA/UDAP-aligned templates; opt-out handling in SMS
- Quarterly review with ops & IT

**Docs**: [Infra baseline](../infra/security-baseline.md) • [Install](../infra/server-install.md)
