# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Single self-contained `site/index.html` — no build step, no server, no external
requests. Deployed to GitHub Pages from `site/` by
`.github/workflows/deploy-pages.yml` on push to `main`. Constraint confirmed by
the repository (README "Sharing the site", the workflow, and the file itself),
not by interview.

## Users

**The table, confirmed as the primary and only named audience.** Six people
who were in the room — Connor (Scottishbard), William (DM), and the players
behind Dablin, Bulbin, Dog, Phoenix Cloak. They arrive already knowing the
story and looking for a specific moment: a line someone said, when an NPC
turned up, what they decided to do next.

Consequence: the site is written for insiders. It does not have to explain
D&D, introduce the party, or stay legible to a stranger who wanders in. The
README's "shareable" framing is about the file being easy to send, not about
courting an outside audience.

## Product Purpose

A living, player's-eye record of one Curse of Strahd campaign, kept so the
table can find what happened and relive how it felt. Success is that a session
gets written up and the site stays current — the workflow has to survive a
tired Sunday night.

## Positioning

Two things a generic campaign wiki cannot copy:

1. **It is player-knowledge only.** No DM secrets, no module spoilers. The
   world docs say so explicitly. The site records what the party has actually
   learned, which means it can be wrong, and its being wrong is part of the
   record.
2. **It is sourced from tape.** Sessions are recorded (Vibe) and transcribed
   locally (Whisper via MLX, `scripts/transcribe.py`), producing
   `transcripts/session-NN-raw.json` with per-segment timestamps. Quotes on
   the site are things people verifiably said, not remembered paraphrase.

## Operating Context

Post-session, one person opens the folder and writes: a
`sessions/session-NN-*.md` from `TEMPLATE.md`, a row in
`world/npc-glossary.md` / `locations.md` / `quotable-moments.md`, a couple of
in-character lines, then hand-edits the JS arrays near the top of
`site/index.html` (marked `// ADD NEW ... HERE`) and refreshes the browser.

## Capabilities and Constraints

- Content lives in plain JS arrays inside the HTML file: `partyMembers`,
  `fallen`, `sessions`, `quotes`, `locations`. Hand-edited. Must stay that
  easy to extend.
- Self-contained: no webfonts, no external images, no CDN, no fetch. Anything
  visual has to be authored in CSS/SVG inside the file.
- `media/` exists but is empty apart from a README — there is no campaign art,
  no maps, no photos. **Do not fabricate any.**
- One session is logged (Session 01, 2026-07-23). The site must not look
  broken at n=1, and must not look designed-for-one at n=40.
- Some facts are openly unresolved and marked as such in the source docs
  (whether "Gerland" is Scottishbard's real name; where "the house" was).
  Uncertainty is content, not a defect to smooth over.

## Brand Commitments

- Title: *Curse of Strahd — Campaign Chronicle*. Tagline in the file: "The
  mists remember everything, even when the party doesn't."
- Voice: dry, specific, unreverent about the table and straight-faced about
  Barovia. Not marketing copy, not a fantasy-novel pastiche.

## Evidence on Hand

- `sessions/session-01-new-allies-and-the-amber-temple-lead.md` — one full
  write-up.
- `transcripts/2026-07-23 20-22-00.json` — raw timestamped transcript.
- `world/npc-glossary.md`, `world/locations.md`, `world/quotable-moments.md`.
- `character/character-sheet-notes.md`, `character/in-character-journal.md`
  (the journal is still an unfilled prompt).
- No images, no logo, no player photos, no maps.

## Product Principles

1. Player knowledge only — the site never knows more than the party does.
2. The tape is the source; quotes are verbatim and attributable to a session.
3. **Both registers, held in tension.** Confirmed by the user: the horror is
   played straight and the table's chaos cuts through it. A dusk-elf massacre
   three lines from "Racist turtle" is what the campaign actually is; neither
   register gets sanded down to make the other comfortable.
4. Adding a session must stay a five-minute, single-file edit.
5. Written for the people who were there.

## Confirmed Constraints

The one thing the user marked as unbreakable in the redesign: **every piece of
content currently on the page survives** — the rolling story summary, the
party roster, the fallen, the session timeline, the quotes, the locations.

**The GitHub Actions deploy must keep working.** Confirmed by the user.
`.github/workflows/deploy-pages.yml` uploads `site/` as the Pages artifact on
every push to `main` that touches `site/**`. Whatever the redesign does, the
site must remain a static directory that Pages can serve with no build step,
no server, and no runtime dependency — anything that needs compiling before it
can be served is out.

Not marked binding, but preserved by choice and by the deploy's shape: the
single self-contained `site/index.html` with hand-edited arrays.

## Accessibility & Inclusion

Read on phones and laptops, often at night. Text contrast ≥4.5:1, visible
keyboard focus, motion gated behind `prefers-reduced-motion` — the standard
the current build already meets and must not regress.
