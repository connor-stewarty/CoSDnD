# Curse of Strahd — Campaign Archive

A living record of our Curse of Strahd campaign, kept from the player's-eye view. This folder is both a working journal and the source material for the showcase site in `site/index.html`.

## Folder guide

- **sessions/** — one markdown file per session, using `TEMPLATE.md` as the starting point. This is the backbone of the archive: what happened, in order.
- **character/** — your character sheet notes and an in-character journal, written after (or during) each session.
- **world/** — living reference docs built up as the party learns things: NPCs met, locations visited, memorable quotes. These are *player-knowledge only* — no spoilers your character wouldn't know.
- **transcripts/** — raw Vibe transcripts land here, one file per session. Treat these as source material, not something to polish — the real writing happens in `sessions/`.
- **media/** — maps, character art, screenshots, battle-map photos — anything visual worth keeping.
- **site/** — `index.html`, the shareable showcase site. Self-contained, no build step — open it in a browser or send the file directly.

## Workflow after each session

1. Record the session with Vibe as usual; drop the transcript (or its export) into `transcripts/session-##.md` (or `.txt`).
2. Skim the transcript and fill out a new `sessions/session-##-<title>.md` from `sessions/TEMPLATE.md`. You don't need to transcribe everything — pull out what mattered: key events, decisions, fights, jokes, cliffhangers.
3. Update the living docs as needed:
   - New NPC? Add a line to `world/npc-glossary.md`.
   - New place? Add it to `world/locations.md`.
   - Someone said something unhinged? `world/quotable-moments.md`.
4. Write (or dictate) a couple of in-character lines in `character/in-character-journal.md` — even two sentences is worth it later.
5. Every so often, open `site/index.html` in a text editor and add the new session/quote/location to the JS arrays near the top of the file (clearly marked `// ADD NEW ... HERE`). Refresh the browser to see it update. No rebuild needed.

## Naming convention

`sessions/session-01-into-barovia.md`, `sessions/session-02-village-of-barovak.md`, etc. — zero-padded number + short slug. Keeps everything sorted chronologically in Finder and in the file list.

## Sharing the site

`site/index.html` is fully self-contained (no external files needed) — you can email it, AirDrop it, or drop it in a shared drive and anyone can just open it in a browser.
