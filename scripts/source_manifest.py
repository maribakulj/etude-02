"""Inventory cached source files without publishing their contents.

Usage: uv run python scripts/source_manifest.py
Writes data/source_manifest.csv with paths relative to data/raw, sizes and SHA-256 hashes.
"""

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "source_manifest.csv"


def main() -> None:
    if not RAW.is_dir():
        raise SystemExit("No data/raw cache found; fetch the source editions first.")
    files = sorted(p for p in RAW.rglob("*") if p.is_file() and not p.is_symlink())
    if not files:
        raise SystemExit("The data/raw cache is empty; the existing manifest was not changed.")
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["path", "bytes", "sha256"])
        for path in files:
            with path.open("rb") as source:
                digest = hashlib.file_digest(source, "sha256").hexdigest()
            writer.writerow([path.relative_to(RAW).as_posix(), path.stat().st_size, digest])
    print(f"Inventoried {len(files)} source files in {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
