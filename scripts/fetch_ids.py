"""Fetch selected Glasgow emblem pages (and their picturae) into the local cache.

Usage: uv run python scripts/fetch_ids.py ID|EDITION [...]
An argument of 4 characters (e.g. A56a) fetches the whole edition from its contents page.
Unlike fetch_core.py, this does not touch data/corpus.jsonl or data/ids.csv.
"""

import sys

from etude02.corpus import RAW
from etude02.glasgow import BASE, Fetcher, decode_mixed, parse_contents, parse_emblem

f = Fetcher(RAW)
ids = []
for arg in sys.argv[1:]:
    if len(arg) == 4:
        page = f.get(f"{BASE}contents.php?id={arg}", f"html/contents_{arg}.html")
        ids += parse_contents(page.decode("latin-1"))
    else:
        ids.append(arg)
for eid in ids:
    html = decode_mixed(f.get(f"{BASE}emblem.php?id={eid}&showrel=y", f"html/{eid}.html"))
    e = parse_emblem(html, eid)
    if e.picture_url:
        f.get(e.picture_url, f"images/{eid}.jpg")
    print(eid, "picture" if e.picture_url else "no picture", flush=True)
