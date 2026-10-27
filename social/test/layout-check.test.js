import { test, before } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { loadSources } from '../lib/sources.js';
import { resolvePost } from '../lib/brief.js';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';
import { ensureSources } from './helpers.js';
import { slideHtml } from '../templates/slides.js';
import { withPage, loadSlide, renderCarousel } from '../render/png.js';
import { checkLayout, LayoutError } from '../render/layout-check.js';

const RUNTIME = fs.readFileSync(path.join(SOCIAL_ROOT, 'templates', 'runtime.js'), 'utf8');
const BASE = path.join(SOCIAL_ROOT, 'out', 'test-week');
let sources;
let post;

before(() => {
  sources = loadSources(ensureSources());
  const brief = JSON.parse(fs.readFileSync(path.join(SOCIAL_ROOT, 'test', 'fixtures', 'brief-valid.json'), 'utf8'));
  post = resolvePost(brief.posts[0], sources);
  fs.mkdirSync(path.join(BASE, 'assets'), { recursive: true });
  fs.copyFileSync(path.join(REPO_ROOT, 'site', 'og', 'beregner.png'), path.join(BASE, 'assets', 'cover.png'));
});

const STYLE = `<style>
*{box-sizing:border-box} body{margin:0;font:30px sans-serif}
.slide-safe{position:relative;margin:72px;width:936px;height:600px}
.cta{background:#0b4f43;color:#fff;padding:20px;width:500px}
.kpi{width:200px;padding:40px;border:3px solid #ccc}
.kpi .v{font-size:90px;font-weight:700;white-space:nowrap}
</style>`;

const check = (body, fn) =>
  withPage(async (page) => {
    await page.setContent(`<!doctype html>${STYLE}<body><div class="slide-safe">${body}</div></body>`);
    await page.addScriptTag({ content: RUNTIME });
    if (fn) await page.evaluate(fn);
    return checkLayout(page);
  });

test('flags a CTA box placed over a source line', async () => {
  const issues = await check(
    '<div style="position:absolute;top:500px;left:0">Kilde: Bolius</div>' +
      '<div class="cta" style="position:absolute;top:480px;left:0">Regn på dit eget hus</div>',
  );
  const overlaps = issues.filter((i) => i.kind === 'overlap');
  assert.ok(overlaps.length >= 1 && overlaps.every((i) => /Kilde: Bolius/.test(i.text)), JSON.stringify(issues));
  assert.ok(overlaps.some((i) => /knap/.test(i.text)), 'CTA-boksen selv skal tælle');
  assert.deepEqual(issues.filter((i) => i.kind !== 'overlap'), []);
});

test('text inside its own CTA is not an overlap; multi-line heading is not an overlap', async () => {
  const issues = await check(
    '<h1 style="width:400px;line-height:.8;margin:0;padding-top:30px">Et ret langt overskrift der brydes over flere linjer</h1>' +
      '<div class="cta" style="margin-top:300px">Se dagens priser →</div>',
  );
  assert.deepEqual(issues, []);
});

test('flags two blocks overlapping in both axes, but not 2px touching', async () => {
  const bad = await check(
    '<div style="position:absolute;top:0">AAAA AAAA</div><div style="position:absolute;top:10px">BBBB BBBB</div>',
  );
  assert.equal(bad.filter((i) => i.kind === 'overlap').length, 1);
  const ok = await check(
    '<div style="position:absolute;top:0;line-height:40px">AAAA</div><div style="position:absolute;top:40px;line-height:40px">BBBB</div>',
  );
  assert.deepEqual(ok, []);
});

test('fitText shrinks then layout check flags overflow at min size', async () => {
  const body = '<div class="kpi"><div class="v" data-fit="kpi" data-min="44">32.388</div></div>';
  const issues = await check(body, () => {
    const el = document.querySelector('.v');
    window.__size = window.fitText(el, 44);
  });
  assert.ok(issues.some((i) => i.kind === 'outside' && /32\.388/.test(i.text)), JSON.stringify(issues));
});

test('flags a wrapped value', async () => {
  const issues = await check('<div class="value" style="width:200px;font-size:60px">Mange ord her nu</div>');
  assert.ok(issues.some((i) => i.kind === 'wrap'), JSON.stringify(issues));
});

test('flags text beyond the safe area', async () => {
  const issues = await check('<div style="position:absolute;left:900px;white-space:nowrap">Lang tekst ud af rammen</div>');
  assert.ok(issues.some((i) => i.kind === 'outside'), JSON.stringify(issues));
});

