"""
Build static entry-point pages for every government form.

Reads the catalogue defined in `data/catalogue.py`, writes one JSON file per
service into `data/services/`, and renders an HTML page for each service plus a
homepage and a category landing page per category.

Output directory: ./out/
"""
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
OUT = ROOT / "out"
DATA_DIR = ROOT / "data"
SERVICES_DIR = DATA_DIR / "services"

# Published GovBB design system stylesheet
STYLES_URL = "https://unpkg.com/@govtech-bb/styles@1.0.0-alpha.16/dist/styles.css"
CREST_URL = "https://unpkg.com/@govtech-bb/styles@1.0.0-alpha.16/dist/assets/images/govbb-creast.svg"
LOGO_URL = "https://unpkg.com/@govtech-bb/styles@1.0.0-alpha.16/dist/assets/images/govbb-logo.svg"

LAST_UPDATED = "12 May 2026"


# --------------------------------------------------------------------------- #
# Reusable HTML chrome
# --------------------------------------------------------------------------- #
def page_head(title: str, description: str = "", site_css: str = "../assets/site.css",
              title_suffix: str = " — The Government of Barbados") -> str:
    desc = escape(description) if description else ""
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{escape(title)}{escape(title_suffix)}</title>
    <meta name="description" content="{desc}" />
    <link rel="stylesheet" href="{STYLES_URL}" />
    <link rel="stylesheet" href="{site_css}" />
  </head>
  <body class="govbb-page">"""


HEADER_BANNER = f"""
    <div>
      <div class="govbb-official-banner">
        <div class="govbb-container govbb-official-banner__inner">
          <div class="govbb-official-banner__crest">
            <img class="govbb-official-banner__icon" src="{CREST_URL}" alt="" />
          </div>
          <div class="govbb-official-banner__text">
            <span>Official government website</span>
          </div>
        </div>
      </div>

      <header class="govbb-header">
        <div class="govbb-container govbb-header__inner">
          <a href="../index.html" aria-label="Go to the alpha.gov.bb homepage">
            <img class="govbb-header__logo" src="{LOGO_URL}" alt="GOVBB" />
          </a>
        </div>
      </header>
    </div>
"""

ALPHA_STATUS = """
      <div class="govbb-status-banner govbb-status-banner--alpha" role="status"
        aria-label="alpha status banner" aria-live="polite">
        <div class="govbb-container">
          <p>This page is in <a class="govbb-link govbb-link--secondary"
            href="#alpha">Alpha</a>.</p>
        </div>
      </div>
"""

FOOTER = f"""
    <footer class="govbb-footer">
      <div class="govbb-container govbb-footer__inner">
        <nav class="govbb-footer__nav" aria-label="Footer">
          <a class="govbb-footer__link" href="../index.html">Home</a>
          <a class="govbb-footer__link" href="#">Terms &amp; Conditions</a>
          <a class="govbb-footer__link" href="#">Careers</a>
        </nav>
        <hr class="govbb-footer__divider" aria-hidden="true" />
        <div class="govbb-footer__end">
          <img class="govbb-footer__coat" src="{CREST_URL}"
            alt="Government of Barbados Coat of Arms" />
          <p class="govbb-footer__copy">© 2026 Government of Barbados</p>
        </div>
      </div>
    </footer>
  </body>
