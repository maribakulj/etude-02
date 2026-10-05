# JOURNAL

## Résumé pour Marcel (6 octobre 2026, fin de la boucle)

**Où on en est.** La boucle s'arrête comme prévu : la problématique et le début du protocole
sont écrits (version 0.3), ont passé deux tours de relecture hostile (quatre relecteurs simulés,
deux « humanités », deux « méthodes »), et ont été testés sur 20 emblèmes. Rien de l'annotation
complète ni de l'article n'a été commencé.

**La question, telle qu'elle est devenue.** Ta question de départ (ce que l'image garde ou perd
par rapport au texte) devient : *quand un emblème d'Alciat a été redessiné plutôt que recopié,
qu'est-ce que le nouveau dessin a changé — dans la scène décrite et dans le sens — et d'où viennent
ces changements ; et comment ces images sont-elles ensuite remises en mots par les catalogues et
par les modèles d'IA ?* Le « ce qui se perd » brut a été abandonné : les relecteurs ont montré que
c'était vrai par construction et étranger à l'époque.

**Ce que le travail a établi en chemin.**
- Corpus complet en local : 640 emblèmes, 4 éditions (1531, 1534, 1550, 1621), textes, traductions,
  Iconclass, gravures ; rien de Glasgow n'est sur GitHub.
- Les deux éditions de 1531 utilisent les mêmes bois ; 98 gravures pour 97 bois (un réemploi).
- Carte des copies (première version, à vérifier) : en 1534, environ la moitié des gravures de
  1531 est redessinée, l'autre copiée ; 1550 et 1621 copient surtout. Les vrais dessinateurs
  indépendants sont 1531, 1534 et Lyon 1547 (Bernard Salomon).
- Les descriptions du catalogue de Glasgow se recopient souvent d'une édition à l'autre (51 sur
  312 identiques).
- Un essai avec un petit modèle d'IA montre que le circuit de test marche, et a révélé un biais
  (le modèle dit trop souvent « oui ») que le protocole corrige.
- J'ai fait des erreurs de lecture des gravures (l'âne de 1531 porte bien un reliquaire) : elles
  sont corrigées et ont servi à durcir le protocole.

**Ce qui ne peut pas avancer sans toi** (détails ci-dessous, « Questions for Marcel ») :
1. lire 4–5 articles payants qui pourraient déjà avoir fait ce travail (surtout Cummings 2007) ;
2. trouver des humains : 2 descripteurs qui ne connaissent pas Alciat, un latiniste, 2 codeurs,
   pour un tour d'étalonnage sur les 20 emblèmes de développement (PROTOCOL §G) — sans eux, pas de
   protocole figé ni de mesure de fiabilité ;
3. décider : un article ou deux (je recommande un article d'histoire de l'art/sémiotique et un
   article « humanités numériques » séparé) ;
4. faire vérifier la carte des copies par un humain.

**Fichiers à lire en premier** : `docs/PROBLEM.md` (la problématique), `docs/PROTOCOL.md` (§G),
`notes/looking/SYNTHESIS.md` (ce que montrent les 20 emblèmes), `docs/reviews/` (les critiques).

---

One entry per wake-up, newest last: date/time, step, what was done, what was found, next.

## Questions for Marcel

