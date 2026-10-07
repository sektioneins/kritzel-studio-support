---
title: Einstellungen
description: Alle Einstellungen von Kritzel Studio mit ihren Standardwerten.
---

Die Einstellungen öffnen Sie mit dem Zahnrad neben dem App-Namen in der Galerie. Sie gelten für die ganze App, nicht für ein einzelnes Projekt. Hier stehen sie in der Reihenfolge, in der die App sie zeigt.

{% include fig.html src="settings_1.webp" size="tall" alt="Die Einstellungen mit den Bereichen Darstellung, Eingabe und Gesten" caption="Die ersten Bereiche der Einstellungen." %}

## Darstellung {#darstellung}

„Design“ wechselt zwischen „Hell“, „Dunkel“ und „System“ (folgt dem Gerät). Standard ist „Dunkel“. „Akzentfarbe“ ändert die Hervorhebungsfarbe der Oberfläche; „Standard“ verwendet den neutralen Akzent des Designs.

## Eingabe {#eingabe}

„Stift-Druckkurve“ ist eine optionale, für die ganze App geltende Kalibrierung Ihres Stifts. Schalten Sie „Globale Druckkurve verwenden“ ein, um sie anzupassen, etwa wenn sich Ihr Stift zu weich oder zu hart anfühlt. Sie wirkt vor der Druckkurve des jeweiligen Pinsel-Presets. Standardmäßig aus.

„Fingerverhalten“ legt fest, was ein einzelner Finger auf der Leinwand tut (nur auf Tablets):

| Option | Wirkung |
|---|---|
| „Zeichnen“ | Der Finger verwendet wie der Stift das aktive Werkzeug. Das ist der Standard. |
| „Verschieben“ | Der Finger verschiebt die Leinwand. Praktisch, wenn Sie nur mit dem Stift zeichnen. |
| „Radieren“ | Der Finger radiert immer, egal welches Werkzeug aktiv ist. |
| „Werkzeug“ | Der Finger verwendet immer das unter „Fingerwerkzeug“ gewählte Werkzeug (Auswahl, Stift, Bleistift, Radierer, Form, Verschieben oder Schneiden). |

Stift und Maus sind davon nicht betroffen, und mit zwei oder mehr Fingern wird immer verschoben und gezoomt.

## Gesten {#gesten}

Auf Tablets können Sie jeder dieser Gesten eine Aktion zuweisen („Keine“, „Rückgängig“, „Wiederherstellen“ oder „Ansicht zurücksetzen“):

| Geste | Standard |
|---|---|
| „Zwei-Finger-Tippen“ | „Rückgängig“ |
| „Drei-Finger-Tippen“ | „Wiederherstellen“ |
| „Ein-Finger-Doppeltippen“ | „Keine“ |
| „Zwei-Finger-Doppeltippen“ | „Keine“ |
| „Drei-Finger-Doppeltippen“ | „Keine“ |
| „Pinch zum Minimum“ (schnelles Zusammenziehen, bis sich die Finger fast berühren) | „Ansicht zurücksetzen“ |
| „Pinch zum Maximum“ (schnelles, weites Auseinanderziehen) | „Keine“ |

## Oberfläche {#oberflaeche}

{% include fig.html src="settings_3.webp" size="tall" alt="Die Bereiche Oberfläche, Leinwand und Export in den Einstellungen" caption="Oberfläche, Leinwand und Export." %}

- „Sprache“: „System“ (Standard), „English“ oder „Deutsch“.
- „Händigkeit“: Bei „Rechts“ (Standard) liegt die Werkzeugleiste links, bei „Links“ rechts und die Felder links.
- „Leistendichte“: „Kompakt“ (Standard) oder „Komfortabel“ mit größeren Schaltflächen.
- „Werkzeugnamen anzeigen“: zeigt unter jedem Werkzeugsymbol seinen Namen. Standardmäßig aus.

## Leinwand {#leinwand}

„Zurücksetzen-Verhalten“ legt fest, was die Schaltfläche „Ansicht zurücksetzen“ zurücksetzt: „Verschiebung zurücksetzen“, „Zoom zurücksetzen“ und „Drehung zurücksetzen“. Alle drei sind standardmäßig an.

