// Zernio: planlægning af godkendte opslag på @energitjekket. Nøglen ligger lokalt, aldrig i repoet.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { SOCIAL_ROOT } from './paths.js';
import { readJson } from './schedule.js';

export const API = 'https://zernio.com/api/v1';
export const PUBLISH_FILE = path.join(SOCIAL_ROOT, 'publish.json');

export function loadPublishConfig(file = PUBLISH_FILE) {
  const c = readJson(file, null);
  if (!c?.accountId || !c?.timezone || !c?.keyFile) throw new Error(`${file} mangler accountId, timezone eller keyFile`);
  return c;
}

/** ZERNIO_API_KEY fra miljøet eller fra keyFile (linjen ZERNIO_API_KEY=...). */
export function readKey(cfg, env = process.env) {
  if (env.ZERNIO_API_KEY) return env.ZERNIO_API_KEY;
  const file = cfg.keyFile.replace(/^~/, os.homedir());
  const m = fs.existsSync(file) ? /^ZERNIO_API_KEY=(.+)$/m.exec(fs.readFileSync(file, 'utf8')) : null;
  if (!m) throw new Error(`ZERNIO_API_KEY mangler (miljøet eller ${cfg.keyFile})`);
  return m[1].trim().replace(/^["']|["']$/g, '');
}

/** "2026-11-02T07:30:00+01:00" -> "2026-11-02T07:30": Zernio får lokal tid + tidszone. */
export const localSlot = (slot) => slot.slice(0, 16);

/**
 * Hvad der skal ske med hvert opslag i schedule.json: 'send', eller 'skip' med en grund.
 * Et opslag sendes aldrig to gange (sent.json), og aldrig til et tidspunkt, der er gået.
 */
export function planSend(schedule, sent, now = new Date()) {
  return schedule.map((p) => {
    if (sent[p.id]) return { post: p, action: 'skip', reason: `allerede planlagt som Zernio-opslag ${sent[p.id].zernioId}` };
    if (new Date(p.slot) <= now) return { post: p, action: 'skip', reason: `${p.slot} er overstået` };
    const missing = p.files.filter((f) => !fs.existsSync(f));
    if (missing.length) return { post: p, action: 'skip', reason: `filer mangler: ${missing.join(', ')}` };
    if (!p.caption?.trim()) return { post: p, action: 'skip', reason: 'caption mangler' };
    return { post: p, action: 'send' };
  });
}

/** POST /posts-kroppen. Carousel = billeder i rækkefølge; short = én MP4 som reel, også vist i feedet. */
export function postBody(post, mediaItems, cfg) {
  return {
    content: post.caption.trimEnd(),
    mediaItems,
    scheduledFor: `${localSlot(post.slot)}:00`,
    timezone: cfg.timezone,
    platforms: [{ platform: 'instagram', accountId: cfg.accountId, ...(post.type === 'short' ? { platformSpecificData: { shareToFeed: true } } : {}) }],
  };
}

export const contentType = (file) => ({ '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.mp4': 'video/mp4' })[path.extname(file).toLowerCase()];

export function client(key, fetchImpl = fetch) {
  const api = async (method, p, body, headers = {}) => {
    const res = await fetchImpl(API + p, {
      method,
      headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json', ...headers },
      body: body ? JSON.stringify(body) : undefined,
    });
    const text = await res.text();
    let json;
    try {
      json = JSON.parse(text || '{}');
    } catch {
      json = { error: text.slice(0, 300) };
    }
    return { code: res.status, json };
  };

  // Zernio gemmer filen og giver Instagram en offentlig adresse.
  const upload = async (file, name) => {
    const bytes = fs.readFileSync(file);
    const type = contentType(file);
    const pre = await api('POST', '/media/presign', { filename: `${name}-${path.basename(file)}`, contentType: type, size: bytes.length });
    if (pre.code !== 200) throw new Error(`presign fejlede (${pre.code}): ${JSON.stringify(pre.json)}`);
    const put = await fetchImpl(pre.json.uploadUrl, { method: 'PUT', headers: { 'Content-Type': type }, body: bytes });
    if (![200, 201, 204].includes(put.status)) throw new Error(`upload fejlede (${put.status}) for ${file}`);
    return { type: type.startsWith('video/') ? 'video' : 'image', url: pre.json.publicUrl };
  };

  const getPost = async (id) => {
    const r = await api('GET', `/posts/${id}`);
    if (r.code !== 200) throw new Error(`GET /posts/${id} gav ${r.code}`);
    return r.json.post || r.json;
  };

  return { api, upload, getPost };
}

/** Lokal tid i tidszonen som "YYYY-MM-DDTHH:MM" (Zernio gemmer UTC). */
export function toLocal(iso, timezone) {
  const parts = Object.fromEntries(
    new Intl.DateTimeFormat('en-CA', { timeZone: timezone, year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' })
      .formatToParts(new Date(iso))
      .map((x) => [x.type, x.value]),
  );
  return `${parts.year}-${parts.month}-${parts.day}T${parts.hour}:${parts.minute}`;
}

/** Tjek efter planlægning: status, konto, tid og medier skal passe. Returnerer en liste af problemer. */
export function readBackProblems(zpost, post, cfg) {
  const problems = [];
  if (zpost.status !== 'scheduled') problems.push(`status er ${zpost.status}, ikke scheduled`);
  const accounts = (zpost.platforms || []).map((p) => p.accountId?._id ?? p.accountId);
  if (!accounts.includes(cfg.accountId)) problems.push(`opslaget ligger ikke på @${cfg.username}`);
  if (!zpost.scheduledFor || toLocal(zpost.scheduledFor, cfg.timezone) !== localSlot(post.slot)) {
    problems.push(`tidspunktet er ${zpost.scheduledFor ? toLocal(zpost.scheduledFor, cfg.timezone) : 'tomt'}, ikke ${localSlot(post.slot)}`);
  }
  if ((zpost.mediaItems || []).length !== post.files.length) problems.push(`${(zpost.mediaItems || []).length} medier, forventede ${post.files.length}`);
  return problems;
}
