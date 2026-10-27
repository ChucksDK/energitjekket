// Kører i siden. Krymper tekst, til den passer, og sætter data-ready, når slidet er klar.
function fitText(el, minPx) {
  let size = parseFloat(getComputedStyle(el).fontSize);
  while ((el.scrollWidth > el.clientWidth || el.scrollHeight > el.clientHeight) && size > minPx) {
    size = Math.max(minPx, size - 2);
    el.style.fontSize = `${size}px`;
  }
  return size;
}

// Midterfeltet må ikke løbe over: krymp titel/brødtekst (ned til deres minimum), til det passer.
function fitContent(content) {
  const items = [...content.querySelectorAll('[data-fit]')].filter((el) => el.dataset.fit !== 'value');
  for (let guard = 0; guard < 200 && content.scrollHeight > content.clientHeight; guard += 1) {
    let shrunk = false;
    for (const el of items) {
      const size = parseFloat(getComputedStyle(el).fontSize);
      const min = Number(el.dataset.min);
      if (size > min) {
        el.style.fontSize = `${Math.max(min, size - 2)}px`;
        shrunk = true;
      }
    }
    if (!shrunk) break;
  }
}

function fitAll() {
  for (const el of document.querySelectorAll('[data-fit]')) fitText(el, Number(el.dataset.min));
  for (const c of document.querySelectorAll('.content')) fitContent(c);
  // KPI-tal side om side får samme størrelse (den mindste).
  for (const row of document.querySelectorAll('.kpis')) {
    const vs = [...row.querySelectorAll('.v')];
    const min = Math.min(...vs.map((el) => parseFloat(getComputedStyle(el).fontSize)));
    for (const el of vs) el.style.fontSize = `${min}px`;
  }
}

window.fitText = fitText;
window.fitAll = fitAll;

window.addEventListener('load', () => {
  Promise.all([
    document.fonts.load('400 50px "DejaVu Sans"'),
    document.fonts.load('700 50px "DejaVu Sans"'),
  ])
    .then(() => document.fonts.ready)
    .then(() => {
      fitAll();
      document.documentElement.dataset.ready = '1';
    });
});

// ---------------------------------------------------------------------------
// Animation til shorts. Alt beregnes ud fra t (sekunder) – ingen CSS-transitions,
// ingen requestAnimationFrame – så samme t giver samme billede.
const FADE = 0.3; // tekst fader/glider ind
const RISE = 24; // px
const COUNT = 0.8; // tal tæller op
const STAGGER = 0.15; // forsinkelse pr. element
const BAR_DUR = 0.8;
const BAR_STAGGER = 0.02;

const clamp01 = (x) => Math.min(1, Math.max(0, x));
const easeOut = (p) => 1 - (1 - p) * (1 - p) * (1 - p);

const NUM_RE = /[-−]?(?:\d{1,3}(?:\.\d{3})+|\d+)(?:,\d+)?/;

// Finder første tal i elementet og gemmer det, så det kan tælles op og skrives tilbage.
function prepCounter(el) {
  const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
  for (let n = walker.nextNode(); n; n = walker.nextNode()) {
    const m = NUM_RE.exec(n.nodeValue);
    if (!m) continue;
    const token = m[0];
    const neg = /^[-−]/.test(token);
    const digits = token.replace(/^[-−]/, '');
    const dec = digits.includes(',') ? digits.split(',')[1].length : 0;
    const grouped = /\./.test(digits);
    const value = Number(digits.replace(/\./g, '').replace(',', '.'));
    const before = n.nodeValue.slice(0, m.index);
    const after = n.nodeValue.slice(m.index + token.length);
    // Tallet pakkes i en span, hvis bredde låses til sluttallet mens der tælles.
    const span = document.createElement('span');
    span.textContent = token;
    n.nodeValue = before;
    n.parentNode.insertBefore(span, n.nextSibling);
    n.parentNode.insertBefore(document.createTextNode(after), span.nextSibling);
    return { span, token, neg, dec, grouped, value, width: span.getBoundingClientRect().width, minus: token[0] };
  }
  return null;
}

function formatDa(c, v) {
  let [int, frac] = (c.dec ? v.toFixed(c.dec) : String(Math.round(v))).split('.');
  if (c.grouped) int = int.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
  return (c.neg ? c.minus : '') + int + (frac ? `,${frac}` : '');
}

function prepSlide(slide) {
  if (slide._anim) return slide._anim;
  const content = slide.querySelector('.content');
  const reveal = [];
  const tag = slide.querySelector('.tag');
  if (tag) reveal.push(tag);
  if (content) reveal.push(...content.children);
  const counters = [...slide.querySelectorAll('.value, .kpi .v')].map((el) => ({ el, c: prepCounter(el) })).filter((x) => x.c);
  const bars = [...slide.querySelectorAll('.bars i')];
  const chart = slide.querySelector('.chart');
  slide._anim = { reveal, counters, bars, chart };
  return slide._anim;
}

function seekSlide(slide, t) {
  const a = prepSlide(slide);
  a.reveal.forEach((el, i) => {
    const p = easeOut(clamp01((t - i * STAGGER) / FADE));
    el.style.opacity = p >= 1 ? '' : String(p);
    el.style.transform = p >= 1 ? '' : `translateY(${((1 - p) * RISE).toFixed(2)}px)`;
  });
  const startOf = (el) => a.reveal.indexOf(el) * STAGGER;
  for (const { el, c } of a.counters) {
    const p = easeOut(clamp01((t - startOf(el.closest('.content > *') || el)) / COUNT));
    if (p >= 1) {
      c.span.textContent = c.token;
      c.span.style.cssText = '';
    } else {
      c.span.textContent = formatDa(c, c.value * p);
      c.span.style.cssText = `display:inline-block;width:${c.width}px;text-align:right;white-space:nowrap`;
    }
  }
  const base = a.chart ? startOf(a.chart) + 0.1 : 0;
  a.bars.forEach((el, i) => {
    const p = easeOut(clamp01((t - base - i * BAR_STAGGER) / BAR_DUR));
    el.style.transformOrigin = 'bottom';
    el.style.transform = p >= 1 ? '' : `scaleY(${p.toFixed(4)})`;
  });
}

window.seek = (t) => seekSlide(document.querySelector('.slide:not(#under .slide)'), t);

// Lægger næste slide under det nuværende (til krydsfade) og tilpasser dets tekst.
window.mountNext = (markup) => {
  const wrap = document.createElement('div');
  wrap.id = 'under';
  wrap.style.cssText = 'position:absolute;left:0;top:0;width:100%;height:100%;z-index:0';
  wrap.innerHTML = markup;
  document.body.prepend(wrap);
  document.body.style.position = 'relative';
  const cur = document.querySelector('.slide:not(#under .slide)');
  cur.style.position = 'relative';
  cur.style.zIndex = '1';
  fitAll();
};
window.seekNext = (t) => seekSlide(document.querySelector('#under .slide'), t);
window.setFade = (opacity) => {
  document.querySelector('.slide:not(#under .slide)').style.opacity = String(opacity);
};
