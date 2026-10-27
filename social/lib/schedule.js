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

const pad = (n) => String(n).padStart(2, '0');

/**
 * "2026-11-02T07:30" -> "2026-11-02T07:30:00+01:00": lokal tid i Europe/Copenhagen med eksplicit offset
 * (+01:00 vintertid, +02:00 sommertid), så Zernio aldrig skal gætte tidszonen.
 */
export function slotWithOffset(slot) {
  const m = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})$/.exec(slot);
  if (!m) throw new Error(`Ugyldigt slot: ${slot}`);
  const [y, mo, d, h, mi] = m.slice(1).map(Number);
  const local = Date.UTC(y, mo - 1, d, h, mi);
  const fmt = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Europe/Copenhagen', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hourCycle: 'h23',
  });
  for (const off of [1, 2]) {
    const parts = Object.fromEntries(fmt.formatToParts(new Date(local - off * 3600000)).map((p) => [p.type, p.value]));
    if (`${parts.year}-${parts.month}-${parts.day}T${parts.hour}:${parts.minute}` === slot) return `${slot}:00+${pad(off)}:00`;
  }
  throw new Error(`Slot findes ikke i Europe/Copenhagen (sommertidsskift): ${slot}`);
}

/** Skriver schedule.json: kun godkendte opslag (eller alle, hvis require_approval er false). */
export function computeSchedule(weekDir, approvals, { requireApproval = true } = {}) {
  return readManifest(weekDir)
    .filter((p) => !requireApproval || approvals[p.id] === true)
    .map((p) => ({
      id: p.id,
      slot: slotWithOffset(p.slot),
      type: p.type,
      files: p.files.map((f) => path.resolve(weekDir, f)),
      caption: fs.readFileSync(path.join(weekDir, p.id, 'caption.txt'), 'utf8'),
    }));
}

export function writeSchedule(weekDir, { requireApproval = true } = {}) {
  const schedule = computeSchedule(weekDir, readJson(path.join(weekDir, 'approvals.json'), {}), { requireApproval });
  writeJsonAtomic(path.join(weekDir, 'schedule.json'), schedule);
  return schedule;
}

/** build.json: id for den aktuelle bygning. Preview-siden sender det med, så en gammel fane ikke kan godkende nyt indhold. */
export const readBuildId = (weekDir) => readJson(path.join(weekDir, 'build.json'), {}).buildId ?? null;
