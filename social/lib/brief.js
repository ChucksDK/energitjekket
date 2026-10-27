import { formatFact } from './format.js';
import { getFact } from './sources.js';

const PLACEHOLDER = /\{([^{}]+)\}/g;
const YEAR = /\b20(2\d|3[0-5])\b/g;
const BANNED = ['!', 'book nu', 'begrænset', 'skynd dig', 'gratis', 'garanti', 'kun i dag', 'spar op til'];
const LAYOUTS = ['cover', 'stat', 'kpi2', 'bars', 'text', 'screenshot', 'end'];
const TYPES = ['carousel', 'short'];
const LIMITS = { tag: 24, title: 60, body: 160 };
const URL_PREFIX = 'https://energitjekket.dk/';

// Fjerner enheden fra en formateret værdi ("32.388 kr." -> "32.388").
const stripUnit = (s) => (/^[\d.,-]+ \S+$/.test(s) ? s.replace(/ \S+$/, '') : s);

export function resolveText(text, sources, { stripUnits = false } = {}) {
  const factIds = [];
  const out = String(text).replace(PLACEHOLDER, (_, id) => {
    const fact = getFact(sources, id);
    if (!factIds.includes(id)) factIds.push(id);
    const f = formatFact(fact.value, fact.unit);
    return stripUnits ? stripUnit(f) : f;
  });
  return { text: out, factIds };
}

// Alle tekstfelter på en slide: [sti, tekst, stripUnits]
function slideFields(slide) {
  const f = [];
  for (const k of ['tag', 'title', 'value', 'body', 'highlight']) {
    if (typeof slide[k] === 'string') f.push([k, slide[k], false]);
  }
  (slide.kpis || []).forEach((k, i) => {
    const hasUnit = Boolean(k.unit);
    if (typeof k.label === 'string') f.push([`kpis[${i}].label`, k.label, false]);
    if (typeof k.value === 'string') f.push([`kpis[${i}].value`, k.value, hasUnit]);
    if (typeof k.unit === 'string') f.push([`kpis[${i}].unit`, k.unit, false]);
  });
  return f;
}

function textErrors(where, text, post, errors) {
  const lower = text.toLowerCase();
  for (const w of BANNED) if (lower.includes(w)) errors.push(`${where}: forbudt: "${w}"`);
  if (post.quote !== true && lower.includes('tilbud')) {
    errors.push(`${where}: "tilbud" er kun tilladt når quote er true`);
  }
  const stripped = text.replace(PLACEHOLDER, ' ').replace(YEAR, ' ');
  for (const m of stripped.match(/\d[\d.,]*\d|\d/g) || []) {
    errors.push(`${where}: tal uden kilde: "${m}"`);
  }
}

export function validatePost(post, sources) {
  const errors = [];
  const slides = Array.isArray(post.slides) ? post.slides : [];

  if (!TYPES.includes(post.type)) errors.push(`type skal være carousel eller short (fik "${post.type}")`);
  if (post.type === 'carousel' && (slides.length < 5 || slides.length > 7)) {
    errors.push(`carousel skal have 5-7 slides (har ${slides.length})`);
  }
  if (post.type === 'short') {
    if (slides.length < 3 || slides.length > 6) errors.push(`short skal have 3-6 slides (har ${slides.length})`);
    if (!post.audio) errors.push('short mangler audio');
  }

  if (typeof post.target_url !== 'string' || !post.target_url.startsWith(URL_PREFIX)) {
    errors.push(`target_url skal starte med ${URL_PREFIX}`);
  } else if (post.quote !== true && /\/tilbud(\/|$|\?|#)/i.test(post.target_url)) {
    errors.push('target_url peger på tilbud, men quote er ikke true');
  }

  const unknown = new Set();
  const checkFacts = (where, text) => {
    for (const [, id] of text.matchAll(PLACEHOLDER)) {
      try {
        getFact(sources, id);
      } catch (e) {
        if (!unknown.has(id)) {
          unknown.add(id);
          errors.push(`${where}: ${e.message}`);
        }
      }
    }
  };

  slides.forEach((slide, i) => {
    const n = `slide ${i + 1}`;
    if (!LAYOUTS.includes(slide.layout)) errors.push(`${n}: ukendt layout "${slide.layout}"`);
    if (slide.bg && i > 0) errors.push(`${n}: bg kun på første slide`);
    for (const [k, text] of slideFields(slide)) {
      textErrors(`${n} ${k}`, text, post, errors);
      checkFacts(`${n} ${k}`, text);
    }
    for (const [k, max] of Object.entries(LIMITS)) {
      if (typeof slide[k] === 'string' && slide[k].length > max) {
        errors.push(`${n} ${k}: for langt (${slide[k].length} tegn, max ${max})`);
      }
    }
  });

  if (typeof post.caption === 'string') {
    textErrors('caption', post.caption, post, errors);
    checkFacts('caption', post.caption);
  }
  (post.hashtags || []).forEach((h, i) => textErrors(`hashtag ${i + 1}`, String(h), post, errors));

  return errors;
}

export function resolvePost(post, sources) {
  const all = new Set();
  const used = (ids) => ids.forEach((id) => all.add(getFact(sources, id).source.name));

  const slides = (post.slides || []).map((slide) => {
    const names = new Set();
    const res = (text, strip = false) => {
      const r = resolveText(text, sources, { stripUnits: strip });
      r.factIds.forEach((id) => names.add(getFact(sources, id).source.name));
      return r.text;
    };
    const out = { ...slide };
    for (const k of ['tag', 'title', 'value', 'body', 'highlight']) {
      if (typeof slide[k] === 'string') out[k] = res(slide[k]);
    }
    if (slide.kpis) {
      out.kpis = slide.kpis.map((k) => ({
        ...k,
        label: typeof k.label === 'string' ? res(k.label) : k.label,
        value: typeof k.value === 'string' ? res(k.value, Boolean(k.unit)) : k.value,
      }));
    }
    out.sources = [...names];
    names.forEach((n) => all.add(n));
    return out;
  });

  const out = { ...post, slides };
  if (typeof post.caption === 'string') {
    const r = resolveText(post.caption, sources);
    used(r.factIds);
    out.caption = r.text;
  }
  out.sources = [...all];
  return out;
}
