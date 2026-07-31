---
name: Curse of Strahd — Campaign Chronicle
description: A player's-eye season record of one Barovia campaign, built to the production craft of an actual-play show hub.
colors:
  void: "#0a090c"
  field: "#121016"
  field-2: "#17141b"
  blood: "#4e1220"
  blood-deep: "#2b0a11"
  blood-line: "#7a2033"
  rose: "#e8a3ad"
  rose-mid: "#d9a7ae"
  rose-dim: "#b2848c"
  bone: "#f0eae0"
  bone-dim: "#b4aa9d"
  bone-faint: "#8b8177"
  gold: "#d9b463"
  gold-mid: "#a8843a"
  gold-dim: "#6f5a28"
  rule: "#2c2429"
  rule-lit: "#453640"
typography:
  display:
    fontFamily: "Cinzel, 'Trajan Pro', Georgia, serif"
    fontSize: "clamp(40px, 8.4vw, 104px)"
    fontWeight: 600
    lineHeight: 1.02
    letterSpacing: "0.03em"
  headline:
    fontFamily: "Cinzel, 'Trajan Pro', Georgia, serif"
    fontSize: "clamp(23px, 3vw, 31px)"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "0.07em"
  title:
    fontFamily: "Cinzel, 'Trajan Pro', Georgia, serif"
    fontSize: "clamp(19px, 2.3vw, 23px)"
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: "0.02em"
  card-title:
    fontFamily: "Cinzel, 'Trajan Pro', Georgia, serif"
    fontSize: "19px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.03em"
  numeral:
    fontFamily: "Cinzel, 'Trajan Pro', Georgia, serif"
    fontSize: "27px"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.02em"
  quote:
    fontFamily: "Cinzel, 'Trajan Pro', Georgia, serif"
    fontSize: "clamp(21px, 2.4vw, 27px)"
    fontWeight: 600
    lineHeight: 1.24
    letterSpacing: "0.005em"
  quote-featured:
    fontFamily: "Cinzel, 'Trajan Pro', Georgia, serif"
    fontSize: "clamp(28px, 4.4vw, 50px)"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "0.005em"
  lede:
    fontFamily: "Alegreya, Georgia, 'Iowan Old Style', serif"
    fontSize: "clamp(19px, 2.4vw, 23px)"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "normal"
  body:
    fontFamily: "Alegreya, Georgia, 'Iowan Old Style', serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.62
    letterSpacing: "normal"
  body-small:
    fontFamily: "Alegreya, Georgia, 'Iowan Old Style', serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "normal"
  aside-italic:
    fontFamily: "Alegreya, Georgia, 'Iowan Old Style', serif"
    fontSize: "16.5px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  label:
    fontFamily: "Alegreya, Georgia, 'Iowan Old Style', serif"
    fontSize: "11.5px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.16em"
  label-small:
    fontFamily: "Alegreya, Georgia, 'Iowan Old Style', serif"
    fontSize: "10.5px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.14em"
  nav:
    fontFamily: "Alegreya, Georgia, 'Iowan Old Style', serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.14em"
rounded:
  none: "0"
  control: "2px"
  surface: "3px"
  focus: "2px"
  headstone: "18px 18px 2px 2px"
spacing:
  s-1: "6px"
  s-2: "12px"
  s-3: "20px"
  s-4: "32px"
  s-5: "52px"
  s-6: "84px"
  s-7: "120px"
