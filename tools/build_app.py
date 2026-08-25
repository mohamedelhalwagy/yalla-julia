# -*- coding: utf-8 -*-
"""
Yalla, Julia! -- Band 1 -- Build script.

Reads tools/content.py, generates an Egyptian voice (ar-EG-SalmaNeural) for
every distinct Arabic string via edge-tts, base64-embeds the MP3s, and writes
a single self-contained HTML app to docs/index.html (served by GitHub Pages).
The edge-tts mp3 cache lives in web/_audio (not shipped).

Usage:
    python3 tools/build_app.py

Requirements:
    pip3 install --user edge-tts
"""

import base64
import html
import json
import os
import subprocess
import sys

from content import CHAPTERS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "docs")           # build cache + final html
OUT_FILE = os.path.join(ROOT, "docs", "index.html")   # served by GitHub Pages (from main branch, /docs)
SITE_CACHE = os.path.join(ROOT, "docs", "_audio")     # edge-tts cache, not shipped

VOICE = "ar-EG-SalmaNeural"   # Egyptian female voice
# VOICE = "ar-EG-ShakirNeural"  # male alternative


def _norm_ar(s):
    return " ".join(str(s).split()).strip()


AUDIO_ID = {}   # the Arabic string -> stable id (a0, a1, ...)
_all_strings = []
for _ch in CHAPTERS:
    for _b in _ch["blocks"]:
        _t = _b.get("type")
        if _t == "letter":
            # the letter glyph itself also gets an id
            _all_strings.append(_b["letter"])
            for _e in _b["examples"]:
                _all_strings.append(_e["arabic"])
        elif _t == "vocab":
            for _w in _b["words"]:
                _all_strings.append(_w["arabic"])
        elif _t == "quiz":
            for _it in _b["items"]:
                _all_strings.append(_it["arabic"])
        elif _t == "dialogue":
            for _ln in _b["lines"]:
                _all_strings.append(_ln["arabic"])
        elif _t == "closing":
            _all_strings.append(_b["arabic"])
        elif _t == "tabledata":
            pass

for _i, _s in enumerate(dict.fromkeys(_all_strings)):
    AUDIO_ID[_s] = f"a{_i}"


def T(s):
    return AUDIO_ID.get(_norm_ar(s))


def generate_audio(text, out_mp3):
    if os.path.exists(out_mp3) and os.path.getsize(out_mp3) > 1000:
        return
    subprocess.run(
        [sys.executable, "-m", "edge_tts", "--voice", VOICE,
         "--text", text, "--write-media", out_mp3],
        check=True, capture_output=True,
    )


def data_uri_for(ar):
    aid = AUDIO_ID[ar]
    mp3 = os.path.join(SITE_CACHE, aid + ".mp3")
    os.makedirs(SITE_CACHE, exist_ok=True)
    generate_audio(ar, mp3)
    with open(mp3, "rb") as f:
        return "data:audio/mpeg;base64," + base64.b64encode(f.read()).decode()


def esc(s):
    return html.escape(str(s), quote=True)


def spk(aid):
    return f'<button class="spk" data-id="{aid}" aria-label="Anhören">🔊</button>'


def ar_span(ar, aid=None):
    aid = aid or T(ar)
    return f'<span class="ar" dir="rtl">{esc(ar)}</span>{spk(aid)}'


