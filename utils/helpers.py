"""Utility helper functions for Animal Shorts Agent System."""

import logging
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


# ============================================================
# YAML Utilities
# ============================================================

def load_yaml(file_path: str | Path) -> dict[str, Any]:
    """
    Load YAML file and return as dictionary.

    Args:
        file_path: Path to YAML file

    Returns:
        Dictionary containing YAML content

    Raises:
        FileNotFoundError: If file doesn't exist
        yaml.YAMLError: If YAML parsing fails
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"YAML file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_yaml(data: dict[str, Any], file_path: str | Path) -> None:
    """
    Save dictionary to YAML file.

    Args:
        data: Dictionary to save
        file_path: Path to save YAML file
    """
    path = Path(file_path)
    ensure_dir(path.parent)

    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )


# ============================================================
# Logging Utilities
# ============================================================

_loggers: dict[str, logging.Logger] = {}


def get_logger(
    name: str,
    level: int = logging.INFO,
    log_file: str | Path | None = None,
) -> logging.Logger:
    """
    Get or create a logger with consistent formatting.

    Args:
        name: Logger name (usually module name)
        level: Logging level
        log_file: Optional file path for file logging

    Returns:
        Configured logger instance
    """
    if name in _loggers:
        return _loggers[name]

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers
    if logger.handlers:
        return logger

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_format = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(name)s: %(message)s",
        datefmt="%H:%M:%S"
    )
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    # File handler (optional)
    if log_file:
        file_path = Path(log_file)
        ensure_dir(file_path.parent)
        file_handler = logging.FileHandler(file_path, encoding="utf-8")
        file_handler.setLevel(level)
        file_format = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(name)s - %(filename)s:%(lineno)d: %(message)s"
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

    _loggers[name] = logger
    return logger


# ============================================================
# File System Utilities
# ============================================================

def ensure_dir(dir_path: str | Path) -> Path:
    """
    Ensure directory exists, create if not.

    Args:
        dir_path: Directory path

    Returns:
        Path object of the directory
    """
    path = Path(dir_path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent


# ============================================================
# String Utilities
# ============================================================

def slugify(text: str, max_length: int = 50) -> str:
    """
    Convert text to URL/file-safe slug.

    Args:
        text: Text to convert
        max_length: Maximum length of slug

    Returns:
        Slugified text
    """
    # Convert to lowercase and replace spaces
    slug = text.lower().strip()
    slug = re.sub(r"[\s_]+", "-", slug)

    # Remove non-alphanumeric characters (keep Korean, English, numbers, hyphens)
    slug = re.sub(r"[^\w가-힣-]", "", slug)

    # Remove multiple hyphens
    slug = re.sub(r"-+", "-", slug)

    # Trim hyphens from ends
    slug = slug.strip("-")

    # Truncate to max length
    if len(slug) > max_length:
        slug = slug[:max_length].rstrip("-")

    return slug or "untitled"


def get_timestamp(format_str: str = "%Y%m%d_%H%M%S") -> str:
    """
    Get current timestamp as formatted string.

    Args:
        format_str: strftime format string

    Returns:
        Formatted timestamp string
    """
    return datetime.now().strftime(format_str)


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to max length with suffix.

    Args:
        text: Text to truncate
        max_length: Maximum length including suffix
        suffix: Suffix to add if truncated

    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


# ============================================================
# Config Utilities
# ============================================================

_config_cache: dict[str, Any] | None = None


def load_config(config_path: str | Path | None = None) -> dict[str, Any]:
    """
    Load main configuration file with caching.

    Args:
        config_path: Optional custom config path

    Returns:
        Configuration dictionary
    """
    global _config_cache

    if _config_cache is not None and config_path is None:
        return _config_cache

    if config_path is None:
        config_path = get_project_root() / "config.yaml"

    config = load_yaml(config_path)

    if config_path is None:
        _config_cache = config

    return config


def get_style_config(style_id: str) -> dict[str, Any]:
    """
    Load style configuration by ID.

    Args:
        style_id: Style identifier (e.g., "cinematic_realistic")

    Returns:
        Style configuration dictionary
    """
    style_path = get_project_root() / "config" / "styles" / f"{style_id}.yaml"
    return load_yaml(style_path)


def get_template(template_id: str) -> dict[str, Any]:
    """
    Load story template by ID.

    Args:
        template_id: Template identifier

    Returns:
        Template configuration dictionary
    """
    template_path = get_project_root() / "library" / "templates" / f"{template_id}.yaml"
    return load_yaml(template_path)
