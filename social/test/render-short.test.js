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
import { renderShort, slideDuration, slideBody, fadeAt, CROSSFADE } from '../render/short.js';

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
  for (const k of ['a', 'b']) {
    assert.match(res[k].text, /^[\d.]+\u00a0kr\.$/, `${k}: ${res[k].text}`);
    assert.notEqual(res[k].text, res.end.text, `${k} er allerede sluttallet`);
  }
  assert.notEqual(res.a.text, res.end.text);
  assert.equal(res.end.text, '32.388 kr.');
  assert.equal(res.a.w, res.end.w);
  assert.equal(res.b.w, res.end.w);
  assert.equal(res.a.h, res.end.h);
  assert.equal(res.end.op, '1');
  assert.ok(!res.final.html.includes('inline-block'), res.final.html);
});

test('mountNext resolves only when the next slide background and images are loaded', async () => {
  const bgSlide = { ...post.slides[0] }; // cover med bg
  const shotFile = path.join(BASE, 'assets', 'cover.png');
  const next = slideHtml(bgSlide, { index: 1, total: 3, format: 'short', baseDir: BASE, targetUrl: post.target_url });
  const cur = slideHtml(post.slides[1], { index: 0, total: 3, format: 'short', baseDir: BASE, targetUrl: post.target_url });
  const res = await withPage(
    async (page) => {
      await loadSlide(page, cur);
      return page.evaluate(async ([m, img]) => {
        const markup = m.replace('<div class="slide-safe">', `<div class="slide-safe"><img id="probe" src="${img}" style="width:10px;height:10px">`);
        const decoded = [];
        const RealImage = window.Image;
        window.Image = function () {
          const im = new RealImage();
          const d = im.decode.bind(im);
          im.decode = () => d().then((r) => (decoded.push(im.src), r));
          return im;
        };
        await window.mountNext(markup);
        window.Image = RealImage;
        const probe = document.getElementById('probe');
        const bgUrl = /url\("?([^")]+)"?\)/.exec(document.querySelector('#under .slide').style.background)?.[1];
                return { complete: probe.complete, w: probe.naturalWidth, bgUrl: !!bgUrl, bgDone: decoded.includes(bgUrl) };
      }, [slideBody(next), 'file://' + shotFile]);
    },
    { width: 1080, height: 1920 },
  );
  assert.ok(res.complete && res.w > 0, JSON.stringify(res));
  assert.ok(res.bgUrl && res.bgDone, JSON.stringify(res));
});

test('renderShort rejects audio names with path separators or ..', async () => {
  for (const name of ['../x.mp3', 'a/b.mp3', 'a\\b.mp3', '..']) {
    await assert.rejects(
      renderShort({ ...post, audio: name }, path.join(tmp, 'y.mp4'), { baseDir: BASE, elpris: sources.elpris, audioDir: tmp }),
      /Ugyldigt lydfilnavn/,
      name,
    );
  }
});

test('renderShort cleans up its temp frames dir on LayoutError', async () => {
  const frameDirs = () => fs.readdirSync(os.tmpdir()).filter((f) => f.startsWith('short-frames-')).length;
  const before = frameDirs();
  const bad = { ...post, slides: post.slides.map((s, i) => (i === 1 ? { ...s, value: 'X'.repeat(45) } : s)) };
  await assert.rejects(
    renderShort(bad, path.join(tmp, 'bad.mp4'), { baseDir: BASE, elpris: sources.elpris, audioDir: tmp }),
    /Layoutfejl/,
  );
  assert.equal(frameDirs(), before);
});

// --- finding 9: ingen frame med tekst fra to slides ---
test('fadeAt: outgoing slide is gone before the incoming text appears', () => {
  const steps = 300;
  let prevOut = 1;
  for (let i = 0; i <= steps; i += 1) {
    const k = (CROSSFADE * i) / steps;
    const { out, in: inn } = fadeAt(k);
    assert.ok(!(out > 0.05 && inn > 0.05), `k=${k.toFixed(3)}: out=${out} in=${inn}`);
    assert.ok(out <= prevOut + 1e-9, 'udgående fader kun ud');
    prevOut = out;
  }
  assert.deepEqual(fadeAt(0), { out: 1, in: 0 });
  assert.equal(fadeAt(CROSSFADE).out, 0);
  assert.equal(fadeAt(CROSSFADE).in, 1);
});

test('transition frames never show text from both slides (30 fps through the crossfade)', async () => {
  const a = slideHtml({ layout: 'stat', tag: 'A', title: 'Første slide', value: '32.388 kr.', body: 'om året.' }, { index: 0, total: 2, format: 'short' });
  const b = slideHtml({ layout: 'text', tag: 'B', title: 'Andet slide', body: 'Noget andet.' }, { index: 1, total: 2, format: 'short' });
  const frames = await withPage(
    async (page) => {
      await loadSlide(page, a);
      await page.evaluate((m) => window.mountNext(m), slideBody(b));
      const out = [];
      for (let n = 0; n <= Math.ceil(CROSSFADE * 30); n += 1) {
        const k = n / 30;
        const f = fadeAt(Math.min(k, CROSSFADE));
        out.push(
          await page.evaluate(
            ([kk, o, i]) => {
              window.seek(3 + kk);
              window.seekNext(kk);
              window.setFade(o, i);
              // Effektiv opacitet = produktet op gennem forfædrene.
              const eff = (el) => {
                let v = 1;
                for (let e = el; e; e = e.parentElement) v *= Number(getComputedStyle(e).opacity);
                return v;
              };
              const cur = document.querySelector('.slide:not(#under .slide) .title');
              const nxt = document.querySelector('#under .slide .title');
              return { k: kk, cur: eff(cur), next: eff(nxt) };
            },
            [k, f.out, f.in],
          ),
        );
      }
      return out;
    },
    { width: 1080, height: 1920 },
  );
  for (const f of frames) assert.ok(!(f.cur > 0.05 && f.next > 0.05), JSON.stringify(f));
  assert.ok(frames[0].cur > 0.95);
  assert.ok(frames.at(-1).next > 0.95 || frames.at(-1).k >= CROSSFADE, JSON.stringify(frames.at(-1)));
});

// --- finding 12: tal, der aldrig har eksisteret, vises ikke ---
test('seek: prices, hours and years appear at full value (no count-up); integers still count', async () => {
  const read = (value) =>
    withPage(
      async (page) => {
        await loadSlide(page, slideHtml({ layout: 'stat', tag: 'T', title: 'Titel', value, body: 'x' }, { index: 0, total: 1, format: 'short' }));
        return page.evaluate(() => {
          window.seek(0.2);
          return document.querySelector('.value').textContent;
        });
      },
      { width: 1080, height: 1920 },
    );
  assert.equal(await read('0,45 kr.'), '0,45\u00a0kr.');
  assert.equal(await read('-0,05 kr.'), '-0,05\u00a0kr.');
  assert.equal(await read('kl. 06'), 'kl.\u00a006');
  assert.equal(await read('2028'), '2028');
  assert.equal(await read('3,2'), '3,2');
  assert.notEqual(await read('32.388 kr.'), '32.388\u00a0kr.');
  assert.notEqual(await read('47 %'), '47\u00a0%');
});
