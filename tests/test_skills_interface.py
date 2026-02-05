"""
Tests for skills interface parameter validation.

These tests assert that each skill module accepts the parameters defined in
skills/README.md and raises clear errors for missing or incorrect parameters.

All tests are expected to fail until the implementation exists.
"""

import pytest
from typing import Any


class TestSkillFetchTrendsInterface:
    """Test parameter validation for skill_fetch_trends."""

    def test_accepts_valid_parameters(self):
        """
        Assert that skill_fetch_trends accepts all required parameters:
        - platform (string)
        - region (string)
        - category (string | null)
        - limit (number)
        """
        from skills.fetch_trends import skill_fetch_trends
        
        result = skill_fetch_trends(
            platform="twitter",
            region="us",
            category="technology",
            limit=10
        )
        
        # Should not raise an error
        assert result is not None

    def test_accepts_null_category(self):
        """
        Assert that skill_fetch_trends accepts null category parameter.
        """
        from skills.fetch_trends import skill_fetch_trends
        
        result = skill_fetch_trends(
            platform="twitter",
            region="us",
            category=None,
            limit=10
        )
        
        assert result is not None

    def test_raises_error_on_missing_platform(self):
        """
        Assert that missing 'platform' parameter raises a clear error.
        """
        from skills.fetch_trends import skill_fetch_trends
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_fetch_trends(
                region="us",
                category=None,
                limit=10
            )
        
        assert "platform" in str(exc_info.value).lower(), \
            "Error message should mention 'platform' parameter"

    def test_raises_error_on_missing_region(self):
        """
        Assert that missing 'region' parameter raises a clear error.
        """
        from skills.fetch_trends import skill_fetch_trends
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_fetch_trends(
                platform="twitter",
                category=None,
                limit=10
            )
        
        assert "region" in str(exc_info.value).lower(), \
            "Error message should mention 'region' parameter"

    def test_raises_error_on_missing_limit(self):
        """
        Assert that missing 'limit' parameter raises a clear error.
        """
        from skills.fetch_trends import skill_fetch_trends
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_fetch_trends(
                platform="twitter",
                region="us",
                category=None
            )
        
        assert "limit" in str(exc_info.value).lower(), \
            "Error message should mention 'limit' parameter"

    def test_raises_error_on_invalid_platform_type(self):
        """
        Assert that incorrect platform type (non-string) raises a clear error.
        """
        from skills.fetch_trends import skill_fetch_trends
        
        with pytest.raises((TypeError, ValueError)) as exc_info:
            skill_fetch_trends(
                platform=123,  # Should be string
                region="us",
                category=None,
                limit=10
            )
        
        assert "platform" in str(exc_info.value).lower() or "type" in str(exc_info.value).lower(), \
            "Error message should mention 'platform' or 'type'"

    def test_raises_error_on_invalid_limit_type(self):
        """
        Assert that incorrect limit type (non-number) raises a clear error.
        """
        from skills.fetch_trends import skill_fetch_trends
        
        with pytest.raises((TypeError, ValueError)) as exc_info:
            skill_fetch_trends(
                platform="twitter",
                region="us",
                category=None,
                limit="ten"  # Should be number
            )
        
        assert "limit" in str(exc_info.value).lower() or "type" in str(exc_info.value).lower(), \
            "Error message should mention 'limit' or 'type'"


class TestSkillGenerateScriptInterface:
    """Test parameter validation for skill_generate_script."""

    def test_accepts_valid_parameters(self):
        """
        Assert that skill_generate_script accepts all required parameters:
        - trend_topic (string)
        - persona_id (string)
        - target_duration_seconds (number)
        - language (string)
        """
        from skills.generate_script import skill_generate_script
        
        result = skill_generate_script(
            trend_topic="AI advancements",
            persona_id="persona_001",
            target_duration_seconds=60,
            language="en"
        )
        
        assert result is not None

    def test_raises_error_on_missing_trend_topic(self):
        """Assert that missing 'trend_topic' raises a clear error."""
        from skills.generate_script import skill_generate_script
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_generate_script(
                persona_id="persona_001",
                target_duration_seconds=60,
                language="en"
            )
        
        assert "trend_topic" in str(exc_info.value).lower() or "topic" in str(exc_info.value).lower()

    def test_raises_error_on_missing_persona_id(self):
        """Assert that missing 'persona_id' raises a clear error."""
        from skills.generate_script import skill_generate_script
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_generate_script(
                trend_topic="AI advancements",
                target_duration_seconds=60,
                language="en"
            )
        
        assert "persona" in str(exc_info.value).lower() or "persona_id" in str(exc_info.value).lower()

    def test_raises_error_on_missing_target_duration(self):
        """Assert that missing 'target_duration_seconds' raises a clear error."""
        from skills.generate_script import skill_generate_script
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_generate_script(
                trend_topic="AI advancements",
                persona_id="persona_001",
                language="en"
            )
        
        assert "duration" in str(exc_info.value).lower() or "target_duration" in str(exc_info.value).lower()

    def test_raises_error_on_missing_language(self):
        """Assert that missing 'language' raises a clear error."""
        from skills.generate_script import skill_generate_script
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_generate_script(
                trend_topic="AI advancements",
                persona_id="persona_001",
                target_duration_seconds=60
            )
        
        assert "language" in str(exc_info.value).lower()


