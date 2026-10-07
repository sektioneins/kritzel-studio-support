---
title: Hilfe und Problemlösung
description: Was die Meldungen von Kritzel Studio bedeuten, wie Speicherwarnungen funktionieren, wo Projekte liegen und wie Sie ein Problem melden.
---

## Häufige Fragen

### Ich kann nicht zeichnen. Es passiert nichts, oder es erscheint ein Hinweis.

Achten Sie auf den Hinweis am unteren Bildschirmrand. „Die aktive Ebene ist gesperrt“ oder „Die aktive Ebene ist ausgeblendet“ bedeutet, dass neue Striche keinen Platz haben: Öffnen Sie das [Ebenenfeld](layers.html) und entsperren oder einblenden Sie die hervorgehobene Ebene, oder tippen Sie eine andere Ebene an. Erscheint kein Hinweis, prüfen Sie, ob ein Finger auf „Verschieben“ statt „Zeichnen“ eingestellt ist („Fingerverhalten“ in den [Einstellungen](settings.html#eingabe)).

### Ich kann eine Auswahl nicht verschieben oder löschen.

Die Auswahl enthält gesperrte Objekte. Tippen Sie im Eigenschaftenfeld auf „Entsperren“ und versuchen Sie es dann noch einmal.

### Der Radierer entfernt den ganzen Strich. Wie radiere ich nur einen Teil?

Der Radierer arbeitet immer mit ganzen Strichen. Schneiden Sie den Strich vorher mit dem Werkzeug [Schneiden](tools.html#schneiden-k) durch und radieren Sie das überflüssige Stück, oder entfernen Sie Punkte mit dem Werkzeug [Punkte](tools.html#punkte-a).

### Wie kopiere ich Striche?

Kopieren und Einfügen von Strichen gibt es noch nicht. Sie können die Ebene duplizieren, auf der sie liegen („Ebene duplizieren“), oder das ganze Projekt („Duplizieren“ in der Galerie).

### Meine Leinwand ist gedreht, oder die Zeichnung ist aus dem Bild verschwunden.

Tippen Sie auf „Ansicht zurücksetzen“ (das Ecken-Symbol oben links) oder drücken Sie <kbd>Strg</kbd>+<kbd>0</kbd>. Ein schnelles Zusammenziehen mit fast geschlossenen Fingern tut standardmäßig dasselbe.

### Warum sieht mein SVG-Export anders aus?

SVG kann keine Pinselstrukturen und keine Bilder enthalten, und Text hängt von den Schriftarten ab, die auf dem anzeigenden Gerät installiert sind. Schalten Sie die „Vektorvorschau“ in der Symbolleiste ein, um zu sehen, wie das SVG aussehen wird, oder exportieren Sie als PDF; dort sind Schriftarten, Strukturen und Bilder eingebettet.

### Wie bringe ich meine Projekte auf ein anderes Gerät?

Exportieren Sie sie in der Galerie als `.kritzel`-Dateien und importieren Sie sie auf dem anderen Gerät mit „Importieren“. Siehe [Projekte sichern](gallery.html#projekte-sichern).

## Speicherwarnungen {#speicherwarnungen}

Große Zeichnungen mit vielen Ebenen und starkem Zoom brauchen viel Arbeitsspeicher. Auf Tablets ist die Speicherüberwachung eingeschaltet und prüft den Verbrauch alle paar Sekunden. Überschreitet er die Warnschwelle (standardmäßig 90 %), gibt Kritzel Studio Zwischenspeicher frei, die sich neu aufbauen lassen, und zeigt „Hoher Speicherverbrauch“ mit dem aktuellen Prozentwert. Bei der kritischen Schwelle (95 %) gibt die App zusätzlich Ebenenbilder frei, kürzt den Rückgängig-Verlauf auf die letzten 20 Schritte und sperrt den Import von Bildern und SVG-Dateien, bis wieder genug Speicher frei ist.

Sehen Sie diese Warnung oft, schließen Sie andere Apps, blenden Sie gerade nicht benötigte Ebenen aus oder fügen Sie Ebenen zusammen. Die Schwellen ändern Sie unter [Einstellungen › Erweitert](settings.html#erweitert).

## Meldungen beim Öffnen und Speichern

| Meldung | Bedeutung |
|---|---|
| „Zeichnung konnte nicht gespeichert werden“ | Die Änderungen ließen sich nicht schreiben, meist weil das Gerät voll ist. Schaffen Sie Platz; Kritzel Studio versucht es weiter. |
| „Projekt konnte nicht geöffnet werden“ | Die Projektdatei fehlt, ist beschädigt oder stammt aus einer neueren Version. Die Datei bleibt unverändert. Ist von einer neueren Version die Rede, aktualisieren Sie die App. |
| „Import fehlgeschlagen“ | Die `.kritzel`-Datei ist beschädigt, zu groß oder stammt aus einer neueren Version von Kritzel Studio. |
| „Einstellungen konnten nicht gelesen werden“ | Die Einstellungsdatei war beschädigt. Es gelten die Standardwerte, und die alte Datei wurde unter dem angezeigten Pfad gesichert. |
| „Einstellungen aus einer neueren Version“ | Eine neuere Version von Kritzel Studio hat die Einstellungen geschrieben. Sie bleiben unangetastet, es gelten die Standardwerte, und Änderungen werden erst nach einem Update der App gespeichert. |
| „Deine Projektliste konnte nicht gelesen werden“ | Die Projektliste wurde aus den gespeicherten Projekten neu aufgebaut. Keine Zeichnung ist verloren, aber Ordner und Papierkorb sind weg, und alle Projekte liegen auf der obersten Ebene. Die alte Liste wurde gesichert. |

## Wo Projekte gespeichert werden

Projekte liegen innerhalb der App:

| Plattform | Speicherort |
|---|---|
| iPad | Privater Speicher der App, in der Dateien-App nicht sichtbar. |
| Android | Privater Speicher der App, wird beim Deinstallieren gelöscht. |
| Mac | `~/Library/Containers/de.s1app.kritzel/Data/Documents/kritzel_projects` |
| Windows | `Dokumente\kritzel_projects` in Ihrem Benutzerordner |

„Info“ im Menü eines Projekts zeigt den genauen Speicherort. Bearbeiten Sie diese Ordner nicht von Hand; für Sicherungen und den Umzug von Projekten gibt es den `.kritzel`-Export.

## Ein Problem melden

Sie haben einen Fehler gefunden oder vermissen eine Funktion? Legen Sie bitte ein Issue auf GitHub an: [{{ site.support_url | remove: 'https://' }}]({{ site.support_url }}). Denselben Link finden Sie im Dialog „Über Kritzel Studio“ unter „Fehler melden / Funktion vorschlagen“. Hilfreich sind Angaben zu Gerät, Betriebssystem und Version von Kritzel Studio (steht im Dialog „Über Kritzel Studio“) sowie die Schritte, die zum Problem führen.

Mehr über Kritzel Studio steht auf der [Webseite]({{ site.website_url }}).
