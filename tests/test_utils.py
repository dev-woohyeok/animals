"""Tests for utility functions."""

import pytest
from pathlib import Path

from utils import (
    load_yaml,
    save_yaml,
    get_logger,
    ensure_dir,
    slugify,
    get_timestamp,
)
from utils.helpers import truncate_text, load_config


class TestYamlUtils:
    """Tests for YAML utilities."""

    def test_save_and_load_yaml(self, tmp_path):
        """Test saving and loading YAML."""
        data = {
            "name": "테스트",
            "value": 123,
            "nested": {"key": "value"},
        }
        file_path = tmp_path / "test.yaml"

        save_yaml(data, file_path)
        loaded = load_yaml(file_path)

        assert loaded["name"] == "테스트"
        assert loaded["value"] == 123
        assert loaded["nested"]["key"] == "value"

    def test_load_yaml_not_found(self):
        """Test loading non-existent YAML."""
        with pytest.raises(FileNotFoundError):
            load_yaml("/non/existent/path.yaml")

    def test_save_yaml_creates_directory(self, tmp_path):
        """Test that save_yaml creates parent directories."""
        file_path = tmp_path / "nested" / "dir" / "test.yaml"
        save_yaml({"test": True}, file_path)

        assert file_path.exists()


class TestLogger:
    """Tests for logging utilities."""

    def test_get_logger(self):
        """Test logger creation."""
        logger = get_logger("test_module")

        assert logger is not None
        assert logger.name == "test_module"

    def test_get_logger_cached(self):
        """Test that logger is cached."""
        logger1 = get_logger("cached_test")
        logger2 = get_logger("cached_test")

        assert logger1 is logger2

    def test_logger_with_file(self, tmp_path):
        """Test logger with file output."""
        log_file = tmp_path / "test.log"
        logger = get_logger("file_test", log_file=log_file)

        logger.info("Test message")

        # File should exist after logging
        assert log_file.exists()


class TestFileSystemUtils:
    """Tests for file system utilities."""

    def test_ensure_dir(self, tmp_path):
        """Test directory creation."""
        new_dir = tmp_path / "new" / "nested" / "dir"
        result = ensure_dir(new_dir)

        assert result.exists()
        assert result.is_dir()

    def test_ensure_dir_existing(self, tmp_path):
        """Test ensure_dir on existing directory."""
        result = ensure_dir(tmp_path)

        assert result == tmp_path


class TestStringUtils:
    """Tests for string utilities."""

    def test_slugify_basic(self):
        """Test basic slugification."""
        assert slugify("Hello World") == "hello-world"

    def test_slugify_korean(self):
        """Test slugification with Korean."""
        result = slugify("골든 리트리버")
        assert "골든" in result
        assert " " not in result

    def test_slugify_special_chars(self):
        """Test slugification removes special chars."""
        result = slugify("Test!@#$%String")
        assert "!" not in result
        assert "@" not in result

    def test_slugify_max_length(self):
        """Test slugification max length."""
        long_text = "a" * 100
        result = slugify(long_text, max_length=50)

        assert len(result) <= 50

    def test_slugify_empty(self):
        """Test slugification of empty string."""
        result = slugify("")
        assert result == "untitled"

    def test_get_timestamp(self):
        """Test timestamp generation."""
        ts = get_timestamp()

        assert len(ts) == 15  # YYYYMMDD_HHMMSS format

    def test_get_timestamp_custom_format(self):
        """Test timestamp with custom format."""
        ts = get_timestamp("%Y-%m-%d")

        assert "-" in ts
        assert len(ts) == 10

    def test_truncate_text(self):
        """Test text truncation."""
        text = "This is a long text that needs truncation"
        result = truncate_text(text, max_length=20)

        assert len(result) == 20
        assert result.endswith("...")

    def test_truncate_text_short(self):
        """Test truncation of short text."""
        text = "Short"
        result = truncate_text(text, max_length=20)

        assert result == text


class TestConfigUtils:
    """Tests for configuration utilities."""

    def test_load_config_default(self):
        """Test loading default config."""
        # This assumes config.yaml exists in project root
        try:
            config = load_config()
            assert isinstance(config, dict)
        except FileNotFoundError:
            pytest.skip("config.yaml not found in expected location")
