"""Side-by-side sheet of one emblem's pictura across the core editions (local only).

Usage: uv run python scripts/contact.py A31b003 [...]  -> data/derived/contact/<id>.jpg
"""

import sys

from PIL import Image, ImageDraw

from etude02.corpus import ROOT, available, image_path, versions

OUT = ROOT / "data" / "derived" / "contact"
H = 420


def sheet(eid: str) -> None:
    tiles = []
    for vid in versions(eid).values():
        p = image_path(vid)
        if not (available(vid) and p.exists()):
            continue
        im = Image.open(p).convert("RGB")
        im = im.resize((round(im.width * H / im.height), H))
        canvas = Image.new("RGB", (im.width, H + 24), "white")
        canvas.paste(im, (0, 24))
        ImageDraw.Draw(canvas).text((4, 4), vid, fill="black")
        tiles.append(canvas)
    if not tiles:
        return
    w = sum(t.width for t in tiles) + 10 * (len(tiles) - 1)
    out = Image.new("RGB", (w, H + 24), "white")
    x = 0
    for t in tiles:
        out.paste(t, (x, 0))
        x += t.width + 10
    OUT.mkdir(parents=True, exist_ok=True)
    out.save(OUT / f"{eid}.jpg", quality=90)


if __name__ == "__main__":

    for eid in sys.argv[1:]:
        sheet(eid)
