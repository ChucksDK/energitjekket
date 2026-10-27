import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { REPO_ROOT, SOCIAL_ROOT } from '../lib/paths.js';
import { slideHtml } from '../templates/slides.js';
import { checkLayout, LayoutError } from './layout-check.js';
import { SIZES, withPage, loadSlide } from './png.js';

const run = promisify(execFile);

export const CROSSFADE = 0.3; // s
const MIN_TOTAL = 10;
const MAX_TOTAL = 20;
const FINAL_T = 60; // langt efter alle animationer

const words = (s) => String(s ?? '').split(/\s+/).filter(Boolean).length;

/** Varighed i sekunder: clamp(2,5 + ord*0,25; 2,5 .. 5). */
export function slideDuration(slide) {
  const parts = [slide.title, slide.value, slide.body, slide.cta];
  for (const k of slide.kpis || []) parts.push(k.label, k.value, k.unit);
  const n = parts.reduce((sum, p) => sum + words(p), 0);
  return Math.min(5, Math.max(2.5, 2.5 + n * 0.25));
}

/** Selve .slide-elementet fra et slideHtml-dokument. */
export const slideBody = (html) => html.slice(html.indexOf('<div class="slide '), html.lastIndexOf('<script>'));

const da = (n) => n.toFixed(1).replace('.', ',');

async function ffprobeDuration(file) {
  const { stdout } = await run('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', file]);
  return Number(stdout.trim());
}

/**
 * Renderer en short til MP4 (1080x1920, fps billeder/s) med musik.
 * opts: { fps=30, audioDir=social/audio, baseDir, elpris }
 */
export async function renderShort(post, outPath, opts = {}) {
  const fps = opts.fps ?? 30;
  const audioDir = opts.audioDir ?? path.join(SOCIAL_ROOT, 'audio');

  if (!post.audio) throw new Error(`Short ${post.id} mangler feltet audio`);
  if (/[\\/]/.test(post.audio) || post.audio.includes('..')) throw new Error(`Ugyldigt lydfilnavn: ${post.audio} (kun filnavn, ingen sti)`);
  const audioFile = path.join(audioDir, post.audio);
  if (!fs.existsSync(audioFile)) throw new Error(`Lydfil mangler: ${path.relative(REPO_ROOT, audioFile)}`);

  const durs = post.slides.map(slideDuration);
  const starts = durs.map((_, i) => durs.slice(0, i).reduce((a, d) => a + d - CROSSFADE, 0));
  const total = starts[starts.length - 1] + durs[durs.length - 1];
  if (total < MIN_TOTAL || total > MAX_TOTAL) {
    throw new Error(`Shortens samlede længde er ${da(total)} s, men skal være mellem ${MIN_TOTAL} og ${MAX_TOTAL} s`);
  }
  const audioDur = await ffprobeDuration(audioFile);
  if (audioDur + 0.05 < total) {
    throw new Error(`Lydfilen ${post.audio} er ${da(audioDur)} s, men shorten er ${da(total)} s`);
  }

  const htmls = post.slides.map((slide, index) =>
    slideHtml(slide, {
      index,
      total: post.slides.length,
      format: 'short',
      elpris: opts.elpris,
      targetUrl: post.target_url,
      baseDir: opts.baseDir,
      screenshotPath:
        slide.layout === 'screenshot' ? path.join(opts.baseDir ?? path.dirname(outPath), 'screens', `${slide.screenshot}.png`) : undefined,
    }),
  );
  // Sluttilstanden skal være pæn, før der tages et eneste billede.

  const frames = fs.mkdtempSync(path.join(os.tmpdir(), 'short-frames-'));
  try {
    await withPage(
      async (page) => {
        for (const [i, html] of htmls.entries()) {
          await loadSlide(page, html);
          await page.evaluate((t) => window.seek(t), FINAL_T);
          const issues = await checkLayout(page);
          if (issues.length) throw new LayoutError(issues, `${post.id} slide ${i + 1}/${htmls.length}`);
        }

        const nFrames = Math.round(total * fps);
        const ends = durs.map((d, i) => starts[i] + d);
        let loaded = -1;
        for (let n = 0; n < nFrames; n += 1) {
          const g = n / fps;
          // Ejeren er første slide, der endnu ikke er færdigt; det næste ligger under under krydsfaden.
          let i = ends.findIndex((e) => g < e - 1e-9);
          if (i < 0) i = htmls.length - 1;
          if (i !== loaded) {
            await loadSlide(page, htmls[i]);
            if (i < htmls.length - 1) await page.evaluate((m) => window.mountNext(m), slideBody(htmls[i + 1]));
            loaded = i;
          }
          const k = i < htmls.length - 1 ? g - starts[i + 1] : -1; // sekunder inde i krydsfaden
          await page.evaluate(
            ([t, nextT, opacity]) => {
              window.seek(t);
              if (nextT !== null) window.seekNext(nextT);
              window.setFade(opacity);
            },
            [g - starts[i], k >= 0 ? k : null, k >= 0 ? 1 - Math.min(1, k / CROSSFADE) : 1],
          );
          await page.screenshot({ path: path.join(frames, `${String(n + 1).padStart(5, '0')}.png`) });
        }
      },
      SIZES.short,
    );

    fs.mkdirSync(path.dirname(outPath), { recursive: true });
    await run('ffmpeg', [
      '-v', 'error', '-y',
      '-framerate', String(fps), '-i', path.join(frames, '%05d.png'),
      '-i', audioFile,
      '-shortest',
      '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', String(fps),
      '-c:a', 'aac',
      '-af', `afade=t=out:st=${(total - 1).toFixed(3)}:d=1`,
      '-movflags', '+faststart',
      outPath,
    ]);
    return outPath;
  } finally {
    fs.rmSync(frames, { recursive: true, force: true });
  }
}
