# Government of Barbados — service entry pages

Prototype entry pages for every form in `/forms`. Each page tells citizens what they need to know, what to bring and how long it takes before they start a form or go to a government office.

Modelled on the alpha.gov.bb pattern at [alpha.gov.bb/family-birth-relationships/get-birth-certificate](https://alpha.gov.bb/family-birth-relationships/get-birth-certificate). Uses the published GovBB design system from `@govtech-bb/styles` (alpha 16).

## How to view it

Open `index.html` in any modern browser. From there you can browse all 7 categories and 62 services.

## Structure

```
entry-pages/
├── index.html                  # Homepage — lists every category
├── categories/                 # One landing page per category
│   ├── driving-and-transport.html
│   ├── national-insurance-and-benefits.html
│   └── …
├── services/                   # The 62 entry pages
│   ├── firearm-licence.html
│   ├── register-or-renew-a-vehicle.html
│   └── …
├── data/
│   ├── manifest.json           # Master catalogue of categories + services
│   └── services/               # One JSON file per service (the source of truth)
│       ├── firearm-licence.json
│       ├── register-or-renew-a-vehicle.json
│       └── …
├── assets/
│   └── site.css                # Page-specific layout on top of @govtech-bb/styles
└── _build/                     # Build script and source data (Python)
    ├── build.py
    └── data/
        ├── catalogue.py
        ├── catalogue_business.py
        └── catalogue_youth.py
```

## How the pages are built

Each service page is rendered from a single JSON file that lives at `data/services/<slug>.json`. The JSON captures:

- **summary** — three or four plain-language paragraphs explaining what the service is for
- **who_can_apply** — eligibility criteria
- **before_you_start** — information the citizen needs to have ready (e.g. NRN, vehicle registration number)
- **documents** — physical or scanned documents they need to bring or upload
- **fees** — itemised cost table
- **how_long** — typical processing time
- **how_to_apply** — step-by-step options
- **edge_cases** — common exceptions ("If your application is rejected…")
- **after** — what happens next
- **contact** — agency, address, phone, email, hours
- **related** — links to related services
- **assumptions** — every guess I made for that page, called out in a yellow callout so reviewers know what to confirm with the responsible agency (fees, processing times, eligibility ages, contact details, document lists, etc.)

`_build/build.py` reads the JSON, renders an HTML page per service, generates the category landing pages and the homepage, and outputs them into the layout above. To regenerate after editing the data:

```bash
cd _build
python3 build.py
```

The build writes its output to `_build/out/`. Copy that over `entry-pages/` to publish.

## Categories

| Category | Services |
|---|---|
| Driving and transport | 18 |
| National Insurance and benefits | 10 |
| Firearms | 4 |
| Safety and public events | 3 |
| Business and companies | 9 |
| Trade, exports and imports | 7 |
| Youth and community programmes | 11 |

## Sources

Forms in this project come from:

- the main `/forms` folder (named PDFs from Royal Barbados Police Force, Barbados Licensing Authority, NIS, CAIPO, BIDC and Customs)
- `/forms/raw-forms` (BLA letter templates, some via OCR)
- `/forms/Ministry of Youth` (BYAC, Get Hired, Pathways, NSCP, YES First Contact, YAR, Youth MC, National Community Cultural Training)

Where two forms differ only by single vs. multiple owners (e.g. sale of vehicle), they are merged into one entry page that mentions both versions. Where the same PDF appears under a UUID file name and a named file, the duplicate is dropped.

## Plain language

Every page is written for citizens, not civil servants. Sentences are short. We say "tell us" not "submit", "check" not "verify", "you" not "the applicant". British English spelling throughout.

## What's next

- Work through the yellow "What we've assumed on this page" callout at the bottom of each entry page with the agency that owns the service. Confirm or correct every item.
- Pull real fees and processing times from the responsible agencies — the current figures are best guesses based on what is publicly known.
- Add a "Start now" button that links to the corresponding online form once each one is built.
- Add a real Last-updated timestamp once owners are assigned.
- Run a plain-language review and an accessibility audit with the GovTech Barbados team.
