---
title: Templates
nav_order: 2
---

# Templates Hub

Choose a department:

- [Sales](/quirk-closedai/templates/sales/)
- [Service](/quirk-closedai/templates/service/)
- [F&I](/quirk-closedai/templates/fi/)
- [Parts](/quirk-closedai/templates/parts/)
- [Accounting](/quirk-closedai/templates/accounting/)
- [Marketing](/quirk-closedai/templates/marketing/)
- [Executive](/quirk-closedai/templates/executive/)

---

## Common Blocks
<details>
  <summary><span class="open">Open for more</span><span class="close" style="display:none">Close</span></summary>

### Placeholders
{% include_relative common/placeholders.md %}

### Disclaimers
{% include_relative common/disclaimers.md %}

### Signatures
{% include_relative common/signatures.md %}

</details>

<script>
  // Toggle label swap for details/summary (your preferred pattern)
  document.querySelectorAll('details').forEach(d=>{
    d.addEventListener('toggle',()=>{
      const s=d.querySelector('summary');
      if(!s) return;
      const open=s.querySelector('.open'), close=s.querySelector('.close');
      if(open && close){ const o=d.open; open.style.display=o?'none':''; close.style.display=o?'':'none';}
    });
  });
</script>