1. **Library access (blocking for any originality claim).** Can you get, via a library, JSTOR,
   Brill or interlibrary loan: Robert Cummings, "Alciato's Illustrated Epigrams", *Emblematica* 15
   (2007): 193–228 (not open on Glasgow's Enlighten); Alison Adams, "The Role of the Translator in
   Sixteenth-Century Alciato Translation", *BHR* 52.2 (1990); Mason Tung, "Seeing is Believing",
   *Emblematica* 20 (2013); John Manning, "A bibliographical approach…", in Daly (ed.), *Andrea
   Alciato and the Emblem Tradition* (1989). Until then the loop writes the problem with these as
   explicit open risks.
2. **Second human coder and a Latinist.** Both reviewers say a reliability claim needs a second
   independent human coder (≈ 30 emblems × 4 editions double-coded) and a Latinist for segmenting
   the epigrams. Do you know someone (colleague, student, emblem specialist)? Could you be one of
   the coders yourself (estimated load in PROTOCOL)?
3. **One article or two?** The humanities reviewer advises a humanities article (sources and
   fidelity of the pictures, copying) and a separate DH article (catalogue propagation and AI
   models). You asked for one article; the protocol is written so that either works. Your call.

---

## 2026-10-05 — loop set up

Repository created, `PLAN.md` written. First pass done before the loop (in conversation):
literature check (Tung's variorum is the nearest prior work; Brandhorst 2025 the nearest
computational one; no systematic typology found, JSTOR not searched) and data feasibility
(Alciato at Glasgow provides text, translation, Iconclass image/text, pictura ≤ 500 px,
concordance; HTML only). Next: S0.

## 2026-10-05 — S0 done

uv project (`src/etude02`, `tests`, `notebooks`, `docs`, `notes/looking`), ruff + pytest green.
S1 (literature) delegated to a background subagent that writes only `notes/literature.md` and
`references.bib`; meanwhile the loop itself does S2 (scraper). Next: S2.

## 2026-10-05 — S2 in progress

`src/etude02/glasgow.py` (cached polite fetcher, mixed Latin-1/UTF-8 decoding, parser for motto,
epigram, translations, notes, Iconclass image/text, related emblems, pictura) with hand-written
fixture tests. Note: each pictura also carries a short **Glasgow alt-text description** ("A scholar
with a finger to his lips in a small room") — a further verbalisation layer of the image, kept in
the corpus. Core fetch (A31b, A34b, A50a, A21a) running in background → `logs/fetch_core.log`.
Next: when the fetch ends, check counts, commit `data/ids.csv`, start S3.

## 2026-10-05 — S3 started while S2 fetch runs

Fetch at A50a (≈ 30 min left, A21a after). Started looking with three editions: notes for
A31b036, 083, 013, 017, 058, 049, 057 in `notes/looking/`. Recurrent observations so far (to be
tested, not yet categories):
- negation carried by **contrast of two terms + deixis** (pointing driver, A34b035);
- abstractions identified by **inscribing their names in the image** (SPES / NEMESIS, A34b079);
- the image depicts **the vehicle of a simile and drops its tenor and speaker** (hares and lion,
  A31b058; winds and oak without Charles V, A31b057);
- **attribute as condensed time/condition** (Occasio's bald back, A31b017);
- negated outcome shown as **co-presence of force and persistence** (A31b057);
- **appearance vs being** cannot be settled by a picture (mask vs severed head, A31b049);
- 1531 woodcuts sometimes **omit the premise** (no image of Isis on the ass, A31b036; the
  "Ethiopian" not dark, A31b083).
**Method warning:** Glasgow alt-texts and Iconclass "image" notations for 1531 describe what the
*text* says, not what the woodcut shows (A31b036, A31b083). The catalogue's image layer is not
independent of the text; the protocol will need an image-only description made blind to the text.
Next: finish S2 checks, complete S3 to ~20 emblems with all four editions.

## 2026-10-05 — S1 done

`notes/literature.md` (≈ 120 works, sections A–J, gap statement, threats to originality) and
`references.bib` (184 entries, 20 marked `[unverified]`) written by a background subagent; spot
checks: Worth's original reference (*Versus* 12, 1975: 85–108) is sourced to note 1 of the 1981
reprint; Cummings 2007 record confirmed on eprints.gla.ac.uk/5531 with **no full text**.
Key points for the problem:
- no systematic coding of text→image operations in Alciato exists in what could be read; Tung's
  212 variorum commentaries were mined: ~a dozen picture-vs-text remarks, no categories;
- Worth (1975) gives the exact "cannot" list (conditionals, counterfactuals, negatives, past/future
  tense, questions) — **never tested on a corpus where each picture's verbal source is known**;
  this is the hook for the semiotic contribution;
- production chain documented: Steyner 1531 calls the cuts rough signs of the author's intention;
  Hunger 1542: the translator described the epigrams for an "unlettered painter" — illustrators
  often worked from a paraphrase, not the Latin (a confound and an opportunity);
- Brandhorst 2004: the text "tells us what we are looking at" — consistent with our observation
  that Glasgow's Iconclass "image" layer is text-dependent; the image/text split has never been
  analysed;
- biggest originality risk: Cummings 2007 (unread). Added to Questions for Marcel.

## 2026-10-05 — S2 done

Core fetch complete: 640 emblem pages (A31b 104, A34b 113, A50a 211, A21a 212), 634 picturae
(1531 has 6 emblems without a woodcut: A31b087, 089, 101–104). Fields present for nearly all:
epigram, English translation, Iconclass image and text, Glasgow alt-text. **All 104 emblems of
1531 have a counterpart in each of the three later core editions** (via "related emblems"), so the
1531 set is a complete 4-edition panel. `data/ids.csv` committed (ids, counts, concordance; no
text). Local `data/corpus.jsonl` is git-ignored. Next: S3 with all four editions.

## 2026-10-05 — S3 done

20 emblems looked at in the four core editions (`notes/looking/`, one file each, links to
Glasgow); synthesis in `notes/looking/SYNTHESIS.md`. Nine candidate operations emerged from the
cases (omission; vehicle-not-tenor; state co-presence; contrast + deixis; attribute as condensed
narrative; naming by inscription or attribute; mood shift; depicting the negated content;
particularisation/generalisation), plus what images must commit to (number, posture, setting,
gender, material, species) and a medium-specific vs picture-generic distinction (colour).
Correction made on the way: appearance-vs-being (mask vs head, 049) *is* depictable with extra
cues (1621). Key structural findings: 1531 departs from the text's key configuration in ≥ 7/19
cases (a special edition, not a representative illustrator); later editions often converge
towards the text; the catalogue's image layer follows the text in some cases and the image in
others — a measurable variable. Next: S4, write `docs/PROBLEM.md`.

## 2026-10-05 — S4 done (v0.1)

`docs/PROBLEM.md` v0.1: sharpened RQ with four sub-questions (losses and operations;
commitments/over-specification; drift; re-verbalisation), gap with nearest works, design evidence
from S3, hypotheses H1–H4 with refutation conditions (+ H5 exploratory), contributions per
discipline, scope limits (1531 panel confirmatory; copying; Latin; intermediaries; resolution; model
contamination; sensitive content). Central design idea made explicit: **divergence items** (picture
and text disagree) separate reading the picture from importing the text. Next: S5, two hostile
reviews.

## 2026-10-05 — S5 done

Two hostile reviews (`docs/reviews/R1-*.md`): both **major revision**. Main lessons: the text is
not fixed (verified: 67/312 epigram pairs differ > 10 % of tokens); the catalogue "leakage" I
reported in S3 is largely **record inheritance** between editions (verified: 51/312 alt-texts
identical) — my S3 claim was wrong as stated; "loss" of conditionals is true by construction, the
period criterion is the *res picta*; operations were derived from the set they would be tested on;
no reliability without a second human. PROBLEM rewritten as v0.2 (multi-source model, res picta
frame, dev/confirm split, copy matrix first, blind descriptions, quantified hypotheses H1–H5),
point-by-point response in `docs/reviews/R1-response.md`. Fixed a parser bug (page-break link text
inside epigrams). Fetching A31a for collation. Two new questions for Marcel (coders; one or two
papers). Next: S6 protocol.

## 2026-10-05 — S6 started; corrections from Tung

Tung's per-emblem commentaries (copied locally to `data/raw/tung/`, not committed) give for every
emblem a **TEXT source**, sometimes a **PICTURE source** (Aesop, Physiologus…), and a "PICTURE
variant" paragraph that describes each cut and states copy relations ("followed in reverse in 34",
"47/83" = same cut, "reuses the cut of emblem 44"). This is the seed of the copy matrix and an
expert description layer.
Corrections to my own S3 readings: **A31b036 — the 1531 ass does carry a shrine** (empty arched
plaque); my "carries nothing" was wrong, and so was the claim that the alt-text there describes
something absent (review R1-humanities obj. 1 rested partly on my error). A31b013 — the 1531 cut is
a **reused block** from another emblem. Method lesson recorded in PROTOCOL: one looker at ≤ 500 px
is not reliable; blind human descriptions + Tung + Gallica scans are needed.

## 2026-10-05 — S6 done (v0.1)

`docs/PROTOCOL.md` v0.1: materials and programmes (P31/P34/P50/P21; Tung's "51" vs our A50a to be
checked), A31a/A31b collation, **copy and source matrix seeded from Tung and checked by two
humans**, development set (20) vs confirmation set (all 84 other emblems of the 1531 panel),
double-coded subset (30, fixed seed), stages A (blind inventory) → B (segmentation on the printed
Latin) → C (relation codes) → D (interpretive labels) → E (catalogue audit) → F (VLM diagnostic
with closed probes, six conditions incl. mismatched text and text-only, ≥ 2 open-weight pinned
models), workload estimate, analysis plan per hypothesis with power simulation gate,
preregistration, ethics, threats table. `docs/ANNOTATION_GUIDE.md` v0.1 with examples from the
development set. Next: S7 pilot (collation, Tung seeds, pilot coding of the dev set).

## 2026-10-05 — S7 pilot, part 1

- **Collation 1531** (`notes/collation_1531.md`): A31a and A31b print every pictura from the same
  blocks; 98 picturae = 97 blocks (A31b013 reuses A31b078's cut), matching Glasgow's 97; type reset
  (mottos, 31 epigrams slightly different). Panel keeps A31b.
- **Copy seeds from Tung** (`src/etude02/tung.py`, `data/copy_seeds.csv`): simple rules resolve
  only ≈ 20 % of pairs (31→34: 18/104), and some seeds are wrong (A31b009). Pilot finding: the
  copy matrix needs a human reading of Tung's paragraphs plus the contact sheets; rules can at
  most pre-fill.
- **Segmentation pilot** on 4 emblems (`annotations/pilot/B_units/`): issues found — overlapping
  RP units (ass carries image / objects on its back), material as RP (depictable only by
  convention), attributes of motion and emotion (slow, proud), irrelevant text variants
  (perdat/perdet) need a relevance rule; 096 is mostly RP-DENIED units with one affirmed key unit.
- Fetcher now retries on dropped connections (Glasgow closed one during the A31a fetch).
- Running: blind-inventory pilot (separate model instance, anonymised pictures); qwen2.5vl:3b
  download for the probe pipeline test.

## 2026-10-05 — S7 pilot, part 2: blind inventory

The blind inventory form was piloted by a separate model instance on 79 anonymised pictures
(`annotations/pilot/A_inventory/`, report there). Two findings:
1. **Content:** on the cases that matter, the blind descriptions agree with Tung and with the
   corrected readings: 1531 Isis cut = "arched plaque, blank, rests on the ass's back"; crowned bird
   (006); gourd on a separate pole (068); blindfolded winged boy (096); the washed man in 083 not
   drawn darker and the scene not recognised as the Ethiopian.
2. **Blindness fails when one describer sees several variants of a subject**: recognition on
   78/79 pictures, spreading across variants and shaping descriptions. For humans as for models,
   Stage A must give each describer **one variant per emblem** (four describer batches in a
   Latin-square), mixed with unrelated pictures, RECOGNISED collected first with a "did it change
   your description?" flag. Also: POSE type, entity ids, counting rule, zoom.
These go into ANNOTATION_GUIDE / PROTOCOL v0.2 at the end of S7.

## 2026-10-06 — S7 done

Probe pipeline tested on qwen2.5vl:3b (after waiting in the heavy-computation queue behind axel
and impressions jobs): 144/144 answers parsed; pattern in the direction of H5 (matching epigram
pulls answers to the text, mismatched does not) **but confounded by a yes-bias** (88/144 "yes",
6/8 probes had "yes" as text answer) → probes must be polarity-balanced (PROTOCOL §8 updated).
`notes/pilot_probes.md`, `notes/pilot_S7.md`, `notebooks/01_pilot.ipynb` (executed). Guide and
protocol at v0.2. Next: S8, second review by fresh reviewers.

## 2026-10-06 — S8 in progress: review 2

Two fresh reviewers (not shown round 1): both **major revision** (`docs/reviews/R2-*.md`). They
converge: (1) the four programmes are not independent illustrators — build the **complete copy
matrix first**, count independent designs, then choose programmes (add de Tournes/Salomon 1547);
(2) restricting H1 to independent re-designs is selection bias and may leave n ≈ 0 — analyse all
pairs and model "redesigned vs kept" as an outcome; (3) decision rules confuse non-significance
with refutation; programme must be fixed only; (4) H3 needs closed property slots; H4 needs a
directional notation-level test; H5 needs its preregistered contrast; (5) the res picta criterion
is one of two period criteria (scene fidelity / carries the point); Greek Anthology and antique
artworks are missing sources; (6) **staffing and reliability must be tested with humans on the
development set before any freeze**; (7) scope: humanities article (RQ1–3) + DH paper (RQ4–5).
Running: a first-pass copy matrix for all 104 emblems from Tung (machine pre-fill, to be
checked by a human).

## 2026-10-06 — S8 done

First-pass copy matrix from Tung for all 104 emblems (`data/copy_matrix_firstpass.csv`, machine
pre-fill, 175/416 rows low confidence): 1534 redraws ≈ 48 / copies ≈ 42 / unclear 14; 1547 ≈ 22
independent; 1551 and 1621 mostly copy. PROBLEM and PROTOCOL rewritten as **v0.3**: panel 1531 /
1534 / de Tournes 1547 (1550, 1621 exploratory); H1 = does a 1531 departure predict redrawing;
H2 = realisation on all pairs with ancestor covariate; H3 = sources vs sham base rate; H4 =
slots; decision tables with equivalence bounds; two period criteria (scene + carries the point);
Greek and antique sources; directional catalogue test and VLM diagnostic moved to a DH companion
with their own preregistration; **human calibration gate before any freeze**. Responses in
`docs/reviews/R2-response.md`. Next: S9.

## 2026-10-06 — S9 done, loop stopped

French summary for Marcel written at the top of this file; README status updated. The loop
stops here as planned (no full annotation, no article). Blocking next steps are human: library
access, calibration round with people, copy-matrix check, publication shape.
