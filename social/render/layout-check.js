// Automatisk layouttjek: kører i siden efter data-ready og før screenshot.
// Issue = { kind: 'outside' | 'overlap' | 'wrap', text }

export class LayoutError extends Error {
  constructor(issues, label = '') {
    const lines = issues.map((i) => `${i.kind}: ${i.text}`);
    super(`Layoutfejl${label ? ` (${label})` : ''}:\n${lines.join('\n')}`);
    this.name = 'LayoutError';
    this.issues = issues;
  }
}

const SAFE = 66; // px fra kanten
const OVERLAP_TOL = 2; // px i begge akser
const OUTSIDE_TOL = 0.5;

function inPage({ SAFE, OVERLAP_TOL, OUTSIDE_TOL }) {
  const issues = [];
  const clip = (s) => {
    const t = s.replace(/\s+/g, ' ').trim();
    return t.length > 40 ? `${t.slice(0, 40)}…` : t;
  };
  const add = (kind, text) => {
    if (!issues.some((i) => i.kind === kind && i.text === text)) issues.push({ kind, text });
  };
  const blockOf = (node) => {
    let el = node.parentElement;
    while (el && el.parentElement && getComputedStyle(el).display === 'inline') el = el.parentElement;
    return el;
  };

  // 1) Alle tekstlinjer (én rect pr. linje pr. tekstnode).
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const items = [];
  for (let n = walker.nextNode(); n; n = walker.nextNode()) {
    if (!n.nodeValue.trim() || n.parentElement.closest('script,style')) continue;
    const range = document.createRange();
    range.selectNodeContents(n);
    for (const r of range.getClientRects()) {
      if (r.width < 0.5 || r.height < 0.5) continue;
      items.push({ node: n, block: blockOf(n), r, text: clip(n.nodeValue) });
    }
  }

  // 2) outside: ud over nærmeste kasse (indholdsfladen) eller sikker zone.
  const vw = document.documentElement.clientWidth;
  const vh = document.documentElement.clientHeight;
  for (const it of items) {
    const box = it.node.parentElement.closest('.box, .kpi, .cta, .slide-safe');
    if (box) {
      const b = box.getBoundingClientRect();
      const cs = getComputedStyle(box);
      const l = b.left + parseFloat(cs.borderLeftWidth) + parseFloat(cs.paddingLeft);
      const rr = b.right - parseFloat(cs.borderRightWidth) - parseFloat(cs.paddingRight);
      const t = b.top + parseFloat(cs.borderTopWidth) + parseFloat(cs.paddingTop);
      const bt = b.bottom - parseFloat(cs.borderBottomWidth) - parseFloat(cs.paddingBottom);
      if (it.r.left < l - OUTSIDE_TOL || it.r.right > rr + OUTSIDE_TOL || it.r.top < t - OUTSIDE_TOL || it.r.bottom > bt + OUTSIDE_TOL) {
        add('outside', `"${it.text}"`);
      }
    }
    if (it.r.left < SAFE - OUTSIDE_TOL || it.r.top < SAFE - OUTSIDE_TOL || it.r.right > vw - SAFE + OUTSIDE_TOL || it.r.bottom > vh - SAFE + OUTSIDE_TOL) {
      add('outside', `"${it.text}" (uden for sikker zone)`);
    }
  }

  // 3) overlap: tekst mod tekst, og tekst mod .bars/.cta/.kpi.
  const hit = (a, b) =>
    Math.min(a.right, b.right) - Math.max(a.left, b.left) > OVERLAP_TOL &&
    Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) > OVERLAP_TOL;
  for (let i = 0; i < items.length; i += 1) {
    for (let j = i + 1; j < items.length; j += 1) {
      const a = items[i];
      const b = items[j];
      if (a.block === b.block) continue;
      if (hit(a.r, b.r)) add('overlap', `"${a.text}" / "${b.text}"`);
    }
  }
  for (const el of document.querySelectorAll('.bars, .cta, .kpi, .phone, .shot, .chart')) {
    const er = el.getBoundingClientRect();
    const names = { bars: 'søjlediagram', cta: 'knap', kpi: 'boks', phone: 'telefonbillede', shot: 'screenshot-felt', chart: 'diagram' };
    const name = names[[...el.classList].find((c) => names[c])];
    for (const it of items) {
      if (el.contains(it.node)) continue;
      if (hit(it.r, er)) add('overlap', `"${it.text}" / ${name}`);
    }
  }

  // 3b) screenshot må ikke presses sammen: telefonen skal fylde mindst 40 % af indholdshøjden.
  for (const phone of document.querySelectorAll('.phone')) {
    const content = phone.closest('.content');
    const ch = content ? content.getBoundingClientRect().height : vh;
    if (phone.getBoundingClientRect().height < 0.4 * ch) add('outside', `telefonbillede er presset sammen (${Math.round(phone.getBoundingClientRect().height)} px)`);
  }

  // 4) wrap: tal og kildelinjen må kun fylde én linje.
  for (const el of document.querySelectorAll('.value, .kpi .v, .foot .src')) {
    const rects = items.filter((it) => el.contains(it.node)).map((it) => it.r);
    const lines = [];
    for (const r of rects) {
      const mid = (r.top + r.bottom) / 2;
      if (!lines.some((l) => mid > l.top && mid < l.bottom)) lines.push({ top: r.top, bottom: r.bottom });
    }
    if (lines.length > 1) add('wrap', `"${clip(el.textContent)}" fylder ${lines.length} linjer`);
  }
  return issues;
}

/** Returnerer liste af layoutproblemer for den indlæste (data-ready) side. */
export function checkLayout(page) {
  return page.evaluate(inPage, { SAFE, OVERLAP_TOL, OUTSIDE_TOL });
}
