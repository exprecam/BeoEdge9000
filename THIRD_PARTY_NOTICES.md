# Third-party notices

## Corsair iCUE widget runtime files (`src/libs/`) — not included in this repository

A widget needs four small helper files that come from Corsair's widget tooling.
Each one carries this header:

> Copyright (c) 2026, Corsair Memory, Inc. All Rights Reserved.
> This file is part of Corsair iCUE Software.

| File | Purpose |
|------|---------|
| `IcueWidgetApiWrapper.js` | Connects the page to the iCUE widget API |
| `SimpleMediaApiWrapper.js` | Reads title / artist / cover / play state from the Media plugin |
| `MediaViewer.js` / `MediaViewer.css` | Renders the user-selected background image or video |

These files are **not** covered by this project's MIT licence and are
**deliberately not committed** here (`src/libs/` is in `.gitignore`).

- To build the widget yourself, copy them into `src/libs/` from the Corsair
  WidgetBuilder Kit, or from any widget generated with it.
- The packaged `.icuewidget` attached to GitHub Releases contains them, as every
  widget produced with Corsair's tooling does. Corsair's own widget guide lists
  exporting an `.icuewidget` and sharing it directly as a way to distribute a
  widget. If you redistribute or fork this project, check the terms of the
  WidgetBuilder Kit you received them from.

## Trademarks

This is an independent fan project. It is **not affiliated with, endorsed by or
sponsored by** Bang & Olufsen or Corsair / Elgato.

*Bang & Olufsen*, *Beosound* and *BeoSound 9000* are trademarks of their
respective owners and are used here only to describe the product that inspired
the visual design. *Corsair*, *iCUE* and *XENEON* are trademarks of their
respective owners. The widget draws its own artwork with CSS; it does not use any
logo, image or font from either company.

If you are a rights holder and would like something changed or removed, please
open an issue and it will be handled promptly.
