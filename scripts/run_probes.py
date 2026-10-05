"""Run closed probes on a local vision-language model through Ollama (PROTOCOL §8, pilot).

Conditions: image, image+motto, image+epigram, image+mismatched epigram, epigram only (no image),
mirrored image+epigram. Three prompt templates. Temperature 0. Answers parsed deterministically.
Usage: uv run python scripts/run_probes.py MODEL [probes.csv]
Output: results/probes/<model>/<probes-stem>.jsonl (committed: answers, not texts).
"""

import base64
import csv
import io
import json
import re
import sys
from pathlib import Path

import requests
from PIL import Image, ImageOps

from etude02.corpus import ROOT, emblem, image_path

TEMPLATES = [
    "{context}Look at the picture. {q} Answer with one word: yes, no, or unsure.",
    "{context}Question about the image: {q} Reply only 'yes', 'no' or 'unsure'.",
    "{context}{q} Base your answer only on what is drawn. One word: yes / no / unsure.",
]
CONDITIONS = [
    "image",
    "image+motto",
    "image+epigram",
    "image+mismatched",
    "text_only",
    "mirrored+epigram",
]


def b64(img: Image.Image) -> str:
    buf = io.BytesIO()
    img.convert("RGB").save(buf, format="JPEG", quality=92)
    return base64.b64encode(buf.getvalue()).decode()


def text_of(eid: str, motto_only: bool = False) -> str:
    e = emblem(eid)
    if motto_only:
        return f"Motto: {e.motto.replace(chr(10), ' ')}\n"
    return (
        f"Motto: {e.motto.replace(chr(10), ' ')}\nEpigram (Latin): {e.epigram}\n"
        f"Translation: {e.epigram_translation}\n"
    )


def parse(ans: str) -> str:
    m = re.match(r"\W*(yes|no|unsure)\b", ans.strip().lower())
    return m.group(1) if m else "unparsed"


def main(model: str, probes_path: Path) -> None:
    probes = list(csv.DictReader(open(probes_path)))
    pics = sorted({p["picture"] for p in probes})
    mismatch = {p: pics[(i + 1) % len(pics)] for i, p in enumerate(pics)}
    out = ROOT / "results" / "probes" / model.replace(":", "_") / f"{probes_path.stem}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w") as fh:
        for p in probes:
            img = Image.open(image_path(p["picture"]))
            for cond in CONDITIONS:
                ctx, images = "", [b64(img)]
                if cond == "image+motto":
                    ctx = text_of(p["picture"], motto_only=True)
                elif cond in ("image+epigram", "mirrored+epigram"):
                    ctx = text_of(p["picture"])
                elif cond == "image+mismatched":
                    ctx = text_of(mismatch[p["picture"]])
                if cond == "text_only":
                    ctx, images = text_of(p["picture"]) + "(No picture is shown.)\n", []
                if cond == "mirrored+epigram":
                    images = [b64(ImageOps.mirror(img))]
                for t, tpl in enumerate(TEMPLATES):
                    prompt = tpl.format(context=ctx, q=p["question"])
                    r = requests.post(
                        "http://localhost:11434/api/generate",
                        json={
                            "model": model,
                            "prompt": prompt,
                            "images": images,
                            "stream": False,
                            "options": {"temperature": 0, "seed": 1, "num_predict": 8},
                        },
                        timeout=600,
                    )
                    raw = r.json().get("response", "")
                    fh.write(
                        json.dumps(
                            {
                                "probe": p["probe_id"],
                                "condition": cond,
                                "template": t,
                                "raw": raw,
                                "answer": parse(raw),
                                "picture_answer": p["picture_answer"],
                                "text_answer": p["text_answer"],
                            }
                        )
                        + "\n"
                    )
                    fh.flush()
    print("written", out)


if __name__ == "__main__":
    main(
        sys.argv[1],
        Path(sys.argv[2] if len(sys.argv) > 2 else ROOT / "probes" / "pilot_probes.csv"),
    )
