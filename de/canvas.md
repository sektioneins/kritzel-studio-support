---
title: Die Leinwand
description: Symbolleiste, Werkzeugleiste, Eigenschaftenfeld, Zen-Modus, Bewegen auf der Leinwand, Rückgängig und automatisches Speichern.
---

Auf der Leinwand wird gezeichnet. Oben liegt die Symbolleiste, an der Seite die Werkzeugleiste, und das Eigenschaftenfeld zeigt die Optionen des aktuellen Werkzeugs.

{% include fig.html src="canvas.webp" alt="Die Leinwand mit Schaltflächengruppen oben links und oben rechts, der Werkzeugleiste links und der Lasche am rechten Rand" caption="Die Leinwand. Auf dem Tablet versteckt sich das Eigenschaftenfeld hinter der kleinen Lasche am rechten Rand." %}

## Die Symbolleiste

Die Symbolleiste besteht aus drei Gruppen. Jede Schaltfläche zeigt ihren Namen, wenn Sie mit der Maus darauf zeigen oder sie gedrückt halten.

Die Gruppe oben links enthält das Wichtigste:

| Schaltfläche | Wirkung |
|---|---|
| Haus | Speichert das Projekt und kehrt zur Galerie zurück („Zurück zur Galerie“). |
| Gebogener Pfeil nach links | „Rückgängig“ |
| Gebogener Pfeil nach rechts | „Wiederholen“ |
| Kreis | „Zen-Modus“: blendet alles außer der Zeichnung aus. |
| Ecken | „Ansicht zurücksetzen“: setzt Zoom, Verschiebung und Drehung zurück. Gedrückt halten oder Rechtsklick setzt nur eines davon zurück („Verschiebung zurücksetzen“, „Zoom zurücksetzen“, „Drehung zurücksetzen“). |

Die zweite Gruppe enthält drei Sperren: „Verschieben sperren“, „Zoom sperren“ und „Drehung sperren“. Eine aktive Sperre wird orange, und der entsprechende Teil jeder Geste wird ignoriert. Das hilft zum Beispiel, wenn Sie zoomen möchten, ohne die Leinwand versehentlich zu drehen. Die Sperren werden nicht gespeichert; beim Öffnen eines Projekts sind sie immer aus.

Die Gruppe oben rechts betrifft das Dokument:

| Schaltfläche | Wirkung |
|---|---|
| Teilen-Symbol | „Exportieren“ als PNG, JPG, SVG, PDF oder `.kritzel`. |
| Download-Symbol | „Importieren“: ein Bild oder eine SVG-Datei in die Zeichnung holen. |
| Seiten-Symbol | „Vektorvorschau“: zeigt die Zeichnung ohne Pinselstrukturen, so wie SVG- und PDF-Export sie ausgeben. |
| Bild-Symbol | „Hintergrund“: Hintergrundfarbe und Vorlagen. |
| Raster-Symbol | „Raster“: Raster und Perspektive. |
| Lineal-Symbol | „Hilfslinien“: Lineale und Ellipsen. |
| Zielscheibe | „An Hilfslinien einrasten“. Nur sichtbar, solange Hilfslinien eingeschaltet sind. |
| Stapel-Symbol | „Ebenen“: blendet das Ebenenfeld ein und aus. |

Ist ein Feld geöffnet, erscheint seine Schaltfläche abgeblendet. In einem schmalen Fenster (unter 700 Pixel Breite) bleiben nur Haus, Rückgängig und Wiederholen in der Leiste; alles andere wandert in das Menü „Mehr“ hinter den drei Punkten.

## Die Werkzeugleiste

Die Werkzeugleiste enthält die zehn Werkzeuge, von oben nach unten: Auswahl, Stift, Bleistift, Radierer, Form, Pipette, Text, Verschieben, Schneiden und Punkte. Die Schaltfläche „Form“ zeigt die aktuell gewählte Form. Mit Tastatur hat jedes Werkzeug ein Kürzel mit einem einzigen Buchstaben, siehe [Tastenkürzel und Gesten](shortcuts.html).

