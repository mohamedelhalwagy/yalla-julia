YALLA, JULIA! -- Arabisch fuer Aegypten -- Band 1 (v2.0, HTML-App)
====================================================================

WAS SICH IN v2.0 GRUNDLEGEND GEAENDERT HAT
--------------------------------------------
v2.0 ist keine LaTeX/PDF-Minimalfassung mehr, sondern eine interaktive
HTML-App. Das behebt die vier Kernprobleme der alten Version auf einen Schlag:

1.  AEgyptische Aussprache (echt!)
    Statt Google-Translate-Links (die alles als steifes Hocharabisch
    vorlesen) wird JEDES arabische Wort im Voraus mit einer echten
    aegyptischen Stimme eingesprochen (Microsoft Edge-TTS, "ar-EG-Salma-
    Neural") und direkt in die App eingebettet. Kein Internet und kein
    Google mehr noetig -- alles liegt in einer einzigen Datei.

2.  Saubere, einfache Schrift
    Die Buchstaben werden in "Noto Naskh Arabic" angezeigt -- die klare,
    moderne Lehrbuch-Schrift (kein kompliziertes Ruq'ah mehr). Ideal fuer
    jemanden, der arabische Buchstaben noch nie gesehen hat. Faellt die
    Schrift weg, nutzt die App automatisch eine System-Schrift auf dem Geraet.

3.  Keine Fotos mehr -- nur Emojis
    Das Bisso-Foto ist raus. Die Charaktere (Am Mahmoud 🚕, Bisso 🐈)
    erscheinen jetzt als einheitliche Emojis auf JEDER Seite. Kein
    Aufwand zum Pflegen, ueberall das gleiche Design.

4.  Design & Interaktion
    Warmes Farbschema, runde Karten, ein oben fixiertes Kapitel-Menue und
    ein Uebungs-Modus ("Karte umdrehen"), in dem Julia die Woerter als
    Karteikarten wiederholen kann.

5.  JEDES Wort hat ein Lautsprecher-Symbol
    Es gibt keine "Herz"-Platzhalter mehr. Jedes arabische Wort (auch die
    einzelnen Buchstaben) hat automatisch echten aegyptischen Ton.

WIE DU DIE APP BAUEST (auf einem Mac oder Linux-Computer)
---------------------------------------------------------
Das fertige Ergebnis liegt schon da:  web/yalla.html
Einfach diese EINE Datei auf Julias Handy/Computer oeffnen (Doppelklick).
Fertig. Kein Server, kein Internet.

Neu bauen (wenn du Inhalte aenderst):
    pip3 install --user edge-tts
    python3 tools/build_app.py

WIE DU INHALTE AENDERST
------------------------
Der ganze Buchtext steckt in  tools/content.py  (strukturierte Daten).
Inhalt anpassen -> obigen Build-Befehl ausfuehren -> web/yalla.html ist neu.

DIE ALTEN LATEX-DATEIEN (PDF)
------------------------------
main.tex, yalla.sty und content/*.tex bleiben unveraendert im Repo und
lassen sich weiterhin per XeLaTeX zu einem Druck-PDF kompilieren. Der HTML-
App ist jetzt aber die Haupt-, interaktive Version.

FEEDBACK-SCHLEIFE
-------------------
Wenn Julia Band 1 durchgearbeitet hat: einfach Mohamed Bescheid sagen,
was gut/schlecht funktioniert hat -- dann geht's weiter mit Band 2.
Fuer Band 2 einfach tools/content.py erweitern und neu bauen.
