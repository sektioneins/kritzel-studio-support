---
title: Auswählen und Transformieren
description: Striche per Antippen oder Lasso auswählen und anschließend verschieben, skalieren, drehen, neigen, verzerren, spiegeln, gruppieren, sperren oder löschen.
---

Alles, was Sie zeichnen, bleibt ein Objekt, das Sie später auswählen und ändern können. Das Auswahlwerkzeug (<kbd>V</kbd>) ist das erste Werkzeug der Werkzeugleiste.

## Auswählen

- Tippen Sie einen Strich an, um ihn auszuwählen. Die bisherige Auswahl wird dabei ersetzt.
- Ziehen Sie auf der Leinwand, um ein Lasso zu zeichnen. Jeder Strich mit einem Punkt innerhalb des Lassos wird ausgewählt.
- Tippen Sie auf eine leere Stelle, um die Auswahl aufzuheben.
- <kbd>Strg</kbd>+<kbd>A</kbd> wählt alles auf sichtbaren, nicht gesperrten Ebenen aus.
- „Gleiche Farbe“ im Eigenschaftenfeld wählt alle Striche aus, die die Farbe der aktuellen Auswahl haben.

{% include fig.html src="lasso.webp" alt="Ein Lasso als blau durchscheinender Kreis um zwei Tannen" caption="Ein Lasso um die Bäume." %}

Gruppierte Striche werden immer gemeinsam ausgewählt. Striche auf ausgeblendeten oder gesperrten Ebenen lassen sich nicht auswählen. Einzeln gesperrte Striche können Sie dagegen auswählen, damit Sie sie entsperren können.

Ein einzelnes Objekt können Sie auch in der Objektliste des [Ebenenfelds](layers.html#objekte) auswählen.

## Der Auswahlrahmen

Eine Auswahl erscheint mit gestricheltem Rahmen, Griffen an Ecken und Kanten und einem runden Griff darüber zum Drehen.

{% include fig.html src="selection.webp" alt="Die ausgewählte Sonne mit gestricheltem Rahmen, acht Griffen, Drehgriff und dem Auswahlfeld rechts" caption="Ein ausgewählter Strich und seine Eigenschaften." %}

- Ziehen Sie innerhalb des Rahmens, um die Auswahl zu verschieben.
- Ziehen Sie einen Eckgriff, um gleichmäßig von der gegenüberliegenden Ecke aus zu skalieren.
- Ziehen Sie einen Kantengriff, um in eine Richtung zu strecken.
- Ziehen Sie den runden Griff über dem Rahmen, um um die Mitte zu drehen.

Jedes Ziehen ist ein Rückgängig-Schritt. Ist in den Rastereinstellungen „Maße anzeigen“ eingeschaltet, steht die Größe der Auswahl unter dem Rahmen.

## Transformationsarten

Die Schaltflächen oben im Eigenschaftenfeld legen fest, was die Griffe tun:

| Art | Wirkung der Griffe |
|---|---|
| „Skalieren“ | Die oben beschriebene Standardart. |
| „Neigen“ | Kantengriffe schrägen die Auswahl seitlich oder nach oben und unten ab. Eckgriffe skalieren weiterhin, Drehen funktioniert ebenfalls. |
| „Verzerren“ | Jeder Eckgriff lässt sich frei bewegen, etwa für perspektivische Verzerrungen. In dieser Art funktionieren nur die Ecken und das Verschieben. |
| „Rahmen“ | Verschiebt die Ecken des Rahmens, ohne die Striche zu verändern. Der angepasste Rahmen erscheint orange; „Rahmen zurücksetzen“ stellt ihn wieder her. |

Wenn Sie eine Auswahl aus mehreren getrennten Objekten drehen, neigen oder verzerren, gruppiert Kritzel Studio sie automatisch, damit ihre Anordnung erhalten bleibt.

## Ausgewählte Striche ändern

{% include fig.html src="selection_multi.webp" alt="Acht ausgewählte Striche mit gemischter Farbe, Größe und Deckkraft im Eigenschaftenfeld und der Schaltfläche Gruppieren" caption="Unterscheiden sich die ausgewählten Striche, zeigt das Feld „(gemischt)“." %}

Das Eigenschaftenfeld zeigt Farbe, Größe und Deckkraft der Auswahl. Unterscheiden sich die ausgewählten Striche, steht „(gemischt)“ am Wert und das Farbfeld zeigt ein Fragezeichen; ein neuer Wert gilt dann für alle. Bei Rechtecken erscheint zusätzlich „Eckenradius“.

Unter den Reglern folgen diese Schaltflächen:

| Schaltfläche | Wirkung |
|---|---|
| „Horiz.“ / „Vert.“ | Spiegelt die Auswahl horizontal oder vertikal. |
| „Löschen“ | Löscht die Auswahl. <kbd>Entf</kbd> und die Rücktaste tun dasselbe. |
| „Gleiche Farbe“ | Wählt alle Striche aus, die die Farbe der Auswahl haben. |
| „Sperren“ / „Entsperren“ | Sperrt die ausgewählten Striche, damit sie nicht versehentlich verschoben, verändert oder radiert werden. |
| „Gruppieren“ | Fasst mehrere Objekte zu einer Gruppe zusammen, die als Ganzes ausgewählt und bewegt wird. Erscheint ab zwei ausgewählten Objekten. |
| „Gruppierung aufheben“ | Teilt die ausgewählten Gruppen wieder auf. |

Ist genau ein Textobjekt ausgewählt, zeigt das Feld stattdessen die Textoptionen, darunter „Text bearbeiten…“.

Enthält eine Auswahl gesperrte Striche, lässt sie sich weder verschieben noch transformieren noch löschen. Kritzel Studio meldet dann „Die Auswahl enthält gesperrte Objekte. Entsperre sie zuerst.“

Kopieren und Einfügen von Strichen gibt es noch nicht. Um eine Zeichnung zu vervielfältigen, duplizieren Sie ihre Ebene oder das ganze Projekt.

## Das Kontextmenü (Desktop)

Auf Mac und PC öffnet ein Rechtsklick auf die Leinwand ein Kontextmenü. Sein Inhalt hängt davon ab, wohin Sie klicken:

- Bei einer Auswahl: „Horizontal spiegeln“, „Vertikal spiegeln“, „Gleiche Farbe auswählen“, „Sperren“ oder „Entsperren“, „Gruppieren“ oder „Gruppierung aufheben“ und „Löschen“.
- Auf einem Strich, wenn nichts ausgewählt ist: „Strich auswählen“, „Gleiche Farbe auswählen“ und „Löschen“.
- Auf leerer Leinwand: „Alle auswählen“ und „Ebenen ein-/ausblenden“.
