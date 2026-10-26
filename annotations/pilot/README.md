# Pilot annotations (S7) — not data

Made by the autonomous loop (an LLM) to test the forms and the guide on the development set.
They are **not** coder data and are never used in confirmatory analysis. Units are paraphrased in
English with Latin line numbers; no Glasgow transcription is copied.

- `A_inventory/` — blind inventories made by a separate model instance that saw only anonymised
  pictures (Stage A form test). Mapping to emblem ids is published in [`blind_map.csv`](blind_map.csv).
- `B_units/` — segmentation pilot (Stage B), one file per emblem (P31 text; variants noted).
- `C_relations/` — relation-coding pilot (Stage C).
