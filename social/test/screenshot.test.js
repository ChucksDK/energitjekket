import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import net from 'node:net';
import os from 'node:os';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { REPO_ROOT } from '../lib/paths.js';
import { shootPage, screenFile } from '../render/screenshot.js';

const PORT = 8765;
const BASE = `http://localhost:${PORT}`;
let server;

const canConnect = () =>
  new Promise((resolve) => {
    const s = net.connect(PORT, '127.0.0.1');
    s.on('connect', () => (s.destroy(), resolve(true)));
    s.on('error', () => resolve(false));
  });

before(async () => {
  server = spawn('python3', ['-m', 'http.server', String(PORT), '--bind', '127.0.0.1'], {
    cwd: path.join(REPO_ROOT, 'site'),
    stdio: 'ignore',
  });
  for (let i = 0; i < 50 && !(await canConnect()); i++) await new Promise((r) => setTimeout(r, 100));
});

after(() => server?.kill());

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
