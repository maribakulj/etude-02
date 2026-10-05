# Research problem — v0.1

*What the woodcut cannot say: text-to-image translation in Alciato's* Emblemata *(1531–1621),
and what cataloguers and machines do with it.*

Status: draft for review 1 (S5). Sources: [`notes/literature.md`](../notes/literature.md) (S1),
[`notes/looking/`](../notes/looking/) (S3). Keys in brackets refer to sections of the literature
notes (e.g. [D1]).

## 1. Starting question and why it must be narrowed

Marcel's starting question: *what can a visual representation keep or express that verbalisation
loses, and the reverse?* Asked in general it has a long theoretical literature — Lessing [C1],
Goodman [C2], Barthes [C3], Jakobson [C4], Panofsky [C5], Worth [D1], formal pictorial semantics
[D6–D9] — and no way to settle it empirically, because in ordinary material we never know the
verbal content a picture was made from, nor what other pictures could have been made from the same
words.

## 2. The case that makes it answerable

Alciato's epigrams were written first as texts, "descriptions of signifying things" [A4]. Pictures
were added by the printer in 1531 as "rough little signs of the author's intention" (Steyner) and
redrawn by successive illustrators, sometimes from a prose paraphrase made "for an unlettered
painter" (Hunger 1542) [A4]. Alciato at Glasgow gives, for each emblem and edition, the Latin text,
an English translation, the woodcut, a short descriptive alt-text and Iconclass notations split into
"relating to the image" and "relating to the text" [A3, E6]. We have fetched four complete
illustration programmes for the 104 emblems of 1531 (Augsburg 1531, Paris 1534, Lyon 1550,
Padua 1621; 98 emblems with a 1531 woodcut, all 104 present in the three later editions).

This gives three properties that no other material offers together:

1. **The verbal source of each picture is known** (the epigram, fixed across editions apart from
   small revisions).
2. **The same text was rendered by several illustrators**, so each text has a small set of
   independent-or-documented-as-copied pictures: a natural replication.
3. **The chain continues after the picture**: modern cataloguers verbalised the picture again
   (alt-text, Iconclass "image"), with the text in view [E1], and vision-language models can be
   asked to do so with or without the text [F1, F10].

## 3. Research question (sharpened)

> **RQ.** When a fixed text is turned into pictures by several illustrators, which kinds of content
> survive, by which operations, and how consistently; and when those pictures are verbalised again
> — by cataloguers and by vision-language models — is the recovered content read from the picture
> or imported from the text?

Sub-questions:

- **RQ1 (losses and operations).** For each category of textual content (object, action, property,
  spatial relation, number, identity/proper name, negation, condition, tense/aspect, modality,
  speech/address, comparison/analogy, abstraction, colour and other medium-bound properties), how
  often is it rendered, and by which operation (§5)?
- **RQ2 (commitments).** What does each picture fix that the text left open (number, posture,
  setting, gender, material, species…), and do the dimensions that vary across illustrators of the
  same text coincide with what the text leaves open?
- **RQ3 (drift).** Across 1531 → 1534 → 1550 → 1621, does fidelity to the text's key configuration
  increase, and does it do so through new interpretation or through copying?
- **RQ4 (re-verbalisation).** On items where picture and text disagree, do the catalogue's image
  layer and VLM descriptions report what the picture shows or what the text says, and how does
  this change when the model is given the motto or the epigram?

## 4. Gap and nearest prior work

As far as open sources show [H]:

- **No reliability-checked typology** of how Alciato's woodcuts render (or fail to render) the
  epigrams. Nearest: Tung's *Variorum* — per-emblem genealogy of pictorial variants, about a dozen
  ad hoc fidelity remarks in 212 commentaries, no categories [A1]; Andenmatten 2018 — qualitative,
  75 animal emblems [B1]; Ureña Bracero 2001 — scattered observations [B2]; Manning 1989 —
  bibliographical [B4]. **Unread and highest risk: Cummings 2007, "Alciato's Illustrated Epigrams"**
  [B5, I].
- **No test of Worth's list** ("pictures cannot depict conditionals, counterfactuals, negatives, or
  past-future tenses… nor ask questions") on a corpus where each picture's verbal source is known
  [D1]. Experimental work on visual negation uses ads, photos and manga with no source text
  [D2–D5]; comprehension studies (Kaup, Orenes) concern readers, not makers [D12].
- **No analysis of the image/text split** in emblem cataloguing, although Brandhorst states that
  the text "quite literally tells us what we are looking at" [E1].
- **No controlled VLM study on emblems** (image only / + motto / + epigram, against human
  judgement). Nearest: Brandhorst 2025, ~11 emblems, one model, no conditions [F1]; Thomas 2025,
  crop vs full page on Bible woodcuts with caption-derived ground truth [F10]. VLM negation
  benchmarks test negation in the query, not negation depicted [F2, F12].

## 5. What the first twenty emblems already show (design evidence, not results)

From [`notes/looking/SYNTHESIS.md`](../notes/looking/SYNTHESIS.md): content the picture cannot
state is not simply dropped; it is **converted** by recurrent operations — omission; depicting the
comparison's vehicle and dropping its tenor; showing two contrasting states side by side
(force + persistence, dead + living); contrast of two terms plus deixis; an attribute that
condenses a narrative; naming by inscription or attribute; turning an imperative into the act
performed; depicting the very content the text denies; particularising or generalising beyond the
text. The 1531 woodcuts depart from the text's key configuration in at least 7 of 19 cases; later
editions often converge towards the text and its sources but can lose a text-relevant distinction.
The catalogue's image layer sometimes follows the text against the woodcut (A31b036, A31b083,
A31b003) and sometimes the woodcut against the text (A31b053).

