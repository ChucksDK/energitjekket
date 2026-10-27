#!/usr/bin/env node
// Bygger en uge: brief -> validering -> screenshots -> PNG/MP4 + caption -> preview.html, schedule.json.
// Exit: 0 hvis mindst ét opslag blev bygget, ellers 1.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import { loadSources, DEFAULT_SOURCES } from '../lib/sources.js';
import { validatePost, resolvePost } from '../lib/brief.js';
import { weekErrors } from '../lib/week.js';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';
import { CONFIG_FILE, loadConfig, writeJsonAtomic, writeSchedule } from '../lib/schedule.js';
import { renderCarousel, withBrowser } from '../render/png.js';
import { renderShort } from '../render/short.js';
import { shootPage, screenFile } from '../render/screenshot.js';
import { previewHtml } from '../templates/preview.html.js';

const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9._-]*$/;
const SAFE_WEEK = /^[A-Za-z0-9][A-Za-z0-9._-]*$/;
const SLOT = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$/;

function parseArgs(argv) {
  const o = { briefs: [] };
  const valued = ['--base', '--sources', '--elpris', '--audio-dir', '--out-root', '--config'];
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (valued.includes(a)) {
      if (argv[i + 1] === undefined) throw new Error(`${a} kræver en værdi`);
      o[a.slice(2).replace(/-(\w)/, (_, c) => c.toUpperCase())] = argv[++i];
    } else if (a.startsWith('--')) throw new Error(`Ukendt argument: ${a}`);
    else o.briefs.push(a);
  }
  if (o.briefs.length !== 1) throw new Error('Brug: node social/bin/build-week.js <brief.json> [--base URL]');
  return o;
}

export const captionText = (post) =>
  [post.caption, post.sources.length ? `Kilde: ${post.sources.join(', ')}` : null, post.hashtags.join(' ')]
    .filter((s) => s !== null && s !== '')
    .join('\n\n') + '\n';

const slotKey = (p) => String(p.slot);

export async function buildWeek(argv, log = console.log) {
  const o = parseArgs(argv);
  const brief = JSON.parse(fs.readFileSync(o.briefs[0], 'utf8'));
  if (typeof brief.week !== 'string' || !SAFE_WEEK.test(brief.week)) throw new Error(`Briefen mangler et gyldigt "week"`);
  if (!Array.isArray(brief.posts)) throw new Error('Briefen mangler "posts"');

  const sourcesFile = o.sources ? path.resolve(o.sources) : DEFAULT_SOURCES;
  const exporter = ['python3', path.join(REPO_ROOT, 'social', 'data', 'export_sources.py'), '--out', sourcesFile];
  if (o.elpris) exporter.push('--elpris', path.resolve(o.elpris));
  execFileSync(exporter[0], exporter.slice(1), { stdio: 'pipe' });
  const sources = loadSources(sourcesFile);
  const config = loadConfig(o.config ? path.resolve(o.config) : CONFIG_FILE);

  const weekDir = path.join(path.resolve(o.outRoot ?? path.join(SOCIAL_ROOT, 'out')), brief.week);
  fs.mkdirSync(path.join(weekDir, 'screens'), { recursive: true });
  // Før noget renderes: ryd godkendelser og plan, så et afbrudt byg aldrig efterlader gamle godkendelser
  // der peger på nye, ugodkendte filer. Nyt build-id gør åbne preview-faner ugyldige.
  const buildId = `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 10)}`;
  fs.rmSync(path.join(weekDir, 'approvals.json'), { force: true });
  for (const f of ['manifest.json', 'schedule.json', 'errors.json']) writeJsonAtomic(path.join(weekDir, f), []);
  writeJsonAtomic(path.join(weekDir, 'build.json'), { buildId });
  const base = o.base ?? 'https://energitjekket.dk';

  const built = [];
  const errors = [];
  const seen = new Set();
  const shot = new Map(); // nøgle -> Promise (hver side tages kun én gang)

  const shoot = (key) => {
    if (!shot.has(key)) shot.set(key, shootPage(key, path.join(weekDir, 'screens', screenFile(key)), base));
    return shot.get(key);
  };

  // Tjek på tværs af ugen: dublerede slots, id/slot-dato, tidspunkt pr. type, fredag 19:30 (elpris-reel).
  const week = weekErrors(brief.posts);

  await withBrowser(async () => {
    for (const [i, post] of brief.posts.entries()) {
      const id = post && typeof post.id === 'string' ? post.id : '(uden id)';
      try {
        if (!SAFE_ID.test(id)) throw new Error(`Ugyldigt opslags-id: ${id}`);
        if (seen.has(id)) throw new Error(`Opslags-id er brugt flere gange: ${id}`);
        seen.add(id);
        if (!SLOT.test(String(post.slot))) throw new Error(`slot skal have formen YYYY-MM-DDTHH:MM (fik "${post.slot}")`);
        const errs = [...week[i], ...validatePost(post, sources)];
        if (errs.length) {
          errors.push({ id, errors: errs });
          continue;
        }
        const resolved = resolvePost(post, sources);
        for (const s of resolved.slides) if (s.layout === 'screenshot') await shoot(s.screenshot);

        const dir = path.join(weekDir, id);
        fs.rmSync(dir, { recursive: true, force: true });
        fs.mkdirSync(dir, { recursive: true });
        const ropts = { baseDir: weekDir, elpris: sources.elpris };
        let files;
        if (resolved.type === 'carousel') files = await renderCarousel(resolved, dir, ropts);
        else files = [await renderShort(resolved, path.join(dir, `${id}.mp4`), { ...ropts, audioDir: o.audioDir })];
        fs.writeFileSync(path.join(dir, 'caption.txt'), captionText(resolved));
        built.push({
          id,
          slot: post.slot,
          type: resolved.type,
          files: files.map((f) => path.relative(weekDir, f).split(path.sep).join('/')),
          caption: captionText(resolved).trimEnd(),
          sources: resolved.sources,
        });
        log(`Bygget: ${id}`);
      } catch (e) {
        errors.push({ id, errors: [e.message] });
        log(`Fejl i ${id}: ${e.message}`);
      }
    }
  });

  built.sort((a, b) => slotKey(a).localeCompare(slotKey(b)));
  writeJsonAtomic(path.join(weekDir, 'manifest.json'), built.map(({ id, slot, type, files }) => ({ id, slot, type, files })));
  writeJsonAtomic(path.join(weekDir, 'errors.json'), errors);
  fs.writeFileSync(path.join(weekDir, 'preview.html'), previewHtml({ week: brief.week, posts: built, errors, buildId, requireApproval: config.require_approval }));
  writeSchedule(weekDir, { requireApproval: config.require_approval });
  log(`Uge ${brief.week}: ${built.length} bygget, ${errors.length} fejlede. ${path.join(weekDir, 'preview.html')}`);
  return { weekDir, built, errors };
}

if (import.meta.url === pathToFileURL(process.argv[1] ?? '').href) {
  buildWeek(process.argv.slice(2)).then(
    ({ built }) => process.exit(built.length ? 0 : 1),
    (e) => {
      console.error(e.message);
      process.exit(1);
    },
  );
}