class TestSkillGenerateVideoInterface:
    """Test parameter validation for skill_generate_video."""

    def test_accepts_valid_parameters(self):
        """
        Assert that skill_generate_video accepts all required parameters:
        - script_text (string)
        - persona_id (string)
        - video_style (string)
        - aspect_ratio (string)
        - language (string)
        """
        from skills.generate_video import skill_generate_video
        
        result = skill_generate_video(
            script_text="Hello world, this is a test script.",
            persona_id="persona_001",
            video_style="modern",
            aspect_ratio="16:9",
            language="en"
        )
        
        assert result is not None

    def test_raises_error_on_missing_script_text(self):
        """Assert that missing 'script_text' raises a clear error."""
        from skills.generate_video import skill_generate_video
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_generate_video(
                persona_id="persona_001",
                video_style="modern",
                aspect_ratio="16:9",
                language="en"
            )
        
        assert "script" in str(exc_info.value).lower() or "script_text" in str(exc_info.value).lower()

    def test_raises_error_on_missing_persona_id(self):
        """Assert that missing 'persona_id' raises a clear error."""
        from skills.generate_video import skill_generate_video
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_generate_video(
                script_text="Hello world",
                video_style="modern",
                aspect_ratio="16:9",
                language="en"
            )
        
        assert "persona" in str(exc_info.value).lower() or "persona_id" in str(exc_info.value).lower()

    def test_raises_error_on_missing_video_style(self):
        """Assert that missing 'video_style' raises a clear error."""
        from skills.generate_video import skill_generate_video
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_generate_video(
                script_text="Hello world",
                persona_id="persona_001",
                aspect_ratio="16:9",
                language="en"
            )
        
        assert "style" in str(exc_info.value).lower() or "video_style" in str(exc_info.value).lower()

    def test_raises_error_on_missing_aspect_ratio(self):
        """Assert that missing 'aspect_ratio' raises a clear error."""
        from skills.generate_video import skill_generate_video
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_generate_video(
                script_text="Hello world",
                persona_id="persona_001",
                video_style="modern",
                language="en"
            )
        
        assert "aspect" in str(exc_info.value).lower() or "aspect_ratio" in str(exc_info.value).lower()

    def test_raises_error_on_missing_language(self):
        """Assert that missing 'language' raises a clear error."""
        from skills.generate_video import skill_generate_video
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_generate_video(
                script_text="Hello world",
                persona_id="persona_001",
                video_style="modern",
                aspect_ratio="16:9"
            )
        
        assert "language" in str(exc_info.value).lower()


class TestSkillPublishVideoInterface:
    """Test parameter validation for skill_publish_video."""

    def test_accepts_valid_parameters(self):
        """
        Assert that skill_publish_video accepts all required parameters:
        - platform (string)
        - video_asset_id (string)
        - caption (string)
        - hashtags (array of strings)
        - schedule_time (ISO-8601 timestamp | null)
        """
        from skills.publish_video import skill_publish_video
        
        result = skill_publish_video(
            platform="youtube",
            video_asset_id="asset_123",
            caption="Check out this video!",
            hashtags=["tech", "ai"],
            schedule_time=None
        )
        
        assert result is not None

    def test_accepts_null_schedule_time(self):
        """Assert that skill_publish_video accepts null schedule_time."""
        from skills.publish_video import skill_publish_video
        
        result = skill_publish_video(
            platform="youtube",
            video_asset_id="asset_123",
            caption="Check out this video!",
            hashtags=["tech"],
            schedule_time=None
        )
        
        assert result is not None

    def test_accepts_valid_schedule_time(self):
        """Assert that skill_publish_video accepts valid ISO-8601 schedule_time."""
        from skills.publish_video import skill_publish_video
        
        result = skill_publish_video(
            platform="youtube",
            video_asset_id="asset_123",
            caption="Check out this video!",
            hashtags=["tech"],
            schedule_time="2026-02-05T12:00:00Z"
        )
        
        assert result is not None

    def test_raises_error_on_missing_platform(self):
        """Assert that missing 'platform' raises a clear error."""
        from skills.publish_video import skill_publish_video
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_publish_video(
                video_asset_id="asset_123",
                caption="Check out this video!",
                hashtags=["tech"],
                schedule_time=None
            )
        
        assert "platform" in str(exc_info.value).lower()

    def test_raises_error_on_missing_video_asset_id(self):
        """Assert that missing 'video_asset_id' raises a clear error."""
        from skills.publish_video import skill_publish_video
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_publish_video(
                platform="youtube",
                caption="Check out this video!",
                hashtags=["tech"],
                schedule_time=None
            )
        
        assert "asset" in str(exc_info.value).lower() or "video_asset_id" in str(exc_info.value).lower()

    def test_raises_error_on_missing_caption(self):
        """Assert that missing 'caption' raises a clear error."""
        from skills.publish_video import skill_publish_video
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_publish_video(
                platform="youtube",
                video_asset_id="asset_123",
                hashtags=["tech"],
                schedule_time=None
            )
        
        assert "caption" in str(exc_info.value).lower()

    def test_raises_error_on_missing_hashtags(self):
        """Assert that missing 'hashtags' raises a clear error."""
        from skills.publish_video import skill_publish_video
        
        with pytest.raises((TypeError, ValueError, KeyError)) as exc_info:
            skill_publish_video(
                platform="youtube",
                video_asset_id="asset_123",
                caption="Check out this video!",
                schedule_time=None
            )
        
        assert "hashtag" in str(exc_info.value).lower()

    def test_raises_error_on_invalid_hashtags_type(self):
        """Assert that incorrect hashtags type (non-array) raises a clear error."""
        from skills.publish_video import skill_publish_video
        
        with pytest.raises((TypeError, ValueError)) as exc_info:
            skill_publish_video(
                platform="youtube",
                video_asset_id="asset_123",
                caption="Check out this video!",
                hashtags="tech,ai",  # Should be array
                schedule_time=None
            )
        
        assert "hashtag" in str(exc_info.value).lower() or "type" in str(exc_info.value).lower() or "array" in str(exc_info.value).lower()