## 6. Hypotheses (each with what would refute it)

Hypotheses are stated at the level of the 1531 panel (104 emblems × 4 programmes). Confirmatory
tests are fixed in the protocol (S6) before full annotation; everything else is exploratory.

- **H1 — Conversion, not a wall.** Content in Worth's categories (negation, condition,
  tense/aspect, modality, question) is rendered directly less often than concrete content of the
  same emblems, but is converted by a small set of operations whose choice depends on the category.
  *Refuted if* (a) the direct-rendering rate of Worth categories is not lower than that of concrete
  content within emblems, or (b) operation type is independent of content category, or (c) the
  operation codes cannot be applied reliably (agreement below the threshold set in S6).
- **H2 — Pictures over-specify where texts are open** (Greenberg's target/over-specificity [D6];
  Abusch & Rooth's compatibility, not entailment [D7]). Across illustrators of the same emblem,
  depicted dimensions the text leaves open vary more than dimensions the text specifies.
  *Refuted if* text-specified dimensions vary as often as unspecified ones.
- **H3 — Convergence over time.** Fidelity to the text's key configuration is lowest in 1531 and
  higher in later programmes, and the gain is not explained by copying alone. This arbitrates
  between Glasgow/Tung ("1531 unfaithful") and Andenmatten ("1534 as bad or worse") [A1, B1].
  *Refuted if* 1534 fidelity is not higher than 1531 on paired emblems, or if all gains sit in
  emblems whose later cuts copy an earlier faithful one.
- **H4 — Re-verbalisers read the text.** On *divergence items* (picture and text disagree), the
  catalogue's image layer and VLM descriptions report the text's content more often than the
  picture's; for VLMs the rate rises from image-only to + motto to + epigram, and negated content
  in the text tends to be reported as depicted (affirmation bias [F2]; Brandhorst's *Ne quid
  nimis* [F1]). *Refuted if* on divergence items the picture's content is reported at least as
  often as the text's, or if adding the text does not increase text-content reports.
- **H5 (exploratory) — Draw the alternative.** For negated binary predicates illustrators depict
  the contrary state more often than for multi-valued predicates (Kaup, Orenes [D12]; Schier via
  Grzankowski [D11]). Likely too few items for a confirmatory test.

## 7. Claimed contributions

- **Emblem studies / art history.** The first systematic, reliability-checked account of how one
  emblem book's texts were rendered by four illustration programmes: what each programme does with
  undepictable content, how often it departs from the text, and whether later programmes correct
  or copy. It turns scattered remarks (Tung, Andenmatten, Ureña) into a measured description and
  settles a disagreement in the literature (H3).
- **Semiotics / philosophy of depiction.** The first production-side test of Worth's list and of
  formal pictorial semantics' predictions (over-specification, compatibility, iconic content
  projecting out of logical operators [D6–D9]) on historical material where the source text is
  known; and a typology of conversion operations that extends Worth's list (speech, identity,
  analogy, medium-bound properties).
- **Information science / computing.** A measure of how far catalogue "image" descriptions depend
  on the text; a controlled evaluation of VLMs with divergence probes that separates reading the
  picture from importing the text; and a released resource (identifiers, our annotations, scripts,
  notebooks) usable as a benchmark of "what the picture shows vs what the text says".

The three parts share **one coding scheme** applied to the text, the woodcut, the catalogue record
and the model output — the measurement that no prior work provides [H6].

## 8. Scope and limits (stated now)

- **Corpus**: the 104 emblems of 1531 in four Latin programmes is the confirmatory panel; the 1534
  additions and the 1550/1621 enlarged books (≈ 212 emblems, three programmes) are exploratory.
- **Independence**: programmes are not independent where blocks were copied; copy relations are
  coded from Tung's *Variorum* and by inspection, and analyses are run with and without copies.
- **Language**: the epigrams are Latin; Glasgow's English translations (declared non-authoritative)
  are a working aid. Content units are segmented on the Latin with the translation alongside; a
  Latinist check of a sample is needed.
- **Intermediaries**: illustrators may have worked from a paraphrase, not the Latin [A4]; a
  "loss" may have happened before the woodcut. The article states this as a limit on causal claims
  about individual illustrators.
- **Image quality**: picturae are ≤ 500 px; fine details (hatching for skin colour or material)
  may need Gallica's higher-resolution scans for disputed cases.
- **Model contamination**: Alciato's emblems and Glasgow's pages are online; a model may recognise
  the emblem and recall its text. Divergence items and an explicit recognition check are the
  safeguards (S6).
- **Sensitive content**: some emblems rest on racialised proverbs (A31b083) and the catalogue uses
  dated terms; the article addresses this explicitly.
- **Not claimed**: anything about emblem books in general, about readers' reception, or about
  pictures in general beyond this corpus.

## 9. Open risks to originality

Cummings 2007; Tung 2012 and 2013; Adams 1990 and 1992; Manning 1989; Scholz 1984; Oversteegen &
Schilperoord 2014 and Sato et al. 2023 in full [I]. Access requested from Marcel (JOURNAL,
"Questions for Marcel").
