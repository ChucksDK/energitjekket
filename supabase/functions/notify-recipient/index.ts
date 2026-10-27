// notify-recipient: kaldes af databasetriggere på public.leads (pg_net).
//  - type "INSERT":   e-mail til Casper om nyt lead
//  - type "ASSIGNED": e-mail til kunden om hvilket firma der har fået oplysningerne
// Funktionen stoler ikke på indholdet i kaldet: den slår leadet op med service role og handler kun ud fra
// databasens tilstand (idempotent via owner_notified_at / customer_notified_at).
// Uden RESEND_API_KEY (eller med DRY_RUN=1 / {"dry_run":true}) sendes intet: der logges, og notify_error udfyldes.
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "npm:@supabase/supabase-js@2";
import { customerEmail, ownerEmail, FROM, CONTACT, type Lead } from "./templates.ts";

const OWNER = Deno.env.get("OWNER_EMAIL") ?? "casper@casperlarsen.dk";
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const json = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { "Content-Type": "application/json" } });

Deno.serve(async (req) => {
  if (req.method !== "POST") return json({ error: "method" }, 405);
  let body: { type?: string; lead_id?: string; dry_run?: boolean };
  try { body = await req.json(); } catch { return json({ error: "bad json" }, 400); }
  const type = body.type, id = body.lead_id ?? "";
  if (!(type === "INSERT" || type === "ASSIGNED") || !UUID.test(id)) return json({ error: "bad request" }, 400);

  const url = Deno.env.get("SUPABASE_URL")!;
  const db = createClient(url, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, { auth: { persistSession: false } });
  const ref = new URL(url).hostname.split(".")[0];
  const { data: lead, error } = await db.from("leads").select("*").eq("id", id).maybeSingle();
  if (error || !lead) return json({ error: "not found" }, 404);
  const l = lead as Lead & { owner_notified_at: string | null; customer_notified_at: string | null };

  let to: string, mail: { subject: string; text: string; html: string }, doneCol: string, kind: string, replyTo: string;
  if (type === "INSERT") {
    if (l.owner_notified_at) return json({ skipped: "owner already notified" });
    to = OWNER; mail = ownerEmail(l, ref); doneCol = "owner_notified_at"; kind = "ny-lead"; replyTo = l.email;
  } else {
    if (!l.assigned_company_name || !l.assigned_company_cvr) return json({ skipped: "not assigned" });
    if (l.customer_notified_at) return json({ skipped: "customer already notified" });
    to = l.email; mail = customerEmail(l); doneCol = "customer_notified_at"; kind = "kunde"; replyTo = CONTACT;
  }

  const rawKey = Deno.env.get("RESEND_API_KEY");
  // tolerér mellemrum/linjeskift/anførselstegn fra copy-paste i Supabase Secrets
  const key = rawKey ? rawKey.trim().replace(/^["'`]+|["'`]+$/g, "").replace(/^Bearer\s+/i, "").trim() : rawKey;
  const dry = !key || Deno.env.get("DRY_RUN") === "1" || body.dry_run === true;
  const stamp = new Date().toISOString();
  if (dry) {
    const why = !key ? "RESEND_API_KEY mangler" : "dry-run";
    console.log(`[notify-recipient] ${why}: ingen e-mail sendt (${kind}) for lead ${id}`);
    await db.from("leads").update({ notify_error: `[${kind}] ${why} – ingen e-mail sendt (${stamp})` }).eq("id", id);
    return json({ dry_run: true, reason: why, kind, to_domain: to.split("@")[1], subject_chars: mail.subject.length, text_chars: mail.text.length });
  }

  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json", "Idempotency-Key": `${kind}-${id}` },
    body: JSON.stringify({ from: FROM, to: [to], reply_to: replyTo, subject: mail.subject, text: mail.text, html: mail.html }),
  });
  if (!r.ok) {
    const msg = (await r.text()).slice(0, 400) + (r.status === 401 ? ` [nøgle-tjek: starter med re_=${key!.startsWith("re_")}, længde=${key!.length}, rå længde=${rawKey!.length}]` : "");
    console.error(`[notify-recipient] Resend fejl ${r.status} (${kind}) for lead ${id}: ${msg}`);
    await db.from("leads").update({ notify_error: `[${kind}] Resend ${r.status}: ${msg} (${stamp})` }).eq("id", id);
    return json({ error: "resend", status: r.status }, 502);
  }
  let resendId: string | null = null;
  try { resendId = (await r.json())?.id ?? null; } catch { /* ignore */ }
  console.log(`[notify-recipient] sendt (${kind}) for lead ${id}, resend id ${resendId}`);
  await db.from("leads").update({ [doneCol]: stamp, notify_error: null }).eq("id", id);
  return json({ sent: true, kind, resend_id: resendId });
});
