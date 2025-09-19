# DNS (Cloudflare) — voice.quirkcars.com

## A record
- Type: **A**
- Name: **voice**
- IPv4: **50.225.38.134**   # replace if your inbound IP differs
- Proxy status: **DNS only** (gray)
- TTL: Auto

## CAA (optional, recommended)
- Type: **CAA**
- Name: **@**
- Tag: **issue**
- Value: **letsencrypt.org**

## Verify
```bash
# Windows
nslookup voice.quirkcars.com
# macOS/Linux
dig +short voice.quirkcars.com
