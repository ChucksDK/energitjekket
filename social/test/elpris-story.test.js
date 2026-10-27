import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync, execFileSync } from 'node:child_process';
import { SOCIAL_ROOT } from '../lib/paths.js';
import { ensureSources } from './helpers.js';
import { danishWeekday, tomorrowCopenhagen } from '../bin/elpris-story.js';

const BIN = path.join(SOCIAL_ROOT, 'bin', 'elpris-story.js');
let sourcesFile;
let tmp;

before(() => {
  sourcesFile = ensureSources();
  tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'story-test-'));
});
after(() => fs.rmSync(tmp, { recursive: true, force: true }));

const run = (...args) => spawnSync('node', [BIN, ...args], { encoding: 'utf8' });
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

test('story writes two 1080x1920 PNGs', () => {
  const out = path.join(tmp, 'ok');
  const r = run('--date', '2026-10-27', '--sources', sourcesFile, '--out', out);
  assert.equal(r.status, 0, r.stderr);
  for (const a of ['DK1', 'DK2']) {
    assert.deepEqual(pngSize(path.join(out, `elpris-${a}.png`)), { w: 1080, h: 1920 });
  }
  assert.equal(fs.readdirSync(out).length, 2);
});

test('story exits 3 when target day missing', () => {
  const out = path.join(tmp, 'missing');
  fs.mkdirSync(out);
  const r = run('--date', '2030-01-01', '--sources', sourcesFile, '--out', out);
  assert.equal(r.status, 3);
  assert.deepEqual(fs.readdirSync(out), []);
});

test('--reel on a non-Saturday exits 4 with "kun lørdag"', () => {
  const out = path.join(tmp, 'notsat');
  const r = run('--reel', '--date', '2026-10-27', '--sources', sourcesFile, '--out', out);
  assert.equal(r.status, 4);
  assert.match(r.stderr, /kun lørdag/);
  assert.ok(!fs.existsSync(out));
});

test('--reel on a Saturday writes a 10-20 s MP4 beside the stories', () => {
  // Kopier fixturens dag til lørdag 2026-10-31 i et midlertidigt register.
  const src = JSON.parse(fs.readFileSync(sourcesFile, 'utf8'));
  src.elpris['2026-10-31'] = src.elpris['2026-10-27'];
  for (const [id, f] of Object.entries({ ...src.facts })) {
    if (id.startsWith('elpris.2026-10-27.')) src.facts[id.replace('2026-10-27', '2026-10-31')] = f;
  }
  const sat = path.join(tmp, 'sat-sources.json');
  fs.writeFileSync(sat, JSON.stringify(src));
  const audioDir = path.join(tmp, 'audio');
  fs.mkdirSync(audioDir);
  execFileSync('ffmpeg', ['-v', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-t', '20', '-y', path.join(audioDir, 'a-01.mp3')]);
  const out = path.join(tmp, 'sat');
  const r = run('--reel', '--date', '2026-10-31', '--sources', sat, '--out', out, '--audio-dir', audioDir);
  assert.equal(r.status, 0, r.stderr);
  const mp4 = path.join(out, 'reel-2026-10-31.mp4');
  const d = Number(execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4]).toString());
  assert.ok(d >= 10 && d <= 20, `varighed ${d}`);
  assert.ok(fs.existsSync(path.join(out, 'elpris-DK1.png')));
});

test('--reel without any audio file exits 4 naming the problem', () => {
  const emptyDir = path.join(tmp, 'noaudio');
  fs.mkdirSync(emptyDir);
  const r = run('--reel', '--date', '2026-10-31', '--sources', sourcesFile, '--out', path.join(tmp, 'x'), '--audio-dir', emptyDir);
  assert.equal(r.status, 4);
});
