import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { publishWeek } from '../bin/publish.js';
import { clashes } from '../bin/queue.js';
import { planSend, postBody, readBackProblems, readKey, toLocal } from '../lib/zernio.js';

const CFG = { username: 'energitjekket', accountId: 'acc1', timezone: 'Europe/Copenhagen', keyFile: '~/nope.env' };
const NOW = new Date('2026-11-01T12:00:00+01:00');

// En uge med ét carousel (2 billeder) og én short på disk.
function makeWeek() {
  const out = fs.mkdtempSync(path.join(os.tmpdir(), 'pub-'));
  const dir = path.join(out, '2026-W45');
  fs.mkdirSync(path.join(dir, 'a'), { recursive: true });
  for (const f of ['a/1.png', 'a/2.png', 'a/s.mp4']) fs.writeFileSync(path.join(dir, f), 'x');
  const schedule = [
    { id: '2026-11-02-am', slot: '2026-11-02T07:30:00+01:00', type: 'carousel', files: [path.join(dir, 'a/1.png'), path.join(dir, 'a/2.png')], caption: 'Hej\n\n#varmepumpe\n' },
    { id: '2026-11-02-pm', slot: '2026-11-02T19:30:00+01:00', type: 'short', files: [path.join(dir, 'a/s.mp4')], caption: 'Short\n' },
  ];
  fs.writeFileSync(path.join(dir, 'schedule.json'), JSON.stringify(schedule));
  fs.writeFileSync(path.join(dir, 'build.json'), JSON.stringify({ buildId: 'b1' }));
  return { out, dir, schedule };
}

// Falsk Zernio: husker oprettede opslag og svarer på GET som det rigtige API (UTC-tid).
function fakeZernio() {
  const posts = {};
  const calls = [];
  let n = 0;
  const res = (status, body) => ({ status, text: async () => JSON.stringify(body) });
  const fetchImpl = async (url, opts) => {
    calls.push({ url, method: opts.method, headers: opts.headers, body: opts.body && typeof opts.body === 'string' ? JSON.parse(opts.body) : null });
    if (url.startsWith('https://upload/')) return res(200, {});
    if (url.endsWith('/media/presign')) return res(200, { uploadUrl: `https://upload/${n}`, publicUrl: `https://cdn/${n++}` });
    if (url.endsWith('/posts') && opts.method === 'POST') {
      const b = JSON.parse(opts.body);
      const id = `z${Object.keys(posts).length + 1}`;
      const utc = new Date(`${b.scheduledFor}+01:00`).toISOString();
      posts[id] = { _id: id, status: 'scheduled', scheduledFor: utc, mediaItems: b.mediaItems, platforms: [{ accountId: { _id: b.platforms[0].accountId } }] };
      return res(201, { post: posts[id] });
    }
    const m = /\/posts\/(\w+)$/.exec(url);
    if (m) return res(200, { post: posts[m[1]] });
    return res(404, {});
  };
  return { fetchImpl, calls, posts };
}

test('planSend skips posts already sent, in the past, or missing files', () => {
  const { schedule } = makeWeek();
  const gone = { ...schedule[1], id: 'x', files: ['/nope.mp4'] };
  const plan = planSend([...schedule, gone], { '2026-11-02-am': { zernioId: 'z9' } }, new Date('2026-11-02T08:00:00+01:00'));
  assert.deepEqual(plan.map((p) => p.action), ['skip', 'send', 'skip']);
  assert.match(plan[0].reason, /allerede planlagt som Zernio-opslag z9/);
  assert.match(plan[2].reason, /filer mangler/);
  assert.match(planSend([schedule[0]], {}, new Date('2026-11-03T00:00:00Z'))[0].reason, /overstået/);
});

test('postBody: local time + timezone, reels shared to the feed, carousels not', () => {
  const { schedule } = makeWeek();
  const c = postBody(schedule[0], [{ type: 'image', url: 'u' }], CFG);
  assert.equal(c.scheduledFor, '2026-11-02T07:30:00');
  assert.equal(c.timezone, 'Europe/Copenhagen');
  assert.equal(c.content, 'Hej\n\n#varmepumpe');
  assert.deepEqual(c.platforms, [{ platform: 'instagram', accountId: 'acc1' }]);
  assert.deepEqual(postBody(schedule[1], [], CFG).platforms[0].platformSpecificData, { shareToFeed: true });
});

