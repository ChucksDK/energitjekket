#!/usr/bin/env node
// Planlægger ugens godkendte opslag (out/<uge>/schedule.json) i Zernio på @energitjekket.
// Uden --send vises kun planen. Med --send uploades filerne, opslaget oprettes og læses tilbage.
// Hvert planlagt opslag skrives i out/<uge>/sent.json, så det aldrig sendes to gange.
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { SOCIAL_ROOT } from '../lib/paths.js';
import { readBuildId, readJson, writeJsonAtomic } from '../lib/schedule.js';
import { client, loadPublishConfig, localSlot, planSend, postBody, readBackProblems, readKey } from '../lib/zernio.js';

export async function publishWeek(week, { send = false, only = null, outRoot = path.join(SOCIAL_ROOT, 'out'), cfg = loadPublishConfig(), key, fetchImpl, now = new Date(), log = console.log } = {}) {
  const weekDir = path.join(outRoot, week);
  const scheduleFile = path.join(weekDir, 'schedule.json');
  if (!fs.existsSync(scheduleFile)) throw new Error(`${scheduleFile} findes ikke. Byg ugen først (build-week.js).`);
  const schedule = readJson(scheduleFile, []).filter((p) => !only || p.id === only);
  const sentFile = path.join(weekDir, 'sent.json');
  const sent = readJson(sentFile, {});
  const plan = planSend(schedule, sent, now);

  log(`@${cfg.username}, uge ${week}: ${schedule.length} godkendte opslag i schedule.json`);
  for (const { post, action, reason } of plan) {
    const what = post.type === 'short' ? 'reel' : `carousel, ${post.files.length} billeder`;
    log(`${action === 'send' ? 'SEND' : 'SKIP'}  ${localSlot(post.slot)}  ${post.id} (${what})${reason ? `: ${reason}` : ''}`);
  }
  const todo = plan.filter((x) => x.action === 'send');
  if (!send) {
    log(todo.length ? `\nIntet er sendt. Tilføj --send for at planlægge ${todo.length} opslag.` : '\nIntet at sende.');
    return { plan, sent: [] };
  }

  const z = client(key ?? readKey(cfg), fetchImpl);
  const buildId = readBuildId(weekDir);
  const done = [];
  for (const { post } of todo) {
    const media = [];
    for (const f of post.files) media.push(await z.upload(f, `${week}-${post.id}`));
    const { code, json } = await z.api('POST', '/posts', postBody(post, media, cfg), { 'Idempotency-Key': `energitjekket-ig-${week}-${post.id}-${buildId}` });
    const zpost = json.post || json;
    if (![200, 201].includes(code) || !zpost.status || ['failed', 'partial'].includes(zpost.status)) {
      const err = (zpost.platforms || []).map((p) => p.errorMessage).filter(Boolean).join('; ') || json.error || JSON.stringify(json).slice(0, 300);
      throw new Error(`Zernio afviste ${post.id} (${code}, status ${zpost.status}): ${err}`);
    }
    const zernioId = zpost._id || zpost.id;
    sent[post.id] = { zernioId, slot: post.slot, buildId, sentAt: new Date().toISOString() };
    writeJsonAtomic(sentFile, sent);
    const problems = readBackProblems(await z.getPost(zernioId), post, cfg);
    log(`${problems.length ? 'PROBLEM' : 'OK'}  ${post.id} -> Zernio ${zernioId}${problems.length ? `: ${problems.join('; ')}` : ''}`);
    done.push({ id: post.id, zernioId, problems });
  }
  return { plan, sent: done };
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  const args = process.argv.slice(2);
  const i = args.indexOf('--only');
  const only = i === -1 ? null : args.splice(i, 2)[1];
  const send = args.includes('--send');
  const week = args.find((a) => !a.startsWith('--'));
  if (!week) {
    console.error('Brug: node social/bin/publish.js <uge> [--send] [--only <opslags-id>]');
    process.exit(2);
  }
  try {
    const { sent } = await publishWeek(week, { send, only });
    if (sent.some((s) => s.problems.length)) process.exit(1);
  } catch (e) {
    console.error(e.message);
    process.exit(1);
  }
}
