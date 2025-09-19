---
title: Templates Catalog
nav_order: 10
render_with_liquid: false
---

<link rel="stylesheet" href="{{ '/assets/css/cards.css' | relative_url }}">
<script src="{{ '/assets/js/copy.js' | relative_url }}"></script>

# Templates Catalog

Copy-ready email/SMS for every department. Use the **Copy** button on any block, then replace `{{…}}` with your CRM merge fields (VinSolutions TargetFields).

<div class="cards">

<div class="card">
  <h3>Sales — Internet Lead (Email)</h3>
  <p>Fast, compliant first touch that confirms availability and proposes an appointment time.</p>
  <div class="meta">Persona: Internet Sales / BDC</div>

```md
Subject: {{FirstName}}, info on the {{Year}} {{Make}} {{Model}}

Hi {{FirstName}},

Thanks for reaching out about the {{Year}} {{Make}} {{Model}}. We have {{AvailabilitySummary}}.

Highlights:
• {{TrimOrPackage}} — {{KeyFeature1}}, {{KeyFeature2}}
• Trade-in welcome — fast, no-obligation appraisal
• Test drive on your schedule (we’re open {{HoursBrief}})

Would {{AppointmentDayTime}} work? I’ll have it pulled up and ready.

Best regards,
{{EmployeeName}} • {{StoreName}}
{{DirectPhone}} | {{Email}}

Hi {{FirstName}}, it’s {{SalespersonName}} at {{StoreName}}.
The {{Year}} {{Make}} {{Model}} you asked about is available.
Want to swing by {{AppointmentDayTime}} or pick another time?
Reply STOP to opt out.

Hi {{FirstName}}, quick update from {{StoreName}} Service —
Your {{Year}} {{Make}} {{Model}} is {{Status}}.
Estimated completion: {{ETA}}.
Reply YES to approve, or call {{ServiceNumber}} with questions.

Subject: Welcome to {{StoreName}} — Your purchase details

Hi {{FirstName}}, thanks again for choosing {{StoreName}}!
Attached are your purchase documents. If you have questions about
warranty coverage or payments, contact {{FIManager}} at {{FIPhone}}.

We’re here for you,
{{StoreName}} Finance & Insurance

Hi {{FirstName}}, your part {{PartNumber}} is ready for pickup at {{StoreName}}.
Please bring ID. Hours: {{PartsHours}}. Need shipping? Reply SHIP.

Subject: Quick favor from {{StoreName}}

Thanks again for your visit, {{FirstName}}. If we earned it,
would you consider leaving a quick review? It helps neighbors find us:
{{ReviewLink}}

If anything wasn’t 5-star, reply here and we’ll make it right.


### `docs/playbooks/index.md`
```markdown
---
title: Playbooks Catalog
nav_order: 20
---

<link rel="stylesheet" href="{{ '/assets/css/cards.css' | relative_url }}">

# Playbooks Catalog

Standard operating procedures (SOPs) by department. These align with the Quirk AI personas and templates.

<div class="cards">

<div class="card">
  <h3>BDC / Internet</h3>
  <p>Speed-to-lead, follow-up cadences, voicemail/SMS/email scripts, and escalation paths.</p>
  <a class="btn" href="bdc_playbook.html">Open BDC Playbook →</a>
</div>

<div class="card">
  <h3>Sales Department</h3>
  <p>Showroom handoffs, trade appraisal intake, pencil guardrails, and delivery checklists.</p>
  <a class="btn" href="sales_playbook.html">Open Sales Playbook →</a>
</div>

<div class="card">
  <h3>Service Department</h3>
  <p>Write-up scripts, multi-point inspection flow, approvals, ETA updates, and QA.</p>
  <a class="btn" href="service_playbook.html">Open Service Playbook →</a>
</div>

<div class="card">
  <h3>Parts Department</h3>
  <p>Counter workflows, special-order promises, returns policy, and inventory notes.</p>
  <a class="btn" href="parts_playbook.html">Open Parts Playbook →</a>
</div>

<div class="card">
  <h3>Finance & Insurance (F&I)</h3>
  <p>Menu presentation, compliance language, and post-sale welcome cadence.</p>
  <a class="btn" href="finance_playbook.html">Open F&I Playbook →</a>
</div>

<div class="card">
  <h3>Accounting</h3>
  <p>Deal posting checks, schedule review cadence, and month-end close checklist.</p>
  <a class="btn" href="accounting_playbook.html">Open Accounting Playbook →</a>
</div>

<div class="card">
  <h3>Executive</h3>
  <p>Metrics to watch, governance cadence, and expansion milestones for the pilot.</p>
  <a class="btn" href="executive_playbook.html">Open Executive Playbook →</a>
</div>

</div>
