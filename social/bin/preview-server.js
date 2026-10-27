#!/usr/bin/env node
// Serverer out/<uge>/ på 127.0.0.1:8787. Eneste skrivende rute: POST /approve {id, approved}.
import fs from 'node:fs';
import http from 'node:http';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { SOCIAL_ROOT } from '../lib/paths.js';
import { loadConfig, readJson, readManifest, writeJsonAtomic, writeSchedule } from '../lib/schedule.js';

const TYPES = {
  '.html': 'text/html; charset=utf-8', '.json': 'application/json; charset=utf-8', '.txt': 'text/plain; charset=utf-8',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.mp4': 'video/mp4',
};
const MAX_BODY = 4096;

export function startServer(weekDir, { port = 8787, requireApproval = true } = {}) {
  const root = fs.realpathSync(weekDir);

  const send = (res, status, body, type = 'text/plain; charset=utf-8', extra = {}) => {
    res.writeHead(status, { 'Content-Type': type, 'Cache-Control': 'no-store', ...extra });
    res.end(body);
  };

  const serveStatic = (req, res) => {
    let rel;
    try {
      rel = decodeURIComponent(new URL(req.url, 'http://x').pathname);
    } catch {
      return send(res, 400, 'Ugyldig sti');
    }
    if (rel.includes('\0')) return send(res, 400, 'Ugyldig sti');
    if (rel === '/') rel = '/preview.html';
    const file = path.resolve(root, `.${rel}`);
    let real;
    try {
      real = fs.realpathSync(file);
    } catch {
      return send(res, 404, 'Ikke fundet');
    }
    if (real !== root && !real.startsWith(root + path.sep)) return send(res, 404, 'Ikke fundet');
    const st = fs.statSync(real);
    if (!st.isFile()) return send(res, 404, 'Ikke fundet');
    const type = TYPES[path.extname(real).toLowerCase()] || 'application/octet-stream';
    const m = /^bytes=(\d*)-(\d*)$/.exec(req.headers.range || '');
    if (m && (m[1] || m[2])) {
      let start = m[1] === '' ? Math.max(0, st.size - Number(m[2])) : Number(m[1]);
      let end = m[1] === '' || m[2] === '' ? st.size - 1 : Math.min(Number(m[2]), st.size - 1);
      if (start > end || start >= st.size) return send(res, 416, 'Ugyldigt interval', 'text/plain', { 'Content-Range': `bytes */${st.size}` });
      res.writeHead(206, { 'Content-Type': type, 'Content-Length': end - start + 1, 'Content-Range': `bytes ${start}-${end}/${st.size}`, 'Accept-Ranges': 'bytes' });
      return req.method === 'HEAD' ? res.end() : fs.createReadStream(real, { start, end }).pipe(res);
    }
    res.writeHead(200, { 'Content-Type': type, 'Content-Length': st.size, 'Accept-Ranges': 'bytes', 'Cache-Control': 'no-store' });
    return req.method === 'HEAD' ? res.end() : fs.createReadStream(real).pipe(res);
  };

  const approve = (req, res) => {
    const origin = req.headers.origin;
    const addr = server.address();
    if (origin && !new Set([`http://127.0.0.1:${addr.port}`, `http://localhost:${addr.port}`]).has(origin)) {
      return send(res, 403, 'Forkert origin');
    }
    if (!/^application\/json\b/i.test(req.headers['content-type'] || '')) return send(res, 415, 'Kræver application/json');
    let body = '';
    let tooBig = false;
    req.on('data', (c) => {
      body += c;
      if (body.length > MAX_BODY) {
        tooBig = true;
        req.destroy();
      }
    });
    req.on('end', () => {
      if (tooBig) return;
      let data;
      try {
        data = JSON.parse(body);
      } catch {
        return send(res, 400, 'Ugyldig JSON');
      }
      if (!data || typeof data.id !== 'string' || typeof data.approved !== 'boolean') {
        return send(res, 400, 'Forventer {id: tekst, approved: boolean}');
      }
      if (!readManifest(root).some((p) => p.id === data.id)) return send(res, 404, `Ukendt opslag: ${data.id}`);
      const file = path.join(root, 'approvals.json');
      const approvals = readJson(file, {});
      approvals[data.id] = data.approved;
      writeJsonAtomic(file, approvals);
      const schedule = writeSchedule(root, { requireApproval });
      send(res, 200, JSON.stringify({ ok: true, scheduled: schedule.map((s) => s.id) }), 'application/json; charset=utf-8');
    });
  };

  const server = http.createServer((req, res) => {
    try {
      const pathname = new URL(req.url, 'http://x').pathname;
      if (pathname === '/approve') {
        return req.method === 'POST' ? approve(req, res) : send(res, 405, 'Kun POST', 'text/plain', { Allow: 'POST' });
      }
      if (req.method === 'GET' || req.method === 'HEAD') return serveStatic(req, res);
      return send(res, 405, 'Metode ikke tilladt');
    } catch (e) {
      return send(res, 500, `Serverfejl: ${e.message}`);
    }
  });
  return new Promise((resolve, reject) => {
    server.once('error', reject);
    server.listen(port, '127.0.0.1', () => resolve(server));
  });
}

async function main(argv) {
  let week;
  let port = 8787;
  let outRoot = path.join(SOCIAL_ROOT, 'out');
  for (let i = 0; i < argv.length; i += 1) {
    if (argv[i] === '--port') port = Number(argv[++i]);
    else if (argv[i] === '--out-root') outRoot = path.resolve(argv[++i]);
    else if (!week) week = argv[i];
    else throw new Error(`Ukendt argument: ${argv[i]}`);
  }
  if (!week) throw new Error('Brug: node social/bin/preview-server.js <uge> [--port N]');
  if (!Number.isInteger(port) || port < 0 || port > 65535) throw new Error('Ugyldig port');
  const weekDir = path.join(outRoot, week);
  if (!fs.existsSync(path.join(weekDir, 'manifest.json'))) throw new Error(`Ugen er ikke bygget: ${weekDir}`);
  const server = await startServer(weekDir, { port, requireApproval: loadConfig().require_approval });
  console.log(`Preview: http://127.0.0.1:${server.address().port}/  (Ctrl+C for at stoppe)`);
}

if (import.meta.url === pathToFileURL(process.argv[1] ?? '').href) {
  main(process.argv.slice(2)).catch((e) => {
    console.error(e.message);
    process.exit(1);
  });
}
