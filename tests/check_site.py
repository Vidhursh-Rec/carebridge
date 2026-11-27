"""Carepedia site checks. Run: python tests/check_site.py  (exit 0 = all pass)."""
import glob
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

HTML = sorted(glob.glob("*.html"))
CSS = sorted(glob.glob("assets/**/*.css", recursive=True))
TEXT = HTML + CSS + sorted(glob.glob("assets/**/*.js", recursive=True)) + ["README.md"]
# Forbidden words live in a git-ignored local file so the list itself is never published.
_LOCAL = os.path.join(ROOT, "tests", "forbidden.local.txt")
FORBIDDEN = [w.strip() for w in open(_LOCAL, encoding="utf-8") if w.strip()] if os.path.exists(_LOCAL) else []
TRACKED = subprocess.run(["git", "ls-files"], capture_output=True, text=True, cwd=ROOT).stdout.split()
REF = re.compile(r'(?:href|src|poster)\s*=\s*"([^"]+)"|url\(\s*["\']?([^"\')]+)')
results = []


def check(name):
    def wrap(fn):
        try:
            out = fn()
            results.append((name, "SKIP" if out == "SKIP" else "PASS", "" if out in (None, "SKIP") else out))
        except AssertionError as e:
            results.append((name, "FAIL", str(e)))
        return fn
    return wrap


def refs(path):
    text = open(path, encoding="utf-8").read()
    return [a or b for a, b in REF.findall(text)]


@check("test_relative_paths")
def _():
    bad = [(f, r) for f in HTML + CSS for r in refs(f) if r.startswith("/") or r.startswith("http://localhost")]
    assert not bad, f"absolute paths: {bad[:5]}"


@check("test_targets_exist")
def _():
    missing = []
    for f in HTML + CSS:
        base = os.path.dirname(f)
        for r in refs(f):
            if r.startswith(("https:", "http:", "mailto:", "data:")) or r.startswith("#"):
                continue
            target = os.path.normpath(os.path.join(base, r.split("#")[0].split("?")[0]))
            if not os.path.exists(target):
                missing.append((f, r))
    for f in HTML:
        text = open(f, encoding="utf-8").read()
        ids = set(re.findall(r'id="([^"]+)"', text))
        for a in re.findall(r'href="#([^"]+)"', text):
            if a not in ids:
                missing.append((f, "#" + a))
        for page, a in re.findall(r'href="([^"#]+\.html)#([^"]+)"', text):
            if os.path.exists(page) and f'id="{a}"' not in open(page, encoding="utf-8").read():
                missing.append((f, f"{page}#{a}"))
    assert not missing, f"missing targets: {missing[:8]}"


@check("test_privacy_strings")
def _():
    assert FORBIDDEN, "tests/forbidden.local.txt is missing or empty"
    hits = []
    text_ext = (".html", ".css", ".js", ".md", ".py", ".cjs", ".txt", ".svg", ".json", ".gitignore")
    scan = set(TEXT + [t for t in TRACKED if t.endswith(text_ext) and "forbidden.local" not in t])
    for f in sorted(scan):
        if os.path.exists(f):
            text = open(f, encoding="utf-8").read()
            hits += [(f, w) for w in FORBIDDEN if w.lower() in text.lower()]
    assert not hits, f"forbidden strings: {hits}"


@check("test_og_absolute")
def _():
    for f in HTML:
        text = open(f, encoding="utf-8").read()
        for prop in ("og:image", "og:url"):
            m = re.search(r'property="%s" content="([^"]+)"' % prop, text)
            assert m, f"{f}: missing {prop}"
            assert m.group(1).startswith("https://vidhursh-rec.github.io/carebridge/"), f"{f}: {prop} not absolute"


@check("test_size_budget")
def _():
    files = [p for p in glob.glob("**/*", recursive=True) if os.path.isfile(p) and not p.startswith((".git", ".superpowers", "tests", "tools", "shots"))]
    total = sum(os.path.getsize(p) for p in files)
    big = [(p, os.path.getsize(p)) for p in files if p.lower().endswith((".jpg", ".jpeg", ".png", ".webp")) and os.path.getsize(p) > 600_000]
    assert total < 8_000_000, f"site is {total} bytes"
    assert not big, f"images over 600 KB: {big}"


@check("test_video_attrs")
def _():
    vids = [(f, v) for f in HTML for v in re.findall(r"<video[^>]*>.*?</video>", open(f, encoding="utf-8").read(), re.S)]
    if not vids:
        return "SKIP"
    for f, v in vids:
        for attr in ("muted", "playsinline", "controls"):
            assert re.search(rf"\b{attr}\b", v), f"{f}: <video> missing {attr}"
        assert ".mp4" in v, f"{f}: <video> has no .mp4 source"


@check("test_layout_no_overflow")
def _():
    if not HTML:
        return "SKIP"
    script = os.path.join(ROOT, "tests", "layout.cjs")
    r = subprocess.run(["node", script, ROOT] + HTML, capture_output=True, text=True, timeout=180)
    assert r.returncode == 0, f"layout runner failed: {r.stderr.strip()[:300]}"
    bad = [x for x in json.loads(r.stdout) if x["scrollWidth"] > x["width"] or x["scrollHeight"] > x["height"]]
    assert not bad, f"page overflows the viewport (only the article pane may scroll): {bad}"


for name, status, msg in results:
    print(f"{status} {name}" + (f": {msg}" if msg else ""))
sys.exit(1 if any(s == "FAIL" for _, s, _ in results) else 0)
