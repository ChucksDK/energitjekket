import { formatFact } from './format.js';
import { getFact } from './sources.js';

const PLACEHOLDER = /\{([^{}]+)\}/g;
const YEAR = /\b20(2\d|3[0-5])\b/g;
export const BANNED = ['!', 'book nu', 'begrænset', 'skynd dig', 'gratis', 'garanti', 'kun i dag', 'spar op til'];
const LAYOUTS = ['cover', 'stat', 'kpi2', 'bars', 'text', 'screenshot', 'end'];
const TYPES = ['carousel', 'short'];
const LIMITS = { tag: 24, title: 60, body: 160 };
const URL_PREFIX = 'https://energitjekket.dk/';
export const ELPRIS_SOURCE_NAME = 'Energi Data Service (Energinet), spotpris';

// Kilden til et søjlediagram: samme kilde som elpris-fakta for dagen (faldback: registerets elpris-kilde).
function barsSource(sources, bars) {
  const id = `elpris.${bars?.date}.${bars?.area}.billigste_pris`;
  if (Object.hasOwn(sources.facts, id)) return sources.facts[id].source.name;
  const any = Object.entries(sources.facts).find(([k]) => k.startsWith('elpris.'));
  return any ? any[1].source.name : ELPRIS_SOURCE_NAME;
}

// Fjerner enheden fra en formateret værdi ("32.388 kr." -> "32.388").
const stripUnit = (s) => (/^[\d.,-]+ \S+$/.test(s) ? s.replace(/ \S+$/, '') : s);

export function resolveText(text, sources, { stripUnits = false } = {}) {
  const factIds = [];
  const out = String(text).replace(PLACEHOLDER, (_, id, offset, whole) => {
    const fact = getFact(sources, id);
    if (!factIds.includes(id)) factIds.push(id);
    const f = stripUnits ? stripUnit(formatFact(fact.value, fact.unit)) : formatFact(fact.value, fact.unit);
    // "ca. {x}." med x = "9.386 kr." må ikke give "kr..": sætningens punktum genbruger forkortelsens.
    return f.endsWith('.') && whole[offset + id.length + 2] === '.' ? f.slice(0, -1) : f;
  });
  return { text: out, factIds };
}

const isObj = (x) => x !== null && typeof x === 'object' && !Array.isArray(x);
const norm = (s) => s.normalize('NFKC').replace(/\p{Cf}/gu, '');

// EN tabel over tekstfelter: bruges af både validering og opløsning.
// visit(path, value, {placeholders, strip}, ctx) returnerer ny værdi; struktur-fejl rapporteres via report(msg).
function walkPost(post, visit, report) {
  const out = { ...post };
  const field = (obj, key, path, opts) => {
    if (obj[key] === undefined || obj[key] === null) return;
    obj[key] = visit(path, obj[key], opts);
  };

  if (post.slides !== undefined && !Array.isArray(post.slides)) report('slides skal være en liste');
  const slides = Array.isArray(post.slides) ? post.slides : [];
  out.slides = slides.map((slide, i) => {
    const n = `slide ${i + 1}`;
    if (!isObj(slide)) {
      report(`${n}: skal være et objekt`);
      return slide;
    }
    const s = { ...slide };
    for (const k of ['tag', 'title', 'value', 'body', 'highlight']) {
      field(s, k, `${n} ${k}`, { placeholders: true, slide: i });
    }
    if (s.kpis !== undefined) {
      if (!Array.isArray(s.kpis)) {
        report(`${n}: kpis skal være en liste`);
      } else {
        s.kpis = s.kpis.map((kpi, j) => {
          if (!isObj(kpi)) {
            report(`${n} kpis[${j}]: skal være et objekt`);
            return kpi;
          }
          const k = { ...kpi };
          const p = `${n} kpis[${j}]`;
          field(k, 'label', `${p}.label`, { placeholders: true, slide: i });
          field(k, 'value', `${p}.value`, { placeholders: true, strip: Boolean(kpi.unit), slide: i });
          field(k, 'unit', `${p}.unit`, { placeholders: false, slide: i });
          return k;
        });
      }
    }
    return s;
  });
  field(out, 'caption', 'caption', { placeholders: true });
  if (out.hashtags !== undefined) {
    if (!Array.isArray(out.hashtags)) report('hashtags skal være en liste');
    else out.hashtags = out.hashtags.map((h, i) => visit(`hashtag ${i + 1}`, h, { placeholders: false }));
  }
  return out;
}

function textErrors(where, text, post, errors) {
  const clean = norm(text);
  const lower = clean.toLowerCase();
  for (const w of BANNED) if (lower.includes(w)) errors.push(`${where}: forbudt: "${w}"`);
  if (post.quote !== true && lower.includes('tilbud')) {
    errors.push(`${where}: "tilbud" er kun tilladt når quote er true`);
  }
  const stripped = clean.replace(PLACEHOLDER, ' ').replace(YEAR, ' ');
  for (const m of stripped.match(/\p{N}[\p{N}.,]*\p{N}|\p{N}/gu) || []) {
    errors.push(`${where}: tal uden kilde: "${m}"`);
  }
}

