import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { chromium } from 'playwright';
import { SOCIAL_ROOT } from '../lib/paths.js';
import { slideHtml } from '../templates/slides.js';

export const SIZES = { carousel: { width: 1080, height: 1350 }, story: { width: 1080, height: 1920 }, short: { width: 1080, height: 1920 } };

const TMP = path.join(SOCIAL_ROOT, 'out', '.tmp');

// Én delt Chromium så længe mindst én withPage/withBrowser kører.
let browserPromise = null;
let users = 0;

async function acquire() {
  users += 1;
  if (!browserPromise) browserPromise = chromium.launch();
  try {
    return await browserPromise;
  } catch (e) {
    users -= 1;
    browserPromise = null;
    throw e;
  }
}

async function release() {
  users -= 1;
  if (users === 0 && browserPromise) {
    const p = browserPromise;
    browserPromise = null;
    await (await p).close();
  }
}

/** Holder browseren åben på tværs af flere withPage-kald. */
export async function withBrowser(fn) {
  await acquire();
  try {
    return await fn();
  } finally {
    await release();
  }
}

/** Kører fn(page) på en side i den givne størrelse (deviceScaleFactor 1). */
export async function withPage(fn, { width = 1080, height = 1350 } = {}) {
  const browser = await acquire();
  let context;
  try {
    context = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: 1 });
    const page = await context.newPage();
    return await fn(page);
  } finally {
    if (context) await context.close();
    await release();
  }
}

/** Indlæser slide-HTML fra en fil (så file://-fonte og -billeder må hentes) og venter på fitText. */
export async function loadSlide(page, html) {
  fs.mkdirSync(TMP, { recursive: true });
  const file = path.join(TMP, `slide-${process.pid}-${Date.now()}-${Math.random().toString(36).slice(2)}.html`);
  fs.writeFileSync(file, html);
  try {
    await page.goto(pathToFileURL(file).href);
    await page.waitForFunction(() => document.documentElement.dataset.ready === '1', null, { timeout: 15000 });
  } finally {
    fs.rmSync(file, { force: true });
  }
}

/**
 * Renderer alle slides i en carousel til outDir/<post.id>-01.png …
 * opts: { elpris?, baseDir? } – baseDir er ugemappen (assets/, screens/).
 */
export async function renderCarousel(post, outDir, opts = {}) {
  fs.mkdirSync(outDir, { recursive: true });
  const total = post.slides.length;
  return withPage(async (page) => {
    const files = [];
    for (const [index, slide] of post.slides.entries()) {
      const screenshotPath =
        slide.layout === 'screenshot' ? path.join(opts.baseDir ?? outDir, 'screens', `${slide.screenshot}.png`) : undefined;
      const html = slideHtml(slide, {
        index,
        total,
        format: 'carousel',
        elpris: opts.elpris,
        targetUrl: post.target_url,
        baseDir: opts.baseDir,
        screenshotPath,
      });
      await loadSlide(page, html);
      const file = path.join(outDir, `${post.id}-${String(index + 1).padStart(2, '0')}.png`);
      await page.screenshot({ path: file });
      files.push(file);
    }
    return files;
  }, SIZES.carousel);
}
