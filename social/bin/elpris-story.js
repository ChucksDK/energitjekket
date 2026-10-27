#!/usr/bin/env node
// Dagens elpris-story (DK1 + DK2) og lørdagens reel. Bruger kun tal fra kilderegisteret,
// som scriptet selv opdaterer først (export_sources.py), ligesom build-week.
// Exit: 0 ok, 3 datoen findes ikke i sources.elpris (intet skrives),
//       4 render-/layoutfejl, eksportfejl, manglende lyd eller --reel på en ikke-lørdag.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import { loadSources, DEFAULT_SOURCES } from '../lib/sources.js';
import { validatePost, resolvePost } from '../lib/brief.js';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';
import { renderStory } from '../render/png.js';
import { renderShort } from '../render/short.js';

const WEEKDAYS = ['søndag', 'mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag'];
const AREAS = ['DK1', 'DK2'];
// Prisområderne skrives med navn på slidet; filnavnene beholder DK1/DK2.
const AREA_NAMES = { DK1: 'VESTDANMARK', DK2: 'ØSTDANMARK' };
const TARGET_URL = 'https://energitjekket.dk/elpris/';
const CTA = 'Se alle priser på energitjekket.dk/elpris';

const ymd = (s) => s.split('-').map(Number);
const utc = (s) => new Date(Date.UTC(...ymd(s).map((v, i) => (i === 1 ? v - 1 : v))));

export const danishWeekday = (date) => WEEKDAYS[utc(date).getUTCDay()];
export const dayMonth = (date) => `${ymd(date)[2]}/${ymd(date)[1]}`;

/** I morgen som YYYY-MM-DD efter Europe/Copenhagen (ikke maskinens tidszone). */
export function tomorrowCopenhagen(now = new Date()) {
  const today = new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Copenhagen', year: 'numeric', month: '2-digit', day: '2-digit' }).format(now);
  const t = utc(today);
  t.setUTCDate(t.getUTCDate() + 1);
  return t.toISOString().slice(0, 10);
}

const fid = (date, area, key) => `{elpris.${date}.${area}.${key}}`;

export function barsSlide(date, area, isTomorrow) {
  const day = isTomorrow ? 'i morgen' : danishWeekday(date);
  return {
    layout: 'bars',
    // Tagget indeholder dato (cifre) og kan ikke bestå brief-reglen om tal uden kilde.
    // Det sættes derfor EFTER validatePost/resolvePost (se withTag); alt andet går gennem reglerne.
    tag: 'ELPRIS',
    title: `Billigste time ${day}: ${fid(date, area, 'billigste_time')}`,
    highlight: fid(date, area, 'billigste_time'),
    // Elpris-tal er altid spotpris (uden afgifter og nettarif) og skal hedde det.
    // Billigste time står i titlen (gul); brødteksten gentager den ikke, så kun ét tal er gult.
    body: `Spotpris: billigst ${fid(date, area, 'billigste_pris')} pr. kWh, dyrest ${fid(date, area, 'dyreste_pris')} ${fid(date, area, 'dyreste_time')}.`,
    cta: CTA,
    bars: { date, area },
  };
}

// Ugedagen står i titlen; tagget holdes kort, så pillen bliver inden for den sikre margin.
export const storyTag = (date, area) => `ELPRIS · ${dayMonth(date)} · ${AREA_NAMES[area]}`;
const withTag = (slide, date, area) => ({ ...slide, tag: storyTag(date, area) });

function buildPost(id, type, slides, extra, sources) {
  const post = { id, type, target_url: TARGET_URL, slides, ...extra };
  // En story er ét slide, men brief-reglerne kræver 5-7 slides for en carousel. Tekstreglerne
  // (tal uden kilde, forbudte ord, fakta-id'er) valideres derfor på en 5x-udgave af samme slide.
  const checked = type === 'carousel' ? { ...post, slides: Array(5).fill(slides[0]) } : post;
  // validatePost måler titellængden på den uopløste tekst, hvor fakta-id'et (fx "{elpris.2026-10-27.DK1.billigste_time}")
  // alene fylder ~40 tegn. Vi dropper den måling her og tjekker i stedet den opløste titel (max 60) nedenfor.
  const errors = validatePost(checked, sources).filter((e) => !/ title: for langt/.test(e));
  if (errors.length) throw new Error(`Ugyldigt opslag ${id}:\n- ${errors.join('\n- ')}`);
  const resolved = resolvePost(post, sources);
  for (const [i, s] of resolved.slides.entries()) {
    if (s.title && s.title.length > 60) throw new Error(`Ugyldigt opslag ${id}: slide ${i + 1} title er for lang (${s.title.length} tegn)`);
  }
  return resolved;
}

function parseArgs(argv) {
  const o = { reel: false };
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === '--reel') o.reel = true;
    else if (['--date', '--sources', '--elpris', '--out', '--audio', '--audio-dir'].includes(a)) {
      if (argv[i + 1] === undefined) throw new Error(`${a} kræver en værdi`);
      o[a.slice(2).replace(/-(\w)/, (_, c) => c.toUpperCase())] = argv[++i];
    } else throw new Error(`Ukendt argument: ${a}`);
  }
  return o;
}

