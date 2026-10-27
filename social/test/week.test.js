import { test } from 'node:test';
import assert from 'node:assert/strict';
import { weekErrors } from '../lib/week.js';
import { slotWithOffset } from '../lib/schedule.js';

const p = (id, slot, type) => ({ id, slot, type });

test('weekErrors: a valid week has no errors', () => {
  const errs = weekErrors([p('2026-11-02-am', '2026-11-02T07:30', 'carousel'), p('2026-11-02-pm', '2026-11-02T19:30', 'short'), p('2026-11-06-am', '2026-11-06T07:30', 'carousel')]);
  assert.deepEqual(errs, [[], [], []]);
});

test('weekErrors: duplicate slot is an error for both posts (finding 14)', () => {
  const errs = weekErrors([p('2026-11-02-am', '2026-11-02T07:30', 'carousel'), p('2026-11-02-am2', '2026-11-02T07:30', 'carousel'), p('2026-11-03-am', '2026-11-03T07:30', 'carousel')]);
  assert.ok(errs[0].some((e) => /slot 2026-11-02T07:30 er brugt af flere opslag: 2026-11-02-am, 2026-11-02-am2/.test(e)), errs[0].join('|'));
  assert.ok(errs[1].some((e) => /brugt af flere opslag/.test(e)));
  assert.deepEqual(errs[2], []);
});

test('weekErrors: id date must match slot date', () => {
  const [e] = weekErrors([p('2026-11-03-am', '2026-11-02T07:30', 'carousel')]);
  assert.ok(e.some((x) => /id 2026-11-03-am passer ikke til slot-datoen 2026-11-02/.test(x)), e.join('|'));
});

test('weekErrors: carousel at 07:30, short at 19:30', () => {
  const errs = weekErrors([p('2026-11-02-am', '2026-11-02T19:30', 'carousel'), p('2026-11-03-pm', '2026-11-03T07:30', 'short')]);
  assert.ok(errs[0].some((x) => /carousel skal ligge kl\. 07:30/.test(x)), errs[0].join('|'));
  assert.ok(errs[1].some((x) => /short skal ligge kl\. 19:30/.test(x)), errs[1].join('|'));
});

test('weekErrors: Friday 19:30 is reserved for the elpris reel (Ruling F1)', () => {
  const [e] = weekErrors([p('2026-11-06-pm', '2026-11-06T19:30', 'short')]);
  assert.ok(e.some((x) => /fredag kl\. 19:30 er reserveret til elpris-reelen/.test(x)), e.join('|'));
});

test('slotWithOffset gives the Europe/Copenhagen offset for the date (finding 15)', () => {
  assert.equal(slotWithOffset('2026-11-02T07:30'), '2026-11-02T07:30:00+01:00');
  assert.equal(slotWithOffset('2026-07-01T19:30'), '2026-07-01T19:30:00+02:00');
  assert.equal(slotWithOffset('2026-03-29T07:30'), '2026-03-29T07:30:00+02:00'); // sommertid fra 29/3 kl. 02
  assert.equal(slotWithOffset('2026-03-28T19:30'), '2026-03-28T19:30:00+01:00');
  assert.equal(slotWithOffset('2026-10-25T07:30'), '2026-10-25T07:30:00+01:00'); // vintertid fra 25/10 kl. 03
  assert.equal(slotWithOffset('2026-10-24T19:30'), '2026-10-24T19:30:00+02:00');
});
