# On-Prem Install — Step by Step (Ubuntu 22.04 LTS)

## 1) Bill of Materials
- 1× server (pilot): 8 vCPU, 16–32 GB RAM, 100 GB SSD, Ubuntu 22.04 LTS
- Static public IP (or NAT with port-forward 80/443)
- DNS: `voice.quirkcars.com` → your public IP
- Outbound HTTPS allowed to: OpenAI API, OS package repos, container registry

## 2) Network + DNS
- Create **A record**: `voice.quirkcars.com` → public IP
- Verify: `nslookup voice.quirkcars.com` returns your IP

## 3) OS hardening (login as admin)
```bash
# new user
sudo adduser quirkai && sudo usermod -aG sudo,docker quirkai
# firewall
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw --force enable