test('every slide of brief-valid.json has zero layout issues', async () => {
  for (const [index, slide] of post.slides.entries()) {
    const html = slideHtml(slide, { index, total: post.slides.length, format: 'carousel', elpris: sources.elpris, targetUrl: post.target_url, baseDir: BASE });
    const issues = await withPage(async (page) => {
      await loadSlide(page, html);
      return checkLayout(page);
    });
    assert.deepEqual(issues, [], `slide ${index + 1}`);
  }
});

test('renderCarousel throws LayoutError and writes no PNG for a broken slide', async () => {
  const out = path.join(SOCIAL_ROOT, 'out', 'test-broken');
  fs.rmSync(out, { recursive: true, force: true });
  const broken = {
    ...post,
    id: 'broken',
    slides: [{ layout: 'kpi2', tag: 'TEST', title: 'T', kpis: [{ label: 'a', value: '1.234.567.890.123' }, { label: 'b', value: '2' }], sources: ['Bolius'] }],
  };
  await assert.rejects(
    renderCarousel(broken, out, { baseDir: BASE }),
    (e) => e instanceof LayoutError && e.issues.length > 0 && /outside/.test(e.message),
  );
  assert.deepEqual(fs.existsSync(out) ? fs.readdirSync(out) : [], []);
});

// --- bars / screenshot ---
const hoursOf = () => sources.elpris['2026-10-27'].DK1.hours;
const barsSlide = (extra = {}) => ({
  layout: 'bars', tag: 'ELPRIS', title: 'Billigste time i morgen', body: 'Se hvornår strømmen er billig.',
  bars: { date: '2026-10-27', area: 'DK1', hours: hoursOf() }, sources: ['Energi Data Service'], ...extra,
});
const checkSlide = (slide, { format = 'carousel', size } = {}) =>
  withPage(
    async (page) => {
      await loadSlide(page, slideHtml(slide, { index: 0, total: 2, format, targetUrl: post.target_url, baseDir: BASE, screenshotPath: path.join(REPO_ROOT, 'site', 'og', 'beregner.png') }));
      return checkLayout(page);
    },
    size ?? { width: 1080, height: 1350 },
  );
const LONG = 'Dette er en meget lang titel om elprisen i morgen som fylder rigtig mange linjer og presser alt andet ned i bunden af sliden '.repeat(3);

test('bars slides (with and without CTA, carousel and story) have zero issues', async () => {
  assert.deepEqual(await checkSlide(barsSlide()), []);
  assert.deepEqual(await checkSlide(barsSlide({ cta: 'Se dagens priser' })), []);
  assert.deepEqual(await checkSlide(barsSlide(), { format: 'story', size: { width: 1080, height: 1920 } }), []);
  assert.deepEqual(await checkSlide(barsSlide({ cta: 'Se dagens priser' }), { format: 'story', size: { width: 1080, height: 1920 } }), []);
});

test('screenshot slide has zero issues', async () => {
  const slide = { layout: 'screenshot', tag: 'BEREGNER', title: 'Sådan ser det ud', screenshot: 'x', sources: ['Bolius'] };
  assert.deepEqual(await checkSlide(slide), []);
});

test('a long title that pushes chart/CTA into the footer is flagged', async () => {
  const issues = await checkSlide(barsSlide({ title: LONG, cta: 'Se dagens priser' }));
  assert.ok(issues.length > 0, 'skulle være flagget');
});

test('a squeezed phone screenshot is flagged', async () => {
  const slide = { layout: 'screenshot', tag: 'BEREGNER', title: LONG, screenshot: 'x', sources: ['Bolius'] };
  const issues = await checkSlide(slide);
  assert.ok(issues.some((i) => /telefonbillede/.test(i.text)), JSON.stringify(issues));
});

test('text overlapping .phone or .chart is flagged', async () => {
  const a = await check('<div class="phone" style="width:300px;height:300px"></div><div style="position:absolute;top:100px;left:50px">Hej verden</div>');
  assert.ok(a.some((i) => i.kind === 'overlap' && /telefonbillede/.test(i.text)), JSON.stringify(a));
  const b = await check('<div class="chart" style="width:300px;height:300px"></div><div style="position:absolute;top:100px;left:50px">Hej verden</div>');
  assert.ok(b.some((i) => i.kind === 'overlap' && /diagram/.test(i.text)), JSON.stringify(b));
});
