---
title: Templates Catalog
nav_order: 10
---

<link rel="stylesheet" href="../assets/css/cards.css">
<script src="../assets/js/copy.js"></script>

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
