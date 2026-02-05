# Running Tests

## Prerequisites

Ensure you have `uv` installed. If not, install it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup

1. **Install dependencies** (including dev dependencies):
   ```bash
   uv sync --extra dev
   ```

## Running Tests

Run all tests:
```bash
uv run pytest tests/ -v
```

Run with more detailed output:
```bash
uv run pytest tests/ -v --tb=short
```

Run a specific test file:
```bash
uv run pytest tests/test_trend_fetcher.py -v
uv run pytest tests/test_skills_interface.py -v
```

Run a specific test:
```bash
uv run pytest tests/test_trend_fetcher.py::TestTrendFetcherAPI::test_fetch_trends_returns_required_structure -v
```

## Expected Behavior

**All tests should FAIL** at this stage because:
- The skill modules don't exist yet (`skills/trend_fetcher.py`, `skills/fetch_trends.py`, etc.)
- The implementations are not written

Expected failure types:
- `ModuleNotFoundError`: When importing non-existent modules
- `ImportError`: When modules exist but functions don't
- `AssertionError`: When functions exist but don't match the contract

This is **correct behavior** for TDD - tests define the expected behavior before implementation.

## Verifying Failures

To verify all tests fail as expected:

```bash
# Count total tests
uv run pytest tests/ --collect-only -q

# Run and see failure summary
uv run pytest tests/ -v --tb=line | grep -E "(FAILED|ERROR|test_)"
```
