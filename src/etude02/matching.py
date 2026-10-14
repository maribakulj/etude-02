"""Copy-matching methods used in the v0.5 study (each scored upright and with the query mirrored).

  sift   SIFT + ratio test + RANSAC affine, number of inliers
  dglob  DINOv2-base CLS cosine
  ddense DINOv2-base patch tokens, mutual nearest neighbours + RANSAC affine on patch centres
  style  layout-free texture statistics (control)
"""

from functools import cache

import cv2
import numpy as np
import torch
from PIL import Image, ImageOps
from transformers import AutoImageProcessor, AutoModel

from .corpus import image_path


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
