#!/usr/bin/env bash

set -e

DIR="$HOME/videos/ytwl"
PYTHON="$HOME/anaconda3/bin/python"

{
  echo "Getting YouTube videos from watch later list"
  echo "Date: $(date)"
  echo "Directory: $(pwd)"
  echo "User: $(whoami)"
  "$PYTHON" --version

  cd "$DIR"
  echo "Changed directory to: $(pwd)"

  "$PYTHON" ./getNow.py

  echo "Done"
} > "$DIR/get.log" 2>&1
