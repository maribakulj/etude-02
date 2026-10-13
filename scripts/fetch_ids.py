"""Fetch selected Glasgow emblem pages (and their picturae) into the local cache.

Usage: uv run python scripts/fetch_ids.py ID [ID ...]
Unlike fetch_core.py, this does not touch data/corpus.jsonl or data/ids.csv.
"""

import sys

from etude02.corpus import RAW
from etude02.glasgow import BASE, Fetcher, decode_mixed, parse_emblem

f = Fetcher(RAW)
for eid in sys.argv[1:]:
    html = decode_mixed(f.get(f"{BASE}emblem.php?id={eid}&showrel=y", f"html/{eid}.html"))
    e = parse_emblem(html, eid)
    if e.picture_url:
        f.get(e.picture_url, f"images/{eid}.jpg")
    print(eid, "picture" if e.picture_url else "no picture", flush=True)
