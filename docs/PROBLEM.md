# Research problem — v0.4 (draft, 2026-10-13)

*Through the picture or through the text? Recovering and explaining the copying history of
Alciato's emblem woodcuts with visual correspondence methods (1531–1621).*

Status: **draft, not frozen, not reviewed.** It replaces v0.3 (in git history, commit `0ce6270`),
for the reasons given in §1. State of the art for this version:
[`notes/sota_2026-10.md`](../notes/sota_2026-10.md). The v0.3 work remains usable: corpus, 20
development emblems, the corrections recorded outside the repository with Codex
(`~/etude-02-collaboration/`).

## 1. Why the problem changes

v0.3 had become a manual coding protocol: 6 to 9 human annotators, one modest descriptive
question (does 1534 render the key units of the text more often than 1531?), and a marginal
computational part. Two things were missed:

1. **The strongest material of the project is not the text–image fit but the copying history.**
   Mason Tung's *Variorum* documents, for 212 emblems in 9 illustration programmes, which cut
   follows which, in which direction, and which designs are new. Expert ground truth on
   transmission across a long series of printed editions is rare.
2. **Visual correspondence methods have changed what can be measured**:
   - near-duplicate and co-segmentation search: ArtMiner, SegSwap;
   - dense features: DINOv3, DIFT;
   - segmentation: SAM 3;
   - pose estimation on art: ViTPose trained on Human-Art.

   None of them has been tested against such a documented history.

## 2. Question

> **RQ.** Can visual correspondence methods recover a documented copying history between the
> illustration programmes of one text (same block, reversed copy, same-direction copy, free copy,
> new design)? And when a picture is redrawn, does it stay closer to the previous picture or to the
> text it illustrates?

Marcel's starting question — what a picture keeps that words lose, and the reverse — comes back in
a measurable form. The epigram is fixed across editions, so each new design can be placed between
two sources: **the previous image and the words**.

Sub-questions:

- **RQ1 — Recovery.** How well do off-the-shelf methods rank and classify the documented relations?
  Methods: global embeddings, dense correspondence with and without mirroring, co-segmentation,
  pose. Breakdown by relation type and by pair of programmes.
- **RQ2 — Mirror.** Reversed copies are frequent in this corpus. Does explicit mirror handling
  change recovery, and can the direction of a copy be inferred?
- **RQ3 — What persists.** Across a copy and across a new design, which components are kept? Figure
  poses (keypoints), main objects (segments), composition (spatial layout of matched regions),
  setting.
- **RQ4 — Picture or text.** For new designs, is the new picture closer to the previous picture or
  to the text? Two independent measures:
  - (a) visual: correspondence with the previous cut, against a baseline of unrelated cuts;
  - (b) textual: realisation of the epigram's depicted entities and relations (detection and
    segmentation by name, checked by humans on a sample), with Tung's notes on which part of the
    text a design illustrates as a reference.
- **RQ5 (descriptive, kept from v0.3).** What do catalogue verbalisations (Glasgow alt-text,
  Iconclass "image", Tung's descriptions) keep of what the pictures show?

## 3. Material

| Tung code | Programme | Glasgow witness | Status |
|---|---|---|---|
| 31 | Augsburg 1531 | A31b (A31a, A34a: same Steyner chain) | local |
| 34 | Paris 1534 | A34b | local |
| 46 | Venice, Aldus 1546 | none found | gap |
| 47 | Lyon, de Tournes 1547 (Salomon); Tung's plates come from the 1556 edition | A56a (1556) | block identity to check |
| 51 | Lyon 1551 | A51a (A50a closely similar) | A50a local; A51a to fetch |
| 67 | Frankfurt 1567 | A67a | to fetch |
| 77 | Antwerp 1577; Tung's plates come from Leiden 1591 | A91a | to fetch |
| 83 | Paris 1583 | FALc (Paris 1584)? | identity to check |
| 21 | Padua 1621 | A21a | local |

Up to 8 of Tung's 9 programmes have a Glasgow witness. Images are ≤ 500 px; Gallica scans are to
be checked where detail matters.

**Ground truth.** Tung's prose relations are extracted into a typed graph, with an evidence
sentence for each edge. A model-made first pass exists for 104 emblems and 4 programmes
(`data/copy_matrix_firstpass.csv`, 175/416 rows low confidence). Its reliability is measured
against an independent second extraction and a human check of a sample. The graph keeps
uncertainty (`unclear`) instead of forcing a class.

## 4. Claimed contribution (to be confirmed by the reading list)

1. **A benchmark**: an expert-documented, typed copying graph over up to 8 printed programmes,
   mirror relations included, with an evaluation protocol. Released as identifiers, relations and
   scripts; no Glasgow images.
2. **A measured answer** to how far current visual correspondence methods recover typed print
   transmission, mirror included. The nearest works are Kaoua et al. 2021 (manuscript illustration
   matching, no relation types, no mirror) and Chung et al. 2014 (same block vs copy, 150 pairs).
3. **A decomposition of what persists** under copying and redesign (pose, objects, layout).
4. **A first computational test** of whether redesigned illustrations follow the previous picture
   or the text.

## 5. What is not claimed

- No claim of historical transmission from similarity alone: similarity proposes, the documented
  history decides.
- No general theory of what pictures or words can express.
- Not a study of Warburg's *Pathosformel*. Pose is one component among others.

## 6. Risks and limits

- **Prior art**:
  - Aubry's group (VHS, AIKON, EIDA) works on illustration similarity in printed scientific books;
  - the Oxford "1516" follow-up to 15cILLUSTRATION;
  - still unread from v0.3: Cummings 2007, Tung 2012 and 2013 (library).
- **Ground-truth quality**: Tung's prose is not a code. Extraction error is measured, and
  low-confidence edges are excluded from headline numbers.
- **Detection bottleneck**: on Human-Art, ViTPose with detected boxes is far below ViTPose with
  ground-truth boxes (0.468 vs 0.800 AP for ViTPose-H). On small woodcuts, figure detection must be
  measured first. There is no pose benchmark for woodcuts.
- **Resolution and witnesses**: ≤ 500 px; block identity between Tung's plates and Glasgow
  witnesses (47/A56a, 83/FALc) must be checked.
- **Compute**: the Mac has 16 GB and the disk is nearly full. Small models run locally through the
  shared queue (`~/outils-seg/lourd.sh`); larger ones (DIFT, SegSwap training) on Colab.
- **RQ4 text side**: detecting the epigram's entities in a woodcut is itself error-prone. It needs
  a human-checked sample before any conclusion.

## 7. Next steps (no code until Marcel asks)

1. Review of this draft (adversarial, humanities + computer vision).
2. Library: Cummings 2007, Tung 2012 and 2013, plus the full text of AIKON (IJDAR 2026).
3. When coding is allowed:
   - fix the extraction (cahier L5, outside the repository);
   - fetch the missing witnesses (A51a, A56a, A67a, A91a);
   - extract Tung's graph;
   - run a pilot on the 20 development emblems: DINOv3 global and dense features with and
     without mirror, against Tung.
