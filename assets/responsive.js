/* Shared behavior for the tablet/phone navigation. */
(() => {
  const toggle = document.querySelector('.hc-menu-toggle');
  const menu = document.getElementById('hc-mobile-nav');
  if (!toggle || !menu) return;
  const setOpen = open => {
    toggle.setAttribute('aria-expanded', String(open));
    menu.hidden = !open;
    toggle.firstChild.textContent = open ? 'Close ' : 'Menu ';
  };
  toggle.addEventListener('click', () => setOpen(menu.hidden));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !menu.hidden) {
      setOpen(false);
      toggle.focus();
    }
  });
  matchMedia('(min-width: 1400px)').addEventListener('change', e => {
    if (e.matches) setOpen(false);
  });
  // Existing exported navigation uses click targets. Add keyboard access.
  document.querySelectorAll('[data-hc-link]').forEach(el => {
    if (el.closest('a,button') || el.querySelector('a,button,[data-hc-link]')) return;
    el.setAttribute('role', 'link');
    el.tabIndex = 0;
    el.addEventListener('keydown', event => {
      if (event.key === 'Enter') { event.preventDefault(); el.click(); }
    });
  });
})();
