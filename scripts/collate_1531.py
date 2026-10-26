"""Collate the two Steyner 1531 editions (A31a, 28 Feb.; A31b, 6 Apr.): woodcut and text.

Writes data/derived/collation_1531.csv (local) and prints a summary. Woodcut identity is judged by
a difference hash on the pictura (small, robust to scanning); text by normalised token similarity.
"""

import csv
import difflib
import re
from collections import Counter

from PIL import Image

from etude02.corpus import ROOT, available, emblem, image_path


def dhash(path, size=16):
    im = Image.open(path).convert("L").resize((size + 1, size))
    px = list(im.get_flattened_data())
    w = size + 1
    return [px[r * w + c] > px[r * w + c + 1] for r in range(size) for c in range(size)]


def norm(t):
    t = t.lower().replace("v", "u").replace("j", "i")
    return re.sub(r"[^a-z ]", " ", t).split()


rows = []
for i in range(1, 105):
    a, b = f"A31a{i:03d}", f"A31b{i:03d}"
    if not (available(a) and available(b)):
        rows.append([a, b, "missing page", "", ""])
        continue
    ea, eb = emblem(a), emblem(b)
    ia, ib = image_path(a), image_path(b)
    if ia.exists() and ib.exists():
        ha, hb = dhash(ia), dhash(ib)
        dist = sum(x != y for x, y in zip(ha, hb, strict=True))
        pic = "same block" if dist <= 40 else f"different? (dhash {dist})"
    else:
        has = {True: "yes", False: "no"}
        pic = f"picture: A31a {has[ia.exists()]}, A31b {has[ib.exists()]}"
    sim = difflib.SequenceMatcher(None, norm(ea.epigram), norm(eb.epigram), autojunk=False).ratio()
    same_motto = norm(ea.motto) == norm(eb.motto)
    rows.append([a, b, pic, f"{sim:.3f}", same_motto])

out = ROOT / "data" / "derived" / "collation_1531.csv"
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["A31a", "A31b", "woodcut", "epigram_similarity", "same_motto"])
    w.writerows(rows)
print(Counter(r[2].split(" (")[0] for r in rows))
print("epigram sim < 0.98:", [(r[1], r[3]) for r in rows if r[3] and float(r[3]) < 0.98])
print("motto differs:", [r[1] for r in rows if r[4] is False])
