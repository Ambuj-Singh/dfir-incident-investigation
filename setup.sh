#!/usr/bin/env bash
# Setup script to create virtualenv and install requirements
set -euo pipefail

if [ -d ".venv" ]; then
  echo "Virtual environment already exists. Activate with: source .venv/bin/activate"
  exit 0
fi

python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. Activate virtualenv with: source .venv/bin/activate"
