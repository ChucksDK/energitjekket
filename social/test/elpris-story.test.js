import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync, execFileSync } from 'node:child_process';
import { SOCIAL_ROOT } from '../lib/paths.js';
import { ensureSources, FIXTURE_ELPRIS } from './helpers.js';
import { danishWeekday, tomorrowCopenhagen, barsSlide, storyTag, pickAudio, main } from '../bin/elpris-story.js';
import { loadSources } from '../lib/sources.js';
import { resolvePost } from '../lib/brief.js';

const BIN = path.join(SOCIAL_ROOT, 'bin', 'elpris-story.js');
let sourcesFile;
let tmp;
let satElpris;
let audioDir;

before(() => {
  sourcesFile = ensureSources();
  tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'story-test-'));
  // Fixturens dag kopieret til lørdag 2026-10-31 (til --reel).
  const raw = JSON.parse(fs.readFileSync(FIXTURE_ELPRIS, 'utf8'));
  raw.days['2026-10-31'] = raw.days['2026-10-27'];
  satElpris = path.join(tmp, 'elpris-sat.json');
  fs.writeFileSync(satElpris, JSON.stringify(raw));
  audioDir = path.join(tmp, 'audio');
  fs.mkdirSync(audioDir);
  execFileSync('ffmpeg', ['-v', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-t', '20', '-y', path.join(audioDir, 'a-01.mp3')]);
});
after(() => fs.rmSync(tmp, { recursive: true, force: true }));

const run = (...args) => spawnSync('node', [BIN, ...args], { encoding: 'utf8' });
// Hvert kald får sit eget register (scriptet skriver det selv).
let n = 0;
const reg = () => path.join(tmp, `sources-${(n += 1)}.json`);
const pngSize = (file) => {
  const b = fs.readFileSync(file);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
};

test('danishWeekday and tomorrowCopenhagen', () => {
  assert.equal(danishWeekday('2026-10-27'), 'tirsdag');
  assert.equal(danishWeekday('2026-10-31'), 'lørdag');
  assert.equal(danishWeekday('2026-11-01'), 'søndag');
  // 23:30 UTC 27/10 er allerede 28/10 i København (CET efter sommertid): i morgen = 29/10.
  assert.equal(tomorrowCopenhagen(new Date('2026-10-27T23:30:00Z')), '2026-10-29');
  assert.equal(tomorrowCopenhagen(new Date('2026-10-27T10:00:00Z')), '2026-10-28');
});

test('story refreshes the register itself and writes two 1080x1920 PNGs', () => {
  const out = path.join(tmp, 'ok');
  const sources = reg();
  assert.ok(!fs.existsSync(sources));
  const r = run('--date', '2026-10-27', '--sources', sources, '--elpris', FIXTURE_ELPRIS, '--out', out);
  assert.equal(r.status, 0, r.stderr);
  assert.ok(loadSources(sources).elpris['2026-10-27'], 'registeret er skrevet af scriptet');
  for (const a of ['DK1', 'DK2']) {
    assert.deepEqual(pngSize(path.join(out, `elpris-${a}.png`)), { w: 1080, h: 1920 });
  }
  assert.deepEqual(fs.readdirSync(out).sort(), ['elpris-DK1.png', 'elpris-DK2.png']);
  assert.deepEqual(fs.readdirSync(tmp).filter((f) => f.startsWith('.story-tmp-')), [], 'ingen temp-mapper tilbage');
});

test('story exits 3 when target day missing', () => {
  const out = path.join(tmp, 'missing');
  fs.mkdirSync(out);
  const r = run('--date', '2030-01-01', '--sources', reg(), '--elpris', FIXTURE_ELPRIS, '--out', out);
  assert.equal(r.status, 3, r.stderr);
  assert.deepEqual(fs.readdirSync(out), []);
});

test('missing date is exit 3 even when --reel has no audio (date is checked before audio)', () => {
  const emptyDir = path.join(tmp, 'noaudio-3');
  fs.mkdirSync(emptyDir);
  const r = run('--reel', '--date', '2026-11-07', '--sources', reg(), '--elpris', FIXTURE_ELPRIS, '--out', path.join(tmp, 'y'), '--audio-dir', emptyDir);
  assert.equal(r.status, 3, r.stderr);
});

