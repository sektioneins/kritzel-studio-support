---
title: Raster, Hilfslinien und Hintergründe
description: Raster und Perspektivraster einrichten, an Rasterlinien einrasten, Lineale und Ellipsen als Hilfslinien setzen, Maße anzeigen sowie Hintergründe und Vorlagen wählen.
---

Raster, Hilfslinien und Hintergrund werden mit jedem Projekt gespeichert und lassen sich wie jede andere Änderung rückgängig machen.

## Raster

Tippen Sie in der Symbolleiste auf das Raster-Symbol, um die Rastereinstellungen zu öffnen.

{% include fig.html src="grid.webp" alt="Ein Grundriss auf blauem Hintergrund mit Karoraster und geöffneten Rastereinstellungen" caption="Ein Karoraster auf dem Hintergrund „Blaupause“." %}

Wählen Sie eine Rasterart: „Aus“, „Punkt“, „Karo“, „Liniert“ (waagerechte Linien wie auf einem Notizblock), „Iso“ (isometrisch) oder „Drei“ (Dreiecke). Die Perspektivraster „1-Pkt“, „2-Pkt“ und „3-Pkt“ folgen weiter unten. Weitere Einstellungen:

- „Abstand“ (8 bis 100) ist der Abstand der Rasterlinien.
- „Unterteilungen“ (nur Karoraster) zeichnet jede n-te Linie kräftiger.
- „Deckkraft“ (5 % bis 50 %) bestimmt, wie deutlich das Raster zu sehen ist. Seine Farbe passt sich automatisch dem Hintergrund an.
- „Am Raster einrasten“ hat drei Zustände. Mehrfaches Antippen schaltet von aus über das Einrasten an Linien zum Einrasten an Linien und Schnittpunkten. Stift- und Bleistiftstriche, die nahe einer Rasterlinie beginnen, folgen ihr; Formen setzen ihre Ecken auf Schnittpunkte.
- „Maße anzeigen“ zeigt Breite und Höhe (in Punkt) beim Zeichnen einer Form und unter einer Auswahl.
- „Raster im Hintergrund“ zeichnet das Raster hinter statt über Ihre Striche.

{% include fig.html src="measurements.webp" alt="Ein ausgewähltes abgerundetes Rechteck mit der Angabe 118 pt x 88 pt darunter" caption="Mit „Maße anzeigen“ steht die Größe einer Auswahl darunter." %}

## Perspektivraster

„1-Pkt“, „2-Pkt“ und „3-Pkt“ zeichnen Fluchtlinien zu einem, zwei oder drei Fluchtpunkten, auf Wunsch mit Horizontlinie.

{% include fig.html src="grid_perspective.webp" alt="Ein Zwei-Punkt-Perspektivraster mit Horizontlinie und einem blauen Fluchtpunktgriff am rechten Rand" caption="Ein Zwei-Punkt-Perspektivraster. Die blauen Griffe sind die Fluchtpunkte." %}

Ziehen Sie den runden Griff eines Fluchtpunkts, um ihn zu verschieben; das klappt mit jedem Werkzeug. „Liniendichte“ (4 bis 40) bestimmt die Zahl der Linien, „Horizont anzeigen“ blendet den Horizont ein oder aus. „Fluchtpunkte speichern“ merkt sich ihre aktuelle Lage, „Fluchtpunkte zurücksetzen“ bringt sie dorthin zurück (oder in die Grundstellung, wenn nichts gespeichert ist). Bei Perspektivrastern gibt es kein Einrasten.

## Hilfslinien

Hilfslinien sind Lineale und Ellipsen, die Sie auf die Leinwand legen und an denen Sie entlangzeichnen, wie mit Lineal oder Schablone auf Papier. Sie gehören nicht zur Zeichnung und werden nicht exportiert.

Tippen Sie in der Symbolleiste auf das Lineal-Symbol. Das Feld „Hilfslinien“ öffnet sich, die Hilfslinien werden eingeschaltet, und falls noch keine existieren, erscheinen zwei gekreuzte Lineale in der Mitte der Ansicht.

