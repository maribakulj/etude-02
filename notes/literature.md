# Literature — deep pass (S1)

Step S1 of [`PLAN.md`](../PLAN.md), written 2026-10-05. One entry per work: reference, what it claims,
method, evidence quality, and what it leaves open for this project. BibTeX keys are in
[`references.bib`](../references.bib).

**How this was done.** Open sources only (web pages, open PDFs, arXiv, repositories, Glasgow's
site). Glasgow was fetched at ≥ 3 s per request; all 212 per-emblem PDFs of Tung's Variorum were
downloaded and text-mined (copies kept outside the repository). The pass was split into one main
thread (Tung, Glasgow, Alciato's and his printers' statements, Brandhorst 2025, Worth, Sato et al.,
negation in VLMs) and four sub-passes (theory classics; formal pictorial semantics and experiments;
computing; emblem studies with a table-of-contents sweep). Every entry says what was actually read:
**read** = the text itself; **abstract** = abstract/metadata only; **via X** = known only through a
secondary source; **record** = catalogue or publisher record only; **[unverified]** = a detail not
confirmed from any source we saw. Nothing was cited from memory.

**Contents.**
A. The Alciato corpus, primary sources, closest Alciato studies ·
B. Emblem scholarship on illustration and pictura–text relations ·
C. Theory: what pictures can and cannot say ·
D. Visual negation, time and condition: philosophy, formal semantics, experiments ·
E. Cataloguing emblems (Iconclass and the role of the text) ·
F. Computing (Iconclass and AI, VLMs, negation, emblems) ·
G. Table-of-contents sweep: what was checked ·
H. Gap statement ·
I. Threats to originality (what we could not check) ·
J. Reading priorities for later steps

**Five findings that shape the problem (details in the entries).**
1. *Nobody has coded the text→image operations of Alciato's woodcuts.* Tung's Variorum (all 212
   commentaries mined) is genealogical description; explicit text–image remarks occur in about a
   dozen emblems and form no categories (A1). Andenmatten 2018 (75 animal emblems) and Ureña 2001 are
   qualitative (B1, B2).
2. *The canonical "cannot" list exists and matches our categories.* Worth (*Versus* 12, 1975):
   pictures "cannot depict conditionals, counterfactuals, negatives, or past-future tenses. Neither
   can they … ask questions" (D1). It has never been tested on a corpus where the verbal source of
   each picture is known.
3. *The chain is documented.* Steyner 1531 calls the cuts "notulis … rudioribus" of the author's
   intention; Hunger 1542 was asked to describe the images at length "pictori idiotae" (A4): the
   illustrator often rendered a prose paraphrase, not the Latin.
4. *Catalogue labels are not image-only.* Brandhorst 2004: motto, epigram and commentary "quite
   literally tell us what we are looking at" (E1). Glasgow's image/text Iconclass split is an
   unanalysed record of that judgement (A3, E6). The Brill Iconclass AI test set mixes motto-derived
   labels into "image" labels (F5).
5. *Machines read the text, not the picture.* Brandhorst 2019 and 2025: Google Vision harvests
   surrounding text; GPT-4o describes the *Ne quid nimis* woman as pouring "carefully" when the
   picture shows her overflowing the dish (F1, F4). NegBench finds an "affirmation bias" (F2).
   No study varies image-only / + motto / + epigram on emblems.

## A. The Alciato corpus, primary sources, and the closest Alciato studies

