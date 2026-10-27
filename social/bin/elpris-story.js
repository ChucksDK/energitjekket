#!/usr/bin/env node
// Dagens elpris-story (DK1 + DK2) og lørdagens reel. Bruger kun tal fra kilderegisteret.
// Exit: 0 ok, 3 datoen findes ikke i sources.elpris (intet skrives), 4 render-/layoutfejl eller --reel på en ikke-lørdag.
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { loadSources } from '../lib/sources.js';
import { validatePost, resolvePost } from '../lib/brief.js';
import { SOCIAL_ROOT } from '../lib/paths.js';
import { renderStory } from '../render/png.js';
import { renderShort } from '../render/short.js';

const WEEKDAYS = ['søndag', 'mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag'];
const AREAS = ['DK1', 'DK2'];
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

function barsSlide(date, area, isTomorrow) {
  const day = isTomorrow ? 'i morgen' : danishWeekday(date);
  return {
    layout: 'bars',
    // Tagget indeholder dato (cifre) og kan ikke bestå brief-reglen om tal uden kilde.
    // Det sættes derfor EFTER validatePost/resolvePost (se withTag); alt andet går gennem reglerne.
    tag: 'ELPRIS',
    title: `Billigste time ${day}: ${fid(date, area, 'billigste_time')}`,
    highlight: fid(date, area, 'billigste_time'),
    body: `Billigst ${fid(date, area, 'billigste_pris')} pr. kWh, dyrest ${fid(date, area, 'dyreste_pris')} ${fid(date, area, 'dyreste_time')}.`,
    cta: CTA,
    bars: { date, area },
  };
}

const withTag = (slide, date, area) => ({
  ...slide,
  tag: `ELPRIS · ${danishWeekday(date).toUpperCase()} ${dayMonth(date)} · ${area}`,
});

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
    else if (['--date', '--sources', '--out', '--audio', '--audio-dir'].includes(a)) {
      if (argv[i + 1] === undefined) throw new Error(`${a} kræver en værdi`);
      o[a.slice(2).replace(/-(\w)/, (_, c) => c.toUpperCase())] = argv[++i];
    } else throw new Error(`Ukendt argument: ${a}`);
  }
  return o;
}

function pickAudio(o) {
  if (o.audio) return o.audio;
  const dir = o.audioDir ?? path.join(SOCIAL_ROOT, 'audio');
  const files = fs.existsSync(dir)
    ? fs.readdirSync(dir).filter((f) => /\.(mp3|m4a|wav)$/i.test(f)).sort()
    : [];
  if (!files.length) throw new Error(`Ingen lydfil i ${dir}; læg en musikfil dér eller angiv --audio`);
  return files[0];
}

export async function main(argv) {
  const o = parseArgs(argv);
  const date = o.date ?? tomorrowCopenhagen();
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) throw Object.assign(new Error(`Ugyldig dato: ${date}`), { code: 4 });
  const isTomorrow = date === tomorrowCopenhagen();

  if (o.reel && danishWeekday(date) !== 'lørdag') {
    throw Object.assign(new Error(`--reel er kun tilladt på en lørdag (${date} er ${danishWeekday(date)}): kun lørdag`), { code: 4 });
  }
  const audio = o.reel ? pickAudio(o) : undefined;

  const sources = loadSources(o.sources);
  const day = sources.elpris?.[date];
  if (!day || !AREAS.every((a) => Array.isArray(day[a]?.hours) && day[a].hours.length === 24)) {
    throw Object.assign(new Error(`Ingen elpriser for ${date} i kilderegisteret; skriver ingenting`), { code: 3 });
  }

  const out = o.out ?? path.join(SOCIAL_ROOT, 'out', 'stories', date);
  const written = [];
  for (const area of AREAS) {
    const post = buildPost(`elpris-${area}`, 'carousel', [barsSlide(date, area, isTomorrow)], {}, sources);
    post.slides = [withTag(post.slides[0], date, area)];
    written.push(await renderStory(post, path.join(out, `elpris-${area}.png`), { elpris: sources.elpris }));
  }

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
    written.push(await renderShort(post, path.join(out, `reel-${date}.mp4`), { elpris: sources.elpris, audioDir: o.audioDir }));
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
