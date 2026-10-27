#!/usr/bin/env node
// Zernio-køen for @energitjekket: se, flyt og aflys planlagte opslag.
//   node social/bin/queue.js list
//   node social/bin/queue.js move <zernio-id> <YYYY-MM-DDTHH:MM> [--send]
//   node social/bin/queue.js cancel <zernio-id> [--send]
// move og cancel viser kun, hvad der vil ske, medmindre --send er med.
import { pathToFileURL } from 'node:url';
import { client, loadPublishConfig, readKey, toLocal } from '../lib/zernio.js';

const DAYS = ['søn', 'man', 'tir', 'ons', 'tor', 'fre', 'lør'];

/** Opslag pr. lokal minut; to opslag i samme minut er et sammenstød. */
export function clashes(posts, timezone) {
  const seen = {};
  for (const p of posts) if (p.scheduledFor) (seen[toLocal(p.scheduledFor, timezone)] ??= []).push(p._id);
  return Object.entries(seen).filter(([, ids]) => ids.length > 1).map(([when]) => when);
}

async function main() {
  const [cmd = 'list', id, when] = process.argv.slice(2).filter((a) => a !== '--send');
  const send = process.argv.includes('--send');
  const cfg = loadPublishConfig();
  const z = client(readKey(cfg));

  if (cmd === 'list') {
    const { code, json } = await z.api('GET', `/posts?accountId=${cfg.accountId}&limit=100`);
    if (code !== 200) throw new Error(`GET /posts gav ${code}`);
    const posts = (json.posts || json).filter((p) => p.status === 'scheduled' || p.status === 'publishing' || p.status === 'failed');
    posts.sort((a, b) => (a.scheduledFor || '').localeCompare(b.scheduledFor || ''));
    for (const p of posts) {
      const local = p.scheduledFor ? toLocal(p.scheduledFor, cfg.timezone) : '-';
      const day = p.scheduledFor ? DAYS[new Date(`${local.slice(0, 10)}T12:00:00Z`).getUTCDay()] : '';
      console.log(`${day} ${local.replace('T', ' ')}  ${p.status}  ${p._id}  ${(p.content || '').split('\n')[0].slice(0, 60)}`);
    }
    const c = clashes(posts, cfg.timezone);
    console.log(`\n${posts.length} i køen på @${cfg.username}. Sammenstød: ${c.length ? c.join(', ') : 'ingen'}`);
    return;
  }

  if (!id) throw new Error('Mangler Zernio-id');
  const before = await z.getPost(id);
  console.log(`${id}: ${before.status}, ${before.scheduledFor ? toLocal(before.scheduledFor, cfg.timezone) : '-'}: ${(before.content || '').split('\n')[0].slice(0, 60)}`);

  if (cmd === 'move') {
    if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$/.test(when || '')) throw new Error('Tidspunkt skal være YYYY-MM-DDTHH:MM (dansk tid)');
    if (!send) return console.log(`Flyttes til ${when}. Tilføj --send.`);
    const r = await z.api('PUT', `/posts/${id}`, { scheduledFor: `${when}:00`, timezone: cfg.timezone });
    if (r.code !== 200) throw new Error(`PUT gav ${r.code}: ${JSON.stringify(r.json).slice(0, 300)}`);
    const after = await z.getPost(id);
    const local = toLocal(after.scheduledFor, cfg.timezone);
    console.log(local === when && after.status === 'scheduled' ? `OK: ${local}` : `PROBLEM: ${after.status}, ${local}`);
    return;
  }

  if (cmd === 'cancel') {
    if (!send) return console.log('Aflyses. Tilføj --send.');
    const r = await z.api('DELETE', `/posts/${id}`);
    if (![200, 204].includes(r.code)) throw new Error(`DELETE gav ${r.code}`);
    console.log('Aflyst. Fjern linjen i out/<uge>/sent.json, hvis opslaget skal kunne sendes igen.');
    return;
  }

  throw new Error(`Ukendt kommando: ${cmd}`);
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  main().catch((e) => {
    console.error(e.message);
    process.exit(1);
  });
}
