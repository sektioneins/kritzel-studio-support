---
title: Help and troubleshooting
description: What Kritzel Studio's messages mean, how memory warnings work, where projects are stored and how to report a problem.
---

## Frequently asked questions

### I can't draw. Nothing happens, or a message appears.

Check the message at the bottom of the screen. 'The active layer is locked' or 'The active layer is hidden' means new strokes have nowhere to go: open the [layer panel](layers.html) and unlock or show the highlighted layer, or tap another layer. If no message appears, check whether a finger is set to pan instead of draw ('Finger behavior' in the [settings](settings.html#input)).

### I can't move or delete a selection.

The selection contains locked objects. Tap 'Unlock' in the property panel, then try again.

### The eraser removes the whole stroke. How do I erase part of it?

The eraser always works on complete strokes. Cut the stroke with the [Slice](tools.html#slice-k) tool first and erase the piece you don't need, or remove points with the [Points](tools.html#points-a) tool.

### How do I copy strokes?

There is no copy and paste for strokes yet. You can duplicate the layer they are on ('Duplicate layer') or the whole project ('Duplicate' in the gallery).

### My canvas is rotated or I've lost my drawing off screen.

Tap 'Reset view' (the corners icon at the top left) or press <kbd>Ctrl</kbd>+<kbd>0</kbd>. A quick pinch with almost closed fingers does the same by default.

### Why does my SVG export look different?

SVG cannot carry brush textures or pictures, and text depends on the fonts installed on the viewing device. Turn on 'Vector Preview' in the toolbar to see what the SVG will look like, or export as PDF, which embeds fonts, textures and pictures.

### How do I move my projects to another device?

Export them as `.kritzel` files in the gallery and import them on the other device with 'Import'. See [Backing up projects](gallery.html#backing-up-projects).

## Memory warnings

Large drawings with many layers and deep zoom need a lot of memory. On tablets the memory monitor is switched on and checks memory use every few seconds. When it crosses the warning threshold (90% by default), Kritzel Studio frees caches it can rebuild and shows 'High memory usage' with the current percentage. At the critical threshold (95%) it also frees layer images, shortens the undo history to the last 20 steps and blocks image and SVG imports until memory is available again.

If you see this warning often, close other apps, hide layers you don't need at the moment, or merge layers. The thresholds can be changed under [Settings › Advanced](settings.html#advanced).

## Messages when opening or saving

| Message | What it means |
|---|---|
| 'Couldn't save your drawing' | The changes could not be written, usually because the device is full. Free some space; Kritzel Studio keeps trying. |
| 'Couldn't open this project' | The project file is missing, damaged or was created by a newer version. The file is left untouched. Update the app if the message mentions a newer version. |
| 'Import Failed' | The `.kritzel` file is damaged, too large, or from a newer version of Kritzel Studio. |
| 'Settings couldn't be read' | The settings file was damaged. Default settings are used and the old file was kept as a backup at the path shown. |
| 'Settings from a newer version' | A newer version of Kritzel Studio wrote the settings. They are left untouched, defaults are used, and changes are not saved until you update the app. |
| 'Your project list couldn't be read' | The list of projects was rebuilt from the projects on disk. No drawing was lost, but folders and the trash are gone and all projects are at the top level. The old list was kept as a backup. |

## Where projects are stored

Projects are saved inside the app:

| Platform | Location |
|---|---|
| iPad | The app's private storage. Not visible in the Files app. |
| Android | The app's private storage. Removed when the app is uninstalled. |
| Mac | `~/Library/Containers/de.s1app.kritzel/Data/Documents/kritzel_projects` |
| Windows | `Documents\kritzel_projects` in your user folder |

'Info' in a project's menu shows the exact location. Don't edit these folders by hand; use `.kritzel` exports for backups and to move projects.

## Reporting a problem

Found a bug or missing a feature? Please open an issue on GitHub: [{{ site.support_url | remove: 'https://' }}]({{ site.support_url }}). You will find the same link under 'Report a bug / request a feature' in the About dialog. It helps if you mention your device, operating system and the version of Kritzel Studio (shown in the About dialog), and describe the steps that lead to the problem.

More about Kritzel Studio is on the [website]({{ site.website_url }}).
