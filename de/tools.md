---
title: Zeichenwerkzeuge
description: So verwenden Sie Stift, Bleistift, Radierer, Form, Pipette, Text, Verschieben, Schneiden und Punkte.
---

Die Werkzeugleiste enthält zehn Werkzeuge. Dieses Kapitel beschreibt alle außer der Auswahl, die ein eigenes Kapitel hat: [Auswählen und Transformieren](selection.html). Der Buchstabe hinter jedem Werkzeugnamen ist sein Tastenkürzel.

Ist die aktive Ebene gesperrt oder ausgeblendet, zeichnen die Werkzeuge nicht und zeigen einen kurzen Hinweis: „Die aktive Ebene ist gesperrt. Zum Zeichnen entsperren.“ bzw. „Die aktive Ebene ist ausgeblendet. Zum Zeichnen einblenden.“ Entsperren oder einblenden können Sie die Ebene im [Ebenenfeld](layers.html).

## Stift (P) und Bleistift (N) {#stift-p-und-bleistift-n}

Stift und Bleistift zeichnen Freihandstriche. Sie unterscheiden sich nur durch ihre Pinsel: Der Stift beginnt mit dem Preset „Variable Breite“, der Bleistift mit „Weich“, einem Bleistift mit Struktur. Beim Wechsel zwischen beiden werden Pinsel, Breite und Deckkraft des jeweiligen Standard-Presets übernommen.

Das Eigenschaftenfeld zeigt:

- den Namen des Pinsels (Presets); antippen, um einen anderen zu wählen, siehe [Pinsel und Farben](brushes-colours.html);
- „Farbe“ mit Harmonievorschlägen und Ihrer Palette;
- „Größe“ von 1 bis 50;
- „Deckkraft“ von 5 % bis 100 %.