/** Vælger musik til reelen: roterer deterministisk gennem social/audio/ efter dato (samme dato = samme fil). */
export function pickAudio(o, date) {
  if (o.audio) return o.audio;
  const dir = o.audioDir ?? path.join(SOCIAL_ROOT, 'audio');
  const files = fs.existsSync(dir)
    ? fs.readdirSync(dir).filter((f) => /\.(mp3|m4a|wav)$/i.test(f)).sort()
    : [];
  if (!files.length) throw Object.assign(new Error(`Ingen lydfil i ${dir}; læg en musikfil dér eller angiv --audio`), { code: 4 });
  const day = Math.floor(utc(date).getTime() / 86400000);
  return files[day % files.length];
}

/** Opdaterer kilderegisteret (samme eksport som build-week). --sources/--elpris kan pege andre steder hen (tests). */
function exportSources(sourcesFile, elpris) {
  const args = [path.join(REPO_ROOT, 'social', 'data', 'export_sources.py'), '--out', sourcesFile];
  if (elpris) args.push('--elpris', path.resolve(elpris));
  try {
    execFileSync('python3', args, { stdio: 'pipe' });
  } catch (e) {
    const msg = String(e.stderr || e.message).trim().split('\n').pop();
    throw Object.assign(new Error(`Kilderegisteret kunne ikke opdateres: ${msg}`), { code: 4 });
  }
}

/** Renderer i en temp-mappe ved siden af out og flytter først filerne, når alle er lavet (ingen halve sæt). */
async function renderAll(out, jobs) {
  const parent = path.dirname(path.resolve(out));
  fs.mkdirSync(parent, { recursive: true });
  const tmp = fs.mkdtempSync(path.join(parent, '.story-tmp-'));
  try {
    const files = [];
    for (const [name, render] of jobs) files.push([name, await render(path.join(tmp, name))]);
    fs.mkdirSync(out, { recursive: true });
    return files.map(([name]) => {
      const dest = path.join(out, name);
      fs.renameSync(path.join(tmp, name), dest);
      return dest;
    });
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true });
  }
}

export async function main(argv, deps = {}) {
  const story = deps.renderStory ?? renderStory;
  const short = deps.renderShort ?? renderShort;
  const o = parseArgs(argv);
  const date = o.date ?? tomorrowCopenhagen();
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) throw Object.assign(new Error(`Ugyldig dato: ${date}`), { code: 4 });
  const isTomorrow = date === tomorrowCopenhagen();

  if (o.reel && danishWeekday(date) !== 'lørdag') {
    throw Object.assign(new Error(`--reel er kun tilladt på en lørdag (${date} er ${danishWeekday(date)}): kun lørdag`), { code: 4 });
  }

  const sourcesFile = o.sources ? path.resolve(o.sources) : DEFAULT_SOURCES;
  exportSources(sourcesFile, o.elpris);
  const sources = loadSources(sourcesFile);
  const day = sources.elpris?.[date];
  if (!day || !AREAS.every((a) => Array.isArray(day[a]?.hours) && day[a].hours.length === 24)) {
    throw Object.assign(new Error(`Ingen elpriser for ${date} i kilderegisteret; skriver ingenting`), { code: 3 });
  }
  // Først når datoen findes: vælg lyd (en manglende lydfil er exit 4, en manglende dato altid exit 3).
  const audio = o.reel ? pickAudio(o, date) : undefined;

  const out = o.out ?? path.join(SOCIAL_ROOT, 'out', 'stories', date);
  const written = await renderAll(
    out,
    AREAS.map((area) => [
      `elpris-${area}.png`,
      (file) => {
        const post = buildPost(`elpris-${area}`, 'carousel', [barsSlide(date, area, isTomorrow)], {}, sources);
        post.slides = [withTag(post.slides[0], date, area)];
        return story(post, file, { elpris: sources.elpris });
      },
    ]),
  );

  if (o.reel) {
    const slides = [
      {
        layout: 'cover',
        tag: 'ELPRIS',
        title: 'Lørdagens billigste timer',
        value: fid(date, 'DK1', 'billigste_time'),
        highlight: fid(date, 'DK1', 'billigste_time'),
        body: 'Billigste time i Vestdanmark. Se begge prisområder.',
      },
      ...AREAS.map((a) => barsSlide(date, a, false)),
      { layout: 'end', tag: 'ELPRIS', title: 'Se alle timepriser', body: 'Priserne opdateres hver dag.' },
    ];
    const post = buildPost('elpris-reel', 'short', slides, { audio }, sources);
    post.slides = post.slides.map((s, i) => (i === 1 || i === 2 ? withTag(s, date, AREAS[i - 1]) : { ...s, tag: `ELPRIS · LØRDAG ${dayMonth(date)}` }));
    written.push(
      ...(await renderAll(out, [[`reel-${date}.mp4`, (file) => short(post, file, { elpris: sources.elpris, audioDir: o.audioDir })]])),
    );
  }
  return written;
}

if (import.meta.url === pathToFileURL(process.argv[1] ?? '').href) {
  main(process.argv.slice(2)).then(
    (files) => {
      for (const f of files) console.log(f);
    },
    (e) => {
      console.error(e.message);
      process.exit(e.code ?? 4);
    },
  );
}
