import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';

export const FIXTURE_ELPRIS = path.join(SOCIAL_ROOT, 'test', 'fixtures', 'elpris_data.json');
export const TEST_SOURCES = path.join(SOCIAL_ROOT, 'out', 'test-sources.json');

// Bygger registeret med fixture-elpriser, så tests består på et rent checkout.
export function ensureSources() {
  {
    execFileSync(
      'python3',
      [path.join(REPO_ROOT, 'social', 'data', 'export_sources.py'), '--elpris', FIXTURE_ELPRIS, '--out', TEST_SOURCES],
      { stdio: 'pipe' },
    );
  }
  return TEST_SOURCES;
}
