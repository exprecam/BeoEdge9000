#!/usr/bin/env python3
"""Package src/ into dist/BeoEdge9000-v<version>.icuewidget (a plain zip archive).

Usage:  python scripts/build.py

Needs the four Corsair helper files in src/libs/ (see THIRD_PARTY_NOTICES.md).
Only the Python standard library is used.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"

REQUIRED_LIBS = [
    "libs/IcueWidgetApiWrapper.js",
    "libs/SimpleMediaApiWrapper.js",
    "libs/MediaViewer.js",
    "libs/MediaViewer.css",
]
IGNORED = {".DS_Store", "Thumbs.db"}


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    try:
        manifest = json.loads((SRC / "manifest.json").read_text(encoding="utf-8"))
        json.loads((SRC / "translation.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"manifest.json / translation.json is missing or invalid: {exc}")

    missing = [lib for lib in REQUIRED_LIBS if not (SRC / lib).is_file()]
    if missing:
        fail(
            "missing Corsair helper files in src/: "
            + ", ".join(missing)
            + "\n       Copy them from the Corsair WidgetBuilder Kit (or from any widget"
            "\n       made with it) into src/libs/. See THIRD_PARTY_NOTICES.md."
        )

    html = (SRC / "index.html").read_text(encoding="utf-8")
    refs = set(re.findall(r'(?:src|href)="((?:libs|resources)/[^"]+)"', html))
    if manifest.get("preview_icon"):
        refs.add(manifest["preview_icon"])
    broken = sorted(r for r in refs if not (SRC / r).is_file())
    if broken:
        fail("files referenced but not found in src/: " + ", ".join(broken))

    version = manifest.get("version", "0.0.0")
    out = DIST / f"BeoEdge9000-v{version}.icuewidget"
    DIST.mkdir(exist_ok=True)

    files = sorted(p for p in SRC.rglob("*") if p.is_file() and p.name not in IGNORED)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            # Forward slashes, fixed timestamp: the archive is identical on every OS and run.
            info = zipfile.ZipInfo(path.relative_to(SRC).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())

    print(f"built {out.relative_to(ROOT)}  ({out.stat().st_size / 1024:.1f} KB, {len(files)} files)")


if __name__ == "__main__":
    main()