# --------------------------------------------------------------------------
def render_block(b):
    t = b.get("type")

    if t == "h1":
        return f'<div class="chaphead">{esc(b["text"])}</div>'
    if t == "h2":
        return f'<h2 class="sechead">{esc(b["text"])}</h2>'
    if t == "p":
        return f'<p class="prose">{esc(b["text"])}</p>'
    if t == "callout":
        return (f'<div class="callout {esc(b.get("variant","tip"))}">'
                f'<div class="co-t"><span class="co-i">{b.get("icon","")}</span>{esc(b.get("title",""))}</div>'
                f'<div class="co-b">{esc(b["text"])}</div></div>')
    if t == "table":
        rows = "".join(f'<tr>{"".join(f"<td>{esc(c)}</td>" for c in r)}</tr>' for r in b["rows"])
        note = (f'<div class="note">{esc(b["note"])}</div>' if b.get("note") else "")
        return (f'<div class="tbl"><table><thead><tr>'
                f'{"".join(f"<th>{esc(c)}</th>" for c in b["header"])}</tr></thead>'
                f'<tbody>{rows}</tbody></table>{note}</div>')
    if t == "legende":
        items = "".join(
            f'<li><span class="lg-i">{i["icon"]}</span> {esc(i["text"])}</li>'
            for i in b["items"])
        return f'<ul class="legende">{items}</ul>'
    if t == "letter":
        ex = "".join(f'<div class="ex"><span class="pos">{esc(e["pos"])}</span>'
                     f'{ar_span(e["arabic"])}'
                     f'<span class="lat">{esc(e["t"])}</span>'
                     f'<span class="mea">{esc(e["meaning"])}</span></div>'
                     for e in b["examples"])
        dots = f'<p class="dots">{esc(b["dots"])}</p>' if b.get("dots") else ""
        return (f'<div class="letter">'
                f'<div class="lc-row"><span class="big">{esc(b["letter"])}</span>'
                f'{spk(T(b["letter"]))}<span class="lname">{esc(b["name"])}</span></div>'
                f'{dots}{ex}</div>')
    if t == "vocab":
        title = f'<div class="vocab-title">{esc(b["title"])}<button class="playall" onclick="playAll(this)">▶ Alle anhören</button></div>' if b.get("title") else ""
        cards = "".join(
            f'<div class="vc">{ar_span(w["arabic"])}'
            f'<span class="lat">{esc(w["t"])}</span>'
            f'<span class="mea">{esc(w["meaning"])}</span></div>'
            for w in b["words"])
        return f'<div class="vocab">{title}{cards}</div>'
    if t == "quiz":
        items = "".join(f'<div class="qitem">'
                        f'<div class="qrow">{ar_span(it["arabic"])}'
                        f'<span class="qmeta">{esc(it["t"])} · {esc(it["meaning"])}</span></div>'
                        f'<button class="qshow" data-a="{esc(it["answer"])}">Antwort zeigen</button>'
                        f'<div class="qans">{esc(it["answer"])}</div></div>'
                        for it in b["items"])
        return f'<div class="quiz">{items}</div>'
    if t == "dialogue":
        lines = "".join(f'<div class="dl"><div class="dl-who">{esc(ln["who"])}</div>'
                        f'<div class="dl-body">{ar_span(ln["arabic"])}'
                        f'<div class="dl-lat">{esc(ln["t"])}</div>'
                        f'<div class="dl-ger">{esc(ln["german"])}</div></div></div>'
                        for ln in b["lines"])
        return f'<div class="dialogue">{lines}</div>'
    if t == "numrow":
        cells = "".join(f'<div class="nc"><span class="nr">{esc(d)}</span>'
                        f'<span class="nl">{esc(l)}</span></div>'
                        for d, l in zip(b["digits"], b["latin"]))
        return f'<div class="numrow">{cells}</div>'
    if t == "closing":
        return (f'<div class="closing"><span class="bigcl">{esc(b["arabic"])}</span>'
                f'{spk(T(b["arabic"]))}'
                f'<div class="cl-lat"><i>{esc(b["latin"])}</i> — {esc(b["latin_text"])}</div></div>')
    return ""


