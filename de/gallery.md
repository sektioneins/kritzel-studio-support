---
title: Galerie und Projekte
description: Projekte in Ordnern organisieren, suchen und sortieren, mehrere gleichzeitig auswählen, den Papierkorb nutzen und Projekte als .kritzel-Dateien sichern.
---

Die Galerie ist der Startbildschirm von Kritzel Studio. Hier sehen und ordnen Sie Ihre Projekte und Ordner, und von hier aus importieren und sichern Sie ganze Projekte.

## Projektkarten

Jedes Projekt erscheint als Karte mit Vorschaubild, Namen und dem Zeitpunkt der letzten Änderung („Vor 5 Min.“, „Vor 3 Std.“, „Vor 2 T.“ usw.; nach 30 Tagen steht dort das Datum). Tippen Sie auf eine Karte, um das Projekt zu öffnen.

Ordner stehen vor den Projekten. Eine Ordnerkarte zeigt, wie viele Elemente sie enthält; antippen öffnet den Ordner. Innerhalb eines Ordners zeigt eine zweite Zeile unter der Leiste einen Zurück-Pfeil und den Pfad (zum Beispiel „Kritzel Studio › Arbeit › Kunden“). Tippen Sie auf einen Teil des Pfads, um dorthin zu springen. Unter Android beendet die Zurück-Taste zuerst die Mehrfachauswahl, geht dann einen Ordner nach oben und schließt die App erst auf der obersten Ebene.

## Aktionen für Projekte

Tippen Sie auf die drei Punkte einer Karte oder klicken Sie am Desktop mit der rechten Maustaste darauf, um ihr Menü zu öffnen:

{% include fig.html src="gallery_menu.webp" alt="Das Aktionsmenü einer Projektkarte mit Umbenennen, Duplizieren, In Ordner verschieben, Exportieren, Info und In den Papierkorb legen" caption="Das Menü einer Projektkarte. Auf dem Tablet öffnet es sich vom unteren Bildschirmrand." %}

| Aktion | Wirkung |
|---|---|
| „Umbenennen“ | Gibt dem Projekt einen neuen Namen. |
| „Duplizieren“ | Legt eine Kopie mit dem Namen „‹Name› (Kopie)“ an. |
| „In Ordner verschieben“ | Verschiebt das Projekt in einen Ordner. In diesem Dialog können Sie auch einen neuen Ordner anlegen und das Projekt in einem Schritt dorthin verschieben. |
| „Exportieren“ | Speichert das Projekt als `.kritzel`-Datei (nicht als Bild; Bilder exportieren Sie auf der Leinwand). |
| „Info“ | Zeigt Erstellungs- und Änderungsdatum, die Zahl der Ebenen, Striche und Bilder, die Formatversion, die Größe auf dem Datenträger und den Speicherort. |
| „In den Papierkorb legen“ | Verschiebt das Projekt in den Papierkorb. |

## Ordner

Mit „Neuer Ordner“ legen Sie einen Ordner in dem Ordner an, den Sie gerade ansehen. Ordner lassen sich bis zu fünf Ebenen tief verschachteln; auf der fünften Ebene verschwindet die Schaltfläche. Das Menü eines Ordners (drei Punkte oder Rechtsklick) bietet „Umbenennen“, „Ordner verschieben“ und „In den Papierkorb legen“. Beim Verschieben eines Ordners wandert sein ganzer Inhalt mit.

Neue Projekte und importierte `.kritzel`-Dateien landen immer in dem Ordner, den Sie gerade geöffnet haben.

## Suchen, sortieren, Ansicht

Das Suchfeld filtert die Projekte schon beim Tippen nach ihrem Namen. Auf der obersten Ebene durchsucht es alle Ordner (aber nicht den Papierkorb), innerhalb eines Ordners diesen Ordner samt Unterordnern.

„Geändert“ neben dem Suchfeld ist die Sortierung. Antippen wechselt zwischen „Geändert“, „Erstellt“ und „Name“, der Pfeil daneben kehrt die Reihenfolge um. Das nächste Symbol wechselt zwischen Kartenraster und Liste. In der Rasteransicht bestimmt der Schieberegler die Kartengröße: je weiter rechts, desto größer die Karten und desto weniger Spalten. Ganz rechts wählt die App die Spaltenzahl selbst. Sortierung, Ansicht und Kartengröße merkt sich Kritzel Studio.

