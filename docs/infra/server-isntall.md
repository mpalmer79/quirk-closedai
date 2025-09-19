---
title: On-Prem Install — Step by Step (Ubuntu 22.04 LTS)
nav_order: 10
---

# On-Prem Install — Step by Step (Ubuntu 22.04 LTS)

This guide brings **Quirk AI Voice (pilot)** online on one Ubuntu server using Docker:
- **Caddy** (TLS reverse proxy) → `https://voice.quirkcars.com`
- **Voice Gateway** (FastAPI) bridging **Twilio Media Streams ↔ OpenAI Realtime**

Only **TCP 80/443** are exposed inbound. No raw audio is stored.

---

## 0) Before you start

- **Domain**: `voice.quirkcars.com` in Cloudflare  
  - **A record**: `voice → <PUBLIC_IP>`  
  - **Proxy**: **DNS only** (gray cloud)  
  - (Optional) **CAA**: `issue letsencrypt.org`
- **Firewall/NAT**: Port-forward TCP **80** and **443** from `<PUBLIC_IP>` → the server’s **LAN IP**.
- **Credentials**:
  - GitHub (read access to this repo)
  - **OpenAI API key**
  - **Twilio** phone number (you will add a small TwiML later)

**Recommended server sizing (pilot)**: 4–8 vCPU, 16–32 GB RAM, 250 GB SSD, Ubuntu **22.04 LTS**, static LAN IP.

---

## 1) Base server setup

Log into the Ubuntu box as an administrator.

```bash
# updates & basics
sudo apt update && sudo apt -y upgrade
sudo apt -y install unattended-upgrades fail2ban ufw curl ca-certificates gnupg

# timezone (adjust as needed)
sudo timedatectl set-timezone America/New_York

# firewall: SSH + 80/443
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw --force enable
