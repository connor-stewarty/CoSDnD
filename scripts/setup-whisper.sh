#!/usr/bin/env bash
# One-time setup: installs mlx-whisper (Apple Silicon-accelerated Whisper) in a
# dedicated virtual environment. Run this once from Terminal on your Mac:
#
#   bash scripts/setup-whisper.sh
#
set -e

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg not found - installing via Homebrew..."
  if ! command -v brew >/dev/null 2>&1; then
    echo "Homebrew isn't installed. Install it from https://brew.sh first, then re-run this script."
    exit 1
  fi
  brew install ffmpeg
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 not found. Install Python 3 (e.g. 'brew install python') and re-run this script."
  exit 1
fi

echo "Creating virtual environment at ~/whisper-env ..."
python3 -m venv ~/whisper-env
source ~/whisper-env/bin/activate
pip install --upgrade pip
pip install mlx-whisper

echo ""
echo "Setup complete."
echo "Next time, activate the environment with:"
echo "    source ~/whisper-env/bin/activate"
echo "Then transcribe a session with:"
echo "    python3 scripts/transcribe.py <path-to-audio-file> <session-number>"