test('--reel on a non-Saturday exits 4 with "kun lørdag"', () => {
  const out = path.join(tmp, 'notsat');
  const r = run('--reel', '--date', '2026-10-27', '--sources', reg(), '--elpris', FIXTURE_ELPRIS, '--out', out);
  assert.equal(r.status, 4);
  assert.match(r.stderr, /kun lørdag/);
  assert.ok(!fs.existsSync(out));
});

test('--reel on a Saturday writes a 10-20 s MP4 beside the stories', () => {
  const out = path.join(tmp, 'sat');
  const r = run('--reel', '--date', '2026-10-31', '--sources', reg(), '--elpris', satElpris, '--out', out, '--audio-dir', audioDir);
  assert.equal(r.status, 0, r.stderr);
  const mp4 = path.join(out, 'reel-2026-10-31.mp4');
  const d = Number(execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4]).toString());
  assert.ok(d >= 10 && d <= 20, `varighed ${d}`);
  assert.ok(fs.existsSync(path.join(out, 'elpris-DK1.png')));
});

test('--reel without any audio file exits 4 naming the problem', () => {
  const emptyDir = path.join(tmp, 'noaudio');
  fs.mkdirSync(emptyDir);
  const r = run('--reel', '--date', '2026-10-31', '--sources', reg(), '--elpris', satElpris, '--out', path.join(tmp, 'x'), '--audio-dir', emptyDir);
  assert.equal(r.status, 4);
  assert.match(r.stderr, /Ingen lydfil/);
});

test('story text names the price as spotpris (finding 2)', () => {
  const src = loadSources(sourcesFile);
  const post = resolvePost({ id: 'x', type: 'carousel', slides: [barsSlide('2026-10-27', 'DK1', false)] }, src);
  assert.match(post.slides[0].body, /^Spotpris: billigst -?\d+,\d\d kr\. pr\. kWh, dyrest -?\d+,\d\d kr\. kl\. \d\d\.$/);
  assert.ok(post.slides[0].sources.every((n) => /spotpris/.test(n)));
});

test('story tag names the price area, not DK1/DK2 (finding 7)', () => {
  assert.equal(storyTag('2026-10-27', 'DK1'), 'ELPRIS · 27/10 · VESTDANMARK');
  assert.equal(storyTag('2026-10-27', 'DK2'), 'ELPRIS · 27/10 · ØSTDANMARK');
});

test('pickAudio rotates through the folder by date, deterministically (finding 7)', () => {
  const dir = path.join(tmp, 'rot');
  fs.mkdirSync(dir);
  for (const f of ['a.m4a', 'b.m4a', 'c.mp3', 'notes.txt']) fs.writeFileSync(path.join(dir, f), '');
  const picks = ['2026-10-31', '2026-11-07', '2026-11-14', '2026-11-21'].map((d) => pickAudio({ audioDir: dir }, d));
  assert.equal(new Set(picks).size, 3, picks.join(','));
  assert.ok(picks.every((p) => ['a.m4a', 'b.m4a', 'c.mp3'].includes(p)));
  assert.equal(pickAudio({ audioDir: dir }, '2026-10-31'), picks[0]);
  assert.equal(pickAudio({ audioDir: dir, audio: 'x.mp3' }, '2026-10-31'), 'x.mp3');
});

test('if the second story fails, no lone first PNG is left (finding 7)', async () => {
  const out = path.join(tmp, 'half');
  let calls = 0;
  const renderStory = async (post, file) => {
    calls += 1;
    if (calls === 2) throw new Error('DK2 gik galt');
    fs.writeFileSync(file, 'png');
    return file;
  };
  await assert.rejects(
    main(['--date', '2026-10-27', '--sources', reg(), '--elpris', FIXTURE_ELPRIS, '--out', out], { renderStory }),
    /DK2 gik galt/,
  );
  assert.equal(calls, 2);
  assert.ok(!fs.existsSync(out) || fs.readdirSync(out).length === 0);
  assert.deepEqual(fs.readdirSync(tmp).filter((f) => f.startsWith('.story-tmp-')), []);
});
