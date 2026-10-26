"""Local corpus access: emblems parsed from the cached Glasgow pages, grouped across editions."""

from __future__ import annotations

from functools import cache
from pathlib import Path

from .glasgow import Emblem, decode_mixed, parse_emblem

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
CORE = ("A31b", "A34b", "A50a", "A21a")


@cache
def emblem(eid: str) -> Emblem:
    return parse_emblem(decode_mixed((RAW / "html" / f"{eid}.html").read_bytes()), eid)


def available(eid: str) -> bool:
    return (RAW / "html" / f"{eid}.html").exists()


def versions(eid: str, editions: tuple[str, ...] = CORE) -> dict[str, str]:
    """Same emblem in each requested edition, by the site's 'related emblems' concordance."""
    group = [eid, *emblem(eid).related]
    out = {}
    for ed in editions:
        hits = [x for x in group if x.startswith(ed)]
        if hits:
            out[ed] = hits[0]
    return out


def image_path(eid: str) -> Path:
    return RAW / "images" / f"{eid}.jpg"