# --------------------------------------------------------------------------
# CSS / JS templates
# --------------------------------------------------------------------------
CSS = """
:root{
  --teal:#1B7F79; --sand:#E8C07D; --red:#C1440E; --night:#123C4A;
  --pale:#FBF4E4; --ink:#22333B;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
     background:var(--pale);color:var(--ink);line-height:1.55;padding-bottom:90px}
.wrap{max-width:760px;margin:0 auto}

/* Arabic text */
.ar{font-size:1.5rem;font-weight:600;direction:rtl;color:var(--night);font-family:"Noto Naskh Arabic","Scheherazade",serif}
.big{font-size:3.4rem;direction:rtl;color:var(--night);font-family:"Noto Naskh Arabic","Scheherazade",serif}
.bigcl{font-size:2.6rem;direction:rtl;color:var(--red);font-weight:700;font-family:"Noto Naskh Arabic","Scheherazade",serif}

/* speaker */
button.spk{border:none;background:none;cursor:pointer;font-size:1.5rem;vertical-align:middle;transition:transform .1s}
button.spk:active{transform:scale(.85)}
.lat{font-style:italic;color:#445}
.mea{color:var(--red);font-weight:600}

/* header */
.topbar{position:sticky;top:0;z-index:50;background:linear-gradient(135deg,var(--teal),var(--night));
  color:#fff;padding:14px 16px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.2)}
.topbar h1{font-size:1.5rem}
.topbar .sub{font-size:.85rem;opacity:.92;margin-top:2px}

/* nav */
.navbar{position:sticky;top:0;z-index:40;background:var(--night);display:flex;gap:6px;
  overflow-x:auto;padding:8px 10px;-webkit-overflow-scrolling:touch}
.navbar a{color:#dce9e7;text-decoration:none;font-size:.72rem;font-weight:600;white-space:nowrap;
  padding:6px 10px;border-radius:20px;background:rgba(255,255,255,.08)}
.navbar a.active{background:var(--red)}

/* chapter */
.chap{padding:6px 16px}
.chaphead{font-size:1.5rem;font-weight:800;color:var(--night);margin:20px 0 6px;
  border-left:6px solid var(--teal);padding-left:12px}
.sechead{font-size:1.15rem;color:var(--teal);margin:22px 0 8px}
.prose{margin:10px 0;font-size:1.02rem}

/* callouts */
.callout{border-radius:14px;padding:14px 16px;margin:16px 0;box-shadow:0 2px 6px rgba(0,0,0,.05)}
.callout .co-t{font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:8px}
.callout .co-i{font-size:1.3rem}
.callout.tip{background:color-mix(in srgb,var(--sand) 30%,#fff);border:1px solid var(--red)}
.callout.laugh{background:color-mix(in srgb,var(--teal) 14%,#fff);border:1px solid var(--teal)}
.callout.taxi{background:#fff;border:1px solid var(--red)}
.callout.taxi .co-t{color:var(--red)}
.callout.bisso{background:#fff;border:1px solid var(--teal)}
.callout.bisso .co-t{color:var(--teal)}
.callout.checkpoint{background:color-mix(in srgb,var(--sand) 40%,#fff);border:1px solid var(--night)}
.callout.ibm{background:var(--night);color:#fff;border:1px solid var(--night)}
.callout.ibm .co-t{color:var(--sand)}

/* tables */
.tbl{margin:14px 0}
table{width:100%;border-collapse:collapse;background:#fff;border-radius:10px;overflow:hidden;
  box-shadow:0 1px 4px rgba(0,0,0,.06)}
th{background:var(--teal);color:#fff;text-align:left;padding:8px 10px;font-size:.85rem}
td{padding:8px 10px;border-bottom:1px solid #eee;font-size:.9rem}
tr:last-child td{border-bottom:none}
.note{font-size:.8rem;color:#667;margin-top:6px;font-style:italic}

/* legende */
.legende{list-style:none}
.legende li{background:#fff;border-radius:10px;padding:10px 14px;margin:8px 0;display:flex;
  align-items:center;gap:12px;box-shadow:0 1px 4px rgba(0,0,0,.05)}
.lg-i{font-size:1.6rem}

/* letter */
.letter{background:#fff;border-radius:16px;padding:18px;margin:16px 0;box-shadow:0 3px 10px rgba(0,0,0,.07)}
.lc-row{display:flex;align-items:center;gap:14px}
.lname{font-style:italic;color:var(--teal);font-size:1.1rem}
.dots{margin:8px 4px 6px;color:#445}
.ex{display:flex;align-items:baseline;flex-wrap:wrap;gap:6px 12px;padding:8px 4px;border-top:1px dashed #ddd}
.pos{font-size:.7rem;background:var(--sand);color:var(--night);border-radius:8px;padding:2px 8px;font-weight:700}

/* vocab */
.vocab{margin:10px 0}
.vocab-title{font-weight:800;color:var(--teal);margin:14px 0 6px}
.vc{background:#fff;border-radius:14px;padding:14px 16px;margin:10px 0;box-shadow:0 2px 6px rgba(0,0,0,.06);
  display:flex;align-items:center;gap:8px 12px;flex-wrap:wrap}
.vc .ar{flex:1 1 auto}

/* quiz */
.qitem{background:#fff;border-radius:12px;padding:14px;margin:10px 0;box-shadow:0 2px 6px rgba(0,0,0,.05)}
.qrow{display:flex;align-items:center;flex-wrap:wrap;gap:8px}
.qmeta{font-style:italic;color:#667;font-size:.9rem}
.qshow{margin-top:6px;border-radius:20px;border:1px solid var(--teal);background:none;color:var(--teal);
  font-weight:700;padding:6px 14px;cursor:pointer}
.qans{margin-top:8px;font-weight:800;color:var(--red);font-size:2rem;display:none;text-align:center}

/* dialogue */
.dialogue{background:var(--night);border-radius:16px;padding:16px;color:#fff}
.dl{display:flex;gap:12px;margin:14px 0}
.dl-who{font-weight:800;color:var(--sand);min-width:96px;font-size:.85rem}
.dl-body{flex:1}
.dl-body .ar{font-size:1.4rem;color:#fff}
.dl-lat{font-style:italic;font-size:.85rem;color:#cfdfdd}
.dl-ger{font-size:.82rem;color:#a9bfbd}

/* numrow */
.numrow{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:16px 0}
.nc{background:#fff;border-radius:12px;padding:10px;width:68px;text-align:center;box-shadow:0 2px 6px rgba(0,0,0,.06)}
.nr{display:block;font-size:2rem;direction:rtl;color:var(--night);font-family:"Noto Naskh Arabic","Scheherazade",serif}
.nl{font-size:.85rem;color:var(--red);font-weight:700}

/* closing */
.closing{text-align:center;margin:30px 0}
.cl-lat{margin-top:6px;color:var(--teal);font-weight:600}

/* chapter footer / flashcard launch */
.chapfoot{margin:8px 0}
.flashbtn{display:block;width:100%;border:none;background:var(--teal);color:#fff;font-weight:800;
  font-size:1rem;padding:14px;border-radius:14px;cursor:pointer;margin-top:6px}
.flashbtn:active{transform:scale(.99)}

/* flashcard overlay */
#flash{position:fixed;inset:0;background:var(--night);z-index:100;display:flex;flex-direction:column;
  align-items:center;justify-content:center;color:#fff;padding:20px;transform:translateY(100%)}
#flash.open{transform:translateY(0)}
.fcard{perspective:1000px;width:min(90vw,360px);height:280px}
.finner{position:relative;width:100%;height:100%;transition:transform .6s;transform-style:preserve-3d;cursor:pointer}
.finner.flipped{transform:rotateY(180deg)}
.fside{position:absolute;inset:0;backface-visibility:hidden;border-radius:20px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:10px;padding:20px}
.f-front{background:var(--card);color:var(--night)}
.f-back{background:var(--red);color:#fff;transform:rotateY(180deg)}
.f-ar{font-size:2.4rem;direction:rtl;font-family:"Noto Naskh Arabic","Scheherazade",serif}
.f-t{font-style:italic;font-size:1rem}
.f-footer{display:flex;justify-content:space-between;width:min(92vw,380px);margin-top:20px;align-items:center}
.f-count{font-size:.9rem}
.f-btns{display:flex;gap:10px}
.fbtn{border-radius:30px;border:none;padding:11px 20px;font-weight:800;cursor:pointer;font-size:.92rem}
.fbtn.know{background:var(--teal);color:#fff}
.fbtn.dont{background:var(--sand);color:var(--night)}
.fbtn.close{background:none;color:#cfdfdd;border:1px solid #456}

/* tempo + play-all */
.ratebtn{position:absolute;right:12px;top:14px;border:none;background:rgba(255,255,255,.16);
  color:#fff;border-radius:20px;padding:6px 13px;font-size:.8rem;font-weight:700;cursor:pointer}
.ratebtn:active{transform:scale(.95)}
.playall{border:none;background:var(--teal);color:#fff;border-radius:16px;padding:6px 13px;
  font-size:.75rem;font-weight:800;cursor:pointer;margin-left:10px;vertical-align:middle}
.playall:active{transform:scale(.95)}
"""

