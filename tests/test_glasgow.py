# The fixture below is written by hand to mimic the site's structure; it contains no Glasgow text.
from etude02.glasgow import decode_mixed, parse_contents, parse_emblem

PAGE = """
<html><body>
<div class="emblem">
<span class="pb"><a href="facsimile.php?id=XX_A1r">Link to an image of this page</a></span>
<div class="T1"><span class="la"><p>MOTTO LINE.</p><p class="translation">Motto gloss</p></span></div>
<div class="pictura"><p><a href="picturae.php?id=Z99a001">
<img src="images/pic_m/Z99a001.jpg" alt="A man and a tree" /></a></p></div>
<div class="T2"><span class="la"><p class="linegroup">First verse,<br />
<span class="indent">second <span class="name" title="X">verse<span class="ref">
<a class="ref" href="#n">[1]</a></span></span>.</span><br /></p>
<p class="translation">First, second.</p></span></div>
<div class="notes"><b>Notes</b>:<br /><p class="note"><b>1.</b> A note.</p></div>
</div>
<div class="box"><h2 class="main-title">Related Emblems</h2>
<ul><li><a href="emblem.php?id=Z98a004"> Other: MOTTO.</a></li>
<li><a href="emblem.php?id=Z97b010"> Other: Motto.</a></li></ul></div>
<div class="box"><h2 class="main-title">Iconclass Keywords</h2>
<p><b>Relating to the image:</b></p>
<ul><li>tree [25G3] <a href="search.php">Search</a> | <a href="b.php">Browse</a></li>
<li>man [31D14] <a href="search.php">Search</a></li></ul>
<p><b>Relating to the text:</b></p>
<ul><li>Patience (+ emblematical representation of concept) [56(+4)] <a href="s">Search</a></li></ul>
</div>
</body></html>
"""


def test_parse_emblem():
    e = parse_emblem(PAGE, "Z99a001")
    assert e.edition == "Z99a"
    assert e.motto == "MOTTO LINE."
    assert e.motto_translation == "Motto gloss"
    assert e.epigram == "First verse,\nsecond verse."
    assert e.epigram_translation == "First, second."
    assert e.picture_alt == "A man and a tree"
    assert e.picture_url.endswith("images/pic_l/Z99a001.jpg")
    assert e.facsimile == "XX_A1r"
    assert e.notes == ["1. A note."]
    assert e.related == ["Z98a004", "Z97b010"]
    assert e.iconclass_image == [
        {"code": "25G3", "label": "tree"},
        {"code": "31D14", "label": "man"},
    ]
    assert e.iconclass_text == [
        {"code": "56(+4)", "label": "Patience (+ emblematical representation of concept)"}
    ]


def test_parse_contents_keeps_order_and_dedups():
    html = '<a href="emblem.php?id=B2">x</a><a href="emblem.php?id=A1">y</a><a href="emblem.php?id=B2">'
    assert parse_contents(html) == ["B2", "A1"]


def test_decode_mixed():
    raw = b"Taciturnit" + "à".encode() + b" caf\xe9"
    assert decode_mixed(raw) == "Taciturnità café"
