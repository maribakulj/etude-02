# Research problem — v0.2

*What the pictura is made from: sources, copying and re-verbalisation in the illustration of
Alciato's* Emblemata *(1531–1621).*

Status: v0.2, revised after review 1 ([`reviews/R1-humanities.md`](reviews/R1-humanities.md),
[`reviews/R1-dh-computing.md`](reviews/R1-dh-computing.md)); the response to each objection is in
[`reviews/R1-response.md`](reviews/R1-response.md). Sources: [`notes/literature.md`](../notes/literature.md)
(S1, sections cited in brackets), [`notes/looking/`](../notes/looking/) (S3).

## 1. Starting question and why it must be narrowed

Marcel's starting question: *what can a visual representation keep or express that verbalisation
loses, and the reverse?* In general it is a theoretical question with a long literature (Lessing,
Goodman, Barthes, Jakobson, Panofsky, Worth; formal pictorial semantics [C, D]). It becomes
empirical only where we know **what verbal material a picture was made from, what other pictures
were made from the same material, and how the picture was put back into words afterwards.**

## 2. The case, stated without the "fixed text" simplification

Alciato's epigrams are texts first, "descriptions of signifying things" [A4]; the 1531 Augsburg
pictures were added by the printer as *notulae rudiores*, rough signs of the author's intention for
the less learned (Steyner) [A4]. For the period, the pictura realises the *res picta* that the text
describes; the meaning (*animus*, Mignault) belongs to the text [B6, B10]. We therefore do **not**
measure whether woodcuts "fail" to depict conditionals or modality — no one expected them to — but
**what the picture is made from and how faithfully it realises the res picta**, the criterion the
period itself applied (Alciato's complaints of 1532 about errors; Hunger's brief of 1542) [A4].

Each illustration programme had **several possible sources**, not one fixed text:

- the epigram **as printed in that edition** (the 1531 text is corrupt and was revised in 1534; in
  our corpus 67 of 312 later/1531 epigram pairs differ by more than 10 % of tokens);
- the **lemma/motto** alone (a cutter may illustrate the title: a stock Cupid for *In statuam
  Amoris*);
- the **commentary** printed with it (1621 Padua prints Mignault, Sánchez and Pignoria [A5]);
- the **visual tradition** (stock iconography of Cupid, Occasio, Isis; Horapollo; existing blocks);
- an **earlier woodcut** (copying, reversed copying, re-cutting) [A1, B4];
- an intermediary **prose description**, documented for Paris 1542 (Hunger) [A4], not for 1531.

After the picture, the chain continues: Glasgow's cataloguers wrote an alt-text and Iconclass
notations "relating to the image" and "to the text" for every emblem in every edition [A3, E6], and
vision-language models can be asked to describe the same pictures.

## 3. Research questions

> **RQ.** For each element of the *res picta* an Alciato epigram describes, which source does each
> illustration programme follow — the text it printed, the motto, the commentary, the visual
> tradition or an earlier block — and when the pictures are put back into words, by cataloguers and
> by models, does the description follow the picture, the text, or an earlier description?

- **RQ1 — Realisation of the res picta.** For each *res picta* unit of the printed text (§5), is it
  present, absent, substituted, contradicted, or accompanied by added elements, in each programme?
  How does this differ between programmes, controlling for copying?
- **RQ2 — Sources of departures.** When a picture departs from its printed text, which alternative
  source explains it best (motto, commentary, stock iconography, earlier block, misreading,
  indeterminate)?
- **RQ3 — Beyond the res picta.** For the argumentative content of the epigram (negation,
  condition, time, speech, comparison, abstraction), which pictorial means do re-designs use when
  they render it at all (inscription, attribute, gesture, co-presence of states, scene substitution),
  and how stable are these means across independent re-designs? This is where Worth's list and
  formal pictorial semantics become testable — as a **descriptive** question, not as a hypothesis
  that the answer is "less than concrete content", which is true by construction.
