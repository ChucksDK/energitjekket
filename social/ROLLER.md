# Hvem gør hvad på @energitjekket

Gælder fra 27. oktober 2026. Læs denne fil før du laver noget til Instagram-kontoen @energitjekket. Reglerne for selve indholdet står i `social/PLAYBOOK.md`; den gælder for alle.

## Kort fortalt

| Hvem | Ansvar | Rører aldrig |
|---|---|---|
| **Claude** | Hele ugens 13 faste opslag: analyse, brief, slides, shorts, captions, Higgsfield-billeder, kontrol og planlægning i Zernio. | Den daglige elpris-story og fredagens kl. 19:30-slot. |
| **Casper** | Godkender hvert opslag i previewet, før Claude planlægger det. Bestemmer, hvornår godkendelsen kan slås fra. | – |
| **Grok** | Kun det, der ikke kan laves på forhånd: den daglige elpris-story og fredagens elpris-reel kl. 19:30. Hvordan Grok gør det, aftaler Casper senere. | Ugens 13 faste opslag og alle andre slots. |

## Claude: ugens faste opslag

Én gang om ugen (normalt i weekenden før ugen) laver Claude næste uges 13 opslag:

- Hver dag kl. 07:30 et carousel (7 i alt).
- Hver dag kl. 19:30 en short, **undtagen fredag** (6 i alt).

Claude skriver selv briefen `social/briefs/<uge>.json` ud fra playbooken, bygger ugen, får Caspers godkendelse og planlægger opslagene i Zernio på kontoen @energitjekket med `social/bin/publish.js`. Planlagte opslag står i `social/out/<uge>/sent.json` med deres Zernio-id.

Grok skriver ikke længere briefen og planlægger ikke ugens opslag.

## Grok: det, der afhænger af dagens elpriser

Elpriserne for i morgen kommer først ca. kl. 13 dagen før. Derfor kan de ikke laves en uge frem, og Claude laver dem ikke.

- **Daglig elpris-story** (efter kl. 13:45): morgendagens spotpriser for Vestdanmark og Østdanmark.
- **Fredag kl. 19:30:** elpris-reel med lørdagens billigste timer. Det er det eneste feed-slot, Grok bruger. Slottet holdes altid tomt i ugens brief.

Værktøjet findes allerede: `node social/bin/elpris-story.js` (og `--reel` om fredagen) laver filerne i `social/out/stories/<dato>/`. Se afsnittet "Daglig elpris-story og fredags-reel" i playbooken. Exit-kode 3 betyder, at priserne ikke findes endnu: så laves der intet den dag.

## Regler for at dele kontoen

1. **Slots er delt op på forhånd.** Claude: alle dage kl. 07:30 og kl. 19:30 undtagen fredag 19:30. Grok: fredag kl. 19:30 og stories. Ingen planlægger i den andens slots.
2. **Tjek køen før du planlægger.** `node social/bin/queue.js list` viser alt, der er planlagt på @energitjekket, med dansk tid og sammenstød.
3. **Ret eller slet ikke den andens opslag.** Er der et problem, så skriv det til Casper.
4. **Samme regler for tal og tone.** Alle tal kommer fra kilderegistret, ingen salgssnak (se "Hårde regler" i playbooken). Elpris kaldes altid spotpris.
