# S7 pilot — what was tested and what changed

All pilot annotations are by the autonomous loop or a separate model instance; they test forms,
not hypotheses (`annotations/pilot/README.md`).

| Component | Result | Change |
|---|---|---|
| 1531 collation | same blocks in A31a/A31b; 97 blocks for 98 picturae (one reuse) | panel = A31b (PROTOCOL §0.1) |
| Copy seeds from Tung | rules resolve ≈ 20 % of pairs, some wrong | human reading of every paragraph |
| Stage A blind inventory (79 pictures) | content agrees with Tung on key cases; **blindness fails** across variants (78/79 recognised) | one variant per emblem per describer; RECOGNISED first + effect flag; POSE; entity ids; counting rule; zoom |
| Stage B segmentation (4 emblems) | 6–9 units/emblem; overlaps; motion/emotion units undecidable; trivial variants | merge rule; `RP-STATE` excluded from fidelity; variant relevance rule |
| Stage C relations (2 emblems × 4) | empty frame case (036 P31); instrument granularity; material contrast lost (059 P21) | `partial` code; granularity rule; shared-cue rule |
| Probe pipeline (8 probes × 6 conditions × 3 templates, qwen2.5vl:3b) | machinery works (144/144 parsed); pattern in H5 direction but confounded by a yes-bias | polarity-balanced probe pairs (PROTOCOL §8) |

Open, needs humans: agreement on RP/AR, on substituted/contradicted/partial, on source labels;
timing per item; P50 vs Tung's "51".
