import fs from 'node:fs';
import path from 'node:path';
import { REPO_ROOT } from '../lib/paths.js';
import { BANNED } from '../lib/brief.js';
import { withPage } from './png.js';

const SITE = path.join(REPO_ROOT, 'site');

/** Filnavn til en skærmbilledenøgle: ':' → '-' + .png (by:aalborg:solceller → by-aalborg-solceller.png). */
export function screenFile(key) {
  return `${key.replaceAll(':', '-')}.png`;
}

/** Nøgle → URL-sti, eller null hvis siden ikke findes. Byer læses fra site/ (de tilføjes dagligt). */
export function pagePath(key) {
  if (key === 'beregner') return '/beregner/';
  if (key === 'elpris') return '/elpris/';
  const m = /^by:([a-z0-9-]+):(solceller|varmepumpe)$/.exec(key);
  if (m) {
    const [, city, service] = m;
    if (fs.existsSync(path.join(SITE, service, city, 'index.html'))) return `/${service}/${city}/`;
  }
  return null;
}

/**
 * Skjules før skærmbilledet. Den sticky mobil-CTA (.mcta) dækker indholdet på alle sider.
 * Bysiderne har desuden salgstekst og tilbudsformular i toppen (header-knap, USP-liste,
 * "Få gratis tilbud"-knap, intro med "tilbud", formularen og sidebar-CTA'en): de skjules,
 * så skærmbilledet kun viser by, overskrift og indhold.
 */
const HIDE_ALL = ['.mcta'];
const HIDE_CITY = ['.hdr-cta', '.usp', '.hero-actions', '.lead-p', '.hero-form', 'form.lead', '.side-cta', '.mini-usp'];
const hideCss = (sel) => `${sel.join(',')}{display:none !important}`;

// Salgsord, der ikke må ses i skærmbilledet (samme liste som brief-reglerne, plus "tilbud").
const SALES_WORDS = [...BANNED.filter((w) => /\p{L}/u.test(w)), 'tilbud'];

/** Synlig tekst inden for viewporten (tekstnoder, hvis linjer ligger i billedet), og om en formular kan ses. */
function viewportText() {
  const vw = window.innerWidth;
  const vh = window.innerHeight;
  const shown = (el) => {
    for (let e = el; e; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.display === 'none' || cs.visibility === 'hidden' || Number(cs.opacity) === 0) return false;
    }
    return true;
  };
  const inView = (r) => r.width > 0 && r.height > 0 && r.bottom > 0 && r.right > 0 && r.top < vh && r.left < vw;
  const parts = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n = walker.nextNode(); n; n = walker.nextNode()) {
    if (!n.nodeValue.trim() || n.parentElement.closest('script,style,noscript') || !shown(n.parentElement)) continue;
    const range = document.createRange();
    range.selectNodeContents(n);
    if ([...range.getClientRects()].some(inView)) parts.push(n.nodeValue.trim());
  }
  const formVisible = [...document.querySelectorAll('form, input:not([type=hidden]), select, textarea')].some(
    (el) => shown(el) && inView(el.getBoundingClientRect()),
  );
  return { text: parts.join(' ').replace(/\s+/g, ' '), formVisible };
}

/**
 * Tager et 390×844-skærmbillede (×3) af toppen af en side; returnerer outPath.
 * Afviser (og gemmer intet), hvis der stadig er salgstekst eller en formular i billedet.
 * info (valgfri) får { text, formVisible } for det synlige udsnit.
 */
export async function shootPage(key, outPath, base = 'https://energitjekket.dk', info = {}) {
  const p = pagePath(key);
  if (!p) throw new Error(`Ukendt side: ${key}`);
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  await withPage(
    async (page) => {
      const r = await page.goto(base.replace(/\/$/, '') + p, { waitUntil: 'networkidle' });
      if (!r || !r.ok()) throw new Error(`Ukendt side: ${key} (HTTP ${r ? r.status() : 'ingen svar'})`);
      await page.addStyleTag({ content: hideCss(key.startsWith('by:') ? [...HIDE_ALL, ...HIDE_CITY] : HIDE_ALL) });
      const seen = await page.evaluate(viewportText);
      Object.assign(info, seen);
      const lower = seen.text.toLowerCase();
      const hit = SALES_WORDS.find((w) => lower.includes(w));
      if (hit) throw new Error(`Skærmbillede af ${key} viser salgstekst ("${hit}"); skjul elementet i render/screenshot.js`);
      if (seen.formVisible) throw new Error(`Skærmbillede af ${key} viser en formular; skjul den i render/screenshot.js`);
      await page.screenshot({ path: outPath });
    },
    { width: 390, height: 844, deviceScaleFactor: 3 },
  );
  return outPath;
}
