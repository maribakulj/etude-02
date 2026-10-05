# Annotation guide — v0.1

For [`PROTOCOL.md`](PROTOCOL.md) stages A–D. Examples are from the development set only; links go
to Alciato at Glasgow. **[pilot]** = to be revised after S7.

## 1. Stage A — blind inventory (picture only)

You see one picture and nothing else. List what is drawn, one item per line:

| Type | What to write | Example |
|---|---|---|
| ENTITY | a person, animal, object, building, plant; number if > 1 | `ENTITY  ass` · `ENTITY  men ×2` |
| ATTRIBUTE | a visible property of an entity (clothing, posture, material cue, wings, blindfold, hatching that darkens skin or surface) | `ATTRIBUTE  boy: wings` · `ATTRIBUTE  boy: blindfold` |
| ACTION | what an entity is doing | `ACTION  man: raises a stick over the ass` |
| RELATION | spatial or physical relation between entities | `RELATION  arched plaque: rests on the ass's back` |
| INSCRIPTION | letters in the picture, transcribed | `INSCRIPTION  on pedestal: SPES` |
| SETTING | interior / landscape / city / sea; frame; background elements | `SETTING  landscape with mountains` |

Rules.
1. **Describe, do not identify.** Write "winged naked boy with arrows", not "Cupid", unless the
   picture itself names him (inscription). If you recognise a figure, add a separate line
   `RECOGNISED  Cupid (why: wings, bow)`; it is kept apart from the description.
2. **Confidence on every line**: `clear` / `probable` / `indeterminate`. At ≤ 500 px many details
   are indeterminate: say so rather than guess (lesson of A31b036, where an empty shrine on the
   ass's back was first misread as a background arch).
3. **Absences are not listed** unless something is visibly incomplete (an empty frame, a figure
   with no hands).
4. Do not read the emblem, its motto or any catalogue record before finishing all your pictures.
   After finishing, say whether you recognised any emblem.

## 2. Stage B — segmenting the text

Work on the **Latin printed in that programme**; the translation is an aid.

### 2.1 Units

A **unit** is one predicate with its arguments, carrying at most one operator (negation,
modality, condition, tense shift, question). Split coordinations; keep a relative clause with its
noun when it only identifies it.

Two kinds:

- **Res picta unit (RP)**: something the text asserts **of the scene to be depicted**: an entity,
  an attribute, an action, a spatial relation, a number. Test: *could a picture of the scene show it
  or show its opposite?*
  - [A31b036](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A31b036)
    *Isidis effigiem tardus gestabat asellus*: RP1 ass carries image of Isis; RP2 ass is slow.
    *genibus … flexis*: RP3 people kneel.
  - [A31b059](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A31b059): RP pot A is
    metal; RP pot B is clay; RP both carried by a stream.
- **Argumentative unit (AR)**: content that is not a property of the scene: moral, general claim,
  belief of a character, condition, negation of a belief, comparison's tenor, speech content,
  temporal sequence beyond one moment, address to the reader. Subtype it:
  `NEG`, `COND`, `TIME`, `MODAL`, `SPEECH`, `COMPAR`, `ABSTR`, `GENERIC`, `ADDRESS`, `BELIEF`.
  - A31b036 *Non es Deus tu aselle, sed Deum vehis*: AR-SPEECH + NEG (not god, but carries god).
  - [A31b068](https://www.emblems.arts.gla.ac.uk/alciato/emblem.php?id=A31b068) "winter will soon
    come and destroy you": AR-TIME + SPEECH.

**Borderline [pilot]**: a speech *act* (someone speaking, gesturing) is RP if the text describes
the gesture (*digito … silentia signet*, A31b003 → RP finger on lips); the *content* of speech is AR.
A personification's identity is RP when the text names a figure that stands in the scene (Virtue
at Ajax's tomb, A31b009); the concept it stands for is AR-ABSTR.

### 2.2 Key units

Key RP units are fixed **before looking at the pictures**: the RP units that the motto, or the
final distich, depends on — the ones without which the point cannot be reached. Typically 1–3 per
emblem. Write the reason in one line.

### 2.3 Refuted or hypothetical scenes

When the text describes a scene to deny it (A31b096, the poets' Cupid "falsely" naked, winged,
blind) or a hypothetical one, its units are coded `RP-DENIED` or `RP-HYPOTHETICAL`; the scene the
text affirms (pomegranate on a black shield) is plain RP.

## 3. Stage C — relation codes (unit × picture)

| Code | Rule | Example |
|---|---|---|
| `present` | the inventory contains an item that realises the unit | A31b003 P31: finger on lips |
| `absent` | nothing in the picture realises the unit, and nothing realises an incompatible alternative | A31b068 P31–P21: winter |
| `substituted` | a different item fills the unit's role (other species, other object, other figure) | A31b006 P31: crown on a crow instead of crows on a sceptre |
| `contradicted` | the picture shows the opposite or an incompatible state | A31b096 P31: blind winged archer where the text affirms the shield (for `RP-DENIED` units, `present` means the denied scene is drawn) |
| `indeterminate` | resolution or damage prevents a decision; check the Gallica scan first | — |

Decision order: indeterminate? → present? → contradicted? → substituted? → absent.
For each code give the inventory line(s) relied on.

**Added**: inventory items that match no unit, excluding SETTING lines. Note them with an
optional source guess (Stage D).

**Stock-convention properties** (for H3 baseline): frame shape, landscape type, architecture,
direction of the composition (left/right). Coded per picture from the inventory.

## 4. Stage D — interpretive labels

### 4.1 Source of a departure

For every key unit coded absent / substituted / contradicted, and every salient added element:

`other passage of printed text` · `motto` · `commentary` (give passage) · `visual tradition`
(name: Aesop illustration, Physiologus, Horapollo, stock Cupid, Ripa-type personification…) ·
`earlier block` (which) · `another emblem's block` (which; e.g. A31b013 P31 reuses the cut of
*In simulachrum spei*, per Tung) · `misreading` (state the reading) · `medium constraint`
(colour in a black-line cut) · `indeterminate`.

Always cite the evidence (Tung paragraph, commentary, comparison image). These labels are
interpretive; they are analysed separately from Stage C.

### 4.2 Pictorial means for argumentative units

Only when the AR unit is rendered at all:

| Means | Example (development set) |
|---|---|
| `inscription` | SPES / NEMESIS on pedestals, A34b079; D M AIACIS, A34b009 |
| `attribute` | bridle for Nemesis, A21a046; Occasio's forelock and bald nape, A31b017 |
| `gesture/deixis` | driver points while whipping, A34b035; lame man points the way, A50a160 |
| `co-presence of states` | dead elm + living vine, A31b012; winds + standing oak, A34b056 |
| `vehicle scene` | hares and dead lion for Hector's speech, A31b058 |
| `depiction of the contrary` | (reserved; to be found in the pilot) |
| `act performed` | the jussive "let him press his lips" drawn as done, A31b003 |
| `other` | describe |

## 5. Things the pilot must settle [pilot]

- Is RP vs AR decidable for speech gestures, personifications and similes with ≥ 0.67 agreement?
- Is `substituted` vs `contradicted` reliably distinguishable?
- How many units per emblem (time budget)?
- Can Stage A coders stay blind (they may recognise famous emblems)?
- Can P50 be equated with Tung's "51" block by block?