Unter den Werkzeugen folgen Ihre Lieblingsstifte und ein Plus, mit dem Sie den aktuellen Stift als Lieblingsstift speichern; siehe [Lieblingsstifte](brushes-colours.html#lieblingsstifte).

Wenn Sie die Werkzeugnamen sehen möchten, schalten Sie in den [Einstellungen](settings.html) „Werkzeugnamen anzeigen“ ein. „Leistendichte“ macht die Schaltflächen größer, und „Händigkeit“ verlegt die Leiste für Linkshänder an den rechten Rand (die Felder wandern dann nach links).

## Das Eigenschaftenfeld

Das Eigenschaftenfeld zeigt die Optionen des aktiven Werkzeugs bzw. beim Auswahlwerkzeug die der ausgewählten Objekte. Am Desktop ist es immer seitlich angedockt. Auf dem Tablet ist es zunächst ausgeblendet: Tippen Sie auf die kleine Lasche am Bildschirmrand, um es zu zeigen, und erneut, um es wieder auszublenden.

In einem schmalen Fenster öffnen sich Eigenschaftenfeld, Ebenenfeld sowie die Einstellungen für Raster, Hintergrund und Hilfslinien als Blatt vom unteren Bildschirmrand.

Viele Werte sind Schieberegler. Tippen Sie auf die Zahl neben einem Regler, um einen genauen Wert einzugeben; <kbd>Enter</kbd> übernimmt ihn, <kbd>Esc</kbd> bricht ab.

## Zen-Modus

Der Zen-Modus blendet Symbolleiste, Werkzeugleiste und alle Felder aus, sodass nur die Zeichnung bleibt. Sie schalten ihn mit der Kreis-Schaltfläche oder mit <kbd>Esc</kbd> ein. Oben links erscheint der Hinweis „Tippen zum Beenden“, der nach einigen Sekunden zu einem fast unsichtbaren Symbol an derselben Stelle verblasst. Tippen Sie darauf oder drücken Sie <kbd>Esc</kbd>, um alles wieder einzublenden.

{% include fig.html src="zen.webp" alt="Die Leinwand im Zen-Modus, nur die Zeichnung und oben links der Hinweis Tippen zum Beenden" caption="Zen-Modus. Der Hinweis oben links holt die Leisten zurück." %}

## Bewegen auf der Leinwand

Auf dem Touchscreen nehmen Sie zwei Finger: bewegen zum Verschieben, auseinander- oder zusammenziehen zum Zoomen, drehen zum Drehen der Leinwand. Alles drei funktioniert gleichzeitig, solange Sie nichts davon sperren. War gerade ein Strich im Gange, als der zweite Finger aufgesetzt wurde, wird er verworfen.

Mit der Maus zoomt das Mausrad um den Mauszeiger, Ziehen mit gedrückter mittlerer Taste verschiebt. Auf dem Trackpad eines Mac zoomen Sie mit zwei Fingern, wischen zum Verschieben und drehen zwei Finger zum Drehen. Auf der Tastatur zoomen <kbd>Strg</kbd>+<kbd>=</kbd> und <kbd>Strg</kbd>+<kbd>-</kbd> hinein und heraus, <kbd>Strg</kbd>+<kbd>0</kbd> setzt die Ansicht zurück.

Der Zoombereich reicht von 5 % bis 5000 %. Jedes Projekt merkt sich seine letzte Ansicht.

Was ein einzelner Finger tut, entscheiden Sie selbst: Standardmäßig zeichnet er mit dem aktiven Werkzeug, er kann aber auch verschieben, radieren oder immer ein bestimmtes Werkzeug verwenden. Siehe „Fingerverhalten“ in den [Einstellungen](settings.html#eingabe). Stift und Maus verwenden immer das aktive Werkzeug.

## Rückgängig und Wiederholen

Fast alles auf der Leinwand lässt sich rückgängig machen: Striche, Löschen, Transformationen, Änderungen an Ebenen, Raster, Hilfslinien und Hintergrund. Änderungen der Ansicht (Zoom, Verschiebung, Drehung) gehören nicht dazu. Das Ziehen eines Schiebereglers zählt als ein Schritt.

Rückgängig und Wiederholen erreichen Sie über die Pfeile in der Symbolleiste, mit <kbd>Strg</kbd>+<kbd>Z</kbd> und <kbd>Strg</kbd>+<kbd>Umschalt</kbd>+<kbd>Z</kbd> oder per Geste: Standardmäßig macht ein Zwei-Finger-Tippen rückgängig, ein Drei-Finger-Tippen wiederholt. Kritzel Studio merkt sich die letzten 100 Schritte. Wird der Arbeitsspeicher sehr knapp, wird der Verlauf auf die letzten 20 Schritte gekürzt.

## Speichern

Kritzel Studio speichert automatisch, etwa fünf Sekunden nach der letzten Änderung und spätestens alle 20 Sekunden, solange ungespeicherte Änderungen vorliegen. Mitten in einem Strich wird nie gespeichert. Vollständig gespeichert, samt Vorschaubild und aktueller Ansicht, wird außerdem, wenn die App in den Hintergrund geht, wenn Sie <kbd>Strg</kbd>+<kbd>S</kbd> drücken und wenn Sie zur Galerie zurückkehren.

Schlägt das Speichern fehl, etwa weil das Gerät voll ist, erscheint die Meldung „Zeichnung konnte nicht gespeichert werden“. Wenn Sie das Projekt dann verlassen möchten, fragt Kritzel Studio nach, ob Sie bleiben („Abbrechen“) oder trotzdem gehen möchten („Trotzdem verlassen“); dabei gehen die ungespeicherten Änderungen verloren.
