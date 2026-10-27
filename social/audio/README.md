# Lyd til shorts

Musikken til shorts og fredagens elpris-reel ligger her. Mappen har i dag fire spor:

| Fil | Længde |
|---|---|
| `bright-explainer-01.m4a` | ca. 52 sek. |
| `bright-explainer-02.m4a` | ca. 110 sek. |
| `melodic-guitar-01.m4a` | ca. 202 sek. |
| `melodic-guitar-02.m4a` | ca. 192 sek. |

Et brief peger på et spor med feltet `audio` (kun filnavnet), fx `"audio": "melodic-guitar-01.m4a"`. Skift mellem sporene hen over ugen. Elpris-reelen (`elpris-story.js --reel`) vælger selv et spor på skift efter datoen.

Nye spor:

- Navngiv dem `<stemning>-<nr>.<ext>` med små bogstaver og bindestreg, fx `rolig-piano-01.m4a`. Kun `mp3`, `m4a` eller `wav`.
- Instrumental (ingen sangtekst), mindst 20 sekunder lang.
- Rettighederne skal være i orden til kommerciel brug på Instagram.
- Tilføj sporet til tabellen her og til listen under `audio` i `social/PLAYBOOK.md`.

Mangler filen, stopper `renderShort` med `Lydfil mangler: social/audio/<navn>`.
