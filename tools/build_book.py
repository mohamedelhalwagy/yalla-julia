# -*- coding: utf-8 -*-
"""
Yalla, Julia! -- Hocharabisch-Ausgabe -- main book builder.

Builds web/index.html from book_fusha.py, reusing build_app's rendering.
Audio: Google Translate voice (captured & embedded) for all Fus'ha strings,
ar-EG-ShakirNeural for Am Mahmouds Masri-Ecke.

Usage:  python3 tools/build_book.py
"""
import base64
import json
import os
import subprocess
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_app as B
from book_fusha import CHAPTERS

VOICE_FALLBACK = "ar-SA-ZariyahNeural"   # only if Google capture fails
VOICE_MASRI = "ar-EG-ShakirNeural"
OUT = os.path.join(B.ROOT, "docs", "index.html")


# ---- collect Arabic strings + per-string voice -----------------------------
_all, _voice_of = [], {}
for ch in CHAPTERS:
    for b in ch["blocks"]:
        t = b.get("type")
        if t == "letter":
            _all.append(b["letter"])
            _all += [e["arabic"] for e in b["examples"]]
        elif t == "vocab":
            _all += [w["arabic"] for w in b["words"]]
        elif t == "quiz":
            _all += [it["arabic"] for it in b["items"]]
        elif t == "atable":
            cols = b.get("ar_col", [])
            cols = cols if isinstance(cols, list) else [cols]
            for r in b["rows"]:
                _all += [r[ci] for ci in cols]
        elif t == "masri":
            _all.append(b["arabic"])
            _voice_of[b["arabic"]] = VOICE_MASRI
        elif t == "closing":
            _all.append(b["arabic"])

AUDIO_ID = {s: f"b{i}" for i, s in enumerate(dict.fromkeys(_all))}
B.AUDIO_ID = AUDIO_ID          # render helpers now resolve our ids


def gen(text, out, voice):
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        return
    subprocess.run(
        [sys.executable, "-m", "edge_tts", "--voice", voice,
         "--text", text, "--write-media", out],
        check=True, capture_output=True,
    )


def google_gen(text, out, tries=3):
    """Capture Google Translate's voice. Cached; falls back to edge-tts on failure."""
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        return "google"
    q = urllib.parse.quote(text)
    url = (f"https://translate.google.com/translate_tts?ie=UTF-8&client=gtx"
           f"&tl=ar&total=1&idx=0&textlen={len(text)}&q={q}")
    ua = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
          "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")
    for t in range(tries):
        try:
            subprocess.run(
                ["curl", "-s", "-f", "--max-time", "20", "-A", ua, "-o", out, url],
                check=True, capture_output=True,
            )
            if os.path.getsize(out) > 1000:
                time.sleep(0.6)          # be gentle with the endpoint
                return "google"
        except subprocess.CalledProcessError:
            time.sleep(1.5 * (t + 1))
    gen(text, out, VOICE_FALLBACK)
    return "fallback"


# ---- custom renderers -------------------------------------------------------
_orig_render_block = B.render_block


def render_block(b):
    t = b.get("type")
    if t == "atable":
        cols = b.get("ar_col", [])
        cols = cols if isinstance(cols, list) else [cols]
        head = "".join(f"<th>{B.esc(c)}</th>" for c in b["header"])
        rows = ""
        for r in b["rows"]:
            cells = ""
            for ci, c in enumerate(r):
                if ci in cols and B.T(c):
                    cells += f"<td>{B.ar_span(c)}</td>"
                else:
                    cells += f"<td>{B.esc(c)}</td>"
            rows += f"<tr>{cells}</tr>"
        note = f'<div class="note">{B.esc(b["note"])}</div>' if b.get("note") else ""
        return (f'<div class="tbl"><table><thead><tr>{head}</tr></thead>'
                f'<tbody>{rows}</tbody></table>{note}</div>')
    if t == "masri":
        return (f'<div class="callout taxi"><div class="co-t"><span class="co-i">🚕</span>'
                f'Am Mahmouds Masri-Ecke</div><div class="co-b">{B.ar_span(b["arabic"])}'
                f'<span class="lat" style="margin-left:8px">{B.esc(b["t"])}</span>'
                f'<div style="margin-top:8px">{B.esc(b["text"])}</div></div></div>')
    return _orig_render_block(b)


B.render_block = render_block   # build_chapter() resolves via module globals


# ---- build ------------------------------------------------------------------
def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    bodies, navs = [], []
    for ch in CHAPTERS:
        bodies.append(B.build_chapter(ch))
        navs.append(f'<a href="#{ch["id"]}" data-c="{ch["id"]}">'
                    f'{B.esc(ch["teaser"].split("—")[0].strip())}</a>')
    body_html = "\n".join(bodies)
    nav_html = "\n".join(navs)

    cache = B.SITE_CACHE
    os.makedirs(cache, exist_ok=True)
    print(f"Capturing {len(AUDIO_ID)} clips (Google voice; Shakir for Masri-Ecke)...")
    audio_json = {}
    src = {"google": 0, "fallback": 0, "masri": 0}
    for s, aid in AUDIO_ID.items():
        mp3 = os.path.join(cache, aid + ".mp3")
        if _voice_of.get(s) == VOICE_MASRI:
            gen(s, mp3, VOICE_MASRI)
            src["masri"] += 1
        else:
            src[google_gen(s, mp3)] += 1
        with open(mp3, "rb") as f:
            audio_json[aid] = {
                "dataUri": "data:audio/mpeg;base64," + base64.b64encode(f.read()).decode(),
                "text": s,
            }
    print(f"Audio sources: {src}")

    doc = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=yes">
<meta name="theme-color" content="#1B7F79">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Yalla Julia">
<title>Yalla, Julia! — Hocharabisch · Band 1</title>
<link rel="manifest" href="manifest.json">
<link rel="icon" type="image/png" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;600;700&display=swap" rel="stylesheet">
<style>{B.CSS}</style>
</head>
<body>
<header class="topbar"><h1>🐪 Yalla, Julia!</h1><div class="sub">Hocharabisch · الفُصْحى · Band 1</div></header>
<nav class="navbar">{nav_html}</nav>
{body_html}
<div class="chap" style="text-align:center;color:#667;font-size:.85rem;padding:10px 16px 30px">
— weitere Teile folgen · Band wächst weiter —
</div>

<div id="flash">
  <div class="fcard"><div class="finner">
    <div class="fside f-front"><div class="f-ar"></div><div class="f-t"></div></div>
    <div class="fside f-back"><div class="f-ar"></div><div class="f-t"></div></div>
  </div></div>
  <div class="f-footer">
    <span class="f-count">1 / 1</span>
    <span>🃏 tippe auf die Karte, um zu drehen</span>
    <button class="fbtn close" onclick="closeFlash()">✕</button>
  </div>
  <div class="f-btns">
    <button class="fbtn know" onclick="next()">✓ Kenn ich</button>
    <button class="fbtn dont" onclick="next()">↻ Nochmal</button>
    <button class="fbtn close" onclick="closeFlash()">Beenden</button>
  </div>
</div>

<script>window.__AUDIO__={json.dumps(audio_json, ensure_ascii=False)};</script>
<script>{B.JS}</script>
</body>
</html>
"""
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"Wrote {OUT} ({os.path.getsize(OUT) // 1024} KB)")


if __name__ == "__main__":
    main()