components:
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.bone-dim}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "0 18px"
    height: "44px"
  button-ghost-hover:
    textColor: "{colors.gold}"
  nav-link:
    backgroundColor: "transparent"
    textColor: "{colors.bone-faint}"
    typography: "{typography.nav}"
    rounded: "{rounded.none}"
    padding: "19px 0"
  nav-link-hover:
    textColor: "{colors.bone}"
  nav-link-current:
    textColor: "{colors.gold}"
  card-cast:
    backgroundColor: "{colors.field-2}"
    textColor: "{colors.bone}"
    rounded: "{rounded.surface}"
    padding: "{spacing.s-3}"
  card-cast-lead:
    backgroundColor: "{colors.field}"
    textColor: "{colors.bone}"
    rounded: "{rounded.surface}"
    padding: "{spacing.s-3}"
  card-memoriam:
    backgroundColor: "#0f0e11"
    textColor: "{colors.bone-dim}"
    rounded: "{rounded.surface}"
    padding: "{spacing.s-3}"
  chip-lead-flag:
    backgroundColor: "rgba(122, 32, 51, 0.22)"
    textColor: "{colors.rose}"
    typography: "{typography.label-small}"
    rounded: "{rounded.control}"
    padding: "2px 8px"
  numeral-plate:
    backgroundColor: "rgba(0, 0, 0, 0.35)"
    textColor: "{colors.gold-mid}"
    typography: "{typography.numeral}"
    rounded: "{rounded.none}"
    size: "62px"
  numeral-plate-open:
    backgroundColor: "rgba(122, 32, 51, 0.34)"
    textColor: "{colors.gold}"
    typography: "{typography.numeral}"
    rounded: "{rounded.none}"
    size: "62px"
---

# Design System: Curse of Strahd — Campaign Chronicle

## Overview

**Creative North Star: "The Season Hub"**

This is Barovia's own dark gothic, played completely straight, arranged as a produced season rather than a wiki: a title card, a cast, an episode log, a record of things people actually said, and a route through the valley. The craft bar was set explicitly by the user against actual-play brands (Critical Role, Dimension 20) — the reference is a show's home page, not a fan page about a show. The register is dry and specific about the table and solemn about the setting; both are held at once, and neither gets sanded down.

The world is built from four materials and nothing else: near-black grounds, oxblood as a committed field, bone as ink, and gold used only as struck metal. There is no photography, no illustration, and no icon set beyond three hand-drawn inline SVG strokes, because `media/` is empty and no campaign art may be invented. Where a portrait would go, a Cinzel initial is cut into the card at device scale and cropped by the card edge. Density is editorial: a 66ch measure for anything read at length, generous vertical air between sections, and cards that stay legible whether the campaign has one session logged or forty.