### A1. Tung, *The Variorum Edition of Alciato's Emblemata* (web, Alciato at Glasgow, "related material")
- **Reference.** Mason Tung, *Andrea Alciato, Emblemata: The Variorum Edition of Alciato's Emblemata*. Online PDFs (preface + 212 per-emblem files), Alciato at Glasgow, University of Glasgow, n.d. (preface PDF created after 2010; it cites the 2010 census update). <https://www.emblems.arts.gla.ac.uk/alciato/tung-variorum.php>; preface <https://www.emblems.arts.gla.ac.uk/alciato/tung/alciatotungedition-000.pdf>; index <https://www.emblems.arts.gla.ac.uk/alciato/tung-variorum-index.php>.
- **Read.** Preface in full; **all 212 per-emblem commentaries** downloaded (3 s between requests) and text-mined; about 20 read closely (3, 11, 12, 19, 27, 30, 44, 59, 101, 104, 107, 118, 121, 131, 132, 145, 156, 158).
- **Numbering.** Tung numbers emblems by the 1621 edition; links below go to the 1621 emblem on Glasgow (`A21a` + number), from which Glasgow's "related emblems" lead to other editions.
- **What it is.** For each emblem: Latin text with textual variants across nine editions (1531, 1534, 1546, 1547/1556, 1551, 1567, 1577/1591, 1583, 1621), a facing page of the woodcuts, and a short "PICTURE variant" commentary (plus "TEXT source"/"PICTURE source" notes, e.g. Greek Anthology, Aesop, Physiologus). Commentary total: c. 35,000 words over 212 emblems (c. 165 words/emblem).
- **Claims (preface).** (i) Steyner 1531: "104 emblems but only 96 woodcuts by Jörg Breu"; Alciato was "dissatisfied with the many illustrations that were unfaithful to their texts" and initiated the 1534 Wechel edition. (Note: the Wechel 1534 dedicatory letter, read on Glasgow, blames textual neglect and says Wechel spared no expense "in formandis iconibus"; the "unfaithful illustrations" formulation is Tung's, not a quotation.) (ii) Scholars "tended to base their conclusions on the woodcuts of one or two editions", which led to misreadings — his example: the 1551 background of emblem [196](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a196) misread as Vulcan, whereas the 1567 cut shows Phidias carving Venus "as the fourth verse in the text clearly states". (iii) Purpose: a "research tool" for art historians, Neo-Latinists and emblem scholars; "the images are not produced to scale".
- **How he describes text–image mismatch (from the full text-mining; regex counts, approximate).** Commentary is overwhelmingly *genealogical and descriptive*: 109/212 commentaries mention reversal ("follows 51 in reverse"), 116 list editions where a cut is "nonexistent", 11 note stock-cut reuse (Aesop editions, Reusner 1581), 32 note inscriptions/labels in the image. Explicit statements relating picture to text occur in only about a dozen emblems, always ad hoc:
  - *partial illustration*: emblem [30](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a030) (1531 "illustrating the second half of the text"; 1547 "a new design illustrating the first half"); emblem [104](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a104) (1531 stock cut of an astrologer "applicable only to the last part of the text");
  - *attribute named in the text added late or not at all*: emblem [27](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a027) (the cubit-ruler "mentioned in the text" appears "for the first time" in 1621); emblem [107](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a107) (dolphin "as called for in the Greek epigram"); emblem [162](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a162) (Myrtilus "named in the Greek epigram");
  - *picture contradicts text*: emblem [145](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a145) (handless judges; 1577 gives them hands "against the text", 1621 "chops off again"); emblem [132](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a132) (1621 "uses a snake (in spite of the text)"); emblem [121](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a121) ("(incorrectly?)");
  - *narrative/temporal logic*: emblem [156](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a156) vs [155](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a155) — Tung reasons that the 1534 background of 155 "failed to illustrate its own text" because Death could not have mistaken arrows "if Cupid was still wearing his own quiver"; in 1547 Cupid is awake and protests, which no longer shows "a willful deception";
  - *printer's error*: emblem [24](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a024) (1577 cut switched with emblem [159](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a159) "by mistake", repeated 1583, corrected 1621); emblem [103](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a103) (block turned on its side);
  - *making the list explicit*: emblem [118](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A21a118) *In colores* (1551 illustrates each of the nine colours "with a scene described in the text"; later editions revert to a single dyer's shop).
- **Categorisation?** None. No typology, no counts, no definitions; "mismatch" is never a category. Illustrators "misreading" texts appears only as a preface generalisation about 1531 and in scattered remarks. Tung does not discuss negation, time, condition or abstraction as such; but several of his cases are exactly such problems (privation in 145; narrative sequence in 155/156; enumerations in 118; futility in 59, where he describes only the washing).
- **Method / evidence quality.** Expert close description by one scholar; very high bibliographical reliability (edition list, page refs), no inter-rater check; descriptive vocabulary not controlled.
- **What it leaves open for us.** (1) A *systematic* record of which text elements each cut renders, omits, adds or contradicts; (2) categories with definitions and reliability; (3) counts across editions; (4) any link to cataloguing or machine description. Tung is our best emblem-by-emblem guide for genealogy (who copied whom, reversals), which we should reuse as a *control for copying* (a "drift" that is only reversal is not interpretive change). His cases 27, 30, 104, 118, 132, 145, 155/156 are ready-made pilot items.

### A2. Tung, "A Concordance to the Fifteen Principal Editions of Alciati's Emblemata" (Emblematica 1) and revision
- **Reference.** Mason Tung, "A Concordance to the Fifteen Principal Editions of Alciati's *Emblemata*", *Emblematica* 1.2 (1986): 319–339. Year conflict resolved: the issue is nominally "Fall 1986" (Glasgow cites "1,2 (1986)") but AMS Press gives its actual publication as July 1987, which is why Tung cites "(1987)". Cite as vol. 1.2 (1986 [1987]). Source for the issue dates: <https://www.amspressinc.com/emblematica.html> (seen by the emblem-studies sub-pass). Revision: "A Revision of 'A Concordance…'", PDF <https://www.emblems.arts.gla.ac.uk/alciato/MasonTungTable.pdf> (linked from the Glasgow home page; not opened in this pass).
- **Claim / method.** Concordance of emblem numbering across editions. Pure bibliography.
- **Leaves open.** It is the backbone for our cross-edition alignment (S2); Glasgow's "related emblems" function already implements a concordance.
- Related Tung items seen cited: "Towards a new Census of Alciati's Editions", *Emblematica* 4 (1989): 135–176 (Glasgow home page); Tung cites himself "Emblematica 4,2: 321–324" for Aesop/Physiologus picture sources (emblems 30, 59, 104, 129) — the census is 4.1 (1989): 135–176, so the 4.2 item is a different, unidentified piece [unverified]. Further Tung items (verified only via Robohn 2021's bibliography): "Alciato's Practices of Imitation", *Emblematica* 19 (2012): 153–257; "Revisiting Alciato and The Greek Anthology", *Emblematica* 14 (2006): 327–348.

### A3. Alciato at Glasgow (site, introductions, help)
- **Reference.** Alison Adams, Stephen Rawles et al., *Alciato at Glasgow*, University of Glasgow (OpenEmblem initiative; British Academy funding). <https://www.emblems.arts.gla.ac.uk/alciato/>.
- **Read.** Home, help, introductions to A31b and A34b, Wechel 1534 prefatory matter, one emblem page (A50a059).
- **Claims.** 22 editions 1531–1621; data now incorporated in Emblematica Online. A31b intro: the 1531 cuts "believed to be by Hans Schäufelein after the Augsburg painter Jörg Breu"; "often of inferior workmanship, and at times ill-suited to their context", yet "the iconographic tradition which they launch is broadly maintained for close on a hundred years"; Peutinger commissioned the woodcuts; the texts show misreadings of a manuscript ("uinxit" for "iunxit"). A34b intro: 113 emblems, woodcuts "possibly designed by Mercure Jollat"; "a few woodcuts however would be revised over subsequent editions, and one replaced ('In astrologos', in the 2nd 1534 edition)". Help page: Iconclass is used "to index images" and "also used experimentally to index mottoes and primary texts (but not secondary texts)", developed with the Dutch Mnemosyne project; each emblem page shows "Relating to the image" vs "Relating to the text" notations.
- **Observation (our own, to be used in S3).** In [A50a059 *Impossibile*](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A50a059), the epigram ("Abluis Aethiopem, quid frustra? ah desine…", "Why are you washing an Ethiopian in vain? Oh, do stop. No one can…") carries futility, an imperative, a negative quantifier and a night metaphor; the *image* notations are all postures, objects and persons (e.g. 31A2541 gripping someone by the arm, 31A5463 towel, 41A3911 well), while *only the text* notations carry "Impossibility (+ emblematical representation of concept) [52BB42(+4)]", "day and night [23R]" and Vanitas [11R5]. The Glasgow split thus already encodes, emblem by emblem, what a cataloguer judged visible vs only in the text — a ready-made instrument for our third question.
- **Attribution of the 1531 cuts — conflicting statements seen.** Glasgow: Schäufelein after Breu (from a monogram on the colophon page); Andenmatten 2018: Breu after Schäufelein's models; Tung's preface, Manning 2002 (via Robohn) and G. Messling, *Hollstein's German Engravings…: Jörg Breu the Elder and the Younger*, part I (2008; publisher page <https://www.hollstein.com/jorg-breu-the-elder-and-the-younger-i.html>): Breu; older views Schäufelein (Duplessis 1884) or Weiditz (Redgrave 1909), via Robohn. For us the designer's identity matters less than the fact that 1531 was designed in Augsburg without Alciato.
- **Evidence quality.** Expert cataloguing; Iconclass assignment rules for "image" vs "text" not documented beyond the help page (to verify in S2: consistency across editions of the same emblem).
- **Leaves open.** Nobody has analysed the image/text Iconclass split as data (as far as we found).

### A4. Statements by Alciato and his printers about the pictures (primary texts, mostly read on Glasgow)
- **Steyner, "Candido lectori" (Augsburg 1531; Glasgow A31a prefatory matter, read).** The printer apologises for the plainness of the "tabellis quae huic operi adiectae sunt" (more elegant pictures would have cost too much) and says: "Utilissimum itaque nobis visum est, si notulis quibusdam obiter, rudioribus, gravissimi authoris intentionem significaremus, quod docti haec per se colligent" — the pictures are *rough little signs of the author's intention, for the less learned*; the learned will gather it by themselves. <https://www.emblems.arts.gla.ac.uk/alciato/othertext.php?id=A31a&t=1>
- **Alciato's preface to Peutinger (1531; reprinted 1534, read on A34b):** "Haec nos festivis Emblemata cudimus horis, / Artificum illustri signaque facta manu. / Vestibus ut torulos, petasis ut figere parmas, / Et valeat tacitis scribere quisque notis." — emblems as designs for craftsmen, so that one may "write with silent signs". <https://www.emblems.arts.gla.ac.uk/alciato/othertext.php?id=A34b&t=1>
- **Wechel's dedication (Paris 1534, read):** the Augsburg book appeared "Autoris iniussu, tam neglecte"; Alciato removed the "mendas", "plurima … retractavit & correxit"; Wechel spared no labour or cost "in formandis iconibus". Nothing says Alciato designed or vetted the pictures. (Tung's "dissatisfied with the many illustrations that were unfaithful to their texts" is an interpretation, not a quotation.)
- **Wolfgang Hunger, dedication of the Paris 1542 Latin–German edition (Glasgow A42b, read):** Wechel sent new emblems "ex Italia ab Alciato recens adlatum" and asked Hunger "ut vertam, & pictori idiotae fusius describam eas imagines, quae quam proxime & venustissime Latini carminis sensum vimque exprimant" — the translator was to *describe at length, for an unlettered painter*, images that would express "the sense and force of the Latin poem". The printer's note adds that the promised extra emblems are missing through the "insignis perfidia sculptoris". <https://www.emblems.arts.gla.ac.uk/alciato/othertext.php?id=A42b&t=1>. English translation: Drysdall 1988 (see B). **This documents a prose intermediary between epigram and woodcut** — a mechanism our error analysis must allow for (an illustrator renders a paraphrase, not the Latin).
- **Letter to Francesco Calvo** (Barni no. 24; dated 9 Dec. 1521 by Ureña Bracero 2001, 9 Jan. 1523 by Andenmatten 2018; often given as Dec. 1522): Latin fragments read in Ureña Bracero 2001 (nn. 4, 14): "Singulis enim epigrammatibus aliquid describo quod ex historia vel rebus naturalibus aliquid elegans significet", "unde pictores, aurifices, fusores id genus conficere possint quae scuta appellamus et petasis figimus vel pro insignibus gestamus qualis anchora Aldi, Columba Frobenii…". Barni's edition (Florence: Le Monnier, 1953) not consulted.
- **Commentary on *De verborum significatione* (1530)**, as quoted by Mignault 1577 and by Heckscher & Wirth 1959: "Verba significant, res significantur: tametsi et res quandoque significent, ut Hieroglyphica apud Orum et Chaeremonem, cuius argumenti et nos carmine libellum composuimus, cui titulus est Emblemata."
- **Letters of 1532** (to Viglius; to Emilio Ferretti, 24 March 1532, admitting the foolishness of the images and the corrupt text): known only via Andenmatten 2018 and Robohn 2021 → [unverified wording]. Drysdall 2001 (via Robohn): Alciato "does not condemn the pictures in principle, but only the errors in them".
- **What this leaves open.** The epigrams were written as *descriptions of signifying things*, meant (in part) for others to make into images; the pictures were added by a printer as "rough signs of intention"; later ones were designed from vernacular prose descriptions. Which elements of a description work as picturing instructions and which only as reading instructions is exactly our question, and the documented chain (Latin → prose description → designer → block-cutter → copyist) is the causal model for drift.

### A5. Mignault, *Syntagma de symbolis* (1577), ed. and trans. Denis Drysdall
- **Reference.** Claude Mignault, "Syntagma de symbolis", in Alciato, *Omnia Emblemata* (Antwerp: Plantin, 1577); critical edition with parallel English by Denis Drysdall, Glasgow emblem website (last updated 2003). <https://www.emblems.arts.gla.ac.uk/Mignault_intro.html>, <https://www.emblems.arts.gla.ac.uk/Mignault_syntagma.html>.
- **Claims.** Repeats Giovio's rules for devising a symbol: (1) apt analogy of "spirit" (motto) and "body" (image); (2) not so obscure as to need a Delian diver; (3) something "attractive and easily distinguished" (stars, moon, fire, clouds, rocks…); (4) "no human figure should be represented, unless very rarely"; (5) motto in a noble/foreign language. On the emblem: it is "often 'silent'; it is not always necessary in the emblem that an epigram should be added"; maxim and emblem "differ as do words and meaning". Drysdall note 31: in the letter to the reader the epigram expresses the *animus*, the picture the *corpus*.
- **Evidence quality.** Primary early-modern theory, reliable edition.
- **Leaves open.** Period theory states division of labour (body/soul) but says nothing about *which* propositional contents the "body" can carry — our question.

### A6. Robohn, *An analysis of the 1546 Venetian edition of Andrea Alciato's Emblematum Libellus* (MA thesis)
- **Reference.** Melissa Ann Robohn, MA thesis, John Cabot University, Rome, 2021. CC BY-NC-ND. <https://archive.johncabot.edu/server/api/core/bitstreams/bfc91d97-6724-46b8-b4bc-5ffcd7af96d0/content>
- **Claims (read relevant chapters).** Synthesises the illustration history: Steyner's idea to add pictures (cf. his *Memorial der Tugent*, 1531, same three-part format); Gabriele's three hypotheses on Alciato's role; Hunger's 1542 preface showing the *translator described the epigrams for the artists* (via Drysdall 1988); attribution history (Duplessis → Schäufelein; Redgrave → Weiditz; "more recent scholarship" → Breu, citing Manning 2002: 43); some 1546 cuts are "merely illustrations of a story". Cites Tung 2013 "Seeing is believing" (Emblematica 20: 379–404) and Cummings 1996.
- **Evidence quality.** Student thesis, careful with sources, secondary for most claims; useful as a citation map, not as authority.
- **Leaves open.** No systematic comparison; qualitative.

### A7. Bässler, *Die Umkehrung der Ekphrasis* (2012), and Wolkenhauer's review
- **Reference.** Andreas Bässler, *Die Umkehrung der Ekphrasis. Zur Entstehung von Alciatos "Emblematum liber" (1531)* (Würzburg: Königshausen & Neumann, 2012), 229 pp. Publisher page <https://verlag.koenigshausen-neumann.de/product/9783826047305-die-umkehrung-der-ekphrasis/>. Review: Anja Wolkenhauer, *Arbitrium* 32.3 (2014): 299–303, DOI 10.1515/arbi-2014-0068 (open copy, Tübingen repository, read in full).
- **Claim (per review).** The emblem originates in the humanist effort to turn ancient ekphraseis (esp. epigrammatic ekphraseis of the Greek Anthology) back into images — a "reversal of ekphrasis"; hence its hybrid text–image status. Appendix lists "Embleme Alciatos und antike Ekphrasen" (pp. 193–199). The reviewer notes that at the end of the 1531 edition some picturae are *not executed* but only described in the text, and criticises philological errors.
- **Evidence quality.** Book not read (review only).
- **Leaves open.** Bässler gives the genetic frame (text → image as the founding direction) but, per the review, no systematic analysis of how the images realise the texts. Our project measures the "reversed ekphrasis" outcome.

### A8. Clement, "Broadcast networks and the Early Modern emblem" (Word & Image 2019)
- **Reference.** Taylor Clement, *Word & Image* 35.4 (2019): 437–455. DOI 10.1080/02666286.2019.1631737 (abstract read via Semantic Scholar/Crossref).
- **Claim.** Artisans produced emblem illustrations by "visual paraphrase" (copying/redrawing blocks); case study of fowling emblems (Alciato *Dolus in suos*, La Perrière LIIII) through Whitney 1586 and Combe 1614, whose translations make the word–image relation "denotative" so readers can decode pictures.
- **Method.** Qualitative case study (one motif).
- **Leaves open.** No typology; the "visual paraphrase" notion is close to our "drift" and should be cited.

## B. Emblem scholarship on Alciato's illustrations and on pictura–text relations

Items marked *(sub-pass)* were located and checked by the emblem-studies sub-pass of this step (scratch files in the session scratchpad); "read" means the text itself was read, "record" means only a catalogue/publisher/secondary record was seen.

### B1. Andenmatten, *Les « Emblèmes » d'André Alciat* (2018) — nearest qualitative precedent
- **Reference.** Anne-Angélique Andenmatten, *Les « Emblèmes » d'André Alciat* (Bern: Peter Lang, 2018), ISBN 978-3-0343-2627-8. Open chapter 2: <https://www.peterlang.com/view/9783034326285/xhtml/chapter02.xhtml> (read, sub-pass).
- **Claims.** Commentary on 75 *animal* emblems; for each poem a choice of woodcuts from the main editions "afin de mesurer l'évolution des motifs et leur adéquation au texte". The 1531 cuts are "attribuées à Jörg Breu, selon les modèles du peintre Hans Schäufelein" (the reverse of Glasgow's attribution). Errors in 1531 picturae could support the view that Alciato took no part, "si toutefois les gravures de la première édition « autorisée » … de 1534, ne renfermaient pas autant d'erreurs, sinon plus".
- **Method / quality.** Philological commentary, qualitative, one domain (animals); no counts.
- **Leaves open.** Her claim that 1534 is as error-prone as 1531 contradicts Glasgow/Tung and is *directly testable* with our scheme. Animals only; no abstraction/negation analysis.

### B2. Ureña Bracero, "Alciato y el poder de la palabra" (2001)
- **Reference.** Jesús Ureña Bracero, "Alciato y el poder de la palabra: poesía, retórica y jeroglíficos", *Anuario de Estudios Filológicos* 24 (2001): 437–451. <https://dialnet.unirioja.es/descarga/articulo/59031.pdf> (read, sub-pass).
- **Claims.** Alciato was indifferent to the woodcuts; lists emblems "capaces de generar más de una imagen" (e.g. nos 96 with 11 images, 117 with 9, 186 with 7); in *In colores* the engraver "no podía representarlos y soluciona el problema dibujando una tintorería" — colour, which a black-and-white woodcut cannot show, becomes a dyer's shop (cf. Tung on emblem 118). Lexical shift in Alciato's own vocabulary from signum/effigies/imago (1531) to arguo/notare/index/symbolum (from 1546).
- **Leaves open.** Isolated observations, but the best seeds for a typology (one-to-many text→image; substitution of an unpicturable predicate by a scene that implies it).

### B3. Balavoine, "Les Emblèmes d'Alciat: sens et contresens" (1982)
- **Reference.** Claudie Balavoine, in Yves Giraud (ed.), *L'Emblème à la Renaissance* (Paris: SEDES, 1982): 49–59. [unverified — not seen; via search results and Ureña 2001].
- **Claim (reported).** The pictures are a *contresens* from 1531: Alciato "ni a voulu, ni a conçu, ni a prévu les images".
- **Leaves open.** A thesis about intention, not a measurement.

### B4. Manning (1989; 2002)
- **References.** John Manning, "A Bibliographical Approach to the Illustrations in Sixteenth-Century Editions of Alciato's *Emblemata*", in Peter M. Daly (ed.), *Andrea Alciato and the Emblem Tradition: Essays in Honor of Virginia Woods Callahan* (New York: AMS Press, 1989): 127–176 [not read; via Robohn 2021]. John Manning, *The Emblem* (London: Reaktion, 2002), archive.org record <https://archive.org/details/emblem0000mann> (lending only; not read).
- **Claims (via Robohn).** The inconsistencies between epigrams and illustrations, "corrected over time", would not have occurred if Alciato had given directions (1989: 145); 1531 designs by Breu; Wechel designs often copied from Augsburg (2002: 43).
- **Method.** Bibliographical (blocks, copying, editions).
- **Leaves open.** Copying genealogy, not semantics of rendering. Manning's bibliographical approach is complementary: we need it to separate inherited from new divergences.

### B5. Adams; Rawles; Cummings; Callahan; Drysdall (Alciato-specific articles, mostly *Emblematica*)
All verified only as references (via Glasgow pages, Robohn 2021's bibliography, or the AMS contents); none read.
- Alison Adams, "The Role of the Translator in Sixteenth-Century Alciato Translation", *Bibliothèque d'Humanisme et Renaissance* 52.2 (1990): 369–383 — Glasgow describes it as "on revisions to woodcuts". **High priority to read** (JSTOR issue page <https://www.jstor.org/stable/i20678982>).
- Alison Adams, "The Woodcuts of Alciati's Death Emblems", *Emblematica* 6.2 (1992) — designers usually copied earlier blocks (via Robohn).
- Robert Cummings, "Alciato's Illustrated Epigrams", *Emblematica* 15 (2007): 193–228 (record: <https://eprints.gla.ac.uk/5531/>) — described in a secondary source as discussing "the appropriateness or not of their illustrations". **The single most important unread item** for originality.
- Robert Cummings, "Alciato's *Emblemata* as an Imaginary Museum", *Emblematica* 10.2 (1996) (pages garbled in Robohn: "268-926").
- Virginia W. Callahan, "A Comment on the 1531 Edition of Alciato's Emblems", *Emblematica* 6.1 (1992): 203–204; "An Interpretation of Four of Alciato's Latin Emblems", *Emblematica* 5.2 (1991).
- Denis L. Drysdall, "Defence and Illustration of the German Language: Wolfgang Hunger's Preface to Alciati's Emblems", *Emblematica* 3.1 (1988): 143–157; "The Emblems in Two Unnoticed Items of Alciato's Correspondence", *Emblematica* 11 (2001).
- Charles W. M. Henebry, "Writing with Dumb Signs: Memory, Rhetoric, and Alciato's *Emblemata*", *Emblematica* 10.2 (1996): 211–244; Henebry, "Figures of Speech: The *Emblematum Liber* as a Handbook of Rhetorical Ornaments", *Neophilologus* 87.2 (2003): 173–191, DOI 10.1023/A:1022622603484.
- Stephen Rawles, "Layout, Typography and Chronology in Chrétien Wechel's Editions of Alciato", in D. Graham (ed.), *An Interregnum of the Sign* (Glasgow Emblem Studies, 2001): 49–71 (cited on Glasgow A34b page).
- Mason Tung, "'Seeing is Believing': A Note on the Forgettable History of Illustrating Alciato's Emblems", *Emblematica* 20 (2013): 379–404 — a research note; per Robohn (pp. 36–37) it asks whether 1546 Aldine designs were emulated by later illustrators (very few were). **Not read; no sign of a typology in the secondary description.**
- **What these leave open.** Together they establish facts about blocks, copying and translators; none (as far as titles, abstracts and secondary descriptions show) codes text→image operations systematically. Cummings 2007 and Adams 1990 must be read before claiming novelty.

### B6. Scholz (1979; 1984; 1991; 1994; 2002)
- **References (verified as records; not read).** Bernhard F. Scholz, "Semantik oder Ontologie. Zur Bestimmung des 'Verhältnisses zur Wirklichkeit' in der neueren Emblemtheorie", *DVjs* 53.3 (1979): 362–377, DOI 10.1007/BF03376363; "Emblematisches Abbilden als Notation. Überlegungen zur Hermeneutik und Semiotik des emblematischen Bildes", *Poetica* 16 (1984): 61–90 [unverified beyond citations]; "The 1531 Augsburg Edition of Alciato's *Emblemata*: A Survey of Research", *Emblematica* 5.2 (1991): 213–254 (Glasgow says 1990; AMS dates vol. 5 to 1991); "The Brevity of Pictures: Sixteenth and Seventeenth Century Views on Counting the Figures in Impresas and Emblems", in *Renaissance-Poetik / Renaissance Poetics* (Berlin: de Gruyter, 1994) [editor/pages unverified]; *Emblem und Emblempoetik. Historische und systematische Studien* (Berlin: Erich Schmidt, 2002) (review: <https://literaturkritik.de/public/rezension.php?rez_id=11190>); "Emblematic Word-Image Relations in Benedictus van Haeften's *Schola Cordis* … and Christopher Harvey's *School of the Heart*", in *Anglo-Dutch Relations in the Field of the Emblem* (Leiden: Brill, 1997): 149–176, DOI 10.1163/9789004617193_012; "Emblematum pater et princeps", *Emblematica* NS 3 (2019).
- **Claims (from titles, reviews and citations only).** Scholz criticises Schöne's "potentielle Faktizität" as confusing semantics with ontology; treats the emblematic picture as a *notation* (a pictura as the realisation of a res picta described in the text); studies early-modern rules about the number of figures in a pictura.
- **Leaves open.** Scholz is the main semiotician of pictura/subscriptio; his "notation" view predicts that a woodcut realises a *description*, so variants should vary only in the dimensions the description leaves open — a hypothesis we can test. Reading the 1984 *Poetica* article is a priority (paywalled).

### B7. Schöne, *Emblematik und Drama im Zeitalter des Barock* (1964)
- **Reference.** Albrecht Schöne (Munich: C. H. Beck, 1964; 2nd ed. 1968; 3rd ed. 1993). Record <https://archive.org/details/emblematikunddra0000albr> (lending only). Quoted via Dietmar Peil, *Zur "angewandten Emblematik" in protestantischen Erbauungsbüchern* (Heidelberg: Winter, 1978), open: <https://epub.ub.uni-muenchen.de/4900/1/4900.pdf>.
- **Claims (via Peil).** The emblem's "Doppelfunktion des Abbildens und Auslegens"; "potentielle Faktizität" and "ideelle Priorität" of the emblematic picture (1968: 21, 28 ff.).
- **Leaves open.** Pure theory, German Baroque; assumes the picture is primary — the opposite of Alciato's genesis (text first). Our corpus is a natural test of what "priority of the picture" becomes when the picture is demonstrably derived.

### B8. Daly (1979/1998; 2014) and the *Index Emblematicus* (1985)
- **References.** Peter M. Daly, *Literature in the Light of the Emblem* (Toronto: University of Toronto Press, 1979; 2nd ed. 1998), record <https://archive.org/details/literatureinligh0000daly>; Daly, *The Emblem in Early Modern Europe: Contributions to the Theory of the Emblem* (Farnham: Ashgate, 2014; Routledge 2016), chapter "On the Interpretation of Emblems", DOI 10.4324/9781315240039-16; Peter M. Daly and Virginia W. Callahan with Simon Cuttler (eds), *Andreas Alciatus 1: The Latin Emblems. Indexes and Lists* (Index Emblematicus; Toronto, 1985), record <https://archive.org/details/andreasalciatusl0001unse>.
- **Claims.** Daly asks "What functional relationship exists between pictura and scriptura?" (1998: 7–8, via sub-pass); in 2014 he admits "In most cases we simply do not know what instructions the artist received… Or did the illustrator take his cues from the texts…?" (OpenAlex excerpt). The *Index Emblematicus* gives picture and motif indexes built on the 1621 pictures.
- **Leaves open.** Daly states the question we operationalise; he does not answer it with data. (Not read in full: lending-only.)

### B9. Russell; Saunders; Enenkel; Gabriele; Rolet (eds); Sharratt
- Daniel S. Russell, *The Emblem and Device in France* (Lexington, KY: French Forum, 1985), record <https://archive.org/details/emblemdeviceinfr0000russ>; *Emblematic Structures in Renaissance French Culture* (Toronto, 1995); "Alciati's Emblems in Renaissance France", *Renaissance Quarterly* 34.4 (1981): 534–554, DOI 10.2307/2861245; "The emblem and authority", *Word & Image* 4.1 (1988): 81–86, DOI 10.1080/02666286.1988.10436222. Not read.
- Alison Saunders, *The Sixteenth-Century French Emblem Book: A Decorative and Useful Genre* (Geneva: Droz, 1988). Not read.
- Karl A. E. Enenkel, *The Invention of the Emblem Book and the Transmission of Knowledge, ca. 1510–1610* (Leiden: Brill, 2019), <https://brill.com/display/title/35816>. Chapters paywalled; via reviews it covers Steyner's earlier illustrated Schwarzenberg books and *res significantes / res significatae*. Nothing found specific to mismatch.
- Mino Gabriele (ed.), Andrea Alciato, *Il libro degli emblemi secondo le edizioni del 1531 e del 1534* (Milan: Adelphi, 2009), ISBN 9788845924415; via Robohn (pp. xxvi–xxxi) three hypotheses on Alciato's role (own drawings — rejected; delegated illustration; printer's initiative, the 1531 case).
- Anne Rolet and Stéphane Rolet (eds), *André Alciat (1492–1550): un humaniste au confluent des savoirs* (Turnhout: Brepols, 2013); contents via BMCR 2016.09.13 <https://bmcr.brynmawr.edu/2016/2016.09.13> (S. Rolet on the image genealogy of *Virtuti fortuna comes*; Choné on colour; Gabriele on mnemonic visualisation).
- Peter Sharratt, *Bernard Salomon, illustrateur lyonnais* (Geneva: Droz, 2005) [not read].
- **Leaves open.** Case studies and monographs; no cross-edition coding.

### B10. Theory of the impresa and emblem in the period: Giovio, Mignault, Miedema
- **Giovio.** Paolo Giovio, *Dialogo dell'imprese militari et amorose* (Rome: Antonio Barre, 1555) — first edition not seen. Read (sub-pass, OCR) in *Ragionamento di Mons. Paolo Giovio sopra i motti, & disegni d'arme, & d'amore, che communemente chiamano imprese* (Venice: Giordano Ziletti, 1556), pp. 6–7, <https://archive.org/details/ragionamentodimo00giov>: "…bisogna ch'habbia cinque conditioni. Prima, giusta proportione d'anima et di corpo. Seconda, ch'ella non sia oscura … né tanto chiara ch'ogni plebeo l'intenda. Terza, che sopra tutto habbia bella vista … stelle, soli, lune, fuoco, acqua, arbori verdeggianti, instrumenti mecanici, animali bizarri, et uccelli fantastichi. Quarta, non ricerca alcuna forma humana. Quinta, richiede il motto, che è l'anima del corpo, et vuole essere communemente d'una lingua diversa…" Mignault 1577 restates the five rules (A5). Heckscher & Wirth 1959 note that the ban on the human figure had little effect on emblems and that Ripa's personification method partly grew from it.
- **Miedema.** Hessel Miedema, "The Term *Emblema* in Alciati", *Journal of the Warburg and Courtauld Institutes* 31 (1968): 234–250, DOI 10.2307/750643 (record verified; not read). Classic argument that for Alciato *emblema* designated the epigram/ornament, not a picture.
- **Leaves open.** Period rules state the division of labour (picture = body, motto = soul; "neither too obscure nor too clear") but say nothing about which logical contents can be carried by the body. The impresa rule "no human form" is the opposite of Alciato's practice (where most picturae show persons) — a measurable contrast.

### B11. Heckscher & Wirth, "Emblem, Emblembuch" (RDK V, 1959); Henkel & Schöne (1967)
- **References.** William S. Heckscher and Karl-August Wirth, "Emblem, Emblembuch", *Reallexikon zur deutschen Kunstgeschichte* V (1959), cols 85–228, open at <https://www.rdklabor.de/wiki/Emblem,_Emblembuch> (read, sub-pass). Arthur Henkel and Albrecht Schöne (eds), *Emblemata. Handbuch zur Sinnbildkunst des XVI. und XVII. Jahrhunderts* (Stuttgart: Metzler, 1967) (record only).
- **Claims.** "Hatte Alciati die Form des E. vorwiegend zur Verwirklichung literarischer Absichten genutzt, so gewann der Bildbestandteil schon bei seinen unmittelbaren Nachfolgern immer größere Bedeutung"; the 1531 layout "künstlerisch noch wenig befriedigend"; icones may be "abstrakt-phantastische Motivgruppierung[en]".
- **Leaves open.** Encyclopaedic synthesis; no measurement.

### B12. Bässler 2012 and Clement 2019 (see A7, A8); Carlisle 2018; Pilacinski et al. 2026
- Rachel M. Carlisle, "From 'Art of Memory' to Naturalism: Andrea Alciato and the Development of the Early Modern Emblem", *Comitatus* 49 (2018): 165–187, DOI 10.1353/cjm.2018.0006 (record; claim per sub-pass: picturae drift from striking memory images toward naturalism). A *diachronic* claim we can test.
- Artur Pilacinski, Filipa Araújo, Zohar Tal, "Per oculos ad loculos? What can we learn from eye tracking about emblem art perception?", *Eikon / Imago* 15 (2026): e99780, DOI 10.5209/eiko.99780 (record) — the only empirical-perception study of emblems found.

### B13. Analogues in book-illustration studies (Word & Image)
- Ruth Samson Luborsky, "Connections and disconnections between images and texts: the case of secular Tudor book illustration", *Word & Image* 3.1 (1987): 74–85, DOI 10.1080/02666286.1987.10435367 — the closest *methodological* analogue (systematic look at image–text (dis)connection in a printed corpus), not about emblems. Not read.
- Michael Hancher, "Definition and depiction", *Word & Image* 26.3 (2010): 244–272, DOI 10.1080/02666280903270360 — what dictionary pictures can show of a definition; relevant to generic vs particular. Not read.
- Julia Thomas and Irene Testini, "Capturing Captions…", *DHQ* 18.2 (2024) — see F.

## C. Theory: what pictures can and cannot say

Items in C1–C10 were read by the theory sub-pass unless marked; quotes are from the editions named.

### C1. Lessing, *Laokoon* (1766)
- **Reference.** Gotthold Ephraim Lessing, *Laokoon: oder über die Grenzen der Malerei und Poesie* (Berlin, 1766) [place/publisher of the first edition unverified]. Read in German (Project Gutenberg #6889, <https://www.gutenberg.org/ebooks/6889>) and in E. Frothingham's English translation (Boston: Roberts Brothers, 1873; Gutenberg #73078, <https://www.gutenberg.org/ebooks/73078>). Quoted by chapter.
- **Claims.** Ch. XVI: signs side by side can represent only objects side by side ("bodies"), consecutive signs only actions; painting "can imitate actions also, but only as they are suggested through forms", and "must therefore choose the most pregnant [moment] … the one most suggestive of what has gone before and what is to follow" ("den prägnantesten … aus welchem das Vorhergehende und Folgende am begreiflichsten wird"). Ch. III: "that only is fruitful which allows free play to the imagination" ("fruchtbar"; the superlative "fruchtbarste Augenblick" is critics' shorthand, not Lessing's). Ch. X: the poet names a personified abstraction; the artist lacks this means "and must therefore give to his personified abstractions certain symbols by which they may be recognized … A female figure holding a bridle in her hand…"; distinction between merely allegorical and "poetical" (instrumental) attributes. Ch. XII: a painted cloud that makes a hero invisible "is a hieroglyphic, a purely symbolic sign … no better than the rolls of paper with sentences upon them, which issue from the mouth of personages in the old Gothic pictures".
- **Method / quality.** Normative semiotic argument from examples.
- **Leaves open.** Lessing names three of our strategies (pregnant moment for time/causality; attribute for abstraction; "hieroglyph"/scroll for invisibility and speech) but treats them as violations, never counts them. His allegorical vs instrumental attribute distinction can become a coding variable (the bridle of Nemesis in Alciato 27 is exactly his example).

### C2. Goodman, *Languages of Art* (1968)
- **Reference.** Nelson Goodman, *Languages of Art: An Approach to a Theory of Symbols* (Indianapolis: Bobbs-Merrill, 1968), LCCN 68-31825; 2nd ed. Hackett 1976 (pagination said to be identical [unverified]). Read via OCR of the 1968 scan (Monoskop).
- **Claims.** Pictures can denote "distributively eagles in general" (p. 21); "man-picture" (kind of picture) vs picture denoting a man: "Not every man-picture represents a man, and conversely not every picture that represents a man is a man-picture" (p. 26); representation-as, including of a "time-slice" (pp. 27–28); personification as metaphor, "labels are transferred from persons to things" (p. 81). Depiction differs from description "primarily through lack of differentiation—indeed through density (and consequent total absence of articulation)—in the symbol scheme" (p. 226); "every difference in every pictorial respect makes a difference" (p. 227); pictorial symbols are "relatively replete" (pp. 229–230).
- **Caution.** The sub-pass found **no** statement in Goodman that "a picture must be determinate where a description need not be"; do not attribute it to him.
- **Leaves open.** Gives the vocabulary for generic vs particular (denotation vs picture-kind) and for "what images fix" (density/repleteness) — but as properties of symbol schemes, not as an empirical claim about illustration.

### C3. Barthes, "Rhétorique de l'image" (1964)
- **Reference.** Roland Barthes, "Rhétorique de l'image", *Communications* 4 (1964): 40–51, DOI 10.3406/comm.1964.1027, <https://www.persee.fr/doc/comm_0588-8018_1964_num_4_1_1027>.
- **Claims.** Two functions of the linguistic message: "d'ancrage et de relais" (p. 44). "Toute image est polysémique … une « chaîne flottante » de signifiés"; anchorage answers "qu'est-ce que c'est ?" and at the symbolic level "guide … l'interprétation"; "le texte a une valeur répressive" (p. 45). Relay: complementary text and image, unity at the level of the diegesis (p. 45). Drawing, unlike photography, is "un message codé": it forces "un certain partage entre le signifiant et l'insignifiant" (p. 46). Barthes cites Ménestrier, *L'art des emblèmes* (1684), as an early thinker on figure and discourse (p. 42–43, n. 3), and gives a literalised verbal metaphor (coffee aroma "prisonnier" → tin with chain and padlock) (p. 45, n. 1).
- **Leaves open.** Barthes theorises text→image *control*; we study the reverse direction (text → image production) and then test anchorage experimentally with VLMs (image only vs + motto vs + epigram).

### C4. Jakobson, "On linguistic aspects of translation" (1959)
- **Reference.** Roman Jakobson, in Reuben A. Brower (ed.), *On Translation* (Cambridge, MA: Harvard University Press, 1959): 232–239. Scan <https://archive.org/details/OnLinguisticAspectsOfTranslation>.
- **Claims.** "Intersemiotic translation or transmutation is an interpretation of verbal signs by means of signs of nonverbal sign systems" (p. 233); poetry allows only "creative transposition … from verbal art into … painting" (p. 238); "Languages differ essentially in what they must convey and not in what they may convey" (pp. 235–236); Repin "baffled as to why Sin had been depicted as a woman by German artists" because *die Sünde* is feminine (p. 237).
- **Leaves open.** Our object is a documented transmutation chain. The "must convey" principle grounds our second question (the visual medium's obligatory choices: sex, number, pose, moment, setting). The Repin remark yields a crisp test: does the sex of personifications follow Latin grammatical gender across editions?

### C5. Panofsky, "Iconography and Iconology" (1939/1955)
- **Reference.** Erwin Panofsky, "Iconography and Iconology: An Introduction to the Study of Renaissance Art", in *Meaning in the Visual Arts* (Garden City, NY: Doubleday Anchor, 1955): 26–54 (orig. introduction to *Studies in Iconology*, Oxford University Press, 1939).
- **Claims.** Three strata: primary (pre-iconographical description of motifs, events, expressions), secondary/conventional (themes, personifications), intrinsic meaning (pp. 28–29). Personifications/symbols convey "abstract and general notions such as Faith, Luxury, Wisdom" (p. 29 n. 1). Iconographical analysis "presupposes a familiarity with specific themes or concepts as transmitted through literary sources" (p. 35), corrected by "the history of types" (pp. 36–37).
- **Leaves open.** Panofsky makes the text the precondition of iconography; an Alciato edition series *is* a history of types per emblem. His model presupposes that the image renders a text-concept; it does not ask what happens to textual content that has no type (negation, condition).
- **Bridge.** Roelof van Straten, "Panofsky and ICONCLASS", *Artibus et Historiae* 7.13 (1986): 165–181, <https://iconclass.org/z/read/1986_van_straten.pdf> (read in part by sub-pass): Iconclass as the tool for Panofsky's second level, including division 5 "Abstract Ideas and Concepts".

### C6. Shatford (1986) and Shatford Layne (1994)
- **References.** Sara Shatford, "Analyzing the Subject of a Picture: A Theoretical Approach", *Cataloging & Classification Quarterly* 6.3 (1986): 39–62, DOI 10.1300/J104v06n03_04. Sara Shatford Layne, "Some Issues in the Indexing of Images", *JASIS* 45.8 (1994): 583–588, DOI 10.1002/(SICI)1097-4571(199409)45:8<583::AID-ASI13>3.0.CO;2-N. **Primary texts not read** (paywall); content via Tomasz Neugebauer, "Image indexing", *The Indexer* 28.3 (2010): 98–101, <https://www.anzsi.org/wp-content/uploads/2019/05/indexer.2010.28.pdf>, and Hollink et al. 2004 <https://homepages.cwi.nl/~hollink/pubs/Hollink04_coid.pdf>.
- **Claims (second-hand).** Generic Of / Specific Of / About crossed with Who / What / Where / When (a 3×4 matrix); "About" holds abstractions, symbols, moods. When covers "specific dates and periods … and recurring time (Spring, Night)"; its About aspect asks whether time is "a manifestation of an abstract idea? A symbol?" (p. 53) and is, per Neugebauer, rarely used. Panofsky's third level is not intended to be indexed.
- **Leaves open.** The matrix has no slot for logical operators (negation, condition, causality); these fall outside cataloguing altogether — a strong point for our third question. Page-quotes must be checked in the original before citation.

### C7. Mitchell, *Iconology* (1986) and *Picture Theory* (1994)
- **References.** W. J. T. Mitchell, *Iconology: Image, Text, Ideology* (Chicago: University of Chicago Press, 1986); *Picture Theory: Essays on Verbal and Visual Representation* (Chicago, 1994) — only "Ekphrasis and the Other" read (Romantic Circles hypertext).
- **Claims.** *Iconology* (pp. 40–43): Lessing warned that painting expressing universal ideas degenerates into "an arbitrary method of writing"; Mitchell: "A picture may articulate abstract ideas by means of allegorical imagery, a practice which, as Lessing notes, approaches the notational procedures of writing systems", and skepticism "reveals the necessarily verbal character of imaging the invisible". *Picture Theory*: ekphrastic indifference/hope/fear; "The shield is an imagetext". The image/text vs imagetext vs image-text convention (usually cited as p. 89 n. 9) [page unverified].
- **Negation.** No discussion of "pictures cannot say not" found in *Iconology*; *Picture Theory* not fully searched.
- **Leaves open.** Mitchell treats the word/image difference as ideological; an empirical typology can show where the difference behaves like a hard limit (negation, condition) and where like convention (attributes).

### C8. Kress & van Leeuwen, *Reading Images* (1996; 2nd ed. 2006)
- **Reference.** Gunther Kress and Theo van Leeuwen, *Reading Images: The Grammar of Visual Design*, 2nd ed. (London: Routledge, 2006; 1st ed. 1996).
- **Claims.** "Not everything that can be realized in language can also be realized by means of images, or vice versa" (p. 19); narrative (vector) vs conceptual ("timeless essence") representations (p. 59); Symbolic Attributive vs Symbolic Suggestive processes; participants in Symbolic Attributive processes "usually pose for the viewer" (p. 105); modality (p. 155). No explicit treatment of visual negation.
- **Leaves open.** The "not everything" claim is stated, never enumerated; the narrative/conceptual and attributive categories are usable codes.

### C9. Groupe µ (1992) and the semiotics of negation in images
- **References.** Groupe µ (F. Edeline, J.-M. Klinkenberg, Ph. Minguet), *Traité du signe visuel. Pour une rhétorique de l'image* (Paris: Seuil, 1992) — not read. Maria Giulia Dondero, "Énonciation visuelle et négation en image : des arts aux sciences", *Actes Sémiotiques* 114 (2011), DOI 10.25965/as.2578 (read in part). Odile Le Guern, "Image de … Entre individu et catégorie, de la logique à la rhétorique", *Actes Sémiotiques* (2010), DOI 10.25965/as.3087 (read in part).
- **Claims.** Dondero: the image is "positive" (it exemplifies properties) but that "ne revient pas à dire qu'elle est destinée à affirmer ce qu'elle met en scène"; images "moduler le représenté par soustraction, diminution, détournement par rapport à une attente — comme l'a très bien montré la rhétorique visuelle du Groupe µ"; negation works through enunciative/metasemiotic devices. Le Guern: images oscillating between type and token (generic vs particular), citing Gombrich, *L'Art et l'illusion*: a picture "ne saurait donc être vrai ou faux, pas plus qu'une déclaration ne saurait être bleue ou verte".
- **Leaves open.** The strongest counter-position to Worth/Wittgenstein: negation by subtraction or thwarted expectation. Our typology needs a class for it.

### C10. Wittgenstein (1914), Gombrich (1964; 1972), Kjørup (1978)
- **Wittgenstein**, *Tagebücher 1914–1916*, entry 26.11.1914 (German text verified at <https://www.wittgensteinproject.org/w/index.php/Tageb%C3%BCcher_1914-1916>; English ed. *Notebooks 1914–1916*, ed. Anscombe & von Wright, Oxford: Blackwell, 1961, not seen): "Kann man denn ein Bild verneinen? Nein. Und darin liegt der Unterschied zwischen Bild und Satz. Das Bild kann als Satz dienen. Dann tritt aber etwas zu ihm hinzu, was macht, daß es nun etwas sagt."
- **Gombrich**, "The Visual Image", *Scientific American* 227.3 (Sept. 1972): 82–96, DOI 10.1038/scientificamerican0972-82; repr. in *The Image and the Eye* (Oxford: Phaidon, 1982): 137–161. **Primary not read**; quote verified through two independent secondary sources (Woodfield, *Journal of Art Historiography* 5, 2011; Nyíri 2009 talk): the visual image "unaided … altogether lacks the possibility of matching the statement function of language"; correct reading depends on "the code, the caption and the context". Gombrich, "Moment and Movement in Art", *JWCI* 27 (1964): 293–306, DOI 10.2307/750521 (not read; critique of the pregnant moment). Gombrich, "Icones Symbolicae: The Visual Image in Neo-Platonic Thought", *JWCI* 11 (1948): 163–192, DOI 10.2307/750466 (not read; canonical on personification and emblematic images).
- **Kjørup**, "Pictorial Speech Acts", *Erkenntnis* 12.1 (1978): 55–71 [pages unverified], DOI 10.1007/BF00209915 — not read; standardly cited for locating assertion/negation in the *use* of pictures.
- **Leaves open.** All are arguments; none tests the claims on a corpus where the verbal source of each picture is known.

### C11. Worth, "Pictures can't say ain't" (1975) — see also D1
(Original reference found in this step: *Versus* 12 (1975): 85–108; read in the 1981 reprint. Full entry in D1.)

## D. Visual negation, time and condition: philosophy, formal pictorial semantics and experiments

### D1. Worth, "Pictures can't say ain't" — original publication found
- **Reference.** Sol Worth, "Pictures Can't Say Ain't", *Versus. Quaderni di studi semiotici* 12 (1975): 85–108. Reprinted (edited) as ch. 7 of Sol Worth, *Studying Visual Communication*, ed. Larry Gross (Philadelphia: University of Pennsylvania Press, 1981). Source of the original reference: note 1 of the 1981 reprint, "This paper originally appeared in Verses [sic] 12 (1975)-85-108. The paper has been edited…". Reprint read in full: <https://scokobro.gitlab.io/rits/assets/docs/Pictures_Can't_Say_Ain't-WORTH-1981.pdf> (copy of Jay Ruby's web edition, ©1996 Tobia Worth). The 1975 Versus original was **not** seen.
- **Claims.** "Pictures … cannot deal with what is not. That is, they cannot represent, portray, symbolize, say, mean, or indicate things equivalent to what verbal utterances of the type 'This is not a …' or 'It is not the case that …' can do." And: "Pictures … cannot depict conditionals, counterfactuals, negatives, or past-future tenses. Neither can they make passive transformations, ask questions…" "Pictures depict the present even when they depict fantasies…". "A picture cannot comment on itself." Conventional signs such as the red crossbar are "not pictorial uses but rather linguistic uses of visual forms"; negation by omission is "trivial" or works on a "value level".
- **Method.** Philosophical/semiotic argument with ethnographic asides; no systematic data.
- **Relevance.** Worth's list (negation, conditionals, counterfactuals, tense, questions, meta-statements) almost coincides with our candidate categories — he is the canonical source to cite and to test. His "linguistic use of visual forms" is exactly the status of inscriptions and banderoles inside emblem woodcuts (Tung notes 32 emblems with lettering, e.g. the Greek "μηδὲν ἀναβαλλόμενος" banderole in emblem 3).
- **Leaves open.** An *empirical* test on a corpus where we know the verbal source the picture had to translate; and the strategies that pictures actually use instead (contrast, failed action, absence of an expected element, inscription).

### D2. Sato, Mineshima & Ueda 2021 (CogSci, arXiv)
- **Reference.** Yuri Sato, Koji Mineshima, Kazuhiro Ueda, "Visual representation of negation: Real world data analysis on comic image design", *Proceedings of the 43rd Annual Conference of the Cognitive Science Society* (2021): 1166–1172; arXiv:2105.10131. <https://arxiv.org/abs/2105.10131> (read).
- **Claims / method.** NegComic dataset: 111 manga pages judged to express negation (Manga109 + award-winning works), split into *existence negation* (¬∃xPx: empty, disappeared, absent; 87 images) and *property negation* (¬Pc: cannot move, not green; 24 images). Caption task with 459 Japanese crowd-workers, six ablation conditions (sequence vs single panel; with/without conventional devices such as radial lines, crosses, blank balloons). People produced significantly more negation phrases than baseline for 56.3% of existence-negation and 33.3% of property-negation images; **17 images conveyed negation "by means of pure visual elements"** (single panel, no devices), 34 needed the sequence. CNN classifiers far below humans. Interpretation: pictures evoke background knowledge (an expected presence) against which absence is read.
- **Evidence quality.** Solid design for its question (ablation, baseline, Fisher tests, Bonferroni); lexicon-based negation detection; Japanese manga only.
- **Leaves open for us.** Their three vehicles (sequence, conventional device, pure depiction + background knowledge) map onto emblem woodcuts, which are single panels (though often with simultaneous narrative), have few conventional devices (inscriptions, rays from clouds), and rely heavily on background knowledge (the reader has the epigram). Their existence/property split is a candidate sub-scheme for our negation category.

### D3. Sato, Mineshima & Ueda 2023 (Cognitive Science)
- **Reference.** "Can Negation Be Depicted? Comparing Human and Machine Understanding of Visual Representations", *Cognitive Science* 47(3) (2023): e13258. DOI 10.1111/cogs.13258; PMID 36960848. Open access (CC BY-NC-ND) per Unpaywall, but the PDF was blocked to our client (403); **abstract only read**.
- **Claims (abstract).** Photographs and manga; human captions show that some images are recognised as expressing negation; humans classify novel images "to some extent"; the image-processing model performs "at about the chance level"; the difference is attributed to "background commonsense knowledge".
- **Leaves open.** Models tested are pre-VLM vision models (per abstract "machine learning model of image processing"); whether current VLMs read negation in *historical allegorical* pictures, and whether text supplied alongside changes this, is untested.

### D4. Oversteegen & Schilperoord 2014
- **Reference.** Eleonore Oversteegen, Joost Schilperoord, "Can pictures say no or not? Negation and denial in the visual mode", *Journal of Pragmatics* 67 (2014): 89–106. DOI 10.1016/j.pragma.2014.03.009. Tilburg repository record (PDF listed, blocked to our client): <https://research.tilburguniversity.edu/en/publications/can-pictures-say-no-or-not-negation-and-denial-in-the-visual-mode/>.
- **Claims (abstract/record and search summaries only).** Yes, pictures can say "no": analysis of advertisements plus a pilot study in which elements were *erased* from advertising photographs; "under certain conditions in the visual mode, removal is interpreted as negation".
- **Evidence quality.** Not read in full → treat details as provisional.
- **Leaves open.** Advertising is designed for one reading; our corpus lets us see the *same* negated sentence rendered by several illustrators.

### D5. Giora, Heruti, Metuki & Fein 2009
- **Reference.** Rachel Giora, Vered Heruti, Nili Metuki, Ofer Fein, "'When we say no we mean no': Interpreting negation in vision and language", *Journal of Pragmatics* 41(11) (2009): 2222–2239. DOI 10.1016/j.pragma.2008.09.041 (DOI resolves to Elsevier record; paywalled; not read).
- **Claims (secondary: Sato et al. 2021 and search summaries).** Discusses interpretations of conventional visual negation devices (crosses, bars) and argues visually negated information remains accessible depending on discourse goals — negation does not suppress the negated concept.
- **Leaves open.** Relevant to the illustrator's dilemma: to negate *X* one must draw *X*. [details unverified]


D6–D17 were read (or not) by the pictorial-semantics sub-pass, as marked.

### D6. Greenberg — formal pictorial semantics
- **References (author PDFs read).** Gabriel Greenberg, "Beyond Resemblance", *Philosophical Review* 122.2 (2013): 215–287, DOI 10.1215/00318108-1963716; "Content and Target in Pictorial Representation", *Ergo* 5.33 (2018): 865–898, DOI 10.3998/ergo.12405314.0005.033; "Tagging: Semantics at the Iconic/Symbolic Interface", *Proceedings of the 22nd Amsterdam Colloquium* (2019): 11–20; "Semantics of Pictorial Space", *Review of Philosophy and Psychology* 12 (2021): 847–887, DOI 10.1007/s13164-020-00513-6; "The Iconic-Symbolic Spectrum", *Philosophical Review* 132.4 (2023): 579–627, DOI 10.1215/00318108-10697558; "Iconic Representation", *MIT Open Encyclopedia of Cognitive Science* (forthcoming), <https://www.gabrielgreenberg.com/docs/mit-iconicity.pdf>; Valeria Giardino & Gabriel Greenberg, "Introduction: Varieties of Iconicity", *RPP* 6 (2015): 1–25, DOI 10.1007/s13164-014-0210-7.
- **Claims.** Pictorial content = a set of world–viewpoint pairs fixed by projection; "pictorial spaces are always partly indeterminate — if nothing else, they are silent with respect to occluded objects, and objects outside the window of the picture plane" (2021). A black-and-white drawing "is wholly indeterminate with respect to color" (2013). Counterfactual and generic pictures have non-factual or kind targets; genericity lies "in the selection of target, rather than in their content" (2018). Key quote (2018): a picture made from an open-ended description "could be quite specific — showing one way the house might look if the modifications were made — even though the preceding discussion may have been comparatively open-ended". "Semantic holism": a drawing that represents shape "must also make a commitment about the location of that object". *Tagging*: icon-dominant multimodal signs in which "words, phrases, and non-linguistic symbols are used to enrich a picture"; speech balloons are "a genre-specific form [of] tagging".
- **On negation.** Greenberg's texts do not treat it; Giardino & Greenberg (2015) only report "the apparent impossibility of expressing negation by pictorial means" as a common objection.
- **Leaves open.** (i) A formal home for "images fix what texts leave open": the text as a description selecting a target set; each woodcut as one over-specific member. Our corpus can test whether the dimensions that vary across editions are exactly those the text leaves open. (ii) Generic vs particular is *not* visible in the picture — so any recovery of it by catalogue or VLM must come from the text. (iii) Inscriptions/banderoles in woodcuts are "tags".

### D7. Abusch; Abusch & Rooth — time, existentials, over-specificity
- **References (read).** Dorit Abusch, "Applying Discourse Semantics and Pragmatics to Co-reference in Picture Sequences", *Proceedings of Sinn und Bedeutung 17* (2013): 9–25; "Possible-Worlds Semantics for Pictures", in *The Wiley Blackwell Companion to Semantics* (2020), DOI 10.1002/9781118788516.sem003 (author's version); Dorit Abusch & Mats Rooth, "Temporal and Intensional Pictorial Conflation", *Proceedings of SuB 26* (2022): 1–19, DOI 10.18148/sub/2022.v26i0.981; "Parallel and Differential Contributions from Language and Image in the Discourse Representation of Picturebooks", *SuB 27* (2023) [pages unverified]. Abusch 2014 (MITWPL 70: 9–29) cited only [unverified].
- **Claims.** "Depicted objects are existentially quantified" (2013). "All semantic contents for pictures come out as stative" (2020). Temporal order in sequences is a discourse default; causal links between panels are inferred, not depicted. *Temporal conflation*: "a single picture combining information from two or more time points" (Masaccio's *Tribute Money*); *intensional conflation*: character plus hallucination. Over-specificity: "a fundamental mismatch between the relatively weak informational content of events of imagining or dreaming, the strong informational content of film shots and realistic pictures, and a semantics for attitudinal constructions requiring entailment. We propose … replacing entailment with compatibility" (2022). Picturebooks (2023): text and image combine conjunctively; linguistic content generates implicatures, pictorial content does not — not depicting the fox yields no "no fox" implicature.
- **Leaves open.** Best formal statement of our second question (text→image as *compatibility*, not entailment) and a prediction for the first: an absence in a woodcut cannot carry negation unless the text sets up the expectation. Conflation is the formal name for continuous narration in emblem picturae (e.g. Alciato 90, Arion: Tung notes "a prior action scene" in the foreground). No early-modern corpus.

### D8. Maier; Maier & Bimpikou — speech, thought, perspective
- **References (read).** Emar Maier, "Picturing Words: The Semantics of Speech Balloons", *Proceedings of the 22nd Amsterdam Colloquium* (2019): 584–592, <https://ling.auf.net/lingbuzz/004938>; Emar Maier & Sofia Bimpikou, "Shifting Perspectives in Pictorial Narratives", *Proceedings of SuB 23*, vol. 2 (2019): 91–105.
- **Claims.** Balloons, motion lines and affixes are "conventional indicators of certain types of events or (mental) states", interpreted symbolically and attached to a discourse referent; speech balloons as quotational event modification. Single images can "depict the perceiving, dreaming or hallucinating character … alongside the contents of their subjective experience" (examples include Bol's *Jacob's Dream*, 1642, and Pereda's *The Knight's Dream*, 1650).
- **Caution.** The formula "pictorial content is not closed under negation" was **not** found in Maier [unverified as his].
- **Leaves open.** Speech is the best-theorised "undrawable"; emblem woodcuts use gesture (finger to lips, *Silentium*, Alciato 11), banderoles (Alciato 3, 134) and inscriptions. Negation, condition and abstraction are untreated.

### D9. Schlenker and "super semantics"
- **References.** Philippe Schlenker, "What is Super Semantics?", *Philosophical Perspectives* 32 (2018): 365–453, DOI 10.1111/phpe.12122 (read in part); Pritty Patel-Grosz, Salvador Mascarenhas, Emmanuel Chemla & Philippe Schlenker, "Super Linguistics: An Introduction", *Linguistics and Philosophy* 46.4 (2023): 627–692, DOI 10.1007/s10988-022-09377-8 (grepped); Schlenker & Jonathan Lamberton, "Iconological Semantics", *Linguistics and Philosophy* 47 (2024): 779–838, DOI 10.1007/s10988-024-09411-x (abstract).
- **Claims.** "Pro-speech pictures" embedded in language ("If at the end of the story [picture], …"): the conditional comes from language, the picture is an iconic constituent. Iconic content tends to project out of logical operators (cosuppositions of co-speech gestures under negation). Iconological semantics combines logical semantics with Greenberg/Abusch pictorial semantics.
- **Leaves open.** Gives the architecture *motto/epigram (logical frame) + pictura (iconic constituent)*; predicts that conditionals and negations in an epigram cannot be carried by the picture alone but can scope over it.

### D10. Cohn — visual language of comics
- **References.** Neil Cohn, *The Visual Language of Comics* (London: Bloomsbury, 2013), DOI 10.5040/9781472542175 (not read); "The Limits of Time and Transitions", *Studies in Comics* 1.1 (2010): 127–147, DOI 10.1386/stic.1.1.127/1 (read); Cohn, Murthy & Foulsham, "Meaning above the Head", *Journal of Cognitive Psychology* 28.5 (2016): 559–574, DOI 10.1080/20445911.2016.1179314; "Combinatorial Morphology in Visual Languages", in G. Booij (ed.), *The Construction of Words* (Springer, 2018): 175–199, DOI 10.1007/978-3-319-74394-3_7 (read); Irmak Hacımusaoğlu & Neil Cohn, "The Meaning of Motion Lines?", *Cognitive Science* 47.11 (2023): e13377, DOI 10.1111/cogs.13377 (abstract).
- **Claims.** A panel can contain duration; visual morphology: affixes, "upfixes", suppletion, reduplication, learned by convention; motion lines are "graphical conventions indexing conceptual path information, which need to be learned". No paper on negation found.
- **Leaves open.** A model for coding conventional emblem signs (attributes, rays from clouds, hands from clouds) as learned "visual morphemes" — the same kind of thing Iconclass codes.

### D11. Grzankowski (2015), Crane (2009) and the philosophical negation debate
- **References.** Alex Grzankowski, "Pictures Have Propositional Content", *RPP* 6 (2015): 151–163, DOI 10.1007/s13164-014-0217-0 (read). Tim Crane, "Is Perception a Propositional Attitude?", *Philosophical Quarterly* 59.236 (2009): 452–469, DOI 10.1111/j.1467-9213.2008.608.x (quoted via Grzankowski).
- **Claims.** Crane: "there is no way of simply using a picture alone to deny what it represents"; Sainsbury: "There is no such thing as the negation of a picture"; Heck: no map is the negation or disjunction of another. Grzankowski concedes "one cannot, via depiction alone, express (say) a negated proposition", cites Schier: one can "at most indirectly represent something as not having some color by directly depicting it as having some other color", and finds it "strained" to depict "there are no unicorns" by leaving them out.
- **Leaves open.** Schier's "depict the contrary" is a precise, codable strategy.

### D12. Kaup, Lüdtke & Zwaan (2006); Orenes (2021) — negation is simulated through the alternative
- **References.** Barbara Kaup, Jana Lüdtke, Rolf A. Zwaan, "Processing Negated Sentences with Contradictory Predicates: Is a Door That Is Not Open Mentally Closed?", *Journal of Pragmatics* 38.7 (2006): 1033–1050, DOI 10.1016/j.pragma.2005.09.012 (not read; via Orenes and Xu et al.). Isabel Orenes, "'Looking at' Negation: Faster Processing for Symbolic Rather Than Iconic Representations", *Journal of Psycholinguistic Research* 50.6 (2021): 1417–1436, DOI 10.1007/s10936-021-09797-w, open at <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8660733/> (read by sub-pass).
- **Claims.** Readers of "the door was not open" first represent the negated state, then the actual one (two-step simulation). Orenes (visual-world eye-tracking, Spanish): negation is represented either symbolically ("no salad") or iconically by the alternative ("soup"); binary predicates favour the iconic alternative, multi-valued predicates favour symbolic plus iconic.
- **Leaves open.** Directly yields two codes (symbolic marker vs drawing the alternative) and a *predictor* (binary vs multi-valued predicate) of which an illustrator will choose — testable on epigram negations.

### D13. van Miltenburg, Morante & Elliott (2016)
- **Reference.** Emiel van Miltenburg, Roser Morante, Desmond Elliott, "Pragmatic Factors in Image Description: The Case of Negations", *Proceedings of the 5th Workshop on Vision and Language* (2016): 54–59, DOI 10.18653/v1/W16-3207, arXiv:1606.06164 (read by sub-pass).
- **Claims.** Negations in 0.56% (Flickr30K) and 0.54% (COCO) of human captions; mostly one annotator in five; categories (κ = 0.67): salient absence (488/892), negation of action/behaviour, attitude, outside the frame, property, (preventing) future events…; negation is used when what is shown mismatches expectation.
- **Leaves open.** A ready-made coding scheme for *descriptions* (human and VLM) of emblem woodcuts; prediction: describers negate only where an expectation is violated.

### D14. Tversky (2011); Heiser & Tversky (2006)
- **References.** Barbara Tversky, "Visualizing Thought", *Topics in Cognitive Science* 3 (2011): 499–535, DOI 10.1111/j.1756-8765.2010.01113.x (read by sub-pass); Julie Heiser & Barbara Tversky, "Arrows in Comprehending and Producing Mechanical Diagrams", *Cognitive Science* 30.3 (2006): 581–592, DOI 10.1207/s15516709cog0000_70 (via Tversky 2011).
- **Claims.** "abstract or invisible concepts like forces, traits, counterfactuals, and negations are not easily conveyed unambiguously in depictions. Even so, conventions for conveying these kinds of concepts have evolved as needed … a gradual process of symbolization akin to language." Arrows elicit causal/functional descriptions.
- **Leaves open.** The "gradual symbolization" claim is diachronic and testable on 1531→1621 picturae.

### D15. Phillips & McQuarrie (2004); Forceville
- **References.** Barbara J. Phillips & Edward F. McQuarrie, "Beyond Visual Metaphor: A New Typology of Visual Rhetoric in Advertising", *Marketing Theory* 4.1–2 (2004): 113–136, DOI 10.1177/1470593104044089 (abstract; grid via secondary sources). Charles Forceville, *Pictorial Metaphor in Advertising* (London: Routledge, 1996), DOI 10.4324/9780203272305; "Pictorial Runes in *Tintin and the Picaros*", *Journal of Pragmatics* 43.3 (2011): 875–890, DOI 10.1016/j.pragma.2010.07.014 (not read).
- **Claims.** 3 × 3 typology: visual structure (juxtaposition, fusion, replacement) × meaning operation (connection, comparison for similarity, comparison for opposition).
- **Leaves open.** An existing, tested typology of *rendering strategies* for designed images — a model for the form (not the content) of our scheme; "comparison for opposition" is a rhetorical route to negation.

### D16. Visual argument and pictorial assertion
- David Fleming, "Can Pictures Be Arguments?", *Argumentation and Advocacy* 33 (1996): 11–22 [unverified; quoted via Tseronis]: a picture "is therefore less available for opposition than language".
- Assimakis Tseronis, "Argumentative Functions of Visuals: Beyond Claiming and Justifying", OSSA 10 (2013), <https://pure.uva.nl/ws/files/1688427/147415_Argumentative_functions_of_visuals_Beyond_claiming_and_justifying.pdf> (read).
- David Novitz, *Pictures and their Use in Communication* (The Hague: Nijhoff, 1977), DOI 10.1007/978-94-010-1063-4 (not read).
- Lukas Lewerentz & Emanuel Viebahn, "Truth and Directness in Pictorial Assertion", *Linguistics and Philosophy* 46.6 (2023): 1441–1465, DOI 10.1007/s10988-023-09392-3 (abstract): pictorial assertions can be indirect in content and target — fits an emblem picture that "asserts" a moral through a scene.
- Maria Esipova, "On Not-at-Issueness in Pictures", *Glossa* 6.1 (2021): 83, DOI 10.5334/gjgl.1314 (abstract; prohibition signs).
- **Leaves open.** Content-vs-use is the right frame for the emblem (the motto supplies the force); none studies historical material.

### D17. Further Sato et al. items and stage- vs individual-level content
- Yuri Sato & Koji Mineshima, "Depicting Negative Information in Photographs, Videos, and Comics: A Preliminary Analysis", *Diagrams 2020*, LNCS 12169: 485–489, DOI 10.1007/978-3-030-54249-8_40; "Can Humans and Machines Classify Photographs as Depicting Negation?", *Diagrams 2021*, LNCS 12909: 348–352, DOI 10.1007/978-3-030-86062-2_35; "Can Machines and Humans Use Negation When Describing Images?", *HAR 2023*, LNCS 14522 (2024): 39–47, DOI 10.1007/978-3-031-55245-8_3 (search abstract only: a captioning model negated less proficiently than humans). None read.
- Yuri Sato, Ayaka Suzuki, Koji Mineshima, "Capturing Stage-Level and Individual-Level Information from Photographs: Human-AI Comparison", *CogSci 2024*: 803–810, <https://escholarship.org/uc/item/00b1f88b> (read by sub-pass): stage-level predicates dominate captions; a CNN handles individual-level (permanent) predicates near chance — relevant to generic/permanent ("the envious man") vs episodic readings of emblem pictures.

## E. Cataloguing emblems: Iconclass, schemas, and the role of the text

### E1. Brandhorst, "Using Iconclass for the Iconographic Indexing of Emblems" (2004) — the text is built into the index
- **Reference.** Hans Brandhorst, in Mara R. Wade (ed.), *Digital Collections and the Management of Knowledge: Renaissance Emblem Literature as a Case Study for the Digitization of Rare Texts and Images* (Salzburg: DigiCULT, 2004): 29–43, <https://www.salzburgresearch.at/wp-content/uploads/2010/10/dc_emblemsbook_lowres.pdf> (read by two sub-passes).
- **Claims.** Under "WYSIWYK: What you see is what you know": the motto, epigram and commentary "quite literally tell us what we are looking at. Without textual information we would often be clueless and unable to provide a correct description of the picture" (examples: Sertorius and the horse's tail; the crane "Pro Grege"). Re-used picturae may need different descriptions.
- **Consequence for us.** Iconclass "image" notations on emblems are **not** an image-only ground truth: the indexer saw the text. Glasgow's split image/text is a cataloguer's judgement of *what is visible given the text*. Any comparison with VLMs must treat it as such (and ideally add a blind, image-only human annotation).

### E2. Rawles, "A Spine of Information Headings" (2004)
- **Reference.** Stephen Rawles, in Wade (ed.) 2004: 19–28 (same PDF; not read in detail).
- **Claim.** A shared set of headings for emblem resources (basis of OpenEmblem / Emblematica Online interoperability).
- **Leaves open.** Descriptive metadata only.

### E3. EMLS Special Issue 20 (2012): Stäcker; Kilton; Graham
- **References (read by computing sub-pass).** Thomas Stäcker, "Practical Issues of the Wolfenbüttel Emblem Schema", *Early Modern Literary Studies* Special Issue 20 (2012): 7, <http://purl.oclc.org/emls/si-20/WADE_Staecker_EMLS_Schema.htm>; Thomas Kilton, "Subject Access Through an Emblem Portal: A Common Standard for Students and Scholars", *EMLS* SI 20 (2012): 5, <http://purl.oclc.org/emls/si-20/WADE_Kilton_EMLS.htm>; David Graham, "'Corpus Electronicum Cano': Some Implications of Very Large Electronic Emblem Corpora", *EMLS* SI 20 (2012): 4, <http://purl.oclc.org/emls/si-20/WADE_GRAHAM_EMLS.htm>.
- **Claims.** Stäcker: Iconclass elements sit inside `emblem:pictura` in the schema (even a biblical-text notation); "It is an act of interpretation rather than description to constitute an emblem." Kilton (three spider emblems): motto, pictura descriptors and topoi "are not sufficient to convey the true meaning of an emblem if the subscriptio cannot be understood." Graham: Iconclass is used at Glasgow and in Emblematica Online "for both visual and textual motif tagging"; reports Peter Daly's objection that Iconclass, built for art history, may not suit emblem books.
- **Leaves open.** Qualitative; nobody quantifies what falls only under "text".

### E4. Cole, Han & Vannoy (2012)
- **Reference.** Timothy W. Cole, Myung-Ja K. Han, Jordan A. Vannoy, "Descriptive metadata, Iconclass, and digitized emblem literature", *Proceedings of JCDL 2012*: 111–120, DOI 10.1145/2232817.2232839 (record only).
- **Leaves open.** To read: may contain quantitative data on Iconclass use in Emblematica Online.

### E5. Boot, *Mesotext* (2009); Leal & Wade (2022)
- Peter Boot, *Mesotext: Digitised Emblems, Modelled Annotations and Humanities Scholarship* (Amsterdam: Amsterdam University Press, 2009), ISBN 9789085550525 (not read). Peter Boot, "What is Next in Digital Emblem Studies?", in L. Grove & A. Saunders (eds), *Transmigrations* (Glasgow Emblem Studies 14; Geneva: Droz) [year unverified], proofs <http://peterboot.nl/pub/Boot_WhatsNext.pdf> (read): an agenda without computer vision.
- Pedro Germano Leal & Mara R. Wade, "Introduction: Digital Emblematica", *Renaissance and Reformation / Early Modern Digital Review* 45.3 (2022): 215–223, DOI 10.33137/rr.v45i3.40432 (intro read): reviews emblem websites; mentions IIIF; no CV/ML/AI.

### E6. Glasgow's Iconclass split as data (our observation; see A3)
- Seen on [A50a059](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A50a059) (*Impossibile*: "Impossibility" only under text) and, by the computing sub-pass, on [A31a017](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A31a017) (*In Occasionem*: 54B121 Occasio both "(+11)" and "(+4)" under *image*, plus razor, baldness, globe). So a personification with its attributes is coded as visible, while futility/impossibility is coded as textual — exactly the boundary our first question is about. **No publication analyses this split.**

## F. Computing: Iconclass and AI, vision-language models, negation, emblems

### F1. Brandhorst 2025, "The elephant in the room" (read in full)
- **Reference.** Hans Brandhorst, "The elephant in the room: Iconography, Iconclass and Artificial Intelligence", essay dated Voorschoten, 19 Aug. 2025 (annotated version of a talk at the 13th SES conference, Vienna, July 2025); PDF <https://iconclass.org/z/read/2025_elephant_in_the_room.pdf>; slides <https://iconclass.org/z/read/2025_ses_elephantroompresentation.pdf>; announced on the Iconclass forum as due to appear in *Emblematica* <https://forum.iconclass.org/t/working-with-the-elephant/339>. Journal publication not verified.
- **Method.** Qualitative probing of ChatGPT‑4o (July 2025) with the prompt "tag with Iconclass and interpret" on: two lion emblems from Zincgref 1619; one from *Emblémes ou devises chrétiennes* (Utrecht 1697, text across two pages); a batch of eight Rollenhagen emblems (Glasgow SM 919 copy with Stirling Maxwell's manuscript notes), compared with Henkel–Schöne and Warncke; repeated runs on two of them. 11 emblems in total, no Alciato.
- **Findings.** (1) Interpretations correct and fast (~15 s) when motto and verse are visible — "clearly based on both the emblem's picturae and their textual elements". (2) Every suggested Iconclass notation was hallucinated (e.g. "25F4 lion", real 25F4 = reptiles), "curiously consistent in their errors". (3) Pictorial descriptions mix correct, misinterpreted and omitted elements; "strategic vagueness" for backgrounds. (4) Key case for us — *Ne quid nimis*: the model describes the woman pouring "carefully", but she "expresses this concept by **not** being careful as she causes the dish to overflow" — i.e. the picture renders the injunction by showing its violation, and the model substitutes the textual moral for what is drawn. Same in *Noli altum sapere* (model "sees" a man plucking fruit, which he does not; misreads the wind-face as divine). (5) Handwritten notes "read" by the model are probably recalled from Wither 1635 online, not transcribed.
- **Evidence quality.** Expert, candid, anecdotal (n≈11, one model, no controls, no image-only condition).
- **Leaves open for us.** Exactly the controlled version: same emblems, image-only vs +motto vs +epigram; Alciato corpus; human reference; measure *which* textual contents leak into descriptions and *which* visible contents are suppressed. Brandhorst's *Ne quid nimis* is a published instance of "negation rendered by depicting the transgression" — and of a model overwriting it with the text.

### F2. Alhamoud et al. 2025, NegBench
- **Reference.** Kumail Alhamoud, Shaden Alshammari, Yonglong Tian, Guohao Li, Philip H. S. Torr, Yoon Kim, Marzyeh Ghassemi, "Vision-Language Models Do Not Understand Negation", CVPR 2025. DOI 10.1109/CVPR52734.2025.02757; arXiv:2501.09425 (abstract read by me; full paper read by the computing sub-pass).
- **Claims.** NegBench: 18 task variations, 79k examples (image, video, medical); retrieval with negation and MCQ with negated captions; "modern VLMs struggle significantly with negation, often performing at chance level"; fine-tuning CLIP on synthetic negated captions gives +10% recall, +28% MCQ accuracy.
- **Details (sub-pass).** Templates "includes A" / "does not include B" / "A but not B"; CLIP-family models near chance on 4-way MCQ; CLIP 82% on affirmation MCQs vs **3%** on negation MCQs (VOC2007); an **affirmation bias** ("a dog" and "no dog" collapse in embedding space; models pick captions that negate objects actually present); scaling and NegCLIP/ConCLIP do not fix it; LLaVA-type models with LLM text encoders do better.
- **Leaves open.** Negation *in the query*, about *photographs*; not negation *depicted* by an image, and not historical/allegorical imagery. The affirmation bias predicts that a VLM given an epigram "do not X" will report X as depicted — the Brandhorst *Ne quid nimis* pattern.

### F3. He 2026, DIVA / Semantic Alignment Gap
- **Reference.** Wei He (University of Exeter), "More Than Meets the Eye: Measuring the Semiotic Gap in Vision-Language Models via Semantic Anchorage", arXiv:2604.17354 (19 Apr 2026), accepted to ACL 2026 main conference (per arXiv comment). <https://arxiv.org/abs/2604.17354> (abstract read).
- **Claims.** DIVA benchmark of paired schematic visualisations of literal vs idiomatic readings of noun compounds; metric Δ (Semantic Alignment Gap) and signed bias b(t); across 8 VLMs a "Literal Superiority Bias"; "increased visual fidelity is associated with weaker symbolic alignment".
- **Details (sub-pass, full text).** DIVA built from the 100 noun compounds of SemEval-2025 AdMIRe; high-fidelity images redrawn as flat "iconographic" renderings by an image model; 1,000 images; Δ computed via embeddings (SigLIP 2, EVA-CLIP, MetaCLIP 2), token likelihoods (Qwen2.5-VL, InternVL3, LLaVA-OneVision) and self-reported confidence (GPT-5, Claude Sonnet 4.5); moving photo → icon lowers Δ in every family; human Δ study (3 annotators, κ = 0.76). Author's own caveat: style confound.
- **Leaves open.** Synthetic images; idioms not emblems; but the literal-vs-figurative axis is the emblem's axis (res picta vs significatio), and "schematic iconicity" resembles woodcut style — a hypothesis we could test.


F4–F16 were located and (where marked) read by the computing sub-pass.

### F4. Brandhorst, "A word is worth a thousand pictures" (2019/2020) — machine "seeing" is harvested text
- **Reference.** Hans Brandhorst, "A word is worth a thousand pictures. Why the use of Iconclass will make Artificial Intelligence smarter" (signed Voorschoten, Oct. 2019; PDF dated Feb. 2020), <https://iconclass.org/testset/ICONCLASS_and_AI.pdf> (read). Related slides: Brandhorst, DCMI 2021 panel, <https://www.dublincore.org/conferences/2021/presentations/why_ai__automated_indexing_what_is_and_is_not_possible/slides/hans_brandhorst.pdf>.
- **Claims.** Google Cloud Vision's "web entities" for a Heinsius *Omnia vincit Amor* emblem begin with a Spanish translation of the motto "which the image does not contain", plus Hercules, Aphrodite, Heinsius, Alciato — "not properties of this particular emblem, let alone visual properties": a visual match followed by text harvested from pages around the copy. Without an online copy (a Solis Hercules and the Nemean lion), output is "Person" — "the lion remains undetected". A walnut emblem retrieved for "embracing" though "there is no embrace in sight".
- **Method / quality.** Anecdotal, precise diagnosis.
- **Leaves open.** A controlled test of *text leakage*: picturae whose copies are online vs held out; image-only vs + motto vs + epigram.

### F5. Brill Iconclass AI Test Set (Posthumus 2020) — labels mix picture and text
- **Reference.** Etienne Posthumus, *Brill Iconclass AI Test Set* (2020), CC0, 87,749 images, <https://iconclass.org/testset/>; HF mirror <https://huggingface.co/datasets/biglam/brill_iconclass> (dataset card read).
- **Claims.** Sampled from Arkyves partners (Rijksmuseum, RKD, HAB Wolfenbüttel, Utrecht, Milan, **Glasgow** emblem collections); inherited catalogue labels; notations attached to whole images.
- **Sub-pass spot-check (non-random, indicative only).** In 500 rows (5 blocks of 100), 34 carry an `86(...)` notation (Iconclass 86 = proverbs, sayings) whose bracket is the *motto text* (e.g. `86(IN ASSENTATORES)` with `86(CONTRA GLI ADULATORI)` — an Alciato motto), and 13 carry division-5 codes with `(+4)` "emblematical representation of concept".
- **Leaves open.** Image-only models trained/evaluated on this set are partly scored on non-visible, text-derived labels; no paper discusses this. (Our own check would need a proper random sample — S2/S6.)

### F6. Posthumus, Brandhorst & Sack (2022); Santini et al. (2023)
- **References.** Etienne Posthumus, Hans Brandhorst, Harald Sack, "The Art Historian's Bicycle Becomes an E-Bike", VISART VI @ ECCV 2022, DOI 10.5281/zenodo.7225425 (read). Cristian Santini, Etienne Posthumus, Mary Ann Tan, Oleksandra Bruns, Tabea Tietz, Harald Sack, "Multimodal Search on Iconclass using Vision-Language Pre-Trained Models", *JCDL 2023*: 285–287, DOI 10.1109/JCDL57899.2023.00061, arXiv:2306.16529 (read).
- **Claims.** E-Bike: CLIP k-NN over 531,172 Arkyves images; notation suggestion from neighbours; micro-F1 0.29, macro-F1 0.18 on a 10k sample (4,341 classes); Panofsky's pre-iconographic level as "a 'natural' starting point for pattern matching software". Santini: CLIP + Faiss retrieval of notations; preference survey with 10 volunteers (multimodal 105 vs TF-IDF 104 preferences); quality "still to be adequately estimated by using objective ground-truths".
- **Evidence quality.** Workshop/demo papers; weak evaluation; no breakdown by Iconclass division.
- **Leaves open.** Whether division 5 (abstract concepts) and "(+4) emblematical" codes are retrievable from pixels — untested.

### F7. Banar, Daelemans & Kestemont (2021; 2023)
- **References.** Nikolay Banar, Walter Daelemans, Mike Kestemont, "Multi-modal Label Retrieval for the Visual Arts: The Case of Iconclass", *ICAART 2021*: 622–629, DOI 10.5220/0010390606220629 (read); "Transfer Learning for the Visual Arts: The Multi-modal Retrieval of Iconclass Codes", *JOCCH* 16.2 (2023): 1–16, DOI 10.1145/3575865 (abstract).
- **Claims.** On 26,725 RKD artworks, "in isolation, textual features [titles] strongly outperform visual features"; combination best; fine-tuned multimodal retrieval improves; out-of-domain poor.
- **Leaves open.** No breakdown by *kind* of concept (what titles supply that pixels cannot).

### F8. Cetinic (2021a, 2021b); Cetinic & She (2022)
- **References.** Eva Cetinic, "Iconographic Image Captioning for Artworks", in *Pattern Recognition. ICPR International Workshops and Challenges* (FAPER 2020), LNCS 12663 (2021), DOI 10.1007/978-3-030-68796-0_36, arXiv:2102.03942 (read); Cetinic, "Towards Generating and Evaluating Iconographic Image Captions of Artworks", *Journal of Imaging* 7.8 (2021): 123, DOI 10.3390/jimaging7080123 (abstract); Eva Cetinic & James She, "Understanding and Creating Art with AI: Review and Outlook", *ACM TOMM* 18.2 (2022): 1–22, DOI 10.1145/3475799 (abstract).
- **Claims.** Converts the Iconclass test set into image–caption pairs and fine-tunes a VLP model; standard captioning metrics "are not very informative"; captions are iconographic labels rather than descriptions.
- **Leaves open.** No analysis of abstract or text-derived labels.

### F9. Milani & Fraternali (2021); Spinaci, Klic & Colavizza (2025)
- **References.** Federico Milani & Piero Fraternali, "A Dataset and a Convolutional Model for Iconography Classification in Paintings", *JOCCH* 14.4 (2021): 1–18, DOI 10.1145/3458885 (abstract). Gianmarco Spinaci, Lukas Klic, Giovanni Colavizza, "Benchmarking Multimodal Large Language Models in Zero-shot and Few-shot Scenarios: Preliminary Results on Studying Christian Iconography", *Computational Humanities Research 2025* (Anthology of Computers and the Humanities 3): 1197–1209, arXiv:2509.18839 (read).
- **Claims.** Saint identification by attributes: CNN ≈ 71% (ArtDL); on Iconclass test-set saints Gemini-2.5-Pro 83–85%, GPT-4o ≈ 75%, CLIP 24–43%; adding Iconclass descriptions to prompts helps CLIP/SigLIP.
- **Leaves open.** Only *particular* figures recognised by attributes — the easiest iconography; nothing on abstraction, negation, generic reference.

### F10. Thomas (2025/2026); Thomas & Hintersteiner (2026) — the only image-only vs image+text comparison on early-modern woodcuts
- **References.** Drew B. Thomas, "Automating Iconclass: LLMs and RAG for Large-Scale Classification of Religious Woodcuts", arXiv:2510.19986 (read); journal version *Digital Culture and Education* 16.3 (2026): 161–182 (not seen). Drew B. Thomas & Julia Hintersteiner, "Transferring AI-Based Iconclass Classification Across Image Traditions: A RAG Pipeline for the Wenzelsbibel", *Histories* 6.1 (2026): 17, DOI 10.3390/histories6010017 (abstract).
- **Claims.** 547 woodcuts (Luther Bibles 1534, 1551 + thematic sets); ground truth from published caption lists; CLIP k-NN F1 0.30; keyword 0.63; GPT-4o descriptions of the *full page* beat descriptions of the *cropped illustration* (F1 0.74 vs 0.63; 0.77 vs 0.52 on 1534); RAG best (0.82); for familiar themes the crop alone is slightly better.
- **Evidence quality.** Careful, but the ground truth is caption-derived (favours text).
- **Leaves open.** Biblical narrative, not emblems; no analysis of *which* content needs the text. Closest methodological precedent for our model conditions.

### F11. Labusch & Neudecker (2023)
- **Reference.** Kai Labusch & Clemens Neudecker, "Gauging the Limitations of Natural Language Supervised Text-Image Metrics Learning by Iconclass Visual Concepts", *HIP '23* (ICDAR workshops): 19–24, DOI 10.1145/3604951.3605516 (abstract only).
- **Claim.** Some Iconclass concepts are learnable by fine-tuned CLIP, others not; qualitative differences hypothesised.
- **Leaves open.** Must be read: if the unlearnable ones are abstract/narrative, it is direct prior evidence for our third question.

### F12. Other VLM negation and compositionality work
- Yuhui Zhang, Yuchang Su, Yiming Liu, Serena Yeung-Levy, "NegVQA: Can Vision Language Models Understand Negation?", *Findings of ACL 2025*, arXiv:2505.22946 (abstract).
- Jaisidh Singh et al., "Learn 'No' to Say 'Yes' Better: Improving Vision-Language Models via Negations", *WACV 2025*: 7991–8001, arXiv:2403.20312 (abstract).
- Junsung Park et al., "Know 'No' Better: A Data-Driven Approach for Enhancing Negation Awareness in CLIP", *ICCV 2025*: 2825–2835, arXiv:2501.10913 (abstract).
- Mert Yuksekgonul et al., "When and Why Vision-Language Models Behave like Bags-of-Words, and What to Do About It?", *ICLR 2023*, arXiv:2210.01936 (abstract) — "NegCLIP" means hard negatives, not linguistic negation.
- Tristan Thrush et al., "Winoground", *CVPR 2022*, arXiv:2204.03162 (abstract).
- Letitia Parcalabescu et al., "VALSE", *ACL 2022*, DOI 10.18653/v1/2022.acl-long.567 (relevant parts read): existence ("there are/are no X") nearly solved; counting, plurality, spatial relations hard.
- **Generation side (closest to the illustrator's task).** Colin Conwell, Rupert Tawiah-Quashie, Tomer Ullman, "Relations, Negations, and Numbers: Looking for Logic in Generative Text-to-Image Models", arXiv:2411.17066 (abstract): with DALL-E 3, no probe exceeds 50% agreement; negation fails most. Omar Elfatairy, Maria A. Bravo, Jessica Bader, Zeynep Akata, "NegT2IBench", arXiv:2610.03084 (2 Oct 2026; abstract): 41.5% of failed statements "render exactly what the prompt forbids" — a modern counterpart of an illustrator drawing the negated object.
- **Still images and time/cause.** VisualCOMET (Park et al., ECCV 2020, arXiv:2004.10796), VCR (Zellers et al., CVPR 2019, arXiv:1811.10830), Sherlock (Hessel et al., ECCV 2022, arXiv:2202.04800) — physical-commonsense before/after inference on photos (abstracts only). No benchmark targets conventional devices for time or condition.
- **Leaves open.** All test negation *in language about* photographs; none tests negation (or time, condition) *depicted* in historical conventional imagery.

### F13. Art, symbol and figurative-meaning benchmarks
- Noa Garcia et al., "A Dataset and Baselines for Visual Question Answering on Art" (AQUA), arXiv:2008.12520 (abstract): splits "visual" vs "knowledge" questions — the nearest precedent for separating image-answerable from text-answerable content.
- Yi Bin et al., "GalleryGPT", *ACM MM 2024*, DOI 10.1145/3664647.3681656; Nicola Fanelli et al., "ArtSeek", arXiv:2507.21917 (abstracts).
- Sebastian Padó & Kerstin Thomas, "Artwork Interpretation with Vision Language Models: A Case Study on Emotions and Emotion Symbols", arXiv:2511.22929 (abstract): models "fail for highly abstract or highly symbolic images. Reliable recognition of symbols remains fundamentally difficult."
- MetaCLUE (Akula et al., CVPR 2023, arXiv:2212.09898); I Spy a Metaphor (Chakrabarty et al., Findings of ACL 2023, arXiv:2305.14724 — LLM writes a "visual elaboration" of a linguistic metaphor, i.e. an automated illustrator); V-FLUTE (Saakyan et al., NAACL 2025, arXiv:2405.01474); IRFL (Yosef et al., arXiv:2303.15445); "Puzzled by Puzzles" rebus study (Lee et al., EMNLP 2025, arXiv:2505.23759). Abstracts only.
- **Not found:** any VLM benchmark on emblems, allegory or personification.

### F14. Brandhorst (2024) and Brandhorst & Posthumus (2024)
- J. P. J. (Hans) Brandhorst, "Standardization at Babel – Iconclass at the next level: a laboratory for image research", *Art Libraries Journal* (2024), DOI 10.1017/alj.2024.14; manuscript <https://iconclass.org/z/read/2024_aljournal_manuscript.pdf> (read): ChatGPT 3.5 asserts Aldus's dolphin-and-anchor is inscribed "Festina lente" (it is inscribed "Aldus"), and invents emblems attributed to Alciato — a model *supplying absent text from priors*.
- Hans Brandhorst & Etienne Posthumus, "One key to open all locks …?", CERL blog, 18 June 2024, <https://cerlblog.wordpress.com/2024/06/18/one-key-to-open-all-locks/>.
- Brandhorst, "Meaningful patterns…", *Bibliothek und Wissenschaft* 55 (2022) [unverified].

### F15. Computational work on emblems and illustrated books
- Michela Vignoli, Chiara Palladino, Rainer Simon, "Machina Emblematica", DH2026 short paper, abstract <https://dh-daejeon.vercel.app/abs/251> [details unverified]: RAG over Camerarius (401 emblems) with OpenCLIP and Qwen2.5-VL; "preliminary"; the model "sometimes misidentifies image content". The only VLM-on-emblems work found; no image-vs-text evaluation.
- Julia Thomas & Irene Testini, "Capturing Captions: Using AI to Identify and Analyse Image Captions in a Large Dataset of Historical Book Illustrations", *DHQ* 18.2 (2024), <https://dhq.digitalhumanities.org/vol/18/2/000740/000740.html> (summary read): ~1M British Library illustrations; "indeterminacy"; captions often quote text the picture does not depict. Largest-scale cousin of our question; mostly post-1700, no emblems.
- Woodcut reuse/matching (not meaning): Matilde Malaspina & Yujie Zhong, "Image-matching technology applied to Fifteenth-century printed book illustration", *Lettera Matematica* (2017), DOI 10.1007/s40329-017-0201-5 (record); EBBA woodcut matching, Fleuron, Ornamento (web summaries only). None applied to Alciato block lineages.
- Daniel van Strien, *iconclass-vlm* (Qwen2.5-VL-3B fine-tuned on the test set), <https://huggingface.co/davanstrien/iconclass-vlm> (card; no evaluation) — inherits the text-derived labels of F5.

## G. Table-of-contents sweep: what was checked

| Source | Coverage | Access | Relevant finds |
|---|---|---|---|
| *Emblematica: Essays in Word and Image*, new series (publisher **Librairie Droz**, not Brill; ISSN 2571-5070; <https://emblematicajournal.com>) | Vol. XXII (2016), vols 1 (2017) to 6 (2024) — titles and abstracts; vol. 7 contents via droz.org / Fabula | Open | Alciato items: Drysdall, "Andrea Alciato: The Law and the Emblems" (2, 2018); Drysdall, "Pythagoras and the Cranes" (3); Scholz, "Emblematum pater et princeps" (3); Drysdall on Aneau's line-for-line translation (6); Caracciolo on Capaccio (2); McDonald on Occasio (1); Howard on Giovio's impresa (5). **No article on illustrators or text–image fidelity.** Brill journal URL returns 404. |
| *Emblematica*, old series (AMS Press, vols 1–21, 1986–2014) | AMS page (contents of vols 14, 15; nominal vs actual issue dates); vol. 20 contents via a notice; others reconstructed from citations (Robohn 2021, SES Newsletter 53, Glasgow) | Mostly **not** open | Tung 2013 "Seeing is Believing" (vol. 20, research note); Cummings 2007 "Alciato's Illustrated Epigrams" (15); Adams 1992 (6.2); Callahan 1991, 1992; Scholz 1991 (5.2); Drysdall 1988, 2001; Probes 2007 "Engraving, Sonnet, Devise: Harmony or Disharmony…" (15); Plotke 2007 "Emblematics and Visual Poetry from a Semiotic Perspective" (15); Daly & Young 2005 on Wither's picture backgrounds (14). |
| SES Collaborative Bibliography (<https://emblemstudies.com/bibliography>) | — | Loaded by JavaScript; API returned 403 | Not obtained — **to open in a browser.** |
| *Word & Image* (Taylor & Francis, 1985–2026) | Full Crossref dump (1,328 records) filtered on emblem / Alciat* / impresa / pictura / woodcut / illustrat* / ekphra*; abstracts via OpenAlex | Metadata open; tandfonline 403 | **One Alciato article: Clement 2019.** Other emblem items: Russell 1988; Tung 1987, 1989 (Peacham); Raspa 1987; Preston 1992; Legge 2000; Bazin 2005; Henry 2006; Partner 2009; Cholcman 2015; Reid 2017; López Calderón 2017. Methodological analogues: Luborsky 1987; Hancher 1992, 2010. |
| *JWCI*; *BHR* | Miedema 1968 (record); Adams 1990 (issue page) | Paywalled | — |
| Glasgow | Alciato at Glasgow introductions (A31a, A31b, A34a, A34b, A42b), prefatory matter (Steyner 1531, Wechel 1534, Hunger 1542), help page, Drysdall's Mignault edition, Tung Variorum (all PDFs) | Open | See A. |
| *RDK* | Heckscher & Wirth 1959, "Emblem, Emblembuch" | Open | B11 |
| OpenAlex (16 queries, 435 works), Crossref, Semantic Scholar, arXiv API, archive.org | Keyword searches on Alciato + illustration/woodcut/pictura; emblem + computer vision / VLM / Iconclass | Open | Andenmatten 2018; Carlisle 2018; Pilacinski et al. 2026; Machina Emblematica 2026; Thomas 2025/2026 |
| Not accessible | JSTOR, Taylor & Francis full texts, Brill chapters, Cairn (Klecker 2007), Heidelberg artdok (Seiler), ResearchGate/Academia, WorldCat; archive.org books are lending-only (Manning 2002, Daly 1998, Russell 1985/1995, Schöne 1964, Daly–Callahan 1985) | — | See I. |

## H. Gap statement

What is **demonstrably not done**, as far as open sources show, with the nearest works:

1. **No systematic typology, with definitions and reliability, of how Alciato's woodcuts render the
   content of the epigrams** — what is rendered, omitted, added, substituted or contradicted, and by
   which device. Nearest: Tung's *Variorum* (A1: per-emblem description of pictorial variants, ~12
   ad hoc fidelity remarks in 212 commentaries, no categories); Andenmatten 2018 (B1: "adéquation au
   texte" for 75 animal emblems, qualitative); Ureña Bracero 2001 (B2: scattered observations,
   e.g. colour → dyer's shop); Manning 1989 (B4: bibliographical); Clement 2019 (A8: "visual
   paraphrase", one motif). Possible exception, **unread**: Cummings 2007, "Alciato's Illustrated
   Epigrams" (B5).
2. **No test of the "pictures cannot say not / if / then / when" thesis on a corpus where the verbal
   source of each picture is known and several independent illustrators rendered the same text.**
   Nearest: Worth 1975 (D1, argument); Sato et al. 2021/2023 (D2–D3, manga and photos with no
   source text); Oversteegen & Schilperoord 2014 (D4, advertisements); Orenes 2021 / Kaup et al.
   2006 (D12, comprehension, not production); van Miltenburg et al. 2016 (D13, captions of photos).
3. **No diachronic measurement of drift that separates inherited copying from new interpretation**
   across 1531–1621. Nearest: Tung's copy chains (A1), Manning (B4), Carlisle 2018 (B12,
   memory-image → naturalism, qualitative), Tversky's "gradual symbolization" (D14, a general claim).
4. **No analysis of the image/text split of Iconclass in emblem cataloguing** (which notation
   families a cataloguer places only under "text"). Nearest: Brandhorst 2004 (E1, principle),
   Kilton 2012 and Stäcker 2012 (E3, qualitative), Cole et al. 2012 (E4, unread).
5. **No controlled study of vision-language models on emblems with image only vs + motto vs +
   epigram, against human judgement, asking which contents leak from text into "description" and
   which visible contents are overwritten.** Nearest: Brandhorst 2025 (F1, ChatGPT‑4o, ~11 emblems,
   no Alciato, no conditions), Brandhorst 2019 (F4, Google Vision), Thomas 2025 (F10, crop vs full
   page on Bible woodcuts, caption-derived ground truth), Spinaci et al. 2025 (F9, saints), Machina
   Emblematica 2026 (F15, prototype). VLM negation work (F2, F12) concerns negation in the *query*,
   not negation *depicted*.
6. **No study putting the three losses on one scale** — illustrator (text→image), cataloguer
   (image→Iconclass, with text in view), model (image±text→description) — under a single coding
   scheme. The theoretical pieces exist separately (Jakobson's transmutation and "must convey",
   Barthes' anchorage, Shatford's of/about, Greenberg's target/over-specificity, Abusch & Rooth's
   compatibility not entailment), but not their joint empirical use.

**What we can therefore claim as new (to be sharpened in S4):** a reliability-checked typology of
text→image rendering strategies derived from one fixed textual corpus with many independent
illustrations; its diachronic profile controlled for copying; and its use as a common yardstick for
catalogue records and VLM descriptions.

**Existing claims we can test rather than assume:** Worth's list (D1); Lessing's attribute/pregnant
moment solutions (C1); Kaup/Orenes' "draw the alternative" for binary predicates (D12); Jakobson's
grammatical-gender prediction for personifications (C4); Glasgow/Tung "1531 unfaithful" vs
Andenmatten "1534 as bad or worse" (A1, B1); Tversky's gradual symbolization (D14); Carlisle's drift
to naturalism (B12); NegBench's affirmation bias in a historical domain (F2); He's
schematic-image advantage on real woodcuts (F3).

## I. Threats to originality (what we could not check)

Candidly, the gap statement rests on titles, abstracts and secondary descriptions for several
items that could contain exactly what we propose:

- **Cummings 2007**, "Alciato's Illustrated Epigrams", *Emblematica* 15: 193–228 — described as
  discussing "the appropriateness or not of their illustrations". Not read. **Highest risk.**
- **Tung 2013**, "Seeing is Believing", *Emblematica* 20: 379–404 — known only from Robohn's
  description; Tung also wrote "Alciato's Practices of Imitation", *Emblematica* 19 (2012): 153–257
  (100+ pages, unread).
- **Adams 1990** (*BHR*, revisions to woodcuts in translations) and **Adams 1992** (death emblems).
- **Manning 1989** (bibliographical approach to the illustrations) and **Manning 2002**.
- **Balavoine 1982** ("sens et contresens") and **Klecker 2007** (*Littérature* 145, on Alciato's
  "signes muets").
- **Scholz 1984** ("Emblematisches Abbilden als Notation") and **Scholz 2002**; **Scholz 1991**
  (survey of research on 1531).
- **Bässler 2012** (only the review read), **Enenkel 2019** chapters, **Gabriele 2009**
  introduction, **Andenmatten 2018** beyond chapter 2, **Sharratt 2005** (Salomon).
- **Daly 1998/2014**, **Russell 1985/1995**, **Saunders 1988**, **Schöne 1964** — lending-only
  copies; their known positions are theoretical, but each may contain case analyses.
- **Oversteegen & Schilperoord 2014** and **Sato et al. 2023** — full texts blocked; their device
  typologies could overlap with our negation sub-scheme.
- **Labusch & Neudecker 2023** (which Iconclass concepts CLIP cannot learn) and **Cole et al.
  2012** (Iconclass in Emblematica Online) — abstracts only.
- **Shatford 1986 / Shatford Layne 1994** — quotes are second-hand (Neugebauer 2010); page numbers
  must be checked.
- The **SES Collaborative Bibliography** could not be queried; the old-series *Emblematica* contents
  (vols 1–13, 16–19, 21) were reconstructed from citations, not seen.
- Non-English scholarship was only lightly searched (French and Spanish items surfaced by chance;
  German Emblemforschung after Scholz/Peil and Italian work on Alciato's images beyond Gabriele were
  not systematically searched).
- Conference talks (SES conferences 2022, 2025) and work in progress (e.g. Brandhorst's announced
  Iconclass–AI experiments, "Machina Emblematica") may overtake the computing part quickly.

Mitigation: these items are listed as reading priorities (J); Marcel may have library access
(JSTOR / Brill / Droz) — to be logged as a question for him in `JOURNAL.md`.

## J. Reading priorities for later steps

1. Cummings 2007; Tung 2013 and 2012; Adams 1990 (interlibrary/JSTOR).
2. Oversteegen & Schilperoord 2014; Sato et al. 2023 full text (OA, blocked to our client — try a
   browser).
3. Scholz 1984; Daly 2014 ch. "On the Interpretation of Emblems"; Manning 1989.
4. Labusch & Neudecker 2023; Cole et al. 2012.
5. Shatford 1986 pp. 43–53 (check quotations).
6. SES Collaborative Bibliography in a browser.
