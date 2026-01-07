"""Core module for Animal Shorts Agent System."""

from .models import (
    InputData,
    Character,
    Story,
    Scene,
    Prompt,
    TitleSet,
    Project,
    ProjectStatus,
    SessionState,
    ValidationResult,
    ConsistencyReport,
)
from .state_manager import StateManager
from .orchestrator import Orchestrator, WorkflowStep
from .library_manager import LibraryManager
from .style_manager import StyleManager, StylePreset
from .history_manager import HistoryManager, HistoryEntry, ChangeType

__all__ = [
    # Models
    "InputData",
    "Character",
    "Story",
    "Scene",
    "Prompt",
    "TitleSet",
    "Project",
    "ProjectStatus",
    "SessionState",
    "ValidationResult",
    "ConsistencyReport",
    # Core
    "StateManager",
    "Orchestrator",
    "WorkflowStep",
    "LibraryManager",
    "StyleManager",
    "StylePreset",
    # Phase 3
    "HistoryManager",
    "HistoryEntry",
    "ChangeType",
]
