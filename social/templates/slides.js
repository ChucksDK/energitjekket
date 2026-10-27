import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';

const TPL = path.join(SOCIAL_ROOT, 'templates');
const FONTS = path.join(REPO_ROOT, 'src', 'fonts');
const HANDLE = '@energitjekket';

// Minimumsstørrelser for fitText (px ved 1080 bredde).
const MIN = { title: 40, value: 72, body: 28, kpi: 44, src: 24, cta: 34 };

const COLORS = { cheap: '#f5b700', normal: '#0f6b55', dear: '#c0392b' };

const SITE = path.join(REPO_ROOT, 'site');
const CTA_LEAD = { beregner: 'Regn på dit eget hus', elpris: 'Se dagens priser', varmepumpe: 'Læs guiden', solceller: 'Læs guiden' };

let cached;
function assets() {
  if (!cached) {
    const font = (file, weight) =>
      `@font-face{font-family:'DejaVu Sans';font-weight:${weight};font-style:normal;` +
      `src:url('${pathToFileURL(path.join(FONTS, file)).href}') format('truetype');}`;
    cached = {
      css: font('DejaVuSans.ttf', 400) + font('DejaVuSans-Bold.ttf', 700) + fs.readFileSync(path.join(TPL, 'base.css'), 'utf8'),
      js: fs.readFileSync(path.join(TPL, 'runtime.js'), 'utf8'),
    };
  }
  return cached;
}

export const esc = (s) =>
  String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);

// Tal og enhed må ikke deles over to linjer: "130 m²", "32.388 kr.", "kl. 06".
// Sammensatte ord med bindestreg ("vand-varmepumpe", "vand-/varmepumpe") må heller ikke brække:
// bogstav-bindestreg-bogstav får en hård bindestreg (U+2011), og "-/" en ordsammenbinder efter skråstregen.
export const glue = (s) =>
  String(s ?? '')
    .replace(/(\d) (?=[^\s\d])/g, '$1\u00a0')
    .replace(/\bkl\. (?=\d)/g, 'kl.\u00a0')
    .replace(/(\p{L})-\/(?=\p{L})/gu, '$1\u2011/\u2060')
    .replace(/(\p{L})-(?=\p{L})/gu, '$1\u2011');

// Escaper teksten og lægger gul markering på første forekomst af highlight.
function marked(text, highlight) {
  const t = String(text);
  const i = highlight ? t.indexOf(highlight) : -1;
  if (i < 0) return esc(glue(t));
  const [a, h, b] = [t.slice(0, i), highlight, t.slice(i + highlight.length)].map((x) => esc(glue(x)));
  return `${a}<span class="y">${h}</span>${b}`;
}

// Kildelinjen viser et kort visningsnavn, så den kan stå på én linje. Elpris skal altid hedde spotpris.
const SOURCE_LABELS = [
  [/^Danmarks Statistik/i, 'Danmarks Statistik'],
  [/^Energi Data Service/i, 'Energi Data Service · spotpris'],
  [/^PVGIS/i, 'PVGIS (EU JRC)'],
  [/^Bolius/i, 'Bolius'],
];
export function sourceLabel(name) {
  const n = String(name).trim();
  for (const [re, label] of SOURCE_LABELS) if (re.test(n)) return label;
  // Ellers udgiveren: "Energisparer.dk: varmepumpe pris …" -> "Energisparer.dk".
  return n.split(/[:,(]/)[0].trim();
}

const fileUrl = (p) => pathToFileURL(p).href;

function title(slide) {
  return slide.title ? `<h1 class="title" data-fit="title" data-min="${MIN.title}">${marked(slide.title, slide.highlight)}</h1>` : '';
}
function body(slide) {
  return slide.body ? `<div class="body" data-fit="body" data-min="${MIN.body}">${marked(slide.body, slide.highlight)}</div>` : '';
}
function value(slide) {
  return slide.value ? `<div class="value" data-fit="value" data-min="${MIN.value}">${marked(slide.value, slide.highlight)}</div>` : '';
}

// Dyreste/billigste 3 timer; værdier ≤ 0 tegnes som 2 px-stub ved bunden.
function barsHtml(hours) {
  const order = hours.map((v, i) => [v, i]).sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  const cheap = new Set(order.slice(0, 3).map(([, i]) => i));
  const dear = new Set(order.slice(-3).map(([, i]) => i));
  const max = Math.max(...hours.filter((v) => v > 0), 0);
  const bars = hours
    .map((v, i) => {
      const color = cheap.has(i) ? COLORS.cheap : dear.has(i) ? COLORS.dear : COLORS.normal;
      const h = v > 0 && max > 0 ? `max(2px, ${((v / max) * 100).toFixed(2)}%)` : '2px';
      return `<i style="height:${h};background:${color}"></i>`;
    })
    .join('');
  return (
    `<div class="chart"><div class="bars">${bars}</div>` +
    '<div class="ax"><span>00</span><span>06</span><span>12</span><span>18</span><span>23</span></div>' +
    `<div class="legend"><span><b style="color:${COLORS.cheap}">■</b> billigst</span>` +
    `<span><b style="color:${COLORS.normal}">■</b> normal</span>` +
    `<span><b style="color:${COLORS.dear}">■</b> dyrest</span></div></div>`
  );
}

// Bysiden (og dens undersider) har byens navn i formularens data-city; guides har en tom data-city.
function cityOf(pathname) {
  const file = path.join(SITE, ...pathname.split('/').filter(Boolean), 'index.html');
  if (!file.startsWith(SITE + path.sep) || !fs.existsSync(file)) return null;
  const m = /data-city="([^"]+)"/.exec(fs.readFileSync(file, 'utf8'));
  return m ? m[1] : null;
}

