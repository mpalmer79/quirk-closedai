# Ops Runbook — Quirk AI (Pilot)

## Start / Stop
```bash
cd /opt/quirk/quirk-closedai/deploy
docker compose up -d         # start
docker compose ps            # status
docker compose logs -f       # tail logs
docker compose down          # stop
