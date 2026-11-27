# Carepedia

The public CareBridge site: a small encyclopedia in an old-style wiki window on a pixel meadow desktop.
Static HTML, CSS and a little JavaScript, served by GitHub Pages.

- Page text lives in `pages.py`; `python build.py` wraps each page in the shared window and sidebar.
- The page never scrolls; only the article pane inside the window does.
- Run the checks: `python tests/check_site.py`
