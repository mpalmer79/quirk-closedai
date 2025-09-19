/* Add "Copy" buttons to code blocks */
(function () {
  function addButtons(root) {
    const blocks = root.querySelectorAll('div.highlighter-rouge, pre.highlight');
    blocks.forEach(block => {
      if (block.querySelector('.copy-btn')) return;
      const btn = document.createElement('button');
      btn.className = 'btn btn-sm copy-btn';
      btn.type = 'button';
      btn.textContent = 'Copy';
      btn.addEventListener('click', async () => {
        const text = block.innerText;
        try {
          await navigator.clipboard.writeText(text);
          btn.textContent = 'Copied!';
          setTimeout(() => (btn.textContent = 'Copy'), 1200);
        } catch (e) {
          console.error(e);
        }
      });
      block.appendChild(btn);
    });
  }
  document.addEventListener('DOMContentLoaded', () => addButtons(document));
})();