</html>
"""


# --------------------------------------------------------------------------- #
# Service entry-page renderer
# --------------------------------------------------------------------------- #
def render_para_list(items):
    """Render a list of strings as <p> blocks (or pass-through HTML)."""
    if isinstance(items, str):
        return f'<p class="govbb-text-body">{escape(items)}</p>'
    return "\n".join(f'<p class="govbb-text-body">{escape(p)}</p>' for p in items)


def render_bullet_list(items):
    lis = "\n".join(f"<li>{escape(i)}</li>" for i in items)
    return f'<ul class="govbb-list govbb-list--bullet">{lis}</ul>'


def render_numbered_list(items):
    lis = "\n".join(f"<li>{escape(i)}</li>" for i in items)
    return f'<ol class="govbb-list govbb-list--number">{lis}</ol>'


def render_service_page(svc: dict, categories: dict) -> str:
    """Render one entry-page from its JSON data."""
    title = svc["title"]
    description = svc.get("description") or svc.get("summary", [""])[0]

    category_slug = svc["category"]
    category_name = categories[category_slug]["name"]

    sections = []

    # Overview
    if svc.get("summary"):
        sections.append(f"""
              <section class="service__section">
                <h2 class="govbb-text-h2">Overview</h2>
                {render_para_list(svc["summary"])}
              </section>""")

    # Who can apply
    if svc.get("who_can_apply"):
        wca = svc["who_can_apply"]
        bullets = render_bullet_list(wca["items"]) if isinstance(wca, dict) else render_bullet_list(wca)
        intro = ""
        if isinstance(wca, dict) and wca.get("intro"):
            intro = f'<p class="govbb-text-body">{escape(wca["intro"])}</p>'
        sections.append(f"""
              <section class="service__section">
                <h2 class="govbb-text-h2">Who can apply</h2>
                {intro}
                {bullets}
              </section>""")

    # Before you start (information needed)
    if svc.get("before_you_start"):
        bys = svc["before_you_start"]
        intro = bys.get("intro", "You will need:")
        items_html = render_bullet_list(bys["items"])
        sections.append(f"""
              <section class="service__section">
                <h2 class="govbb-text-h2">Before you start</h2>
                <p class="govbb-text-body">{escape(intro)}</p>
                {items_html}
              </section>""")

    # Documents you need to bring
    if svc.get("documents"):
        docs = svc["documents"]
        intro = docs.get("intro", "You will need to bring or upload:")
        items = docs["items"]
        list_html = []
        for d in items:
            if isinstance(d, dict):
                name = escape(d["name"])
                note = d.get("note", "")
                note_html = f' <span class="service__doc-note">{escape(note)}</span>' if note else ""
                list_html.append(f"<li><strong>{name}</strong>{note_html}</li>")
            else:
                list_html.append(f"<li>{escape(d)}</li>")
        items_html = '<ul class="govbb-list govbb-list--bullet service__doc-list">' + "\n".join(list_html) + "</ul>"
        sections.append(f"""
              <section class="service__section">
                <h2 class="govbb-text-h2">Documents you need</h2>
                <p class="govbb-text-body">{escape(intro)}</p>
                {items_html}
              </section>""")

    # Cost
    if svc.get("fees"):
        fees = svc["fees"]
        body = ""
        if isinstance(fees, str):
            body = f'<p class="govbb-text-body">{escape(fees)}</p>'
        else:
            if fees.get("summary"):
                body += render_para_list(fees["summary"])
            if fees.get("items"):
                rows = "".join(
                    f'<tr><th scope="row">{escape(i["label"])}</th><td>{escape(i["amount"])}</td></tr>'
                    for i in fees["items"]
                )
                body += f'<table class="service__fees"><tbody>{rows}</tbody></table>'
            if fees.get("notes"):
                body += render_para_list(fees["notes"])
        sections.append(f"""
              <section class="service__section">
                <h2 class="govbb-text-h2">Cost</h2>
                {body}
              </section>""")

    # How long it takes
    if svc.get("how_long"):
        sections.append(f"""
              <section class="service__section">
                <h2 class="govbb-text-h2">How long it takes</h2>
                {render_para_list(svc["how_long"])}
              </section>""")

    # How to apply
    if svc.get("how_to_apply"):
        h2a = svc["how_to_apply"]
        body_parts = []
        if isinstance(h2a, dict):
            if h2a.get("intro"):
                body_parts.append(render_para_list(h2a["intro"]))
            if h2a.get("steps"):
                body_parts.append(render_numbered_list(h2a["steps"]))
            if h2a.get("options"):
                for opt in h2a["options"]:
                    head = f'<h3 class="govbb-text-h3">{escape(opt["heading"])}</h3>'
                    content = render_para_list(opt["content"])
                    body_parts.append(head + content)
        else:
            body_parts.append(render_numbered_list(h2a))
        body = "\n".join(body_parts)
        sections.append(f"""
              <section class="service__section">
                <h2 class="govbb-text-h2">How to apply</h2>
                {body}
              </section>""")

    # Edge cases
    for ec in svc.get("edge_cases", []):
        head = escape(ec["heading"])
        content = render_para_list(ec["content"])
        sections.append(f"""
              <section class="service__section">
                <h2 class="govbb-text-h2">{head}</h2>
                {content}
              </section>""")

    # After
    if svc.get("after"):
        sections.append(f"""
              <section class="service__section">
                <h2 class="govbb-text-h2">After you apply</h2>
                {render_para_list(svc["after"])}
              </section>""")

    # Contact
    if svc.get("contact"):
        c = svc["contact"]
        lines = []
        if c.get("agency"):
            lines.append(f'<p class="govbb-text-body"><strong>{escape(c["agency"])}</strong></p>')
        if c.get("address"):
            addr_lines = "<br>".join(escape(l) for l in c["address"].split("\n"))
            lines.append(f'<p class="govbb-text-body">{addr_lines}</p>')
        if c.get("phone"):
            phones = c["phone"] if isinstance(c["phone"], list) else [c["phone"]]
            for p in phones:
                lines.append(f'<p class="govbb-text-body">{escape(p)}</p>')
        if c.get("email"):
            lines.append(f'<p class="govbb-text-body"><a class="govbb-link" href="mailto:{escape(c["email"])}">{escape(c["email"])}</a></p>')
        if c.get("hours"):
            lines.append(f'<p class="govbb-text-body">{escape(c["hours"])}</p>')
        sections.append(f"""
              <section class="service__section">
                <h2 class="govbb-text-h2">Contact</h2>
                {''.join(lines)}
              </section>""")

    # Related forms
    if svc.get("related"):
        items = svc["related"]
        rel = "\n".join(
            f'<li><a class="govbb-link" href="{escape(r["slug"])}.html">{escape(r["title"])}</a></li>'
            for r in items
        )
        sections.append(f"""
              <section class="service__section">
                <h2 class="govbb-text-h2">Related services</h2>
                <ul class="govbb-list govbb-list--bullet">{rel}</ul>
              </section>""")

    sections_html = "\n".join(sections)

    return f"""{page_head(title, description)}
    {HEADER_BANNER}
    <main class="govbb-page__main">
      {ALPHA_STATUS}
      <div class="govbb-container service-page">
        <nav class="govbb-breadcrumbs" aria-label="Breadcrumb">
          <ol class="govbb-breadcrumbs__list">
            <li class="govbb-breadcrumbs__item">
              <a class="govbb-breadcrumbs__link" href="../index.html">Home</a>
            </li>
            <li class="govbb-breadcrumbs__item">
              <a class="govbb-breadcrumbs__link"
                href="../categories/{escape(category_slug)}.html">{escape(category_name)}</a>
            </li>
            <li class="govbb-breadcrumbs__item" aria-current="page">{escape(title)}</li>
          </ol>
        </nav>

        <div class="service__grid">
          <div class="service__main">
            <h1 class="govbb-text-display">{escape(title)}</h1>
            <div class="service__meta">
              <p class="govbb-text-caption">Last updated: {escape(LAST_UPDATED)}</p>
            </div>
            <div class="service__sections">
{sections_html}
              <div class="service__feedback">
                <h3 class="govbb-text-h3">Was this helpful?</h3>
                <p class="govbb-text-body">Give us your feedback about this page.</p>
                <a class="govbb-link govbb-link--secondary govbb-font-body" href="#">Help us improve alpha.gov.bb</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
    {FOOTER}"""


# --------------------------------------------------------------------------- #
# Category landing page renderer
# --------------------------------------------------------------------------- #
def render_category_page(cat_slug: str, category: dict, services: list[dict]) -> str:
    items_html = "\n".join(
        f'''<div class="category__item">
              <a class="govbb-link category__link" href="../services/{escape(s["slug"])}.html">{escape(s["title"])}</a>
            </div>'''
        for s in services
    )
    return f"""{page_head(category["name"], category.get("description", ""))}
    {HEADER_BANNER}
    <main class="govbb-page__main">
      {ALPHA_STATUS}
      <div class="govbb-container category-page">
        <nav class="govbb-breadcrumbs" aria-label="Breadcrumb">
          <ol class="govbb-breadcrumbs__list">
            <li class="govbb-breadcrumbs__item">
              <a class="govbb-breadcrumbs__link" href="../index.html">Home</a>
            </li>
            <li class="govbb-breadcrumbs__item" aria-current="page">{escape(category["name"])}</li>
          </ol>
        </nav>

        <div class="category">
          <h1 class="govbb-text-display">{escape(category["name"])}</h1>
          <p class="govbb-text-body">{escape(category.get("description", ""))}</p>
          <div class="category__list">
            {items_html}
          </div>
          <div class="category__feedback">
            <h3 class="govbb-text-h3">Was this helpful?</h3>
            <p class="govbb-text-body">Give us your feedback about this page.</p>
            <a class="govbb-link govbb-link--secondary govbb-font-body" href="#">Help us improve alpha.gov.bb</a>
          </div>
        </div>
      </div>
    </main>
    {FOOTER}"""


# --------------------------------------------------------------------------- #
# Homepage renderer
# --------------------------------------------------------------------------- #
def render_homepage(categories: dict, services_by_cat: dict) -> str:
    cat_cards = []
    for slug, cat in categories.items():
        n = len(services_by_cat.get(slug, []))
        cat_cards.append(f'''
          <div class="home__card">
            <h2 class="govbb-text-h2"><a class="govbb-link" href="categories/{escape(slug)}.html">{escape(cat["name"])}</a></h2>
            <p class="govbb-text-body">{escape(cat.get("description", ""))}</p>
            <p class="govbb-text-caption">{n} service{"s" if n != 1 else ""}</p>
          </div>''')
    cards_html = "\n".join(cat_cards)
    return f"""{page_head("Find a government service", "Find out what you need before you start a government form. Each entry page tells you what documents to bring, how long it takes, and what it will cost.", site_css="assets/site.css")}
    {HEADER_BANNER.replace('href="../index.html"', 'href="index.html"')}
    <main class="govbb-page__main">
      {ALPHA_STATUS}
      <div class="govbb-container home-page">
        <div class="home__intro">
          <h1 class="govbb-text-display">Find a government service</h1>
          <p class="govbb-text-body home__lede">Before you start a form or go to a government office, find out what you will need. Each page tells you what to bring, how long it takes and what it will cost.</p>
        </div>
        <div class="home__grid">
          {cards_html}
        </div>
        <div class="category__feedback" style="margin-top: var(--spacing-l);">
          <h3 class="govbb-text-h3">Was this helpful?</h3>
          <p class="govbb-text-body">Give us your feedback about this page.</p>
          <a class="govbb-link govbb-link--secondary govbb-font-body" href="#">Help us improve alpha.gov.bb</a>
        </div>
      </div>
    </main>
    <footer class="govbb-footer">
      <div class="govbb-container govbb-footer__inner">
        <nav class="govbb-footer__nav" aria-label="Footer">
          <a class="govbb-footer__link" href="index.html">Home</a>
          <a class="govbb-footer__link" href="#">Terms &amp; Conditions</a>
          <a class="govbb-footer__link" href="#">Careers</a>
        </nav>
        <hr class="govbb-footer__divider" aria-hidden="true" />
        <div class="govbb-footer__end">
          <img class="govbb-footer__coat" src="{CREST_URL}" alt="Government of Barbados Coat of Arms" />
          <p class="govbb-footer__copy">© 2026 Government of Barbados</p>
        </div>
      </div>
    </footer>
  </body>
