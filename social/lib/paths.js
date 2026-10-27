import path from 'node:path';
import { fileURLToPath } from 'node:url';

const LIB_DIR = path.dirname(fileURLToPath(import.meta.url));

export const SOCIAL_ROOT = path.resolve(LIB_DIR, '..');
export const REPO_ROOT = path.resolve(SOCIAL_ROOT, '..');
