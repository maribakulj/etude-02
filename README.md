# étude 02

Research on how words and pictures construct meaning, using the illustrated editions of Andrea
Alciato's *Emblemata* (1531–1621). This repository contains the code, research notes, annotations
and experimental results.

## What is an emblem?

An early modern emblem commonly brings together a short motto (*inscriptio*), a picture
(*pictura*) and a poem or epigram (*subscriptio*). This influential arrangement admits exceptions:
some emblems have no picture, and the parts are not always arranged together on the page. The
[Glasgow introduction to the 1531 edition](https://www.emblems.arts.gla.ac.uk/alciato/books.php?id=A31b)
explains both the pattern and its early variations.

The parts contribute differently to the meaning. A picture may show an animal, a gesture or an
encounter; the poem can make that scene an argument about power, prudence, friendship or fortune;
the motto can guide its interpretation. Understanding the emblem therefore involves relating
visible things to a proposition, an analogy or a moral point. Naming the objects in the picture
is one part of that task.

Alciato's epigrams circulated in manuscript before the first illustrated editions. Printers
commissioned woodcuts, and later editions copied, reversed, modified or replaced their designs.
The corpus thus lets us examine both relations **between text and image** and relations **between
successive images**. Neither relation is simple: the texts also change, and an illustrator may
draw on an earlier picture, a translation, a commentary or another visual source.

## Why this corpus matters for text and vision

Our starting question is: **what can a picture express or specify that words leave open, and
what can words express or explain that a picture leaves implicit?** Emblems make this question
concrete in several ways.

| Feature of the corpus | What it lets us investigate |
|---|---|
| Motto, poem and picture contribute to one emblem | How recognition of a scene relates to interpretation of its point; how language guides visual interpretation. |
| Several designs illustrate the same emblem | Which figures, objects, poses and spatial relations persist through redrawing, and which change. |
| Copies coexist with independent designs | Whether visual similarity indicates transmission, shared subject matter or a common textual source. |
| Poems contain dialogue, temporal relations, conditions and abstractions | How pictures convey these through attributes, composition and conventions, and what a viewer must infer. |
| Catalogues provide descriptions and Iconclass indexing | What happens when an image is put back into words, and how cataloguing depends on textual and historical knowledge. |

For example, in [*In occasionem* (Opportunity)](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A31b017),
the epigram takes the form of questions and answers about a figure's attributes. A forelock and
the bald back of the head express the idea that opportunity can be seized as it approaches, but
cannot be caught once it has passed. The picture can retain attributes while the poem unfolds
their temporal and practical meaning. This gives us several distinct things to study: whether an
attribute is visible, whether it is recognised, and whether its significance is understood.
Our [comparison across four editions](notes/looking/A31b017.md) records changes in the design.

This also creates useful questions for computational models. A visual matcher must find
corresponding parts despite changes in line, composition and orientation. A vision-language model
may recognise the subject from a motto or a familiar poem while overlooking what this particular
woodcut shows. Comparing image-only, text-only and combined conditions, including mismatched
texts, could help separate those sources of an answer. Such tests belong to the broader research
programme; the current v0.5 experiments concern visual matching.

These are historical comparisons with partial controls. Editions share blocks and copy one
another; the verbal source is not constant; the scenes rely on learned conventions. We therefore
need to document transmission and inspect individual witnesses before interpreting differences
as evidence about a medium or a model. The question is how particular pictures convey meaning,
rather than an assumption that time, negation or abstraction cannot be depicted.

## Current study: transmission and visual correspondence

The [research problem, v0.5](docs/PROBLEM.md), focuses on three questions:

1. **Ancestor attribution:** can visual methods identify a woodcut's documented model among
   earlier witnesses, including other designs of the same emblem?
2. **Copy orientation:** can they distinguish copies that preserve left and right from copies
   that reverse them?
3. **Correspondence through redrawing:** can they locate corresponding parts when an image has
   been re-engraved or freely adapted? A small manually annotated evaluation set is planned.

[Mason Tung's *Variorum Edition*](https://www.emblems.arts.gla.ac.uk/alciato/tung-variorum.php)
provides expert accounts of pictorial variants and copying relations. We extract dependency,
orientation and fidelity as separate fields, retaining the evidence and its uncertainty. Tung's
account is selective: an unmentioned relation cannot be treated as evidence of independence.
These are relations between documented witnesses, not a complete reconstruction of production.

This visual work supports a later question about text and image: when a design changes, does the
change draw on the printed epigram, a commentary, a translation or another picture, and how does
it change the scene or its point? Catalogue descriptions and vision-language models remain
further research directions, outside the current v0.5 evaluation.

Prior work and open questions are discussed in the [literature notes](notes/literature.md),
the [visual-methods review](notes/sota_2026-10.md) and [review responses](docs/reviews/).
The proposed contribution is an evaluation against documented historical relations, followed by
human inspection of agreements and disagreements. Finding similar images alone cannot establish
a copying history.

## Sources and corpus coverage

[Alciato at Glasgow](https://www.emblems.arts.gla.ac.uk/alciato/index.php) provides 22 editions
dated 1531–1621, in Latin and several vernacular languages. Alciato's collection eventually reaches
212 distinct emblems; these recur across editions with different numbering, texts and pictures.
Edition records must therefore be distinguished from distinct emblems and from independent
visual designs.

The Glasgow resource provides transcriptions, facsimiles, translations, cross-edition links and
Iconclass notations separated into "image" and "text". That separation is itself material for
study: it does not guarantee that the image indexing was made independently of the poem, or
independently for each edition. Tung supplies a further scholarly evidence layer. Emblematica
Online and higher-resolution Gallica scans are sources for planned extensions.

The local core comprises A31b (1531), A34b (1534), A50a (1550) and A21a (1621), with A31a used for
collation. The v0.5 full run adds A56a (1556), A51a (1551), A67a (1567) and A91a (1591), evaluating
seven witnesses across the 212 emblems wherever images and documented relations are available.
An edition used as a witness can postdate the illustration programme it represents; witness dates
and programme dates must be kept separate. See the [full-run report](notes/v05_full.md).

**Repository contents.** Scripts, identifiers, our annotations and experimental results are
versioned. Downloaded Glasgow images, transcriptions and Tung source files stay in the ignored
local cache (`data/raw/`); the assembled `data/corpus.jsonl`, derived files (`data/derived/`) and
logs are also ignored. They are not missing commits. Downloaded source material is kept out of
git under the project's redistribution policy.

The [data and reproduction guide](docs/DATA.md) documents the source files, published analysis
artifacts and commands needed to rebuild the cache. A [source manifest](data/source_manifest.csv)
records file names, sizes and SHA-256 checksums without redistributing their contents. See also
the [attribution and reuse notice](NOTICE.md).

## Status and preliminary results

The research problem is **v0.5, draft**. The [protocol](docs/PROTOCOL.md) and
[annotation guide](docs/ANNOTATION_GUIDE.md) still describe **v0.3** and need revision for the
current study. The [original loop plan](PLAN.md) and the French summary at the start of
[the journal](JOURNAL.md) describe the earlier phase; later journal entries record the reframing.

After development on 20 emblems, the [full v0.5 run](notes/v05_full.md) covered the 212-emblem
collection with the available witnesses:

- **Copy orientation:** DINOv2 dense matching with RANSAC reached balanced accuracy
  **0.84 [0.79, 0.88]** on 235 pairs; on 142 pairs with explicitly stated orientation,
  **0.82 [0.75, 0.89]**.
- **Ancestor attribution:** DINOv2 global features reached top-1 accuracy **0.66**, against
  **0.60** for the chronological prior, on 475 queries. The overall gain remains modest.

These are preliminary results against machine-extracted readings of Tung, **without human
adjudication yet**. Many same-direction labels are inferred from his notation. The experiments
use Glasgow images at up to about 500 px and DINOv2; the proposed DINOv3 and other correspondence
methods have not been evaluated here. The next steps are human label checking, inspection of
matching errors and preparation of the correspondence annotations.

## Working locally

Install dependencies and rebuild the four-edition core (downloads are cached and rate-limited):

```sh
uv sync
uv run python scripts/fetch_core.py
```

Fetch the additional full-run witnesses and generate a comparison sheet:

```sh
uv run python scripts/fetch_ids.py A56a A51a A67a A91a
uv run python scripts/contact.py A31b017
```

For the 1531 collation, also fetch `A31a`. To reproduce the saved full-run scores after fetching
the core and additional witnesses, run `uv run python scripts/run_v05_full.py`. This downloads
the DINOv2 model on first use and performs substantial local computation.

The sheet is written to `data/derived/contact/`. The additional-edition fetch fills the cache
without updating `data/corpus.jsonl` or `data/ids.csv`. See [`scripts/`](scripts/) for the pilot
and full-run entry points, and [`results/v05_full/`](results/v05_full/) for the saved scores.
