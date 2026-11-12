#!/usr/bin/env python3
"""Sanity checks that need no Corsair files (they also run in CI).

  1. manifest.json and translation.json are valid JSON
  2. every tr('...') label used in index.html exists in every language
  3. the inline JavaScript has no syntax error (needs Node.js; skipped if absent)

Usage:  python scripts/check.py
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"
errors = []

try:
    manifest = json.loads((SRC / "manifest.json").read_text(encoding="utf-8"))
    translations = json.loads((SRC / "translation.json").read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    sys.exit(f"error: invalid JSON: {exc}")

for field in ("id", "name", "version", "supported_devices"):
    if field not in manifest:
        errors.append(f"manifest.json: missing '{field}'")

html = (SRC / "index.html").read_text(encoding="utf-8")

labels = set(re.findall(r"tr\('([^']+)'\)", html)) | set(re.findall(r'tr\("([^"]+)"\)', html))
for lang, data in translations.items():
    table = data.get("translation", {})
    absent = sorted(label for label in labels if label not in table)
    if absent:
        errors.append(f"translation.json [{lang}]: missing {absent}")

scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
node = shutil.which("node")
if not node:
    print("note: Node.js not found, JavaScript syntax check skipped")
elif not scripts:
    errors.append("index.html: no inline <script> found")
else:
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as tmp:
        tmp.write("\n".join(scripts))
    result = subprocess.run([node, "--check", tmp.name], capture_output=True, text=True)
    Path(tmp.name).unlink(missing_ok=True)
    if result.returncode != 0:
        errors.append("index.html: JavaScript syntax error\n" + result.stderr.strip())

if errors:
    print("\n".join(f"error: {e}" for e in errors), file=sys.stderr)
    sys.exit(1)
print(f"ok: {len(labels)} labels x {len(translations)} languages, manifest v{manifest['version']}")
