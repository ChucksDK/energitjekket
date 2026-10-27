import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import http from 'node:http';
import os from 'node:os';
import path from 'node:path';
import { execFile, execFileSync } from 'node:child_process';
import { promisify } from 'node:util';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';
import { FIXTURE_ELPRIS } from './helpers.js';
import { startServer } from '../bin/preview-server.js';

const run = promisify(execFile);
const BUILD = path.join(SOCIAL_ROOT, 'bin', 'build-week.js');
const WEEK = '2026-W45';
const AM = '2026-11-02-am';
const PM = '2026-11-02-pm';
const BAD = '2026-11-03-am';
let tmp;
let site;
let base;
let sourcesFile;
let outRoot;
let weekDir;
let result;

const fixture = JSON.parse(fs.readFileSync(path.join(SOCIAL_ROOT, 'test', 'fixtures', 'brief-valid.json'), 'utf8'));

function carousel() {
  const p = structuredClone(fixture.posts[0]);
  p.slides[3] = { layout: 'screenshot', tag: 'BEREGNER', title: 'Sådan ser beregneren ud', screenshot: 'beregner' };
  return p;
}
function badPost() {
  const p = structuredClone(fixture.posts[0]);
  p.id = BAD;
  p.slot = '2026-11-03T07:30';
  p.slides[1].value = '{pv.nowhere.syd}';
  return p;
}
function short() {
  const p = structuredClone(fixture.posts[1]);
  p.audio = 'silent.m4a';
  return p;
}
const writeBrief = (name, posts) => {
  const f = path.join(tmp, name);
  fs.writeFileSync(f, JSON.stringify({ week: WEEK, posts }));
  return f;
};
const args = (brief, extra = []) => [
  BUILD, brief, '--base', base, '--sources', sourcesFile, '--elpris', FIXTURE_ELPRIS,
  '--audio-dir', path.join(tmp, 'audio'), '--out-root', outRoot, ...extra,
];
const readJson = (f) => JSON.parse(fs.readFileSync(path.join(weekDir, f), 'utf8'));
const buildId = () => readJson('build.json').buildId;
const post = (port, body) =>
  fetch(`http://127.0.0.1:${port}/approve`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ buildId: buildId(), ...body }),
  });

function seedAssets() {
  fs.mkdirSync(path.join(weekDir, 'assets'), { recursive: true });
  fs.copyFileSync(path.join(REPO_ROOT, 'site', 'og', 'beregner.png'), path.join(weekDir, 'assets', 'cover.png'));
}

before(async () => {
  tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'build-week-'));
  sourcesFile = path.join(tmp, 'sources.json');
  outRoot = path.join(tmp, 'out');
  weekDir = path.join(outRoot, WEEK);
  seedAssets();
  fs.mkdirSync(path.join(tmp, 'audio'));
  execFileSync('ffmpeg', ['-v', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-t', '25', '-y', path.join(tmp, 'audio', 'silent.m4a')]);
  // Lokal "energitjekket.dk" til screenshots.
  site = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end('<!doctype html><body style="margin:0;background:#0f6b55"><h1 style="color:#fff;font:700 40px sans-serif;padding:60px 20px">Beregner</h1>');
  });
  await new Promise((r) => site.listen(0, '127.0.0.1', r));
  base = `http://127.0.0.1:${site.address().port}`;
  const brief = writeBrief('brief.json', [short(), badPost(), carousel()]);
  result = await run('node', args(brief), { cwd: REPO_ROOT, maxBuffer: 1 << 24 });
});
after(() => {
  site?.close();
  fs.rmSync(tmp, { recursive: true, force: true });
});

test('build-week continues past an invalid post', () => {
  // exit 0 (run() ville ellers have kastet); det gyldige opslag er bygget
  const files = readJson('manifest.json').find((p) => p.id === AM).files;
  assert.equal(files.length, 5);
  for (const f of files) assert.ok(fs.statSync(path.join(weekDir, f)).size > 1000, f);
  assert.ok(fs.existsSync(path.join(weekDir, 'screens', 'beregner.png')));
  const errors = readJson('errors.json');
  assert.equal(errors.length, 1);
  assert.equal(errors[0].id, BAD);
  assert.ok(errors[0].errors.some((e) => e.includes('Ukendt fakta-id')), errors[0].errors.join('|'));
  assert.deepEqual(readJson('schedule.json'), []);
  assert.ok(!fs.existsSync(path.join(weekDir, BAD)));
});