**Provenance.** The direction roll ran DEGRADED: `concept-seed.mjs --scope direction --mode experience` could not reach `https://impeccable.style/api/roll` (the environment's proxy returns 403 on CONNECT), so there are no challenger cards, no QUALITY BAR boards, and no approved comp. The seed key `1fc2c67f` printed in the direction contract is **uncorroborable** and must not be read by a later pass as a verified roll. The roll dealt index 3 of the grounded list — a court-reporter "transcript of proceedings" world. The user took the **standing exit** (candidate 1, the category standard) instead. That exit is now a brand commitment, not a fallback: this project is the dark Barovia gothic played straight, and a future pass must not "restore" the dealt transcript world.

**Key Characteristics:**
- Oxblood is a field that carries whole regions, never an accent swatch.
- Two typefaces only, both embedded as base64 latin woff2 subsets; zero network requests.
- Gold appears at hairline weight — rules, frames, numerals, nodes, links, focus.
- Depth is tonal and hairline-drawn; one soft shadow token exists and no other.
- Every device on the page carries meaning: the ghost initial stands in for art that does not exist, the dashed rail segment marks a road not walked.
- Exactly one authored motion moment; everything else is functional state transition.

## Colors

A four-material palette: near-black grounds, one saturated oxblood field, warm bone ink, and gold as struck metal.

### Primary
- **Oxblood Field** (`{colors.blood-deep}` → `{colors.blood}`): the committed color. It is not an accent — it grounds three whole regions of the page as gradient fields: the cold open (title card and "The Story So Far" as one continuous field down to void), the quotes section, and the credits footer. Rendered as a radial bloom over a vertical gradient, never as a flat fill.
- **Blood Line** (`{colors.blood-line}`): the oxblood hairline. Top border of an oxblood band, border of a lead cast card, the inset top rule on an opened episode, and the tint inside translucent oxblood washes (`rgba(122, 32, 51, …)`).

### Secondary
- **Gold** (`{colors.gold}`): struck metal. Links, focus ring, the second line of the title, the drop cap, the active nav underline, the open episode numeral, the ghost initial's tint. Never a fill behind text.
- **Gold Mid** (`{colors.gold-mid}`): the working metal weight — closed episode numerals, beat dashes, meta keys, the title card's corner-frame strokes, route nodes.
- **Gold Dim** (`{colors.gold-dim}`): ornament only. Section trail rules, the dashed unvisited rail, hover borders. Fails text contrast; never used for text.

### Tertiary
- **Rose** (`{colors.rose}`), **Rose Mid** (`{colors.rose-mid}`), **Rose Dim** (`{colors.rose-dim}`): the ink family that survives on oxblood ground — the "Played by you" flag, quote attributions, and the muted aside text inside an oxblood band. Bone would go chalky against oxblood; rose keeps the field warm.

### Neutral
- **Void** (`{colors.void}`): the page ground and the base of every dark region; also the hollow fill inside an unvisited route node.
- **Field** (`{colors.field}`) / **Field 2** (`{colors.field-2}`): the two raised tones. `field` is a dark band section; `field-2` is a card face and the ground of an opened episode.
- **Bone** (`{colors.bone}`): primary text, headings, names, beats.
- **Bone Dim** (`{colors.bone-dim}`): secondary prose — card blurbs, recaps, cliffhangers, credit values.
- **Bone Faint** (`{colors.bone-faint}`): tertiary metadata — session dates, memoriam text, resting nav links, empty-state notes.
- **Rule** (`{colors.rule}`) / **Rule Lit** (`{colors.rule-lit}`): the two hairline weights. `rule` divides sections and episodes; `rule-lit` draws the lighter internal divider, control borders, the route rail, and the headstone.

### Named Rules

**The Committed Field Rule.** Oxblood is a ground, not an accent. It may only be spent on a full-width region that owns its whole vertical span (cold open, quotes, credits). A component never gets an oxblood fill of its own except as a translucent wash (`rgba(122, 32, 51, 0.2–0.35)`) signalling state.

**The Alternating Third Rule.** The bottom third of the page runs oxblood (quotes) → dark band (The Valley) → oxblood (credits). This alternation is deliberate: the dark band is the breath between the table's voice and the sign-off. Do not "fix" it by collapsing the two oxblood fields into one continuous run.

**The Struck Metal Rule.** Gold is metal struck into a surface: hairlines, frames, numerals, nodes, dashes, underlines, focus rings, and links. It is never a background behind text and never a filled button.

**The Text-Safe Ramp Rule.** `{colors.gold-dim}` and `{colors.blood}` are hairline-and-ornament values only. The text-safe inks are `{colors.gold}`, `{colors.gold-mid}`, `{colors.bone}`, `{colors.bone-dim}`, `{colors.bone-faint}` — and on oxblood ground, the rose family. Every text/background pair on the shipped page clears 4.5:1; any new pair must be checked before it ships.

**The No Local Ground Rule.** A component sitting inside an oxblood band declares no background of its own. The credits footer carries `padding` and nothing else, because a local background would quietly override the committed field.

## Typography

**Display Font:** Cinzel 600 (with 'Trajan Pro', Georgia, serif)
**Body Font:** Alegreya 400 / 400 italic / 700 (with Georgia, 'Iowan Old Style', serif)

Both are embedded in the page as base64 latin woff2 subsets inside `<style id="typefaces">`. This is a hard constraint, not a convenience: the site must remain one self-contained file that makes zero network requests and deploys as a static `site/` directory through GitHub Actions.

**Character:** Cinzel is an inscriptional Roman capital — it reads as carved, and it does the work of engraved signage on the title card, the section headings, and the episode numerals. Alegreya is a warm literary serif that stays comfortable at 18px for long stretches at night. The pairing is a monument and a book, which is exactly the split between how the world is titled and how it is read.

### Hierarchy
- **Display** (Cinzel 600, `clamp(40px, 8.4vw, 104px)`, 1.02, +0.03em): the title card only. Set on two lines with the second line in gold.
- **Headline** (Cinzel 600, `clamp(23px, 3vw, 31px)`, 1.15, +0.07em, uppercase): section headings, each followed by a gold trail rule that fades right.
- **Title** (Cinzel 600, `clamp(19px, 2.3vw, 23px)`, 1.22, +0.02em): episode titles in the log.
- **Card Title** (Cinzel 600, 19px, 1.2, +0.03em): cast names and place names. Memoriam names run one step down (17px) in bone-dim.
- **Numeral** (Cinzel 600, 27px, 1, +0.02em): zero-padded episode numbers, struck on their plate.
- **Quote** (Cinzel 600, `clamp(21px, 2.4vw, 27px)`, 1.24): the table's voice, set upright as display rather than as body italic. The first quote is featured at `clamp(28px, 4.4vw, 50px)` / 1.12 across the full grid width.
- **Lede** (Alegreya 400, `clamp(19px, 2.4vw, 23px)`, 1.55): the rolling story summary, opened with a floated Cinzel 600 drop cap in gold at 3.4em / 0.84.
- **Body** (Alegreya 400, 18px, 1.62; 17px below 820px): all sustained prose, capped at a 66ch measure.
- **Body Small** (Alegreya 400, 14.5–17.5px, 1.55): card blurbs, place descriptions, recaps, credit values.
- **Aside Italic** (Alegreya 400 italic, 15–20px, 1.45–1.5): the subtitle, the standing line, cliffhangers, quote attributions, the colophon motto, empty-state notes.
- **Label** (Alegreya 700, 11.5px / 10.5px, +0.16em / +0.14em, uppercase, gold): field labels and the small caps voice.
- **Nav** (Alegreya 700, 12px, +0.14em, uppercase; 11px / +0.10em below 820px).

### Named Rules

**The Two Voices Rule.** Anything titled or numbered is Cinzel 600. Anything read at length is Alegreya. There is no third face and no weight outside 400 / 400i / 600 (Cinzel) / 700 (Alegreya). A new face means a new base64 payload in the file, so the answer is no.

**The Table's Voice Rule.** The page's ambient register is Barovia's — solemn, italic, at a reading measure. The quotes section inverts every one of those: upright Cinzel, heavy, short measure, loud, on oxblood ground. That inversion is the whole point of the section; do not normalize it into body italic.

**The Field-Label Rule.** The gold uppercase label names a value that sits beneath or beside it — a definition term, a role under a cast name, a sub-heading inside an opened episode. It never sits above a headline as a kicker or eyebrow. If a label has no value attached to it, it does not belong on the page.

## Layout

A single centered column: `1120px` max width with `32px` gutters (`20px` below 820px). Long-form text is further capped at a `66ch` measure, so prose never runs the full page width even when its container does.

The spacing rhythm is a seven-step scale climbing at roughly 1.6× (`6 / 12 / 20 / 32 / 52 / 84 / 120px`). Sections are padded `120px` top and `84px` bottom, dropping to `84 / 52px` below 820px. Section heads are a baseline-aligned flex row: heading, then a flexible gold trail rule, then an optional right-hand aside count.

Grids are all `auto-fill` / `auto-fit` with `minmax(min(N, 100%), 1fr)` so they reflow without breakpoints: cast at 288px minimum, memoriam at 440px, quotes at 300px, credits at 220px. The opened episode body is a two-column plate (1.4fr / 0.6fr) with a full-width closing row for the cliffhanger, indented 84px to clear the numeral plate; it collapses to one column below 820px. The nav bar is sticky at 58px (52px narrow) with matching `scroll-padding-top`.

### Named Rules

**The Measure Rule.** Anything read at length is capped at 66ch (`--measure`), regardless of how wide its container is.

**The n=1 to n=40 Rule.** Every list renders from a hand-edited JS array (`partyMembers`, `fallen`, `sessions`, `quotes`, `locations`, `dungeonMaster`) and must look composed at one entry and at forty. Counts are rendered as a spelled-out sentence rather than a scoreboard; the newest episode opens by default; every list has a written empty state; the memoriam block and the in-memoriam credit column remove themselves entirely when nothing has died.

**The One Bar Rule.** Below 820px the sticky bar carries the navigation and drops the wordmark. A phone bar holds one or the other, and the title card already carries the identity.

## Elevation & Depth

Depth is tonal and hairline-drawn, not shadowed. Surfaces separate by stepping through `void → field → field-2` and by a 1px rule at every seam; the two rule weights (`rule` for structure, `rule-lit` for internal division) do most of the work that shadows would do elsewhere. There is exactly one shadow token in the system, and it is a soft diffuse lift under cast cards, not a cast shadow.

### Shadow Vocabulary
- **Lift** (`box-shadow: 0 14px 30px -18px rgba(0,0,0,0.9)`): the only ambient shadow. Cast cards only — it seats the plate on the ground without drawing an edge.
- **Struck top rule** (`box-shadow: inset 0 1px 0 var(--blood-line)`): not depth; an oxblood hairline struck across the top of an opened episode.
- **Title relief** (`text-shadow: 0 1px 0 rgba(0,0,0,0.9), 0 18px 46px rgba(0,0,0,0.55)`): title-card lettering only, so the display type holds against the mist.

### Named Rules

**The One Shadow Rule.** `--lift` is the system's entire shadow vocabulary. New surfaces separate by tone and hairline. No hard-offset shadows, no stacked elevation ramp, no glow.

**The Backdrop Rule.** The only translucent surface on the page is the sticky bar (`rgba(10,9,12,0.86)` with a 10px backdrop blur). Cards and bands are opaque.

## Shapes

The form language is near-square. Radius is effectively zero: `3px` on cards, `2px` on controls, chips, and the focus ring, and `0` on the numeral plate, the title frame, and the nav underline. The single deliberate curve on the page is the memoriam marker — a 36×44px headstone with `18px 18px 2px 2px` corners, which reads as a shape rather than a rounded box.

Everything else is drawn with 1px strokes: the title card's struck frame (an inset gold-tinted rectangle with heavier gold caps at top and bottom edges), the section trail rule, the route rail, the beat dashes, the memoriam divider. Recurring silhouettes: the 62px square numeral plate, the 9px diamond route node (a rotated square, solid when visited and hollow-with-gold-outline when not), and the 210px Cinzel initial cropped by the cast card's bottom-right corner. Icons are three inline SVG symbols (chevron, sort, headstone), stroked at 1.5 with round caps in `currentColor` — never an icon font, never a glyph character.

## Components

### Buttons
- **Shape:** near-square (2px radius), 44px minimum height, 18px horizontal padding.
- **Ghost (the only variant):** transparent ground, bone-dim label type, `rule-lit` 1px border, with a 13px inline SVG icon on the left. Used once, for the session-log order toggle.
- **Hover:** ink goes gold, border goes gold-dim, ground picks up a 5% gold wash — all over 180ms ease.
- **Focus:** the global 2px gold outline at 3px offset.
- There is no filled or primary button in this system. The page has one control; it does not need a hierarchy of them.

### Chips
- **Lead flag** ("Played by you"): translucent oxblood ground, `blood-line` border, rose ink, 10.5px uppercase label type at 2/8px padding, 2px radius. Marks the card belonging to whoever is reading.

### Cards / Containers
- **Cast card:** `field-2 → field` vertical gradient with a 135° 1.2%-white hatch over it, `rule` border, 3px radius, `--lift` shadow, 20px body padding, contents stacked at 6px gaps. The lead variant swaps to a `blood-line` border and adds an oxblood radial bloom from the top-right corner.
- **Memoriam card:** flatter and quieter — `#0f0e11` ground, `rule` border, no shadow, a 36px headstone marker in a fixed first column, name in bone-dim, body in bone-faint.
- **Shadow strategy:** see Elevation. Cast cards lift; nothing else does.

### Navigation
Sticky translucent bar with a blurred backdrop and a `rule` bottom border. The wordmark is 13px Cinzel at +0.2em with the "OF" in gold-mid. Links are 12px uppercase Alegreya 700 in bone-faint, going bone on hover and gold when current; the current link also draws a 1px gold underline that scales in from `scaleX(0)` over 220ms on a decelerating curve. Current state is set by an IntersectionObserver against the section the reader is actually in, offset for the bar height. The nav scrolls horizontally on narrow screens with the scrollbar hidden.

### Episode Log (signature)
Each session is a native `<details>` disclosure divided by `rule` hairlines; the newest is open on load. The summary is a three-area grid: numeral plate, title and meta stack, chevron.
- **The number plate** changes all three of its surfaces between states. Closed: `rule-lit` border, black-35% ground, gold-mid ink. Open: gold-dim border, oxblood-34% ground, gold ink. Hover takes ink and border to gold without changing the ground. The plate is the state indicator, not decoration.
- **Open body:** an oxblood-to-transparent wash over `field-2` fading out by 420px, plus an inset `blood-line` top rule. Content splits into beats (gold-mid dash markers) and a "Line of the night" aside; the cliffhanger spans the full plate as the closing beat.
- **Chevron:** 15px inline SVG, rotates 180° over 260ms and goes gold when open.

### The Valley Route (signature)
Locations render as a vertical route rather than a list. A 1px `rule-lit` rail runs the left edge between nodes — clipped at the top of the first entry and stopped 39px into the last, so the road begins and ends at a node rather than running off. Each entry carries a 9px gold-mid diamond. A place the party has only heard about renders hollow (void fill, gold-dim outline) with its incoming rail segment dashed (`repeating-linear-gradient`, 5px on / 6px off) and its label reading "Not been there yet". The detection is content-driven — the blurb saying the party has not been there is what draws the dashed road.

### The Ghost Initial (signature)
No portraits exist and none may be fabricated, so the first letter of the character's name is cut into the cast card itself: Cinzel 600 at 210px, 17% gold, anchored past the bottom-right corner so the card edge crops it. It is sized as a real device, not as a faint watermark. On a lead card it tints rose instead.

### Motion
One authored moment: two radial mist layers on the cold open, drifting vertically (±7%), scaling 1 → 1.3, and fading 0.55 → 1 over 26s and 37s, alternating. There is deliberately **no horizontal translation** — a fog, not a marquee. Everything else is functional: 180–260ms transitions on disclosure, nav state, and control hover. All of it, including smooth scrolling, is disabled under `prefers-reduced-motion: reduce`.

## Do's and Don'ts

### Do:
- **Do** spend oxblood as a full-width field that owns its whole region, and keep the bottom-third alternation (quotes oxblood → Valley dark → credits oxblood) exactly as built.
- **Do** keep gold at hairline weight — rules, frames, numerals, nodes, links, focus — per The Struck Metal Rule.
- **Do** check every new text/background pair against 4.5:1, and treat `--gold-dim` and `--blood` as ornament-only values.
- **Do** set anything titled or numbered in Cinzel 600 and anything read at length in Alegreya, capped at the 66ch measure.
- **Do** give every new list a written empty state and make it compose at one entry and at forty.
- **Do** draw new structure with 1px `rule` / `rule-lit` hairlines and tonal steps rather than reaching for a shadow.
- **Do** gate any new motion behind `prefers-reduced-motion` and keep it non-horizontal.
- **Do** make each device mean something — if a variant does not encode a fact about the campaign, it is decoration.

### Don't:
- **Don't** fabricate campaign art, maps, portraits, or photographs. `media/` is empty by fact, and the ghost initial exists precisely so that stays true.
- **Don't** add a third typeface, a webfont link, a CDN, an icon font, or any request that leaves the page. The file must stay self-contained and deployable as a static `site/` directory.
- **Don't** use glyph characters or icon-font symbols for icons; the three inline SVG symbols, stroked at 1.5, are the vocabulary.
- **Don't** add a hard-offset or stacked shadow. `--lift` is the whole vocabulary.
- **Don't** place a kicker or eyebrow above a headline. The uppercase gold label is a field label and must have a value under or beside it.
- **Don't** give a component its own background inside an oxblood band, and don't set a background on the credits footer.
- **Don't** put a fill behind gold text or build a filled/primary button; the one control on the page is a ghost.
- **Don't** smooth over uncertainty. "Class unconfirmed", "Not been there yet", and unresolved facts are content and get their own quiet typographic treatment, not a fake value.