- **RQ4 — Re-verbalisation.** How much of Glasgow's image-layer description is inherited from the
  record of another edition rather than written from the picture; and, on items where the picture
  demonstrably differs from the text (established blind, §6), do catalogue records and VLM
  descriptions report the picture, the text, or prior knowledge?

## 4. Gap and positioning (narrowed)

Not claimed: "the first typology" — inscriptions for personifications, attributes as condensed
narrative and stock substitution are known to emblem studies [B]. Claimed:

1. **A reliability-checked, copy-controlled coding** of res picta realisation across four
   programmes of one emblem book, with explicit source attribution for every departure. Nearest:
   Tung's *Variorum* (genealogy, ad hoc fidelity remarks, no coding) [A1]; Andenmatten 2018
   (qualitative, animal emblems) [B1]; Manning 1989 (bibliographical) [B4]. **Must be read before
   the claim is frozen:** Cummings 2007, Tung 2012/2013, Scholz 1984/1991, Manning 1989, Adams
   1990, Balavoine 1982, Klecker 2007 [I].
2. **A measured arbitration** of a disagreement in the literature: 1531 "unfaithful" (Glasgow,
   Tung) vs 1534 "as bad or worse" (Andenmatten) [A1, B1].
3. **A production-side, descriptive test of what pictures do with argumentative content** where the
   verbal source is known (Worth 1975; Greenberg; Abusch & Rooth) [D1, D6, D7].
4. **A provenance audit of a major emblem catalogue's image layer** (record inheritance across
   editions; how often image-layer notations are unsupported by the picture) — no analysis exists
   [E1, E6].
5. **A small, contamination-aware diagnostic of VLMs** on divergence items with closed probes [F1,
   F2, F10] — offered as a diagnostic and a released probe set, not a benchmark.

## 5. Units and observable relations (definitions; detailed in PROTOCOL)

- **Res picta unit**: an entity, attribute, action or spatial relation that the printed epigram (or
  motto) asserts of the depicted scene (e.g. *ass carries image of Isis*). Segmented on the Latin,
  by a written grammar (one predicate + arguments per unit), with the translation as an aid only.
