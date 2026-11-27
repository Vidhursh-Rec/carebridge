"""Build Carepedia: wraps every page in the shared desktop + window + sidebar frame.
Run: python build.py   (writes the .html pages at the repo root)
"""
import html
import os

from pages import PAGES, SITE_NAME

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://vidhursh-rec.github.io/carebridge/"
EDITED = "27 November 2026"

ICONS = {
    "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>',
    "book": '<path d="M4 19.5V5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2Z"/><path d="M8 7h7M8 11h7"/>',
    "flow": '<rect x="3" y="3" width="6" height="6" rx="1"/><rect x="15" y="15" width="6" height="6" rx="1"/><path d="M9 6h6a3 3 0 0 1 3 3v6"/>',
    "play": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m10 9 5 3-5 3Z"/>',
    "lang": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "trophy": '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0Z"/><path d="M7 6H4a3 3 0 0 0 3 4M17 6h3a3 3 0 0 1-3 4"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "map": '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2Z"/><path d="M9 4v14M15 6v14"/>',
    "screens": '<rect x="2" y="4" width="14" height="10" rx="1"/><rect x="17" y="8" width="5" height="11" rx="1"/><path d="M6 18h6"/>',
    "list": '<path d="M8 6h13M8 12h13M8 18h13"/><circle cx="4" cy="6" r="1"/><circle cx="4" cy="12" r="1"/><circle cx="4" cy="18" r="1"/>',
}


def icon(name, size=34):
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


LEFT = [("index.html", "home", "Main page"), ("carebridge.html", "book", "CareBridge"),
        ("how-it-works.html", "flow", "How it works"), ("design.html#launch-video", "play", "Demo"),
        ("languages.html", "lang", "Languages")]
RIGHT = [("origin.html", "trophy", "Origin"), ("history.html", "clock", "Changelog"),
         ("roadmap.html", "map", "Roadmap"), ("design.html", "screens", "Screens"),
         ("all-pages.html", "list", "All pages")]


def desk_icons(items, side):
    links = "\n".join(f'    <a class="desk-icon" href="{h}">{icon(i)}<span>{html.escape(t)}</span></a>' for h, i, t in items)
    return f'  <nav class="desk-icons {side}" aria-label="Shortcuts">\n{links}\n  </nav>'


def frame(slug, page):
    title = page["title"]
    nav = [("index.html", "Main page"), ("carebridge.html", "Featured article"), ("all-pages.html", "All pages"),
           ("all-pages.html?random", "Random article"), ("history.html", "Recent changes")]
    nav_html = "\n".join(
        f'          <li><a href="{h}"{" class=\"current\"" if h == slug else ""}{" data-random" if h.endswith("?random") else ""}>{t}</a></li>'
        for h, t in nav)
    tabs = ""
    if page.get("tabs", True):
        hist = slug == "history.html"
        tabs = (f'      <div class="tabs">\n        <a class="tab{"" if hist else " active"}" href="{"carebridge.html" if hist else slug}">article</a>\n'
                '        <span class="tab inert">discussion</span>\n        <span class="tab inert">view source</span>\n'
                f'        <a class="tab{" active" if hist else ""}" href="history.html">history</a>\n      </div>\n')
    heading = page.get("heading", title)
    sub = '' if page.get("portal") else '      <p class="from">From Carepedia, the free encyclopedia</p>\n'
    desc = html.escape(page["description"], quote=True)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)} - {SITE_NAME}</title>
  <meta name="description" content="{desc}" />
  <meta property="og:title" content="{html.escape(title)} - {SITE_NAME}, the free encyclopedia" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{BASE}{'' if slug == 'index.html' else slug}" />
  <meta property="og:image" content="{BASE}assets/photos/runner-up.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="icon" href="assets/brand/favicon-64.png" type="image/png" />
  <link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png" />
  <link rel="stylesheet" href="assets/site.css" />
  <script src="assets/site.js" defer></script>
</head>
<body>
  <div class="meadow" aria-hidden="true"></div>

  <header class="topbar">
    <a class="brand" href="index.html"><img src="assets/brand/favicon-64.png" alt="" width="28" height="28" /><span>CareBridge</span></a>
    <nav class="topnav" aria-label="Main">
      <a href="carebridge.html">Product</a><a href="how-it-works.html">How it works</a><a href="languages.html">Languages</a>
      <a href="origin.html">Story</a><a href="history.html">Changelog</a>
    </nav>
    <a class="cta" href="design.html#launch-video">Watch the demo</a>
  </header>

{desk_icons(LEFT, "left")}
{desk_icons(RIGHT, "right")}

  <div class="window" role="application" aria-label="{SITE_NAME}">
    <div class="titlebar">
      <button type="button" class="menu-btn" data-menu aria-expanded="false" aria-label="Open navigation">&#9776; Menu</button>
      <button type="button" class="nav-btn" data-back aria-label="Back">&#8249;</button>
      <button type="button" class="nav-btn" data-forward aria-label="Forward">&#8250;</button>
      <span class="win-title">{html.escape(title)} - {SITE_NAME}</span>
      <span class="win-ctrl" aria-hidden="true"><i></i><i></i><i></i></span>
    </div>
    <div class="win-body">
      <aside class="sidebar">
        <a class="logo" href="index.html" aria-label="{SITE_NAME} main page">
          <span class="logo-ring"><img src="assets/brand/nurse.png" alt="" width="104" height="114" /></span>
          <span class="logo-name">{SITE_NAME}</span>
          <span class="logo-tag">The Free Encyclopedia</span>
        </a>
        <div class="portlet">
          <h3>Search</h3>
          <form class="search" action="all-pages.html" method="get" role="search">
            <input name="q" type="search" placeholder="Search {SITE_NAME}" aria-label="Search {SITE_NAME}" />
            <div><button type="submit" name="go" value="1">Go</button><button type="submit">Search</button></div>
          </form>
        </div>
        <div class="portlet">
          <h3>Navigation</h3>
          <ul class="box">
{nav_html}
          </ul>
        </div>
        <div class="portlet">
          <h3>The app</h3>
          <ul class="box">
            <li><a href="design.html#launch-video">Launch video</a></li>
            <li><a href="design.html">Screens</a></li>
            <li><a href="roadmap.html">Version 2</a></li>
          </ul>
        </div>
      </aside>
      <main class="main" id="main" tabindex="-1">
{tabs}      <h1 class="page-title">{html.escape(heading)}</h1>
{sub}{page["body"]}
        <footer class="page-foot">
          <p>This page was last edited on {EDITED}. Text written by Vidhursh Kumar. App data shown is synthetic.</p>
          <p>{SITE_NAME} is a personal project page in the style of an encyclopedia. Not affiliated with Wikipedia or the Wikimedia Foundation.</p>
          <p><a href="index.html">Main Page</a> · <a href="all-pages.html">All pages</a> · <a href="history.html">Recent changes</a></p>
        </footer>
      </main>
    </div>
  </div>
</body>
</html>
'''


if __name__ == "__main__":
    for old in os.listdir(ROOT):
        if old.endswith(".html"):
            os.remove(os.path.join(ROOT, old))
    for slug, page in PAGES.items():
        with open(os.path.join(ROOT, slug), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(frame(slug, page))
    print(f"built {len(PAGES)} pages")
