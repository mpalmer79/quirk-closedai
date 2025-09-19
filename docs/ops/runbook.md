---
title: Ops Runbook — Quirk AI
nav_order: 60
---

# Ops Runbook — Quirk AI (Pilot)

This runbook covers day-to-day ops for the on-prem pilot stack (Caddy proxy + Voice Gateway).

---

## Start / Stop

```bash
cd /opt/quirk/quirk-closedai/deploy

# start
docker compose up -d

# status
docker compose ps

# tail logs (all services)
docker compose logs -f

# stop
docker compose down