- **Argumentative unit**: content the epigram asserts that is not a property of the depicted scene
  (moral, condition, negation of a belief, speech, comparison's tenor, temporal sequence).
- **Key units**: fixed *a priori* as the res picta units the motto or the final distich depends on.
- **Observable relation** per unit × picture: present / absent / substituted / contradicted /
  indeterminate (≤ 500 px; checked on Gallica scans where needed), plus **added** elements.
- **Interpretive labels** (operation, source) are coded **separately** and marked interpretive.

## 6. Design commitments (from review 1)

- **Development vs confirmation.** The 20 emblems of S3 are the development set. The coding
  scheme is frozen on them; confirmatory analyses use a fresh stratified random sample of the
  remaining 1531 emblems.
- **Copy and source matrix first.** For each emblem × programme pair: same block / reversed copy /
  free copy / independent re-design / indeterminate, from Tung's *Variorum* and inspection. Tests
  of convergence use independent re-designs, and copy relation enters models as a covariate.
- **Which 1531.** A31a (28 Feb. 1531) and A31b (6 Apr. 1531) are collated; the panel uses the
  edition whose blocks are complete, and the count of woodcuts is reconciled with Glasgow and Tung.
- **Blind image-only descriptions** of every picture in the confirmation sample are written by a
  coder who has not read the epigram, *before* text-informed coding. Divergence items are defined
  from them, not from text-informed judgement.
- **Two independent human coders** for a double-coded subset, with a Latinist for segmentation;
  machine coding, if used, is a measured condition, never a coder.
- **Each hypothesis has a named test, effect-size threshold and multiplicity correction** (below),
  with minimum detectable effects simulated from pilot rates before confirmation.

## 7. Hypotheses

Confirmatory on the 1531 panel's fresh sample; models are mixed-effects logistic regressions with
random intercepts for emblem and programme and a copy-relation covariate; Holm correction across
H1–H4; categories with fewer than 15 units are reported descriptively only.

- **H1 — 1531 is less faithful than 1534.** The probability that a key res picta unit is present
  is lower in 1531 than in 1534 (odds ratio ≤ 0.67, one-sided α = .05 after Holm), restricted to
  pairs coded as independent re-designs. *Refuted* if the odds ratio's upper 95 % bound exceeds 1;
  *inconclusive* in between. This arbitrates Glasgow/Tung vs Andenmatten.
- **H2 — Departures have identifiable non-textual sources.** Among departures from the printed text
  in all programmes, at least half are attributed by both coders to a named alternative source
  (motto, commentary, stock iconography, earlier block), with κ ≥ 0.67 on the source label.
  *Refuted* if attributable departures are < 50 % or the source label is not reliable (then RQ2 is
  reported as indeterminate).
- **H3 — Re-designs commit where the text is open, and keep what it specifies.** Across
  independent re-designs of the same emblem, a text-specified depicted property (number, posture,
  material, species, spatial relation named in the text) changes value less often than a property
  the text leaves open, *relative to the baseline rate of change of stock-convention properties*
  (frame, landscape, architecture). *Refuted* if specified and unspecified properties change at
  rates whose ratio's 95 % interval includes 1.
- **H4 — Catalogue image layers propagate across editions.** For a picture whose content differs
  from the picture of another edition (blind descriptions), the catalogue's image-layer record
  matches the *other edition's* record more often than the differences between the pictures
  warrant (string and notation-set overlap compared with a baseline of record overlap for pictures
  judged the same). *Refuted* if record overlap does not exceed the picture-similarity baseline.
  Observed already (descriptive, not a test): 51 of 312 later-edition alt-texts are identical to
  the 1531 alt-text, 9 Iconclass-image sets identical.
- **H5 — VLMs on divergence items (diagnostic).** On closed probes written from blind descriptions,
  accuracy about the picture falls when the matching epigram is added and does not fall (or falls
  less) when a mismatched epigram is added; text-only answers measure prior knowledge. Thresholds
  fixed in PROTOCOL after the pilot; reported as a diagnostic.

RQ3 (argumentative content) is descriptive: frequencies and examples of pictorial means, with
reliability, and the specific predictions of Worth, Kaup/Orenes (draw the alternative for binary
predicates) and Abusch (stative content, no implicature from absence) checked where items allow.

## 8. Scope and limits

- **Corpus**: the 1531 panel in four Latin programmes is confirmatory; the enlarged books
  (≈ 212 emblems, three programmes) and other editions are exploratory.
- **Format and workshop** (oblong 1531, square later, dense 1550) are recorded as covariates.
- **Intermediaries**: Hunger's prose brief is evidence for Paris 1542 only; for 1531 the possible
  sources are the manuscript text and lemmata (Peutinger circle) — stated, not assumed.
- **Resolution**: ≤ 500 px; Gallica scans for every divergence item and disputed case.
- **Model contamination**: Glasgow pairs these images with texts online; mitigation by mismatched
  text, text-only, perturbed images, open-weight pinned models, several prompts, deterministic
  probe scoring (PROTOCOL).
- **Sensitive content**: racialised proverbs and dated catalogue terms (A31b083) addressed
  explicitly.
- **Publication shape**: one article with three linked parts, or a humanities article (RQ1–RQ3)
  plus a DH companion (RQ4) — a decision for Marcel (JOURNAL). The protocol is modular so that
  either is possible.

## 9. Open risks to originality

Cummings 2007; Tung 2012, 2013; Scholz 1984, 1991; Manning 1989; Adams 1990, 1992; Balavoine 1982;
Klecker 2007; Oversteegen & Schilperoord 2014 and Sato et al. 2023 in full [I]. Access requested
from Marcel.
