# Review 1 — DH / computing reviewer (subagent, 2026-10-05), on PROBLEM.md v0.1

Verdict: **major revision**. Summary of objections (full text kept in the session log):

1. BLOCKING — constructs undefined ("content unit", "key configuration", "fidelity", "divergence
   item"). Segment the Latin into propositions with a written grammar; fix "key" a priori (units
   the motto or final distich depend on); report unitising α_u and coding α separately.
2. BLOCKING — operations derived from the 20 design emblems they would be tested on. Freeze the
   scheme; confirm on a fresh stratified random sample; the 20 are a development set.
3. BLOCKING — one annotator + LLM is not reliability. Second independent human on ≥ 25 % (or 30
   emblems × 4 editions); pre-registered α ≥ 0.67 (0.80 for tested categories); budget
   ≈ 3,300 judgements per coder.
4. BLOCKING for H1–H3 — clustering, copying, rare Worth units, underpowered H3. Mixed-effects
   logistic models (emblem, edition), copy covariate, minimum detectable effects by simulation,
   Holm correction; categories with < ~15 units descriptive only.
5. BLOCKING — refutation conditions lack tests and thresholds; H2 near-tautological without a
   baseline and definitions of "dimension" and "varies".
6. BLOCKING for catalogue claim — H4 for catalogues near-trivial (cataloguers saw the text);
   record reuse (51/312 later alt-texts byte-identical to 1531; 9 identical Iconclass-image sets);
   divergence defined by text-informed coders is circular. Reframe as an audit; deduplicate;
   define divergence from blind image-only descriptions collected before reading the text.
7. BLOCKING for computing — contamination. Perturbations (mirror/crop), mismatched-text and
   text-only conditions, ≥ 2 open-weight pinned models, temperature 0 + samples, 3–5 prompts.
8. BLOCKING — LLM-as-judge shares the bias under study. Closed yes/no probes per divergence item,
   written from blind descriptions, scored deterministically; human validation.
9. NON-BLOCKING — computing part thin (30–40 items): scale or present as a controlled diagnostic
   with a released probe set and datasheet.
10. NON-BLOCKING — Latin vs translation; intermediaries: Latinist segmentation; check on 15
    emblems; code "source uncertain".
11. NON-BLOCKING — ≤ 500 px: "indeterminate" code; Gallica high-res for divergence items.
12. NON-BLOCKING, urgent — read Cummings 2007 before freezing §7.

Top 3: dev/confirm split + two humans + unit definitions; divergence without the text + audit of
record reuse; quantitative hypotheses + contamination-aware VLM design with deterministic probes.
