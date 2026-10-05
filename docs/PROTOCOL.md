# Protocol — v0.1

Implements [`PROBLEM.md`](PROBLEM.md) v0.2. Coding rules are in
[`ANNOTATION_GUIDE.md`](ANNOTATION_GUIDE.md). Everything marked **[pilot]** is tested in S7 and
may change before the protocol is frozen; nothing in the confirmation set is coded before the
freeze.

## 0. Materials and editions

| Programme | Glasgow id | Place, printer, date | Role |
|---|---|---|---|
| P31 | A31b (A31a collated) | Augsburg, Steyner, 1531 | first programme |
| P34 | A34b | Paris, Wechel, 1534 | first "authorised" programme |
| P50 | A50a | Lyon, Rouille/Bonhomme, 1550 | Lyon programme (Tung codes the 1551 Lyon edition, "51"; P50 ↔ 51 identity to be checked block by block) |
| P21 | A21a | Padua, Tozzi, 1621 | late programme with commentaries |

Per emblem and programme we store (locally, `data/corpus.jsonl`, git-ignored): printed motto and
epigram (Glasgow transcription), English translation, Glasgow notes, alt-text, Iconclass "image"
and "text" notations, pictura (≤ 500 px). Committed: `data/ids.csv` (ids, concordance, counts).
Expert reference layer: Tung's *Variorum* commentaries (TEXT source, PICTURE source, PICTURE
variant paragraphs; local copy in `data/raw/tung/`, not redistributed).

### 0.1 Which 1531

A31a (28 Feb. 1531) and A31b (6 Apr. 1531) are collated woodcut by woodcut (image hash + visual
check) and text by text. Output `data/derived/collation_1531.csv`: same block / different block /
missing. The panel uses A31b unless the collation shows A31a to be more complete; the woodcut count
is reconciled with Glasgow (97) and Tung (96) and every discrepancy explained in
`notes/collation_1531.md`.

### 0.2 Copy and source matrix (before any coding of fidelity)

For each emblem and each pair of programmes (P31–P34, P34–P50, P50–P21, P31–P50, P31–P21,
P34–P21): `same block` / `reversed copy` / `free copy` (same composition, redrawn) /
`independent design` / `reused block from another emblem` / `indeterminate`.

1. **Seed** from Tung's PICTURE variant paragraphs, parsed by rules ("follows 31 in reverse" →
   reversed copy; "47/83" → same block; "reuses the cut of emblem N" → reused block; "new design" →
   independent) — script `src/etude02/tung.py`, every seed shown with its sentence.
2. **Check** by two humans on contact sheets (`scripts/contact.py`), blind to each other; κ
   reported; disagreements resolved by discussion and logged.
3. **Sources**: Tung's TEXT source (Greek Anthology etc.) and PICTURE source (Aesop, Physiologus,
   Horapollo…) are recorded as candidate sources for RQ2.

Committed: `data/copy_matrix.csv`.

## 1. Sets

- **Development set**: the 20 emblems of S3 (`notes/looking/`). Used to write and pilot the guide.
  Never used in confirmatory tests.
- **Confirmation set**: all other emblems of the 1531 panel (84 emblems; 78 with a P31 woodcut),
  in the four programmes. Using the whole remainder avoids sampling choices. Exploratory extension:
  emblems added in 1534 and later (P34/P50/P21 only).
- **Double-coded subset**: 30 emblems of the confirmation set, drawn at random with a fixed seed
  (`numpy.random.default_rng(20261005)`), stratified by whether the 1531 cut is a reused block.

## 2. Stages and who does them

Order matters: blind descriptions come before anyone codes a picture against its text.

