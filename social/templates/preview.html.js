// Selvstændig preview-side for en uge. Ingen eksterne ressourcer.
const esc = (s) =>
  String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);

const DAYS = ['søndag', 'mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag'];
const MONTHS = ['januar', 'februar', 'marts', 'april', 'maj', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'december'];

/** "2026-11-02T07:30" -> "mandag 2. november 2026 kl. 07:30" (ingen tidszoneomregning). */
export function danishSlot(slot) {
  const m = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})/.exec(slot || '');
  if (!m) return String(slot);
  const [y, mo, d] = [Number(m[1]), Number(m[2]), Number(m[3])];
  const wd = DAYS[new Date(Date.UTC(y, mo - 1, d)).getUTCDay()];
  return `${wd} ${d}. ${MONTHS[mo - 1]} ${y} kl. ${m[4]}:${m[5]}`;
}

const TYPE = { carousel: 'Carousel', short: 'Short' };
const enc = (rel) => rel.split('/').map(encodeURIComponent).join('/');

function postHtml(p, approvals) {
  const media =
    p.type === 'short'
      ? p.files.map((f) => `<video controls preload="metadata" src="${esc(enc(f))}"></video>`).join('')
      : `<div class="row">${p.files.map((f) => `<img loading="lazy" src="${esc(enc(f))}" alt="">`).join('')}</div>`;
  const state = approvals[p.id] === true ? 'approved' : approvals[p.id] === false ? 'rejected' : '';
  const label = state === 'approved' ? 'Godkendt' : state === 'rejected' ? 'Afvist' : 'Afventer';
  return `<section class="post ${state}" data-id="${esc(p.id)}">
  <header><h2>${esc(danishSlot(p.slot))}</h2><span class="type">${TYPE[p.type] || esc(p.type)}</span><span class="id">${esc(p.id)}</span><span class="status">${label}</span></header>
  ${media}
  <pre class="caption">${esc(p.caption)}</pre>
  <p class="src">Kilder: ${p.sources.length ? esc(p.sources.join(', ')) : 'ingen'}</p>
  <div class="actions"><button class="ok" data-approve="true">Godkend</button><button class="no" data-approve="false">Afvis</button></div>
  <p class="note" hidden></p>
</section>`;
}

/**
 * posts: [{id, slot, type, files (relative), caption, sources[]}] i slot-rækkefølge
 * errors: [{id, errors[]}]; approvals: {id: boolean}
 */
export function previewHtml({ week, posts, errors = [], approvals = {} }) {
  const errHtml = errors.length
    ? `<section class="errors"><h2>Opslag der ikke blev bygget</h2>${errors
        .map((e) => `<div class="err"><strong>${esc(e.id)}</strong><ul>${e.errors.map((m) => `<li>${esc(m)}</li>`).join('')}</ul></div>`)
        .join('')}</section>`
    : '';
  return `<!doctype html>
<html lang="da"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Preview ${esc(week)}</title>
<style>
:root{--ink:#13201d;--muted:#4f5e5a;--line:#e1e8e5;--mint:#f2f8f5;--green:#0f6b55;--dark:#0b4f43;--red:#c0392b}
*{box-sizing:border-box}body{margin:0;background:var(--mint);color:var(--ink);font:16px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}
main{max-width:1100px;margin:0 auto;padding:24px 16px 64px}h1{color:var(--dark);margin:0 0 4px}.sub{color:var(--muted);margin:0 0 24px}
.post{background:#fff;border:1px solid var(--line);border-radius:12px;padding:20px;margin-bottom:24px}
.post.approved{border-color:var(--green);box-shadow:0 0 0 2px var(--green)}.post.rejected{opacity:.6}
header{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:baseline;margin-bottom:12px}h2{font-size:20px;margin:0;color:var(--dark)}
.type{background:var(--dark);color:#fff;border-radius:999px;padding:2px 12px;font-size:13px}.id{color:var(--muted);font-size:13px}.status{margin-left:auto;font-weight:600}
.row{display:flex;gap:12px;overflow-x:auto;padding-bottom:8px}.row img{height:420px;width:auto;border:1px solid var(--line);border-radius:8px;flex:none}
video{max-height:560px;max-width:100%;border-radius:8px;background:#000}
.caption{white-space:pre-wrap;font:inherit;background:var(--mint);border-radius:8px;padding:12px;margin:14px 0 8px}.src{color:var(--muted);margin:0 0 12px;font-size:14px}
button{font:inherit;font-weight:600;border:0;border-radius:8px;padding:10px 22px;cursor:pointer;margin-right:10px;color:#fff}.ok{background:var(--green)}.no{background:#6b7773}
.note{color:var(--red);font-weight:600;margin:10px 0 0}
.errors{background:#fff;border:2px solid var(--red);border-radius:12px;padding:16px 20px;margin-bottom:24px}.errors h2,.err strong,.err li{color:var(--red)}
</style></head><body><main>
<h1>Ugens opslag ${esc(week)}</h1>
<p class="sub">${posts.length} opslag klar til godkendelse. Godkend eller afvis hvert opslag; kun godkendte havner i planen.</p>
${errHtml}
${posts.map((p) => postHtml(p, approvals)).join('\n')}
</main>
<script>
const NOSERVER='Preview-serveren kører ikke. Start den med: node social/bin/preview-server.js ${esc(week)} - og åbn siden på http://127.0.0.1:8787/';
document.querySelectorAll('.post').forEach((sec)=>{
  const note=sec.querySelector('.note');
  sec.querySelectorAll('button').forEach((b)=>b.addEventListener('click',async()=>{
    const approved=b.dataset.approve==='true';
    try{
      if(location.protocol==='file:')throw new Error('file');
      const r=await fetch('/approve',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id:sec.dataset.id,approved})});
      if(!r.ok)throw new Error(await r.text());
      sec.className='post '+(approved?'approved':'rejected');
      sec.querySelector('.status').textContent=approved?'Godkendt':'Afvist';
      note.hidden=true;
    }catch(e){note.textContent=e.message==='file'||e instanceof TypeError?NOSERVER:'Fejl: '+e.message;note.hidden=false;}
  }));
});
fetch('/approvals.json').then((r)=>r.ok?r.json():{}).then((a)=>{
  document.querySelectorAll('.post').forEach((sec)=>{
    const v=a[sec.dataset.id];if(v===undefined)return;
    sec.className='post '+(v?'approved':'rejected');sec.querySelector('.status').textContent=v?'Godkendt':'Afvist';
  });
}).catch(()=>{});
</script></body></html>
`;
}
