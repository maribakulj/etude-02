# Protocol — v0.3

Implements [`PROBLEM.md`](PROBLEM.md) v0.3. Coding rules: [`ANNOTATION_GUIDE.md`](ANNOTATION_GUIDE.md).
v0.3 (after review 2): panel rebuilt around independent designs (1531, 1534, de Tournes);
**human calibration gate (§G) before any freeze**; decision tables in PROBLEM §6; directional
catalogue test; VLM diagnostic moved to a separately preregistered DH companion (§8).
Nothing in the confirmation set is coded before the freeze.

## 0. Materials, programmes, copy matrix

| Programme | Glasgow id | Place, printer, date | Role |
|---|---|---|---|
| P31 | A31b (= A31a blocks) | Augsburg, Steyner, 1531 (Breu workshop) | primary |
| P34 | A34b (A34a to collate) | Paris, Wechel, 1534 | primary |
| P47 | A56a? (to check) | Lyon, de Tournes, 1547/1556 (Bernard Salomon) | primary if Glasgow's 1556 carries the 1547 cuts; else Gallica |
| P50 | A50a | Lyon, Rouille/Bonhomme, 1550 (Tung's "51" to equate) | exploratory (mostly copies) |
| P21 | A21a | Padua, Tozzi, 1621 | exploratory (≈ 76/104 copies) |

Stored locally per emblem and programme: printed motto and epigram, translation, notes, alt-text,
Iconclass image/text, pictura. Expert layer: Tung's *Variorum* (TEXT source, PICTURE source,
PICTURE variant), local only.

**1531 collation** — done (`notes/collation_1531.md`): same blocks in A31a/A31b; 97 blocks for
98 picturae. **1534 collation** (A34a vs A34b; *In astrologos* replaced) and **P50 vs Tung's 51**
to do before the freeze.

**Copy matrix.** First pass done by a model instance reading every Tung paragraph
(`data/copy_matrix_firstpass.csv`; 175/416 rows low confidence): per emblem × programme, the
**ancestor** design and relation (same block / reversed copy / free copy / independent /
reused other emblem / unclear). To be checked by two humans on the contact sheets, blind to each
other; α reported; disagreements resolved and logged → `data/copy_matrix.csv`. The relation enters
models as a property of each picture (its ancestor relation), not of a pair.

## 1. Sets

- **Development set**: the 20 emblems of S3. Used for the guide, the calibration round (§G) and
  merge/drop decisions. Never in confirmatory tests.
- **Confirmation set**: the other 84 emblems of the 1531 panel (78 with a P31 woodcut) in P31,
  P34, P47. Missing pictures (6 without a 1531 cut) are excluded from H1/H2 and counted;
  `indeterminate` codes excluded with a sensitivity analysis treating them as absent.
- **Double-coded subset**: 30 confirmation emblems, random with a fixed seed (20261005).

## G. Calibration gate (before the freeze) — requires humans

1. Two describers (Stage A), two segmenters (Stage B, one a Latinist), two coders (Stages C–D)
   work independently on the development set (20 emblems × 3 primary programmes).
2. Each task is timed; α with bootstrap 95 % CIs per code family.
3. Codes below threshold (α < 0.67; < 0.80 for codes entering H1–H4) are merged or dropped
   **here**, never on the confirmation set.
4. The checked copy matrix and these real rates feed the power simulation (§9).
5. Only then: freeze, tag, deposit on OSF or Zenodo (mandatory), and code the confirmation set.

If the people cannot be found, the study is re-scoped to what one coder plus a Latinist can do
(descriptive RQ1–RQ4 with single-coder caveats), and the reliability claims are dropped.

## 2. Stages and who does them

Order matters: blind descriptions come before anyone codes a picture against its text.

