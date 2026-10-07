---
title: Pinsel und Farben
description: Pinsel-Presets wählen und anpassen, Lieblingsstifte speichern, Farben wählen, Farbharmonien nutzen und Paletten verwalten.
---

## Pinsel-Presets

Ein Preset beschreibt, wie sich ein Pinsel verhält: wie stark er auf Druck reagiert, ob seine Enden spitz auslaufen, ob er eine Struktur hat. Tippen Sie oben im Feld von Stift oder Bleistift auf den Preset-Namen, um die Preset-Auswahl zu öffnen.

{% include fig.html src="preset_picker.webp" alt="Die Preset-Auswahl mit den Kategorien Stifte, Bleistifte und Marker und einem Beispielstrich je Preset" caption="Die Preset-Auswahl." %}

Tippen Sie ein Preset an, um es zu verwenden. Kritzel Studio wechselt bei Bedarf zu Stift oder Bleistift und übernimmt Breite und Deckkraft des Presets. Zuletzt gewählte Presets erscheinen während der laufenden Sitzung in einer Zeile oben in der Auswahl.

Kritzel Studio bringt diese Presets mit:

| Kategorie | Preset | Breite | Deckkraft | Eigenschaften |
|---|---|---|---|---|
| Stifte | „Variable Breite“ | 4 | 100 % | Allround-Stift mit Druck; Standard |
| Stifte | „Feste Breite“ | 3 | 100 % | Gleichbleibende Breite, ignoriert den Druck |
| Stifte | „Füllfeder“ | 5 | 100 % | Starke Druckreaktion, spitz auslaufende Enden |
| Stifte | „Kugelschreiber“ | 2,5 | 100 % | Dünn und fest |
| Bleistifte | „Weich“ | 4 | 85 % | Bleistiftstruktur, spitze Enden; Standard-Bleistift |
| Bleistifte | „Hart“ | 2,5 | 90 % | Bleistiftstruktur, feiner |
| Bleistifte | „Druckbleistift“ | 1,5 | 95 % | Bleistiftstruktur, gleichmäßig feine Linie |
| Marker | „Breit“ | 16 | 90 % | Breit, gleichbleibende Breite |
| Marker | „Feine Spitze“ | 3 | 100 % | Feiner Marker |
| Marker | „Textmarker“ | 24 | 35 % | Durchscheinend, zum Hervorheben |

## Eigene Presets anlegen

Halten Sie ein Preset in der Auswahl gedrückt, um den Preset-Editor zu öffnen. Ein Beispielstrich oben zeigt die Wirkung jeder Änderung.

{% include fig.html src="preset_editor.webp" size="narrow" alt="Der Preset-Editor mit Reglern für Kantenglättung, Stabilisierung und Verdünnung, Druckkurve, Schaltern für Verjüngung und Kappen sowie der Pinselstruktur" caption="Der Preset-Editor, geöffnet mit dem eingebauten Preset „Füllfeder“." %}

| Einstellung | Wirkung |
|---|---|
| „Kantenglättung“ | Glättet den Umriss des Strichs. |
| „Stabilisierung“ | Gleicht zittrige Linien aus. Höhere Werte lassen die Linie etwas hinter dem Stift herlaufen. |
| „Verdünnung“ | Wie stark der Druck die Breite verändert. Negative Werte machen den Strich bei weniger Druck dicker. |
| „Druckkurve“ | Setzt den Stiftdruck in Breite um. Ziehen Sie die beiden Kontrollpunkte oder wählen Sie „Linear“, „Weich“ oder „Fest“. |
| „Verjüngung Anfang“ / „Verjüngung Ende“ | Lässt den Strich am Anfang oder Ende spitz auslaufen; „Länge“ bestimmt, wie lang. |
| „Kappe Anfang“ / „Kappe Ende“ | Rundet die Enden des Strichs ab. |
| „Pinselstruktur“ | „Keine“, „Bleistift“, „Aquarell“ oder „Spray“, dazu „Texturstärke“. |

