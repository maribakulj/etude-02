# Research problem — v0.3

*Redrawing or keeping: how Alciato's* Emblemata *were pictured, copied and re-described
(1531–1621).*

Status: v0.3, after two review rounds ([`reviews/`](reviews/)); responses in
[`reviews/R1-response.md`](reviews/R1-response.md) and [`reviews/R2-response.md`](reviews/R2-response.md).
Not frozen: the human calibration round (PROTOCOL §G) must happen first. Sources:
[`notes/literature.md`](../notes/literature.md) (sections in brackets), [`notes/looking/`](../notes/looking/),
first-pass copy matrix [`data/copy_matrix_firstpass.csv`](../data/copy_matrix_firstpass.csv).

## 1. From the starting question to a testable one

Marcel's starting question — *what can a visual representation keep or express that verbalisation
loses, and the reverse?* — becomes empirical only where we know what verbal material a picture
was made from, what other pictures were made from the same material, and how the picture was put
back into words afterwards. Alciato's *Emblemata* provide all three: texts written first, pictures
added and redrawn by successive printers, and modern catalogue descriptions of every picture.

## 2. The case

- **Texts first.** Many epigrams render Greek epigrams (Planudean Anthology), several of them
  ekphraseis of real artworks (Lysippus' *Kairos* behind *In occasionem*) [A1, A4]; the Latin was
  revised between editions (67 of 312 later/1531 pairs differ by > 10 % of tokens).
- **Pictures added and redrawn.** Augsburg 1531 (Steyner; Breu workshop) added cuts described by
  the printer as *notulae rudiores* signifying the author's *intentio* [A4]; Paris 1534 (Wechel)
  redrew or copied them; Lyon de Tournes 1547/1556 (Bernard Salomon), Lyon Rouille/Bonhomme
  1548–51, Padua 1621 (Tozzi) followed. Blocks were capital: reused (1531 *Illicitum non
  sperandum* prints the cut of *In simulachrum spei*), carried over, copied, reversed.
- **What the period asked of a picture.** Two criteria, both attested: that it show the thing the
  text describes without error (Alciato's complaints of 1532 about the 1531 cuts) and that it
  express "the sense and force of the Latin poem" (Hunger's brief, Paris 1542) [A4]. The later
  *corpus/animus* doctrine (Giovio 1555, Mignault 1577) is impresa theory and is **not** applied
  to 1531–34.
- **First-pass copy matrix (machine pre-fill from Tung, 175/416 rows low confidence; to be checked
  by a human).** For the 104 emblems of 1531: Paris 1534 redraws ≈ 48 designs independently and
  copies ≈ 42 (14 unclear); de Tournes 1547 adds ≈ 22 independent designs; Lyon 1551 and Padua
  1621 mostly copy (≈ 82 and ≈ 76 copies). **Padua 1621 is therefore not an independent
  programme**; the independent pictorial decisions are concentrated in 1531, 1534 and 1547.
- **Re-description.** Glasgow's catalogue gives, for every emblem in every edition, an alt-text and
  Iconclass notations "relating to the image" and "to the text" [A3, E6]; 51 of 312 later-edition
  alt-texts are identical to the 1531 one.

## 3. Research questions

> **RQ.** When an emblem's picture was redrawn rather than kept, what did the new design change —
> in the scene the text describes and in its point — and from which source; and how are these
> pictures put back into words by catalogues and by models?

- **RQ1 — Redraw or keep.** Which 1531 designs did Paris 1534 redraw, which did it copy, and does
  a 1531 departure from the text predict redrawing? (Same question for 1547 against its models.)
- **RQ2 — What changes.** For each key unit of the scene, is it present, partial, absent,
  substituted or contradicted in each design; and does the design **carry the point** of the
  epigram? Compared between 1531 and 1534 on all pairs, copy relation as covariate.
- **RQ3 — Sources.** Which source explains each departure or addition: the Latin printed, the
  Greek source epigram, the motto, an antique artwork or coin type, stock iconography, an earlier
  block, another emblem's block, printer/format, misreading — with a base rate (§6, H3).
- **RQ4 — Argumentative content (descriptive).** For negation, condition, time, speech,
  comparison and abstraction, which pictorial means (inscription, attribute, gesture, co-presence
  of states, vehicle scene, act performed) appear in independent designs; a production-side check
  of Worth's list and formal pictorial semantics [D1, D6, D7], without the trivial claim that such
  content is rendered less often.
- **RQ5 — Re-description (DH companion).** Catalogue record propagation between editions, and a
  contamination-aware diagnostic of vision-language models on pictures that diverge from their text.

## 4. Positioning (narrow claims)

Not claimed: the first typology of emblem illustration devices (inscriptions, attributes, stock
substitution are known [B]). Claimed, subject to reading Cummings 2007, Tung 2006/2012/2013,
Scholz 1984/1991, Andenmatten 2018 in full [I]:

1. a copy-controlled, reliability-checked account of **which designs were redrawn and why**,
   arbitrating "1531 unfaithful" (Glasgow, Tung) vs "1534 as bad or worse" (Andenmatten) [A1, B1];
2. **source attribution with a base rate**, including the Greek source texts and antique
   artworks behind the epigrams (Bässler's "reversal of ekphrasis") [A7];
3. a **production-side test** of what pictures do with argumentative content where the verbal
   source is known [D];
4. (DH companion) a **directional audit of catalogue record propagation** and a small,
   preregistered **VLM diagnostic** [E, F].

## 5. Units and codes (summary; ANNOTATION_GUIDE)

Res picta (RP) units and argumentative (AR) units segmented on the printed Latin; key units fixed
a priori from the motto or final distich; codes present / partial / absent / substituted /
contradicted / indeterminate; `carries the point` yes / no / indeterminate per design;
interpretive labels (source, pictorial means) coded separately. **Primary units for 1531–1534
comparisons are those present in both printed texts.**

## 6. Hypotheses and decision rules

All models: programme as a **fixed** effect; random intercept for emblem (and describer where
Stage A data enter); copy relation coded per picture as its **ancestor relation** (independent /
free copy / reversed copy / same block). Holm correction across H1–H4. For each hypothesis:
**support**, **refute** or **inconclusive** by interval rules fixed below; non-significance is
never refutation.

| | Hypothesis | Test | Support | Refute | Otherwise |
|---|---|---|---|---|---|
| H1 | A 1531 departure from the text predicts that 1534 redrew the design | logistic GLMM: redrawn (independent) vs copied ~ 1531 key-unit departure | OR > 1, 95 % CI above 1.5 | 95 % CI within [0.67, 1.5] (equivalence) | inconclusive |
| H2 | On all 1531/1534 pairs, key units are realised more often in 1534 | logistic GLMM: present ~ programme + ancestor relation | OR(1534 vs 1531) CI above 1.5 | CI within [0.67, 1.5] | inconclusive |
| H3 | Departures have identifiable non-textual sources more often than chance | proportion of departures attributed by both coders, vs the same procedure on **sham pairs** (a departure matched with another emblem's candidate sources) | difference > 0.2, 95 % CI above 0.1 | CI within [−0.1, 0.1] | inconclusive |
| H4 | Independent re-designs vary text-open figural slots more than text-specified slots | GLMM on slot changes between independent designs (closed slot list: count, pose, orientation, material cue, held attribute) ~ specified × slot; random emblem and slot | OR(open vs specified) CI above 1.5 | CI within [0.67, 1.5] | inconclusive |

Power is simulated (PROTOCOL §9) from the calibration round's real rates and the checked copy
matrix; any hypothesis that cannot reach 80 % power at its support threshold is declared
descriptive **before** the confirmation set is coded.

DH companion (RQ5), preregistered separately: **H5** — catalogue inheritance is directional
(an Iconclass-image notation unsupported by picture X but supported by picture Y of the same
emblem is evidence of Y→X propagation); **H6** — on divergence items, VLM answers agree with the
text more when the matching epigram is given than when a mismatched one is (primary contrast:
condition 3 vs 4; probes nested in items; logistic GLMM; smallest effect of interest: 10
percentage points).

## 7. Scope and limits

- **Panel.** Primary: 1531 (A31b, same blocks as A31a), 1534 (A34b; A34a collation pending) and
  de Tournes (Salomon) for the 104 emblems of 1531. Lyon 1550/51 and Padua 1621 are exploratory
  (copy chains). Whether Glasgow's de Tournes 1556 (A56a) carries the 1547 Salomon cuts is to be
  checked.
- **Commentary** as a source is tested only for designs that post-date the commentary.
- **Staffing.** The design needs humans (describers who do not know Alciato, a Latinist, two
  coders); the calibration round (PROTOCOL §G) times the tasks and decides what is feasible.
- **Resolution.** Gallica scans are the default for Stage A where available, Glasgow ≤ 500 px
  otherwise.
- **Close readings.** The humanities article pairs counts with close readings of exemplary cases
  (036, 006, 096, 013).
- **Publication shape.** Recommended: a humanities article (RQ1–RQ4) and a DH companion (RQ5);
  Marcel decides.
- **Sensitive content.** Racialised proverbs and dated catalogue terms handled explicitly.