| Stage | Task | Coder(s) | Blind to |
|---|---|---|---|
| A | **Blind inventory** of each picture (entities, attributes, pose, actions, relations, inscriptions, setting, indeterminate zones) | Three describer batches, **one variant per emblem each** (Latin square over the primary programmes), mixed with unrelated pictures; humans who do not know Alciato; double-described subset | epigram, motto, translation, Glasgow record, Tung, other variants |
| B | **Segmentation** of each printed epigram + motto into res picta and argumentative units; key units | two independent segmenters (one Latinist) on the double-coded subset; the key-unit setter is not the Stage C coder for that emblem | pictures |
| C | **Relation coding** unit × picture: present / partial / absent / substituted / contradicted / indeterminate; **carries the point** per design; **added** elements (from A's inventory); **slots** (count, pose, orientation, material cue, held attribute) per matched entity | Human A; human B on subset | — |
| D | **Interpretive labels**: source of each departure (RQ2); pictorial means for argumentative units (RQ3) | Human A; human B on subset | — |
| E | **Catalogue audit** (RQ4): record inheritance + support of image-layer notations | scripts + human A | — |
| F | **VLM diagnostic** (H5) | scripts; human validation of scoring | — |

Machine coding (an LLM applying the guide) may be run **as a separate measured condition** and
compared with humans; it never replaces a coder and never resolves a disagreement.

**Stage A staffing.** The pilot showed that a describer who sees several variants of one subject
recognises it and lets recognition shape the description. Three describers (or three sessions
separated by unrelated material) are therefore needed for Stage A; each describes ≈ 84 pictures.

**Workload estimate (to be replaced by calibration timings).** Confirmation set ≈ 84 emblems × 3
primary programmes ≈ 250 pictures.
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
  salient added element: `printed text (other passage)` / `Greek source text` / `motto` / `commentary` (only for
  designs that post-date it) / `antique artwork or coin type` / `visual tradition` (name it) /
  `earlier block` / `another emblem's block` / `printer/format` / `misreading` / `medium
  constraint` / `indeterminate`. **Base rate (H3):** the same procedure is applied to sham pairs
  (a departure presented with another emblem's candidate sources), coders blind to which is sham. Evidence required: a reference (Tung, a stock image, the
  commentary passage).
- **Pictorial means** (RQ3) for each argumentative unit rendered at all: `inscription` /
  `attribute` / `gesture or deixis` / `co-presence of contrasting states` / `scene of the
  comparison's vehicle` / `depiction of the contrary` / `act performed (mood shift)` / `other`.

## 7. Stage E — catalogue audit (DH companion, H5)

1. **Support coding**: each Iconclass-image notation of each picture coded supported /
   unsupported / indeterminate against that picture's blind inventory.
2. **Directional test**: within an emblem, a notation unsupported by picture X but supported by
   picture Y (and present in Y's record) counts as evidence of Y→X propagation; the asymmetry
   between directions estimates the cataloguing order. Logistic GLMM with emblem random effect;
   main test on pairs whose pictures differ (independent designs).
3. Descriptive: identical / near-identical alt-texts and notation sets between programmes
   (51/312 alt-texts identical to 1531 already observed).

## 8. Stage F — VLM diagnostic (DH companion, H6; preregistered separately)

- **Divergence items** from Stage C (resting on blind inventories); probes written **from blind
  inventories only** (the pilot's Tung-based probes are discarded).
- **Probe form**: positive contrastive pairs or two-choice questions (*"Is there a sceptre or a
  crown?"*), not negated twins (negation is itself a known model weakness); answer set
  `A / B / cannot tell`; picture-consistent and text-consistent options balanced across positions.
- **Conditions**: (1) image; (2) image + motto; (3) image + epigram; (4) image + mismatched
  epigram matched for length and checked for shared motifs; (5) epigram only, asked as "Based on
  this text, would the picture show A or B?" and scored apart; (6) image mirrored + epigram;
  (7) **recognition control**: non-Alciato woodcuts of the same subjects (e.g. Aesop editions),
  image only.
- **Models**: ≥ 2 open-weight 7–8 B models at 4-bit, run sequentially through `lourd.sh`, pinned by
  weight digest, quantisation and runtime version; API models optional, with id and date.
  Temperature 0; 3 prompt templates.
- **Primary contrast**: text-consistent answers, condition 3 vs 4; probes nested in items;
  logistic GLMM (item random effect) or a permutation test over items; smallest effect of interest
  10 percentage points.

## 9. Analysis plan

Decision tables in PROBLEM §6 (H1–H4). Programme fixed; random intercepts for emblem and, where
Stage A enters, describer; ancestor relation as covariate; R `lme4::glmer` from a notebook
(sensitivity: GEE with emblem clusters). Holm across H1–H4. Primary 1531/1534 comparisons on units
present in both printed texts; edition-specific units as sensitivity. Power: simulation with the
calibration round's rates, the checked copy matrix's structure and the actual cluster sizes; a
hypothesis below 80 % power at its support threshold is declared descriptive before coding the
confirmation set. RQ4 descriptive; categories < 15 units reported as counts and examples.

## 10. Preregistration and release

After S7–S8, the frozen PROTOCOL, ANNOTATION_GUIDE, probes and analysis notebooks (on simulated
data) are tagged in git (`protocol-v1.0`) and **deposited on OSF or as a timestamped Zenodo release
(mandatory)** before the confirmation set is coded. The DH companion (§7–8) has its own deposit. Released: scripts, identifiers, copy matrix, our annotations, probes,
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
