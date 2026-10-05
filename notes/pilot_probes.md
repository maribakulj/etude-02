# Probe pipeline pilot (S7) — a test of the machinery, not a result

8 closed probes on 7 development pictures (all P31, chosen from Tung + blind inventories),
6 conditions × 3 prompt templates, `qwen2.5vl:3b` via Ollama, temperature 0, seed 1
(`scripts/run_probes.py`, raw answers in `results/probes/qwen2.5vl_3b/pilot_probes.jsonl`).

**Machinery.** 144/144 answers parsed deterministically (no `unparsed`); ≈ 3 s per call on this Mac.

**Pattern (n = 24 answers per condition, 8 probes; far too small to test anything):**

| Condition | agrees with picture | agrees with text |
|---|---|---|
| image only | 17 | 7 |
| image + motto | 16 | 8 |
| image + epigram | 10 | 14 |
| image + **mismatched** epigram | 19 | 5 |
| epigram only (no image) | 9 | 15 |
| mirrored image + epigram | 11 | 13 |

The direction is the one H5 describes (the matching epigram pulls answers towards the text; a
mismatched one does not), but see the flaw below.

**Design flaw found.** The model answered "yes" 88/144 times, and 6 of the 8 probes have "yes" as
the text answer. An affirmation bias alone would produce part of the pattern. **Fix (PROTOCOL
§8):** balance probes so that, within each item, the text-consistent answer is "yes" for half the
probes and "no" for the other half (pair each probe with its polarity-reversed twin), and report
results by polarity.

Other notes: the mismatched-epigram pairing must avoid emblems that share motifs; the text-only
condition shows the model answers "about the picture" from the text alone (15/24 text-consistent),
which is the prior to subtract.
