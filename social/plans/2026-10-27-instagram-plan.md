# Energitjekket Instagram Production – Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A JS toolchain in `social/` that turns Grok's weekly brief into 14 validated, layout-checked Instagram posts (PNG carousels + MP4 shorts) in style A, a preview page where Casper approves them, and a daily elpris story script.

**Architecture:** A Python exporter turns the repo's own data (`src/*.py`, `src/elpris_data.json`) plus a short hand list of site-verified facts into one source register (`social/data/sources.json`). Brief text never contains digits; it contains `{fact.id}` placeholders that the renderer fills from the register, so no number can be made up. HTML templates in style A are rendered with Playwright to PNG (and frame-by-frame to MP4 via ffmpeg), and every rendered slide passes an automatic layout check (no overlap, no overflow, no wrapped numbers) before it reaches the weekly preview.

**Tech Stack:** Node 24 (ESM, `node --test`), `playwright` (Chromium already in `~/Library/Caches/ms-playwright`), ffmpeg 8, Python 3 for the exporter (`unittest`).

**Spec:** `social/2026-10-27-instagram-design.md` (reference look: `social/reference/style-mockup-a-v2.html`).

## Global Constraints

- All post text is Danish. No voiceover.
- Colors: `#0b4f43` dark green, `#0f6b55` green, `#f5b700` yellow (only the single most important word/number per slide), `#f2f8f5`/`#e7f2ee` mint, `#13201d` text, `#4f5e5a` muted, `#e1e8e5` lines, `#c0392b` for "dyrest" bars only.
- Sizes: carousel 1080×1350, story/short 1080×1920. Safe margin 66 px on every side.
- Every slide: top = tag pill; middle = content; bottom = source line + `@energitjekket` (+ `Swipe →` on carousel slides that are not last). No absolutely positioned text.
- Numbers never wrap (`white-space:nowrap`); unit on its own line in KPI boxes. Text never clipped.
- No digit may appear in brief text (slides or caption) except inside `{fact.id}` placeholders and four-digit years 2020–2035.
- Banned in slide text and captions (case-insensitive): `!`, `book nu`, `begrænset`, `skynd dig`, `gratis`, `garanti`, `kun i dag`, `spar op til`. The words `tilbud`/`få tilbud` and any URL under `/tilbud/` are allowed only when `post.quote === true`.
- Every `target_url` starts with `https://energitjekket.dk/`.
- Carousel: 5–7 slides. Short: 3–6 slides, 10–20 s total, 30 fps.
- Slots: 07:30 carousel, 19:30 short, Europe/Copenhagen.
- Write output only under `social/out/` (git-ignored). Do not modify `src/`, `site/`, `deploy/` or `src/refresh_elpris.py`.
- Commit on local branch `social-instagram`; never push (pushing main deploys to Vercel).

## Review Focus

1. **The brief references a fact ID that doesn't exist, e.g. a city not yet in the register.** The expected behavior is that the post is rejected with the missing ID named, and the rest of the week still builds. Test: `build-week continues past an invalid post` (Task 9).
2. **Long Danish words, e.g. "landsgennemsnit" or "Varmepumpepuljen", in narrow KPI boxes.** The text shrinks down to the minimum size, and if it still doesn't fit the layout check fails. It must never be clipped. Test: `fitText shrinks then layout check flags overflow at min size` (Task 5).
3. **`elpris_data.json` has today's prices but not tomorrow's when the story runs.** The script exits 3 and writes no PNG. It never falls back to today's prices. Test: `story exits 3 when target day missing` (Task 8).
4. **Negative or zero spot prices.** Bars stay inside the chart and "0,00 kr."/"-0,05 kr." format correctly. Tests: `formatFact handles negative kr_per_kwh` (Task 1) and `bars chart clamps negative values to baseline` (Task 4).
5. **A short with no audio file present** (`social/audio/` ships empty, and Casper adds the tracks). The renderer fails with a clear message naming the missing file, rather than making a silent MP4. Test: `renderShort rejects missing audio` (Task 6).

