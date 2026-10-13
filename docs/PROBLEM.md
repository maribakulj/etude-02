# Research problem — v0.5 (draft, 2026-10-13)

*Copied, reversed or redrawn: testing visual correspondence methods against the documented
relations between the illustrated editions of Alciato's* Emblemata *(1531–1621).*

Status: **draft, not frozen.** v0.5 answers review round 4 ([`reviews/R4-v0.4.md`](reviews/R4-v0.4.md)).
State of the art: [`notes/sota_2026-10.md`](../notes/sota_2026-10.md). Earlier versions are in git
history: v0.3 (manual coding of text–image fit), v0.4 (first visual reframing).

## 1. Why

- **The material.** Mason Tung's *Variorum* comments on the cuts of 212 emblems in 9 illustration
  programmes and says, in prose, which design follows which, in which direction, and which designs
  are new. An expert account of transmission over a long series of printed editions is rare.
- **The methods.** Recent visual correspondence methods have not been tested against such an
  account: dense features (DINOv3), co-segmentation (SegSwap), print-reuse search (VISE, used by
  Lyon16ci), unified correspondence (MATCHA).
- **What is not done yet** (state of the art):
  - typing the relation between two cuts;
  - inferring the direction of a copy (reversed or same-direction);
  - evaluating against an expert ground truth.

  Lyon16ci (Lyon illustrations 1480–1600) finds reuse of identical cuts but does none of these.
  Kaoua et al. 2021 match illustrations across manuscripts without typing. Chung et al. 2014
  separate same block from copy on ballads (150 pairs).

## 2. What Tung is, and what he is not

Tung is **not a coded stemma** (review R4):
- his vocabulary is graded and inconsistent: "follows", "in reverse", "copied", "models after",
  "same cut";
- "47/83" can mean a re-engraved, near-identical cut;
- he describes from reproductions: 1547 shown through the 1556 edition, 1577 through Leiden 1591;
- he is selective: an unstated relation is not an absent one;
- he names sources outside the 9 programmes: Wechel 1542, Lyon 1548/49, de Tournes' *Aesopi
  Phrygis Fabulae*, Reusner 1581, Gesner and Belon, Ovid.

Hence:

- **Ground truth = "relations between documented witnesses"**, not "the copying history".
- **Nodes** are dated witnesses (programme × edition held by Glasgow or Gallica). Edges whose
  witness postdates the copying event are flagged.
- **Edges** are built bottom-up from Tung's phrases. The phrase inventory is published with counts.
  A phrase is mapped to a label only where it decides it. Three separate fields:
  - `dependency`: yes / no / Tung-unspecified;
  - `orientation`: same / reversed / NA;
  - `fidelity`: close / free / NA.
- **Block identity** (same block vs recut) is decided on physical evidence, never from Tung's
  wording: cracks, frame breaks, measured size, on scans.
- **Unstated pairs are never scored as negatives.**
- Edges where Tung names an outside source are tagged; results are reported with and without them.
- **Reliability**: two independent extractions (at least one human) plus human adjudication on ≥ 100
  edges, κ per field. Headline numbers use adjudicated edges; the rest is a sensitivity analysis.
  Tung's omissions are estimated on a sample of about 50 unstated pairs checked by eye.

## 3. Questions

- **RQ1 — Ancestor attribution.** Given a cut, can methods identify its documented model among the
  earlier witnesses of the **same emblem** (chance 1/k reported)? A harder setting retrieves it from
  the whole corpus, with independent designs of the same emblem as hard negatives.
- **RQ2 — Direction.** Given a dependent pair, can methods tell a reversed copy from a
  same-direction one? Flipping the query makes retrieval mirror-invariant; it does not solve
  direction. Flip-augmented global features may fail here (cf. *Telling Left from Right*, CVPR
  2024), while asymmetric dense matching may succeed. Balanced accuracy.
- **RQ3 — What persists (a small correspondence benchmark).** On about 40 dependent pairs, scans
  annotated by hand with 5–10 corresponding points on figures and objects. Two uses:
  - measure how well dense methods follow parts through redrawing (PCK);
  - describe which parts are kept, displaced or lost.

  Copies under redrawing are a hard and unbenchmarked correspondence regime.
