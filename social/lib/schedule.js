// Fælles logik for ugemappen: atomisk JSON-skrivning, godkendelser og schedule.json.
import fs from 'node:fs';
import path from 'node:path';
import { SOCIAL_ROOT } from './paths.js';

export const CONFIG_FILE = path.join(SOCIAL_ROOT, 'config.json');

export function writeJsonAtomic(file, data) {
  const tmp = `${file}.${process.pid}.${Date.now()}.tmp`;
  fs.writeFileSync(tmp, `${JSON.stringify(data, null, 2)}\n`);
  fs.renameSync(tmp, file);
}

export function readJson(file, fallback) {
  if (!fs.existsSync(file)) return fallback;
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

export function loadConfig(file = CONFIG_FILE) {
  const c = readJson(file, {});
  return { require_approval: c.require_approval !== false };
}

/** manifest.json: byggede opslag i slot-rækkefølge, filer relative til ugemappen. */
export function readManifest(weekDir) {
  return readJson(path.join(weekDir, 'manifest.json'), []);
}

/** Skriver schedule.json: kun godkendte opslag (eller alle, hvis require_approval er false). */
export function writeSchedule(weekDir, { requireApproval = true } = {}) {
  const approvals = readJson(path.join(weekDir, 'approvals.json'), {});
  const schedule = readManifest(weekDir)
    .filter((p) => !requireApproval || approvals[p.id] === true)
    .map((p) => ({
      id: p.id,
      slot: p.slot,
      type: p.type,
      files: p.files.map((f) => path.resolve(weekDir, f)),
      caption: fs.readFileSync(path.join(weekDir, p.id, 'caption.txt'), 'utf8'),
    }));
  writeJsonAtomic(path.join(weekDir, 'schedule.json'), schedule);
  return schedule;
}
