#!/usr/bin/env python3
"""
Transcribe a Curse of Strahd session recording locally using Whisper via MLX
(Apple Silicon-accelerated - Metal/Neural Engine, no cloud API, no API key).

Setup (once):   bash scripts/setup-whisper.sh
Usage:          source ~/whisper-env/bin/activate
                python3 scripts/transcribe.py <audio-file> [session-number]

Example:
    python3 scripts/transcribe.py ~/Downloads/session3.m4a 03

Writes transcripts/session-<NN>-raw.txt (plain text) and
       transcripts/session-<NN>-raw.json (text + per-segment timestamps)

Model: defaults to whisper-large-v3-turbo (fast, ~near-large-v3 accuracy).
For max accuracy instead of speed, change MODEL below to
"mlx-community/whisper-large-v3-mlx" - on 32GB RAM either runs comfortably.
"""
import sys
import os
import json

MODEL = "mlx-community/whisper-large-v3-turbo"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 transcribe.py <audio-file> [session-number]")
        sys.exit(1)

    try:
        import mlx_whisper
    except ImportError:
        print("mlx-whisper isn't installed. Run: bash scripts/setup-whisper.sh")
        sys.exit(1)

    audio_path = sys.argv[1]
    if not os.path.exists(audio_path):
        print(f"Audio file not found: {audio_path}")
        sys.exit(1)

    session_num = sys.argv[2] if len(sys.argv) > 2 else "XX"

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(repo_root, "transcripts")
    os.makedirs(out_dir, exist_ok=True)

    print(f"Transcribing {audio_path} with {MODEL} ...")
    print("(first run downloads the model from Hugging Face - a few GB, one-time)")

    result = mlx_whisper.transcribe(audio_path, path_or_hf_repo=MODEL)

    out_txt = os.path.join(out_dir, f"session-{session_num}-raw.txt")
    with open(out_txt, "w") as f:
        f.write(result["text"].strip() + "\n")

    out_json = os.path.join(out_dir, f"session-{session_num}-raw.json")
    with open(out_json, "w") as f:
        json.dump(result, f, indent=2)

    print("Done.")
    print(f"  Plain text:       {out_txt}")
    print(f"  With timestamps:  {out_json}")
    print("Now pull the highlights into a new sessions/session-XX-*.md using TEMPLATE.md.")


if __name__ == "__main__":
    main()
