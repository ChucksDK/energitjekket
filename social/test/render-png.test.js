import { test, before } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { loadSources } from '../lib/sources.js';
import { resolvePost } from '../lib/brief.js';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';
import { ensureSources } from './helpers.js';
import { slideHtml } from '../templates/slides.js';
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
  assert.match(last, /energitjekket\.dk\/beregner/);
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
