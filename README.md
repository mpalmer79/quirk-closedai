# Quirk AI 
_On-premises corporate server for Quirk Auto Dealers_

This repository is the working blueprint to deploy a **closed, on-premise** server that improves efficiency, consistency, and profitability across **Sales, Service, Parts, F&I, BDC, and Marketing**—while safeguarding data and meeting OEM/regulatory requirements.

---

## What’s included

- **Prompt System**
  - `config/system_prompt.md` – master system style/guardrails  
  - `config/meta_prompt.md` – how the assistant plans/asks for missing info  
  - `config/prompts/*` – department personas & SOP hooks (Sales, Service, Marketing, Finance, Voice)
- **Voice (Realtime)**
  - FastAPI gateway that bridges **Twilio Media Streams ↔ OpenAI Realtime**
  - Reverse proxy (Caddy) with automatic TLS for `voice.quirkcars.com`
- **Docs site** (GitHub Pages, Just-the-Docs)
  - Templates (email/SMS), department playbooks, governance, infra how-tos, runbooks
- **Tests**
  - Prompt smoke tests and examples to keep tone/compliance from drifting

---

## Phase-1 Scope (pilot)

- Internal copilots for BDC, Internet Sales, Showroom, Service Writers, Parts, Marketing  
- Text generation, summarization, classification, checklists, guided forms  
- **Read-only** adapters to CRM/DMS (e.g., VIN Solutions), inventory feeds, site forms

**Out of scope (P1):** direct DMS/CRM writes; public internet access; autonomous actions without human review.

---

## Goals & guardrails

**Primary goals**
- Reduce handle time on common tasks by **30–50%** within 90 days  
- Standardize tone & compliance across stores/brands  
- Centralize SOPs → reusable prompts

**Safety constraints**
- On-prem hosting; no PII leaves the network  
- Encryption in transit; logging with **redaction** (VIN/email/phone)  
- OEM voice + legal/TCPA/UDAP compliance

**Governance**
- PR-based prompt changes, changelog, prompt tests

---

## Quick start

### A) Docs site (already live via GitHub Pages)
- The site builds from `/docs`. Push a commit to update it.
- Local preview (optional):
  ```bash
  # requires Ruby/Jekyll, optional for contributors
  bundle install
  bundle exec jekyll serve --livereload

### DNS + networking (summary)
  Cloudflare DNS → A record: voice → <public_IP> (DNS only, gray cloud)

Open firewall/NAT: forward TCP 80/443 → proxy host (Caddy)

Caddy auto-issues TLS via Let’s Encrypt (needs port 80 reachable)

Detailed steps live in docs/infra/.

## Environmental variables

| Key                     | Where            | Purpose                                                                |
| ----------------------- | ---------------- | ---------------------------------------------------------------------- |
| `OPENAI_API_KEY`        | `.env` / secrets | API key for Realtime/Chat                                              |
| `OPENAI_REALTIME_MODEL` | `.env`           | Realtime model name (e.g., `gpt-realtime-preview`)                     |
| `SYSTEM_PROMPT_PATH`    | `.env`           | Path to system instructions (default `config/prompts/voice_system.md`) |
| `BIDIRECTIONAL_STREAMS` | `.env`           | `true/false` for Twilio media return path                              |
| `DOMAIN`                | `deploy/.env`    | Public FQDN (e.g., `voice.quirkcars.com`)                              |
| `LETS_ENCRYPT_EMAIL`    | `deploy/.env`    | ACME contact for TLS issuance                                          |

## License

Apache-2.0. See LICENSE.

## Repository structure (displays much better in Code view)

</pre>
quirk-closedai/
├─ config/
│  ├─ system_prompt.md
│  ├─ meta_prompt.md
│  └─ prompts/
│     ├─ sales.md
│     ├─ service.md
│     ├─ marketing.md
│     ├─ finance.md
│     └─ voice_system.md
├─ docs/
│  ├─ index.md                           # site home (Just-the-Docs)
│  ├─ templates/                         # CRM-ready email/SMS bundles
│  │  └─ sales/index.md
│  ├─ playbooks/                         # departmental SOPs
│  ├─ voice/
│  │  ├─ overview.md
│  │  └─ quickstart.md
│  ├─ infra/
│  │  ├─ server-install.md
│  │  ├─ security-baseline.md
│  │  └─ dns-cloudflare.md
│  └─ ops/
│     └─ runbook.md
├─ src/
│  └─ voice_gateway/
│     ├─ server.py                       # Twilio WS endpoint (/realtime/twilio)
│     ├─ openai_bridge.py                # OpenAI Realtime websocket client
│     ├─ audio_utils.py                  # μ-law/PCM helpers, resampling
│     └─ policy.py                       # redaction utils (VIN/email/phone)
├─ tests/
│  └─ test_prompts.py
├─ deploy/
│  ├─ compose.yml                        # Caddy + Gateway stack
│  ├─ gateway.Dockerfile
│  ├─ .env.example
│  └─ caddy/
│     └─ Caddyfile
├─ .env.example
├─ requirements.txt
├─ .gitignore
├─ LICENSE
└─ README.md


