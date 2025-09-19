<script>
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('pre.code').forEach(block => {
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.textContent = 'Copy';
    btn.addEventListener('click', async () => {
      const text = block.innerText.replace(/^Copy\n/, '');
      try {
        await navigator.clipboard.writeText(text);
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 1200);
      } catch(e){ console.error(e); }
    });
    block.prepend(btn);
  });
});
</script>
