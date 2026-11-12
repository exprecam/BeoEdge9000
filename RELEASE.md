# Publishing and releasing (maintainer notes)

## One-time setup

1. On GitHub, create an **empty** repository (no README, no licence, no .gitignore — they are already here).
   Suggested name: `beoedge9000-icue-widget`.
2. In `LICENSE`, replace `YOUR NAME` with your name (or pseudonym). Optionally set `"author"` in
   `src/manifest.json` (it is `Custom` for now) — it is shown in iCUE.
3. Push:

   ```bash
   git init
   git add -A
   git status            # check: src/libs/ and dist/ must NOT be listed
   git commit -m "Initial public release"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/beoedge9000-icue-widget.git
   git push -u origin main
   ```

4. On the repository page, **About** (gear icon):
   - Description: `Beosound 9000–inspired media widget for the Corsair XENEON EDGE (iCUE)`
   - Topics: `icue`, `xeneon-edge`, `corsair`, `widget`, `media-player`, `html-css-javascript`
5. Take a screenshot on the real XENEON EDGE, save it as `docs/screenshots/preview.png`, uncomment
   the image line at the top of both READMEs, commit and push.

## Publishing a release

1. Make sure `version` in `src/manifest.json` and the top entry of `CHANGELOG.md` match.
2. `python scripts/check.py && python scripts/build.py`
3. **Import `dist/BeoEdge9000-vX.Y.Z.icuewidget` into iCUE and test it on the device** — this is the
   exact file users will get.
4. Tag and push:

   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```

5. On GitHub: **Releases → Draft a new release**, choose the tag, paste the changelog entry as the
   description, and **attach `dist/BeoEdge9000-vX.Y.Z.icuewidget`**. (The `.icuewidget` contains
   Corsair's helper files, which is why it is built locally and not by CI.)

## Before the very first public release

- [ ] The built `.icuewidget` imports and runs on a real XENEON EDGE.
- [ ] `git status` shows no `src/libs/` and no `dist/`.
- [ ] Read the terms of the Corsair WidgetBuilder Kit you took `src/libs/` from, to confirm that
      redistributing a packaged widget is fine for you (see `THIRD_PARTY_NOTICES.md`).
- [ ] You are comfortable with the brand names shown on the widget ("BANG & OLUFSEN", "BeoEdge9000")
      and in the repository. They are used to describe the inspiration only, but rights holders can
      object to such uses. The disclaimer is in `THIRD_PARTY_NOTICES.md`.
- [ ] A screenshot is in the README.

## Next versions

Bump `version` in `src/manifest.json`, add a `CHANGELOG.md` entry, then follow
"Publishing a release". iCUE uses the manifest version to tell an update from the installed widget.
