import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';

test('paths resolve to the repo and social directories', () => {
  assert.equal(path.basename(SOCIAL_ROOT), 'social');
  assert.equal(path.join(REPO_ROOT, 'social'), SOCIAL_ROOT);
  assert.ok(fs.existsSync(path.join(REPO_ROOT, 'src')));
});
