# BeoEdge 9000 — a Beosound 9000–inspired media widget for the XENEON EDGE

[Français](README.fr.md)

A media-player widget for the Corsair **XENEON EDGE** (iCUE), drawn entirely in CSS and
inspired by the look of the Bang & Olufsen Beosound 9000 six-disc CD changer: brushed-aluminium
glass front, six disc bays, a sliding read head with a brushed-metal knob, a black glass display and
a ribbed anthracite panel.

> Independent fan project. Not affiliated with or endorsed by Bang & Olufsen or Corsair —
> see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

<!-- TODO: add a screenshot taken on your XENEON EDGE, then uncomment:
![BeoEdge 9000 on the XENEON EDGE](docs/screenshots/preview.png)
-->

## Features

- **Six disc bays.** Each new track is "loaded" into the next bay (1 → 6, then around again). Going
  back to a track already loaded just re-selects its disc, so the bays act as a short play history,
  with the album cover on each disc.
- **Sliding read head.** The knob and aluminium plate glide to the disc that is playing, shrink and
  clamp onto its hub. The playing disc keeps an amber ring and its LED lights up. With nothing
  played yet, the head waits full-size on bay 1.
- **Spinning disc with inertia.** The playing disc spins up when playback starts and winds down
  gradually on pause. Speed is adjustable (30–400 rpm).
- **Black glass display.** Disc number, scrolling title, artist, PLAY / PAUSE / STANDBY and a
  level meter.
- **Standby clock.** With no media, the display shows the time and date in amber, in your system's
  format and language.
- **Controls.** The knob toggles play/pause; touch-style previous / next keys sit in the display.
- **Three finishes** (Silver, Anthracite, Black), amber or cover-colour glow, custom background
  (colour, image or video), idle cover, 12 languages.

## Requirements

- Windows, with a **XENEON EDGE**
- **iCUE 5.44 or later** (the minimum listed in Corsair's custom-widget guide)
- The **Media** plugin (`widgetbuilder.mediadataprovider`, v1.1), which iCUE provides. Play, pause,
  next and previous need that version of the plugin.

## Install

1. Download `BeoEdge9000-vX.Y.Z.icuewidget` from the
   [Releases](../../releases) page.
2. Double-click the file, **or** open iCUE's Widgets panel, click **+** and select it.
3. Add the widget to your XENEON EDGE dashboard. It is designed for the wide format
   (about 2536×696) and scales down to other sizes.

## Settings

| Group | Setting | Values |
|-------|---------|--------|
| Media Personalization | Text Color | colour (default white) |
| | Background | colour (default `#ebeae6`) |
| | Image | background image or video |
| | Background Opacity | 0–100 % |
| | Idle Cover | image shown on disc 1 until a track is loaded |
| Appearance | Finish | Silver, Anthracite, Black |
| | Glow Color | Amber, or colour taken from the cover |
| | Disc Speed | 30–400 rpm (default 150) |
| Spectrum | Show Spectrum | on / off |
| | Spectrum Opacity | 10–100 % |

## Known limitations

- **The level meter is not an audio analysis.** iCUE does not give widgets the audio signal, so
  the bars are generated (a rhythm derived from the track name) and follow play / pause only.
- The disc spins at 150 rpm by default, slower than a real CD player, so that it stays readable
  on screen.
- The disc history lives in memory: it resets when the widget reloads.
- Covers are cropped to a circle, and the read head hides the centre of the playing disc's cover.
- The Media plugin only offers next / previous, so a disc cannot be selected directly.
- Windows only, as declared in the manifest.

## Build from source

You need Python 3. Node.js is optional (JavaScript syntax check).

```bash
python scripts/check.py   # validate JSON, translations and the inline JavaScript
python scripts/build.py   # produces dist/BeoEdge9000-vX.Y.Z.icuewidget
```

`build.py` expects four helper files from Corsair in `src/libs/`. They are copyrighted by
Corsair, so they are **not in this repository**: copy them from the Corsair WidgetBuilder Kit (or
from any widget made with it). Details in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Source layout:

```
src/index.html          the whole widget (HTML + CSS + JS)
src/manifest.json       iCUE manifest
src/translation.json    labels, 12 languages
src/resources/          preview icon
src/libs/               Corsair helper files (local only, git-ignored)
scripts/                build.py, check.py
```

All the layout is drawn on a 355 × 100 grid (`--u` in the CSS), so it keeps its proportions at
any size.

## Contributing

Issues and pull requests are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). New settings need a
translation in every language of `translation.json`; `scripts/check.py` verifies it.

## Licence

MIT for the original work in this repository — see [LICENSE](LICENSE). Corsair's helper files and
the trademarks mentioned above belong to their owners.