JS = r"""
let AUDIO = window.__AUDIO__;
const player=new Audio(); player.preload='auto';
const _urls={};

// ---- tempo (persisted) ----
let rate=parseFloat(localStorage.getItem('yj_rate')||'1');
const rateBtn=document.getElementById('rateBtn');
function applyRate(){
  player.playbackRate=rate;
  if(rateBtn){ rateBtn.textContent = rate<1 ? '🐢 langsam' : '🐇 normal'; }
}
if(rateBtn){
  rateBtn.addEventListener('click',()=>{
    rate = rate<1 ? 1 : 0.75;
    try{localStorage.setItem('yj_rate',rate);}catch(e){}
    applyRate();
  });
  applyRate();
}

function urlFor(aid){
  if(_urls[aid]) return _urls[aid];
  try{
    const parts=AUDIO[aid].dataUri.split(',');
    const mime=(parts[0].match(/data:(.*?)[;]/)||[,'audio/mpeg'])[1]||'audio/mpeg';
    const bin=atob(parts[1]);
    const bytes=new Uint8Array(bin.length);
    for(let i=0;i<bin.length;i++) bytes[i]=bin.charCodeAt(i);
    _urls[aid]=URL.createObjectURL(new Blob([bytes],{type:mime}));
  }catch(e){ _urls[aid]=AUDIO[aid].dataUri; }
  return _urls[aid];
}

// ---- "Alle anhören" queue ----
let queue=[],qi=0,qPlaying=false,qBtn=null;
function playAll(btn){
  if(qPlaying){ stopQueue(); return; }
  const spks=[...btn.closest('.vocab').querySelectorAll('.spk')];
  queue=spks.map(b=>b.dataset.id).filter(id=>AUDIO[id]);
  if(!queue.length) return;
  qi=0; qPlaying=true; qBtn=btn; btn.textContent='⏹ Stop';
  playQ();
}
function playQ(){
  if(!qPlaying||qi>=queue.length){ stopQueue(); return; }
  play(queue[qi]);
  player.onended=()=>{ qi++; setTimeout(()=>{ if(qPlaying) playQ(); },700); };
}
function stopQueue(){
  qPlaying=false; player.onended=null;
  if(qBtn){ qBtn.textContent='▶ Alle anhören'; qBtn=null; }
}

// ---- progress (persisted) ----
let prog={};
try{ prog=JSON.parse(localStorage.getItem('yj_prog')||'{}'); }catch(e){ prog={}; }
function saveProg(){ try{localStorage.setItem('yj_prog',JSON.stringify(prog));}catch(e){} }
function updateFlashBtns(){
  document.querySelectorAll('.flashbtn').forEach(btn=>{
    const mch=(btn.getAttribute('onclick')||'').match(/'([^']+)'/);
    if(!mch) return;
    const chap=document.querySelector('.chap[data-c="'+mch[1]+'"]');
    if(!chap) return;
    const aids=[...chap.querySelectorAll('.vc .spk')].map(b=>b.dataset.id);
    const known=aids.filter(id=>prog[id]==='know').length;
    btn.textContent = known>0
      ? '🃏 Übe diese Wörter · ✓ '+known+' / '+aids.length
      : '🃏 Übe diese Wörter';
  });
}

function play(aid){
  if(!AUDIO[aid]) return;
  if(qPlaying) stopQueue();
  const u=urlFor(aid);
  player.pause();
  if(player.src!==u){ player.src=u; } else { try{player.currentTime=0;}catch(e){} }
  player.playbackRate=rate;
  player.play().catch(()=>{});
}
document.body.addEventListener('click', e=>{
  const b=e.target.closest('.spk'); if(b) play(b.dataset.id);
  const q=e.target.closest('.qshow'); if(q){ const ans=q.nextElementSibling;
    const vis=ans.style.display==='block'; q.textContent=vis?'Antwort zeigen':'Verstecken';
    ans.style.display=vis?'none':'block'; }
});

// chapter nav active state
const secs=[...document.querySelectorAll('.chap')];
const navs=[...document.querySelectorAll('.navbar a')];
function onScroll(){ let cur=secs[0];
  for(const s of secs){ if(s.getBoundingClientRect().top<=80) cur=s; }
  navs.forEach(n=>n.classList.toggle('active',n.dataset.c===cur.dataset.c)); }
addEventListener('scroll',onScroll); addEventListener('load',onScroll);

// flashcard mode
const flash=document.getElementById('flash');
let deck=[],pos=0,curChap=null;
function openFlash(chid){
  const chap=document.querySelector('.chap[data-c="'+chid+'"]'); if(!chap) return;
  curChap=chid;
  deck=[...chap.querySelectorAll('.vc')].map(v=>({
    ar:v.querySelector('.ar').textContent.trim(),
    lat:v.querySelector('.lat').textContent.trim()||'',
    mea:v.querySelector('.mea').textContent.trim()||'',
    aid:v.querySelector('.ar').nextElementSibling ? v.querySelector('.spk').dataset.id : null
  }));
  if(!deck.length) return;
  for(let i=deck.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[deck[i],deck[j]]=[deck[j],deck[i]];}
  pos=0; flash.classList.add('open'); renderCard();
}
function renderCard(){
  const c=deck[pos];
  document.querySelector('.f-front .f-ar').textContent=c.ar;
  document.querySelector('.f-back .f-ar').textContent=c.lat||'';
  document.querySelector('.f-front .f-t').textContent='tippe, um zu hören';
  document.querySelector('.f-back .f-t').textContent = c.mea || '';
  document.querySelector('.finner').classList.remove('flipped');
  const known=deck.filter(x=>x.aid&&prog[x.aid]==='know').length;
  document.querySelector('.f-count').textContent=(pos+1)+' / '+deck.length+'  ·  ✓ '+known;
  if(c.aid) play(c.aid);
}
function flipCard(){document.querySelector('.finner').classList.toggle('flipped')}
function next(kind){
  if(kind && deck[pos] && deck[pos].aid){ prog[deck[pos].aid]=kind; saveProg(); }
  pos=(pos+1)%deck.length; renderCard();
}
function closeFlash(){flash.classList.remove('open'); updateFlashBtns();}
document.querySelector('.finner').addEventListener('click',flipCard);
updateFlashBtns();

if('serviceWorker' in navigator){navigator.serviceWorker.register('sw.js').catch(()=>{});}
"""

