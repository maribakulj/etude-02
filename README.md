# étude 02 — what cannot be drawn

A research article and its companion repository (code, notebooks, annotations).

## Question

What can a visual representation keep or express that verbalisation loses, and the reverse?

Field of observation: the emblems of Andrea Alciato (*Emblematum liber*, 1531, and its re-editions
up to 1621). Alciato's epigrams were first texts; illustrators drew woodcuts from them, and later
illustrators redrew them edition after edition. This gives a chain of translations:

> epigram (text) → woodcut (image, 16th c.) → catalogue record and Iconclass (text, 20th–21st c.)
> → description by a vision-language model (today)

Working questions (to be sharpened — see [`PLAN.md`](PLAN.md)):

1. How do illustrators render what cannot be drawn: negation, time, condition, causality,
   abstraction, speech, generic vs particular?
2. What does the image fix that the text left open (number, posture, arrangement, setting), and
   how do these choices drift across editions?
3. Do cataloguers and vision-language models (with and without the text) lose the same things as
   the illustrator, or different ones?

## Prior work this project must position itself against

- Mason Tung, *Variorum Edition of Alciato's Emblemata* (Alciato at Glasgow): pictorial variants
  commented case by case, without typology or measurement.
- John Manning (1989): bibliographical approach to the woodblocks.
- Hans Brandhorst (2025), "The elephant in the room": ChatGPT reads emblems through their text and
  invents Iconclass notations (qualitative, a handful of examples, not Alciato).
- Visual negation: Oversteegen & Schilperoord (2014); Sato, Mineshima & Ueda (2023);
  Alhamoud et al. (NegBench, CVPR 2025).

## Data

Main source: [Alciato at Glasgow](https://www.emblems.arts.gla.ac.uk/alciato/) — 22 editions,
3,648 emblems (212 distinct): Latin text, English translation, Iconclass notations split into
"image" and "text", woodcut, cross-edition concordance. Also Emblematica Online (stable handles)
and Gallica (IIIF, higher resolution).

**Rights.** Texts and images belong to the University of Glasgow. This repository contains no
images and no transcriptions: only the scripts that fetch them, our own annotations, and
identifiers. Images stay on the local machine (`data/raw/`, `data/images/`, git-ignored) or in
private storage.

## Status

Research problem and protocol under construction by an autonomous loop. Steering document:
[`PLAN.md`](PLAN.md); log: [`JOURNAL.md`](JOURNAL.md).