</html>
"""


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #
SITE_CSS = """/* Page-specific layout on top of @govtech-bb/styles */

.service-page,
.category-page,
.home-page {
  padding-block: var(--spacing-m);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-m);
}

.service__grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--spacing-m);
}

.service__main {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-m);
}

.service__meta {
  padding-bottom: var(--spacing-s);
  border-bottom: 4px solid var(--color-blue-10);
  color: var(--color-mid-grey-00);
}

.service__sections {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-m);
}

.service__section {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-s);
}

.service__feedback,
.category__feedback {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: var(--spacing-xs);
  border: 4px solid var(--color-yellow-100);
  background: var(--color-yellow-40);
  padding: var(--spacing-xm) var(--spacing-s);
}

.service__doc-note {
  display: block;
  color: var(--color-mid-grey-00);
  font-size: var(--font-size-body-sm);
}

.service__fees {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--font-size-body);
}

.service__fees th,
.service__fees td {
  text-align: left;
  padding: var(--spacing-xs) var(--spacing-s);
  border-bottom: 1px solid var(--color-grey-00);
}

.service__fees th {
  font-weight: 600;
  width: 60%;
}

.category {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-s);
}

.category__list {
  display: flex;
  flex-direction: column;
  border-bottom: 2px solid var(--color-grey-00);
}

