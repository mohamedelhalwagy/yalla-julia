# -*- coding: utf-8 -*-
"""
A/B/C voice test page: Zariyah vs Hamed vs Google Translate.
Builds web/tts-test.html. Usage: python3 tools/build_tts_test.py
"""
import base64
import json
import os
import subprocess
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "docs", "_audio")
OUT = os.path.join(ROOT, "docs", "tts-test.html")

WORDS = [
    ("بَيْتٌ", "baytun", "ein Haus"),
    ("كِتَابٌ", "kitābun", "ein Buch"),
    ("تُفَّاحَةٌ", "tuffāḥatun", "ein Apfel"),
    ("كُرْسِيٌّ", "kursiyyun", "ein Stuhl"),
    ("النُّورُ", "an-nūru", "das Licht (Sonnenbuchstabe!)"),
    ("البَيْتُ كَبِيرٌ", "al-baytu kabīrun", "Das Haus ist groß."),
]


def gen(text, voice, out):
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        return
    subprocess.run([sys.executable, "-m", "edge_tts", "--voice", voice,
                    "--text", text, "--write-media", out],
                   check=True, capture_output=True)


def datauri(text, voice, aid):
    os.makedirs(CACHE, exist_ok=True)
    mp3 = os.path.join(CACHE, aid + ".mp3")
    gen(text, voice, mp3)
    with open(mp3, "rb") as f:
        return "data:audio/mpeg;base64," + base64.b64encode(f.read()).decode()


def google_datauri(text, aid):
    """Capture Google Translate's voice once (server-side) and embed it."""
    os.makedirs(CACHE, exist_ok=True)
    mp3 = os.path.join(CACHE, aid + ".mp3")
    if not (os.path.exists(mp3) and os.path.getsize(mp3) > 1000):
        q = urllib.parse.quote(text)
        url = (f"https://translate.google.com/translate_tts?ie=UTF-8&client=gtx"
               f"&tl=ar&total=1&idx=0&textlen={len(text)}&q={q}")
        subprocess.run(
            ["curl", "-s", "-f", "-A",
             "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
             "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
             "-o", mp3, url],
            check=True, capture_output=True,
        )
    with open(mp3, "rb") as f:
        return "data:audio/mpeg;base64," + base64.b64encode(f.read()).decode()


cards, embedded = [], {}
for i, (ar, lat, de) in enumerate(WORDS):
    embedded[f"tz{i}"] = datauri(ar, "ar-SA-ZariyahNeural", f"tz{i}")
    embedded[f"th{i}"] = datauri(ar, "ar-SA-HamedNeural", f"th{i}")
    embedded[f"tg{i}"] = google_datauri(ar, f"tg{i}")
    cards.append(f"""
<div class="card">
  <div class="arline">{ar}</div>
  <div class="latline"><i>{lat}</i> — {de}</div>
  <div class="btns">
    <button onclick="play('tz{i}')">🔵 Zariyah</button>
    <button onclick="play('th{i}')">⚫ Hamed</button>
    <button class="g" onclick="play('tg{i}')">🟢 Google</button>
  </div>
</div>""")

doc = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Yalla, Julia! — Stimmen-Test</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;600;700&display=swap" rel="stylesheet">
<style>
body{font-family:-apple-system,system-ui,sans-serif;background:#FBF4E4;color:#22333B;margin:0;padding-bottom:60px}
.top{background:linear-gradient(135deg,#1B7F79,#123C4A);color:#fff;padding:18px;text-align:center}
.top h1{margin:0;font-size:1.3rem} .top p{margin:6px 0 0;font-size:.85rem;opacity:.9}
.card{background:#fff;border-radius:16px;margin:14px;padding:16px;box-shadow:0 2px 8px rgba(0,0,0,.07)}
.arline{font-family:"Noto Naskh Arabic",serif;font-size:2rem;color:#123C4A;direction:rtl;text-align:right}
.latline{font-size:.85rem;color:#445;margin:4px 0 10px}
.btns{display:flex;gap:8px;flex-wrap:wrap}
button{border:none;border-radius:20px;padding:9px 16px;font-weight:700;font-size:.85rem;cursor:pointer;background:#1B7F79;color:#fff}
button.g{background:#2E7D32}
button:active{transform:scale(.96)}
.note{margin:14px;font-size:.8rem;color:#667;font-style:italic}
</style>
</head>
<body>
<div class="top"><h1>🔬 Stimmen-Test — Wer spricht das Tanwīn am besten?</h1>
<p>Tippe pro Wort auf alle drei und vergleiche: hörst du das „-un“ am Ende?</p></div>
__CARDS__
<p class="note">Alle drei Stimmen sind eingebettet — funktioniert komplett offline.</p>
<script>
let cur=null;
function play(id){ if(cur)cur.pause(); cur=new Audio(window.__A__[id]); cur.play().catch(()=>{}); }
window.__A__=__AUDIO_JSON__;
</script>
</body>
</html>
"""
doc = doc.replace("__CARDS__", "".join(cards)).replace("__AUDIO_JSON__", json.dumps(embedded))
with open(OUT, "w", encoding="utf-8") as f:
    f.write(doc)
print("Wrote", OUT, os.path.getsize(OUT) // 1024, "KB")
