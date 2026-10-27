import { test, before } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { loadSources } from '../lib/sources.js';
import { resolvePost } from '../lib/brief.js';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';
import { ensureSources } from './helpers.js';
import { slideHtml, glue } from '../templates/slides.js';
import { checkLayout } from '../render/layout-check.js';
import { renderCarousel, withPage, loadSlide } from '../render/png.js';

const OUT = path.join(SOCIAL_ROOT, 'out', 'test');
const BASE = path.join(SOCIAL_ROOT, 'out', 'test-week');
let sources;
let post;

before(() => {
  sources = loadSources(ensureSources());
  const brief = JSON.parse(fs.readFileSync(path.join(SOCIAL_ROOT, 'test', 'fixtures', 'brief-valid.json'), 'utf8'));
  post = resolvePost(brief.posts[0], sources);
  // Ugemappe med assets/cover.png (fixturens bg) – et vilkårligt PNG fra repoet.
  fs.mkdirSync(path.join(BASE, 'assets'), { recursive: true });
  fs.copyFileSync(path.join(REPO_ROOT, 'site', 'og', 'beregner.png'), path.join(BASE, 'assets', 'cover.png'));
});

const pngSize = (file) => {
  const b = fs.readFileSync(file);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
};

test('renderCarousel writes one 1080x1350 PNG per slide', async () => {
  fs.rmSync(OUT, { recursive: true, force: true });
  const files = await renderCarousel(post, OUT, { elpris: sources.elpris, baseDir: BASE });
  assert.ok(files.length >= 5 && files.length <= 7, `fik ${files.length} filer`);
  assert.equal(files.length, post.slides.length);
  files.forEach((f, i) => {
    assert.equal(path.basename(f), `${post.id}-0${i + 1}.png`);
    assert.deepEqual(pngSize(f), { w: 1080, h: 1350 });
  });
});

test('slideHtml appends position to the tag and builds the bottom bar', () => {
  const html = slideHtml(post.slides[1], { index: 1, total: 5, format: 'carousel', targetUrl: post.target_url });
  assert.match(html, /OLIEFYR · 2\/5/);
  assert.match(html, /Kilde: Bolius/);
  assert.match(html, /@energitjekket/);
  assert.match(html, /<b>Swipe →<\/b>/);
  const last = slideHtml(post.slides[4], { index: 4, total: 5, format: 'carousel', targetUrl: post.target_url });
  assert.doesNotMatch(last, /<b>Swipe →<\/b>/);
  assert.match(last, /Regn på dit eget hus →/);
  assert.match(last, /energitjekket\.dk\/<wbr>beregner/);
});

test('bars chart clamps negative values to baseline', async () => {
  const hours = Array.from({ length: 24 }, (_, h) => 0.2 + h * 0.05);
  hours[3] = -0.3;
  hours[4] = 0;
  const slide = {
    layout: 'bars',
    tag: 'ELPRIS',
    title: 'Billigste time i morgen: kl. 03',
    body: 'Negative priser i nat.',
    bars: { date: '2026-10-27', area: 'DK1', hours },
    sources: ['Energi Data Service'],
  };
  const html = slideHtml(slide, { index: 0, total: 1, format: 'story' });
  const res = await withPage(
    async (page) => {
      await loadSlide(page, html);
      return page.evaluate(() => {
        const box = document.querySelector('.bars').getBoundingClientRect();
        return [...document.querySelectorAll('.bars i')].map((el) => {
          const r = el.getBoundingClientRect();
          return {
            inside: r.top >= box.top - 0.5 && r.bottom <= box.bottom + 0.5 && r.left >= box.left - 0.5 && r.right <= box.right + 0.5,
            h: r.height,
            bg: getComputedStyle(el).backgroundColor,
          };
        });
      });
    },
    { width: 1080, height: 1920 },
  );
  assert.equal(res.length, 24);
  for (const [i, r] of res.entries()) assert.ok(r.inside, `bar ${i} uden for .bars`);
  assert.equal(res[3].h, 2);
  assert.equal(res[4].h, 2);
  // billigste 3 gule, dyreste 3 røde
  assert.equal(res.filter((r) => r.bg === 'rgb(245, 183, 0)').length, 3);
  assert.equal(res.filter((r) => r.bg === 'rgb(192, 57, 43)').length, 3);
  assert.equal(res[23].bg, 'rgb(192, 57, 43)');
});

test('KPI values keep their 88px start size when they fit; stat body joins number and unit with NBSP', async () => {
  const kpi = slideHtml(post.slides[2], { index: 2, total: 5, format: 'carousel' });
  const stat = slideHtml(post.slides[1], { index: 1, total: 5, format: 'carousel' });
  assert.match(stat, /130 m²/);
  const sizes = await withPage(async (page) => {
    await loadSlide(page, kpi);
    return page.evaluate(() => [...document.querySelectorAll('.kpi .v')].map((el) => getComputedStyle(el).fontSize));
  });
  assert.deepEqual(sizes, ['88px', '88px']);
});

test('cover bg: relative path without baseDir throws', () => {
  assert.throws(
    () => slideHtml(post.slides[0], { index: 0, total: 5, format: 'carousel' }),
    /Baggrundsbillede kræver baseDir/,
  );
});

test('cover bg: missing file throws', () => {
  assert.throws(
    () => slideHtml({ ...post.slides[0], bg: 'assets/findes-ikke.png' }, { index: 0, total: 5, format: 'carousel', baseDir: BASE }),
    /Baggrundsbillede mangler/,
  );
});

