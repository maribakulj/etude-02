"""v0.5 pilot: ancestor attribution and copy direction on the 20 development emblems.

Ground truth: annotations/pilot_v05/tung_edges_dev.csv (Tung's prose, adjudicated by the loop,
pending human check). Witnesses: 31=A31b, 34=A34b, 47=A56a, 51=A51a, 77=A91a, 21=A21a.
Methods (each scored upright and with the query mirrored):
  sift   SIFT + ratio test + RANSAC affine, number of inliers
  dglob  DINOv2-base CLS cosine (DINOv3 weights are gated)
  ddense DINOv2-base patch tokens, mutual nearest neighbours + RANSAC affine on patch centres
  style  layout-free texture statistics (gradient-orientation and intensity histograms), cosine
  prior always the chronologically nearest earlier witness (attribution only)
Output: results/pilot_v05/*.csv and a printed summary. Local images only; nothing fetched.
"""

import csv
import random

import numpy as np

from etude02.corpus import ROOT, emblem, image_path
from etude02.matching import METHODS

ORDER = ["31", "34", "47", "51", "77", "21"]
WITNESS = {"31": "A31b", "34": "A34b", "47": "A56a", "51": "A51a", "77": "A91a", "21": "A21a"}
OUT = ROOT / "results" / "pilot_v05"
GT = ROOT / "annotations" / "pilot_v05" / "tung_edges_dev.csv"


def witness_id(e31: str, prog: str) -> str | None:
    if prog == "31":
        return e31 if image_path(e31).exists() else None
    hits = [r for r in emblem(e31).related if r.startswith(WITNESS[prog])]
    return hits[0] if hits and image_path(hits[0]).exists() else None




def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(open(GT)))
    attr, dirn = [], []
    for r in rows:
        if r["dependency"] != "yes" or r["ancestor"] not in ORDER:
            continue
        e31, prog, anc = r["emblem"], r["prog"], r["ancestor"]
        q = witness_id(e31, prog)
        if q is None:
            continue
        earlier = [p for p in ORDER[: ORDER.index(prog)]]
        cands = {p: witness_id(e31, p) for p in earlier}
        cands = {p: c for p, c in cands.items() if c is not None}
        if anc not in cands:
            continue
        generic = "rest of the editions" in r["evidence"]
        rec = {"emblem": e31, "prog": prog, "query": q, "ancestor": anc, "k": len(cands),
               "generic": generic, "orientation": r["tung_orientation"]}
        for name, fn in METHODS.items():
            sc = {p: max(fn(q, c, False), fn(q, c, True)) for p, c in cands.items()}
            best = max(sc, key=sc.get)
            rank = sorted(sc, key=sc.get, reverse=True).index(anc) + 1
            rec[f"{name}_top1"] = int(best == anc)
            rec[f"{name}_rr"] = 1 / rank
        nearest = max(cands, key=ORDER.index)
        rec["prior_top1"] = int(nearest == anc)
        rec["prior_rr"] = 1 / (sorted(cands, key=ORDER.index, reverse=True).index(anc) + 1)
        attr.append(rec)
        if r["tung_orientation"] in ("reversed", "stated_same"):
            a = cands[anc]
            d = {"emblem": e31, "prog": prog, "query": q, "anc": a,
                 "truth": "reversed" if r["tung_orientation"] == "reversed" else "same"}
            for name in ("sift", "dglob", "ddense"):
                up, fl = METHODS[name](q, a, False), METHODS[name](q, a, True)
                d[f"{name}_up"], d[f"{name}_flip"] = round(up, 4), round(fl, 4)
                d[f"{name}_pred"] = "reversed" if fl > up else "same"
            dirn.append(d)
    for name, data in (("attribution", attr), ("direction", dirn)):
        with open(OUT / f"{name}.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(data[0]))
            w.writeheader()
            w.writerows(data)
    report(attr, dirn)


def boot(vals, n=2000, seed=0):
    rng = random.Random(seed)
    m = [np.mean([rng.choice(vals) for _ in vals]) for _ in range(n)]
    return np.mean(vals), np.percentile(m, 2.5), np.percentile(m, 97.5)


def report(attr, dirn):
    print(f"ATTRIBUTION: {len(attr)} queries "
          f"({sum(not a['generic'] for a in attr)} with a specifically named ancestor)")
    print(f"  chance top-1 = {np.mean([1 / a['k'] for a in attr]):.2f}")
    for subset, sel in (("all", attr), ("specific", [a for a in attr if not a["generic"]])):
        for name in ["prior", *METHODS]:
            m, lo, hi = boot([a[f"{name}_top1"] for a in sel])
            print(f"  [{subset}] {name:6s} top-1 {m:.2f} [{lo:.2f}, {hi:.2f}]  "
                  f"MRR {np.mean([a[f'{name}_rr'] for a in sel]):.2f}")
    print(f"DIRECTION: {len(dirn)} pairs "
          f"({sum(d['truth'] == 'reversed' for d in dirn)} reversed, "
          f"{sum(d['truth'] == 'same' for d in dirn)} same)")
    for name in ("sift", "dglob", "ddense"):
        rev = [d[f"{name}_pred"] == "reversed" for d in dirn if d["truth"] == "reversed"]
        same = [d[f"{name}_pred"] == "same" for d in dirn if d["truth"] == "same"]
        bal = (np.mean(rev) + np.mean(same)) / 2
        print(f"  {name:6s} balanced acc {bal:.2f}  (reversed {np.mean(rev):.2f}, "
              f"same {np.mean(same):.2f})")


if __name__ == "__main__":
    main()
