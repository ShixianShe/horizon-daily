#!/bin/bash
# Horizon Daily — run aggregation, convert to bilingual, and send via email
set -e
cd "$(dirname "$0")"

echo "===== Horizon Daily Pipeline ====="
echo ""

echo "Step 1/2: Running Horizon (fetch + analyze + summarize)..."
uv run horizon
echo ""

echo "Step 2/2: Converting to bilingual & sending email..."
uv run python bilingual.py
echo ""

echo "Done! Check your email for the bilingual briefing."
