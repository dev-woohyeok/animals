"""Tests for agent classes."""

import pytest
from unittest.mock import Mock, patch

from agents import (
    BaseAgent,
    InputAgent,
    StoryAgent,
    SceneAgent,
    PromptAgent,
    TranslationAgent,
    TitleAgent,
    ConfirmAgent,
    OutputAgent,
)
from core.models import InputData, Story, Scene, Prompt


class TestBaseAgent:
    """Tests for BaseAgent class."""

    def test_base_agent_initialization(self):
        """Test that BaseAgent can be subclassed."""
        # BaseAgent is abstract, we test via InputAgent
        agent = InputAgent()
        assert agent.name == "InputAgent"

    def test_log_method(self):
        """Test logging functionality."""
        agent = InputAgent()
        # Should not raise
        agent.log("Test message")


class TestInputAgent:
    """Tests for InputAgent."""

    def test_process_input_data(self, sample_input_data):
        """Test processing InputData."""
        agent = InputAgent()
        result = agent.process(sample_input_data)

        assert isinstance(result, InputData)
        assert result.animal == sample_input_data.animal

    def test_process_dict_input(self, sample_input_dict):
        """Test processing dictionary input."""
        agent = InputAgent()
        result = agent.process(sample_input_dict)

        assert isinstance(result, InputData)
        assert result.animal == sample_input_dict["animal"]

    def test_normalize_text(self):
        """Test text normalization."""
        agent = InputAgent()
        result = agent.process({
            "animal": "  골든 리트리버  ",
            "situation": "테스트 상황",
        })

        assert result.animal == "골든 리트리버"


class TestStoryAgent:
    """Tests for StoryAgent."""

    def test_initialization(self):
        """Test StoryAgent initialization."""
        agent = StoryAgent()
        assert agent.name == "StoryAgent"

    @patch.object(StoryAgent, '_call_claude')
    def test_process_returns_story(self, mock_claude, sample_input_data):
        """Test that process returns a Story."""
        mock_claude.return_value = '''
        {
            "title": "테스트 스토리",
            "synopsis": "테스트 시놉시스",
            "arc": [
                {"phase": "도입", "description": "시작", "beats": [], "emotion": "슬픔"}
            ],
            "total_duration": 90
        }
        '''
        agent = StoryAgent()
        result = agent.process(sample_input_data)

        assert isinstance(result, Story)
        assert result.title == "테스트 스토리"


class TestSceneAgent:
    """Tests for SceneAgent."""

    def test_initialization(self):
        """Test SceneAgent initialization."""
        agent = SceneAgent()
        assert agent.name == "SceneAgent"


class TestPromptAgent:
    """Tests for PromptAgent."""

    def test_initialization(self):
        """Test PromptAgent initialization."""
        agent = PromptAgent()
        assert agent.name == "PromptAgent"

    def test_build_character_description(self, sample_character):
        """Test character description building."""
        agent = PromptAgent()
        desc = agent._build_character_description(sample_character)

        assert "golden retriever" in desc


class TestTranslationAgent:
    """Tests for TranslationAgent."""

    def test_initialization(self):
        """Test TranslationAgent initialization."""
        agent = TranslationAgent()
        assert agent.name == "TranslationAgent"


class TestTitleAgent:
    """Tests for TitleAgent."""

    def test_initialization(self):
        """Test TitleAgent initialization."""
        agent = TitleAgent()
        assert agent.name == "TitleAgent"

    def test_default_titles_creation(self, sample_story):
        """Test default title creation."""
        agent = TitleAgent()
        titles = agent._create_default_titles(sample_story)

        assert titles.main_title == sample_story.title
        assert titles.platform_variants is not None


class TestConfirmAgent:
    """Tests for ConfirmAgent."""

    def test_initialization(self):
        """Test ConfirmAgent initialization."""
        agent = ConfirmAgent()
        assert agent.name == "ConfirmAgent"
        assert agent.console is not None


class TestOutputAgent:
    """Tests for OutputAgent."""

    def test_initialization(self):
        """Test OutputAgent initialization."""
        agent = OutputAgent()
        assert agent.name == "OutputAgent"

    def test_get_clipboard_text(self, sample_prompts):
        """Test clipboard text generation."""
        agent = OutputAgent()
        text = agent.get_clipboard_text(sample_prompts)

        assert "SCENE 1" in text
        assert sample_prompts[0].english in text
