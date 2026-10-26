"""Fetch and parse emblem pages from Alciato at Glasgow.

The site serves HTML only, declared ISO-8859-1 but with some UTF-8 sequences mixed in
(e.g. Iconclass labels). Everything fetched is cached under ``data/raw`` and never fetched twice.
Images and transcriptions belong to the University of Glasgow and stay out of git.
"""

from __future__ import annotations

import re
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

import requests
from bs4 import BeautifulSoup, Tag

BASE = "https://www.emblems.arts.gla.ac.uk/alciato/"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.0 Safari/605.1.15"
)
DELAY_S = 3.0
EMBLEM_ID = re.compile(r"emblem\.php\?(?:[^\"'#]*&(?:amp;)?)?id=([A-Za-z0-9]+)")
ICONCLASS = re.compile(r"^(?P<label>.*?)\s*\[(?P<code>[^\]]+)\]\s*$")
_UTF8_SEQ = re.compile(
    rb"[\xc2-\xdf][\x80-\xbf]|[\xe0-\xef][\x80-\xbf]{2}|[\xf0-\xf4][\x80-\xbf]{3}"
)


def decode_mixed(raw: bytes) -> str:
    """Decode bytes that are mostly Latin-1 but contain stray UTF-8 sequences."""
    out, pos = [], 0
    for m in _UTF8_SEQ.finditer(raw):
        out.append(raw[pos : m.start()].decode("latin-1"))
        try:
            out.append(m.group().decode("utf-8"))
        except UnicodeDecodeError:
            out.append(m.group().decode("latin-1"))
        pos = m.end()
    out.append(raw[pos:].decode("latin-1"))
    return "".join(out)


class Fetcher:
    """Polite cached HTTP client: one request every ``delay`` seconds, back-off on 429/5xx."""

    def __init__(self, cache: Path, delay: float = DELAY_S):
        self.cache = cache
        self.delay = delay
        self._last = 0.0
        self.session = requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT

    def get(self, url: str, name: str) -> bytes:
        path = self.cache / name
        if path.exists() and path.stat().st_size > 0:
            return path.read_bytes()
        for attempt in range(5):
            wait = self.delay - (time.monotonic() - self._last)
            if wait > 0:
                time.sleep(wait)
            self._last = time.monotonic()
            try:
                r = self.session.get(url, timeout=60)
            except requests.ConnectionError:
                time.sleep(60 * (attempt + 1))
                continue
            if r.status_code == 200:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(r.content)
                return r.content
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(30 * (attempt + 1))
                continue
            r.raise_for_status()
        raise RuntimeError(f"giving up on {url}")


@dataclass
class Emblem:
    id: str
    edition: str
    motto: str = ""
    motto_translation: str = ""
    epigram: str = ""
    epigram_translation: str = ""
    picture_alt: str = ""
    picture_url: str = ""
    facsimile: str = ""
    notes: list[str] = field(default_factory=list)
    iconclass_image: list[dict] = field(default_factory=list)
    iconclass_text: list[dict] = field(default_factory=list)
    related: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


def _text(node: Tag | None) -> str:
    if node is None:
        return ""
    return re.sub(r"\s+", " ", node.get_text(" ", strip=True)).strip()


def _latin_and_translation(block: Tag | None) -> tuple[str, str]:
    if block is None:
        return "", ""
    block = BeautifulSoup(str(block), "html.parser")
    for ref in block.select("span.ref, span.pb"):
        ref.decompose()
    translation = " ".join(_text(p) for p in block.select("p.translation"))
    for p in block.select("p.translation"):
        p.decompose()
    lines = []
    for p in block.find_all("p"):
        for br in p.find_all("br"):
            br.replace_with("\n")
        lines.extend(x.strip() for x in p.get_text().split("\n"))
    latin = "\n".join(re.sub(r"\s+", " ", x) for x in lines if x.strip())
    return latin, translation


def parse_contents(html: str) -> list[str]:
    """Emblem ids listed on an edition's contents page, in book order."""
    seen: dict[str, None] = {}
    for m in EMBLEM_ID.finditer(html):
        seen.setdefault(m.group(1), None)
    return list(seen)


def _iconclass(ul: Tag | None) -> list[dict]:
    items = []
    if ul is None:
        return items
    for li in ul.find_all("li", recursive=False):
        label = next((s for s in li.strings if s.parent is li), "").strip()
        m = ICONCLASS.match(label)
        if m:
            items.append({"code": m["code"].strip(), "label": m["label"].strip()})
    return items


def parse_emblem(html: str, emblem_id: str) -> Emblem:
    soup = BeautifulSoup(html, "html.parser")
    e = Emblem(id=emblem_id, edition=emblem_id[:4])
    body = soup.select_one("div.emblem")
    if not isinstance(body, Tag):
        return e
    e.motto, e.motto_translation = _latin_and_translation(body.select_one("div.T1"))
    e.epigram, e.epigram_translation = _latin_and_translation(body.select_one("div.T2"))
    img = body.select_one("div.pictura img")
    if img is not None:
        e.picture_alt = img.get("alt", "").strip()
        e.picture_url = BASE + img.get("src", "").replace("pic_m", "pic_l")
    fac = body.select_one("span.pb a")
    if fac is not None:
        e.facsimile = fac.get("href", "").split("id=")[-1]
    e.notes = [_text(p) for p in body.select("div.notes p.note")]
    for box in soup.select("div.box"):
        title = _text(box.select_one("h2"))
        if title.startswith("Related"):
            e.related = [
                m.group(1)
                for a in box.select("ul li a")
                if (m := EMBLEM_ID.search(a.get("href", "")))
            ]
        elif title.startswith("Iconclass"):
            for b in box.find_all("b"):
                ul = b.find_parent("p").find_next_sibling("ul")
                if "image" in _text(b):
                    e.iconclass_image = _iconclass(ul)
                elif "text" in _text(b):
                    e.iconclass_text = _iconclass(ul)
    return e
