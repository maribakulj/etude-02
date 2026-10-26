"""Fetch the core editions from Alciato at Glasgow into data/raw and build the local corpus.

Usage: uv run python scripts/fetch_core.py [EDITION ...]
Writes data/corpus.jsonl (local, git-ignored: contains Glasgow transcriptions) and
data/ids.csv (committed: identifiers and concordance only).
"""

import csv
import json
import sys
from pathlib import Path

from etude02.glasgow import BASE, Fetcher, decode_mixed, parse_contents, parse_emblem

CORE = ["A31b", "A34b", "A50a", "A21a"]
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


def main(editions: list[str]) -> None:
    f = Fetcher(RAW)
    rows = []
    for ed in editions:
        ids = parse_contents(
            f.get(f"{BASE}contents.php?id={ed}", f"html/contents_{ed}.html").decode("latin-1")
        )
        print(ed, len(ids), "emblems", flush=True)
        for i, eid in enumerate(ids, 1):
            html = decode_mixed(f.get(f"{BASE}emblem.php?id={eid}&showrel=y", f"html/{eid}.html"))
            e = parse_emblem(html, eid)
            if e.picture_url:
                f.get(e.picture_url, f"images/{eid}.jpg")
            d = e.to_dict()
            d["position"] = i
            rows.append(d)
            if i % 20 == 0:
                print(" ", eid, flush=True)
    seen = {}
    corpus = ROOT / "data" / "corpus.jsonl"
    if corpus.exists():
        for line in corpus.read_text().splitlines():
            d = json.loads(line)
            seen[d["id"]] = d
    for d in rows:
        seen[d["id"]] = d
    corpus.write_text("".join(json.dumps(d, ensure_ascii=False) + "\n" for d in seen.values()))
    with open(ROOT / "data" / "ids.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(
            [
                "id",
                "edition",
                "position",
                "has_picture",
                "n_iconclass_image",
                "n_iconclass_text",
                "related",
            ]
        )
        for d in seen.values():
            w.writerow(
                [
                    d["id"],
                    d["edition"],
                    d["position"],
                    bool(d["picture_url"]),
                    len(d["iconclass_image"]),
                    len(d["iconclass_text"]),
                    " ".join(d["related"]),
                ]
            )
    print("done", len(seen), flush=True)


if __name__ == "__main__":
    main(sys.argv[1:] or CORE)
