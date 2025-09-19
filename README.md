Project Name: Dealer Group Closed AI Assistant (DG‑AI)

Purpose: Stand up an on‑prem, closed AI assistant that improves efficiency, consistency, and profitability across sales, service, parts, finance, and marketing while safeguarding data and complying with OEM and regulatory requirements.

Scope (Phase 1):

Internal assistance for BDC, Internet Sales, Showroom, Service Writers, Parts, and Marketing.

Text generation, summarization, classification, checklisting, and form guidance.

Read‑only or controlled adapters to CRM (e.g., VIN Solutions), DMS, inventory feeds, and website forms.

Out‑of‑Scope (Phase 1):

Direct database writes to DMS/CRM.

Public web access; model remains closed/offline (except whitelisted OEM docs if mirrored on‑prem).

Autonomous actions without human review.

Primary Goals:

Reduce handle time for common tasks by 30–50% within 90 days of pilot.

Standardize tone and compliance across stores/brands.

Centralize knowledge (playbooks, SOPs, scripts) into reusable prompts.

Constraints:

On‑prem hosting, no PII leaves network; encryption at rest and in transit.

OEM brand voice, legal/regulatory compliance (TCPA, UDAP, etc.).

Key Stakeholders: IT (infra/security), Operations leadership, GSMs/FSMs, BDC Managers, Service Directors, Marketing.

Success Metrics: SLA response speed, adoption by department, CSAT (internal), lead response quality (external), rework/QA defects, compliance exceptions.

Risks & Mitigations:

Hallucination → strict system prompt, retrieval grounding, uncertainty handling.

Data exposure → on‑prem isolation, role‑based access, logging, redaction.

Drift → PR‑based prompt governance, change log, test harness.

Phasing:

P1 (0–4 wks): Internal copilots + prompt repo; read‑only adapters.

P2 (5–12 wks): Department playbooks, basic automations; limited write‑backs with approvals.

P3 (13+ wks): Expanded automations, reporting, A/B tests, broader integrations.
