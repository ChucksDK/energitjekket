import { test, before } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { loadSources, getFact } from '../lib/sources.js';
import { SOCIAL_ROOT } from '../lib/paths.js';
import { ensureSources } from './helpers.js';

let file;
let s;
before(() => {
  file = ensureSources();
  s = loadSources(file);
});

test('getFact returns bolius.oliefyr', () => {
  assert.equal(getFact(s, 'bolius.oliefyr').value, 32388);
});

test('getFact throws on unknown id', () => {
  assert.throws(() => getFact(s, 'nope'), /Ukendt fakta-id: nope/);
});

test('facts.js bolius lists formatted values', () => {
  const out = execFileSync('node', [path.join(SOCIAL_ROOT, 'bin', 'facts.js'), '--sources', file, 'bolius'], { encoding: 'utf8' });
  assert.match(out, /bolius\.oliefyr\t32\.388 kr\./);
});

test('fixture elpris day is present', () => {
  assert.equal(getFact(s, 'elpris.2026-10-27.DK1.billigste_time').value, 6);
  assert.equal(s.elpris['2026-10-27'].DK1.hours.length, 24);
});