def build_chapter(c):
    """Render all blocks of one chapter, collecting its nav + body."""
    parts = []
    for b in c["blocks"]:
        parts.append(render_block(b))
    body = "\n".join(parts)
    # Only offer flashcards for chapters that have vocab/quiz cards with words
    has_review = any(b.get("type") in ("vocab", "quiz") for b in c["blocks"])
    flash_btn = ('<button class="flashbtn" onclick="openFlash(\'%s\')">🃏 Übe diese Wörter</button>'
                 % c["id"]) if has_review else ""
    return (f'<section class="chap" data-c="{c["id"]}">{body}'
            f'<div class="chapfoot">{flash_btn}</div></section>')


def build_page(body_html, nav_html):
    # Abbreviate nav ids to "T1".. etc for display
    audio_json = json.dumps({aid: {"dataUri": data_uri_for(ar), "text": ar}
                             for ar, aid in AUDIO_ID.items()})
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
<title>Yalla, Julia! — Band 1</title>
<link rel="manifest" href="manifest.json">
<link rel="icon" type="image/png" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="topbar"><h1>🐪 Yalla, Julia!</h1><div class="sub">Arabisch für Ägypten · Band 1</div></header>
<nav class="navbar">{nav_html}</nav>
{body_html}

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
    <button class="fbtn know" onclick="next('know')">✓ Kenn ich</button>
    <button class="fbtn dont" onclick="next('again')">↻ Nochmal</button>
    <button class="fbtn close" onclick="closeFlash()">Beenden</button>
  </div>
</div>

<script>window.__AUDIO__={audio_json};</script>
<script>{JS}</script>
</body>
</html>
"""
    return doc


# --------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    chapter_bodies = []
    navs = []
    for c in CHAPTERS:
        chapter_bodies.append(build_chapter(c))
        navs.append(f'<a href="#{c["id"]}" data-c="{c["id"]}">{esc(c["teaser"].split("—")[0].strip())}</a>')
    body_html = "\n".join(chapter_bodies)
    nav_html = "\n".join(navs)

    print(f"Found {len(AUDIO_ID)} unique Arabic strings to synthesize...")
    os.makedirs(SITE_CACHE, exist_ok=True)
    for ar, aid in AUDIO_ID.items():
        generate_audio(ar, os.path.join(SITE_CACHE, aid + ".mp3"))
    print("Audio synthesized/cached.")

    doc = build_page(body_html, nav_html)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(doc)
    size = os.path.getsize(OUT_FILE) // 1024
    print(f"Wrote {OUT_FILE} ({size} KB)")


if __name__ == "__main__":
    main()
