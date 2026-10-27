// Tjek på tværs af ugens opslag (før noget renderes). Fejl rapporteres pr. opslag i errors.json.
const SLOT = /^(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2})$/;
const TIME = { carousel: '07:30', short: '19:30' };

const weekday = (date) => new Date(`${date}T12:00:00Z`).getUTCDay();

/** Returnerer en liste af fejl pr. opslag (samme rækkefølge som posts). */
export function weekErrors(posts) {
  const errs = posts.map(() => []);
  const bySlot = new Map();
  posts.forEach((post, i) => {
    const m = SLOT.exec(String(post?.slot));
    if (!m) return; // formatfejlen rapporteres af build-week
    const [, date, time] = m;
    const id = typeof post.id === 'string' ? post.id : '';
    if (!id.startsWith(`${date}-`)) errs[i].push(`id ${id || '(uden id)'} passer ikke til slot-datoen ${date} (id skal være ${date}-am eller ${date}-pm)`);
    if (TIME[post.type] && time !== TIME[post.type]) errs[i].push(`${post.type} skal ligge kl. ${TIME[post.type]} (slot er ${post.slot})`);
    if (weekday(date) === 5 && time === '19:30') {
      errs[i].push('fredag kl. 19:30 er reserveret til elpris-reelen (elpris-story.js --reel køres fredag efter 13:45); flyt opslaget');
    }
    if (!bySlot.has(post.slot)) bySlot.set(post.slot, []);
    bySlot.get(post.slot).push(i);
  });
  for (const [slot, idx] of bySlot) {
    if (idx.length < 2) continue;
    const ids = idx.map((i) => posts[i].id ?? '(uden id)').join(', ');
    for (const i of idx) errs[i].push(`slot ${slot} er brugt af flere opslag: ${ids}`);
  }
  return errs;
}
