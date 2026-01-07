"""Data models for Animal Shorts Agent System."""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ProjectStatus(str, Enum):
    """Project status enum."""
    DRAFT = "draft"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class EmotionType(str, Enum):
    """Emotion type enum for scenes."""
    SADNESS = "sadness"
    HOPE = "hope"
    JOY = "joy"
    TENSION = "tension"
    PEACE = "peace"
    WARMTH = "warmth"
    LONELINESS = "loneliness"


# ============================================================
# Input Models
# ============================================================

class InputData(BaseModel):
    """User input data structure."""
    animal: str = Field(..., description="동물 종류 (예: 골든 리트리버 강아지)")
    situation: str = Field(..., description="상황 설명 (예: 버려진 후 노인을 만남)")
    emotions: list[str] = Field(default_factory=list, description="감정 키워드들")
    ending: Optional[str] = Field(None, description="결말 (선택)")
    template_id: Optional[str] = Field(None, description="사용할 스토리 템플릿 ID")
    character_id: Optional[str] = Field(None, description="사용할 캐릭터 ID")


# ============================================================
# Character Models
# ============================================================

class VisualDescription(BaseModel):
    """Character visual description."""
    fur: Optional[str] = Field(None, description="털/외피 설명")
    eyes: Optional[str] = Field(None, description="눈 설명")
    size: Optional[str] = Field(None, description="크기/나이")
    distinctive_features: list[str] = Field(default_factory=list, description="특징")


class Character(BaseModel):
    """Character definition for consistency."""
    id: str = Field(..., description="고유 ID")
    name: Optional[str] = Field(None, description="캐릭터 이름 (한글)")
    species: str = Field(..., description="종 (영문)")
    visual_description: VisualDescription
    sora2_prompt_fragment: str = Field(..., description="Sora2용 설명 문장")
    personality_traits: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)
    used_in_projects: list[str] = Field(default_factory=list)


# ============================================================
# Story Models
# ============================================================

class StoryBeat(BaseModel):
    """Individual story beat."""
    description: str
    emotion: str


class StoryPhase(BaseModel):
    """Story phase (도입, 전개, 위기, 해결, 결말)."""
    phase: str = Field(..., description="단계명")
    description: str
    beats: list[str] = Field(default_factory=list)
    emotion: str


class EmotionPoint(BaseModel):
    """Point on emotional journey."""
    position: float = Field(..., ge=0, le=1, description="0-1 사이 위치")
    emotion: str
    intensity: int = Field(..., ge=0, le=100)


class Story(BaseModel):
    """Complete story structure."""
    title: str
    synopsis: str = Field(..., description="1-2문장 요약")
    arc: list[StoryPhase] = Field(default_factory=list)
    character_development: Optional[str] = None
    emotional_journey: list[EmotionPoint] = Field(default_factory=list)
    total_duration: int = Field(default=90, description="예상 총 길이 (초)")


# ============================================================
# Scene Models
# ============================================================

class CameraSettings(BaseModel):
    """Camera settings for a scene."""
    movement: str = Field(..., description="카메라 움직임 (dolly, tracking, static)")
    angle: str = Field(..., description="앵글 (wide, medium, close-up)")
    transition: Optional[str] = Field(None, description="이전 장면과의 전환")


class Scene(BaseModel):
    """Individual scene definition."""
    id: int
    title: str
    title_en: Optional[str] = None
    duration: int = Field(default=15, description="장면 길이 (초)")
    description: str
    action: str = Field(..., description="주요 동작")
    emotion: str
    camera: CameraSettings
    lighting: str
    key_elements: list[str] = Field(default_factory=list)


# ============================================================
# Prompt Models
# ============================================================

class PromptStructure(BaseModel):
    """Structured prompt components."""
    character_desc: str = Field(..., description="캐릭터 외형 설명")
    setting: str = Field(..., description="배경/장소")
    action: str = Field(..., description="동작/행동")
    camera: str = Field(..., description="카메라 워크")
    lighting: str = Field(..., description="조명")
    atmosphere: str = Field(..., description="분위기/감정")


class Prompt(BaseModel):
    """Sora2 prompt for a scene."""
    scene_id: int
    english: str = Field(..., description="영어 프롬프트 (Sora2용)")
    korean: Optional[str] = Field(None, description="한국어 번역 (참고용)")
    structure: PromptStructure
    tokens_estimate: Optional[int] = None
    quality_score: Optional[int] = Field(None, ge=0, le=100)


# ============================================================
# Title Models
# ============================================================

class PlatformTitles(BaseModel):
    """Platform-specific title variants."""
    youtube_shorts: str = Field(..., max_length=100)
    instagram_reels: str
    tiktok: str


class TitleHooks(BaseModel):
    """Different hook styles for titles."""
    emotional: str = Field(..., description="감정 자극형")
    curiosity: str = Field(..., description="호기심 유발형")
    outcome: str = Field(..., description="결과 강조형")


class TitleSet(BaseModel):
    """Complete title set for a project."""
    main_title: str = Field(..., description="메인 제목")
    subtitle: Optional[str] = None
    platform_variants: PlatformTitles
    hooks: TitleHooks


# ============================================================
# Validation Models
# ============================================================

class ScoreBreakdown(BaseModel):
    """Quality score breakdown."""
    specificity: int = Field(..., ge=0, le=100, description="구체성")
    sora2_compatibility: int = Field(..., ge=0, le=100, description="Sora2 호환성")
    emotional_clarity: int = Field(..., ge=0, le=100, description="감정 명확성")
    technical_accuracy: int = Field(..., ge=0, le=100, description="기술 정확성")


class ValidationIssue(BaseModel):
    """Validation issue."""
    severity: str = Field(..., description="심각도: error, warning, info")
    message: str
    suggestion: Optional[str] = None


class ValidationResult(BaseModel):
    """Prompt validation result."""
    score: int = Field(..., ge=0, le=100)
    breakdown: ScoreBreakdown
    issues: list[ValidationIssue] = Field(default_factory=list)
    suggestions: list[str] = Field(default_factory=list)
    is_valid: bool = True


class ConsistencyReport(BaseModel):
    """Consistency check report."""
    is_consistent: bool
    character_match: float = Field(..., ge=0, le=1)
    style_match: float = Field(..., ge=0, le=1)
    background_continuity: float = Field(..., ge=0, le=1)
    issues: list[str] = Field(default_factory=list)


# ============================================================
# Project Models
# ============================================================

class ProjectSummary(BaseModel):
    """Project summary statistics."""
    total_scenes: int
    total_duration: str  # e.g., "90s"
    average_quality_score: Optional[float] = None


class Project(BaseModel):
    """Complete project structure."""
    id: str
    slug: str
    name: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    status: ProjectStatus = ProjectStatus.DRAFT

    # References
    character_id: Optional[str] = None
    template_id: Optional[str] = None
    style_id: str = "cinematic_realistic"

    # Content
    input_data: Optional[InputData] = None
    character: Optional[Character] = None
    story: Optional[Story] = None
    scenes: list[Scene] = Field(default_factory=list)
    prompts: list[Prompt] = Field(default_factory=list)
    titles: Optional[TitleSet] = None

    # Metadata
    current_version: int = 1
    summary: Optional[ProjectSummary] = None


# ============================================================
# Session State
# ============================================================

class SessionState(BaseModel):
    """Current session state for workflow management."""
    current_step: str = "input"  # input, story, scene, prompt, title, confirm, output
    project: Optional[Project] = None
    pending_confirmations: list[str] = Field(default_factory=list)
    history: list[dict] = Field(default_factory=list)
