#!/usr/bin/env bash
set -euo pipefail
sudo apt-get update
sudo apt-get install -y git
sudo mkdir -p /opt/quirk && sudo chown -R $USER:$USER /opt/quirk
cd /opt/quirk
git clone https://github.com/mpalmer79/quirk-closedai.git
cd quirk-closedai/deploy
cp .env.example .env
echo "Edit deploy/.env, then run: docker compose up -d"