## Export {#export}

„Standardformat“ (PNG, JPG, SVG oder PDF; Standard PNG) und „Standard-DPI“ (72, 150, 300 oder 600; Standard 150) sind die Werte, mit denen der Export-Dialog startet. Bei jedem Export können Sie sie trotzdem ändern.

## Hintergrundvorlagen {#hintergrundvorlagen}

{% include fig.html src="settings_2.webp" size="tall" alt="Die Liste der Hintergrundvorlagen mit Cremeweiß als Standard, darunter der Anfang der Tastenkürzel" caption="Hintergrundvorlagen und der Anfang der Tastenkürzel." %}

Diese Liste enthält die Vorlagen, die für neue Projekte und im Feld „Hintergrund“ angeboten werden. Die erste Vorlage trägt die Markierung „Standard“ und wird für neue Projekte und den Schnellstart verwendet.

- Ziehen Sie eine Vorlage an ihrem Griff, um die Reihenfolge zu ändern. Wandert eine andere Vorlage nach oben, wird sie zur Standardvorlage.
- Doppeltippen auf einen Namen benennt die Vorlage um.
- Der Stift öffnet „Vorlage bearbeiten“: Name, Hintergrundfarbe (oder transparent), Rastertyp und Rastereinstellungen sowie „Anfangs-Stiftfarbe“.
- Der Papierkorb löscht eine Vorlage nach einer Rückfrage.
- „Vorlage hinzufügen“ legt eine neue an; „Auf Standards zurücksetzen“ stellt die fünf eingebauten Vorlagen wieder her und entfernt Ihre eigenen.

## Tastenkürzel {#tastenkuerzel}

Jedes Tastenkürzel lässt sich ändern. Tippen Sie ein Kürzel an und drücken Sie dann die neue Tastenkombination; <kbd>Esc</kbd> bricht ab. Ist die Kombination schon vergeben, fragt Kritzel Studio, ob sie neu zugewiesen werden soll („Neu zuweisen“). Neben geänderten Kürzeln erscheint ein Symbol zum Zurücksetzen, und „Alle auf Standard zurücksetzen“ stellt alle wieder her. Die Standardbelegung finden Sie unter [Tastenkürzel und Gesten](shortcuts.html).

## Erweitert {#erweitert}

Tippen Sie auf „Erweitert“, um diesen Bereich aufzuklappen.

{% include fig.html src="settings_advanced.webp" size="tall" alt="Der Bereich Erweitert mit Speicherüberwachung, Schwellen, Viewport-Rasterisierung, Trefferbereichen der Griffe und Alle Vorschauen neu erstellen" caption="Die erweiterten Einstellungen." %}

- „Speicherüberwachung“ beobachtet den Speicherverbrauch und warnt, bevor er knapp wird. Auf Tablets standardmäßig an, am Desktop aus. „Warnschwelle“ (Standard 90 %) und „Kritische Schwelle“ (Standard 95 %) legen fest, wann gewarnt wird. Siehe [Speicherwarnungen](help.html#speicherwarnungen).
- „Viewport-Rasterisierung“ rendert nur den sichtbaren Teil der Zeichnung und hält so den Speicherverbrauch bei großen Leinwänden gering. Auf Tablets standardmäßig an.
- „Trefferbereich der Griffe (Maus/Stift)“ (Standard 12 px) und „Trefferbereich der Griffe (Finger)“ (Standard 20 px) bestimmen, wie genau Sie zielen müssen, um einen Auswahlgriff zu fassen.
- „Alle Vorschauen neu erstellen“ erzeugt die Vorschaubilder aller Projekte in der Galerie neu.

## Über Kritzel Studio {#ueber}

„Über Kritzel Studio“ zeigt die Version, verlinkt die Webseite und den Issue-Tracker für Fehlermeldungen und Funktionswünsche und listet die Open-Source-Lizenzen der verwendeten Komponenten. Sie erreichen den Dialog auch, indem Sie in der Galerie auf den App-Namen tippen.
