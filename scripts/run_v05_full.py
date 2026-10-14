"""v0.5 full run: ancestor attribution and copy direction over all Tung emblems with witnesses.

Ground truth: annotations/pilot_v05/tung_edges_dev.csv (20 emblems) plus
annotations/v05_full/edges_*.csv (the other emblems), all read from Tung's prose by the loop or
its subagents (human check pending). Witnesses: 31=A31b, 34=A34b, 47=A56a, 51=A51a, 67=A67a,
77=A91a, 21=A21a, found through the related-emblem list of each A21a page.
Output: results/v05_full/{attribution,direction}.csv and a printed summary with bootstrap
intervals over emblems.
"""

import csv
import random

import numpy as np

from etude02.corpus import ROOT, available, emblem, image_path
from etude02.matching import METHODS

ORDER = ["31", "34", "47", "51", "67", "77", "21"]
WITNESS = {"31": "A31b", "34": "A34b", "47": "A56a", "51": "A51a", "67": "A67a", "77": "A91a",
           "21": "A21a"}
OUT = ROOT / "results" / "v05_full"


def witnesses(tung: int) -> dict[str, str]:
    a21 = f"A21a{tung:03d}"
    group = [a21, *emblem(a21).related]
    out = {}
    for prog, ed in WITNESS.items():
        hits = [g for g in group if g.startswith(ed) and available(g) and image_path(g).exists()]
        if hits:
            out[prog] = hits[0]
    return out


def load_edges() -> list[dict]:
    rows = []
    for r in csv.DictReader(open(ROOT / "annotations" / "pilot_v05" / "tung_edges_dev.csv")):
        r = dict(r)
        r["source"] = "dev"
        rows.append(r)
    for p in sorted((ROOT / "annotations" / "v05_full").glob("edges_*.csv")):
        for r in csv.DictReader(open(p)):
            r = dict(r)
            r["source"] = p.stem
            rows.append(r)
    return rows


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    attr, dirn, skipped = [], [], {}
    for r in load_edges():
        if r["dependency"] != "yes":
            continue
        tung, prog, anc = int(r["tung"]), r["prog"], r["ancestor"]
        why = None
        if any(k in r["flags"] for k in ("partial", "hedged")):
            why = "partial or hedged"
        elif anc not in ORDER:
            why = "ancestor outside panel"
        elif prog not in ORDER or ORDER.index(anc) >= ORDER.index(prog):
            why = "bad order"
        if why is None:
            w = witnesses(tung)
            if prog not in w:
                why = "no query witness"
            elif anc not in w:
                why = "no ancestor witness"
        if why:
            skipped[why] = skipped.get(why, 0) + 1
            continue
        q = w[prog]
        cands = {p: c for p, c in w.items() if ORDER.index(p) < ORDER.index(prog)}
        rec = {"tung": tung, "prog": prog, "query": q, "ancestor": anc, "anc_id": w[anc],
               "k": len(cands), "generic": "generic" in r["flags"],
               "orientation": r["tung_orientation"], "source": r["source"]}
        for name, fn in METHODS.items():
            sc = {p: max(fn(q, c, False), fn(q, c, True)) for p, c in cands.items()}
            ranked = sorted(sc, key=lambda p: sc[p], reverse=True)
            rec[f"{name}_top1"] = int(ranked[0] == anc)
            rec[f"{name}_rr"] = 1 / (ranked.index(anc) + 1)
        by_date = sorted(cands, key=ORDER.index, reverse=True)
        rec["prior_top1"] = int(by_date[0] == anc)
        rec["prior_rr"] = 1 / (by_date.index(anc) + 1)
        attr.append(rec)
        if r["tung_orientation"] in ("reversed", "stated_same"):
            a = w[anc]
            d = {"tung": tung, "prog": prog, "query": q, "anc": a,
                 "truth": "reversed" if r["tung_orientation"] == "reversed" else "same",
                 "implied": "implied" in r["flags"], "source": r["source"]}
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
    print("skipped dependent edges:", skipped)
    report(attr, dirn)


def cluster_boot(rows, stat, key="tung", n=2000, seed=0):
    groups: dict = {}
    for r in rows:
        groups.setdefault(r[key], []).append(r)
    keys = list(groups)
    rng = random.Random(seed)
    vals = []
    for _ in range(n):
        sample = [r for k in (rng.choice(keys) for _ in keys) for r in groups[k]]
        v = stat(sample)
        if v == v:  # not NaN
            vals.append(v)
    return stat(rows), np.percentile(vals, 2.5), np.percentile(vals, 97.5)


def top1(name):
    return lambda rows: float(np.mean([r[f"{name}_top1"] for r in rows]))


def balanced(name):
    def f(rows):
        rev = [r[f"{name}_pred"] == "reversed" for r in rows if r["truth"] == "reversed"]
        same = [r[f"{name}_pred"] == "same" for r in rows if r["truth"] == "same"]
        return (np.mean(rev) + np.mean(same)) / 2 if rev and same else float("nan")
    return f


def report(attr, dirn):
    n_emb = len({a["tung"] for a in attr})
    print(f"ATTRIBUTION: {len(attr)} queries over {n_emb} emblems; "
          f"chance top-1 = {np.mean([1 / a['k'] for a in attr]):.2f}")
    for subset, sel in (("all", attr), ("specific", [a for a in attr if not a["generic"]])):
        print(f"  [{subset}] n = {len(sel)}")
        for name in ["prior", *METHODS]:
            m, lo, hi = cluster_boot(sel, top1(name))
            print(f"    {name:6s} top-1 {m:.2f} [{lo:.2f}, {hi:.2f}]")
    for subset, sel in (("all", dirn), ("explicit only", [d for d in dirn if not d["implied"]])):
        nr = sum(d["truth"] == "reversed" for d in sel)
        print(f"DIRECTION [{subset}]: {len(sel)} pairs ({nr} reversed, {len(sel) - nr} same)")
        for name in ("sift", "dglob", "ddense"):
            m, lo, hi = cluster_boot(sel, balanced(name))
            print(f"    {name:6s} balanced acc {m:.2f} [{lo:.2f}, {hi:.2f}]")


if __name__ == "__main__":
    main()
