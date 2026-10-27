// E-mailskabeloner for Energitjekket (dansk). Ren tekst + simpel HTML.
export type Lead = {
  id: string; created_at: string; service: string; city: string | null; page_url: string | null;
  answers: Record<string, unknown>; name: string; email: string; phone: string; postal_code: string;
  consent_version: string; consent_at: string; utm: Record<string, unknown>;
  assigned_company_name: string | null; assigned_company_cvr: string | null;
};

export const BRAND = "Energitjekket";
export const FROM = "Energitjekket <kontakt@energitjekket.dk>";
export const CONTACT = "kontakt@energitjekket.dk";
const SITE = "https://www.energitjekket.dk";
const COMPANY_FOOTER = "Energitjekket drives af ANGU ApS, CVR 40086560, Prins Christians Vænge 16, 8660 Skanderborg.";

export const esc = (s: unknown) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]!));
const product = (svc: string) => (svc === "varmepumpe" ? "en luft til vand-varmepumpe" : "solceller");
const wrap = (inner: string) =>
  `<!doctype html><html lang="da"><body style="margin:0;background:#f6f8f7;font-family:Arial,Helvetica,sans-serif;color:#13201d">` +
  `<div style="max-width:560px;margin:0 auto;padding:24px"><div style="background:#fff;border:1px solid #e1e8e5;border-radius:12px;padding:24px;line-height:1.55;font-size:15px">` +
  inner + `</div><p style="font-size:12px;color:#4f5e5a;margin-top:16px">${esc(COMPANY_FOOTER)}</p></div></body></html>`;

/** Til kunden, når en installatør har fået oplysningerne. */
export function customerEmail(l: Lead) {
  const co = l.assigned_company_name ?? "", cvr = l.assigned_company_cvr ?? "";
  const subject = `Dine oplysninger er sendt til ${co}`;
  const text = [
    `Hej ${l.name}`,
    ``,
    `Tak for din forespørgsel om ${product(l.service)} via ${BRAND}.`,
    ``,
    `Vi har nu sendt dine oplysninger (navn, telefon, e-mail, postnummer og dine svar fra formularen) til:`,
    `${co}, CVR ${cvr} (https://datacvr.virk.dk/enhed/virksomhed/${cvr})`,
    ``,
    `Firmaet kontakter dig på telefon eller e-mail med et uforpligtende tilbud. Du bestemmer selv, om du vil sige ja.`,
    ``,
    `Vil du ikke kontaktes, eller vil du trække dit samtykke tilbage, så skriv til ${CONTACT}. Så giver vi besked til ${co} og sletter dine oplysninger hos os.`,
    `Læs mere i vores privatlivspolitik: ${SITE}/privatlivspolitik/`,
    ``,
    `Venlig hilsen`,
    BRAND,
    ``,
    COMPANY_FOOTER,
  ].join("\n");
  const html = wrap(
    `<p>Hej ${esc(l.name)}</p>` +
    `<p>Tak for din forespørgsel om ${esc(product(l.service))} via ${BRAND}.</p>` +
    `<p>Vi har nu sendt dine oplysninger (navn, telefon, e-mail, postnummer og dine svar fra formularen) til:</p>` +
    `<p style="background:#f2f8f5;border-radius:10px;padding:12px 14px"><strong>${esc(co)}</strong><br>CVR <a href="https://datacvr.virk.dk/enhed/virksomhed/${esc(cvr)}">${esc(cvr)}</a></p>` +
    `<p>Firmaet kontakter dig på telefon eller e-mail med et uforpligtende tilbud. Du bestemmer selv, om du vil sige ja.</p>` +
    `<p><strong>Vil du ikke kontaktes, eller vil du trække dit samtykke tilbage?</strong> Skriv til <a href="mailto:${CONTACT}">${CONTACT}</a>. Så giver vi besked til ${esc(co)} og sletter dine oplysninger hos os. Læs mere i vores <a href="${SITE}/privatlivspolitik/">privatlivspolitik</a>.</p>` +
    `<p>Venlig hilsen<br>${BRAND}</p>`,
  );
  return { subject, text, html };
}

/** Til Casper ved hvert nyt lead. */
export function ownerEmail(l: Lead, projectRef: string) {
  const svc = l.service === "varmepumpe" ? "Varmepumpe" : "Solceller";
  const subject = `Nyt lead: ${svc} i ${l.city || "ukendt by"} (${l.postal_code})`;
  const answers = Object.entries(l.answers || {}).map(([k, v]) => `${k}: ${v}`);
  const sql = `update public.leads set assigned_company_name = 'Firmanavn ApS', assigned_company_cvr = '12345678' where id = '${l.id}';`;
  const editor = `https://supabase.com/dashboard/project/${projectRef}/editor`;
  const rows: [string, string][] = [
    ["Navn", l.name], ["Telefon", l.phone], ["E-mail", l.email], ["Postnummer", l.postal_code],
    ["Ydelse", svc], ["By (side)", l.city || "-"], ["Side", l.page_url || "-"], ["Modtaget", l.created_at],
    ["Samtykke", `${l.consent_version} (${l.consent_at})`], ["Lead-id", l.id],
  ];
  const text = [
    `Nyt lead fra energitjekket.dk`, ``,
    ...rows.map(([k, v]) => `${k}: ${v}`), ``,
    `Svar fra formularen:`, ...(answers.length ? answers : ["(ingen)"]), ``,
    `Når du har sendt leadet til et firma, så udfyld firmaets navn og CVR (Table Editor: ${editor}, tabellen leads), eller kør:`,
    sql, ``,
    `Så får kunden automatisk en e-mail med firmaets navn og CVR.`,
  ].join("\n");
  const html = wrap(
    `<p><strong>Nyt lead fra energitjekket.dk</strong></p><table style="border-collapse:collapse;font-size:14px">` +
    rows.map(([k, v]) => `<tr><td style="padding:4px 12px 4px 0;color:#4f5e5a">${esc(k)}</td><td style="padding:4px 0">${esc(v)}</td></tr>`).join("") +
    `</table><p><strong>Svar fra formularen</strong></p><ul>` + (answers.length ? answers.map((a) => `<li>${esc(a)}</li>`).join("") : "<li>(ingen)</li>") + `</ul>` +
    `<p>Når du har sendt leadet til et firma, så udfyld <code>assigned_company_name</code> og <code>assigned_company_cvr</code> i <a href="${editor}">Table Editor</a> (tabellen <code>leads</code>), eller kør:</p>` +
    `<pre style="white-space:pre-wrap;background:#f6f8f7;padding:10px;border-radius:8px;font-size:12px">${esc(sql)}</pre>` +
    `<p>Så får kunden automatisk en e-mail med firmaets navn og CVR.</p>`,
  );
  return { subject, text, html };
}
