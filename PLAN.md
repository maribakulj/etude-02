# PLAN — steering document for the autonomous loop

Owner: Marcel. Written 2026-10-05. The loop reads this file and the end of `JOURNAL.md` at every
wake-up, does the next unchecked step, logs it, commits, pushes, and schedules the next wake-up.

## Goal of this loop (and when it stops)

Reach, **without supervision**:

1. **`docs/PROBLEM.md`** — a very solid research problem: a sharpened question, the gap it fills
   (with verified references), the claimed original contribution for each of the three
   disciplines (art history / emblem studies, semiotics, information science / computing),
   hypotheses each stated with what would refute them, and scope limits.
2. **`docs/PROTOCOL.md` v0.1** — the beginning of a rigorous protocol: corpus and sampling,
   unit of analysis, annotation scheme with definitions, decision rules and worked examples,
   reliability plan, measures, model conditions, analyses, threats to validity, what is
   pre-registered vs exploratory.
3. A **pilot**: the scheme applied to ~20 emblems × several editions, with the problems it revealed
   and the revisions made.
4. Both documents have survived **two adversarial reviews** (fresh subagents playing hostile
   reviewers: one from *Word & Image* / *Emblematica*, one from *Digital Scholarship in the
   Humanities* / a computing venue), with every blocking objection answered in the text or listed
   as an accepted limitation.

When 1–4 are done: write a final journal entry, a short summary for Marcel (in French, plain words)
at the top of `JOURNAL.md`, stop the loop, and do **not** start the full annotation or the article.

## Rules

- **Everything in English** (code, docs, notebooks, commits). Only the summary for Marcel is French.
- **No images or Glasgow transcriptions in git.** They live in `data/raw/`, `data/images/`
  (git-ignored). Commit scripts, identifiers, our own annotations, aggregate results.
- **Polite fetching**: Glasgow ≥ 3 s between requests; Gallica ≥ 10 s with a Mozilla User-Agent;
  back off on any 429/5xx. Cache everything; never fetch twice.
- **Look before measuring.** Open the woodcuts (Read tool on the image files) and read the Latin and
  the translation before designing any category. Every observation in notes cites the emblem with
  a clickable link (`https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A31b003`).
- **Never invent a reference.** Every citation must have been found (URL or catalogue record).
  Unverifiable items are marked `[unverified]`. Keep `references.bib`.
- **Do not import conclusions from `~/caypollard`.** Its methodology is judged unreliable by Marcel.
  Its code may be read, not trusted.
- **Machine annotation is not ground truth.** If a model annotates, it is a measured condition,
  compared with human judgement — never a substitute for it. Plan for Marcel as human annotator and
  say how many items he would need to do.
- **Heavy computation**: at most 2 at once on this 16 GB Mac, through `~/outils-seg/lourd.sh`.
  This loop should need little (no training).
- **Git**: work on branch `research`, commit each meaningful step, push it (`git push`). Do not merge
  into `main`, do not force-push.
- **One writer**: only this loop writes in `~/etude-02`.
- If blocked by something only Marcel can decide, log it under "Questions for Marcel" in
  `JOURNAL.md`, take the most conservative reasonable choice, and continue.

## Steps

- [ ] **S0 — Set-up.** `uv` project (Python ≥ 3.11), `src/etude02/`, `tests/`, `notebooks/`,
  `docs/`, `notes/`, `references.bib`. Minimal lint/test config.
- [ ] **S1 — Literature, deep pass.** Build on the first pass (see README). Read what is openly
  readable: Tung's variorum preface and several of its per-emblem PDFs, Brandhorst 2025, Sato et al.
  2023, Oversteegen & Schilperoord 2014, Worth (find the original reference), Goodman's
  density/articulation, Barthes' anchorage/relay, Jakobson's intersemiotic translation,
  Panofsky's levels, Shatford's of/about, Scholz and Daly on emblem text–image theory, Giovio's
  rules for the impresa. Search open tables of contents of *Emblematica* and *Word & Image* for
  any typological study of Alciato's illustrations. Output: `notes/literature.md` (one entry per
  work: claim, method, what it leaves open for us) and `references.bib`.
- [ ] **S2 — Corpus core.** Scraper `src/etude02/glasgow.py` (tested on saved HTML fixtures we write
  ourselves, not on Glasgow files): edition contents → emblem pages → motto, epigram, translation,
  notes, Iconclass (image vs text), related emblems, pictura image. Core editions: A31b (1531
  Steyner), A34b (1534 Wechel), A50a (1550 Lyon), A21a (1621 Padua). Local corpus
  `data/corpus.jsonl`; committed: `data/ids.csv` (emblem ids, concordance, no text).
- [ ] **S3 — Looking.** Pick ~20 emblems with a stated rationale (some whose epigram contains
  negation, time, condition, speech, abstraction; some with strong pictorial drift; some controls).
  For each: read Latin + translation, look at the woodcut in all core editions, write
  `notes/looking/<emblem>.md`: what the text says that the image cannot, what the image fixes that
  the text left open, what changed between editions, what Iconclass "image" vs "text" kept.
  No categories decided in advance; let them come from the cases.
- [ ] **S4 — Problem.** Write `docs/PROBLEM.md` from S1 + S3. Sharpen the question until each
  hypothesis is testable on this corpus. State the contribution per discipline and the nearest
  prior work it goes beyond.
- [ ] **S5 — Review 1 of the problem.** Two hostile reviewer subagents (humanities venue; DH /
  computing venue). Log objections verbatim-in-summary; revise.
- [ ] **S6 — Protocol v0.1.** `docs/PROTOCOL.md` + annotation scheme `docs/ANNOTATION_GUIDE.md`
  (categories from S3, definitions, decision rules, examples with links). Model conditions for the
  machine part (image only / + motto / + epigram; which open and API models; prompts fixed in
  advance). How Iconclass "image" vs "text" splits are used. Reliability plan.
- [ ] **S7 — Pilot.** Apply the scheme to the S3 emblems (all core editions). Record every case the
  guide could not decide. Small model pilot (a few emblems, cheap) only to test the pipeline, not to
  report results. Revise guide and protocol → v0.2. Notebook `notebooks/01_pilot.ipynb`.
- [ ] **S8 — Review 2** of PROBLEM + PROTOCOL (fresh reviewers, not told about review 1). Revise.
- [ ] **S9 — Close.** Final journal entry, French summary for Marcel, update README status, push,
  stop the loop.
