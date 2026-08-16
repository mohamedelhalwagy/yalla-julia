YALLA, JULIA! -- Arabisch fuer Aegypten -- Band 1 (v1.1, Bugfix-Version)
==========================================================================

WAS SICH GEAENDERT HAT (v1.0 -> v1.1)
---------------------------------------
- FIX: "Scheherazade New" war auf Overleaf nicht installiert und liess den
  Build fehlschlagen (fatal fontspec error) -- das war die Ursache fuer die
  fehlenden einzelnen Buchstaben, die kaputte Formatierung danach und die
  fehlenden Aussprache-Icons. Jetzt gibt es einen automatischen Fallback auf
  eine garantiert vorhandene Schrift (Amiri), der niemals fehlschlaegt.
- Ein paar zu fortgeschrittene/foermliche Beispielwoerter (Fuchs, "Hadith")
  wurden durch einfachere Alltagswoerter ersetzt (Kuehlschrank, "viel").
  Teil 0 wurde umformuliert: der Fokus liegt jetzt klar auf normalem,
  gesprochenem Alltagsarabisch statt auf der Fusha/Masri-Unterscheidung.
- Aussprache-Icon ist jetzt farbig (teal) und etwas groesser, leichter zu sehen.

WIE DU DAS KOMPILIERST (Overleaf)
----------------------------------
1. Neues Overleaf-Projekt -> "Upload Project" -> diese ZIP-Datei hochladen
   (oder die alten Dateien im bestehenden Projekt ersetzen).
2. WICHTIG: Menu (oben links) -> Compiler -> auf "XeLaTeX" umstellen.
3. Kompiliere ZUERST smoke_test.tex als Hauptdokument. Pruefe besonders:
   erscheint der einzelne Buchstabe "ت" sichtbar? Das war genau der Bug.
4. Wenn der Smoke-Test sauber aussieht: main.tex als Hauptdokument waehlen.

WIE DIE AUSSPRACHE-LINKS FUNKTIONIEREN
----------------------------------------
Jedes Vokabel-Wort hat ein tuerkisfarbenes Lautsprecher-Symbol daneben.
Antippen im PDF (am Handy oder im Browser, mit Internetverbindung) oeffnet
Google Translate mit dem Wort schon eingetragen -- dort auf das
Lautsprecher-Symbol tippen, um es zu hoeren. Das ist Hocharabisch-
Standardaussprache (Google-TTS), nicht der aegyptische Akzent. Woerter mit
Herz-Symbol warten auf Mohameds eigene Aufnahme (spaetere Version).

WAS NOCH AUSSTEHT
-------------------
- Portraet von "Am Mahmoud" und Cover-Illustration (Bild-Generierung wartet
  auf Freigabe im Tool)
- Ein paar Audio-Aufnahmen von Mohamed fuer die Herz-markierten Phrasen

FEEDBACK-SCHLEIFE
-------------------
Wenn Julia Band 1 durchgearbeitet hat: einfach Mohamed Bescheid sagen,
was gut/schlecht funktioniert hat -- dann geht's weiter mit Band 2.
