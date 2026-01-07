"""Pytest configuration and fixtures for Animal Shorts Agent System tests."""

import pytest
from pathlib import Path
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
)


# ============================================================
# Input Fixtures
# ============================================================

@pytest.fixture
def sample_input_data() -> InputData:
    """Sample input data for testing."""
    return InputData(
        animal="골든 리트리버 강아지",
        situation="버려진 후 외로운 노인을 만나 서로의 가족이 됨",
        emotions=["따뜻함", "감동", "치유"],
        ending="행복한 결말",
    )


@pytest.fixture
def sample_input_dict() -> dict:
    """Sample input as dictionary."""
    return {
        "animal": "아기 고슴도치",
        "situation": "골든 리트리버에게 구조되어 함께 자람",
        "emotions": ["귀여움", "우정", "가족"],
    }


# ============================================================
# Story Fixtures
# ============================================================

@pytest.fixture
def sample_story() -> Story:
    """Sample story for testing."""
    return Story(
        title="골든 리트리버와 아기 고슴도치",
        synopsis="골든 리트리버가 구조한 아기 고슴도치와 함께 가족이 되는 이야기",
        arc=[
            StoryPhase(
                phase="도입",
                description="비 오는 날, 골든 리트리버가 무언가를 입에 물고 집에 온다",
                beats=["빗속에서 발견", "조심스럽게 물고 옴"],
                emotion="호기심, 따뜻함",
            ),
            StoryPhase(
                phase="전개",
                description="아기 고슴도치를 돌보기 시작한다",
                beats=["첫 만남", "먹이 주기"],
                emotion="보호본능, 애정",
            ),
            StoryPhase(
                phase="결말",
                description="함께 성장하며 가족이 된다",
                beats=["함께하는 일상", "가족 사진"],
                emotion="행복, 완전함",
            ),
        ],
        total_duration=90,
    )


# ============================================================
# Scene Fixtures
# ============================================================

@pytest.fixture
def sample_scenes() -> list[Scene]:
    """Sample scenes for testing."""
    return [
        Scene(
            id=1,
            title="발견",
            title_en="Discovery",
            duration=15,
            description="골든 리트리버가 아기 고슴도치를 발견한다",
            action="입에 조심스럽게 물고 온다",
            emotion="호기심, 조심스러움",
            camera=CameraSettings(
                movement="slow dolly in",
                angle="medium shot",
                transition="fade from black",
            ),
            lighting="warm afternoon light",
            key_elements=["골든 리트리버", "아기 고슴도치", "거실"],
        ),
        Scene(
            id=2,
            title="첫 만남",
            title_en="First Meeting",
            duration=12,
            description="담요 위에 내려놓고 코를 댄다",
            action="부드럽게 코로 쿡쿡 찌른다",
            emotion="부드러움, 신뢰",
            camera=CameraSettings(
                movement="static",
                angle="close-up",
            ),
            lighting="soft indoor light",
            key_elements=["담요", "교감 장면"],
        ),
    ]


# ============================================================
# Prompt Fixtures
# ============================================================

@pytest.fixture
def sample_prompts() -> list[Prompt]:
    """Sample prompts for testing."""
    return [
        Prompt(
            scene_id=1,
            english="A golden retriever with cream-colored fur carefully carries a tiny hedgehog...",
            korean="크림색 털의 골든 리트리버가 작은 고슴도치를 조심스럽게 물고...",
            structure=PromptStructure(
                character_desc="golden retriever with cream-colored fur",
                setting="cozy living room, afternoon",
                action="carefully carries a tiny hedgehog in its mouth",
                camera="slow dolly in, medium shot",
                lighting="warm afternoon light through window",
                atmosphere="curious and gentle",
            ),
            quality_score=85,
        ),
    ]


# ============================================================
# Title Fixtures
# ============================================================

@pytest.fixture
def sample_titles() -> TitleSet:
    """Sample title set for testing."""
    return TitleSet(
        main_title="골든 리트리버가 데려온 작은 손님",
        subtitle="솔방울 가족의 시작",
        platform_variants=PlatformTitles(
            youtube_shorts="💕 골든 리트리버가 뭔가를 물고왔는데... (실화)",
            instagram_reels="강아지가 데려온 특별한 손님 🦔✨",
            tiktok="우리 강아지가 이걸 물고왔어... 결말 보고 울었음 😭",
        ),
        hooks=TitleHooks(
            emotional="눈물 없이 못 보는 골든 리트리버 이야기",
            curiosity="강아지가 물고 온 것의 정체는?",
            outcome="예상치 못한 가족이 된 둘",
        ),
    )


# ============================================================
# Character Fixtures
# ============================================================

@pytest.fixture
def sample_character() -> Character:
    """Sample character for testing."""
    return Character(
        id="char_golden_001",
        name="뽀삐",
        species="golden retriever",
        visual_description=VisualDescription(
            fur="soft cream-colored fluffy fur",
            eyes="warm brown expressive eyes",
            size="medium-sized adult",
            distinctive_features=["slightly floppy ears", "white chest patch"],
        ),
        sora2_prompt_fragment="A golden retriever with soft cream-colored fluffy fur, warm brown expressive eyes, slightly floppy ears, and a white patch on its chest",
        personality_traits=["gentle", "protective", "curious"],
    )


# ============================================================
# Project Fixtures
# ============================================================

@pytest.fixture
def sample_project(
    sample_input_data,
    sample_story,
    sample_scenes,
    sample_prompts,
    sample_titles,
) -> Project:
    """Sample complete project for testing."""
    return Project(
        id="proj_test_001",
        slug="test-project",
        name="테스트 프로젝트",
        status=ProjectStatus.DRAFT,
        input_data=sample_input_data,
        story=sample_story,
        scenes=sample_scenes,
        prompts=sample_prompts,
        titles=sample_titles,
    )


# ============================================================
# Path Fixtures
# ============================================================

@pytest.fixture
def test_output_dir(tmp_path) -> Path:
    """Temporary directory for test outputs."""
    output_dir = tmp_path / "test_output"
    output_dir.mkdir()
    return output_dir


@pytest.fixture
def test_projects_dir(tmp_path) -> Path:
    """Temporary directory for test projects."""
    projects_dir = tmp_path / "test_projects"
    projects_dir.mkdir()
    return projects_dir