{% include fig.html src="guides.webp" alt="Eine Ellipsen-Hilfslinie über der Zeichnung mit ihren Griffen und dem Feld Hilfslinien mit Reglern für Drehung, Radius und Bogenwinkel" caption="Eine Ellipsen-Hilfslinie in Bearbeitung." %}

- „+ Lineal“ und „+ Ellipse“ setzen eine neue Hilfslinie in die Mitte der Ansicht.
- Tippen Sie eine Hilfslinie in der Liste an, um sie zu bearbeiten: „Drehung“, bei Linealen „Länge“, bei Ellipsen „Radius X“, „Radius Y“ und „Bogenwinkel“ (für Bögen). Der Papierkorb löscht sie, „Alle entfernen“ löscht alle.
- Das Kästchen neben „Hilfslinien“ schaltet alle Hilfslinien ein oder aus.

Solange das Feld geöffnet ist, bearbeiten Sie Hilfslinien auch direkt auf der Leinwand: Ziehen verschiebt eine Hilfslinie, das Ende eines Lineals dreht es und ändert seine Länge, der runde Griff dreht, und die Griffe einer Ellipse ändern Radien und Bogenwinkel. Zwei Finger auf einer Hilfslinie verschieben, drehen und (bei Ellipsen) skalieren sie. Ist das Feld geschlossen, bleiben die Hilfslinien an ihrem Platz und lassen sich nicht versehentlich verschieben.

### An Hilfslinien einrasten

Bei eingeschalteten Hilfslinien zeigt die Symbolleiste eine Zielscheibe: „An Hilfslinien einrasten“. Ist sie aktiv, folgt jeder Stift-, Bleistift- oder Formstrich, der nahe einer Hilfslinie beginnt, genau dieser Hilfslinie. So ziehen Sie gerade Linien am Lineal entlang oder saubere Bögen an einer Ellipse.

## Hintergrund

Das Bild-Symbol in der Symbolleiste öffnet die Hintergrundeinstellungen.

{% include fig.html src="background.webp" size="narrow" alt="Das Feld Hintergrund mit den Vorlagen Cremeweiß, Weiß, Transparent, Dunkel und Blaupause sowie Eigene Farbe, Als Vorlage speichern und Vorlagen verwalten" caption="Das Feld „Hintergrund“." %}

Tippen Sie eine Vorlage an, um ihre Hintergrundfarbe und ihr Raster in einem Schritt zu übernehmen. Mit „Eigene Farbe...“ wählen Sie eine beliebige Hintergrundfarbe. „Transparent“ zeigt ein Schachbrettmuster; PNG-Exporte eines solchen Projekts haben einen transparenten Hintergrund.

## Vorlagen

Vorlagen fassen Hintergrundfarbe, Raster und Anfangsfarbe des Stifts zusammen. Sie werden beim Anlegen eines Projekts und im Feld „Hintergrund“ angeboten. Kritzel Studio bringt fünf mit:

| Vorlage | Hintergrund | Raster | Stiftfarbe |
|---|---|---|---|
| „Cremeweiß“ | warmes Cremeweiß | keines | Dunkelgrau |
| „Weiß“ | Weiß | keines | Schwarz |
| „Transparent“ | transparent | keines | Schwarz |
| „Dunkel“ | fast Schwarz | keines | Weiß |
| „Blaupause“ | Dunkelblau | Karo | Weiß |

„Als Vorlage speichern“ legt den aktuellen Hintergrund, das Raster und die Stiftfarbe als neue Vorlage an. „Vorlagen verwalten“ öffnet die Vorlagenliste in den Einstellungen, wo Sie Vorlagen bearbeiten, umbenennen, umsortieren und löschen. Die erste Vorlage der Liste ist die Standardvorlage für neue Projekte. Siehe [Einstellungen](settings.html#hintergrundvorlagen).
