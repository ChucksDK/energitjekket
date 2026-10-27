import { test } from 'node:test';
import assert from 'node:assert/strict';
import { formatFact } from '../lib/format.js';

test('formats Danish numbers and units', () => {
  assert.equal(formatFact(32388, 'kr'), '32.388 kr.');
  assert.equal(formatFact(0.2418, 'kr_per_kwh'), '0,24 kr.');
  assert.equal(formatFact(986, 'kwh_per_kwp'), '986 kWh');
  assert.equal(formatFact(48.4, 'pct'), '48 %');
  assert.equal(formatFact(6, 'hour'), 'kl. 06');
  assert.equal(formatFact(130, 'm2'), '130 m²');
  assert.equal(formatFact(3.5, 'scop'), '3,5');
  assert.equal(formatFact(18100, 'kwh'), '18.100 kWh');
});

test('formatFact handles negative kr_per_kwh', () => {
  assert.equal(formatFact(-0.05, 'kr_per_kwh'), '-0,05 kr.');
  assert.equal(formatFact(0, 'kr_per_kwh'), '0,00 kr.');
});

test('formats kwp and count units', () => {
  assert.equal(formatFact(10.5, 'kwp'), '11 kWp');
  assert.equal(formatFact(1000, 'count'), '1.000');
});

test('throws on unknown unit', () => {
  assert.throws(() => formatFact(1, 'furlong'), /unknown unit/i);
});