test('caption.txt has caption, source line and hashtags', () => {
  const txt = fs.readFileSync(path.join(weekDir, AM, 'caption.txt'), 'utf8');
  assert.match(txt, /^Oliefyr er dyrt at have i et standardhus på 130 m²: ca\. 32\.388 kr\. om året\./);
  assert.match(txt, /\n\nKilde: Bolius[^\n]*\n\n#varmepumpe #oliefyr #viborg\n$/);
  assert.ok(!txt.includes('{'));
});

test('short is rendered as an MP4 and posts are listed in slot order', () => {
  const m = readJson('manifest.json');
  assert.deepEqual(m.map((p) => p.id), [AM, PM]);
  const mp4 = path.join(weekDir, m[1].files[0]);
  assert.match(mp4, /\.mp4$/);
  assert.ok(fs.statSync(mp4).size > 10000);
});

test('preview.html shows posts, errors and buttons in Danish', () => {
  const html = fs.readFileSync(path.join(weekDir, 'preview.html'), 'utf8');
  assert.ok(html.indexOf(AM) < html.indexOf(PM));
  assert.match(html, /mandag 2\. november 2026 kl\. 07:30/);
  assert.match(html, /<video controls/);
  assert.match(html, /Godkend/);
  assert.match(html, /Afvis/);
  assert.match(html, /Ukendt fakta-id: pv\.nowhere\.syd/);
  assert.match(html, /Preview-serveren kører ikke/);
});

test('preview-server approves, rejects and regenerates schedule.json', async () => {
  const server = await startServer(weekDir, { port: 0, requireApproval: true });
  const { port } = server.address();
  try {
    const ok = await post(port, { id: AM, approved: true });
    assert.equal(ok.status, 200);
    const sched = readJson('schedule.json');
    assert.equal(sched.length, 1);
    assert.equal(sched[0].id, AM);
    assert.equal(sched[0].slot, '2026-11-02T07:30:00+01:00');
    assert.equal(sched[0].type, 'carousel');
    assert.equal(sched[0].files.length, 5);
    assert.ok(sched[0].files.every((f) => path.isAbsolute(f) && fs.existsSync(f)));
    assert.equal(sched[0].caption, fs.readFileSync(path.join(weekDir, AM, 'caption.txt'), 'utf8'));
    assert.deepEqual(readJson('approvals.json'), { [AM]: true });

    assert.equal((await post(port, { id: PM, approved: true })).status, 200);
    assert.deepEqual(readJson('schedule.json').map((s) => s.id), [AM, PM]);
    assert.equal((await post(port, { id: AM, approved: false })).status, 200);
    assert.deepEqual(readJson('schedule.json').map((s) => s.id), [PM]);

    // Afviste/ukendte/ugyldige anmodninger
    assert.equal((await post(port, { id: BAD, approved: true })).status, 404);
    assert.equal((await post(port, { id: '../x', approved: true })).status, 404);
    assert.equal((await post(port, { id: AM, approved: 'ja' })).status, 400);
    const wrongType = await fetch(`http://127.0.0.1:${port}/approve`, { method: 'POST', headers: { 'Content-Type': 'text/plain' }, body: '{}' });
    assert.equal(wrongType.status, 415);
    const foreign = await fetch(`http://127.0.0.1:${port}/approve`, {
      method: 'POST', headers: { 'Content-Type': 'application/json', Origin: 'http://evil.example' }, body: JSON.stringify({ buildId: buildId(), id: AM, approved: true }),
    });
    assert.equal(foreign.status, 403);
    assert.equal((await fetch(`http://127.0.0.1:${port}/approve`)).status, 405);
    assert.deepEqual(readJson('approvals.json'), { [AM]: false, [PM]: true });
  } finally {
    server.close();
  }
});

test('preview-server serves the week dir without path traversal', async () => {
  fs.writeFileSync(path.join(outRoot, 'secret.txt'), 'hemmelig');
  const server = await startServer(weekDir, { port: 0 });
  const { port } = server.address();
  const get = (p) =>
    new Promise((resolve) => {
      // http.get rører ikke ved stien, så %2e%2e og rå ../ når serveren uændret.
      http.get({ host: '127.0.0.1', port, path: p }, (res) => {
        let b = '';
        res.on('data', (c) => (b += c));
        res.on('end', () => resolve({ status: res.statusCode, body: b }));
      });
    });
  try {
    assert.equal((await get('/')).status, 200);
    assert.match((await get('/preview.html')).body, /Ugens opslag/);
    assert.equal((await get(`/${AM}/${AM}-01.png`)).status, 200);
    for (const p of ['/../secret.txt', '/%2e%2e/secret.txt', '/..%2fsecret.txt', `/${AM}/../../secret.txt`, '/%00']) {
      const r = await get(p);
      assert.notEqual(r.status, 200, p);
      assert.ok(!r.body.includes('hemmelig'), p);
    }
    const ranged = await new Promise((resolve) =>
      http.get({ host: '127.0.0.1', port, path: '/preview.html', headers: { Range: 'bytes=0-9' } }, (res) => {
        res.resume();
        resolve(res.statusCode);
      }),
    );
    assert.equal(ranged, 206);
  } finally {
    server.close();
  }
});

test('rebuild invalidates approvals (require_approval:true)', async () => {
  const cfg = path.join(tmp, 'config-closed.json');
  fs.writeFileSync(cfg, JSON.stringify({ require_approval: true }));
  const brief = writeBrief('brief-rebuild.json', [carousel()]);
  await run('node', args(brief, ['--config', cfg]), { cwd: REPO_ROOT, maxBuffer: 1 << 24 });
  const oldId = buildId();
  const server = await startServer(weekDir, { port: 0, configFile: cfg });
  const { port } = server.address();
  try {
    assert.equal((await post(port, { id: AM, approved: true })).status, 200);
    assert.deepEqual(readJson('schedule.json').map((s) => s.id), [AM]);
    assert.ok(fs.existsSync(path.join(weekDir, 'approvals.json')));

    await run('node', args(brief, ['--config', cfg]), { cwd: REPO_ROOT, maxBuffer: 1 << 24 });
    assert.deepEqual(readJson('schedule.json'), []);
    assert.ok(!fs.existsSync(path.join(weekDir, 'approvals.json')));
    assert.notEqual(buildId(), oldId);

    // En gammel fane (gammelt build-id) kan ikke godkende genbygget indhold.
    const stale = await post(port, { id: AM, approved: true, buildId: oldId });
    assert.equal(stale.status, 409);
    assert.deepEqual(readJson('schedule.json'), []);
    assert.ok(!fs.existsSync(path.join(weekDir, 'approvals.json')));
    assert.equal((await post(port, { id: AM, approved: true })).status, 200);

    // Fejl ved beregning af planen: 500 og intet ændres.
    assert.equal((await post(port, { id: AM, approved: false })).status, 200);
    const approvalsBefore = fs.readFileSync(path.join(weekDir, 'approvals.json'), 'utf8');
    const scheduleBefore = fs.readFileSync(path.join(weekDir, 'schedule.json'), 'utf8');
    const cap = path.join(weekDir, AM, 'caption.txt');
    const saved = fs.readFileSync(cap);
    fs.rmSync(cap);
    try {
      assert.equal((await post(port, { id: AM, approved: true })).status, 500);
    } finally {
      fs.writeFileSync(cap, saved);
    }
    assert.equal(fs.readFileSync(path.join(weekDir, 'approvals.json'), 'utf8'), approvalsBefore);
    assert.equal(fs.readFileSync(path.join(weekDir, 'schedule.json'), 'utf8'), scheduleBefore);
  } finally {
    server.close();
  }
});

test('require_approval:false writes every built post into schedule.json', async () => {
  const cfg = path.join(tmp, 'config-open.json');
  fs.writeFileSync(cfg, JSON.stringify({ require_approval: false }));
  const brief = writeBrief('brief-open.json', [badPost(), carousel()]);
  await run('node', args(brief, ['--config', cfg]), { cwd: REPO_ROOT, maxBuffer: 1 << 24 });
  const sched = readJson('schedule.json');
  assert.deepEqual(sched.map((s) => s.id), [AM]);
  assert.equal(sched[0].files.length, 5);
  assert.ok(!fs.existsSync(path.join(weekDir, 'approvals.json')));
  const html = fs.readFileSync(path.join(weekDir, 'preview.html'), 'utf8');
  assert.match(html, /Godkendelse er slået fra/);
  assert.match(html, /data-approve="true" disabled/);
  // Serveren læser konfigurationen pr. anmodning og afviser godkendelser.
  const server = await startServer(weekDir, { port: 0, configFile: cfg });
  try {
    assert.equal((await post(server.address().port, { id: AM, approved: true })).status, 409);
  } finally {
    server.close();
  }
  assert.deepEqual(readJson('schedule.json').map((s) => s.id), [AM]);
  // Gamle godkendelser og det gamle short-opslag er væk efter ombygning.
  assert.ok(!readJson('manifest.json').some((p) => p.id === PM));
});

test('build-week exits 1 when no post could be built', async () => {
  const brief = writeBrief('brief-none.json', [badPost()]);
  await assert.rejects(run('node', args(brief), { cwd: REPO_ROOT }), (e) => e.code === 1);
  assert.deepEqual(readJson('schedule.json'), []);
  assert.equal(readJson('errors.json')[0].id, BAD);
});

test('week-level errors are reported per post and the rest is skipped (finding 14)', async () => {
  const friday = { ...short(), id: '2026-11-06-pm', slot: '2026-11-06T19:30' };
  const dupA = { ...carousel(), id: '2026-11-04-am', slot: '2026-11-04T07:30' };
  const dupB = { ...carousel(), id: '2026-11-04-am2', slot: '2026-11-04T07:30' };
  const wrongTime = { ...carousel(), id: '2026-11-05-pm', slot: '2026-11-05T19:30' };
  const brief = writeBrief('brief-week.json', [friday, dupA, dupB, wrongTime]);
  await assert.rejects(run('node', args(brief), { cwd: REPO_ROOT, maxBuffer: 1 << 24 }), (e) => e.code === 1);
  const errors = Object.fromEntries(readJson('errors.json').map((e) => [e.id, e.errors.join(' | ')]));
  assert.match(errors['2026-11-06-pm'], /fredag kl\. 19:30 er reserveret/);
  assert.match(errors['2026-11-04-am'], /brugt af flere opslag/);
  assert.match(errors['2026-11-04-am2'], /brugt af flere opslag/);
  assert.match(errors['2026-11-05-pm'], /carousel skal ligge kl\. 07:30/);
  assert.deepEqual(readJson('manifest.json'), []);
});

test('/approve answers 500 JSON on malformed build.json, config or manifest and the server stays up (finding 13)', async () => {
  const brief = writeBrief('brief-500.json', [carousel()]);
  await run('node', args(brief), { cwd: REPO_ROOT, maxBuffer: 1 << 24 });
  const cfg = path.join(tmp, 'config-500.json');
  fs.writeFileSync(cfg, JSON.stringify({ require_approval: true }));
  const server = await startServer(weekDir, { port: 0, configFile: cfg });
  const { port } = server.address();
  const id = buildId();
  const approve = () =>
    fetch(`http://127.0.0.1:${port}/approve`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ buildId: id, id: AM, approved: true }) });
  const broken = async (file, restore) => {
    const saved = fs.readFileSync(file);
    fs.writeFileSync(file, '{ikke json');
    try {
      const r = await approve();
      assert.equal(r.status, 500, file);
      assert.match(r.headers.get('content-type'), /application\/json/);
      const body = await r.json();
      assert.equal(body.ok, false);
      assert.ok(body.error.length > 0);
      assert.equal((await fetch(`http://127.0.0.1:${port}/preview.html`)).status, 200, 'serveren kører videre');
    } finally {
      fs.writeFileSync(file, restore ?? saved);
    }
  };
  try {
    await broken(path.join(weekDir, 'build.json'));
    await broken(cfg);
    await broken(path.join(weekDir, 'manifest.json'));
    assert.equal((await approve()).status, 200);
  } finally {
    server.close();
  }
});

test('bg images next to the brief are copied into the week dir (finding 17)', async () => {
  const p = carousel();
  p.slides[0].bg = 'assets/brief-own/cover-b.png';
  fs.mkdirSync(path.join(tmp, 'assets', 'brief-own'), { recursive: true });
  fs.copyFileSync(path.join(REPO_ROOT, 'site', 'og', 'beregner.png'), path.join(tmp, 'assets', 'brief-own', 'cover-b.png'));
  const brief = writeBrief('brief-assets.json', [p]);
  await run('node', args(brief), { cwd: REPO_ROOT, maxBuffer: 1 << 24 });
  assert.deepEqual(readJson('errors.json'), []);
  assert.ok(fs.existsSync(path.join(weekDir, 'assets', 'brief-own', 'cover-b.png')));
  // En sti ud af mappen afvises.
  const bad = carousel();
  bad.slides[0].bg = '../../outside.png';
  await assert.rejects(run('node', args(writeBrief('brief-assets-bad.json', [bad])), { cwd: REPO_ROOT, maxBuffer: 1 << 24 }), (e) => e.code === 1);
  assert.match(readJson('errors.json')[0].errors.join('|'), /bg skal være en relativ sti/);
});
