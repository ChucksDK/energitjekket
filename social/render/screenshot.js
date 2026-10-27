import fs from 'node:fs';
import path from 'node:path';
import { REPO_ROOT } from '../lib/paths.js';
import { withPage } from './png.js';

const SITE = path.join(REPO_ROOT, 'site');
const SERVICES = { solceller: 'solceller', varmepumpe: 'varmepumpe' };

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
    if (fs.existsSync(path.join(SITE, SERVICES[service], city, 'index.html'))) return `/${service}/${city}/`;
  }
  return null;
}

/** Skjuler den sticky mobil-CTA (.mcta), som ellers dækker indholdet. Intet andet ændres. */
const HIDE_CTA = '.mcta{display:none !important}';

/** Tager et 390×844-skærmbillede (×3) af forsiden af en side; returnerer outPath. */
export async function shootPage(key, outPath, base = 'https://energitjekket.dk') {
  const p = pagePath(key);
  if (!p) throw new Error(`Ukendt side: ${key}`);
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  await withPage(
    async (page) => {
      await page.goto(base.replace(/\/$/, '') + p, { waitUntil: 'networkidle' });
      await page.addStyleTag({ content: HIDE_CTA });
      await page.screenshot({ path: outPath });
    },
    { width: 390, height: 844, deviceScaleFactor: 3 },
  );
  return outPath;
}