{% include fig.html src="gallery_list.webp" alt="Die Galerie in der Listenansicht mit aufklappbaren Ordnerzeilen und Projektzeilen mit kleinen Vorschaubildern" caption="Die Listenansicht. Ordner lassen sich direkt aufklappen." %}

In der Listenansicht klappen Sie Ordner direkt in der Liste auf und zu; ein Doppeltippen öffnet den Ordner. Projektzeilen haben hier kein eigenes Menü. Zum Umbenennen oder für die Projektinfo wechseln Sie zurück zur Rasteransicht. Verschieben, Duplizieren, Exportieren und Löschen funktionieren in beiden Ansichten über die Mehrfachauswahl.

In einem schmalen Fenster (Tablet im Hochformat oder kleines Desktop-Fenster) wandern Sortierung, Ansicht und Kartengröße in ein Menü „Ansicht“, und das Suchfeld schrumpft zu einer Lupe.

## Mehrere Projekte auswählen

Halten Sie eine Projektkarte gedrückt, um die Mehrfachauswahl zu starten. Jede Karte zeigt dann ein rundes Kästchen; tippen Sie weitere Karten an, um sie hinzuzufügen. Die Leiste unten zeigt, wie viele Projekte ausgewählt sind, und bietet „Verschieben“, „Duplizieren“, „Exportieren“, „In den Papierkorb legen“ und „Abbrechen“. Heben Sie die Auswahl des letzten Projekts auf, endet die Mehrfachauswahl.

{% include fig.html src="gallery_multiselect.webp" alt="Zwei ausgewählte Projektkarten mit Häkchen und die Aktionsleiste am unteren Rand" caption="Mehrfachauswahl mit zwei Projekten und der Aktionsleiste." %}

## Der Papierkorb

Projekte und Ordner im Papierkorb sind noch nicht gelöscht. Sobald etwas darin liegt, erscheint der Papierkorb als letzte Karte auf der obersten Ebene. Im Papierkorb können Sie Einträge endgültig löschen („Endgültig löschen“) oder mit „Papierkorb leeren“ alles auf einmal entfernen. Beides fragt vorher nach und lässt sich nicht rückgängig machen.

Einen eigenen Befehl zum Wiederherstellen gibt es nicht. Um ein Projekt zurückzuholen, wählen Sie „In Ordner verschieben“ und dann „Stammordner (kein Ordner)“ oder einen beliebigen Ordner, bei einem Ordner „Ordner verschieben“. Aus dem Papierkorb wird nichts automatisch gelöscht.

## Ein Projekt importieren

„Importieren“ in der Galerie öffnet eine `.kritzel`-Datei. Das Projekt wird als Kopie in den aktuell geöffneten Ordner übernommen; die Originaldatei bleibt unverändert. Bilder und SVG-Dateien importieren Sie dagegen innerhalb eines Projekts (siehe [Import und Export](import-export.html)) oder indem Sie sie aus einer anderen App mit Kritzel Studio öffnen.

Schlägt der Import fehl, nennt eine Meldung den Grund: Die Datei ist keine gültige `.kritzel`-Datei, sie stammt aus einer neueren Version von Kritzel Studio, oder sie ist zu groß.

## Projekte sichern {#projekte-sichern}

Ihre Projekte liegen im privaten Speicher der App. Auf iPad und Android sind sie weder in der Dateien-App noch in einem Dateimanager sichtbar, und Android löscht sie beim Deinstallieren der App. Eine Kopie behalten Sie, indem Sie `.kritzel`-Dateien exportieren:

1. Halten Sie ein Projekt gedrückt, um die Mehrfachauswahl zu starten, und tippen Sie alle Projekte an, die Sie sichern möchten.
2. Tippen Sie auf „Exportieren“.
3. Auf dem Tablet öffnet sich das Teilen-Menü: Speichern Sie die Dateien in Ihrem Cloud-Speicher, schicken Sie sie sich selbst oder legen Sie sie in der Dateien-App ab. Am Desktop wählen Sie einen Zielordner.

Eine `.kritzel`-Datei enthält das vollständige Projekt einschließlich importierter Bilder und lässt sich auf jedem Gerät mit Kritzel Studio wieder importieren.