- **Exploratory, not part of paper A — attribution of departures.** For each element added or
  removed against the previous cut, is it licensed by:
  - the epigram printed in that edition;
  - a commentary or translation printed in that edition;
  - an outside visual source;
  - none of these?

  Coded by hand. Tung already gives cases ("21 adds the cubit-ruler mentioned in the text for the
  first time"). This replaces the false choice "previous picture or text" of v0.4. It is where
  Marcel's starting question (what pictures keep and words lose) returns, with historical sources.

Dropped from this study: catalogue verbalisations (former RQ5).

## 4. Controls and baselines

- **Leakage**:
  - witnesses that print the same blocks are merged into one node;
  - a query never retrieves its own programme;
  - a **style-only control** (a classifier that predicts the programme) is tested as a predictor of
    dependency.
- **Methods, kept to four plus controls**:
  1. SIFT/VISE + RANSAC ± flip (the Lyon16ci tool; Chung et al. 2014 features as a reference);
  2. DINOv3 global ± flip;
  3. DINOv3 dense mutual nearest neighbours ± flip;
  4. SegSwap with released weights.

  Controls: edge chamfer, CLIP, style-only, chance. Pose models only after a figure-detection check
  on woodcuts, and not in the first paper.
- **Statistics**: bootstrap over emblems (not pairs). With 100–200 pairs per label, intervals of
  about ± 7 points are expected and will be stated.

## 5. Material and witnesses

| Tung code | Glasgow witness | Status |
|---|---|---|
| 31 | A31b (A31a, A34a same chain) | local |
| 34 | A34b | local |
| 46 | — | missing |
| 47 | A56a (1556) | to fetch; block identity with Tung's plates to check |
| 51 | A51a (A50a close; 1548/49 Lyon origin to locate) | A50a local; A51a to fetch |
| 67 | A67a | to fetch |
| 77 | A91a (Tung's own source, Leiden 1591) | to fetch; needed for 21's ancestors |
| 83 | FALc (Paris 1584)? | identity to check |
| 21 | A21a | local |
| outside | Wechel 1542 (A42a/b at Glasgow), Lyon 1548/49 (A49a, FALb), Aesop editions | to fetch where held |

Images are ≤ 500 px at Glasgow; Gallica scans are needed for block identity and correspondence
annotation.

## 6. Contributions and papers

- **Paper A** (DSH, ICDAR or VISART):
  - the adjudicated typed graph of relations between witnesses, released with evidence sentences;
  - ancestor attribution and direction inference results;
  - the correspondence set for redrawn copies.
- **Paper B** (*Emblematica* or *Word & Image*), later: attribution of departures. It also uses
  machine–Tung disagreements as a check on Tung, and searches for unreported copies in the Aesop,
  Ovid and Reusner corpora.

**What humanists gain from A:**
- a systematic check of Tung, with disagreements adjudicated by hand;
- an estimate of what he omits;
- workshop practice quantified: how often copies are reversed (transfer), and what is simplified
  or dropped.

## 6b. Scale-up (planned after the pilot)

The pilot only decides whether the computational part holds. The study is meant to scale.

| Stage | Corpus | Role |
|---|---|---|
| 1. Pilot | 20 development emblems, about 60 adjudicated edges | go / no-go |
| 2. Full Alciato | 212 emblems × Tung's programmes with a Glasgow witness (about 1,500 cuts); then all 22 Glasgow editions (about 3,600 pictures) | the evaluated benchmark (paper A) |
| 3. Large unlabelled corpora | Emblematica Online (about 33,000 emblems); Lyon16ci (about 10,000 Lyon illustrations, 1480–1600); Salomon's Aesop, Ovid and Bible cuts and their European copies; Whitney 1586 (after Plantin); Gallica | **discovery**: unreported copies, reuse chains, the rate of reversed copying at scale; a human-checked sample measures precision |

Why both are needed:
- **Massive processing alone** gives similarity clusters that nobody can verify. That already
  exists (Visual Contagions, Lyon16ci search).
- **A small benchmark alone** is an analysis paper.

The contribution is the combination: a method whose behaviour is **measured against an expert
ground truth** (stage 2), applied at a scale where it **finds what experts have not recorded**
(stage 3), with the error rate carried over from stage 2.

Compute: stage 3 needs Colab or a larger machine; the Mac is enough only for stages 1–2.

## 7. Risks

- **Prior art**:
  - Lyon16ci likely covers the Lyon witnesses (47, 51). Run its demo with Alciato cuts, upright
    and mirrored, before claiming;
  - Aubry's group (VHS, AIKON);
  - still unread: Cummings 2007; Tung 1989 (*Emblematica* 4.2), 2012 and 2013; Green 1872;
    Saunders 1988; Adams, Rawles & Saunders; Sharratt 2005.
- **Labels**: if a field has fewer than about 30 adjudicated edges for a value, that value is merged
  or reported descriptively.
- **Resolution**: 500 px is enough for attribution, maybe not for block identity.
- **Compute**: DINOv3-B, CLIP and SIFT run on the Mac; SegSwap, DIFT and MATCHA run on Colab.

## 8. Minimal pilot (about 2 days, no training; needs Marcel's go-ahead to code)

1. Inventory Tung's relation phrases. Adjudicate by hand the relations of the 20 development
   emblems across 31 / 34 / 50 / 21: about 60 edges, the three fields, an evidence sentence each.
2. Within-emblem ancestor attribution and direction, with:
   - SIFT + RANSAC ± flip;
   - DINOv3 global ± flip;
   - DINOv3 dense mutual nearest neighbours ± flip;
   - the style-only control.
3. Click 5 corresponding points on 10 dependent pairs; DINOv3 PCK.

**Go / no-go.**
- If dense features do not beat SIFT-flip and the style control on attribution by more than the
  interval, the attribution framing is weak.
- If direction accuracy is near 50 % for flip-augmented features but clearly higher for asymmetric
  matching, that is the core result of paper A.
