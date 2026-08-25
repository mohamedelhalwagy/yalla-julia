# 🐪 Yalla, Julia! — Hocharabisch · Band 1

Interaktives Arabisch-Lehrbuch (الفُصْحى / Hocharabisch) mit voller Vokalierung
(Tashkeel), eingebettetem Audio (Google-Stimme) und Flashcard-Modus.

**Lesen & hören:** https://mohamedelhalwagy.github.io/yalla-julia/

### Auf dem iPhone installieren
1. URL in **Safari** öffnen
2. Teilen-Button → **„Zum Home-Bildschirm"**
3. Fertig — funktioniert danach komplett offline

### Struktur
| Datei | Inhalt |
|-------|--------|
| `index.html` | **Das Buch** (Hocharabisch-Ausgabe) — wird bei jedem Kapitel neu gebaut |
| `masri.html` | Archiv: die alte Masri-Ausgabe (Band 1, Dialekt) |
| `yalla.html` | Weiterleitung zur neuen Ausgabe (Alte-Installationen kompatibel) |
| `tts-test.html` | Stimmen-Vergleich (Zariyah vs. Hamed vs. Google) |

### Bauen
```
python3 tools/build_book.py
```
- Inhalt: `tools/book_fusha.py` (einzige Datei, die man für neue Kapitel editiert)
- Audio: Google-Translate-Stimme wird pro Satz erfasst, gecacht (`web/_audio`)
  und als Base64 eingebettet; Masri-Ecke spricht `ar-EG-ShakirNeural`;
  Fallback: `ar-SA-ZariyahNeural`
- Das Buch wächst Kapitel für Kapitel — Julia installiert einmal, Updates kommen automatisch.