.category__item {
  padding-block: var(--spacing-s);
  border-top: 2px solid var(--color-grey-00);
}

.category__link {
  font-size: var(--font-size-body-lg);
  line-height: var(--line-height-body-lg);
}

.home__intro {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-s);
}

.home__lede {
  font-size: var(--font-size-body-lg);
}

.home__grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--spacing-m);
}

.home__card {
  padding: var(--spacing-m);
  border: 2px solid var(--color-grey-00);
  border-top: 6px solid var(--color-blue-100);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xs);
  background: var(--color-white, #fff);
}

@media (width >= 1024px) {
  .service__grid {
    grid-template-columns: repeat(3, 1fr);
    gap: var(--spacing-xl);
  }
  .service__main {
    grid-column: span 2;
  }
  .home__grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .category__item {
    padding-block: var(--spacing-m);
  }
  .category__link {
    font-size: var(--font-size-h3);
    line-height: var(--line-height-h3);
  }
}
"""


def main():
    # Lazy import so the data file can be edited without breaking imports
    from data.catalogue import CATEGORIES, _all_services
    SERVICES = _all_services()

    # Reset output
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "services").mkdir(parents=True)
    (OUT / "categories").mkdir()
    (OUT / "assets").mkdir()
    (OUT / "data" / "services").mkdir(parents=True)

    # Write CSS
    (OUT / "assets" / "site.css").write_text(SITE_CSS)

    # Group services by category
    services_by_cat: dict[str, list[dict]] = {slug: [] for slug in CATEGORIES}
    for svc in SERVICES:
        services_by_cat.setdefault(svc["category"], []).append(svc)

    # Sort services within each category by title
    for slug in services_by_cat:
        services_by_cat[slug].sort(key=lambda s: s["title"])

    # Write JSON per service AND a master manifest
    SERVICES_DIR.mkdir(parents=True, exist_ok=True)
    for svc in SERVICES:
        path = SERVICES_DIR / f"{svc['slug']}.json"
        path.write_text(json.dumps(svc, indent=2, ensure_ascii=False))
        # Also copy to output data folder so it's deployable
        (OUT / "data" / "services" / f"{svc['slug']}.json").write_text(
            json.dumps(svc, indent=2, ensure_ascii=False)
        )

    # Master manifest
    manifest = {
        "categories": CATEGORIES,
        "services": [
            {
                "slug": s["slug"],
                "title": s["title"],
                "category": s["category"],
                "description": s.get("description", ""),
            }
            for s in SERVICES
        ],
    }
    (DATA_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    (OUT / "data" / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))

    # Render service pages
    for svc in SERVICES:
        html = render_service_page(svc, CATEGORIES)
        (OUT / "services" / f"{svc['slug']}.html").write_text(html)

    # Render category pages
    for slug, cat in CATEGORIES.items():
        html = render_category_page(slug, cat, services_by_cat[slug])
        (OUT / "categories" / f"{slug}.html").write_text(html)

    # Render homepage
    (OUT / "index.html").write_text(render_homepage(CATEGORIES, services_by_cat))

    print(f"Built {len(SERVICES)} service pages across {len(CATEGORIES)} categories.")
    print(f"Output: {OUT}")


if __name__ == "__main__":
    main()
