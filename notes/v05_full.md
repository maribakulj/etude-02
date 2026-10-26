# Full run v0.5 — all 212 emblems (2026-10-14)

Script: [`scripts/run_v05_full.py`](../scripts/run_v05_full.py). Ground truth:
[`annotations/pilot_v05/tung_edges_dev.csv`](../annotations/pilot_v05/tung_edges_dev.csv) and
[`annotations/v05_full/edges_*.csv`](../annotations/v05_full/), read from Tung's prose by the loop
and three subagents (**no human check yet**). Scores: [`results/v05_full/`](../results/v05_full/).
Same methods as the pilot (`src/etude02/matching.py`): SIFT + RANSAC, DINOv2-base global, DINOv2
dense mutual-NN + RANSAC, style control; DINOv3 is still gated. Images ≤ 500 px.

Witnesses: 31 = A31b, 34 = A34b, 47 = A56a, 51 = A51a, 67 = A67a, 77 = A91a, 21 = A21a, all fetched
(833 pages for the four new editions). Available per programme: 21: 212, 51: 211, 77: 210, 67: 133,
34: 113, 47: 113, 31: 98.

Dependent edges set aside: 21 with an ancestor outside the panel, 12 partial or hedged, 1 without an
ancestor witness. Intervals: 95 % bootstrap over emblems.

## RQ1 — ancestor attribution (475 queries, 172 emblems, chance 0.40)

| method | all (475) | specifically named ancestor (407) |
|---|---|---|
| chronological prior | 0.60 [0.56, 0.64] | 0.65 [0.61, 0.69] |
| SIFT | 0.39 [0.34, 0.43] | 0.39 [0.34, 0.44] |
| DINOv2 global | **0.66 [0.61, 0.71]** | **0.70 [0.66, 0.75]** |
| DINOv2 dense | 0.64 [0.60, 0.69] | 0.68 [0.63, 0.73] |
| style control | 0.41 [0.37, 0.45] | 0.42 [0.38, 0.47] |

By programme (top-1; k = mean number of candidates):

| query | n | k | prior | global | dense |
|---|---|---|---|---|---|
| 21 | 125 | 4.5 | 0.83 | 0.80 | 0.82 |
| 34 | 32 | 1.0 | 1.00 | 1.00 | 1.00 |
| 47 | 46 | 1.9 | 0.89 | 0.83 | 0.70 |
| 51 | 78 | 2.9 | 0.62 | 0.65 | 0.51 |
| 67 | 77 | 3.6 | 0.49 | 0.39 | 0.45 |
| 77 | 117 | 4.0 | 0.18 | **0.54** | **0.54** |

- Image features beat the prior only modestly overall (+6 points, intervals overlap).
- The gain sits in **77 (Leiden 1591)**: Tung mostly derives it from 51 or 47, not from the nearest
  earlier witness 67, and the image methods find that (0.54 vs 0.18).
- Where the prior is wrong (191 queries), global features recover the ancestor 35 % of the time.
- SIFT stays at chance: the copies are redrawn, not reprinted. The style control is at chance, so
  the signal is not "same workshop look".
- The 34 queries have one candidate (k = 1) and inflate every score a little.

Verdict unchanged from the pilot: **attribution as framed is weak**; a combination of prior and
image is the obvious next test, but it should not become the headline.

## RQ2 — copy direction

| set | pairs | SIFT | DINOv2 global | DINOv2 dense |
|---|---|---|---|---|
| all | 235 (123 reversed, 112 same) | 0.53 [0.47, 0.59] | 0.63 [0.57, 0.69] | **0.84 [0.79, 0.88]** |
| explicit only | 142 (121 reversed, 21 same) | 0.51 [0.41, 0.61] | 0.63 [0.51, 0.74] | **0.82 [0.75, 0.89]** |

Balanced accuracy. Per class for dense matching: reversed found 0.73 (all) / 0.74 (explicit); same
found 0.95 / 0.90.

- **The pilot result holds at eight times the size**: 0.84 on 29 pairs became 0.84 on 235 pairs,
  with a much tighter interval. Global features stay biased towards "same" (reversed found 0.51).
- Main confound: 91 of the 112 "same" pairs are *implied* (21 copying 77, from Tung's "77/21"
  notation), all in one programme. The explicit-only set removes them but leaves only 21 "same"
  pairs, so the "same" side is still thin.
- The dense method misses about a quarter of the reversed copies. These failures are the first
  thing to look at by eye.

## What this does not show yet

- Labels are machine reads of Tung, not adjudicated. A human check of the orientation labels comes
  first (a sample of the 235 direction pairs, all of the dense method's errors).
- 500 px Glasgow images only; DINOv2, not DINOv3.
- Block identity (same block vs recut) is untouched.

## Next

1. Human check of the orientation labels (small page to prepare).
2. Look at the ~33 reversed pairs the dense method calls "same".
3. DINOv3 (licence on Hugging Face, Marcel's account) and MATCHA / DIFT on Colab.
4. Clicking tool for RQ3 correspondences.
