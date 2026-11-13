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

/* Light the existing bear's flame without changing the original logo asset. */
(() => {
  const mark = document.querySelector('[data-pencil-name="Header"] [data-pencil-name="LogoMark"]');
  if (!mark || mark.querySelector('.hc-logo-fire')) return;
  const logo = mark.closest('[data-pencil-name="Logo"]');
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');
  mark.insertAdjacentHTML('beforeend', `
    <svg class="hc-logo-fire" viewBox="0 0 413 466" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="hc-fire-halo">
          <stop offset="0" stop-color="#FFCF70" stop-opacity=".9"/>
          <stop offset=".42" stop-color="#ED9B3A" stop-opacity=".36"/>
          <stop offset="1" stop-color="#ED9B3A" stop-opacity="0"/>
        </radialGradient>
        <linearGradient id="hc-fire-color" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stop-color="#FFD98A"/>
          <stop offset=".5" stop-color="#ED9A3D"/>
          <stop offset="1" stop-color="#B95124"/>
        </linearGradient>
      </defs>
      <ellipse class="hc-logo-halo" cx="121" cy="184" rx="77" ry="84" fill="url(#hc-fire-halo)"/>
      <g class="hc-logo-rays" fill="none" stroke="#D69A43" stroke-width="3" stroke-linecap="round">
        <path d="M108 156 67 91 M111 151 86 69 M119 142 117 49 M128 147 151 34 M139 149 189 28 M146 156 226 39"/>
        <path d="M99 165 48 123 M95 175 34 152 M93 185 24 183 M94 196 22 216 M99 207 25 255 M106 216 37 306"/>
      </g>
      <path class="hc-logo-flame" fill="url(#hc-fire-color)" d="M122 213 C108 213 102 203 104 189 C101 178 110 165 116 158 C113 153 115 148 117 145 C124 151 127 158 126 165 C131 162 132 158 131 154 C134 167 144 178 144 191 C146 204 136 213 122 213 Z"/>
      <path class="hc-logo-core" fill="#FFE5A3" d="M121 208 C112 204 113 196 117 190 C121 184 122 180 121 176 C131 184 128 190 132 195 C136 202 129 209 121 208 Z"/>
    </svg>`);
  mark.classList.add('hc-logo-lit');
  let timer;
  const ignite = () => {
    if (reduceMotion.matches || mark.classList.contains('hc-logo-igniting')) return;
    mark.classList.add('hc-logo-igniting');
    timer = setTimeout(() => mark.classList.remove('hc-logo-igniting'), 3600);
  };
  const stop = () => {
    clearTimeout(timer);
    mark.classList.remove('hc-logo-igniting');
  };
  reduceMotion.addEventListener('change', () => { if (reduceMotion.matches) stop(); });
  logo?.addEventListener('pointerenter', event => { if (event.pointerType === 'mouse') ignite(); });
  logo?.addEventListener('focusin', ignite);
  ignite();
})();