---

### Task 1: Scaffold and Danish number formatting

**Files:**
- Create: `social/package.json`, `social/.gitignore`, `social/lib/format.js`
- Test: `social/test/format.test.js`

**Interfaces:**
- Produces: `formatFact(value: number, unit: Unit): string` where `Unit = 'kr'|'kr_per_kwh'|'kwh'|'kwh_per_kwp'|'pct'|'hour'|'m2'|'kwp'|'count'|'scop'`.

- [ ] **Step 1:** Create `social/package.json` (`"type":"module"`, `"private":true`, dependency `"playwright": "1.48.2"`, scripts `"test": "node --test test/"`), `social/.gitignore` with `out/`, `node_modules/`, `data/sources.json`. Run `cd social && npm install`. Expected: installs without downloading browsers (set `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1` if it tries; an existing Chromium build is used via `chromium.launch()`, and if the version mismatches pick the closest matching playwright version for the cached `chromium-1140`…`1248` builds).
- [ ] **Step 2: Write the failing test** `social/test/format.test.js`:
```js
assert.equal(formatFact(32388,'kr'),'32.388 kr.');
assert.equal(formatFact(0.2418,'kr_per_kwh'),'0,24 kr.');
assert.equal(formatFact(-0.05,'kr_per_kwh'),'-0,05 kr.');   // formatFact handles negative kr_per_kwh
assert.equal(formatFact(986,'kwh_per_kwp'),'986 kWh');
assert.equal(formatFact(48.4,'pct'),'48 %');
assert.equal(formatFact(6,'hour'),'kl. 06');
assert.equal(formatFact(130,'m2'),'130 m²');
assert.equal(formatFact(3.5,'scop'),'3,5');
assert.equal(formatFact(18100,'kwh'),'18.100 kWh');
```
- [ ] **Step 3:** Run `cd social && npm test`. Expected: FAIL (module not found).
- [ ] **Step 4:** Implement `formatFact` in `social/lib/format.js` with `Intl.NumberFormat('da-DK')`; `kr` 0 decimals, `kr_per_kwh` 2 decimals, `pct` 0 decimals, `scop` 1 decimal, `hour` zero-padded. Unknown unit throws.
- [ ] **Step 5:** Run `npm test`. Expected: PASS.
- [ ] **Step 6:** Commit `git checkout -b social-instagram && git add social && git commit -m "social: scaffold + Danish number formatting"`.

### Task 2: Source register

**Files:**
- Create: `social/data/export_sources.py`, `social/data/manual_facts.json`, `social/lib/sources.js`, `social/bin/facts.js`
- Test: `social/data/test_export_sources.py`, `social/test/sources.test.js`