test('footer shows short display names for sources (finding 2/3)', async () => {
  const { sourceLabel } = await import('../templates/slides.js');
  assert.equal(sourceLabel('Danmarks Statistik BOL102 (2026)'), 'Danmarks Statistik');
  assert.equal(sourceLabel('Energi Data Service (Energinet), spotpris'), 'Energi Data Service · spotpris');
  assert.equal(sourceLabel('PVGIS 5.3 (EU JRC)'), 'PVGIS (EU JRC)');
  assert.equal(sourceLabel('Bolius: pris på opvarmningsformer'), 'Bolius');
  assert.equal(sourceLabel('Energisparer.dk: varmepumpe pris 2026 (kommerciel kilde, okt. 2026)'), 'Energisparer.dk');
  const html = slideHtml({ layout: 'text', tag: 'T', title: 'x', sources: ['Energi Data Service (Energinet), spotpris'] }, { index: 0, total: 1, format: 'story' });
  assert.match(html, /Kilde: Energi Data Service · spotpris/);
});

// --- finding 10: sammensatte ord med bindestreg brækker ikke ---
test('glue joins letter-hyphen-letter with a non-breaking hyphen, not elsewhere', () => {
  assert.equal(glue('luft til vand-varmepumpe'), 'luft til vand\u2011varmepumpe');
  assert.equal(glue('vand-/varmepumpe'), 'vand\u2011/\u2060varmepumpe');
  assert.equal(glue('olie- eller gasfyr'), 'olie- eller gasfyr');
  assert.equal(glue('-0,05 kr.'), '-0,05\u00a0kr.');
  const html = slideHtml({ layout: 'kpi2', tag: 'T', title: 'Luft til vand-varmepumpe', kpis: [{ label: 'Luft til vand-varmepumpe', value: '1', unit: 'x' }, { label: 'b', value: '2' }] }, { index: 0, total: 1, format: 'story' });
  assert.ok(html.includes('Luft til vand\u2011varmepumpe</h1>'), 'titel');
  assert.ok(html.includes('<div class="k">Luft til vand\u2011varmepumpe</div>'), 'KPI-label');
});

test('a hyphenated compound in a narrow KPI label never splits at the hyphen', async () => {
  const slide = { layout: 'kpi2', tag: 'T', title: 'Varme', kpis: [{ label: 'Luft til vand-varmepumpe', value: '12.345', unit: 'kr./år' }, { label: 'Jordvarme', value: '11.000', unit: 'kr./år' }] };
  const lines = await withPage(async (page) => {
    await loadSlide(page, slideHtml(slide, { index: 0, total: 1, format: 'carousel' }));
    return page.evaluate(() => {
      const k = document.querySelector('.kpi .k');
      const r = document.createRange();
      const t = k.firstChild;
      const i = t.nodeValue.indexOf('vand');
      r.setStart(t, i);
      r.setEnd(t, t.nodeValue.length);
      return new Set([...r.getClientRects()].map((x) => Math.round(x.top))).size;
    });
  });
  assert.equal(lines, 1);
});

// --- finding 11: slutslidets link-boks klarer lange adresser ---
test('end CTA: lead text by page type and <wbr> after each slash', () => {
  const cta = (url) => /<div class="cta box"[^>]*>(.*?)<\/div>/.exec(slideHtml({ layout: 'end', tag: 'T', title: 'x' }, { index: 0, total: 1, format: 'story', targetUrl: url }))[1];
  assert.match(cta('https://energitjekket.dk/varmepumpe/skift-oliefyr/'), /^Læs guiden →<br>energitjekket\.dk\/<wbr>varmepumpe\/<wbr>skift-oliefyr$/);
  assert.match(cta('https://energitjekket.dk/solceller/kan-det-betale-sig/'), /^Læs guiden →/);
  assert.match(cta('https://energitjekket.dk/beregner/'), /^Regn på dit eget hus →<br>energitjekket\.dk\/<wbr>beregner$/);
  assert.match(cta('https://energitjekket.dk/elpris/'), /^Se dagens priser →/);
  assert.match(cta('https://energitjekket.dk/solceller/aalborg/'), /^Se tallene for Aalborg →/);
  assert.match(cta('https://energitjekket.dk/solceller/naestved/'), /^Se tallene for Næstved →/);
  assert.match(cta('https://energitjekket.dk/varmepumpe/viborg/fjernvarme-eller-varmepumpe/'), /^Se tallene for Viborg →/);
});

test('end slides with long URLs pass the layout check (carousel and short)', async () => {
  const urls = [
    'https://energitjekket.dk/varmepumpe/viborg/fjernvarme-eller-varmepumpe/',
    'https://energitjekket.dk/varmepumpe/aarhus/fjernvarme-eller-varmepumpe/',
    'https://energitjekket.dk/solceller/fladt-tag-og-carport/',
    'https://energitjekket.dk/varmepumpe/luft-til-luft-pris/',
  ];
  const slide = { layout: 'end', tag: 'LÆS MERE', title: 'Status for fjernvarmen i Viborg', body: 'Status, priser og tal for hele kommunen. Linket står i bio.' };
  for (const [format, size] of [['carousel', { width: 1080, height: 1350 }], ['short', { width: 1080, height: 1920 }]]) {
    for (const targetUrl of urls) {
      const issues = await withPage(async (page) => {
        await loadSlide(page, slideHtml(slide, { index: 4, total: 5, format, targetUrl }));
        return checkLayout(page);
      }, size);
      assert.deepEqual(issues, [], `${format} ${targetUrl}`);
    }
  }
});
