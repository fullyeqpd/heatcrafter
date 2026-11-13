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

/* Illuminate the original rays in both marks; the bear and lettering stay still. */
(() => {
  const marks = document.querySelectorAll('[data-pencil-name="Header"] [data-pencil-name="LogoMark"], [data-pencil-name="FooterLogoImg"]');
  const inkSource = new URL('../images/hc-mark-ink.png', document.currentScript.src).href;
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');
  marks.forEach((mark, index) => {
    if (mark.querySelector('.hc-logo-fire')) return;
    const footer = mark.dataset.pencilName === 'FooterLogoImg';
    const id = `hc-fire-${index}`;
    // The footer artwork uses the same mark, offset 200px within its wordmark.
    mark.insertAdjacentHTML('beforeend', `
      <svg class="hc-logo-fire" viewBox="${footer ? '0 0 834 674' : '0 0 413 466'}" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <filter id="${id}-ray-contrast" color-interpolation-filters="sRGB">
            <feComponentTransfer>
              <feFuncR type="linear" slope="10" intercept="-1.2"/>
              <feFuncG type="linear" slope="10" intercept="-1.2"/>
              <feFuncB type="linear" slope="10" intercept="-1.2"/>
              <feFuncA type="linear" slope="5" intercept="0"/>
            </feComponentTransfer>
            <feComponentTransfer>
              <feFuncR type="gamma" amplitude="1" exponent=".3" offset="0"/>
              <feFuncG type="gamma" amplitude="1" exponent=".3" offset="0"/>
              <feFuncB type="gamma" amplitude="1" exponent=".3" offset="0"/>
            </feComponentTransfer>
          </filter>
          <mask id="${id}-ray-mask" maskUnits="userSpaceOnUse" x="0" y="0" width="413" height="466" style="mask-type:luminance">
            <image href="${inkSource}" width="413" height="466" filter="url(#${id}-ray-contrast)"/>
          </mask>
          <radialGradient id="${id}-ray-color" cx="29.8%" cy="40%" r="82%">
            <stop offset="0" stop-color="#FFF5BE"/>
            <stop offset=".35" stop-color="#FFD25D"/>
            <stop offset="1" stop-color="#E79B30"/>
          </radialGradient>
          <radialGradient id="${id}-halo">
            <stop offset="0" stop-color="#FFF1A6" stop-opacity="1"/>
            <stop offset=".42" stop-color="#FFC34D" stop-opacity=".65"/>
            <stop offset="1" stop-color="#FFC34D" stop-opacity="0"/>
          </radialGradient>
          <linearGradient id="${id}-color" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stop-color="#FFF4BF"/>
            <stop offset=".5" stop-color="#FFD05D"/>
            <stop offset="1" stop-color="#EF922C"/>
          </linearGradient>
        </defs>
        <g transform="${footer ? 'translate(200 0)' : 'translate(0 0)'}">
          <rect class="hc-logo-rays" width="413" height="466" fill="url(#${id}-ray-color)" mask="url(#${id}-ray-mask)"/>
          <ellipse class="hc-logo-halo" cx="121" cy="184" rx="90" ry="96" fill="url(#${id}-halo)"/>
          <path class="hc-logo-flame" fill="url(#${id}-color)" d="M122 213 C108 213 102 203 104 189 C101 178 110 165 116 158 C113 153 115 148 117 145 C124 151 127 158 126 165 C131 162 132 158 131 154 C134 167 144 178 144 191 C146 204 136 213 122 213 Z"/>
          <path class="hc-logo-core" fill="#FFF9DC" d="M121 208 C112 204 113 196 117 190 C121 184 122 180 121 176 C131 184 128 190 132 195 C136 202 129 209 121 208 Z"/>
        </g>
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
    const hoverTarget = footer ? mark : mark.closest('[data-pencil-name="Logo"]');
    const focusTarget = mark.closest(footer ? '[data-pencil-name="FooterBrand"]' : '[data-pencil-name="Logo"]');
    hoverTarget?.addEventListener('pointerenter', event => { if (event.pointerType === 'mouse') ignite(); });
    focusTarget?.addEventListener('focusin', ignite);
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(entries => {
        if (entries.some(entry => entry.isIntersecting)) {
          ignite();
          observer.disconnect();
        }
      }, {threshold: .35});
      observer.observe(mark);
    } else {
      ignite();
    }
  });
})();