Mit einem Stift folgt die Strichstärke Ihrem Druck. Mit Finger oder Maus berechnen die meisten Pinsel den Druck aus der Zeichengeschwindigkeit. Wie der Druck umgesetzt wird, stellen Sie in den Pinseleinstellungen und mit einer globalen Druckkurve in den [Einstellungen](settings.html#eingabe) ein.

Ist ein Raster mit Einrasten aktiv, folgt ein Strich, der nahe einer Rasterlinie beginnt, dieser Linie. Sind Hilfslinien eingeschaltet und „An Hilfslinien einrasten“ aktiv, folgt ein Strich, der nahe einer Hilfslinie beginnt, ihr auf ganzer Länge. Siehe [Raster, Hilfslinien und Hintergründe](grids-guides.html).

## Radierer (E) {#radierer-e}

Der Radierer entfernt ganze Striche. Tippen Sie einen Strich an oder wischen Sie über mehrere; sie verschwinden schon während der Bewegung. Ein Wischen ist ein Rückgängig-Schritt. Der Radierer wirkt auf alle sichtbaren, nicht gesperrten Ebenen, nicht nur auf die aktive, und lässt gesperrte Striche aus. Einstellungen gibt es keine.

Um nur einen Teil eines Strichs zu entfernen, schneiden Sie ihn vorher mit dem Werkzeug [Schneiden](#schneiden-k) durch oder bearbeiten seine Punkte mit dem Werkzeug [Punkte](#punkte-a).

## Form (S) {#form-s}

Das Werkzeug „Form“ zeichnet Linien, Rechtecke, Ellipsen, Polygone und Polygonzüge. Die Art der Form wählen Sie oben im Eigenschaftenfeld.

{% include fig.html src="panel_shape.webp" alt="Das Eigenschaftenfeld des Formwerkzeugs mit Linie, Rechteck, Ellipse, Polygon und Polygonzug, der Füllung und dem Eckenradius" caption="Optionen für Formen: Art, Füllung, Eckenradius (Rechtecke) bzw. Seitenzahl (Polygone), Farbe, Größe und Deckkraft." %}

Für Linie, Rechteck, Ellipse oder Polygon drücken Sie am Startpunkt und ziehen bis zur gegenüberliegenden Ecke. Weitere Optionen:

- „Füllung“ wechselt zwischen „Kontur“ und „Gefüllt“.
- „Eckenradius“ (0 bis 100) rundet die Ecken von Rechtecken ab.
- „Seiten“ (3 bis 12) legt die Eckenzahl eines Polygons fest.

Einen Polygonzug bauen Sie Punkt für Punkt: Jedes Antippen setzt eine Ecke. Tippen Sie erneut auf den ersten Punkt, um die Form zu schließen (dafür sind mindestens drei Punkte nötig). Solange Sie an einem Polygonzug arbeiten, zeigt das Feld „Fertig“, das ihn als offene Linie übernimmt, und „Abbrechen“, das ihn verwirft. Auch der Wechsel zu einem anderen Werkzeug übernimmt ihn als offene Linie.

Ist in den Rastereinstellungen „Maße anzeigen“ eingeschaltet, sehen Sie beim Ziehen Breite und Höhe der Form. Start- und Endpunkte rasten genauso an Rasterschnittpunkten und Hilfslinien ein wie Stiftstriche.

## Pipette (I) {#pipette-i}

Tippen Sie einen beliebigen Strich an, um seine Farbe zu übernehmen. Danach wechselt Kritzel Studio zurück zum vorherigen Werkzeug, nun mit der neuen Farbe. Berücksichtigt werden nur sichtbare, nicht gesperrte Ebenen.

## Text (T) {#text-t}

Tippen Sie auf die Stelle der Leinwand, an der der Text beginnen soll. Der Dialog „Text hinzufügen“ öffnet sich:

{% include fig.html src="text_dialog.webp" size="narrow" alt="Der Dialog Text hinzufügen mit Textfeld, Schriftart, Farbe, Größe, Fett, Kursiv, Ausrichtung und Vorschau" caption="Der Dialog „Text hinzufügen“." %}

- Geben Sie Ihren Text ein. Zeilenumbrüche sind erlaubt.
- „Schriftart“: Roboto, Open Sans, Montserrat, Lora, Source Code Pro, Caveat, Pacifico oder Permanent Marker.
- „Farbe“ und „Größe“ (8 bis 144).
- Fett, kursiv und Ausrichtung (links, zentriert, rechts).

„Hinzufügen“ setzt den Text. Um einen vorhandenen Text später zu ändern, tippen Sie ihn mit dem Auswahlwerkzeug doppelt an, oder wählen Sie ihn aus und tippen im Eigenschaftenfeld auf „Text bearbeiten…“. Ein Antippen mit dem Textwerkzeug legt dagegen einen neuen Text an.

Text lässt sich wie jedes andere Objekt verschieben, skalieren und drehen.

## Verschieben (U) {#verschieben-u}

Das Werkzeug „Verschieben“ schiebt die Punkte von Strichen umher, als würden Sie sie mit dem Finger anstoßen. Ein Kreis zeigt den Wirkungsbereich. Ziehen Sie über einen Strich: Punkte nahe der Kreismitte bewegen sich am stärksten.

„Radius“ (10 bis 200, in Bildschirmpixeln) legt die Kreisgröße fest, „Stärke“ (10 % bis 100 %), wie weit sich die Punkte bewegen. Das Werkzeug wirkt nur auf die aktive Ebene und lässt Text, Bilder und gesperrte Striche aus.

## Schneiden (K) {#schneiden-k}

„Schneiden“ teilt Striche. Ziehen Sie eine gerade Linie über einen oder mehrere Striche; sobald Sie Finger oder Stift anheben, wird jeder gekreuzte Strich in einzelne Stücke geteilt. Die Stücke können Sie danach einzeln auswählen, umfärben oder löschen.

{% include fig.html src="slice.webp" alt="Eine rot gestrichelte Schnittlinie quer über die Bergumrisse" caption="Die gestrichelte Linie zeigt, wo die Striche geteilt werden." %}

Das Werkzeug wirkt auf alle sichtbaren, nicht gesperrten Ebenen. Text, Bilder und gesperrte Striche werden nicht geschnitten.

## Punkte (A) {#punkte-a}

Mit dem Werkzeug „Punkte“ bearbeiten Sie die einzelnen Punkte eines Strichs. Tippen Sie einen Strich an, um ihn auszuwählen; auf seinen Punkten erscheinen Griffe.

{% include fig.html src="points.webp" alt="Ein Bergumriss mit gefüllten Punktgriffen und hohlen Griffen dazwischen" caption="Gefüllte Griffe sind Punkte, hohle Griffe fügen einen neuen Punkt ein." %}

- Ziehen Sie einen gefüllten Griff, um den Punkt zu verschieben.
- Ziehen Sie über eine freie Fläche, um mehrere Punkte mit einem Rechteck auszuwählen, und ziehen Sie dann einen davon, um alle zu verschieben.
- Tippen oder ziehen Sie einen hohlen Griff zwischen zwei Punkten, um dort einen neuen Punkt einzufügen.
- Tippen Sie einen Griff doppelt an, um den Punkt zu löschen, oder wählen Sie Punkte aus und tippen auf „Punkte löschen“ (oder drücken <kbd>Entf</kbd> bzw. die Rücktaste).

Ein Strich braucht mindestens zwei Punkte. Text und Bilder haben keine bearbeitbaren Punkte.

Rechtecke, Ellipsen, Linien und Polygone sind durch ihre Eckpunkte definiert, nicht durch bearbeitbare Punkte. Wählen Sie eine solche Form aus und tippen Sie auf „In Freiform umwandeln“, um daraus einen Polygonzug mit bearbeitbaren Punkten zu machen. Die Form sieht danach genauso aus, der SVG-Export schreibt sie dann aber als Pfad statt als Rechteck- oder Ellipsen-Element.
