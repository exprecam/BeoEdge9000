# Contributing

Thanks for your interest! Bug reports, ideas and pull requests are welcome.

## Before opening an issue

Please include: Windows version, iCUE version, XENEON EDGE widget size, the media player you were
using (Spotify, browser, ...) and what you expected versus what happened. A screenshot helps a lot.
The bug-report form asks for these.

## Working on the code

The whole widget is in `src/index.html` (HTML, CSS and JavaScript in one file, as iCUE expects).

```bash
python scripts/check.py   # must pass before a pull request
python scripts/build.py   # needs the Corsair helper files in src/libs/ (see THIRD_PARTY_NOTICES.md)
```

Then import `dist/*.icuewidget` into iCUE (double-click it) and check it on the real XENEON EDGE:
a browser preview does not behave exactly like iCUE's embedded engine.

Guidelines:

- **Never commit the Corsair files** in `src/libs/` (they are git-ignored).
- Every new user-facing label must be added to **all** languages in `src/translation.json`.
  `scripts/check.py` fails otherwise.
- Sizes in the CSS use `calc(var(--u) * N)` so the layout scales; avoid raw pixel sizes.
- Keep idle cost low: avoid work that runs every frame when nothing is moving.
- Do not add logos, images or fonts owned by Bang & Olufsen or Corsair.
- Describe what you changed and how you tested it in the pull request.

By contributing you agree that your contribution is released under the MIT licence of this project.