// "Læs guiden →<br>energitjekket.dk/<wbr>varmepumpe/<wbr>skift-oliefyr": må brydes efter hver skråstreg.
function ctaFromUrl(targetUrl) {
  if (!targetUrl) throw new Error('end-slide kræver ctx.targetUrl');
  const u = new URL(targetUrl);
  const p = u.pathname.replace(/\/+$/, '');
  const first = p.split('/').filter(Boolean)[0] || '';
  const city = first === 'solceller' || first === 'varmepumpe' ? cityOf(p) : null;
  const lead = city ? `Se tallene for ${city}` : CTA_LEAD[first] || 'Læs mere';
  const shown = (u.host + p).split('/').map(esc).join('/<wbr>');
  return `${esc(lead)} →<br>${shown}`;
}

function bgStyle(slide, ctx) {
  if (!slide.bg) return '';
  if (!path.isAbsolute(slide.bg) && !ctx.baseDir) throw new Error(`Baggrundsbillede kræver baseDir: ${slide.bg}`);
  const p = path.isAbsolute(slide.bg) ? slide.bg : path.resolve(ctx.baseDir, slide.bg);
  if (!fs.existsSync(p)) throw new Error(`Baggrundsbillede mangler: ${p}`);
  return (
    ' style="background:linear-gradient(rgba(11,79,67,.15),rgba(11,79,67,.85)),' +
    `url('${fileUrl(p)}') center/cover no-repeat #0b4f43"`
  );
}

const LAYOUTS = {
  cover: (s) => ({ dark: true, html: `<div class="content center">${title(s)}${value(s)}${body(s)}</div>` }),
  stat: (s) => ({ html: `<div class="content center">${title(s)}${value(s)}${body(s)}</div>` }),
  text: (s) => ({ html: `<div class="content center">${title(s)}${body(s)}</div>` }),
  kpi2: (s) => {
    const kpis = (s.kpis || [])
      .map(
        (k) =>
          `<div class="kpi box"><div class="k">${esc(glue(k.label))}</div>` +
          `<div class="v" data-fit="kpi" data-min="${MIN.kpi}">${esc(k.value)}</div>` +
          (k.unit ? `<div class="u">${esc(k.unit)}</div>` : '') +
          '</div>',
      )
      .join('');
    return { html: `<div class="content center">${title(s)}${body(s)}<div class="kpis">${kpis}</div></div>` };
  },
  bars: (s, ctx) => {
    const { date, area } = s.bars || {};
    const hours = s.bars?.hours ?? ctx.elpris?.[date]?.[area]?.hours;
    if (!Array.isArray(hours) || hours.length !== 24) throw new Error(`Ingen timepriser for ${date} ${area}`);
    const cta = s.cta ? `<div class="cta box">${esc(s.cta)}</div>` : '';
    return { html: `<div class="content">${title(s)}${body(s)}${barsHtml(hours)}${cta}</div>` };
  },
  screenshot: (s, ctx) => {
    if (!ctx.screenshotPath) throw new Error('screenshot-slide kræver ctx.screenshotPath');
    if (!fs.existsSync(ctx.screenshotPath)) throw new Error(`Screenshot mangler: ${ctx.screenshotPath}`);
    return {
      html:
        `<div class="content">${title(s)}` +
        `<div class="shot"><div class="phone"><img src="${esc(fileUrl(ctx.screenshotPath))}" alt=""></div></div></div>`,
    };
  },
  end: (s, ctx) => ({
    html:
      `<div class="content center">${title(s)}${body(s)}` +
      `<div class="cta box" data-fit="cta" data-min="${MIN.cta}">${ctaFromUrl(ctx.targetUrl)}</div>` +
      '<div class="note">Gem opslaget til senere</div></div>',
  }),
};

// Bund: kildelinjen på sin egen linje i fuld bredde (krymper i stedet for at bryde), derunder @energitjekket (+ Swipe →).
function footHtml(slide, ctx) {
  const names = [...new Set((slide.sources || []).map(sourceLabel))];
  const src = names.length ? `<span class="src" data-fit="src" data-min="${MIN.src}">Kilde: ${esc(names.join(' · '))}</span>` : '';
  const swipe = ctx.format === 'carousel' && ctx.index < ctx.total - 1;
  return `<div class="foot">${src}<div class="fr"><span>${HANDLE}</span>${swipe ? '<b>Swipe →</b>' : ''}</div></div>`;
}

/**
 * Fuldt HTML-dokument for ét slide.
 * ctx: { index, total, format:'carousel'|'story'|'short', elpris?, targetUrl?, screenshotPath?, baseDir? }
 */
export function slideHtml(slide, ctx) {
  const make = LAYOUTS[slide.layout];
  if (!make) throw new Error(`Ukendt layout: ${slide.layout}`);
  const { dark, html } = make(slide, ctx);
  const counter = ctx.format === 'carousel' && ctx.total > 1 ? ` · ${ctx.index + 1}/${ctx.total}` : '';
  const tag = slide.tag ? `<span class="tag">${esc(slide.tag + counter)}</span>` : '';
  const bg = dark ? bgStyle(slide, ctx) : '';
  const { css, js } = assets();
  return (
    '<!doctype html><html lang="da"><head><meta charset="utf-8">' +
    `<style>${css}</style></head><body>` +
    `<div class="slide layout-${slide.layout} format-${ctx.format}${dark ? ' dark' : ''}${bg ? ' has-bg' : ''}"${bg}>` +
    `<div class="slide-safe">${tag}${html}${footHtml(slide, ctx)}</div></div>` +
    `<script>${js}</script></body></html>`
  );
}
