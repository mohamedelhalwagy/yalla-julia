# -*- coding: utf-8 -*-
"""
Yalla, Julia! -- Band 1 -- structured content.

This file is the ONLY place you edit content. The builder (build_app.py)
reads this and turns it into a finished app (audio + HTML). For Band 2,
copy this file, extend the lists below, and re-run the builder.
"""


def letter_blocks(letters):
    """Return the list of block dicts for a letter section (one per letter)."""
    blocks = []
    for lt in letters:
        blocks.append({
            "type": "letter",
            "letter": lt["letter"],
            "name": lt["name"],
            "dots": lt["dots"],
            "examples": [
                {"arabic": a, "t": t, "meaning": m, "pos": p}
                for (a, t, m, p) in lt["examples"]
            ],
        })
    return blocks


def vocab_lists(groups):
    """Turn a list of (title, [words]) into 'vocab' blocks."""
    out = []
    for title, words in groups:
        out.append({
            "type": "vocab",
            "title": title,
            "words": [
                {"arabic": w[0], "t": w[1], "meaning": w[2]}
                for w in words
            ],
        })
    return out


CHAPTERS = [
    # =========================================================================
    # Teil 0
    # =========================================================================
    {
        "id": "teil0",
        "teaser": "Wie dieses Buch funktioniert",
        "blocks": [
            {"type": "h1", "text": "Teil 0 — Wie dieses Buch funktioniert"},
            {"type": "p", "text": "Liebe Julia, das hier ist kein Lehrbuch, das dich langweilen "
             "will. Es ist eine Einladung: an Straßenschilder, Taxifahrer, Kaffeehausbesitzer "
             "und mindestens eine sehr selbstbewusste Straßenkatze namens Bisso. Los geht's — "
             "ganz von vorne, ganz in Ruhe."},
            {"type": "h2", "text": "Was du hier lernst: ganz normales, gesprochenes Arabisch"},
            {"type": "p", "text": "Arabisch hat zwei Ebenen: eine Schriftsprache für Nachrichten "
             "und Bücher (Fus'Ha), und die Sprache, die 90 Millionen Menschen in Kairo tatsächlich "
             "sprechen (Masri, Ägyptisch-Arabisch). Dieses Buch konzentriert sich fast vollständig "
             "auf Masri — das normale, entspannte Alltagsarabisch, das du beim Taxifahren, im Café "
             "und beim Feilschen brauchst. Nur an wenigen Stellen zeigen wir dir kurz den "
             "Fus'Ha-Unterschied, falls du ihn mal auf einem Schild siehst."},
            {"type": "callout", "variant": "tip", "title": "Insider-Tipp", "icon": "💡",
             "text": "Du musst dir jetzt noch gar keine Sorgen um „zwei Sprachen“ machen. "
             "Für den Anfang gilt: lern die Wörter in diesem Buch so, wie sie dastehen — das ist "
             "genau das Arabisch, das echte Menschen in Ägypten mit dir sprechen werden."},
            {"type": "h2", "text": "Die Julia-Umschrift"},
            {"type": "p", "text": "Arabisch hat Laute, die es im Deutschen nicht gibt — aber du "
             "hast einen Heimvorteil: Deutsch besitzt bereits zwei Laute, an denen "
             "Englischsprachige verzweifeln."},
            {"type": "table",
             "header": ["Zeichen", "Beispiel", "Eselsbrücke"],
             "rows": [
                 ["ch", "chalás", "wie ch in „Bach“"],
                 ["sch", "schukran", "wie sch in „Schule“"],
                 ["g", "gamíl", "wie g in „geben“ — ägyptisch, nie „dsch“!"],
                 ["'", "'ahwa", "ein kleiner Stopp, wie in „Spiegel-ei“"],
                 ["3", "3áyez", "ein Laut tief aus dem Hals"],
                 ["H", "aHmed", "ein heißes, geflüstertes H"],
             ],
             "note": "Betonte Silben tragen einen Akzent (chalás). Mehr brauchst du nicht, um "
             "loszulegen."},
            {"type": "h2", "text": "Die Symbole in diesem Buch"},
            {"type": "legende",
             "items": [
                 {"icon": "🔊", "text": "Ägyptische Aussprache — echt, nicht förmlich"},
                 {"icon": "🚕", "text": "Am Mahmoud, der Taxifahrer, hat etwas zu sagen"},
                 {"icon": "🐈", "text": "Bisso, die Straßenkatze, hat eine Meinung"},
                 {"icon": "💡", "text": "Insider-Tipp für Ägypten"},
                 {"icon": "🏁", "text": "Checkpoint — kurz prüfen, ob's sitzt"},
                 {"icon": "🃏", "text": "Karte umdrehen im Übungsmodus"},
             ]},
            {"type": "callout", "variant": "taxi", "title": "Am Mahmoud sagt...", "icon": "🚕",
             "text": "Am Mahmoud fährt seit 30 Jahren Taxi in Kairo, kennt jeden Umweg und "
             "jeden Trick, und ist der Meinung, dass jeder Preis Verhandlungssache ist."},
            {"type": "callout", "variant": "bisso", "title": "Bissos Ecke", "icon": "🐈",
             "text": "Bisso ist eine Straßenkatze mit einer eingekerbten Ohrspitze und starken "
             "Meinungen zu Essensresten."},
            {"type": "closing", "arabic": "يلا بينا", "latin": "yalla beena",
             "latin_text": "los geht's, wir beide!"},
        ],
    },

    # =========================================================================
    # Teil 1
    # =========================================================================
    {
        "id": "teil1",
        "teaser": "Buchstaben-Werkstatt I — Die Verbinder",
        "blocks": [
            {"type": "h1", "text": "Buchstaben-Werkstatt I — Die Verbinder"},
            {"type": "p", "text": "Fünf Buchstaben, ein Skelett: ب ت ث ن ي sehen sich in der "
             "Wortmitte alle sehr ähnlich — ein kleiner „Zahn“. Was sie unterscheidet, sind nur "
             "die Punkte."},
            {"type": "p", "text": "ب ت ث ن ي — tippe auf einen Buchstaben, um ihn zu hören.", },
            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "Stell dir eine Familie von fünf Geschwistern vor, die alle das gleiche "
             "T-Shirt tragen — man erkennt sie nur an den Punkten, die sie sich ins Gesicht "
             "gemalt haben. Das ist ب ت ث ن ي."},
            *letter_blocks([
                {"letter": "ب", "name": "baa", "dots": "Ein Punkt darunter.",
                 "examples": [("بيت", "bayt", "Haus", "Anfang"),
                              ("كبير", "kabír", "groß", "Mitte"),
                              ("طبيب", "Tabíb", "Arzt", "Ende")]},
                {"letter": "ت", "name": "taa", "dots": "Zwei Punkte darüber.",
                 "examples": [("تفاح", "tuffáH", "Apfel", "Anfang"),
                              ("كتاب", "kitáb", "Buch", "Mitte"),
                              ("بنت", "bint", "Mädchen", "Ende")]},
                {"letter": "ث", "name": "thaa",
                 "dots": "Drei Punkte darüber. Ein seltener Gast im Alltag — diese zwei Wörter "
                 "reichen für den Anfang völlig.",
                 "examples": [("ثلاجة", "taláaga", "Kühlschrank", "Anfang"),
                              ("كتير", "kitír", "viel / sehr — kennst du schon!", "Mitte")]},
                {"letter": "ن", "name": "nuun", "dots": "Ein Punkt darüber, tiefere Schale.",
                 "examples": [("نور", "nuur", "Licht", "Anfang"),
                              ("كنافة", "kunaafa", "das Dessert!", "Mitte"),
                              ("لبن", "laban", "Milch", "Ende")]},
                {"letter": "ي", "name": "yaa", "dots": "Zwei Punkte darunter, Schwanz am Ende.",
                 "examples": [("ياسمين", "yasmín", "Jasmin", "Anfang"),
                              ("بيت", "bayt", "Haus — y in der Mitte", "Mitte"),
                              ("كرسي", "kursi", "Stuhl", "Ende")]},
            ]),
            {"type": "callout", "variant": "tip", "title": "Insider-Tipp", "icon": "💡",
             "text": "كنافة (kunaafa) ist ein warmes, sirupsüßes Gebäck mit Käse oder Sahne — DER "
             "Grund, im Ramadan hungrig zu bleiben. Merk dir das Wort."},
            {"type": "callout", "variant": "checkpoint", "title": "Checkpoint", "icon": "🏁",
             "text": "Kannst du ب, ت, ث, ن und ي in einem Wort wiedererkennen, nur an den Punkten? "
             "Wenn ja: weiter zu Teil 2!"},
        ],
    },

    # =========================================================================
    # Teil 2
    # =========================================================================
    {
        "id": "teil2",
        "teaser": "Buchstaben-Werkstatt II — Die Sturköpfe",
        "blocks": [
            {"type": "h1", "text": "Buchstaben-Werkstatt II — Die Sturköpfe"},
            {"type": "p", "text": "Diese sechs Buchstaben sind Einzelgänger: ا و ر ز د ذ geben zwar "
             "gerne eine Hand nach hinten, weigern sich aber, nach vorne eine zweite Hand "
             "auszustrecken."},
            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "Das sind die Sturköpfe der Familie: sie hören zu (verbinden sich mit dem, was "
             "davor kommt), aber sie antworten nie (verbinden sich nie mit dem, was danach kommt). "
             "Ziemlich deutsches Verhalten, eigentlich."},
            *letter_blocks([
                {"letter": "ا", "name": "alif", "dots": "",
                 "examples": [("بابا", "baaba", "Papa", "nach einem Buchstaben")]},
                {"letter": "و", "name": "waaw", "dots": "",
                 "examples": [("ورد", "ward", "Rose", "w"),
                              ("أبو", "abu", "Vater von...", "nach einem Buchstaben")]},
                {"letter": "ر", "name": "raa", "dots": "",
                 "examples": [("ورد", "ward", "Rose (r in der Mitte)", "r"),
                              ("قمر", "qamar", "Mond", "nach einem Buchstaben")]},
                {"letter": "ز", "name": "zaay", "dots": "",
                 "examples": [("زهرة", "zahra", "Blume", "z"),
                              ("موز", "mooz", "Banane", "nach einem Buchstaben")]},
                {"letter": "د", "name": "daal", "dots": "",
                 "examples": [("دار", "daar", "Haus / Anwesen", "d"),
                              ("ولد", "walad", "Junge", "nach einem Buchstaben")]},
                {"letter": "ذ", "name": "dhaal",
                 "dots": "Selten im Alltag — im Masri wird daraus meist ein „d“ oder „z“.",
                 "examples": [("هذا", "haadha", "dieses hier; Masri oft: da", "nach einem Buchstaben")]},
            ]),
            {"type": "callout", "variant": "tip", "title": "Insider-Tipp", "icon": "💡",
             "text": "موز (mooz) — Banane. Ja, wirklich, es klingt fast wie im Deutschen mit Akzent. "
             "Ägyptische Bananen sind kleiner und süßer — probier sie."},
            {"type": "callout", "variant": "checkpoint", "title": "Checkpoint", "icon": "🏁",
             "text": "Merksatz: ا و ر ز د ذ geben nie eine zweite Hand. Nach ihnen fängt jeder "
             "Buchstabe wieder ganz von vorne an — das ist Absicht, kein Druckfehler!"},
        ],
    },

    # =========================================================================
    # Teil 3
    # =========================================================================
    {
        "id": "teil3",
        "teaser": "Die kleinen Helfer — Vokale",
        "blocks": [
            {"type": "h1", "text": "Die kleinen Helfer — Vokale"},
            {"type": "p", "text": "Arabisch schreibt normalerweise nur die Konsonanten und langen "
             "Vokale. Die kurzen Vokale (a, i, u) werden meist nicht geschrieben — du musst sie "
             "lernen wie Melodien. In Lehrbüchern (und hier) setzen wir sie aber als kleine "
             "Hilfszeichen über oder unter den Buchstaben."},
            {"type": "table",
             "header": ["Name", "Lage", "Beispiel", "Klingt wie"],
             "rows": [
                 ["Fatha", "Strich oben", "بَ (ba)", "kurzes a"],
                 ["Kasra", "Strich unten", "بِ (bi)", "kurzes i"],
                 ["Damma", "Komma oben", "بُ (bu)", "kurzes u"],
                 ["Sukun", "Kringel oben", "بْ (b)", "gar kein Vokal"],
                 ["Shadda", "kleines w oben", "بّ (bb)", "doppelter Konsonant"],
             ],
             "tr_audio": ["ba", "bi", "bu"]},
            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "Fatha sieht aus wie ein kleiner, gefallener Schnurrbart über dem Buchstaben. "
             "Kasra ist derselbe Schnurrbart, nur er ist heruntergefallen und liegt jetzt unten. "
             "Damma ist ein winziges Ohr, das nach oben lauscht."},
            {"type": "h2", "text": "Die drei langen Vokale"},
            {"type": "p", "text": "Lange Vokale werden dagegen tatsächlich als eigene Buchstaben "
             "geschrieben: ا für langes aa, و für langes uu, ي für langes ii."},
            {
                "type": "vocab",
                "title": "Lange Vokale",
                "words": [
                    {"arabic": "كتاب", "t": "kitáb", "meaning": "Buch (langes aa)"},
                    {"arabic": "دور", "t": "duur", "meaning": "Rollen / Runden (langes uu)"},
                    {"arabic": "كبير", "t": "kabír", "meaning": "groß (langes ii)"},
                ],
            },
            {"type": "callout", "variant": "tip", "title": "Insider-Tipp", "icon": "💡",
             "text": "Ein Wort, das du garantiert brauchen wirst: حبيبي — Habíbi — „mein "
             "Schatz/Liebling“. Langes ii mitten im Wort. Wenn Mohamed dich so nennt, weißt du "
             "jetzt auch, warum es sich so lang anhört."},
            {"type": "h2", "text": "Kurzer Vergleich"},
            {
                "type": "vocab",
                "title": "Buch — Bücher",
                "words": [
                    {"arabic": "كتاب", "t": "kitáb", "meaning": "(ein) Buch — mit langem a"},
                    {"arabic": "كُتُب", "t": "kutub", "meaning": "Bücher (Plural!) — mit kurzem u, u"},
                ],
            },
            {"type": "callout", "variant": "checkpoint", "title": "Checkpoint", "icon": "🏁",
             "text": "Du musst die Vokalzeichen nicht auswendig zeichnen können — du musst sie nur "
             "erkennen. Im echten Alltag (Straßenschilder, WhatsApp) verschwinden sie fast komplett "
             "— Muttersprachler lesen Arabisch meistens ohne sie, so wie du „Str.“ automatisch als "
             "„Straße“ liest."},
        ],
    },

    # =========================================================================
    # Teil 4
    # =========================================================================
    {
        "id": "teil4",
        "teaser": "Überleben I — Begrüßung",
        "blocks": [
            {"type": "h1", "text": "Überleben I — Die Begrüßungs-Choreografie"},
            {"type": "p", "text": "In Ägypten ist eine Begrüßung kein einzelnes Wort — es ist ein "
             "kleines Ritual mit festen Schritten, wie ein Tanz. Wenn du den ersten Schritt machst, "
             "muss die andere Person mit dem passenden zweiten Schritt antworten. Das ist keine "
             "Höflichkeit, das ist Choreografie."},
            {
                "type": "vocab",
                "title": "Die Begrüßungs-Choreografie",
                "words": [
                    {"arabic": "السلام عليكم", "t": "as-salámu 3aláykum",
                     "meaning": "Der Friede sei mit dir (universeller Gruß)"},
                    {"arabic": "وعليكم السلام", "t": "wa 3aláykum as-saláam",
                     "meaning": "Antwort: und mit dir sei der Friede"},
                    {"arabic": "صباح الخير", "t": "SabáaH el-kheir", "meaning": "Guten Morgen"},
                    {"arabic": "صباح النور", "t": "SabáaH en-nuur",
                     "meaning": "Antwort auf Guten Morgen"},
                    {"arabic": "مساء الخير", "t": "masáa' el-kheir", "meaning": "Guten Abend"},
                    {"arabic": "مساء النور", "t": "masáa' en-nuur",
                     "meaning": "Antwort auf Guten Abend"},
                    {"arabic": "إزيك", "t": "izzáyyak",
                     "meaning": "Wie geht's dir? (zu einem Mann, Masri)"},
                    {"arabic": "إزيك", "t": "izzáyyik",
                     "meaning": "Wie geht's dir? (zu einer Frau, gleiche Schrift!)"},
                    {"arabic": "كويس، الحمد لله", "t": "kwáyyes, el-Hamdu lilláh",
                     "meaning": "Gut, Gott sei Dank (Standardantwort — immer!)"},
                    {"arabic": "شكراً", "t": "shukran", "meaning": "Danke"},
                    {"arabic": "العفو", "t": "el-3afw",
                     "meaning": "Bitte / Gerne (Antwort auf Danke)"},
                    {"arabic": "من فضلك", "t": "min faDlak", "meaning": "Bitte (zu einem Mann)"},
                    {"arabic": "من فضلك", "t": "min faDlik", "meaning": "Bitte (zu einer Frau)"},
                    {"arabic": "مع السلامة", "t": "ma3a s-saláama",
                     "meaning": "Tschüss („geh in Frieden“)"},
                    {"arabic": "تصبح على خير", "t": "tuSbaH 3ala kheir",
                     "meaning": "Gute Nacht (zu einem Mann)"},
                ],
            },
            {"type": "callout", "variant": "taxi", "title": "Am Mahmoud sagt...", "icon": "🚕",
             "text": "Egal wie dein Tag war — auf „izzayyak?“ antwortest du IMMER mit „kwayyes, "
             "el-Hamdu lillah“. Auch wenn dein Taxi gerade eine Panne hatte. Das ist keine Lüge, "
             "das ist Etikette."},
            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "Die Antwort auf „Wie geht's?“ in Ägypten ist wie das deutsche „gut, und dir?“ "
             "— nur, dass „gut“ hier gesetzlich vorgeschrieben zu sein scheint. Niemand antwortet "
             "ehrlich. Das ist Teil des Charmes."},
            {"type": "callout", "variant": "checkpoint", "title": "Checkpoint", "icon": "🏁",
             "text": "Übe laut: „as-salámu 3aláykum“ sagen, kurze Pause, dann selbst mit „wa "
             "3aláykum as-saláam“ antworten. Wenn das flüssig klingt, bist du bereit für echte "
             "Menschen."},
        ],
    },

    # =========================================================================
    # Teil 5
    # =========================================================================
    {
        "id": "teil5",
        "teaser": "Überleben II — Ja, Nein, Feilschen",
        "blocks": [
            {"type": "h1", "text": "Überleben II — Ja, Nein und die Kunst des Feilschens"},
            {"type": "h2", "text": "Ja und Nein"},
            *vocab_lists([
                ("Ja und Nein", [
                    ("أيوه", "aywa", "Ja (Masri, das gebräuchlichste)"),
                    ("آه", "aah", "Ja (noch informeller)"),
                    ("لأ", "la'", "Nein (Masri, betont)"),
                    ("لا، شكراً", "la, shukran", "Nein, danke"),
                ]),
            ]),
            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "Fus'Ha-Nein heißt لا (la) — kurz, unschuldig, harmlos. Masri-Nein heißt لأ "
             "(la') — mit einem kleinen Kehlkopf-Stopp am Ende, der Entschlossenheit signalisiert. "
             "Julia, lern dieses Nein. Du wirst es auf dem Basar brauchen."},
            {"type": "h2", "text": "Feilschen — eine Nationalsportart"},
            *vocab_lists([
                ("Feilschen", [
                    ("بكام ده؟", "bikaam da?", "Wie viel kostet das?"),
                    ("غالي أوي!", "gháali awi!", "Viel zu teuer!"),
                    ("كتير أوي", "kitír awi", "sehr / zu viel"),
                    ("ممكن تنزل السعر؟", "mumkin tinzil is-si3r?",
                     "Kannst du mit dem Preis runtergehen?"),
                    ("ماشي", "máashi", "Okay, abgemacht"),
                    ("والله؟", "walláhi?",
                     "Wirklich?! (bei Gott — Ausdruck des Erstaunens)"),
                ]),
            ]),
            {"type": "callout", "variant": "taxi", "title": "Am Mahmoud sagt...", "icon": "🚕",
             "text": "Der erste Preis, den ein Verkäufer nennt, ist wie das erste Angebot bei einem "
             "Flohmarkt in Bayern: eine Einladung, nicht eine Tatsache. Wenn du nicht handelst, ist "
             "das für uns fast unhöflich — es nimmt uns den Spaß."},
            {"type": "callout", "variant": "tip", "title": "Insider-Tipp", "icon": "💡",
             "text": "Faustregel für Touristen-Basare: biete zuerst die Hälfte des genannten Preises, "
             "lächle dabei, und lass dich langsam Richtung Mitte verhandeln. Bei غالي أوي! („viel zu "
             "teuer!“) darfst du theatralisch die Augenbrauen hochziehen — das gehört dazu."},
            {"type": "callout", "variant": "checkpoint", "title": "Checkpoint", "icon": "🏁",
             "text": "Rollenspiel-Vorbereitung: du wirst بكام ده؟, غالي أوي! und ماشي in Teil 8 in "
             "einem echten Dialog mit Am Mahmoud brauchen. Sprich sie schon jetzt laut."},
        ],
    },

    # =========================================================================
    # Teil 6
    # =========================================================================
    {
        "id": "teil6",
        "teaser": "Die IBM-Regel",
        "blocks": [
            {"type": "h1", "text": "Die IBM-Regel"},
            {"type": "callout", "variant": "ibm", "title": "Die IBM-Regel", "icon": "⏱",
             "text": "Inshallah, Bukra, Maalesh — die drei Wörter, die gemeinsam die gesamte "
             "ägyptische Zeitplanung erklären. Wenn ein Termin „inshallah bukra“ (so Gott will, "
             "morgen) stattfindet und es doch nicht klappt, sagt man einfach „ma3lesh“ (macht "
             "nichts) und macht weiter. Willkommen im System."},
            *vocab_lists([
                ("Die IBM-Wörter", [
                    ("يلا", "yalla", "Los geht's! / Komm schon! / Beeil dich!"),
                    ("خلاص", "khaláS", "Fertig. Schluss. Genug. (das nützlichste Wort überhaupt)"),
                    ("معلش", "ma3lesh", "Macht nichts / Kein Problem / Tut mir leid"),
                    ("إن شاء الله", "inshallah", "So Gott will („vielleicht, vielleicht auch nicht“)"),
                    ("بكرة", "bükra", "Morgen (der Tag nach heute — theoretisch)"),
                    ("حاضر", "HáaDir", "Wird gemacht! / Jawohl! (nützlich gegenüber Am Mahmoud)"),
                ]),
            ]),
            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "خلاص (khaláS) ist das Schweizer Taschenmesser der arabischen Sprache. Es "
             "bedeutet: „fertig“, „genug jetzt“, „okay, abgemacht“, „lass uns aufhören zu streiten“ "
             "— und manchmal einfach nur „...“. Wenn du nur ein Wort aus diesem Buch behältst, "
             "nimm dieses."},
            {"type": "callout", "variant": "bisso", "title": "Bissos Ecke", "icon": "🐈",
             "text": "Wenn Bisso genug vom Streicheln hat, sagt sie es nicht mit Worten — sie geht "
             "einfach. Julia, das ist خلاص in Katzenform."},
            {"type": "callout", "variant": "tip", "title": "Insider-Tipp", "icon": "💡",
             "text": "بكرة (bukra, „morgen“) ist mit Vorsicht zu genießen — es bedeutet nicht "
             "zwingend „in 24 Stunden“. Es bedeutet eher „nicht heute, aber irgendwann bestimmt“. "
             "Plane entsprechend."},
            {"type": "callout", "variant": "checkpoint", "title": "Checkpoint", "icon": "🏁",
             "text": "Baue einen Satz mit allen drei IBM-Wörtern: „Kommst du morgen?“ — „Inshallah, "
             "bukra!“ — und wenn es nicht klappt: „Ma3lesh!“ Übe das laut, am besten mit einem "
             "Augenzwinkern."},
        ],
    },

    # =========================================================================
    # Teil 7
    # =========================================================================
    {
        "id": "teil7",
        "teaser": "Zahlen — Von 1 bis 10",
        "blocks": [
            {"type": "h1", "text": "Zahlen — Von 1 bis 10"},
            *vocab_lists([
                ("Die Zahlen 1 bis 10", [
                    ("واحد", "wáaHid", "1"),
                    ("اثنين", "itnéin", "2"),
                    ("ثلاثة", "taláata", "3"),
                    ("أربعة", "árba3a", "4"),
                    ("خمسة", "khámsa", "5"),
                    ("ستة", "sítta", "6"),
                    ("سبعة", "sáb3a", "7"),
                    ("ثمانية", "tamánya", "8"),
                    ("تسعة", "tís3a", "9"),
                    ("عشرة", "3áshara", "10"),
                ]),
            ]),
            {"type": "callout", "variant": "laugh", "title": "Lach-Pause", "icon": "😄",
             "text": "Kleine Ironie des Schicksals: die Ziffern, die wir im Deutschen „arabische "
             "Ziffern“ nennen (0,1,2,3...), sehen im echten Arabisch ganz anders aus. Die Ägypter "
             "benutzen ihre eigenen Symbole — entdecke sie unten."},
            {"type": "h2", "text": "Die echten arabischen Ziffern"},
            {"type": "numrow", "digits": ["٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"],
             "latin": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]},
            {"type": "callout", "variant": "tip", "title": "Insider-Tipp", "icon": "💡",
             "text": "Diese Ziffern siehst du auf ägyptischen Preisschildern, Nummernschildern und "
             "Restaurantrechnungen. Lohnt sich, sie zu erkennen, bevor du beim Feilschen (Teil 5!) "
             "über den Preis verhandelst, den du gar nicht lesen kannst."},
            {"type": "callout", "variant": "checkpoint", "title": "Checkpoint", "icon": "🏁",
             "text": "Zähle laut von 1 bis 10 auf Arabisch, während du an den Fingern abzählst — "
             "eine der ältesten und zuverlässigsten Lernmethoden der Welt."},
        ],
    },

    # =========================================================================
    # Teil 8
    # =========================================================================
    {
        "id": "teil8",
        "teaser": "Übungen & Rollenspiel",
        "blocks": [
            {"type": "h1", "text": "Übungen, Rätsel und ein Rollenspiel"},
            {"type": "h2", "text": "1. Buchstaben-Zuordnung"},
            {"type": "p", "text": "Zu welchem Buchstaben gehört der erste Laut in diesen Wörtern? "
             "Schreib den Buchstaben daneben — oder tippe auf 🔊 und vergleiche."},
            {
                "type": "quiz",
                "items": [
                    {"arabic": "بيت", "t": "bayt", "meaning": "Haus", "answer": "ب"},
                    {"arabic": "تفاح", "t": "tuffáH", "meaning": "Apfel", "answer": "ت"},
                    {"arabic": "نور", "t": "nuur", "meaning": "Licht", "answer": "ن"},
                    {"arabic": "ورد", "t": "ward", "meaning": "Rose", "answer": "و"},
                    {"arabic": "موز", "t": "mooz", "meaning": "Banane", "answer": "م"},
                    {"arabic": "دار", "t": "daar", "meaning": "Haus / Anwesen", "answer": "د"},
                ],
            },
            {"type": "h2", "text": "2. Rollenspiel: „Ertappt in Kairo“"},
            {
                "type": "dialogue",
                "title": "Mit Am Mahmoud unterwegs",
                "lines": [
                    {"who": "Am Mahmoud", "arabic": "أهلاً! إزيك؟", "t": "ahlan! izzáyyik?",
                     "german": "Willkommen! Wie geht's dir?"},
                    {"who": "Julia", "arabic": "كويسة، الحمد لله! إنتي إزيك؟", "t": "kwayyesa, el-hamdu lillah! inti izzáyyik?",
                     "german": "Gut, Gott sei Dank! Und dir?"},
                    {"who": "Am Mahmoud", "arabic": "الحمد لله! فين عايزة تروحي؟", "t": "el-hamdu lillah! feen 3ayza trooHi?",
                     "german": "Gott sei Dank! Wohin willst du?"},
                    {"who": "Julia", "arabic": "للسوق، من فضلك.", "t": "lissuu', min fadlik.",
                     "german": "Zum Markt, bitte."},
                    {"who": "Am Mahmoud", "arabic": "ماشي! يلا بينا!", "t": "máashi! yalla beena!",
                     "german": "Okay! Auf geht's!"},
                    {"who": "Am Mahmoud", "arabic": "بمية جنيه.", "t": "bimiya gineih.",
                     "german": "Das macht 100 Pfund."},
                    {"who": "Julia", "arabic": "غالي أوي! خمسين!", "t": "gháali awi! khamseen!",
                     "german": "Viel zu teuer! Fünfzig!"},
                    {"who": "Am Mahmoud", "arabic": "طيب... معلش، ماشي!", "t": "tayyeb... ma3lesh, máashi!",
                     "german": "Na gut... macht nichts, abgemacht!"},
                ],
            },
            {"type": "callout", "variant": "bisso", "title": "Bissos Ecke", "icon": "🐈",
             "text": "Während die beiden verhandeln, klaut Bisso in aller Ruhe ein Stück Fladenbrot "
             "aus Julias Tasche. Niemand hat es kommen sehen. So ist das Leben in Kairo: man "
             "verhandelt um fünfzig Pfund und verliert das Brot trotzdem."},
            {"type": "callout", "variant": "checkpoint", "title": "Geschafft!", "icon": "🎉",
             "text": "Du kennst jetzt elf Buchstaben, alle Vokalzeichen, eine komplette "
             "Begrüßungs-Choreografie, wie man in Kairo feilscht, die IBM-Regel und die Zahlen 1 bis "
             "10. Das ist ehrlich schon eine Menge — مبروك! (mabruk — Glückwunsch!). Band 2 nimmt "
             "die restlichen Buchstaben vor, dazu Café-Bestellungen und mehr Am Mahmoud. Sag einfach "
             "Mohamed Bescheid, wenn du bereit bist."},
        ],
    },
]
