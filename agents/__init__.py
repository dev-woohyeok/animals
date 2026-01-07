"""Agents module for Animal Shorts Agent System."""

from .base import BaseAgent
from .input_agent import InputAgent
from .story_agent import StoryAgent
from .scene_agent import SceneAgent
from .prompt_agent import PromptAgent
from .translation_agent import TranslationAgent
from .title_agent import TitleAgent
from .confirm_agent import ConfirmAgent
from .output_agent import OutputAgent

# Phase 2 agents
from .validation_agent import ValidationAgent
from .version_agent import VersionAgent, PromptVersion
from .regen_agent import RegenAgent

# Phase 3 agents
from .compare_agent import CompareAgent, DiffType, DiffResult

__all__ = [
    # Core agents
    "BaseAgent",
    "InputAgent",
    "StoryAgent",
    "SceneAgent",
    "PromptAgent",
    "TranslationAgent",
    "TitleAgent",
    "ConfirmAgent",
    "OutputAgent",
    # Phase 2 agents
    "ValidationAgent",
    "VersionAgent",
    "PromptVersion",
    "RegenAgent",
    # Phase 3 agents
    "CompareAgent",
    "DiffType",
    "DiffResult",
]
