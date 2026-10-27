import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { loadSources } from '../lib/sources.js';
import { resolvePost } from '../lib/brief.js';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';
import { ensureSources } from './helpers.js';
import { slideHtml } from '../templates/slides.js';
import { withPage, loadSlide } from '../render/png.js';
import { renderShort, slideDuration } from '../render/short.js';

const BASE = path.join(SOCIAL_ROOT, 'out', 'test-week-short');
let sources;
let post;
let tmp;

before(() => {
  sources = loadSources(ensureSources());
  const brief = JSON.parse(fs.readFileSync(path.join(SOCIAL_ROOT, 'test', 'fixtures', 'brief-valid.json'), 'utf8'));
  post = resolvePost(brief.posts[1], sources);
  fs.mkdirSync(path.join(BASE, 'assets'), { recursive: true });
  fs.copyFileSync(path.join(REPO_ROOT, 'site', 'og', 'beregner.png'), path.join(BASE, 'assets', 'cover.png'));
  tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'short-test-'));
  execFileSync('ffmpeg', ['-v', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-t', '20', '-y', path.join(tmp, 'rolig-01.mp3')]);
});
after(() => fs.rmSync(tmp, { recursive: true, force: true }));

const probe = (file) =>
  JSON.parse(execFileSync('ffprobe', ['-v', 'error', '-show_streams', '-show_format', '-of', 'json', file]).toString());

test('renderShort rejects missing audio', async () => {
  await assert.rejects(
    renderShort({ ...post, audio: 'nope.mp3' }, path.join(tmp, 'x.mp4'), { baseDir: BASE, elpris: sources.elpris }),
    /Lydfil mangler: social\/audio\/nope\.mp3/,
  );
  assert.ok(!fs.existsSync(path.join(tmp, 'x.mp4')));
});

test('renderShort writes a 1080x1920 30 fps MP4 of 10-20 s with audio', async () => {
  const out = path.join(tmp, 'short.mp4');
  await renderShort(post, out, { baseDir: BASE, elpris: sources.elpris, audioDir: tmp });
  const info = probe(out);
  const v = info.streams.find((s) => s.codec_type === 'video');
  assert.equal(v.width, 1080);
  assert.equal(v.height, 1920);
  assert.equal(v.r_frame_rate, '30/1');
  assert.ok(info.streams.some((s) => s.codec_type === 'audio'));
  const dur = Number(info.format.duration);
  assert.ok(dur >= 10 && dur <= 20, `varighed ${dur}`);
});

test('renderShort throws a Danish error naming the duration when outside 10-20 s', async () => {
  const short = { ...post, slides: post.slides.slice(0, 2) };
  await assert.rejects(
    renderShort(short, path.join(tmp, 'kort.mp4'), { baseDir: BASE, elpris: sources.elpris, audioDir: tmp }),
    /længde.*\d+,\d s.*10.*20/,
  );
});

test('slideDuration is clamped to 2.5-5 s', () => {
  assert.equal(slideDuration({ title: 'Et' }), 2.75);
  assert.equal(slideDuration({ title: 'ord '.repeat(50) }), 5);
  assert.equal(slideDuration({}), 2.5);
});

test('seek: values count up with Danish formatting, end exactly on the final text, width stays fixed', async () => {
  const slide = { layout: 'stat', tag: 'T', title: 'Titel', value: '32.388 kr.', body: 'x', highlight: '32.388 kr.' };
  const html = slideHtml(slide, { index: 0, total: 1, format: 'short' });
  const res = await withPage(
    async (page) => {
      await loadSlide(page, html);
      const read = (t) =>
        page.evaluate((tt) => {
          window.seek(tt);
          const el = document.querySelector('.value');
          return { text: el.textContent, w: el.getBoundingClientRect().width, h: el.getBoundingClientRect().height, op: getComputedStyle(document.querySelector('.title')).opacity };
        }, t);
      const out = { a: await read(0.2), b: await read(0.5), end: await read(10) };
      out.final = await page.evaluate(() => ({ html: document.querySelector('.value').innerHTML, style: document.querySelector('.value').getAttribute('style') }));
      return out;
    },
    { width: 1080, height: 1920 },
  );
  for (const k of ['a', 'b']) assert.match(res[k].text, /^\d{1,2}(\.\d{3})? kr\.$/.replace ? /^[\d.]+ kr\.$/ : /./, `${k}: ${res[k].text}`);
  assert.notEqual(res.a.text, res.end.text);
  assert.equal(res.end.text, '32.388 kr.');
  assert.equal(res.a.w, res.end.w);
  assert.equal(res.b.w, res.end.w);
  assert.equal(res.a.h, res.end.h);
  assert.equal(res.end.op, '1');
  assert.ok(!res.final.html.includes('inline-block'), res.final.html);
});
