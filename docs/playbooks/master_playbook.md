# Dealer Group Master Playbook (`docs/playbooks/master_playbook.md`)

*This master playbook unifies all departmental SOPs (Sales, Service, F\&I, Parts, Accounting, BDC, Marketing, Executive) into one cross‑functional reference. It is designed for group‑wide alignment and AI‑powered support.*

---

## 1. Purpose

* Provide a single source of truth for all dealership operations.
* Ensure consistency across rooftops and brands.
* Define escalation paths and KPIs group‑wide.
* Enable AI assistant to support cross‑department workflows.

---

## 2. Department Summaries

### Sales

* Internet/phone lead response within 15 minutes.
* Showroom process: greet → needs analysis → demo → write‑up.
* Trade appraisal: sight unseen (form) or in‑person.
* Closing → warm handoff to F\&I.
* KPIs: lead response time, appointment show %, closing ratio, gross per unit.

### Service

* Appointment confirmation with transportation options.
* Write‑up: confirm concerns, walkaround, MPI.
* Estimate approval via text/email templates.
* RO closure: QC, invoice, pickup message.
* KPIs: hours/RO, ELR, CSI, first contact resolution.

### F\&I

* Warm handoff from Sales.
* Credit application & lender selection.
* Product menu presentation (100% disclosure).
* Contracting & CIT monitoring.
* KPIs: product penetration %, per‑copy gross, CIT aging, compliance exceptions.

### Parts

* Retail counter sales & service RO support.
* Wholesale order processing & delivery.
* Inventory management, obsolescence control.
* Returns, cores, special orders.
* KPIs: parts gross %, fill rate, AR aging, obsolescence %.

### Accounting

* Deal posting & reconciliation.
* Contracts in Transit monitoring.
* DMV/titling submissions.
* Monthly financial statement preparation.
* KPIs: CIT aging, warranty receivable aging, statement timeliness, audit findings.

### BDC

* Internet/phone lead handling.
* Appointment setting for sales & service.
* No‑show handling.
* Equity mining & declined work campaigns.
* KPIs: lead response time, appointment set vs. show %, declined work conversion.

### Marketing

* Monthly campaign calendar aligned with GSMs/Directors.
* Creative development with OEM compliance.
* Digital marketing: paid search, display, social.
* Email & CRM campaigns.
* KPIs: CPL, ROI, lead conversions, campaign performance.

### Executive / GM

* Daily AI dashboard review.
* Weekly KPI review meetings.
* Monthly financial statement analysis.
* Quarterly governance & compliance audit.
* KPIs: consolidated sales/service/F\&I/parts/accounting performance.

---

## 3. Cross‑Department Escalations

* **Lead aging >24h:** escalate to BDC Manager → GSM → GM.
* **CIT aging >10 days:** escalate to F\&I Manager → Controller → GM.
* **Warranty receivable >30 days:** escalate to Service Manager → Service Director → Exec.
* **Parts backorder >14 days:** escalate to Parts Manager → Fixed Ops Director.
* **CSI drop >5 points:** escalate to Service Manager → GM → Exec.
* **Compliance violation:** escalate immediately to Compliance Officer → Dealer Principal.

---

## 4. Group‑Wide KPIs

* **Sales:** Response time, closing ratio, gross per unit.
* **Service:** Hours/RO, ELR, CSI.
* **Parts:** Fill rate, obsolescence %.
* **F\&I:** Product penetration %, per‑copy gross, CIT aging.
* **Accounting:** Statement timeliness, reconciliation accuracy.
* **BDC:** Appointment show %, conversion rates.
* **Marketing:** CPL, ROI, conversion rates.
* **Executive:** Consolidated P\&L, CSI trends, compliance scorecard.

---

## 5. AI Assistant Integration

* AI loads correct persona (`config/prompts/`) per department.
* AI references playbooks (`docs/playbooks/`) for workflows/SOPs.
* AI enforces governance rules (`docs/governance.md`).
* AI generates executive summaries & alerts for outliers.

---

## 6. Continuous Improvement Cadence

* **Daily:** AI dashboard alerts + manager reviews.
* **Weekly:** Department huddles (Sales, Service, Parts, F\&I, BDC, Marketing).
* **Monthly:** GM + Executive financial/ops review.
* **Quarterly:** Governance & compliance audit.
* **Annual:** Strategic planning session with Dealer Principals.

---

## Quick Reference Snippets

* "Group response time for internet leads is {{minutes}} minutes vs. target {{target}}."
* "CIT aging for the group is {{days}} days—exceeds target, escalation triggered."
* "CSI dropped {{points}} points this month due to {{root\_cause}}. Action plan: {{steps}}."

---

*End of Dealer Group Master Playbook v1*