**Interfaces:**
- Produces `social/data/sources.json`: `{ "generated": ISO, "facts": { [id]: { value:number, unit:Unit, label:string, source:{name,url} } }, "elpris": { [date]: { DK1:{hours:number[24]}, DK2:{...} } } }`.
- Produces `loadSources(path?: string): Sources`, `getFact(sources, id): Fact` (throws `Error('Ukendt fakta-id: <id>')`).
- Produces CLI `node social/bin/facts.js [prefix]` printing `id<TAB>formatted<TAB>label<TAB>source` lines (Grok's lookup).

Fact IDs (exact):
- From `src/data_local_gen.py` for every key in `PV` (the 11 cities + any added later): `pv.<city>.syd` (unit `kwh_per_kwp`), `pv.<city>.month.<1..12>` (`kwh_per_kwp`, monthly). Source name `PVGIS 5.3 (EU JRC)`, url = that city's `url_syd`.
- From `HEAT`: `heat.<city>.fjernvarme_pct` = FJ/sum(all codes)·100 and `heat.<city>.varmepumpe_pct` = VP/sum·100 (unit `pct`). Only FJ and VP — other codes' meanings aren't documented in the repo. Source `Danmarks Statistik BOL102 (2026)`, url `https://www.statbank.dk/BOL102`.
- From `src/elpris_data.json`, for every day and area: `elpris.<YYYY-MM-DD>.<DK1|DK2>.billigste_time` (`hour`), `.billigste_pris`, `.dyreste_time`, `.dyreste_pris`, `.gns_pris` (`kr_per_kwh`, hourly average of the quarter-hour `spot` values, i.e. 4 quarters per hour). Also store the 24 hourly averages under `elpris`. Source `Energi Data Service (Energinet), spotpris`, url `https://www.energidataservice.dk/`.
- From `social/data/manual_facts.json`: `[{id, value, unit, label, source_key, site_text}]`, where `source_key` is a key in `src/data.py` `S` (source name/url taken from there). Initial entries: `bolius.hus.m2` 130, `bolius.hus.kwh` 18100, `bolius.oliefyr` 32388, `bolius.gasfyr` 18433, `bolius.elradiator` 30974, `bolius.fjernvarme` 16953, `bolius.ltv_radiator` 9386, `bolius.ltv_gulvvarme` 7288, `bolius.jordvarme_radiator` 8725, `bolius.jordvarme_gulvvarme` 6960 (all `source_key: "bolius_varme"`, `site_text` = the formatted string, e.g. `"32.388 kr."`), `beregner.scop` 3.5 and `beregner.elpris_dk1` 1.45, `beregner.elpris_dk2` 1.55, `beregner.anlaeg_kwp` 6, `beregner.egetforbrug_pct` 35, each with its source key as used on `/beregner/`.

- [ ] **Step 1: Write the failing Python test** `test_export_sources.py`: `pv.aalborg.syd` exists with unit `kwh_per_kwp` and value equal to `data_local_gen.PV['aalborg']['syd']`; `len([k for k in facts if k.startswith('pv.kolding.month.')]) == 12`; `elpris.2026-10-27.DK1.billigste_time` value is 6 for the committed `elpris_data.json`; a manual fact whose `site_text` is absent from every `site/**/*.html` makes `build_register()` raise `ValueError` naming the id.
- [ ] **Step 2:** Run `python3 -m unittest social/data/test_export_sources.py`. Expected: FAIL.
- [ ] **Step 3:** Implement `build_register(repo_root: Path) -> dict` and `main()` (writes `social/data/sources.json`) in `export_sources.py`, importing `src/` modules via `sys.path`.
- [ ] **Step 4:** Run the Python test. Expected: PASS.
- [ ] **Step 5: Write the failing JS test** `sources.test.js`: `getFact(s,'bolius.oliefyr').value === 32388`; `getFact(s,'nope')` throws `/Ukendt fakta-id: nope/`; `facts.js bolius` stdout contains `bolius.oliefyr\t32.388 kr.`.
- [ ] **Step 6:** Implement `sources.js` and `bin/facts.js`; run `python3 social/data/export_sources.py && npm test`. Expected: PASS.
- [ ] **Step 7:** Commit `social: source register from repo data`.

### Task 3: Brief schema, placeholder resolution and copy rules

**Files:**
- Create: `social/lib/brief.js`, `social/test/fixtures/brief-valid.json`, `social/test/fixtures/brief-bad.json`
- Test: `social/test/brief.test.js`

**Interfaces:**
- Consumes: `getFact`, `formatFact`.
- Produces brief format (also documented in PLAYBOOK):
```json
{ "week": "2026-W45",
  "posts": [{ "id": "2026-11-02-am", "slot": "2026-11-02T07:30", "type": "carousel|short",
    "pillar": "varmepumpe|solceller|by|quiz|mix", "city": "viborg", "quote": false,
    "target_url": "https://energitjekket.dk/beregner/", "audio": "rolig-01.mp3",
    "slides": [{ "layout": "cover|stat|kpi2|bars|text|screenshot|end",
      "tag": "VARMEPUMPE", "title": "Har du oliefyr? Så betaler du ca.",
      "value": "{bolius.oliefyr}", "body": "om året for varme i et {bolius.hus.m2} hus.",
      "highlight": "{bolius.oliefyr}", "kpis": [{"label":"Oliefyr","value":"{bolius.oliefyr}","unit":"kr./år"}],
      "bars": {"date":"2026-10-28","area":"DK1"}, "screenshot": "beregner", "bg": "assets/cover.png" }],
    "caption": "…", "hashtags": ["#varmepumpe"] }] }
```
- Produces `resolveText(text: string, sources): {text: string, factIds: string[]}` (formats `{id}` via `formatFact`, and the KPI `value` is formatted without its unit when `kpis[].unit` is given), and `validatePost(post, sources): string[]` (Danish error messages; empty = valid), `resolvePost(post, sources): ResolvedPost` (all text resolved; each slide gets `sources: string[]` = unique source names of its facts).

- [ ] **Step 1: Write failing tests** in `brief.test.js`:
  - `resolveText('ca. {bolius.oliefyr}', s).text === 'ca. 32.388 kr.'`
  - `validatePost` on a slide title `'Spar 30.000 kr.'` → errors include `tal uden kilde: "30.000"`
  - title containing `'2028'` → no digit error (year allowed)
  - caption containing `'!'` → error `forbudt: "!"`
  - `quote:false` with `target_url` `https://energitjekket.dk/solceller/tilbud/` → error mentioning `tilbud`
  - `target_url` `https://example.com/` → error
  - carousel with 4 slides → error; short with 7 slides → error
  - `bg` on slide index 1 → error (`bg kun på første slide`)
  - title over 60 chars, body over 160 chars, tag over 24 chars → one error each
  - unknown fact id → error `Ukendt fakta-id`
  - `fixtures/brief-valid.json` (one carousel using the oil-boiler copy from the mockup, one short) → `[]` for both posts.
- [ ] **Step 2:** Run `npm test`. Expected: FAIL.
- [ ] **Step 3:** Implement `brief.js`. Digit check: strip `{…}` placeholders and `\b20(2\d|3[0-5])\b`, then any `\d` is an error quoting the number run.
- [ ] **Step 4:** Run `npm test`. Expected: PASS.
- [ ] **Step 5:** Commit `social: brief validation and fact placeholders`.

### Task 4: Style A slide templates and PNG carousel render

**Files:**
- Create: `social/templates/base.css`, `social/templates/slides.js`, `social/templates/runtime.js` (in-page: `fitText`), `social/render/png.js`
- Test: `social/test/render-png.test.js`

**Interfaces:**
- Consumes: `ResolvedPost`, `sources.elpris`.
- Produces `slideHtml(slide: ResolvedSlide, ctx: {index:number, total:number, format:'carousel'|'story'|'short', elpris?}): string` (full HTML doc, inlines `base.css` + `runtime.js`, fonts from `src/fonts/` via `file://`; the mockup's Inter/system-ui is replaced by DejaVu Sans to match `src/visuals.py`). Produces `renderCarousel(post: ResolvedPost, outDir: string): Promise<string[]>` → `outDir/<post.id>-01.png` …. `withPage(fn)` helper shared by later tasks (one browser, page sized to the format at deviceScaleFactor 1).
- Layouts follow `social/reference/style-mockup-a-v2.html` scaled ×(1080/324): `cover` (dark green bg, yellow tag, title, big yellow value, body), `stat` (mint bg, title, big value, body), `kpi2` (two KPI boxes, unit line under value), `bars` (24 hourly bars from `sources.elpris[date][area].hours`: cheapest 3 hours yellow, dearest 3 red, rest `#0f6b55`; values ≤0 drawn as a 2 px baseline stub), `text` (title + body), `screenshot` (phone frame with image from Task 7), `end` (link CTA box: `Regn på dit eget hus → energitjekket.dk/…` built from `target_url` path). The tag gets ` · i/n` appended automatically. `bg` on the cover = image with `linear-gradient(rgba(11,79,67,.15),rgba(11,79,67,.85))` overlay.
- `fitText(el, minPx)` in runtime.js: while `el.scrollWidth > el.clientWidth || el.scrollHeight > el.clientHeight` and font-size > minPx, shrink by 2 px. Mins: title 40 px, value 72 px, body 28 px, KPI value 44 px (at 1080 width).

- [ ] **Step 1: Write failing test**: rendering `brief-valid.json` post 1 creates 5–7 PNGs; each is 1080×1350 (read the PNG header bytes 16–24); and `bars chart clamps negative values to baseline`: a `bars` slide with an injected `hours` array containing `-0.3` renders with every `.bars i` element's bounding box inside the `.bars` container (query via `page.evaluate` on `slideHtml` output).
- [ ] **Step 2:** Run. Expected: FAIL.
- [ ] **Step 3:** Implement templates and `renderCarousel`.
- [ ] **Step 4:** Run `npm test`. Expected: PASS. Then open `social/out/test/*.png` and compare by eye with `social/reference/style-mockup-a-v2.html`. Colors, hierarchy and bottom bar should match.
- [ ] **Step 5:** Commit `social: style A templates + carousel PNG render`.

### Task 5: Automatic layout check

**Files:**
- Create: `social/render/layout-check.js`
- Modify: `social/render/png.js` (run the check before each screenshot; throw `LayoutError` with issues)
- Test: `social/test/layout-check.test.js`

**Interfaces:**
- Produces `checkLayout(page): Promise<Issue[]>`, `Issue = {kind:'outside'|'overlap'|'wrap', text:string}`; `class LayoutError extends Error { issues: Issue[] }`.
- Rules (run in page): collect every text node's client rects (Range API). `outside`: rect beyond its nearest `.box`/`.kpi`/`.slide-safe` container (66 px safe margin) by >0.5 px. `overlap`: two rects intersect by >2 px in both axes, unless both belong to the same block element (multi-line heading). Text vs. `.bars` and `.cta` elements counts too. `wrap`: any `.value`/`.kpi .v` element with more than one client rect line.

- [ ] **Step 1: Write failing tests**: a hand-written HTML with a `.cta` placed over a source line → one `overlap`; a KPI box 200 px wide with value `"32.388"` at 90 px → `fitText shrinks then layout check flags overflow at min size` (after `fitText` it reaches 44 px and still overflows → `outside`); `brief-valid.json` slides → `[]`.
- [ ] **Step 2:** Run. Expected: FAIL.
- [ ] **Step 3:** Implement and wire into `renderCarousel`.
- [ ] **Step 4:** Run `npm test`. Expected: PASS.
- [ ] **Step 5:** Commit `social: layout check (overlap, overflow, wrap)`.

### Task 6: Short (MP4) renderer

**Files:**
- Create: `social/render/short.js`, `social/audio/README.md`
- Test: `social/test/render-short.test.js`

**Interfaces:**
- Consumes: `slideHtml(…, {format:'short'})`, `checkLayout`, `withPage`.
- Produces `renderShort(post: ResolvedPost, outPath: string, opts?: {fps?:30}): Promise<string>`.
- Approach: one page per slide at 1080×1920; `runtime.js` exposes `window.seek(t)` which sets the animation state (values count up from 0 over 0.8 s with ease-out; bars grow over 0.8 s staggered 20 ms; text fades/slides up 24 px over 0.3 s). Before frame capture, run `seek(final)` and `checkLayout` on the final state. Slide duration = `clamp(2.5 + words*0.25, 2.5, 5)` s; total must land in 10–20 s or throw. Frames are captured with `page.screenshot` per frame into a temp dir; `ffmpeg -framerate 30 -i %05d.png -i audio/<post.audio> -shortest -c:v libx264 -pix_fmt yuv420p -c:a aac -af "afade=t=out:st=<dur-1>:d=1"`. 0.3 s crossfade between slides is done in-page by rendering the next slide underneath during the last 9 frames.
- `audio/README.md`: Casper drops rights-free tracks here (no lyrics, ≥20 s); brief `audio` names one.

- [ ] **Step 1: Write failing tests**: `renderShort rejects missing audio` → rejects with `/Lydfil mangler: social\/audio\/nope.mp3/`; with a 20 s silent track generated in the test (`ffmpeg -f lavfi -i anullsrc -t 20 test.mp3`), the valid fixture short yields an MP4 where `ffprobe` reports 1080×1920, 30 fps, duration 10–20 s, and an audio stream.
- [ ] **Step 2:** Run. Expected: FAIL.
- [ ] **Step 3:** Implement.
- [ ] **Step 4:** Run `npm test`. Expected: PASS. Watch the MP4 once.
- [ ] **Step 5:** Commit `social: animated short renderer`.

### Task 7: Live-site screenshots

**Files:**
- Create: `social/render/screenshot.js`
- Test: `social/test/screenshot.test.js`

**Interfaces:**
- Produces `PAGES = {beregner:'/beregner/', elpris:'/elpris/', 'by:<city>:solceller':'/solceller/<city>/', 'by:<city>:varmepumpe':'/varmepumpe/<city>/'}` and `shootPage(key: string, outPath: string, base='https://energitjekket.dk'): Promise<string>`. Viewport 390×844 at deviceScaleFactor 3, wait for `networkidle`, and hide the sticky mobile CTA (it would cover the content). Nothing else on the page is changed. The screenshot slide layout (Task 4) reads `social/out/<week>/screens/<key>.png`.

- [ ] **Step 1: Write failing test**: serve `site/` with `python3 -m http.server 8765` in the test (spawned and killed after). `shootPage('beregner', tmp, 'http://localhost:8765')` produces a 1170×2532 PNG. An unknown key rejects with `/Ukendt side/`.
- [ ] **Step 2:** Run. Expected: FAIL.
- [ ] **Step 3:** Implement.
- [ ] **Step 4:** Run `npm test`. Expected: PASS.
- [ ] **Step 5:** Commit `social: live-site screenshots`.

### Task 8: Daily elpris story and Friday reel

**Files:**
- Create: `social/bin/elpris-story.js`
- Modify: `README.md` (one paragraph in the "Elpris-rutinen" section: after `refresh_elpris.py` exits 0, run `python3 social/data/export_sources.py && node social/bin/elpris-story.js`; on Fridays also `--reel`)
- Test: `social/test/elpris-story.test.js`

**Interfaces:**
- Consumes: register, `slideHtml`, `renderCarousel`-style PNG path (story format), `renderShort`.
- CLI: `node social/bin/elpris-story.js [--date YYYY-MM-DD] [--reel] [--sources path] [--out dir]`. The default date is tomorrow (Europe/Copenhagen). It writes `social/out/stories/<date>/elpris-DK1.png` and `elpris-DK2.png` (1080×1920, one `bars` slide: tag `ELPRIS · <WEEKDAY> <d/m> · <area>`, title `Billigste time i morgen: {…billigste_time}` (the words "i morgen" only when the date is tomorrow; otherwise `Billigste time <weekday>:`), body with cheapest and dearest price, CTA `Se alle priser på energitjekket.dk/elpris`, source line). The Danish weekday is generated by the script, not taken from a brief. `--reel` additionally writes `reel-<date>.mp4` titled `Lørdagens billigste timer` (only allowed when the date is a Saturday), using the first file in `social/audio/` alphabetically unless `--audio` is given. Exit codes: 0 ok, 3 `date` not in `sources.elpris` (no files written), 4 render/layout failure.

- [ ] **Step 1: Write failing tests**: `--date 2026-10-27` with the committed data → exit 0 and two PNGs 1080×1920; `story exits 3 when target day missing` (`--date 2030-01-01`) → exit 3, out dir empty; `--reel --date 2026-10-27` (a Tuesday) → exit 4 with message `kun lørdag`.
- [ ] **Step 2:** Run. Expected: FAIL.
- [ ] **Step 3:** Implement and add the README paragraph.
- [ ] **Step 4:** Run `npm test`. Expected: PASS.
- [ ] **Step 5:** Commit `social: daily elpris story + Saturday reel`.

### Task 9: Weekly build, preview and approval

**Files:**
- Create: `social/bin/build-week.js`, `social/bin/preview-server.js`, `social/templates/preview.html.js`
- Test: `social/test/build-week.test.js`

**Interfaces:**
- Consumes: everything above.
- `node social/bin/build-week.js social/briefs/<week>.json` → runs the exporter first, then for every post: `validatePost` → `resolvePost` → shoots needed screenshots → render (carousel/short) → writes `social/out/<week>/<post.id>/` with files + `caption.txt` (resolved caption + blank line + `Kilde: …` + hashtags). Failing posts are listed in `out/<week>/errors.json` (`[{id, errors[]}]`) and the run continues. Exit 0 if ≥1 post built, 1 otherwise. It also writes `preview.html` and `schedule.json` (initially `[]`).
- `node social/bin/preview-server.js <week>` serves `out/<week>/` on `localhost:8787`. The preview page shows the posts in slot order (date, time, type, all slides/video, caption, sources, errors in red) with Godkend/Afvis buttons that `POST /approve {id, approved}`. The server writes `approvals.json` and regenerates `schedule.json` = approved posts only, each `{id, slot, type, files:[abs paths], caption}`. Config `social/config.json` `{ "require_approval": true }`: when false, `build-week` writes every built post straight into `schedule.json`.

- [ ] **Step 1: Write failing tests**: `build-week continues past an invalid post` (brief with one valid carousel and one post using `{pv.nowhere.syd}`) → exit 0, the valid post's PNGs exist, `errors.json` names the bad id and `Ukendt fakta-id`; after `POST /approve {id:'…-am',approved:true}` → `schedule.json` has exactly that post; with `require_approval:false` → `schedule.json` contains the valid post without a request.
- [ ] **Step 2:** Run. Expected: FAIL.
- [ ] **Step 3:** Implement.
- [ ] **Step 4:** Run `npm test`. Expected: PASS. Build the fixture week and open the preview once by hand.
- [ ] **Step 5:** Commit `social: weekly build, preview and approval`.

### Task 10: Playbook for Grok and Claude

**Files:**
- Create: `social/PLAYBOOK.md`, `social/briefs/EXAMPLE-2026-W45.json` (a full 14-post example week that passes `build-week` with zero errors)
- Test: `social/test/example-week.test.js` (validates every post of the example brief → no errors)

**Content of PLAYBOOK.md (Danish):** the roles (Grok writes the brief by Sunday, Claude builds and humanizes the captions, Casper approves in the preview, Grok schedules `schedule.json` in Zernio at 07:30/19:30), the week plan table and pillar mix from the spec, the hard rules (numbers only as `{fact.id}`, find IDs with `node social/bin/facts.js <prefix>`, no sales talk, banned words, `tilbud` only when `quote:true`, no repeat of a city within 2 weeks or an angle within 3), the brief schema with one annotated example post per layout, the Higgsfield prompt rules (Danish homes/interiors, natural light, no faces toward the camera, no text in the image, no brand marks, cover/hook only, file into `social/out/<week>/assets/`), the caption rules (3–6 lines, "link i bio", the specific page, source line, 3–5 Danish hashtags, humanizer pass), and the commands in order. Elpris story: runs by script after 13:45, outputs in `social/out/stories/<date>/`, Grok schedules them.

- [ ] **Step 1:** Write the failing test (example brief must be fully valid and contain 14 posts: 7 carousels at 07:30 and 7 shorts at 19:30; ≥8 posts with pillar `varmepumpe` or city posts about varmepumpe, ≤6 solceller).
- [ ] **Step 2:** Run. Expected: FAIL.
- [ ] **Step 3:** Write `PLAYBOOK.md` and the example brief.
- [ ] **Step 4:** Run `npm test` and `node social/bin/build-week.js social/briefs/EXAMPLE-2026-W45.json`. Expected: tests pass, 14 posts are built, `errors.json` is empty, and no layout errors occur. (A short build needs one track in `social/audio/`; use a generated silent track for this check and delete it afterwards.)
- [ ] **Step 5:** Commit `social: playbook + example week`.