test('toLocal converts Zernio UTC back to Danish time across DST', () => {
  assert.equal(toLocal('2026-11-02T06:30:00.000Z', 'Europe/Copenhagen'), '2026-11-02T07:30');
  assert.equal(toLocal('2026-07-01T17:30:00.000Z', 'Europe/Copenhagen'), '2026-07-01T19:30');
});

test('readBackProblems catches wrong account, time, status and media count', () => {
  const post = { slot: '2026-11-02T07:30:00+01:00', files: ['a', 'b'] };
  const ok = { status: 'scheduled', scheduledFor: '2026-11-02T06:30:00Z', mediaItems: [{}, {}], platforms: [{ accountId: 'acc1' }] };
  assert.deepEqual(readBackProblems(ok, post, CFG), []);
  const bad = { status: 'failed', scheduledFor: '2026-11-02T07:30:00Z', mediaItems: [{}], platforms: [{ accountId: 'other' }] };
  assert.equal(readBackProblems(bad, post, CFG).length, 4);
});

test('readKey prefers the environment and never needs the file then', () => {
  assert.equal(readKey(CFG, { ZERNIO_API_KEY: 'k' }), 'k');
  assert.throws(() => readKey(CFG, {}), /ZERNIO_API_KEY mangler/);
});

test('publishWeek without --send sends nothing', async () => {
  const { out } = makeWeek();
  const z = fakeZernio();
  const r = await publishWeek('2026-W45', { outRoot: out, cfg: CFG, key: 'k', fetchImpl: z.fetchImpl, now: NOW, log: () => {} });
  assert.equal(z.calls.length, 0);
  assert.deepEqual(r.plan.map((p) => p.action), ['send', 'send']);
});

test('publishWeek --send uploads, posts, reads back, logs sent.json, and never sends twice', async () => {
  const { out, dir } = makeWeek();
  const z = fakeZernio();
  const opts = { send: true, outRoot: out, cfg: CFG, key: 'k', fetchImpl: z.fetchImpl, now: NOW, log: () => {} };
  const r = await publishWeek('2026-W45', opts);
  assert.deepEqual(r.sent.map((s) => [s.id, s.problems]), [['2026-11-02-am', []], ['2026-11-02-pm', []]]);
  assert.equal(z.calls.filter((c) => c.url.endsWith('/media/presign')).length, 3);
  const created = z.calls.filter((c) => c.url.endsWith('/posts') && c.method === 'POST');
  assert.equal(created[0].headers['Idempotency-Key'], 'energitjekket-ig-2026-W45-2026-11-02-am-b1');
  assert.deepEqual(created[0].body.mediaItems.map((m) => m.type), ['image', 'image']);
  assert.deepEqual(created[1].body.mediaItems.map((m) => m.type), ['video']);
  const sent = JSON.parse(fs.readFileSync(path.join(dir, 'sent.json'), 'utf8'));
  assert.equal(sent['2026-11-02-am'].zernioId, 'z1');

  const again = await publishWeek('2026-W45', opts);
  assert.deepEqual(again.sent, []);
  assert.ok(again.plan.every((p) => p.action === 'skip'));
});

test('publishWeek --only sends a single post', async () => {
  const { out } = makeWeek();
  const z = fakeZernio();
  const r = await publishWeek('2026-W45', { send: true, only: '2026-11-02-pm', outRoot: out, cfg: CFG, key: 'k', fetchImpl: z.fetchImpl, now: NOW, log: () => {} });
  assert.deepEqual(r.sent.map((s) => s.id), ['2026-11-02-pm']);
});

test('clashes finds two posts in the same local minute', () => {
  const posts = [{ _id: 'a', scheduledFor: '2026-11-02T06:30:00Z' }, { _id: 'b', scheduledFor: '2026-11-02T06:30:00Z' }, { _id: 'c', scheduledFor: '2026-11-02T18:30:00Z' }];
  assert.deepEqual(clashes(posts, 'Europe/Copenhagen'), ['2026-11-02T07:30']);
});
