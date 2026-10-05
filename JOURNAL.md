# JOURNAL

One entry per wake-up, newest last: date/time, step, what was done, what was found, next.

## Questions for Marcel

1. **Library access (blocking for any originality claim).** Can you get, via a library, JSTOR,
   Brill or interlibrary loan: Robert Cummings, "Alciato's Illustrated Epigrams", *Emblematica* 15
   (2007): 193–228 (not open on Glasgow's Enlighten); Alison Adams, "The Role of the Translator in
   Sixteenth-Century Alciato Translation", *BHR* 52.2 (1990); Mason Tung, "Seeing is Believing",
   *Emblematica* 20 (2013); John Manning, "A bibliographical approach…", in Daly (ed.), *Andrea
   Alciato and the Emblem Tradition* (1989). Until then the loop writes the problem with these as
   explicit open risks.

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

## 2026-10-05 evening — S2 in progress

`src/etude02/glasgow.py` (cached polite fetcher, mixed Latin-1/UTF-8 decoding, parser for motto,
epigram, translations, notes, Iconclass image/text, related emblems, pictura) with hand-written
fixture tests. Note: each pictura also carries a short **Glasgow alt-text description** ("A scholar
with a finger to his lips in a small room") — a further verbalisation layer of the image, kept in
the corpus. Core fetch (A31b, A34b, A50a, A21a) running in background → `logs/fetch_core.log`.
Next: when the fetch ends, check counts, commit `data/ids.csv`, start S3.

## 2026-10-05 20:05 — S3 started while S2 fetch runs

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

## 2026-10-05 20:50 — S1 done

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