| Stage | Task | Coder(s) | Blind to |
|---|---|---|---|
| A | **Blind inventory** of each picture (entities, attributes, actions, relations, inscriptions, setting, indeterminate zones) | Human B (has not read the emblems); second human on the double-coded subset | epigram, motto, translation, Glasgow record, Tung |
| B | **Segmentation** of each printed epigram + motto into res picta and argumentative units; key units | Latinist + human A | pictures |
| C | **Relation coding** unit × picture: present / absent / substituted / contradicted / indeterminate; **added** elements (from A's inventory) | Human A; human B on subset | — |
| D | **Interpretive labels**: source of each departure (RQ2); pictorial means for argumentative units (RQ3) | Human A; human B on subset | — |
| E | **Catalogue audit** (RQ4): record inheritance + support of image-layer notations | scripts + human A | — |
| F | **VLM diagnostic** (H5) | scripts; human validation of scoring | — |

Machine coding (an LLM applying the guide) may be run **as a separate measured condition** and
compared with humans; it never replaces a coder and never resolves a disagreement.

**Workload estimate [pilot].** Confirmation set ≈ 84 emblems × 4 programmes ≈ 330 pictures.
Stage A ≈ 5 min/picture (≈ 28 h). Stage B ≈ 15 min/emblem (≈ 21 h, Latinist + A). Stage C+D ≈
8 units × 4 pictures × 0.5 min ≈ 16 min/emblem (≈ 22 h). Double coding adds ≈ 35 %. These
figures are to be replaced by pilot timings.

## 3. Stage A — blind inventory

Viewer: the picture alone (Glasgow `pic_l` image; Gallica scan when the coder flags
"indeterminate" and a scan exists), no caption. Form: one line per item, typed
`ENTITY | ATTRIBUTE | ACTION | RELATION | INSCRIPTION | SETTING`, each with a confidence
(`clear` / `probable` / `indeterminate`). Plain English, no identification of mythological or
allegorical figures unless an attribute or inscription in the picture identifies them (say which).
Output `annotations/A_inventory/<picture_id>.tsv`.

## 4. Stage B — segmentation

On the **Latin printed in that programme** (texts differ; see PROBLEM §2), translation as an aid.
Grammar in ANNOTATION_GUIDE §2. Unitising agreement on the double-coded subset: Krippendorff's α_u
(target ≥ 0.67). Output `annotations/B_units/<emblem>_<programme>.tsv`.

## 5. Stage C — relation coding

For each res picta unit × picture: the code and a pointer to the inventory line(s) that justify it.
`added` = inventory items that match no unit (excluding setting/frame, coded separately as
stock-convention properties for H3). Reliability: Krippendorff's α (nominal) per code family;
≥ 0.80 for codes used in H1/H3/H4, ≥ 0.67 otherwise; codes below threshold are merged or dropped
**before** confirmatory analysis, and the change is logged.

## 6. Stage D — interpretive labels

- **Source of departure** (RQ2/H2), for each absent/substituted/contradicted key unit and each
  salient added element: `printed text (other passage)` / `motto` / `commentary` / `visual
  tradition` (name it) / `earlier block` / `another emblem's block` / `misreading` /
  `medium constraint` / `indeterminate`. Evidence required: a reference (Tung, a stock image, the
  commentary passage).
- **Pictorial means** (RQ3) for each argumentative unit rendered at all: `inscription` /
  `attribute` / `gesture or deixis` / `co-presence of contrasting states` / `scene of the
  comparison's vehicle` / `depiction of the contrary` / `act performed (mood shift)` / `other`.

## 7. Stage E — catalogue audit (RQ4, H4)

1. **Inheritance**: for each emblem, pairwise similarity between programmes' alt-texts
   (normalised token edit similarity) and Iconclass-image sets (Jaccard). Identical and
   near-identical (≥ 0.9) pairs counted.
2. **Picture baseline**: pairwise similarity of the blind inventories (Jaccard on normalised items)
   and the copy-matrix relation.
3. **Test (H4)**: logistic/beta regression of record similarity on picture similarity and copy
   relation; inheritance = record similarity in excess of what picture similarity predicts.
   Threshold: excess significant at α = .05 (Holm) with a median excess ≥ 0.2.
4. **Support audit** (descriptive): each Iconclass-image notation of the confirmation set checked
   against the blind inventory: supported / unsupported / indeterminate; rate per programme.
5. We will ask Alciato at Glasgow (via Marcel, if he agrees) in what order editions were
   catalogued; until then the direction of inheritance is not claimed.

## 8. Stage F — VLM diagnostic (H5)

- **Divergence items**: pictures where the blind inventory contradicts or lacks a key res picta
  unit of the printed text (from Stage C, which itself rests on Stage A).
- **Probes**: 2–4 closed questions per divergence item written from the blind inventory, answer
  set `yes / no / cannot tell` ("Is anything carried on the animal's back?", "Is the washed man
  drawn darker than the others?"). Written before any model is run; committed.
- **Conditions**: (1) image only; (2) image + motto; (3) image + epigram (Latin + translation);
  (4) image + **mismatched** epigram (another emblem's, matched for length); (5) epigram only, no
  image (prior knowledge); (6) image mirrored + epigram (perturbation).
- **Models**: at least two open-weight models with pinned checkpoints run locally (candidates:
  Qwen2.5-VL-7B-Instruct, a LLaVA-OneVision or InternVL3 of similar size, via MLX on this Mac;
  heavy runs through `~/outils-seg/lourd.sh`); optionally one API model with the date and model id
  recorded. Temperature 0; 3 paraphrased prompt templates per condition; answers parsed
  deterministically (first token among the answer set; anything else = `unparsed`, reported).
- **Measures**: accuracy against the blind inventory; **text-import rate** = answers that agree
  with the text and disagree with the picture; difference between conditions 3 and 4 (text-reading
  vs recall), condition 5 (prior). **[pilot]** thresholds fixed after S7.
- **Scoring validation**: none needed for closed answers; a human checks 10 % of `unparsed`.

## 9. Analysis plan (confirmatory)

- **H1**: logistic GLMM, outcome = key res picta unit present (vs absent/substituted/contradicted;
  `indeterminate` excluded), fixed effect programme (P31 vs P34), random intercept emblem,
  covariate copy relation (P34 copies P31 / independent); restricted analysis on independent
  designs. Tool: R `lme4::glmer` called from a notebook (fallback: Python `statsmodels` GEE with
  emblem clusters as sensitivity analysis). Decision rule as in PROBLEM §7.
- **H2**: proportion of departures with a named source agreed by both coders, Wilson 95 % CI;
  κ on source labels.
- **H3**: logistic GLMM, outcome = property changes between two independent designs of the same
  emblem; fixed effect property type (text-specified / text-open / stock convention); random
  intercept emblem. Decision on the ratio specified/open, relative to stock convention.
- **H4**: as §7.3.
- **Multiplicity**: Holm across H1–H4.
- **Power**: before confirmation, simulate minimum detectable effects from pilot rates (S7) with
  the actual cluster structure; if H1 cannot detect OR = 0.67 with 80 % power, H1 is
  re-declared descriptive **before** coding the confirmation set.
- **Descriptive**: RQ3 means by argumentative category; categories with < 15 units reported as
  counts and examples only.

## 10. Preregistration and release

After S7–S8, the frozen PROTOCOL, ANNOTATION_GUIDE, probes and analysis notebooks (on simulated
data) are tagged in git (`protocol-v1.0`) and, if Marcel agrees, deposited on OSF before the
confirmation set is coded. Released: scripts, identifiers, copy matrix, our annotations, probes,
model outputs; not released: Glasgow images and transcriptions (fetched by script).

## 11. Ethics and sensitive content

Emblems resting on racialised proverbs (e.g. *Impossibile*) and dated catalogue terms are quoted
as historical evidence with explicit framing; our own codes use neutral descriptive terms.

## 12. Threats to validity (tracked)

| Threat | Mitigation |
|---|---|
| Single looker misreads low-resolution cuts (happened: A31b036) | Stage A by humans, `indeterminate` code, Gallica scans, Tung as reference |
| Coders know Alciato well → not blind | Stage A coder chosen for not knowing the emblems; check by asking them to name the emblem after coding |
| Text variants across programmes | Code against the text each programme printed |
| Copying inflates agreement between programmes | Copy matrix; covariate; analyses on independent designs |
| Development-set circularity | Dev set excluded from tests; guide frozen before confirmation |
| Catalogue order unknown | No claim on direction of inheritance without Glasgow's answer |
| Model contamination | Conditions 4–6; open-weight pinned models |
| Translation drives segmentation | Latin-first segmentation; Latinist |
