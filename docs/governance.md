# Governance & Security Policy  
_Dealer Group Closed AI Assistant (DG-AI)_

---

## 1. Purpose
This document defines how prompts, adapters, and workflows are governed, tested, and secured in the DG-AI environment. It ensures consistency, compliance, and protection of customer and enterprise data across all dealerships and brands.

---

## 2. Change Control
- **Prompt Changes**
  - All edits to `config/` prompts (system, meta, department sub-prompts) must be submitted as a Pull Request (PR).
  - Required reviewers: at least one **IT approver** and one **Operations approver**.
  - PR must include description of intent, scope, and impact.
- **Code Changes**
  - All modifications to `src/` must pass automated tests in `tests/` before merging.
  - Breaking changes must include an updated entry in `docs/changelog.md`.

---

## 3. Access Control
- **Developers:** Full read/write to code and prompts via GitHub.
- **Ops Leadership:** Read access to prompts/docs; review role on PRs.
- **Dealership Staff:** Access to compiled AI application only, no repo access.
- **Secrets:** `.env` files never committed to Git. API keys and credentials managed via secure vault (on-prem or enterprise secrets manager).

---

## 4. Data Handling
- No customer PII (names, emails, phone, VINs, financials) stored in AI logs.
- Logs may contain metadata only: timestamp, department, token counts, success/failure.
- If debugging requires message bodies, masking must be applied first.
- Data never leaves the on-prem environment; no external API calls unless explicitly whitelisted.

---

## 5. Security
- All traffic encrypted in transit (TLS).
- Data encrypted at rest in local DB or storage volumes.
- Role-based permissions for adapters (CRM/DMS) to enforce least-privilege access.
- Regular audit of adapter logs for unauthorized use.

---

## 6. Testing & QA
- Automated tests in `tests/` ensure:
  - Prompts contain required sections (Purpose, Inputs, Outputs, Quality gates).
  - Adapters return safe mock data when APIs unavailable.
  - Governance policy is referenced in `README.md`.
- Quarterly prompt review cycle with IT + Ops.

---

## 7. Compliance
- All outputs must align with:
  - OEM brand guidelines.
  - TCPA (Telephone Consumer Protection Act).
  - UDAP (Unfair and Deceptive Acts and Practices).
  - State & federal privacy laws (e.g., GLBA, CCPA if applicable).
- Compliance exceptions must be flagged and escalated.

---

## 8. Versioning & Documentation
- `docs/changelog.md` maintained with every significant change.
- Repo tags/releases created at major milestones (P1 Pilot, P2 Rollout, etc.).
- Architecture diagrams maintained in `docs/architecture.md`.

---

## 9. Governance Roles
- **Prompt Maintainer:** Ensures prompt quality, approves changes.
- **Adapter Maintainer:** Owns integration layer security and correctness.
- **Ops Reviewer:** Confirms outputs align with store processes.
- **IT Security Reviewer:** Validates data handling and access control.

---

## 10. Review Cycle
- Weekly: PR review sync (if pending).
- Monthly: Adapter/API security check.
- Quarterly: Prompt/Persona review & compliance audit.

---

