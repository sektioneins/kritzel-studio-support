---
title: Import und Export
description: Bilder und SVG-Dateien importieren, Dateien aus anderen Apps öffnen und Zeichnungen als PNG, JPG, SVG, PDF oder .kritzel exportieren.
---

## Bilder importieren

Tippen Sie innerhalb eines Projekts auf das Download-Symbol in der Symbolleiste und wählen Sie „Bild…“. Kritzel Studio nimmt PNG-, JPG-, GIF-, BMP- und WebP-Dateien an.

Das Bild landet auf einer neuen Ebene über der aktiven, benannt nach der Datei. Es wird auf höchstens 800 × 800 Leinwandeinheiten verkleinert, in der Ansicht zentriert und gleich ausgewählt, sodass Sie es sofort verschieben, skalieren und drehen können. Importierte Bilder werden im Projekt gespeichert. Gut geeignet ist das etwa für ein Referenzfoto oder einen Scan auf einer eigenen Ebene, den Sie auf einer Ebene darüber nachzeichnen; die Bildebene sperren Sie dabei oder verringern ihre Deckkraft.

## SVG-Dateien importieren

Mit „SVG…“ im selben Menü importieren Sie Vektorgrafiken. Die Grafik landet auf einer neuen Ebene, benannt nach der Datei und in der Ansicht zentriert, und jede Form wird ein bearbeitbarer Strich oder eine Form. Ein kurzer Bericht zeigt danach, wie viele Elemente importiert wurden und was sich nicht übernehmen ließ.

Kritzel Studio versteht die gängigen Bestandteile von SVG: Rechtecke, Kreise, Ellipsen, Linien, Polylinien, Polygone und Pfade, Gruppen, Transformationen, Füll- und Linienfarben und -breiten, Deckkraft, wiederverwendete Elemente (`<use>`) und einfache Stylesheets. Manches wird vereinfacht oder weggelassen, und der Bericht nennt es:

- Text wird übersprungen.
- Eingebettete Bilder werden übersprungen.
- Verläufe werden zu einer einzigen Farbe (der ersten Farbe des Verlaufs).
- Beschneidungen, Masken und Filter werden ignoriert; die Form wird ohne sie übernommen.
- Eine Form mit Füllung und Kontur behält nur die Füllung.
- Gedrehte oder geneigte Rechtecke und Ellipsen werden zu Polygonen.
- Sehr detailreiche Zeichnungen werden ausgedünnt, damit der Import zügig bleibt.

## Dateien aus anderen Apps öffnen

Kritzel Studio kann Dateien auch direkt aus einem Dateimanager, der Dateien-App, dem Finder oder dem Explorer öffnen („Öffnen mit“). Jede Datei wird zu einem neuen Projekt, das sich sofort öffnet:

- Eine `.kritzel`-Datei wird als Kopie auf der obersten Ebene der Galerie importiert.
- Eine SVG-Datei wird zu einem neuen Projekt mit dem Namen der Datei; die Grafik liegt auf der ersten Ebene.
- Ein Bild wird zu einem neuen Projekt mit dem Bild auf einer eigenen Ebene.

Welche Dateitypen das System Kritzel Studio anbietet, hängt von der Plattform ab. Auf iPad und Mac lassen sich `.kritzel`-, SVG- und Bilddateien mit Kritzel Studio öffnen. Unter Android verwenden Sie „Öffnen mit“ im Dateimanager (im Teilen-Menü von Android erscheint Kritzel Studio nicht). Unter Windows öffnet ein Doppelklick auf eine `.kritzel`-Datei Kritzel Studio, und bei SVG-Dateien steht Kritzel Studio unter „Öffnen mit“ zur Wahl.

## Eine Zeichnung exportieren

Tippen Sie auf das Teilen-Symbol in der Symbolleiste oder drücken Sie <kbd>Strg</kbd>+<kbd>E</kbd>, um den Export-Dialog zu öffnen.

{% include fig.html src="export.webp" size="narrow" alt="Der Export-Dialog mit Format PNG, Bereich Gesamte Leinwand, Auflösung 150 DPI, dem Kästchen Transparenter Hintergrund und der Bildgröße in Pixeln" caption="Export als PNG. Unter den Optionen steht die Größe des Bilds." %}

Wählen Sie ein Format:

| Format | Geeignet für | Gut zu wissen |
|---|---|---|
| PNG | Bilder weitergeben, Transparenz | Auflösung 72, 150, 300 oder 600 DPI. „Transparenter Hintergrund“ lässt den Hintergrund leer. |
| JPG | Fotos und kleine Dateien | Dieselben Auflösungen, dazu „Qualität“ (10 % bis 100 %, Standard 90 %). JPG kennt keine Transparenz; ein transparenter Hintergrund wird weiß. |
| SVG | Weiterbearbeitung in Vektorprogrammen | Ebenen werden benannte Gruppen, Text bleibt Text. Bilder fehlen, Pinselstrukturen werden einfarbig. Schriftarten werden nur namentlich genannt, nicht eingebettet. |
| PDF | Drucken und Dokumente | Eine Seite, genau so groß wie die Zeichnung. Striche, Formen und Text bleiben Vektoren, Schriftarten werden eingebettet. Mit „Texturen & Bilder einbeziehen“ (standardmäßig an) werden strukturierte Striche und Bilder als Bild eingebettet; ausgeschaltet entsteht ein reines Vektor-PDF ohne sie. |
| KRITZEL | Sicherungen und Umzug auf ein anderes Gerät | Das vollständige Projekt mit Bildern und Ebenen. Lässt sich verlustfrei wieder importieren. |

„Bereich“ bestimmt, was exportiert wird. „Gesamte Leinwand“ exportiert alles auf sichtbaren Ebenen, zugeschnitten auf die Zeichnung; ausgeblendete Ebenen fehlen. „Auswahl“ exportiert nur die ausgewählten Objekte (wählen Sie sie vorher aus).

Geht in einem Format etwas verloren, warnt der Dialog vor dem Export, zum Beispiel „14 texturierte Striche werden als einfarbige Flächen exportiert“.

{% include fig.html src="export_svg.webp" size="narrow" alt="Der Export-Dialog für SVG mit dem Hinweis, dass 14 texturierte Striche als einfarbige Flächen exportiert werden" caption="Ein Hinweis vor einem SVG-Export." %}

Die Auflösung bezieht sich auf die Größe der Zeichnung: Bei 72 DPI entspricht eine Leinwandeinheit einem Pixel. Die längere Seite eines exportierten Bilds ist auf 8192 Pixel begrenzt. Würden Ihre Einstellungen das überschreiten, zeigt der Dialog die Auflösung an, die tatsächlich verwendet wird.

Die Datei erhält den Namen des Projekts. Auf dem Tablet öffnet Kritzel Studio anschließend das Teilen-Menü, über das Sie die Datei speichern, verschicken oder in einer anderen App öffnen. Auf Mac und PC wählen Sie den Speicherort in einem Speichern-Dialog.

Mit welchem Format und welcher Auflösung der Dialog startet, legen Sie in den [Einstellungen](settings.html#export) fest.

## Ganze Projekte exportieren

Um ein oder mehrere vollständige Projekte als `.kritzel`-Dateien zu exportieren, verwenden Sie „Exportieren“ in der Galerie. Siehe [Projekte sichern](gallery.html#projekte-sichern).
