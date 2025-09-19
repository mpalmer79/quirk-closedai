# Quirk AI — On-Prem Server (Infra Index)

This section documents how to stand up the **corporate, on-prem** Quirk AI stack.

**What you’ll deploy (MVP)**
- **Voice Gateway (FastAPI/UVicorn)** — our Twilio/OpenAI bridge  
- **Reverse Proxy (Caddy)** — TLS, HTTP→WS proxy for `voice.quirkcars.com`
- **System hardening + ops** — firewall, logs, backups, updates

**Environments**  
- `pilot` (single node) → `prod` (HA later)

**Quick links**
- [Server Bill of Materials](./server-install.md#1-bill-of-materials)  
- [Step-by-step Install](./server-install.md#2-step-by-step-install)  
- [Network & Security Baseline](./security-baseline.md)  
- [Ops Runbook](../ops/runbook.md)
