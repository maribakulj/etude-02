"""Seed copy relations between core programmes from Tung (for human checking).

Writes data/copy_seeds.csv: emblem (1531 id), Tung number, pair, guess, evidence sentence.
The evidence sentences quote Tung's Variorum and stay local (data/derived); the committed file
keeps only ids, pair and guess.
"""

import csv
import json

from etude02.corpus import ROOT, versions
from etude02.tung import seed

PAIRS = [("31", "34"), ("34", "51"), ("51", "21"), ("31", "21")]

ids = [json.loads(line)["id"] for line in open(ROOT / "data" / "corpus.jsonl")]
ids = [i for i in ids if i.startswith("A31b")]
out = ROOT / "data" / "derived"
out.mkdir(parents=True, exist_ok=True)
with (
    open(ROOT / "data" / "copy_seeds.csv", "w", newline="") as pub,
    open(out / "copy_seeds_evidence.csv", "w", newline="") as loc,
):
    wp, wl = csv.writer(pub), csv.writer(loc)
    wp.writerow(["emblem", "tung", "earlier", "later", "guess"])
    wl.writerow(["emblem", "tung", "earlier", "later", "guess", "evidence"])
    for e in ids:
        n = int(versions(e)["A21a"][4:])
        for a, b in PAIRS:
            s = seed(n, a, b)
            wp.writerow([e, n, a, b, s.guess])
            wl.writerow([e, n, a, b, s.guess, s.evidence])
