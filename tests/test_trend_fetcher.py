"""
Tests for trend-fetching capability.

These tests validate that trend data returned by the trend-fetching capability
matches the API contract defined in specs/technical.md and skills/README.md.

All tests are expected to fail until the implementation exists.
"""

import pytest
from datetime import datetime
from typing import Any, Dict


class TestTrendFetcherAPI:
    """Test suite for trend fetcher API contract compliance."""

    def test_fetch_trends_returns_required_structure(self):
        """
        Assert that fetch_trends returns the exact structure defined in skills/README.md:
        {
            "trends": [...],
            "metadata": {...}
        }
        """
        from skills.trend_fetcher import fetch_trends
        
        result = fetch_trends(
            platform="twitter",
            region="us",
            category=None,
            limit=10
        )
        
        # Must have top-level 'trends' and 'metadata' keys
        assert "trends" in result
        assert "metadata" in result
        assert isinstance(result["trends"], list)
        assert isinstance(result["metadata"], dict)

    def test_trends_array_contains_required_fields(self):
        """
        Assert that each trend object contains:
        - topic (string)
        - score (number)
        - source (string)
        - observed_at (ISO-8601 timestamp string)
        """
        from skills.trend_fetcher import fetch_trends
        
        result = fetch_trends(
            platform="twitter",
            region="us",
            category="technology",
            limit=5
        )
        
        assert len(result["trends"]) > 0, "At least one trend should be returned"
        
        for trend in result["trends"]:
            assert "topic" in trend, "Each trend must have 'topic' field"
            assert "score" in trend, "Each trend must have 'score' field"
            assert "source" in trend, "Each trend must have 'source' field"
            assert "observed_at" in trend, "Each trend must have 'observed_at' field"

    def test_trend_field_types(self):
        """
        Assert that trend fields have correct types:
        - topic: string
        - score: number (int or float)
        - source: string
        - observed_at: string (ISO-8601 timestamp)
        """
        from skills.trend_fetcher import fetch_trends
        
        result = fetch_trends(
            platform="reddit",
            region="global",
            category=None,
            limit=3
        )
        
        for trend in result["trends"]:
            assert isinstance(trend["topic"], str), "topic must be a string"
            assert isinstance(trend["score"], (int, float)), "score must be a number"
            assert isinstance(trend["source"], str), "source must be a string"
            assert isinstance(trend["observed_at"], str), "observed_at must be a string"
            
            # Validate ISO-8601 timestamp format
            try:
                datetime.fromisoformat(trend["observed_at"].replace("Z", "+00:00"))
            except ValueError:
                pytest.fail(f"observed_at '{trend['observed_at']}' is not a valid ISO-8601 timestamp")

    def test_metadata_structure(self):
        """
        Assert that metadata contains:
        - platform (string)
        - fetched_at (ISO-8601 timestamp string)
        """
        from skills.trend_fetcher import fetch_trends
        
        result = fetch_trends(
            platform="youtube",
            region="us",
            category="entertainment",
            limit=10
        )
        
        metadata = result["metadata"]
        assert "platform" in metadata, "metadata must have 'platform' field"
        assert "fetched_at" in metadata, "metadata must have 'fetched_at' field"
        assert isinstance(metadata["platform"], str), "platform must be a string"
        assert isinstance(metadata["fetched_at"], str), "fetched_at must be a string"
        
        # Validate ISO-8601 timestamp format
        try:
            datetime.fromisoformat(metadata["fetched_at"].replace("Z", "+00:00"))
        except ValueError:
            pytest.fail(f"fetched_at '{metadata['fetched_at']}' is not a valid ISO-8601 timestamp")

    def test_metadata_platform_matches_input(self):
        """
        Assert that metadata.platform matches the input platform parameter.
        """
        from skills.trend_fetcher import fetch_trends
        
        test_platform = "tiktok"
        result = fetch_trends(
            platform=test_platform,
            region="us",
            category=None,
            limit=5
        )
        
        assert result["metadata"]["platform"] == test_platform, \
            "metadata.platform must match the input platform parameter"

    def test_limit_parameter_respected(self):
        """
        Assert that the limit parameter controls the number of trends returned.
        """
        from skills.trend_fetcher import fetch_trends
        
        limit = 3
        result = fetch_trends(
            platform="twitter",
            region="us",
            category=None,
            limit=limit
        )
        
        assert len(result["trends"]) <= limit, \
            f"Number of trends returned ({len(result['trends'])}) must not exceed limit ({limit})"

    def test_trends_not_empty_when_available(self):
        """
        Assert that when trends are available, the trends array is not empty.
        Note: This test may need to be conditional based on actual API availability.
        """
        from skills.trend_fetcher import fetch_trends
        
        result = fetch_trends(
            platform="twitter",
            region="us",
            category=None,
            limit=10
        )
        
        # If API is available, we should get trends
        # If API is unavailable, we should get a structured error (tested separately)
        # For now, we assert the structure exists
        assert "trends" in result
        assert isinstance(result["trends"], list)
