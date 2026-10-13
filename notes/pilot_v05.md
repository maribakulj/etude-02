# Pilot v0.5 — ancestor attribution and copy direction (2026-10-13)

Script: [`scripts/pilot_v05.py`](../scripts/pilot_v05.py). Ground truth:
[`annotations/pilot_v05/tung_edges_dev.csv`](../annotations/pilot_v05/tung_edges_dev.csv).
Scores: [`results/pilot_v05/`](../results/pilot_v05/). 20 development emblems; witnesses
31 = A31b, 34 = A34b, 47 = A56a (Tung's own source for "47"), 51 = A51a, 77 = A91a (Tung's own
source for "77"), 21 = A21a. The three missing witnesses were fetched for these 20 emblems only
(60 pages, `scripts/fetch_ids.py`).

## Ground truth (pilot quality)

100 edges (20 emblems × 5 programmes), each read from Tung's prose with its evidence phrase:
- 62 dependent;
- 26 Tung-unspecified;
- 11 not dependent (new design or reuse of another emblem's cut);
- 1 not applicable (no 1531 cut).

Orientation of the dependent edges:
- 17 "in reverse";
- 13 stated or implied same direction;
- 32 not stated.

**Caveats.**
- The adjudication was done by the loop (a model), not by a human.
- "77/21" is read as "same direction", which is implied, not stated.
- "followed in the rest of the editions" names the origin of a design, not the nearest model.
  These 18 edges are reported separately as "generic".

## Methods

Each method is scored with the query upright and mirrored.

| Method | What it computes |
|---|---|
| `sift` | SIFT keypoints + ratio test + RANSAC affine; number of inliers |
| `dglob` | DINOv2-base global token, cosine |
| `ddense` | DINOv2-base patch tokens; mutual nearest neighbours + RANSAC affine on patch positions |
| `style` | layout-free texture statistics (control) |
| `prior` | always the chronologically nearest earlier witness (control) |

DINOv2 was used because DINOv3 weights are gated on Hugging Face and need Marcel's account.

## Results

**RQ1 — ancestor attribution** (61 queries; chance top-1 = 0.41).

| Method | top-1, all 61 [95 % CI] | top-1, 43 with a named ancestor |
|---|---|---|
| prior | 0.61 [0.49, 0.72] | 0.74 [0.60, 0.86] |
| sift | 0.38 [0.26, 0.49] | 0.40 |
| dglob | 0.64 [0.51, 0.75] | 0.77 [0.63, 0.88] |
| ddense | 0.54 [0.43, 0.67] | 0.63 |
| style | 0.44 [0.33, 0.57] | 0.49 |

**RQ2 — direction** (29 dependent pairs with a stated or implied orientation: 16 reversed, 13
same). Balanced accuracy, bootstrap over emblems:

| Method | Balanced accuracy | Reversed found | Same found |
|---|---|---|---|
| sift | 0.52 [0.32, 0.71] | 0.50 | 0.54 |
| dglob | 0.61 [0.42, 0.76] | 0.38 | 0.85 |
| **ddense** | **0.84 [0.72, 0.94]** | 0.75 | 0.92 |

The 5 `ddense` errors are listed in `results/pilot_v05/direction.csv`. Looked at by eye:
- A51a153 → A91a153 (lion and hares): a method error. Tung says 77 reverses 51.
- A31b003 → A34b003 (single standing figure): hard to judge by eye at 500 px.
- A34b058 → A56a058 (pots): unclear on the image.

## Reading (go / no-go)

- **Attribution: weak, as the reviewer feared.** Global DINOv2 does no better than "take the
  nearest earlier edition" (0.77 vs 0.74, intervals overlap widely). SIFT is below chance: these
  copies are **redrawn**, not printed from the same block, so local keypoints do not match. The
  style control is near chance (good: style does not drive the result). On this corpus, attribution
  is mostly given by chronology; it can only become interesting as a hard setting (corpus-wide
  retrieval, outside sources, unstated pairs).
- **Direction: go.** Dense matching with geometric verification tells a reversed copy from a
  same-direction one in about 5 cases out of 6. Global features are biased towards "same" (they are
  close to mirror-invariant). SIFT is at chance. This is the pattern the computer-vision reviewer
  named as the core result of paper A, with *Telling Left from Right* (CVPR 2024) as the reference.
  **But n = 29**, labels adjudicated by a model, one feature extractor, 500 px images: a signal,
  not a result.

## Not done

- RQ3 correspondence clicks (5 points on 10 pairs): they need a human. A small clicking tool is
  to be written for Marcel or a helper.

## Next

1. Human check of the 100 edges, above all the 29 orientation labels: orientation is directly
   visible, so a human can verify it in a few minutes per pair.
2. Scale direction to the full 212 emblems. This needs a full fetch of A56a, A51a, A67a and A91a,
   about 20 minutes per edition at the polite rate. Expected: a few hundred dependent pairs.
3. Add DINOv3 (Marcel accepts the licence on Hugging Face) and one diffusion or MATCHA feature, on
   Colab.
4. Design the direction method properly: why does dense verification work, and where does it fail
   (symmetric scenes, single figures)?
