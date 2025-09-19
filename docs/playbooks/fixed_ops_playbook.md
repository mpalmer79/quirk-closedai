# Fixed Ops Department Playbook (`docs/playbooks/fixed_ops_playbook.md`)

*This playbook covers **Service, Parts, and Collision/Body Shop** operations, aligning with sub‑personas in `config/prompts/` and providing department‑wide SOPs.*

---

## 1. Service Operations (Summary)

### Workflow: End‑to‑End RO Lifecycle

1. Appointment booked → confirmation sent.
2. Customer check‑in → walkaround, concern capture, op‑codes.
3. Tech diagnosis → advisor builds estimate.
4. Customer approval → RO updated, parts sourced.
5. Work completed → QC/test drive.
6. Invoice prepared → payment processed.
7. Pickup → customer feedback request.

**SOP Notes:**

* Always capture contact preference.
* Use MPI to identify upsell/retention opportunities.
* Escalate safety issues immediately.

(See `service_playbook.md` for full workflows.)

---

## 2. Parts Operations

### Workflow: Parts Counter Sale

1. Receive customer/technician request.
2. Verify part number in DMS/catalog.
3. Check stock → pull or order if out.
4. Quote price + availability.
5. Invoice & collect payment (retail) or charge to RO (internal).

**SOP Notes:**

* Verify VIN for correct part fitment.
* Track special orders; collect deposits.

### Workflow: Parts Inventory Control

1. Conduct daily bin counts for fast‑moving items.
2. Post receipts in DMS same day.
3. Reconcile inventory monthly.
4. Report variances >\$100 to Parts Manager.

**SOP Notes:**

* Use perpetual inventory practices.
* Rotate stock; return obsolete parts.

### Workflow: Wholesale Parts Order

1. Receive order via phone/fax/portal.
2. Verify credit/account status.
3. Pick, invoice, and prepare delivery.
4. Route via delivery driver or ship.

**SOP Notes:**

* Maintain delivery log.
* Follow up on AR balances >30 days.

---

## 3. Collision / Body Shop Operations

### Workflow: Estimating & Intake

1. Greet customer; collect insurance/lienholder info.
2. Perform walkaround + photos.
3. Write estimate in CCC/Mitchell/Alldata.
4. Submit to insurer for approval.
5. Schedule repair and parts order.

**SOP Notes:**

* Use OEM repair procedures when available.
* Document all supplements clearly.

### Workflow: Repair Process

1. Disassemble → identify hidden damage.
2. Update insurer/customer on supplements.
3. Complete structural, mechanical, body, paint work.
4. QC inspection + alignment checks.
5. Clean vehicle; stage for delivery.

### Workflow: Delivery

1. Review repairs with customer.
2. Collect deductible/payment.
3. Provide warranty info.
4. Close RO in DMS.

**SOP Notes:**

* Maintain CSI by proactive updates.
* Track cycle time (keys‑to‑keys metric).

---

## 4. Fixed Ops Cross‑Department Processes

### Workflow: Warranty Claim Submission

1. Service Advisor completes RO with proper op‑codes.
2. Warranty Clerk verifies labor ops, parts numbers, story.
3. Submit to OEM portal.
4. Track claim aging; resolve rejections.

**SOP Notes:**

* Claims >30 days = escalation.
* OEM audits require detailed causals/corrections.

### Workflow: Customer Pay + Parts Integration

1. Service Advisor sells recommended work.
2. Parts Department verifies part # and availability.
3. Parts charged to RO; labor added.
4. Invoice reflects both accurately.

**SOP Notes:**

* Communication between departments critical.
* Always confirm ETA with parts before quoting.

---

## 5. Escalation Handling

* **Safety Concern:** Do not release vehicle; offer tow/loaner; escalate to manager.
* **Parts Backorder >14 days:** Notify customer weekly; escalate to Fixed Ops Director.
* **Collision Supplements >20% original estimate:** Notify insurer and customer immediately.
* **Warranty Rejection:** Escalate to Warranty Administrator + Service Director.

---

## 6. KPIs & Continuous Improvement

* **Service:** ELR, Hours/RO, CSI, First Contact Resolution.
* **Parts:** Gross profit %, fill rate, obsolescence %, wholesale AR aging.
* **Collision:** Cycle time, CSI, supplement ratio, gross profit %.
* **Cross‑Dept:** Warranty receivable aging, parts‑to‑labor ratio.

**Continuous Improvement Cadence:**

* Weekly advisor/parts/collision huddle → CSI & backlog review.
* Monthly Fixed Ops Director meeting → KPIs, warranty aging, comebacks.

---

## Quick Reference Snippets

* "Your part is on order; ETA {{date}}. We’ll notify as soon as it arrives."
* "Insurance approved supplement #{{id}}; repairs continue, ETA {{date}}."
* "Our goal is to complete {{repairs}} by {{eta}}; we’ll update you if that changes."

---

*End of Fixed Ops Department Playbook v1*

