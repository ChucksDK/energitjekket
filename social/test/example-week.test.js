import { test, before } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { loadSources } from '../lib/sources.js';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';
import { validatePost, resolvePost } from '../lib/brief.js';
import { slideDuration, CROSSFADE } from '../render/short.js';
import { pagePath } from '../render/screenshot.js';
import { ensureSources } from './helpers.js';

const BRIEF = path.join(SOCIAL_ROOT, 'briefs', 'EXAMPLE-2026-W45.json');
let s;
let brief;
before(() => {
  s = loadSources(ensureSources());
  brief = JSON.parse(fs.readFileSync(BRIEF, 'utf8'));
});

const area = (p) => {
  const url = p.target_url || '';
  if (p.pillar === 'varmepumpe' || (p.city && url.includes('/varmepumpe/'))) return 'varmepumpe';
  if (p.pillar === 'solceller' || (p.city && url.includes('/solceller/'))) return 'solceller';
  return p.pillar;
};

test('example week has 13 posts: 7 carousels at 07:30, 6 shorts at 19:30, Friday 19:30 left for the elpris reel (Ruling F1)', () => {
  assert.equal(brief.week, 'EXAMPLE-2026-W45');
  assert.equal(brief.posts.length, 13);
  const carousels = brief.posts.filter((p) => p.type === 'carousel');
  const shorts = brief.posts.filter((p) => p.type === 'short');
  assert.equal(carousels.length, 7);
  assert.equal(shorts.length, 6);
  assert.ok(carousels.every((p) => p.slot.endsWith('T07:30')), 'carousels kl. 07:30');
  assert.ok(shorts.every((p) => p.slot.endsWith('T19:30')), 'shorts kl. 19:30');
  const days = new Set(brief.posts.map((p) => p.slot.slice(0, 10)));
  assert.equal(days.size, 7);
  assert.equal(new Set(brief.posts.map((p) => p.id)).size, 13);
  assert.equal(new Set(brief.posts.map((p) => p.slot)).size, 13);
  const friday = brief.posts.filter((p) => new Date(`${p.slot}:00Z`).getUTCDay() === 5);
  assert.deepEqual(friday.map((p) => p.slot.slice(11)), ['07:30'], 'fredag 19:30 er reelens plads');
});

test('every post in the example week validates', () => {
  for (const p of brief.posts) assert.deepEqual(validatePost(p, s), [], p.id);
});

test('pillar mix: at least 8 heat pump posts, at most 6 solar posts', () => {
  const count = (a) => brief.posts.filter((p) => area(p) === a).length;
  assert.ok(count('varmepumpe') >= 8, `varmepumpe: ${count('varmepumpe')}`);
  assert.ok(count('solceller') <= 6, `solceller: ${count('solceller')}`);
});

test('week contains two city posts, a quiz, a calculator short with screenshot and no elpris bars post (F1)', () => {
  const cities = new Set(brief.posts.filter((p) => p.city).map((p) => p.city));
  assert.ok(cities.size >= 2, [...cities].join(','));
  assert.ok(brief.posts.some((p) => p.angle && /quiz/i.test(p.angle)));
  assert.ok(brief.posts.some((p) => p.type === 'short' && p.slides.some((sl) => sl.layout === 'screenshot' && sl.screenshot === 'beregner')));
  assert.ok(!brief.posts.some((p) => p.pillar === 'elpris' || p.slides.some((sl) => sl.layout === 'bars')), 'elpris hører til elpris-story.js');
});

test('screenshots, audio and short durations are buildable', () => {
  for (const p of brief.posts) {
    for (const sl of p.slides) if (sl.layout === 'screenshot') assert.ok(pagePath(sl.screenshot), `${p.id}: ${sl.screenshot}`);
    if (p.type !== 'short') continue;
    assert.ok(fs.existsSync(path.join(SOCIAL_ROOT, 'audio', p.audio)), `${p.id}: ${p.audio}`);
    const { slides } = resolvePost(p, s);
    const total = slides.reduce((a, sl) => a + slideDuration(sl), 0) - CROSSFADE * (slides.length - 1);
    assert.ok(total >= 10 && total <= 20, `${p.id}: ${total.toFixed(1)} s`);
  }
});

// --- finding 21 ---
test('captions: 3-6 lines, mention "link i bio"; 3-5 hashtags', () => {
  for (const p of brief.posts) {
    const lines = p.caption.split('\n').filter((l) => l.trim());
    assert.ok(lines.length >= 3 && lines.length <= 6, `${p.id}: ${lines.length} linjer`);
    assert.match(p.caption, /link i bio/i, p.id);
    assert.ok(p.hashtags.length >= 3 && p.hashtags.length <= 5, `${p.id}: ${p.hashtags.length} hashtags`);
  }
});

test('every target_url is a page under site/', () => {
  for (const p of brief.posts) {
    const rel = new URL(p.target_url).pathname.split('/').filter(Boolean);
    assert.ok(fs.existsSync(path.join(REPO_ROOT, 'site', ...rel, 'index.html')), `${p.id}: ${p.target_url}`);
  }
});

test('bg images exist next to the brief (tracked in git)', () => {
  const bgs = brief.posts.flatMap((p) => p.slides.filter((sl) => sl.bg).map((sl) => [p.id, sl.bg]));
  assert.ok(bgs.length >= 1);
  for (const [id, bg] of bgs) assert.ok(fs.existsSync(path.join(path.dirname(BRIEF), bg)), `${id}: ${bg}`);
});

test('city posts use different cities', () => {
  const cities = brief.posts.filter((p) => p.city).map((p) => p.city);
  assert.equal(new Set(cities).size, cities.length, cities.join(','));
});

test('posts end on an end slide (link from target_url), not a "LINK I BIO" text slide', () => {
  for (const p of brief.posts) {
    assert.ok(!p.slides.some((sl) => sl.tag === 'LINK I BIO'), p.id);
  }
  assert.ok(brief.posts.filter((p) => p.slides.at(-1).layout === 'end').length >= 10);
});
