"""Tests for core data models."""

import pytest
from datetime import datetime

from core.models import (
    InputData,
    Story,
    StoryPhase,
    Scene,
    CameraSettings,
    Prompt,
    PromptStructure,
    TitleSet,
    PlatformTitles,
    TitleHooks,
    Character,
    VisualDescription,
    Project,
    ProjectStatus,
    ValidationResult,
    ScoreBreakdown,
)


class TestInputData:
    """Tests for InputData model."""

    def test_create_basic(self):
        """Test basic InputData creation."""
        data = InputData(
            animal="골든 리트리버",
            situation="버려진 강아지가 구조됨",
        )
        assert data.animal == "골든 리트리버"
        assert data.situation == "버려진 강아지가 구조됨"
        assert data.emotions == []

    def test_create_with_all_fields(self):
        """Test InputData with all fields."""
        data = InputData(
            animal="아기 고양이",
            situation="길에서 구조됨",
            emotions=["슬픔", "희망"],
            ending="행복한 결말",
            template_id="rescue_reunion",
            character_id="char_001",
        )
        assert len(data.emotions) == 2
        assert data.ending == "행복한 결말"


class TestStory:
    """Tests for Story model."""

    def test_create_story(self, sample_story):
        """Test Story creation."""
        assert sample_story.title == "골든 리트리버와 아기 고슴도치"
        assert len(sample_story.arc) == 3
        assert sample_story.total_duration == 90

    def test_story_phases(self, sample_story):
        """Test story phases."""
        phases = [phase.phase for phase in sample_story.arc]
        assert "도입" in phases
        assert "결말" in phases


class TestScene:
    """Tests for Scene model."""

    def test_create_scene(self, sample_scenes):
        """Test Scene creation."""
        scene = sample_scenes[0]
        assert scene.id == 1
        assert scene.title == "발견"
        assert scene.duration == 15

    def test_camera_settings(self, sample_scenes):
        """Test CameraSettings."""
        camera = sample_scenes[0].camera
        assert camera.movement == "slow dolly in"
        assert camera.angle == "medium shot"


class TestPrompt:
    """Tests for Prompt model."""

    def test_create_prompt(self, sample_prompts):
        """Test Prompt creation."""
        prompt = sample_prompts[0]
        assert prompt.scene_id == 1
        assert "golden retriever" in prompt.english
        assert prompt.korean is not None

    def test_prompt_structure(self, sample_prompts):
        """Test PromptStructure."""
        structure = sample_prompts[0].structure
        assert structure.character_desc != ""
        assert structure.camera != ""


class TestTitleSet:
    """Tests for TitleSet model."""

    def test_create_title_set(self, sample_titles):
        """Test TitleSet creation."""
        assert sample_titles.main_title != ""
        assert sample_titles.platform_variants is not None
        assert sample_titles.hooks is not None

    def test_platform_variants(self, sample_titles):
        """Test platform-specific titles."""
        variants = sample_titles.platform_variants
        assert len(variants.youtube_shorts) <= 100  # YouTube limit
        assert variants.instagram_reels != ""
        assert variants.tiktok != ""

    def test_hooks(self, sample_titles):
        """Test title hooks."""
        hooks = sample_titles.hooks
        assert hooks.emotional != ""
        assert hooks.curiosity != ""
        assert hooks.outcome != ""


class TestCharacter:
    """Tests for Character model."""

    def test_create_character(self, sample_character):
        """Test Character creation."""
        assert sample_character.id == "char_golden_001"
        assert sample_character.species == "golden retriever"

    def test_visual_description(self, sample_character):
        """Test VisualDescription."""
        visual = sample_character.visual_description
        assert visual.fur is not None
        assert visual.eyes is not None

    def test_sora2_fragment(self, sample_character):
        """Test Sora2 prompt fragment."""
        assert "golden retriever" in sample_character.sora2_prompt_fragment


class TestProject:
    """Tests for Project model."""

    def test_create_project(self, sample_project):
        """Test Project creation."""
        assert sample_project.id == "proj_test_001"
        assert sample_project.status == ProjectStatus.DRAFT

    def test_project_has_all_components(self, sample_project):
        """Test Project has all components."""
        assert sample_project.input_data is not None
        assert sample_project.story is not None
        assert sample_project.scenes is not None
        assert sample_project.prompts is not None
        assert sample_project.titles is not None

    def test_project_status_enum(self):
        """Test ProjectStatus enum."""
        assert ProjectStatus.DRAFT == "draft"
        assert ProjectStatus.IN_PROGRESS == "in_progress"
        assert ProjectStatus.COMPLETED == "completed"


class TestValidationResult:
    """Tests for ValidationResult model."""

    def test_create_validation_result(self):
        """Test ValidationResult creation."""
        result = ValidationResult(
            score=85,
            breakdown=ScoreBreakdown(
                specificity=90,
                sora2_compatibility=80,
                emotional_clarity=85,
                technical_accuracy=85,
            ),
            is_valid=True,
        )
        assert result.score == 85
        assert result.is_valid
        assert result.breakdown.specificity == 90
