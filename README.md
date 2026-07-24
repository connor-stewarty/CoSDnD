# Curse of Strahd — Campaign Archive

A living record of our Curse of Strahd campaign, kept from the player's-eye view. This folder is both a working journal and the source material for the showcase site in `site/index.html`.

## Folder guide

- **sessions/** — one markdown file per session, using `TEMPLATE.md` as the starting point. This is the backbone of the archive: what happened, in order.
- **character/** — your character sheet notes and an in-character journal, written after (or during) each session.
- **world/** — living reference docs built up as the party learns things: NPCs met, locations visited, memorable quotes. These are *player-knowledge only* — no spoilers your character wouldn't know.
- **transcripts/** — raw transcripts land here, one file per session. Treat these as source material, not something to polish — the real writing happens in `sessions/`.
- **media/** — maps, character art, screenshots, battle-map photos — anything visual worth keeping.
- **site/** — `index.html`, the shareable showcase site. Self-contained, no build step — open it in a browser or send the file directly.
- **scripts/** — local, offline speech-to-text tooling (see below) for turning a raw session recording into a transcript without relying on Vibe or any cloud service.

## Workflow after each session

1. Record the session with Vibe as usual. If you want a raw text transcript and Vibe hasn't already given you one, run it through the local Whisper setup in `scripts/` (below) instead.
2. Skim the transcript and fill out a new `sessions/session-##-<title>.md` from `sessions/TEMPLATE.md`. You don't need to transcribe everything — pull out what mattered: key events, decisions, fights, jokes, cliffhangers.
3. Update the living docs as needed:
   - New NPC? Add a line to `world/npc-glossary.md`.
   - New place? Add it to `world/locations.md`.
   - Someone said something unhinged? `world/quotable-moments.md`.
4. Write (or dictate) a couple of in-character lines in `character/in-character-journal.md` — even two sentences is worth it later.
5. Every so often, open `site/index.html` in a text editor and add the new session/quote/location to the JS arrays near the top of the file (clearly marked `// ADD NEW ... HERE`). Refresh the browser to see it update. No rebuild needed.

## Transcribing a recording locally (Whisper via MLX)

If you have a raw audio recording (from Vibe or otherwise) and want a text transcript, `scripts/` has a small offline pipeline built for Apple Silicon Macs — no cloud API, no account, no cost per minute.

One-time setup, from Terminal in this folder:
```
bash scripts/setup-whisper.sh
```
This installs `ffmpeg` (via Homebrew, if missing) and `mlx-whisper` in a dedicated virtual environment at `~/whisper-env`.

To transcribe a session:
```
source ~/whisper-env/bin/activate
python3 scripts/transcribe.py path/to/session-audio.m4a 03
```
(the `03` is the session number — just used to name the output files). This writes `transcripts/session-03-raw.txt` (plain text) and `transcripts/session-03-raw.json` (text plus per-segment timestamps).

By default this uses `whisper-large-v3-turbo` — fast and very accurate. On an M1 Pro with 32GB RAM you can just as easily run the full, slightly-more-accurate `large-v3` model instead by editing the `MODEL` line at the top of `scripts/transcribe.py` to `"mlx-community/whisper-large-v3-mlx"`.

## Naming convention

`sessions/session-01-into-barovia.md`, `sessions/session-02-village-of-barovak.md`, etc. — zero-padded number + short slug. Keeps everything sorted chronologically in Finder and in the file list.

## Sharing the site

`site/index.html` is fully self-contained (no external files needed) — you can email it, AirDrop it, or drop it in a shared drive and anyone can just open it in a browser.