Eingebaute Presets lassen sich nicht ändern. Mit „Als Neu speichern“ legen Sie Ihre Einstellungen als neues Preset „‹Name› (Eigenes)“ an, das gleich aktiv wird. Ein eigenes Preset können Sie später mit „Speichern“ ändern oder mit „Löschen“ entfernen. Breite und Deckkraft ändert der Editor nicht; die stellen Sie im Eigenschaftenfeld ein.

Pinselstrukturen erscheinen auf der Leinwand und in PNG-, JPG- und PDF-Exporten. Der SVG-Export und der PDF-Export ohne „Texturen & Bilder einbeziehen“ zeichnen strukturierte Striche einfarbig. Wie das aussieht, zeigt die „Vektorvorschau“ in der Symbolleiste.

## Lieblingsstifte {#lieblingsstifte}

Lieblingsstifte sind Abkürzungen in der Werkzeugleiste. Ein Lieblingsstift merkt sich Preset, Farbe, Breite und Deckkraft.

- Tippen Sie auf das Plus unter den Werkzeugen, um den aktuellen Stift als Lieblingsstift zu speichern („Als Lieblingsstift speichern“).
- Tippen Sie einen Lieblingsstift an, um zu ihm zu wechseln.
- Tippen Sie ihn doppelt an, um ihn mit Ihren aktuellen Einstellungen zu überschreiben.
- Halten Sie ihn gedrückt und ziehen Sie ihn, um die Reihenfolge zu ändern. Ziehen Sie ihn aus der Leiste heraus, um ihn zu entfernen.

Lieblingsstifte gelten für alle Projekte.

## Eine Farbe wählen

Die Zeile „Farbe“ im Eigenschaftenfeld zeigt die aktuelle Farbe. Tippen Sie auf das runde Farbfeld, um die Farbauswahl zu öffnen.

{% include fig.html src="color_picker.webp" size="tall" alt="Die Farbauswahl mit Vorschaubalken, Farbkreis mit Sättigungsfeld, Abstufungen und eingeklappten Bereichen für Zuletzt verwendet, RGB, HSL, Hex, Kritzel-Farben und Farbharmonie" caption="Die Farbauswahl." %}

Die Farbauswahl hat mehrere Bereiche, die Sie auf- und zuklappen können:

- „Farbkreis“: Farbton am Ring, Sättigung und Helligkeit im Quadrat wählen. Die Felder darunter bieten hellere und dunklere Abstufungen.
- „Zuletzt verwendet“: die letzten zwölf bestätigten Farben.
- „RGB“ und „HSL“: Regler für genaue Werte.
- „Hex“: einen Farbcode wie `#3D7EA6` eingeben.
- „Kritzel-Farben“: 24 fertige Farben.
- „Farbharmonie“ und „Palette“, siehe unten.

„Fertig“ übernimmt die Farbe. Die Transparenz gehört nicht zur Farbe; dafür ist der Regler „Deckkraft“ im Eigenschaftenfeld da.

## Farbharmonie

Unter der Farbe schlägt das Eigenschaftenfeld passende Farben vor. Wählen Sie „Analog“ (benachbarte Farbtöne), „Komplementär“ (der gegenüberliegende Farbton), „Triadisch“ (drei gleichmäßig verteilte Farbtöne) oder „Mono“ (Abstufungen desselben Farbtons) und tippen Sie ein Farbfeld an, um die Farbe zu verwenden. „Zur Palette hinzufügen“ übernimmt die Vorschläge in die aktive Palette oder legt eine neue an, falls Sie noch keine haben.

## Paletten

Paletten sind Ihre eigenen Farbsammlungen und gelten für alle Projekte. Sobald es mindestens eine Palette gibt, erscheint sie im Eigenschaftenfeld unter den Harmonievorschlägen.

- Tippen Sie ein Farbfeld an, um die Farbe zu verwenden.
- Tippen Sie auf das Plus, um die aktuelle Farbe hinzuzufügen.
- Halten Sie ein Farbfeld gedrückt und ziehen Sie es, um die Reihenfolge zu ändern; lassen Sie es außerhalb der Palette los, um es zu entfernen.
- Eine andere Palette wählen Sie in der Auswahlliste über den Farbfeldern.

„Paletten verwalten“ öffnet einen Dialog, in dem Sie Paletten anlegen („Neue Palette“), umbenennen, duplizieren, umsortieren und löschen.
