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

test('brief-bad.json: each post yields its specific error', () => {
  const expected = {
    'bad-digits': 'tal uden kilde: "30.000"',
    'bad-banned': 'forbudt: "book nu"',
    'bad-quote': 'tilbud',
    'bad-url': 'target_url skal starte med',
    'bad-count': 'carousel skal have 5-7 slides',
    'bad-bg': 'bg kun på første slide',
    'bad-lengths': 'for langt',
    'bad-fact': 'Ukendt fakta-id: bolius.findes.ikke',
    'bad-short-count': 'short skal have 3-6 slides',
  };
  assert.deepEqual(bad.posts.map((p) => p.id).sort(), Object.keys(expected).sort());
  for (const p of bad.posts) assert.ok(has(validatePost(p, s), expected[p.id]), p.id);
});

test('digits in highlight and kpi label/value/unit', () => {
  assert.ok(has(mod((p) => (p.slides[1].highlight = 'ca. 500')), 'highlight: tal uden kilde: "500"'));
  assert.ok(has(mod((p) => (p.slides[2].kpis[0].label = 'Over 40')), 'kpis[0].label: tal uden kilde'));
  assert.ok(has(mod((p) => (p.slides[2].kpis[0].value = '123')), 'kpis[0].value: tal uden kilde'));
  assert.ok(has(mod((p) => (p.slides[2].kpis[0].unit = 'kr./9')), 'kpis[0].unit: tal uden kilde'));
});

test('non-string text fields are errors', () => {
  assert.ok(has(mod((p) => (p.slides[0].value = 32388)), 'value: skal være tekst'));
  assert.ok(has(mod((p) => (p.slides[1].title = 30000)), 'title: skal være tekst'));
  assert.ok(has(mod((p) => (p.slides[2].kpis[0].value = 5)), 'kpis[0].value: skal være tekst'));
  assert.ok(has(mod((p) => (p.slides[2].kpis[0].unit = 5)), 'kpis[0].unit: skal være tekst'));
  assert.ok(has(mod((p) => (p.caption = 7)), 'caption: skal være tekst'));
  assert.ok(has(mod((p) => (p.hashtags = [1])), 'hashtag 1: skal være tekst'));
});

test('unicode digits and lookalikes', () => {
  assert.ok(has(mod((p) => (p.caption = 'Spar ３０ kr')), 'tal uden kilde'));
  assert.ok(has(mod((p) => (p.caption = 'Spar ٣٠ kr')), 'tal uden kilde'));
  assert.ok(has(mod((p) => (p.caption = 'Halv ½ pris')), 'tal uden kilde'));
  assert.ok(has(mod((p) => (p.caption = 'Se nu！')), 'forbudt: "!"'));
  assert.ok(has(mod((p) => (p.caption = 'gra\u00adtis')), 'forbudt: "gratis"'));
  assert.ok(has(mod((p) => (p.caption = 'gra\u200btis')), 'forbudt: "gratis"'));
});

test('placeholders are not allowed in hashtags or kpi unit', () => {
  assert.ok(has(mod((p) => (p.hashtags = ['#{nope.x}'])), 'hashtag 1'));
  assert.ok(has(mod((p) => (p.hashtags = ['#{bolius.oliefyr}'])), 'pladsholdere'));
  assert.ok(has(mod((p) => (p.slides[2].kpis[0].unit = '{bolius.oliefyr}')), 'kpis[0].unit: pladsholdere'));
});

test('malformed posts return errors instead of throwing', () => {
  for (const fn of [
    (p) => (p.slides[1] = null),
    (p) => (p.slides[2].kpis = 'x'),
    (p) => (p.slides[2].kpis = [null]),
    (p) => (p.hashtags = 'x'),
    (p) => (p.slides = 'x'),
    (p) => delete p.slides,
  ]) {
    const e = mod(fn);
    assert.ok(e.length > 0);
  }
  assert.ok(validatePost(null, s).length > 0);
});

test('tilbud path detection: encoded and prefix', () => {
  assert.ok(has(mod((p) => (p.target_url = 'https://energitjekket.dk/%74ilbud/')), 'tilbud'));
  assert.ok(has(mod((p) => (p.target_url = 'https://energitjekket.dk/tilbud')), 'tilbud'));
  assert.ok(!has(mod((p) => (p.target_url = 'https://energitjekket.dk/beregner/?ref=tilbud')), 'target_url peger'));
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

test('length limits are measured on resolved text (R6)', () => {
  const id = 'elpris.2026-10-27.DK1.billigste_time';
  // Rå titel > 60 tegn pga. pladsholderen, men opløst er den kort.
  const ok = mod((p) => {
    p.slides[1].title = `Billigste time i morgen er kl. {${id}}`;
  });
  assert.equal(has(ok, 'for langt'), false, ok.join('\n'));
  // Opløst tekst > 60 tegn fejler stadig.
  const bad = mod((p) => {
    p.slides[1].title = `Billigst kl. {${id}} ${'x'.repeat(60)}`;
  });
  assert.ok(has(bad, 'slide 2 title: for langt'), bad.join('\n'));
  // Ukendt id: rå tekst måles, og ukendt-fejlen rapporteres.
  const unk = mod((p) => {
    p.slides[1].title = `{elpris.2026-10-27.DK1.nowhere_${'y'.repeat(50)}}`;
  });
  assert.ok(has(unk, 'Ukendt fakta-id'));
  assert.ok(has(unk, 'for langt'));
});

test('bars slide gets the elpris source on the slide and in the post (finding 1)', () => {
  const p = clone(valid.posts[0]);
  p.slides[3] = { layout: 'bars', tag: 'ELPRIS', title: 'Spotpris time for time', bars: { date: '2026-10-27', area: 'DK1' } };
  const r = resolvePost(p, s);
  const name = s.facts['elpris.2026-10-27.DK1.billigste_pris'].source.name;
  assert.match(name, /spotpris/);
  assert.deepEqual(r.slides[3].sources, [name]);
  assert.ok(r.sources.includes(name));
});

test('bars slide must point at a date and area that exist in sources.elpris (finding 5)', () => {
  const withBars = (bars) => mod((p) => (p.slides[3] = { layout: 'bars', tag: 'ELPRIS', title: 'Spotpris time for time', bars }));
  assert.deepEqual(withBars({ date: '2026-10-27', area: 'DK1' }), []);
  assert.ok(has(withBars({ date: '2026-10-20', area: 'DK1' }), 'slide 4: ingen elpriser for 2026-10-20 DK1'), withBars({ date: '2026-10-20', area: 'DK1' }).join('|'));
  assert.ok(has(withBars({ date: '2026-10-27', area: 'DK3' }), 'ingen elpriser for 2026-10-27 DK3'));
  assert.ok(has(withBars(undefined), 'slide 4: bars mangler'));
});
