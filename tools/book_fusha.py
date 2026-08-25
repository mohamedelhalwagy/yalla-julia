# -*- coding: utf-8 -*-
"""
Yalla, Julia! -- Hocharabisch-Ausgabe (الفُصْحى) -- Band 1 -- structured content.

Dies ist die EINZIGE Datei für den Inhalt des neuen Buches.
Neue Blocktypen (zusätzlich zu build_app.py):
  "atable" -- Tabelle mit Audio in bestimmten Spalten (ar_col: int oder Liste)
  "masri"  -- Am Mahmouds Masri-Ecke (ar-EG-Stimme, Dialekt-Kuriosität)
"""

CHAPTERS = [
    # =========================================================================
    # Teil 0 -- Willkommen
    # =========================================================================
    {
        "id": "teil0",
        "teaser": "Willkommen",
        "blocks": [
            {"type": "h1", "text": "Willkommen, Julia! — أَهْلًا بِكِ"},

            {"type": "p",
             "text": "Liebe Julia, willkommen zur großen Ausgabe. Dieses Buch lehrt dich jetzt "
             "das Hocharabische — الفُصْحى, „die klarste Sprache“. Das ist das Arabisch der "
             "Bücher, der Nachrichten, der Straßenschilder und des Korans: die Sprache mit dem "
             "berühmten, präzisen Grammatik-System. Genau das Richtige für jemanden, der "
             "Grammatik so liebt wie du."},

            {"type": "callout", "variant": "ibm", "title": "Warum Hocharabisch?", "icon": "🏛",
             "text": "Drei gute Gründe: (1) Die Grammatik ist ein Wunderwerk aus klaren Regeln — "
             "Endungen, Fälle, Muster, die sich logisch zusammensetzen. (2) Alles Geschriebene in "
             "der arabischen Welt ist Hocharabisch — wer liest, werft es. (3) Jedes gesprochene "
             "Dialekt-Wort wird später leichter, weil du das Gerüst schon hast. Und die "
             "ägyptische Straße? Die kriegen wir als Dessert — in Am Mahmouds Masri-Ecke."},

            {"type": "h2", "text": "Drei Fakten — in 30 Sekunden verstehst du Arabisch besser "
             "als die meisten Touristen"},
            {"type": "table",
             "header": ["Fakt", "Was es für dich bedeutet"],
             "rows": [
                 ["Arabisch schreibt von rechts nach links",
                  "Dein Auge startet rechts — fühlt sich nach drei Tagen normal an"],
                 ["Es gibt 28 Buchstaben, keine Groß- und Kleinbuchstaben",
                  "Weniger zu lernen als Deutsch! Kein „Substantive groß“-Stress"],
                 ["Kurze Vokale sind kleine Zeichen über/unter den Buchstaben",
                  "Wir setzen sie in diesem Buch auf JEDES Wort — du kannst nichts falsch lesen"],
             ]},

            {"type": "h2", "text": "So liest du dieses Buch"},
            {"type": "legende",
             "items": [
                 {"icon": "🔊", "text": "Jedes arabische Wort hat einen Play-Knopf — klare "
                  "Nachrichtensprecher-Arabisch, mit allen Endungen"},
                 {"icon": "🔤", "text": "Die Umschrift (kitāb, ṭabīb) zeigt dir die Aussprache "
                  "in vertrauten Zeichen"},
                 {"icon": "🚕", "text": "Am Mahmouds Masri-Ecke — so sagt man es auf Kairos "
                  "Straßen (zum Lachen, nicht zum Lernen)"},
                 {"icon": "🐈", "text": "Bisso, die Straßenkatze, hat immer eine Meinung — und "
                  "manchmal eine grammatische"},
                 {"icon": "💡", "text": "Tipps für den Kopf — Merksätze, die bleiben"},
                 {"icon": "🏁", "text": "Checkpoint — kurz prüfen, ob es sitzt"},
                 {"icon": "🃏", "text": "Flashcard-Modus — die Wörter des Kapitels im Test"},
             ]},

            {"type": "callout", "variant": "tip", "title": "Dein Lernrhythmus", "icon": "📅",
             "text": "Zehn Minuten am Tag schlagen drei Stunden am Wochenende. Der Rhythmus: "
             "(1) Das Kapitel einmal laut mitlesen. (2) Jedes 🔊 hören und nachsprechen — "
             "mit dem 🐢-Knopf oben rechts, wenn es zu schnell ist. (3) Die Flashcards des "
             "Kapitels, bis alles ✓ sitzt — der Zähler merkt sich, was du kannst. Mehr "
             "braucht es nicht. Versprochen."},

            {"type": "h2", "text": "Die Umschrift — dein Schlüssel zum Klang"},
            {"type": "p",
             "text": "Wir schreiben Arabisch mit ein paar Sonderzeichen um. Die kennst du zum "
             "Glück schon aus dem Deutschen — hier die komplette Liste:"},
            {"type": "atable",
             "header": ["Zeichen", "Klang", "Arabisch", "Beispiel"],
             "ar_col": [2],
             "rows": [
                 ["ā", "langes aa — wie in „Haa!“", "كِتَابٌ", "kitāb — ein Buch"],
                 ["ī", "langes ii — wie in „Bier“", "كَبِيرٌ", "kabīr — groß"],
                 ["ū", "langes uu — wie in „Uhr“", "نُورٌ", "nūr — Licht"],
                 ["ṭ", "schweres T — Zunge etwas tiefer", "طَبِيبٌ", "ṭabīb — Arzt"],
                 ["ḥ", "scharfes, gehauchtes H", "مِفْتَاحٌ", "miftāḥ — ein Schlüssel"],
                 ["'", "kleiner Knacklaut (Hamza)", "أَهْلًا", "ahlan — willkommen"],
             ],
             "note": "Mehr brauchst du nicht. Alles andere klingt genau wie im Deutschen."},

            {"type": "callout", "variant": "taxi", "title": "Am Mahmoud stellt sich vor", "icon": "🚕",
             "text": "Am Mahmoud fährt seit 30 Jahren Taxi in Kairo, kennt jeden Umweg und ist "
             "der Meinung, dass jeder Preis Verhandlungssache ist — auch der Preis für "
             "Grammatik. In seiner Ecke übersetzt er dir jedes Kapitel in echtes Kairo-Arabisch. "
             "Achtung: Er nimmt keine Endungen mit."},

            {"type": "callout", "variant": "bisso", "title": "Bisso stellt sich vor", "icon": "🐈",
             "text": "Bisso ist eine Straßenkatze mit einer eingekerbten Ohrspitze und starken "
             "Meinungen zu Essensresten, Sonnenplätzen und — wie du noch sehen wirst — zu "
             "grammatikalisch korrektem Sitzverhalten."},

            {"type": "callout", "variant": "checkpoint", "title": "Bereit?", "icon": "🏁",
             "text": "In Teil 1 lernst du deine ersten fünf Buchstaben — und gleich dazu die "
             "drei Grammatik-Geheimnisse, mit denen du deine ersten echten arabischen Wörter "
             "bauen und verstehen kannst. Los!"},

            {"type": "closing", "arabic": "أَهْلًا وَسَهْلًا!", "latin": "ahlan wa-sahlan",
             "latin_text": "Willkommen und sei ganz leicht! — der klassische arabische Gruß"},
        ],
    },

    # =========================================================================
    # Teil 1 -- Buchstaben-Werkstatt I
    # =========================================================================
    {
        "id": "teil1",
        "teaser": "Teil 1 — Werkstatt I",
        "blocks": [
            {"type": "h1", "text": "Teil 1 — Die Buchstaben-Werkstatt I: ب ت ث ن ي"},

            {"type": "p",
             "text": "Fünf Buchstaben, ein Skelett: ب ت ث ن ي sehen sich in der Wortmitte alle "
             "sehr ähnlich — ein kleiner „Zahn“. Was sie unterscheidet, sind nur die Punkte. "
             "Tippe auf jedes Zeichen, um es zu hören."},

            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "Stell dir eine Familie von fünf Geschwistern vor, die alle das gleiche "
             "T-Shirt tragen — man erkennt sie nur an den Punkten, die sie sich ins Gesicht "
             "gemalt haben. Das ist ب ت ث ن ي."},

            # ---------------- die fünf Buchstaben ----------------
            {"type": "letter", "letter": "بَ", "name": "bā — ba",
             "dots": "Ein Punkt darunter. Er sieht aus wie ein kleines Auge, das unter dem "
             "Buchstaben wohnt.",
             "examples": [
                 {"arabic": "بَيْتٌ", "t": "baytun", "meaning": "ein Haus", "pos": "Anfang"},
                 {"arabic": "كَبِيرٌ", "t": "kabīrun", "meaning": "groß", "pos": "Mitte"},
                 {"arabic": "طَبِيبٌ", "t": "ṭabībun", "meaning": "ein Arzt", "pos": "Anfang & Ende"},
             ]},
            {"type": "letter", "letter": "تَ", "name": "tā — ta",
             "dots": "Zwei Punkte darüber — wie zwei kleine Augen, die nach oben schauen.",
             "examples": [
                 {"arabic": "تُفَّاحَةٌ", "t": "tuffāḥatun", "meaning": "ein Apfel (mit Shadda!)", "pos": "Anfang"},
                 {"arabic": "كِتَابٌ", "t": "kitābun", "meaning": "ein Buch", "pos": "Mitte"},
                 {"arabic": "بِنْتٌ", "t": "bintun", "meaning": "ein Mädchen", "pos": "Ende"},
             ]},
            {"type": "letter", "letter": "ثَ", "name": "thā — th (wie in engl. „think“)",
             "dots": "Drei Punkte darüber. Ein seltener Gast — diese zwei Wörter reichen für den Anfang.",
             "examples": [
                 {"arabic": "ثَلَاثَةٌ", "t": "thalāthatun", "meaning": "drei", "pos": "Anfang"},
                 {"arabic": "ثَوْرٌ", "t": "thawrun", "meaning": "ein Stier", "pos": "Anfang"},
             ]},
            {"type": "letter", "letter": "نَ", "name": "nūn — n",
             "dots": "Ein Punkt darüber, tiefere Schale — der Punkt sitzt wie ein Tropfen in einer Schale.",
             "examples": [
                 {"arabic": "نُورٌ", "t": "nūrun", "meaning": "Licht", "pos": "Anfang"},
                 {"arabic": "نَهْرٌ", "t": "nahrun", "meaning": "ein Fluss", "pos": "Anfang"},
                 {"arabic": "لَبَنٌ", "t": "labanun", "meaning": "Milch", "pos": "Ende"},
             ]},
            {"type": "letter", "letter": "يَ", "name": "yā — y / ii",
             "dots": "Zwei Punkte darunter, Schwanz am Ende. Als langer Vokal ii und als "
             "Konsonant y in einem.",
             "examples": [
                 {"arabic": "يَدٌ", "t": "yadun", "meaning": "eine Hand", "pos": "Anfang"},
                 {"arabic": "بَيْتٌ", "t": "baytun", "meaning": "Haus — hier als Diphthong ay", "pos": "Mitte"},
                 {"arabic": "كُرْسِيٌّ", "t": "kursiyyun", "meaning": "ein Stuhl (Shadda + Tanwīn!)", "pos": "Ende"},
             ]},

            # ---------------- Grammatik 1: Lesehilfe Tashkeel ----------------
            {"type": "h2", "text": "Grammatik-Geheimnis 1: Die Vokalzeichen lesen (التَّشْكِيل)"},
            {"type": "p",
             "text": "Kurze Vokale stehen als kleine Zeichen über oder unter dem Buchstaben — "
             "wie Musiknoten. Du musst sie nicht schreiben können, nur mitlesen können. "
             "Hier die komplette Werkzeugliste, immer am Beispiel ب:"},
            {"type": "atable",
             "header": ["Zeichen", "Name", "Klang", "Beispiel"],
             "ar_col": 0,
             "rows": [
                 ["بَ", "Fatha", "kurzes a", "بَ — ba"],
                 ["بِ", "Kasra", "kurzes i", "بِ — bi"],
                 ["بُ", "Damma", "kurzes u", "بُ — bu"],
                 ["بْ", "Sukūn", "kein Vokal", "بْ — b (Pausenzeichen)"],
                 ["بّ", "Shadda", "doppelter Konsonant", "بّ — bb"],
                 ["بٌ", "Tanwīn Damm", "un — „ein“ (unbestimmt!)", "بَيْتٌ — baytun"],
             ],
             "note": "Merksatz für Julia: Doppeltes Zeichen am Wortende = „ein“. "
             "Einfaches Zeichen = „der/die/das“. Das ist das ganze Geheimnis."},

            # ---------------- Grammatik 2: Tanwin ----------------
            {"type": "h2", "text": "Grammatik-Geheimnis 2: Das Tanwīn — das eingebaute „ein“ "
             "(التَّنْوِين)"},
            {"type": "p",
             "text": "Das Arabische hat kein eigenes Wort für „ein/eine“ — es baut die "
             "Unbestimmtheit direkt ins Wort ein: als doppelte Endung, den Tanwīn (تنوين, "
             "„das N-förmige“, weil man ein verstecktes n hört). بَيْتٌ liest sich also "
             "bayt-un — „Haus-un“ = „ein Haus“."},
            {"type": "atable",
             "header": ["Form", "Klang", "Rolle", "Deutsch"],
             "ar_col": 0,
             "rows": [
                 ["بَيْتٌ", "baytun", "Nominativ — der Täter des Satzes", "ein Haus (macht etwas)"],
                 ["بَيْتًا", "baytan", "Akkusativ — das Ziel", "ein Haus (womit/worin?)"],
                 ["بَيْتٍ", "baytin", "Genitiv — nach „von/ in/ auf“", "eines Hauses"],
             ],
             "note": "Keine Panik vor den drei Fällen! Für jetzt reicht: doppeltes Zeichen "
             "gesehen → „ein“ gedacht. Die Fälle kommen später, sanft und mit vielen Beispielen."},

            # ---------------- Grammatik 3: al- ----------------
            {"type": "h2", "text": "Grammatik-Geheimnis 3: ال — der bestimmte Artikel"},
            {"type": "p",
             "text": "Bestimmtheit geht auch: الْ vor das Wort, fertig ist „der/die/das“. "
             "البَيْتُ = al-baytu = „das Haus“. Deutsch hat Artikel nur am Anfang — Arabisch "
             "hat sie am Anfang (ال) UND am Ende (Endung). Doppelt gemoppelt und stolz drauf."},
            {"type": "atable",
             "header": ["unbestimmt", "bestimmt", "Klang", "Deutsch"],
             "ar_col": [0, 1],
             "rows": [
                 ["بَيْتٌ", "البَيْتُ", "baytun → al-baytu", "ein Haus → das Haus"],
                 ["كِتَابٌ", "الكِتَابُ", "kitābun → al-kitābu", "ein Buch → das Buch"],
                 ["نُورٌ", "النُّورُ", "nūrun → an-nūru", "Licht → das Licht"],
             ]},

            # ---------------- Grammatik 4: Sonne & Mond ----------------
            {"type": "h2", "text": "Bonus-Geheimnis: Sonnen- & Mond-Buchstaben ☀️🌙 "
             "(حُرُوف شَمْسِيَّة وَقَمَرِيَّة)"},
            {"type": "p",
             "text": "Jetzt der schönste Trick des Arabischen. Das ال hat ein Geheimnis: Vor "
             "14 „Sonnenbuchstaben“ schmilzt das l hinein — man sieht es noch, aber man hört es "
             "nicht mehr. Stattdessen bekommt der folgende Buchstabe eine Shadda: التُّفَّاحُ "
             "spricht man at-tuffāḥu, nicht „al-tuffāḥu“. Vor den anderen 14 „Mondbuchstaben“ "
             "bleibt das l klar und hörbar: البَيْتُ = al-baytu."},
            {"type": "atable",
             "header": ["Buchstabe", "Typ", "Beispiel", "Gesprochen"],
             "ar_col": [2],
             "rows": [
                 ["ب", "🌙 Mond — l bleibt hörbar", "البَيْتُ", "al-baytu"],
                 ["ي", "🌙 Mond — l bleibt hörbar", "اليَدُ", "al-yadu"],
                 ["ت", "☀️ Sonne — l schmilzt (Shadda!)", "التُّفَّاحُ", "at-tuffāḥu"],
                 ["ث", "☀️ Sonne — l schmilzt (Shadda!)", "الثَّوْرُ", "ath-thawru"],
                 ["ن", "☀️ Sonne — l schmilzt (Shadda!)", "النُّورُ", "an-nūru"],
             ],
             "note": "Von unseren fünf Geschwistern sind ب und ي kühl und mondig, während "
             "ت، ث، ن volle Sonne tanken. Die restlichen 23 Buchstaben kommen in den nächsten "
             "Teilen — dann komplettieren wir die zwei 14er-Familien."},

            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "Die Sonnenbuchstaben sind so heiß, dass das l darin einfach schmilzt wie "
             "Eis in Kairo im Juli. Die Mondbuchstaben bleiben kühl, distanziert und lassen das l "
             "unangetastet — sehr skandinavisch, eigentlich."},

            # ---------------- Vokabeln (Flashcards) ----------------
            {"type": "vocab", "title": "Deine ersten acht Wörter — voll vokalisiert",
             "words": [
                 {"arabic": "بَيْتٌ", "t": "baytun", "meaning": "ein Haus"},
                 {"arabic": "كِتَابٌ", "t": "kitābun", "meaning": "ein Buch"},
                 {"arabic": "طَبِيبٌ", "t": "ṭabībun", "meaning": "ein Arzt"},
                 {"arabic": "تُفَّاحَةٌ", "t": "tuffāḥatun", "meaning": "ein Apfel"},
                 {"arabic": "بِنْتٌ", "t": "bintun", "meaning": "ein Mädchen"},
                 {"arabic": "نُورٌ", "t": "nūrun", "meaning": "Licht"},
                 {"arabic": "لَبَنٌ", "t": "labanun", "meaning": "Milch"},
                 {"arabic": "كُرْسِيٌّ", "t": "kursiyyun", "meaning": "ein Stuhl"},
             ]},

            # ---------------- Masri-Ecke ----------------
            {"type": "masri",
             "arabic": "الكِتَابِ دَه كَبِير أَوِي!",
             "t": "il-kitāb da kabīr awi!",
             "text": "Und in Kairo? Da verschwindet das ganze Tanwīn sofort auf der Straße: "
             "aus كِتَابٌ wird schlicht kitāb, alle Endungen fliegen raus. Am Mahmoud sagt: "
             "„Die Grammatik bleibt zu Hause, wenn wir auf die Straße gehen.“ Genau deshalb "
             "lernen wir die saubere Sprache — die Straße kriegen wir später geschenkt."},

            {"type": "callout", "variant": "bisso", "title": "Bissos Ecke", "icon": "🐈",
             "text": "Bisso sitzt auf dem Stuhl: عَلَى الكُرْسِيِّ (3alā l-kursiyyi). Kleine "
             "Vorschau fürs scharfe Auge: nach عَلَى (auf) steht der Genitiv — deshalb كُرْسِيٍّ "
             "mit -in. Bisso versteht das. Julia auch, spätestens in Teil 4."},

            # ---------------- Quiz ----------------
            {"type": "h2", "text": "Schnell-Quiz: Welcher Buchstabe beginnt das Wort?"},
            {"type": "quiz", "items": [
                {"arabic": "بَابٌ", "t": "bābun", "meaning": "eine Tür", "answer": "ب"},
                {"arabic": "تُفَّاحَةٌ", "t": "tuffāḥatun", "meaning": "ein Apfel", "answer": "ت"},
                {"arabic": "ثَوْرٌ", "t": "thawrun", "meaning": "ein Stier", "answer": "ث"},
                {"arabic": "نُورٌ", "t": "nūrun", "meaning": "Licht", "answer": "ن"},
                {"arabic": "يَدٌ", "t": "yadun", "meaning": "eine Hand", "answer": "ي"},
            ]},

            {"type": "callout", "variant": "checkpoint", "title": "Checkpoint", "icon": "🏁",
             "text": "Drei Fragen an dich: (1) Erkennst du in البَيْتُ das Wort بَيْتٌ wieder? "
             "(2) Warum hört man in التُّفَّاحُ kein „l“? (3) Was bedeutet das doppelte Zeichen "
             "in بَيْتٌ? Wenn alle drei sitzen: Du hast das Fundament der ganzen Sprache "
             "verstanden — weiter zu Teil 2!"},

            {"type": "closing", "arabic": "هَيَّا بِنَا!", "latin": "hayyā binā",
             "latin_text": "Auf geht's, wir beide! — das klassische Arabisch für yalla bēna"},
        ],
    },

    # =========================================================================
    # Teil 2 -- Buchstaben-Werkstatt II (Sturköpfe + lange Vokale)
    # =========================================================================
    {
        "id": "teil2",
        "teaser": "Teil 2 — Werkstatt II",
        "blocks": [
            {"type": "h1", "text": "Teil 2 — Die Buchstaben-Werkstatt II: ا و ر ز د ذ"},

            {"type": "p",
             "text": "Sechs Buchstaben mit Charakter: ا و ر ز د ذ verbinden sich zwar mit dem, "
             "was vor ihnen kommt — aber niemals mit dem, was danach kommt. Nach ihnen fängt "
             "jeder Buchstabe wieder von vorne an. Kein Druckfehler. Absicht."},

            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "Das sind die Sturköpfe der Familie: Sie hören zu (verbinden sich nach "
             "hinten), aber sie geben nie die Hand (verbinden sich nie nach vorne). Ziemlich "
             "deutsches Verhalten, eigentlich."},

            # ---------------- die sechs Sturköpfe ----------------
            {"type": "letter", "letter": "أَ", "name": "alif — a / ā",
             "dots": "Keine Punkte, kein Vorne-Verbinden — der gerade Rücken des Alphabets. "
             "Am Wortanfang trägt er den Hamza-Knacklaut wie einen Sattel.",
             "examples": [
                 {"arabic": "أَبٌ", "t": "abun", "meaning": "ein Vater (Hamza reitet auf dem Alif)", "pos": "Anfang"},
                 {"arabic": "بَابٌ", "t": "bābun", "meaning": "eine Tür — langes ā", "pos": "Mitte"},
                 {"arabic": "كِتَابٌ", "t": "kitābun", "meaning": "ein Buch — langes ā", "pos": "Mitte"},
             ]},
            {"type": "letter", "letter": "وَ", "name": "wāw — w / ū",
             "dots": "Zwei Talente: als Konsonant w und als langer Vokal ū. Sieht aus wie ein "
             "kleiner Mond mit Schwanz.",
             "examples": [
                 {"arabic": "وَلَدٌ", "t": "waladun", "meaning": "ein Junge (Konsonant w)", "pos": "Anfang"},
                 {"arabic": "نُورٌ", "t": "nūrun", "meaning": "Licht — langes ū", "pos": "Mitte"},
                 {"arabic": "وَرْدَةٌ", "t": "wardatun", "meaning": "eine Rose", "pos": "Anfang"},
             ]},
            {"type": "letter", "letter": "رَ", "name": "rā — r",
             "dots": "Zunge zittern lassen wie ein Motor — das arabische r rollt von ganz allein.",
             "examples": [
                 {"arabic": "رَجُلٌ", "t": "rajulun", "meaning": "ein Mann", "pos": "Anfang"},
                 {"arabic": "وَرْدَةٌ", "t": "wardatun", "meaning": "eine Rose (r in der Mitte)", "pos": "Mitte"},
                 {"arabic": "نَهْرٌ", "t": "nahrun", "meaning": "ein Fluss (r am Ende)", "pos": "Ende"},
             ]},
            {"type": "letter", "letter": "زَ", "name": "zāy — stimmhaftes s (wie in „Rose“)",
             "dots": "Punkt oben, eleganter Schweif. In der Mitte sieht er genauso aus — nur einsam.",
             "examples": [
                 {"arabic": "زَيْتٌ", "t": "zaytun", "meaning": "Öl", "pos": "Anfang"},
                 {"arabic": "زَرَافَةٌ", "t": "zarāfatun", "meaning": "eine Giraffe", "pos": "Anfang"},
             ]},
            {"type": "letter", "letter": "دَ", "name": "dāl — d",
             "dots": "Ein Winkel, mehr nicht. Verbindet sich nie nach vorne — Sturkopf Nummer eins.",
             "examples": [
                 {"arabic": "دَرْسٌ", "t": "darsun", "meaning": "eine Lektion", "pos": "Anfang"},
                 {"arabic": "دَارٌ", "t": "dārun", "meaning": "ein Haus, ein Anwesen — langes ā", "pos": "Anfang"},
                 {"arabic": "وَلَدٌ", "t": "waladun", "meaning": "ein Junge (d am Ende)", "pos": "Ende"},
             ]},
            {"type": "letter", "letter": "ذَ", "name": "dhāl — weiches th (wie in engl. „this“)",
             "dots": "Der Bruder des د — gleiche Form, aber mit Hut. Selten, aber edel.",
             "examples": [
                 {"arabic": "ذَهَبٌ", "t": "dhabun", "meaning": "Gold", "pos": "Anfang"},
                 {"arabic": "هَذَا", "t": "hādhā", "meaning": "dieser hier", "pos": "Mitte"},
             ]},

            # ---------------- Grammatik: lange Vokale ----------------
            {"type": "h2", "text": "Grammatik-Geheimnis 4: Länge ändert die Bedeutung!"},
            {"type": "p",
             "text": "Lange Vokale (ā, ī, ū) sind echte Buchstaben (ا و ي) — kurze sind nur "
             "Zeichen (َ ِ ُ). Das klingt nach Detail. Ist es nicht: Die Länge dreht das Wort "
             "komplett um. Zwei Beispiele, die man nie vergisst:"},
            {"type": "atable",
             "header": ["mit langem Vokal", "mit kurzem Vokal", "Die Überraschung"],
             "ar_col": [0, 1],
             "rows": [
                 ["كِتَابٌ", "كُتُبٌ", "kitābun = ein Buch → kutubun = BÜCHER!"],
                 ["رِجَالٌ", "رَجُلٌ", "rijālun = MÄNNER → rajulun = ein Mann"],
             ],
             "note": "Merksatz: Ein Dehn-Zeichen mehr kann aus einem Buch eine ganze "
             "Bibliothek machen. Deshalb: Vokale hören, nicht raten."},

            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "Stell dir vor, im Deutschen wäre „Hahn“ mit kurzem a plötzlich „Hun“ und "
             "würde einen Huhn-Plural auslösen. Genau so fühlt sich كِتَابٌ gegen كُتُبٌ an. "
             "Arabisch nimmt seine Vokale ernst. Sehr ernst."},

            # ---------------- Vokabeln ----------------
            {"type": "vocab", "title": "Acht neue Wörter — Familie und Gold",
             "words": [
                 {"arabic": "أَبٌ", "t": "abun", "meaning": "ein Vater"},
                 {"arabic": "أُمٌّ", "t": "ummun", "meaning": "eine Mutter (mit Shadda!)"},
                 {"arabic": "وَلَدٌ", "t": "waladun", "meaning": "ein Junge"},
                 {"arabic": "وَرْدَةٌ", "t": "wardatun", "meaning": "eine Rose"},
                 {"arabic": "رَجُلٌ", "t": "rajulun", "meaning": "ein Mann"},
                 {"arabic": "زَيْتٌ", "t": "zaytun", "meaning": "Öl"},
                 {"arabic": "دَرْسٌ", "t": "darsun", "meaning": "eine Lektion"},
                 {"arabic": "ذَهَبٌ", "t": "dhabun", "meaning": "Gold"},
             ]},

            # ---------------- Masri-Ecke ----------------
            {"type": "masri",
             "arabic": "الذَّهَبِ دَه غَالِي أَوِي!",
             "t": "id-dahab da ghāli awi!",
             "text": "Am Mahmoud zum Thema Gold: „id-dahab da ghāli awi!“ — Dieses Gold ist "
             "sehr teuer! Merk dir غَالِي (ghāli, teuer) gut — es ist DAS Verhandlungswort "
             "Ägyptens. Und das Tanwīn? Wie immer: auf der Straße verboten."},

            {"type": "callout", "variant": "bisso", "title": "Bissos Ecke", "icon": "🐈",
             "text": "Bisso und die وَرْدَةٌ: Rosenduft — herrlich. Rosendornen — Verrat. "
             "Katzenlogik in Reinform. Übrigens: Wenn Bisso neugierig ist, krümmt sich ihr "
             "Schwanz genau zu einem وَ. Der einzige Sturkopf, den sie akzeptiert."},

            # ---------------- Quiz ----------------
            {"type": "h2", "text": "Schnell-Quiz: Welcher Sturkopf beginnt das Wort?"},
            {"type": "quiz", "items": [
                {"arabic": "وَرْدَةٌ", "t": "wardatun", "meaning": "eine Rose", "answer": "و"},
                {"arabic": "رَجُلٌ", "t": "rajulun", "meaning": "ein Mann", "answer": "ر"},
                {"arabic": "زَيْتٌ", "t": "zaytun", "meaning": "Öl", "answer": "ز"},
                {"arabic": "دَرْسٌ", "t": "darsun", "meaning": "eine Lektion", "answer": "د"},
                {"arabic": "ذَهَبٌ", "t": "dhabun", "meaning": "Gold", "answer": "ذ"},
            ]},

            {"type": "callout", "variant": "checkpoint", "title": "Checkpoint", "icon": "🏁",
             "text": "Drei Fragen: (1) Warum verbindet sich دَ in وَلَدٌ nicht mit dem ل danach? "
             "(2) Was ist der Unterschied zwischen كِتَابٌ und كُتُبٌ? (3) Wie viele "
             "Buchstaben kannst du jetzt schon lesen? Elf! Das ist ein Drittel des Alphabets."},

            {"type": "closing", "arabic": "مُمْتَازٌ!", "latin": "mumtāzun",
             "latin_text": "Ausgezeichnet! — genau das bist du"},
        ],
    },

    # =========================================================================
    # Teil 3 -- Buchstaben-Werkstatt III (Die Kehl-Bande)
    # =========================================================================
    {
        "id": "teil3",
        "teaser": "Teil 3 — Werkstatt III",
        "blocks": [
            {"type": "h1", "text": "Teil 3 — Die Buchstaben-Werkstatt III: ج ح خ ع غ"},

            {"type": "p",
             "text": "Fünf Buchstaben, die tief im Hals wohnen: die Kehl-Bande. Deutsch hat "
             "genau ein h — Arabisch hat ein ganzes Orchester. Keine Sorge: Mit den 🔊-Knöpfen "
             "und ein bisschen Mut bekommst du alle fünf."},

            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "Stell dir den Hals als fünfstöckiges Haus vor: ه wohnt im Erdgeschoss "
             "(ganz leicht), ح im ersten (gehaucht), خ im zweiten (kratzig), ع im dritten "
             "(gedrosselt), غ im vierten (rollig). Die Nachbarn hören sich gegenseitig — aber "
             "verwechselt wird niemand."},

            # ---------------- die fünf Hals-Buchstaben ----------------
            {"type": "letter", "letter": "جَ", "name": "jīm — dsch (wie in „Dschungel“)",
             "dots": "Ein Punkt in der Mitte — der Bauchnabel-Buchstabe. Er VERBINDET sich in "
             "beide Richtungen: kein Sturkopf!",
             "examples": [
                 {"arabic": "جَمَلٌ", "t": "jamalun", "meaning": "ein Kamel 🐪", "pos": "Anfang"},
                 {"arabic": "جَبَلٌ", "t": "jabalun", "meaning": "ein Berg", "pos": "Anfang"},
             ]},
            {"type": "letter", "letter": "حَ", "name": "ḥā — scharfes, gehauchtes H",
             "dots": "Keine Punkte — man erkennt ihn am Klang: wie ausatmen auf einem "
             "kalten Spiegel.",
             "examples": [
                 {"arabic": "حُبٌّ", "t": "ḥubbun", "meaning": "Liebe (mit Shadda!)", "pos": "Anfang"},
                 {"arabic": "أَحْمَد", "t": "aḥmad", "meaning": "Ahmad — ḥ in der Mitte", "pos": "Mitte"},
             ]},
            {"type": "letter", "letter": "خَ", "name": "khā — ch (wie in „Bach“)",
             "dots": "Punkt oben — der kratzige Bruder des ح. Dein deutsches „Bach“-ch ist "
             "schon perfekt.",
             "examples": [
                 {"arabic": "خُبْزٌ", "t": "khubzun", "meaning": "Brot", "pos": "Anfang"},
                 {"arabic": "خَيْرٌ", "t": "khayrun", "meaning": "das Gute", "pos": "Anfang"},
             ]},
            {"type": "letter", "letter": "عَ", "name": "ʿayn — DER Kehllaut",
             "dots": "Der Star des Alphabets. Klingt wie ein „a“, bei dem man sich selbst "
             "sanft am Hals drückt. Übe: Hand an den Hals, Ton an.",
             "examples": [
                 {"arabic": "عَيْنٌ", "t": "3aynun", "meaning": "ein Auge, eine Quelle", "pos": "Anfang"},
                 {"arabic": "عَرَبِيٌّ", "t": "3arabiyyun", "meaning": "arabisch (Shadda + Tanwīn!)", "pos": "Mitte & Ende"},
             ]},
            {"type": "letter", "letter": "غَ", "name": "ghayn — zärtliches Kehl-r",
             "dots": "Punkt oben auf dem ع — klingt wie das französische r in „Paris“. "
             "Schnurren erlaubt.",
             "examples": [
                 {"arabic": "غَدًا", "t": "ghadan", "meaning": "morgen", "pos": "Anfang"},
                 {"arabic": "غُرَابٌ", "t": "ghurābun", "meaning": "ein Rabe", "pos": "Anfang"},
             ]},

            # ---------------- Grammatik: die H-Familie ----------------
            {"type": "h2", "text": "Grammatik-Geheimnis 5: Die H-Familie im Überblick"},
            {"type": "p",
             "text": "Fünf Buchstaben, die Deutsche alle als „h“ hören — und die für arabische "
             "Ohren so verschieden sind wie T und D für dich. Hier die komplette Familie zum "
             "Anhören und Unterscheiden:"},
            {"type": "atable",
             "header": ["Zeichen", "Stockwerk", "Arabisch", "Umschrift"],
             "ar_col": [0, 2],
             "rows": [
                 ["هَ", "Erdgeschoss — leichtes h", "هُنَا", "hunā — hier"],
                 ["حَ", "1. Stock — gehaucht, scharf", "أَحْمَد", "aḥmad"],
                 ["خَ", "2. Stock — kratziges ch", "خُبْزٌ", "khubz — Brot"],
                 ["عَ", "3. Stock — gedrosselt", "عَيْنٌ", "3ayn — Auge"],
                 ["غَ", "4. Stock — schnurrendes r", "غُرَابٌ", "ghurāb — Rabe"],
             ],
             "note": "Tipp: Hände an den Hals, die Reihe runterlesen und die Vibration "
             "fühlen. Von stockwerk zu Stockwerk wandert der Ton nach oben."},

            # ---------------- Grammatik: und = وَ ----------------
            {"type": "h2", "text": "Grammatik-Geheimnis 6: „und“ klebt — die Waw als Vorsilbe"},
            {"type": "p",
             "text": "Und jetzt das erste Wort, das du Bauen kannst: وَ bedeutet „und“ — aber "
             "es steht nie allein. Es KLEBT an das nächste Wort: أَبٌ وَأُمٌّ spricht man "
             "„abun wa-ummun“. Ein Wort, ein Grammatik-Kleber. So baut Arabisch Sätze wie "
             "Lego."},

            {"type": "atable",
             "header": ["… und …", "Klang", "Deutsch"],
             "ar_col": 0,
             "rows": [
                 ["أَبٌ وَأُمٌّ", "abun wa-ummun", "ein Vater und eine Mutter"],
                 ["دَرْسٌ وَكِتَابٌ", "darsun wa-kitābun", "eine Lektion und ein Buch"],
             ],
             "note": "Siehst du es? Das وَ verschmilzt mit dem nächsten Wort zu EINEM "
             "Sprechrhythmus: wa-UMMUN, wa-kitāBUN. Arabisch redet in Wellen."},

            # ---------------- Vokabeln ----------------
            {"type": "vocab", "title": "Acht neue Wörter — Kamele und Brot",
             "words": [
                 {"arabic": "جَمَلٌ", "t": "jamalun", "meaning": "ein Kamel 🐪"},
                 {"arabic": "جَبَلٌ", "t": "jabalun", "meaning": "ein Berg"},
                 {"arabic": "حُبٌّ", "t": "ḥubbun", "meaning": "Liebe"},
                 {"arabic": "خُبْزٌ", "t": "khubzun", "meaning": "Brot"},
                 {"arabic": "عَيْنٌ", "t": "3aynun", "meaning": "ein Auge, eine Quelle"},
                 {"arabic": "غُرَابٌ", "t": "ghurābun", "meaning": "ein Rabe"},
                 {"arabic": "غَدًا", "t": "ghadan", "meaning": "morgen"},
                 {"arabic": "أُمٌّ", "t": "ummun", "meaning": "eine Mutter"},
             ]},

            # ---------------- Masri-Ecke ----------------
            {"type": "masri",
             "arabic": "الخُبْزِ عِنْدَنَا اسْمُهُ عِيش!",
             "t": "il-khubz 3andana ismuh 3ēsh!",
             "text": "Am Mahmoud klärt auf: „Brot sagen wir عِيش (ʿēš). Und weißt du was? "
             "عِيش kommt vom Wort ‚leben‘ — Brot ist Leben. Punkt.“ In Kairo stimmt das "
             "wörtlich: Ohne ʿēš kein Tag. Grammatik-Endungen auch hier: Fehlanzeige."},

            {"type": "callout", "variant": "bisso", "title": "Bissos Ecke", "icon": "🐈",
             "text": "Bisso hat das Wort خُبْزٌ nie gelernt — und beherrscht es perfekt. "
             "Flüstert Julia es nur, materialisiert Bisso in unter vier Sekunden aus dem "
             "Nichts. Wissenschaftler rätseln. Bisso isst."},

            # ---------------- Quiz ----------------
            {"type": "h2", "text": "Schnell-Quiz: Welcher Hals-Buchstabe beginnt das Wort?"},
            {"type": "quiz", "items": [
                {"arabic": "جَمَلٌ", "t": "jamalun", "meaning": "ein Kamel", "answer": "ج"},
                {"arabic": "حُبٌّ", "t": "ḥubbun", "meaning": "Liebe", "answer": "ح"},
                {"arabic": "خُبْزٌ", "t": "khubzun", "meaning": "Brot", "answer": "خ"},
                {"arabic": "عَيْنٌ", "t": "3aynun", "meaning": "ein Auge", "answer": "ع"},
                {"arabic": "غُرَابٌ", "t": "ghurābun", "meaning": "ein Rabe", "answer": "غ"},
            ]},

            {"type": "callout", "variant": "checkpoint", "title": "Checkpoint", "icon": "🏁",
             "text": "Drei Fragen: (1) Welcher Buchstabe ist kein Sturkopf — und verbindet "
             "sich beidseitig? (ج!) (2) Wie sagt man „Brot und Leben“ auf Kairoisch? "
             "(ʿēš!) (3) Kannst du أَبٌ وَأُمٌّ flüssig sagen? Dann: Sechzehn Buchstaben "
             "kannst du jetzt — mehr als die Hälfte des Alphabets!"},

            {"type": "closing", "arabic": "إِلَى اللِّقَاءِ!", "latin": "ilā l-liqāʾi",
             "latin_text": "Bis zum Wiedersehen! — das elegante Abschied"},
        ],
    },
]
