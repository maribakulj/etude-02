"""Seed the copy matrix from Mason Tung's Variorum commentaries (local text copies).

Tung numbers emblems in the 1621 order and refers to editions by two-digit codes: 31, 34, 46, 47,
51, 67, 77, 83, 21 ("47/83" = the same cut in two editions). This module extracts, for a pair of
editions, the sentences that mention the later one, and guesses a relation by simple rules. Every
guess is a *seed* for human checking (PROTOCOL §0.2), never a final code.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TUNG = ROOT / "data" / "raw" / "tung" / "tungtxt"
CODE = {"A31b": "31", "A34b": "34", "A50a": "51", "A21a": "21"}


def commentary(n: int) -> str:
    p = TUNG / f"{n:03d}.comm"
    if not p.exists():
        return ""
    text = re.sub(r"\s+", " ", p.read_text(errors="replace"))
    text = text.replace("Commentary", "").strip("_ ")
    return text.split(" Emblem ")[0]


def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.;])\s+", text) if s.strip()]


def _mentions(sentence: str, code: str) -> bool:
    return re.search(rf"(?<![\d.]){code}(?![\d])", sentence) is not None


@dataclass
class Seed:
    later: str
    earlier: str
    guess: str
    evidence: str


def seed(n: int, earlier: str, later: str) -> Seed:
    """Guess the relation of ``later``'s cut to ``earlier``'s (Tung codes, e.g. '31', '34')."""
    sents = sentences(commentary(n))
    if not sents:
        return Seed(later, earlier, "no commentary", "")
    hits = [s for s in sents if _mentions(s, later)]
    for i, s in enumerate(sents):
        low = s.lower()
        if _mentions(s, later) and "this design" in low and "follow" in low and i > 0:
            prev = sents[i - 1]
            if _mentions(prev, earlier) and not _mentions(prev, later):
                kind = "reversed copy" if "revers" in low else "free copy"
                return Seed(later, earlier, kind, prev + " " + s)
    for s in hits:
        low = s.lower()
        if "reuses the cut" in low:
            return Seed(later, earlier, "reused block from another emblem", s)
        if "nonexistent" in low:
            continue
        if _mentions(s, earlier) and ("follow" in low or "same" in low):
            kind = "reversed copy" if "revers" in low else "free copy"
            return Seed(later, earlier, kind, s)
        if "new design" in low:
            return Seed(later, earlier, "independent design", s)
    for i, s in enumerate(sents):
        low = s.lower()
        if "followed in the rest" in low or "followed by the rest" in low:
            prev = " ".join(sents[max(0, i - 1) : i + 1])
            if _mentions(prev, earlier):
                kind = "reversed copy" if "revers" in low else "free copy"
                exc = re.search(r"except[^.]*", low)
                if exc and _mentions(exc.group(), later):
                    return Seed(later, earlier, "exception to a copy (check)", prev)
                return Seed(later, earlier, kind, prev)
    if hits:
        return Seed(later, earlier, "mentioned, relation unclear", " | ".join(hits))
    return Seed(later, earlier, "not mentioned", "")
