(() => {
  const d = document, root = d.documentElement, KEY = 'ayf-theme';

  /* Theme: horizon toggle */
  const toggle = d.querySelector('.horizon');
  const sync = () => {
    const dark = root.dataset.theme === 'dark';
    if (toggle) {
      toggle.setAttribute('aria-checked', String(dark));
      toggle.setAttribute('aria-label', dark ? 'Switch to day mode' : 'Switch to night mode');
    }
    const meta = d.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = dark ? '#0B1433' : '#18255A';
  };
  sync();
  toggle?.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem(KEY, root.dataset.theme); } catch (e) {}
    sync();
  });
  try {
    matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
      let saved = null; try { saved = localStorage.getItem(KEY); } catch (_) {}
      if (!saved) { root.dataset.theme = e.matches ? 'dark' : 'light'; sync(); }
    });
  } catch (e) {}

  /* Header shadow + back to top */
  const header = d.querySelector('.site-header');
  const top = d.querySelector('.to-top');
  const onScroll = () => {
    const y = scrollY;
    header?.classList.toggle('scrolled', y > 8);
    top?.classList.toggle('show', y > 700);
  };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  top?.addEventListener('click', () => scrollTo({ top: 0, behavior: 'smooth' }));

  /* Desktop dropdowns */
  const items = [...d.querySelectorAll('.nav-item.has-menu')];
  const closeAll = except => items.forEach(i => { if (i !== except) { i.classList.remove('open'); i.querySelector('.nav-link')?.setAttribute('aria-expanded', 'false'); } });
  items.forEach(item => {
    const btn = item.querySelector('.nav-link');
    let t;
    const open = () => { clearTimeout(t); closeAll(item); item.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); };
    const close = () => { t = setTimeout(() => { item.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }, 160); };
    btn.addEventListener('click', e => { e.preventDefault(); item.classList.contains('open') ? (item.classList.remove('open'), btn.setAttribute('aria-expanded', 'false')) : open(); });
    item.addEventListener('mouseenter', () => { if (matchMedia('(hover:hover)').matches) open(); });
    item.addEventListener('mouseleave', () => { if (matchMedia('(hover:hover)').matches) close(); });
    item.addEventListener('focusout', e => { if (!item.contains(e.relatedTarget)) close(); });
  });
  d.addEventListener('click', e => { if (!e.target.closest('.nav-item')) closeAll(); });

  /* Mobile drawer */
  const menuBtn = d.querySelector('.menu-btn');
  const drawer = d.querySelector('.drawer');
  const setDrawer = open => {
    drawer?.classList.toggle('open', open);
    menuBtn?.setAttribute('aria-expanded', String(open));
    menuBtn?.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    d.body.style.overflow = open ? 'hidden' : '';
  };
  menuBtn?.addEventListener('click', () => setDrawer(!drawer.classList.contains('open')));
  drawer?.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setDrawer(false)));
  addEventListener('resize', () => { if (innerWidth > 1060) setDrawer(false); });
  d.addEventListener('keydown', e => { if (e.key === 'Escape') { setDrawer(false); closeAll(); } });

  /* Reveal on scroll */
  const reveals = d.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } }), { threshold: .12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(r => io.observe(r));
  } else reveals.forEach(r => r.classList.add('in'));

  /* Count up */
  const counters = d.querySelectorAll('[data-count]');
  const run = el => {
    const end = +el.dataset.count, dur = 1400, t0 = performance.now();
    const step = t => { const p = Math.min(1, (t - t0) / dur), v = Math.round(end * (1 - Math.pow(1 - p, 3))); el.textContent = v; if (p < 1) requestAnimationFrame(step); };
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) { el.textContent = end; return; }
    requestAnimationFrame(step);
  };
  if ('IntersectionObserver' in window) {
    const co = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { run(en.target); co.unobserve(en.target); } }), { threshold: .6 });
    counters.forEach(c => co.observe(c));
  }

  /* On this page: active chip */
  const chips = [...d.querySelectorAll('.onpage a[href^="#"]')];
  if (chips.length && 'IntersectionObserver' in window) {
    const map = new Map(chips.map(a => [a.getAttribute('href').slice(1), a]));
    const so = new IntersectionObserver(es => es.forEach(en => {
      if (en.isIntersecting) { chips.forEach(c => c.classList.remove('active')); const a = map.get(en.target.id); a?.classList.add('active'); a?.scrollIntoView({ block: 'nearest', inline: 'center' }); }
    }), { rootMargin: '-45% 0px -50% 0px' });
    map.forEach((_, id) => { const s = d.getElementById(id); if (s) so.observe(s); });
  }

  /* Filters (news + gallery) */
  d.querySelectorAll('.filters').forEach(group => {
    const target = d.querySelector(group.dataset.target);
    group.querySelectorAll('button').forEach(b => b.addEventListener('click', () => {
      group.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', String(x === b)));
      const f = b.dataset.filter;
      target?.querySelectorAll('[data-cat]').forEach(el => { el.hidden = f !== 'all' && !el.dataset.cat.split(' ').includes(f); });
    }));
  });

  /* Lightbox */
  const lb = d.querySelector('.lightbox');
  if (lb) {
    const shots = [...d.querySelectorAll('.shot[data-full]')];
    let idx = 0;
    const show = i => {
      const visible = shots.filter(s => !s.hidden);
      if (!visible.length) return;
      idx = (i + visible.length) % visible.length;
      const s = visible[idx];
      lb.querySelector('img').src = s.dataset.full;
      lb.querySelector('img').alt = s.querySelector('img').alt;
      lb.querySelector('strong').textContent = s.dataset.title;
      lb.querySelector('span').textContent = s.dataset.meta;
    };
    shots.forEach(s => s.addEventListener('click', () => { show(shots.filter(x => !x.hidden).indexOf(s)); lb.showModal(); }));
    lb.querySelector('.lb-close').addEventListener('click', () => lb.close());
    lb.querySelector('.lb-prev').addEventListener('click', () => show(idx - 1));
    lb.querySelector('.lb-next').addEventListener('click', () => show(idx + 1));
    lb.addEventListener('click', e => { if (e.target === lb) lb.close(); });
    lb.addEventListener('keydown', e => { if (e.key === 'ArrowLeft') show(idx - 1); if (e.key === 'ArrowRight') show(idx + 1); });
  }

  /* Contact form: prepare an email */
  const form = d.querySelector('#contact-form');
  if (form) {
    const topic = new URLSearchParams(location.search).get('topic');
    const sel = form.querySelector('[name=topic]');
    if (topic && [...sel.options].some(o => o.value === topic)) sel.value = topic;
    form.addEventListener('submit', e => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const v = n => form.querySelector(`[name=${n}]`).value.trim();
      const label = sel.options[sel.selectedIndex].text;
      const subject = encodeURIComponent(`${label}: message from ${v('name')}`);
      const body = encodeURIComponent(`Name: ${v('name')}\nEmail: ${v('email')}\nPhone: ${v('phone') || 'Not provided'}\nTopic: ${label}\n\n${v('message')}`);
      location.href = `mailto:ayt2018foundation@gmail.com?subject=${subject}&body=${body}`;
      form.querySelector('.form-status').textContent = 'Your email app is opening with your message ready to send.';
    });
  }

  d.querySelectorAll('[data-year]').forEach(x => x.textContent = new Date().getFullYear());
})();
