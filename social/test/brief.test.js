import { test, before } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { loadSources } from '../lib/sources.js';
import { SOCIAL_ROOT } from '../lib/paths.js';
import { ensureSources } from './helpers.js';
import { resolveText, validatePost, resolvePost } from '../lib/brief.js';

let s;
let valid;
let bad;
const fx = (n) => JSON.parse(fs.readFileSync(path.join(SOCIAL_ROOT, 'test', 'fixtures', n), 'utf8'));
before(() => {
  s = loadSources(ensureSources());
  valid = fx('brief-valid.json');
  bad = fx('brief-bad.json');
});

const clone = (o) => structuredClone(o);
const mod = (fn) => {
  const p = clone(valid.posts[0]);
  fn(p);
  return validatePost(p, s);
};
const has = (errs, needle) => errs.some((e) => e.includes(needle));

test('resolveText formats placeholders and reports fact ids', () => {
  const r = resolveText('ca. {bolius.oliefyr}', s);
  assert.equal(r.text, 'ca. 32.388 kr.');
  assert.deepEqual(r.factIds, ['bolius.oliefyr']);
});

test('resolveText throws on unknown fact id', () => {
  assert.throws(() => resolveText('{nope.x}', s), /Ukendt fakta-id: nope\.x/);
});

test('valid fixture: both posts have no errors', () => {
  for (const p of valid.posts) assert.deepEqual(validatePost(p, s), []);
});

test('valid fixture: carousel and short shapes', () => {
  const [c, sh] = valid.posts;
  assert.ok(c.slides.length >= 5 && c.slides.length <= 7);
  assert.equal(sh.audio, 'rolig-01.mp3');
  assert.ok(sh.slides.length >= 3 && sh.slides.length <= 6);
});

test('digit without source is an error', () => {
  const e = mod((p) => (p.slides[1].title = 'Spar 30.000 kr.'));
  assert.ok(has(e, 'tal uden kilde: "30.000"'), e.join('|'));
});

test('years 2020-2035 are allowed', () => {
  const e = mod((p) => (p.slides[1].title = 'Priser i 2028'));
  assert.ok(!has(e, 'tal uden kilde'), e.join('|'));
});

test('year-like 2040 is not allowed', () => {
  assert.ok(has(mod((p) => (p.slides[1].title = 'Om 2040')), 'tal uden kilde: "2040"'));
});

test('digits in caption and hashtags are errors', () => {
  assert.ok(has(mod((p) => (p.caption = 'Spar 5 procent')), 'tal uden kilde: "5"'));
  assert.ok(has(mod((p) => (p.hashtags = ['#viborg2'])), 'tal uden kilde'));
});

test('banned punctuation and phrases', () => {
  assert.ok(has(mod((p) => (p.caption = 'Se nu!')), 'forbudt: "!"'));
  assert.ok(has(mod((p) => (p.slides[3].body = 'Det er GRATIS her')), 'forbudt: "gratis"'));
  assert.ok(has(mod((p) => (p.slides[3].body = 'Spar op til meget')), 'forbudt: "spar op til"'));
});

test('tilbud only allowed when quote is true', () => {
  const url = 'https://energitjekket.dk/solceller/tilbud/';
  assert.ok(has(mod((p) => (p.target_url = url)), 'tilbud'));
  assert.ok(has(mod((p) => (p.caption = 'Få tilbud nu')), 'tilbud'));
  const ok = mod((p) => {
    p.quote = true;
    p.target_url = url;
    p.caption = 'Få tilbud på solceller.';
  });
  assert.ok(!has(ok, 'tilbud'), ok.join('|'));
});

test('target_url must be on energitjekket.dk', () => {
  assert.ok(has(mod((p) => (p.target_url = 'https://example.com/')), 'target_url'));
});

test('slide counts', () => {
  assert.ok(has(mod((p) => (p.slides = p.slides.slice(0, 4))), 'slides'));
  const sh = clone(valid.posts[1]);
  sh.slides = Array.from({ length: 7 }, () => clone(sh.slides[1]));
  assert.ok(has(validatePost(sh, s), 'slides'));
});

test('bg only on first slide', () => {
  assert.ok(has(mod((p) => (p.slides[1].bg = 'assets/x.png')), 'bg kun på første slide'));
});

test('length limits give one error each', () => {
  const e = mod((p) => {
    p.slides[1].title = 'a'.repeat(61);
    p.slides[1].body = 'b'.repeat(161);
    p.slides[1].tag = 'C'.repeat(25);
  });
  assert.equal(e.filter((x) => x.includes('title')).length, 1, e.join('|'));
  assert.equal(e.filter((x) => x.includes('body')).length, 1);
  assert.equal(e.filter((x) => x.includes('tag')).length, 1);
});

test('unknown fact id is reported', () => {
  const e = mod((p) => (p.slides[1].value = '{bolius.findes.ikke}'));
  assert.ok(has(e, 'Ukendt fakta-id: bolius.findes.ikke'), e.join('|'));
});

test('short requires audio', () => {
  const sh = clone(valid.posts[1]);
  delete sh.audio;
  assert.ok(has(validatePost(sh, s), 'audio'));
});

test('brief-bad.json: every post has at least one error', () => {
  assert.ok(bad.posts.length >= 5);
  for (const p of bad.posts) assert.ok(validatePost(p, s).length > 0, p.id);
});

test('resolvePost resolves text, kpi values without unit, and collects sources', () => {
  const r = resolvePost(valid.posts[0], s);
  assert.equal(r.slides[0].value, '32.388 kr.');
  assert.equal(r.slides[0].body, 'om året for varme i et 130 m² hus.');
  assert.equal(r.slides[2].kpis[0].value, '32.388');
  assert.equal(r.slides[2].kpis[0].unit, 'kr./år');
  assert.deepEqual(r.slides[0].sources, ['Bolius: pris på opvarmningsformer']);
  assert.deepEqual(r.slides[3].sources, []);
  assert.deepEqual(r.sources, ['Bolius: pris på opvarmningsformer']);
  assert.ok(r.caption.includes('32.388 kr.'));
  assert.equal(valid.posts[0].slides[0].value, '{bolius.oliefyr}', 'input not mutated');
});
