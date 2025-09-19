---
title: Voice Quickstart
nav_order: 3
---

# Quirk AI Voice — Quickstart

## 1) Configure & run the gateway
```bash
cp .env.example .env
# edit .env with your API key + model
pip install -r requirements.txt
uvicorn src.voice_gateway.server:app --host 0.0.0.0 --port 8080
