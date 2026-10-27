import fs from 'node:fs';
import path from 'node:path';
import { SOCIAL_ROOT } from './paths.js';

export const DEFAULT_SOURCES = path.join(SOCIAL_ROOT, 'data', 'sources.json');

export function loadSources(file = DEFAULT_SOURCES) {
  if (!fs.existsSync(file)) {
    throw new Error(`Kilderegister mangler: ${file}. Kør: python3 social/data/export_sources.py`);
  }
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

export function getFact(sources, id) {
  const fact = Object.hasOwn(sources.facts, id) ? sources.facts[id] : undefined;
  if (!fact) throw new Error(`Ukendt fakta-id: ${id}`);
  return fact;
}
