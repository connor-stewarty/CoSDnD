# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A Curse of Strahd campaign archive, not a software project. There is no package
manifest, no build step, no test suite, and no dependencies to install. The
deliverable is `site/index.html` — one self-contained page — and the prose in
`sessions/`, `world/` and `character/` that feeds it.

The dominant task here is: **a session transcript arrives, and everything
downstream of it gets updated.** Read `README.md` for the human version of that
workflow and `PRODUCT.md` for who the site is for and what may not change.

## The session-update pipeline

When handed a new transcript, the order that works is:

1. **Store the raw transcript** in `transcripts/`, under the recorder's own
   filename (`2026-08-27 18-38-15.txt`). Do not rename or clean it — that folder
   is storage, and `transcripts/README.md` says so. If several passes of the same
   recording arrive (`.srt` + `.txt`, v1 + v2), keep the cleanest one; they are
   the same audio.
2. **Read the whole transcript.** These run 2–3 hours and the recaps are written
   from the tape, not from a summary of it. Check for a top-level `before.md`
   prep note too — recordings often start mid-scene.
3. **Write `sessions/session-NN-<slug>.md`** from `sessions/TEMPLATE.md`. Keep
   the template's section headings.
4. **Update the living docs** in `world/` — `npc-glossary.md`, `locations.md`,
   `quotable-moments.md`. Existing rows get amended, not just appended to; an NPC
   who did something new this session needs their row updated.
5. **Update `site/index.html`** — the JS arrays, and the rolling summary if the
   party's situation has moved (see below).

`character/in-character-journal.md` is the user's own first-person writing. Leave
it to them.

## Editing site/index.html

The file is ~340KB because two typefaces are embedded as base64 woff2 and party
portraits as base64 JPEG/PNG. The part you edit is the plain JS data section near
the bottom, marked with `// ADD NEW ... HERE` comments:

`dungeonMaster`, `portraits`, `partyMembers`, `fallen`, `sessions`, `quotes`,
`locations`. Everything below `RENDERING` is machinery.

Non-obvious behavior worth knowing before you edit:

- **`locations` renders in array order**, not sorted by session — a new entry
  goes where it belongs on the route through the valley, not at the end by
  default.
- **A location's "Not been there yet" state is inferred from its blurb text**
  (`/not (yet )?visited|a lead only/i`), not from a flag. Rewriting a lead's
  blurb is what promotes it to visited.
- **`renderStanding()` spells out counts as words** and reads as a sentence, so
  it stays legible at one session and at forty. Empty states are written, not
  absent — keep that true for anything you add.
- **Every session is addressable at `#session-NN`.** The timeline is built by
  script, so the anchor doesn't exist when the browser first goes looking for a
  fragment — `revealSession()` does the scroll instead, with smooth scrolling
  suppressed for that opening jump only. Open state lives in the `openSessions`
  set, which `renderTimeline()` re-syncs to the DOM on every render so entries
  survive a sort flip. Hash updates are driven off `summary` **clicks**, not the
  `toggle` event: `toggle` also fires for the entry render opens by default,
  which would stamp a hash onto a plain page load.

### Hard constraints on the site

These are confirmed product constraints, not preferences (`PRODUCT.md`,
`DESIGN.md`):

- **Self-contained, single file, zero network requests.** No CDN, no webfont
  link, no icon font, no `fetch`. Images go in as `data:` URIs. Anything that
  needs compiling before it can be served is out.
- **The GitHub Pages deploy must keep working.** `.github/workflows/deploy-pages.yml`
  uploads `site/` as-is on every push to `main` touching `site/**`. It must stay a
  static directory.
- **Every piece of content currently on the page survives** a redesign — the
  rolling summary, roster, fallen, timeline, quotes, locations.
- `site/FONT-LICENSE.txt` (SIL OFL 1.1) covers both embedded faces and ships
  alongside the page.

## Verifying a site change

There is nothing to run, so verify by parsing and rendering:

```bash
# Does the script still parse, and do the data arrays evaluate?
node -e "
const m=require('fs').readFileSync('site/index.html','utf8').match(/<script>([\s\S]*?)<\/script>/)[1];
const f=new Function(m.split('const ESCAPES')[0]+'; return {sessions:sessions.length,quotes:quotes.length,locations:locations.length};');
console.log(f());"
```

For a real render, Chromium and Playwright are available in this environment
(`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`; never run `playwright install`).
Load the page over `file://` — it works, since nothing is fetched — collect
`pageerror`/`console` errors, and assert on rendered text rather than eyeballing
a screenshot alone.

## Transcribing audio locally

`scripts/transcribe.py` is an offline Whisper-via-MLX pipeline built for Apple
Silicon — it runs on the user's Mac, not here.

```bash
bash scripts/setup-whisper.sh              # once: ffmpeg + mlx-whisper in ~/whisper-env
source ~/whisper-env/bin/activate
python3 scripts/transcribe.py path/to/session-audio.m4a 03
```

Writes `transcripts/session-03-raw.txt` and `.json`. Note the mismatch: the
script names files `session-NN-raw.*`, while transcripts that arrive from Vibe or
from a manual Whisper run keep their timestamp filenames. Both live in
`transcripts/`.

## Writing rules that are easy to break

Drawn from `PRODUCT.md` and `DESIGN.md`; breaking these damages the archive
rather than just the prose:

- **Player knowledge only.** The site and the `world/` docs never know more than
  the party does. No module spoilers, no DM secrets, no "actually this is a
  vestige of divine power." If the DM said he can't explain something yet, record
  that he said it.
- **Quotes are verbatim from tape** and attributed to a session. Do not tidy a
  line into something funnier.
- **Uncertainty is content.** "Class unconfirmed", "Not been there yet", "exact
  name TBD", contradictory spellings — these get recorded and given their own
  quiet treatment, never smoothed into a confident guess. Open questions belong in
  the recap's *DM notes / questions for next time*.
- **Both registers, held in tension.** The horror is played straight; the table's
  chaos cuts through it. A dusk-elf massacre three lines from "Racist turtle" is
  what this campaign is. Neither gets sanded down to make the other comfortable.
- **Don't fabricate campaign art.** Only real supplied images go in. The ghost
  Cinzel initial exists precisely as the stand-in for art that doesn't exist.
  (`DESIGN.md` says `media/` is empty — that line predates the cast portraits in
  `media/portraits/`; the ghost initial is still the fallback for anyone without
  one.)
- Voice: dry and specific about the table, straight-faced about Barovia. Not
  marketing copy, not fantasy-novel pastiche.
- Written for the six people who were in the room. It does not have to explain
  D&D or introduce the party.

## Design work

`DESIGN.md` is the built design system, derived from the shipped page — read its
**Do's and Don'ts** before any visual change. The `impeccable` skill is installed
at project scope (`.claude/skills/impeccable/`) with four subagents in
`.claude/agents/`, and `.claude/settings.local.json` wires a design hook to run on
`Edit|Write|MultiEdit` and on `Stop`. Expect that hook to fire when you touch the
site.

## Conventions

- Session files: `sessions/session-01-into-barovia.md` — zero-padded number, short
  slug, sorts chronologically.
- Media: name with the session number where relevant
  (`session-03-vallaki-map.jpg`).
- Audio is gitignored (`*.mp3`, `*.wav`, `*.m4a`, `*.aac`); transcripts are not.
