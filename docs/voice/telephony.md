---
title: Telephony Integration (Pilot)
nav_order: 2
---

# Quirk AI Voice — Telephony (Pilot)

This page shows how to point a **pilot phone number** at your on-prem **Quirk Voice Gateway** so it can stream audio to/from the **OpenAI Realtime API**.

> **You will not commit any secrets here.** DNS, TLS certs, and Twilio auth tokens live outside the repo.

---

## 1) Prerequisites

- A public DNS name for your gateway, e.g. **`voice.quirkcars.com`**
- Valid TLS (Let’s Encrypt is fine) so you can accept **WSS** (secure WebSockets)
- Your gateway running the **FastAPI** app from `src/voice_gateway/server.py` (default `/realtime/twilio` WS route)
- A **pilot phone number** (Twilio recommended for the first test)

---

## 2) Reverse proxy (Nginx) for WebSocket

Point your public DNS to the reverse proxy in front of the gateway, then add this Nginx block:

```nginx
server {
  server_name voice.quirkcars.com;
  listen 443 ssl http2;

  # TLS
  ssl_certificate     /etc/letsencrypt/live/voice.quirkcars.com/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/voice.quirkcars.com/privkey.pem;

  # WebSocket → FastAPI (local)
  location /realtime/twilio {
    proxy_pass              http://127.0.0.1:8080;  # FastAPI host:port
    proxy_http_version      1.1;
    proxy_set_header        Upgrade $http_upgrade;
    proxy_set_header        Connection "Upgrade";
    proxy_set_header        Host $host;
    proxy_read_timeout      3600s;
  }

  # Optional: health check
  location /health {
    proxy_pass http://127.0.0.1:8080/health;
  }
}

