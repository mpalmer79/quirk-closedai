# DG-AI Architecture Overview
_Dealer Group Closed AI Assistant_

---

## 1. High-Level Diagram (Text)

[Dealership Staff / Customer Inputs]
|
v
+---------------------+
| FastAPI Gateway |
| (src/server.py) |
+---------------------+
|
v
+-------------------------+
| Prompt Loader |
| - system_prompt.md |
| - meta_prompt.md |
| - department subprompts|
+-------------------------+
|
v
+-------------------------+
| Local AI Model Server |
| (OpenAI-compatible API)|
+-------------------------+
|

| |
v v
Adapters Knowledge Base
(src/adapters/) (future RAG/data layer)
|
|-- vinsolutions.py -> CRM (leads, history)
|-- dms.py -> DMS (ROs, parts, acct)
|-- oem_feeds.py -> OEM docs (incentives, recalls)


---

## 2. Components

### 🔹 FastAPI Gateway
- Entry point for all requests (`/chat`, `/health`).  
- Wraps user input with system + meta + department prompts.  
- Sends structured messages to the model server.  

### 🔹 Prompt Loader
- Reads all config files in `config/`.  
- Composes base (meta + system) + optional department sub-prompt.  
- Ensures consistency and governance across responses.  

### 🔹 Local AI Model Server
- Closed environment (on-prem).  
- Exposed via OpenAI-compatible REST API.  
- Model can be upgraded without changing app code.  

### 🔹 Adapters (`src/adapters/`)
- **VinSolutions CRM Adapter** (`vinsolutions.py`)  
  - Read-only for leads, internet sales, customer history.  
- **DMS Adapter** (`dms.py`)  
  - Read-only for repair orders, service history, parts inventory.  
- **Future Adapters**  
  - `oem_feeds.py` for mirrored OEM incentives, recall data.  
  - `eleads.py` if multiple CRMs in use.  

### 🔹 Knowledge Base (Future)
- Centralized repo of SOPs, OEM policies, dealership playbooks.  
- Can be exposed via vector database + retrieval-augmented generation (RAG).  

---

## 3. Security Layers
- On-prem hosting; no external internet calls unless explicitly whitelisted.  
- `.env` holds API keys/creds (ignored in git).  
- TLS for all traffic; RBAC for adapter access.  
- Logs store metadata only (no PII).  

---

## 4. Department Flow (Example)

**Sales Lead → DG-AI**
1. BDC agent enters lead context.  
2. FastAPI wraps with `system + meta + sales.md`.  
3. Model generates compliant, branded first-response.  
4. (Optional) Adapter pulls CRM lead history for grounding.  

**Service RO Update → DG-AI**
1. Advisor requests status update draft.  
2. FastAPI wraps with `system + meta + service.md`.  
3. DMS adapter fetches RO details.  
4. Model generates update message for customer.  

---

## 5. Next Steps
- Add Mermaid diagram for auto-render in GitHub.  
- Extend adapters with mock endpoints for dev/test.  
- Link architecture doc to `README.md`.  