export function validatePost(post, sources) {
  const errors = [];
  if (!isObj(post)) return ['post skal være et objekt'];
  const slideCount = Array.isArray(post.slides) ? post.slides.length : 0;

  if (!TYPES.includes(post.type)) errors.push(`type skal være carousel eller short (fik "${post.type}")`);
  if (post.type === 'carousel' && (slideCount < 5 || slideCount > 7)) {
    errors.push(`carousel skal have 5-7 slides (har ${slideCount})`);
  }
  if (post.type === 'short') {
    if (slideCount < 3 || slideCount > 6) errors.push(`short skal have 3-6 slides (har ${slideCount})`);
    if (!post.audio) errors.push('short mangler audio');
  }

  if (typeof post.target_url !== 'string' || !post.target_url.startsWith(URL_PREFIX)) {
    errors.push(`target_url skal starte med ${URL_PREFIX}`);
  } else if (post.quote !== true) {
    let p = post.target_url.slice(URL_PREFIX.length - 1).split(/[?#]/)[0];
    try {
      p = decodeURIComponent(p);
    } catch {
      errors.push('target_url kan ikke afkodes');
    }
    if (/^\/tilbud(\/|$)/i.test(p) || /\/tilbud(\/|$)/i.test(p)) {
      errors.push('target_url peger på tilbud, men quote er ikke true');
    }
  }

  const unknown = new Set();
  const visit = (where, value, opts) => {
    if (typeof value !== 'string') {
      errors.push(`${where}: skal være tekst (fik ${typeof value})`);
      return value;
    }
    textErrors(where, value, post, errors);
    if (!opts.placeholders) {
      if (/[{}]/.test(value)) errors.push(`${where}: pladsholdere er ikke tilladt her`);
    } else {
      for (const [, id] of value.matchAll(PLACEHOLDER)) {
        try {
          getFact(sources, id);
        } catch (e) {
          if (!unknown.has(id)) {
            unknown.add(id);
            errors.push(`${where}: ${e.message}`);
          }
        }
      }
    }
    const m = /^(slide \d+) (tag|title|body)$/.exec(where);
    if (m) {
      // Længden måles på den opløste tekst; ukendt fakta-id er allerede rapporteret, så mål da den rå tekst.
      let measured = value;
      if (opts.placeholders) {
        try {
          measured = resolveText(value, sources).text;
        } catch {
          measured = value;
        }
      }
      if (measured.length > LIMITS[m[2]]) {
        errors.push(`${where}: for langt (${measured.length} tegn, max ${LIMITS[m[2]]})`);
      }
    }
    return value;
  };
  walkPost(post, visit, (msg) => errors.push(msg));

  if (Array.isArray(post.slides)) {
    post.slides.forEach((slide, i) => {
      if (!isObj(slide)) return;
      const n = `slide ${i + 1}`;
      if (!LAYOUTS.includes(slide.layout)) errors.push(`${n}: ukendt layout "${slide.layout}"`);
      if (slide.bg && i > 0) errors.push(`${n}: bg kun på første slide`);
      if (slide.layout === 'bars') {
        // Søjlerne tegnes ud fra registerets timepriser. Datoen skal findes nu, ellers kan opslaget ikke bygges igen.
        const { date, area } = isObj(slide.bars) ? slide.bars : {};
        if (!isObj(slide.bars) || typeof date !== 'string' || typeof area !== 'string') {
          errors.push(`${n}: bars mangler {date, area}`);
        } else if (!Array.isArray(sources.elpris?.[date]?.[area]?.hours)) {
          errors.push(`${n}: ingen elpriser for ${date} ${area} i kilderegisteret (elpris-opslag hører til elpris-story.js, ikke ugens brief)`);
        }
      }
    });
  }
  return errors;
}

export function resolvePost(post, sources) {
  const all = new Set();
  const perSlide = new Map();
  const visit = (_where, value, opts) => {
    if (typeof value !== 'string' || !opts.placeholders) return value;
    const r = resolveText(value, sources, { stripUnits: Boolean(opts.strip) });
    for (const id of r.factIds) {
      const name = getFact(sources, id).source.name;
      all.add(name);
      if (opts.slide !== undefined) {
        if (!perSlide.has(opts.slide)) perSlide.set(opts.slide, new Set());
        perSlide.get(opts.slide).add(name);
      }
    }
    return r.text;
  };
  const out = walkPost(post, visit, () => {});
  out.slides = out.slides.map((s, i) => {
    const names = new Set(perSlide.get(i) || []);
    // Søjlerne er tal, selv om de ikke står som pladsholder: kilden skal stå på slidet.
    if (s.layout === 'bars') {
      const name = barsSource(sources, s.bars);
      names.add(name);
      all.add(name);
    }
    return { ...s, sources: [...names] };
  });
  out.sources = [...all];
  return out;
}
