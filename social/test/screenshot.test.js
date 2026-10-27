import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import net from 'node:net';
import os from 'node:os';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { REPO_ROOT } from '../lib/paths.js';
import { shootPage, screenFile } from '../render/screenshot.js';

let server;
let emptyServer;
let BASE;
let EMPTY_BASE;

const freePort = () =>
  new Promise((resolve, reject) => {
    const s = net.createServer();
    s.on('error', reject);
    s.listen(0, '127.0.0.1', () => {
      const { port } = s.address();
      s.close(() => resolve(port));
    });
  });

const canConnect = (port) =>
  new Promise((resolve) => {
    const s = net.connect(port, '127.0.0.1');
    s.on('connect', () => (s.destroy(), resolve(true)));
    s.on('error', () => resolve(false));
  });

async function serve(dir) {
  const port = await freePort();
  const proc = spawn('python3', ['-m', 'http.server', String(port), '--bind', '127.0.0.1'], { cwd: dir, stdio: 'ignore' });
  for (let i = 0; i < 50 && !(await canConnect(port)); i++) await new Promise((r) => setTimeout(r, 100));
  return { proc, base: `http://127.0.0.1:${port}` };
}

const stop = (proc) =>
  new Promise((resolve) => {
    if (!proc || proc.exitCode !== null) return resolve();
    proc.once('exit', resolve);
    proc.kill();
  });

before(async () => {
  ({ proc: server, base: BASE } = await serve(path.join(REPO_ROOT, 'site')));
  // Tom mappe: alle sider giver 404 (som en by, der ikke er udrullet endnu).
  ({ proc: emptyServer, base: EMPTY_BASE } = await serve(fs.mkdtempSync(path.join(os.tmpdir(), 'empty-site-'))));
});

after(async () => {
  await Promise.all([stop(server), stop(emptyServer)]);
});

const pngSize = (file) => {
  const b = fs.readFileSync(file);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
};

test('screenFile erstatter : med - og tilføjer .png', () => {
  assert.equal(screenFile('by:aalborg:solceller'), 'by-aalborg-solceller.png');
  assert.equal(screenFile('beregner'), 'beregner.png');
});

test('shootPage: beregner giver 1170x2532 PNG', async () => {
  const out = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'shot-')), 'b.png');
  assert.equal(await shootPage('beregner', out, BASE), out);
  assert.deepEqual(pngSize(out), { w: 1170, h: 2532 });
});

test('shootPage: bysider findes ud fra site/', async () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'shot-'));
  const out = path.join(dir, 'c.png');
  await shootPage('by:aalborg:solceller', out, BASE);
  assert.deepEqual(pngSize(out), { w: 1170, h: 2532 });
  await assert.rejects(shootPage('by:findesikke:solceller', out, BASE), /Ukendt side/);
  await assert.rejects(shootPage('by:aalborg:tag', out, BASE), /Ukendt side/);
});

test('shootPage: ukendt nøgle afvises', async () => {
  await assert.rejects(shootPage('nope', '/tmp/x.png', BASE), /Ukendt side/);
});

test('shootPage: 404 på live-siden afvises og skærmbilledet gemmes ikke', async () => {
  const out = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'shot-')), 'x.png');
  await assert.rejects(shootPage('by:aalborg:solceller', out, EMPTY_BASE), /Ukendt side: by:aalborg:solceller \(HTTP 404\)/);
  assert.equal(fs.existsSync(out), false);
});

// Finding 4: ingen salgstekst i skærmbilledet (det synlige udsnit af siden).
const SALES = /gratis|tilbud|book nu|begrænset|skynd dig|garanti|kun i dag|spar op til/i;
for (const key of ['by:aalborg:solceller', 'by:viborg:varmepumpe', 'by:naestved:solceller', 'beregner', 'elpris']) {
  test(`shootPage ${key}: no sales text or lead form in the captured viewport`, async () => {
    const out = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'shot-')), 's.png');
    const seen = {};
    assert.equal(await shootPage(key, out, BASE, seen), out);
    assert.ok(seen.text.length > 50, seen.text);
    assert.doesNotMatch(seen.text, SALES, seen.text);
    assert.equal(seen.formVisible, false);
  });
}
