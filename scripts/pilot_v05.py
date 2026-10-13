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
from functools import cache

import cv2
import numpy as np
import torch
from PIL import Image, ImageOps
from transformers import AutoImageProcessor, AutoModel

from etude02.corpus import ROOT, emblem, image_path

ORDER = ["31", "34", "47", "51", "77", "21"]
WITNESS = {"31": "A31b", "34": "A34b", "47": "A56a", "51": "A51a", "77": "A91a", "21": "A21a"}
OUT = ROOT / "results" / "pilot_v05"
GT = ROOT / "annotations" / "pilot_v05" / "tung_edges_dev.csv"


def witness_id(e31: str, prog: str) -> str | None:
    if prog == "31":
        return e31 if image_path(e31).exists() else None
    hits = [r for r in emblem(e31).related if r.startswith(WITNESS[prog])]
    return hits[0] if hits and image_path(hits[0]).exists() else None


@cache
def gray(eid: str, flip: bool = False) -> np.ndarray:
    im = Image.open(image_path(eid)).convert("L")
    if flip:
        im = ImageOps.mirror(im)
    return np.asarray(im)


# --- SIFT + RANSAC -------------------------------------------------------------------------
_sift = cv2.SIFT_create(nfeatures=4000)


@cache
def sift_feats(eid: str, flip: bool):
    return _sift.detectAndCompute(gray(eid, flip), None)


def sift_score(q: str, a: str, flip: bool) -> float:
    kq, dq = sift_feats(q, flip)
    ka, da = sift_feats(a, False)
    if dq is None or da is None or len(kq) < 3 or len(ka) < 3:
        return 0.0
    pairs = cv2.BFMatcher().knnMatch(dq, da, k=2)
    good = [m for m, n in (p for p in pairs if len(p) == 2) if m.distance < 0.8 * n.distance]
    if len(good) < 4:
        return float(len(good))
    src = np.float32([kq[m.queryIdx].pt for m in good])
    dst = np.float32([ka[m.trainIdx].pt for m in good])
    _, inl = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=8.0)
    return float(inl.sum()) if inl is not None else 0.0


# --- DINOv2 --------------------------------------------------------------------------------
_proc = AutoImageProcessor.from_pretrained("facebook/dinov2-base")
_model = AutoModel.from_pretrained("facebook/dinov2-base").eval()
SIDE = 448  # 32 x 32 patches of 14 px


@cache
def dino(eid: str, flip: bool):
    im = Image.open(image_path(eid)).convert("RGB").resize((SIDE, SIDE))
    if flip:
        im = ImageOps.mirror(im)
    x = _proc(images=im, return_tensors="pt", do_resize=False, do_center_crop=False)
    with torch.no_grad():
        h = _model(**x).last_hidden_state[0]
    cls = torch.nn.functional.normalize(h[0], dim=0).numpy()
    patches = torch.nn.functional.normalize(h[1:], dim=1).numpy()
    return cls, patches


def dglob_score(q, a, flip):
    return float(dino(q, flip)[0] @ dino(a, False)[0])


GRID = SIDE // 14
_centres = np.array([(c + 0.5, r + 0.5) for r in range(GRID) for c in range(GRID)], np.float32)


def ddense_score(q, a, flip):
    pq, pa = dino(q, flip)[1], dino(a, False)[1]
    s = pq @ pa.T
    i2j, j2i = s.argmax(1), s.argmax(0)
    mutual = np.where(j2i[i2j] == np.arange(len(i2j)))[0]
    if len(mutual) < 4:
        return float(len(mutual))
    src, dst = _centres[mutual], _centres[i2j[mutual]]
    _, inl = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=1.5)
    return float(inl.sum()) if inl is not None else 0.0


# --- style-only control --------------------------------------------------------------------
@cache
def style_vec(eid: str):
    g = gray(eid).astype(np.float32) / 255
    gx, gy = cv2.Sobel(g, cv2.CV_32F, 1, 0), cv2.Sobel(g, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)
    h1, _ = np.histogram(ang % np.pi, bins=18, range=(0, np.pi), weights=mag)
    h2, _ = np.histogram(g, bins=16, range=(0, 1))
    h3, _ = np.histogram(mag, bins=16, range=(0, 2))
    v = np.concatenate([h1 / (h1.sum() + 1e-9), h2 / h2.sum(), h3 / h3.sum()])
    return v / np.linalg.norm(v)


def style_score(q, a, flip):
    return float(style_vec(q) @ style_vec(a))  # layout-free: flip has no effect


METHODS = {"sift": sift_score, "dglob": dglob_score, "ddense": ddense_score, "style": style_score}


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
