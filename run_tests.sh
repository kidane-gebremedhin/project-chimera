#!/bin/bash
# Quick test runner script for Project Chimera

set -e

echo "=========================================="
echo "Running Project Chimera Tests"
echo "=========================================="
echo ""

# Check if uv is available
if ! command -v uv &> /dev/null; then
    echo "❌ Error: uv is not installed"
    echo "Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "📦 Syncing dependencies..."
uv sync --extra dev

echo ""
echo "🧪 Running tests (expecting all to fail)..."
echo ""

# Run tests with verbose output
uv run pytest tests/ -v --tb=short

echo ""
echo "=========================================="
echo "Test run complete!"
echo "=========================================="
echo ""
echo "Note: All tests should fail at this stage (TDD approach)."
echo "This is expected - tests define behavior before implementation."
