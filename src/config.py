# -*- coding: utf-8 -*-
"""ÉT sted at ændre brand, domæne og virksomhedsoplysninger. Kør derefter: python3 build.py"""
BRAND = "Energitjekket"
BRAND_TAGLINE = "Uafhængig formidling af tilbud på solceller og varmepumper"
SITE_URL = "https://energitjekket.dk"   # uden afsluttende skråstreg
CONTACT_EMAIL = "kontakt@energitjekket.dk"   # godkendt af Casper 25/10 2026 (domænet er endnu ikke købt)
CONTACT_PHONE = "29 72 84 48"               # vises ikke på datacvr.virk.dk (25/10 2026); stammer fra cvrdb.dk/estatistik.dk. OBS: sandsynligvis privat nummer – overvej et dedikeret
COMPANY_NAME = "ANGU ApS"                   # juridisk navn på den dataansvarlige virksomhed (CVR-opslag 23/10 2026)
CVR = "40086560"
COMPANY_STREET = "Prins Christians Vænge 16"
COMPANY_ZIP = "8660"
COMPANY_CITY = "Skanderborg"
COMPANY_ADDRESS = f"{COMPANY_STREET}, {COMPANY_ZIP} {COMPANY_CITY}"   # registreret adresse i CVR
COMPANY_WEBSITE = "www.casperlarsen.dk"     # registreret hjemmeside i CVR (bruges ikke på sitet)
# Officiel kilde, tjekket 25/10 2026: https://datacvr.virk.dk/enhed/virksomhed/40086560 (ANGU ApS, Prins Christians Vænge 16, Skanderborg Bakker, 8660 Skanderborg, ApS, startdato 10.12.2018, status Normal)
# Tidligere kilder: https://cvrdb.dk/virksomhed/dk/angu-aps/40086560 · https://estatistik.dk/virksomhed/angu-aps/40086560 · https://datacvrapi.dk/virksomhed/angu-aps-40086560
TRUST_TEXT = "Vi kender markedet for solceller og varmepumper, og vi arbejder kun sammen med installatører, der lever op til en række krav og har positiv feedback fra tidligere kunder."
LAST_CHECKED = "23. oktober 2026"           # dato for seneste faktatjek af tal og regler
LAST_CHECKED_ISO = "2026-10-23"
LAST_UPDATED = "25. oktober 2026"           # standard "Opdateret"-dato (synlig + dateModified). Per side: "updated" i NATIONAL/CITIES
LAST_UPDATED_ISO = "2026-10-25"
COMPANY_FOUNDED = "2018-12-10"              # startdato i CVR
CVR_URL = "https://datacvr.virk.dk/enhed/virksomhed/40086560"

# Supabase (projekt "energitjekket", ref ckdrjxjdxprezsvfdpet, eu-west-1). Publishable key er offentlig og må ligge i browseren;
# RLS tillader kun INSERT i public.leads. Brug ALDRIG service_role/secret key her.
SUPABASE_URL = "https://ckdrjxjdxprezsvfdpet.supabase.co"
SUPABASE_PUBLISHABLE_KEY = "sb_publishable_aRI1q3wllbs5kT-nIaYp1w_VtVo_mJR"
CONSENT_VERSION = "2026-10-25-v2"

# Vercel-statistik (Web Analytics slået til i dashboardet 25.10.2026 af Casper).
WEB_ANALYTICS = True
SPEED_INSIGHTS = True

# Egen cookiefri førstepartsstatistik -> CRM-Supabase (casper-crm, eu-central-1), edge-funktionen "track".
# Ingen nøgler i browseren; funktionen er offentlig, men tillader kun disse origins. Slå fra her eller med TRACK_ENABLED=false.
FIRST_PARTY_ANALYTICS = True
FP_ANALYTICS_ENDPOINT = "https://zogqspzdxddaxtlotfgn.supabase.co/functions/v1/track"
FP_ANALYTICS_SITE = "energitjekket.dk"

# Krydslinks til administratortjekket.dk (samme ejer). Kun bysider, der svarede 200 live uden noindex (curl), tjekket 27/10 2026.
# Bruges som én inline-tekstlink i "boliger"-afsnittet på solcelle-bysiden. Tilføj en by først, når siden er live.
CROSS_SITE_URL = "https://administratortjekket.dk"
CROSS_CITY_LINKS = {"aarhus": "/ejendomsadministration/aarhus/", "odense": "/ejendomsadministration/odense/", "aalborg": "/ejendomsadministration/aalborg/",
                    "randers": "/ejendomsadministration/randers/", "naestved": "/ejendomsadministration/naestved/",
                    "kolding": "/ejendomsadministration/kolding/", "vejle": "/ejendomsadministration/vejle/"}
