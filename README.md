# Kritzel Studio support

This repository is the public support home of **Kritzel Studio**, the vector drawing app for tablets and desktop by SektionEins GmbH.

- **Bug reports and feature requests:** please open an [issue](https://github.com/sektioneins/kritzel-studio-support/issues). Mention your device, operating system and the app version (shown under 'About Kritzel Studio').
- **User manual:** <https://sektioneins.github.io/kritzel-studio-support/>, in English and German.

## The manual

The manual is a small Jekyll site published with GitHub Pages straight from the `gh-pages` branch (Settings › Pages › Deploy from a branch › `gh-pages` / root). There is no build step to run; GitHub builds it on every push to `gh-pages`.

```
_config.yml         site settings (baseurl, support and website links, app version)
_data/nav.yml       chapter order and chapter titles in both languages
_data/i18n.yml      layout strings (Contents, Previous, Next, ...) per language
_layouts/           the page layout (sidebar, language switch, pager)
_includes/fig.html  screenshot with caption: {% include fig.html src="x.webp" alt="..." caption="..." %}
assets/             stylesheet, logo, favicon
index.html          landing page with the language choice
en/, de/            one Markdown file per chapter, same file names in both languages
en/img/, de/img/    screenshots of the English and the German app (WebP)
tools/              scripts used to produce the screenshots (not published)
```

To add a chapter, create `en/<slug>.md` and `de/<slug>.md` and add the slug to `_data/nav.yml`. The language switch links to the page with the same file name in the other language, so both languages always need the same set of files. Links to a heading in the German pages use explicit ids (`## Projekte sichern {#projekte-sichern}`), because generated ids drop umlauts.

### Writing style

English pages use British English, German pages address the reader as "Sie" and use „…“ quotes. Button and menu labels are quoted exactly as the app shows them (English labels from `lib/l10n/app_en.arb`, German ones from `app_de.arb` in the app repository). No dashes as punctuation in either language.

### Local preview

```sh
gem install --user-install jekyll webrick kramdown-parser-gfm
jekyll serve
# open http://127.0.0.1:4000/kritzel-studio-support/
```

GitHub Pages builds with Jekyll 3.10; the site only uses features that work the same in Jekyll 3 and 4.

## Screenshots

The screenshots were taken from the debug build of the app on an Android tablet (Galaxy Tab S9 FE, 2304 × 1440, landscape, dark theme) with `adb`, never on an emulator. The tools in `tools/`:

- `gen_samples.py` generates the sample drawings (landscape sketch, logo ideas, floor plan, flower doodles, notes) as project folders plus a `gallery.json`. They were copied into the debug app's storage with `adb shell run-as de.s1app.kritzel.debug` while the app was stopped.
- `shot.sh <name> [delay]` captures the device screen into `shots/<name>.png` and writes a half-size preview.
- `tap.sh x y` taps at preview coordinates; `gesture.py path x,y x,y ...` sends a multi-point touch path (for lassos and slice lines; finish with `gesture.py up x,y` or `gesture.py cancel x,y`).
- `process.sh <shots_dir> <repo_root>` crops dialogs and settings pages and converts everything to WebP into `en/img` and `de/img`. It needs Bash 4 or later and ImageMagick.

For the German set, the app language was switched to 'Deutsch' in the settings and the same screens were captured again with a `de_` prefix.
