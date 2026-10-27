#!/usr/bin/env node
import { loadSources } from '../lib/sources.js';
import { formatFact } from '../lib/format.js';

const args = process.argv.slice(2);
let file;
const i = args.indexOf('--sources');
if (i !== -1) file = args.splice(i, 2)[1];
const prefix = args[0] ?? '';

const s = loadSources(file);
for (const [id, f] of Object.entries(s.facts)) {
  if (!id.startsWith(prefix)) continue;
  console.log([id, formatFact(f.value, f.unit), f.label, f.source.name].join('\t'));
}
