"""History Manager - Track changes and enable rollback."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, TypeVar, Generic
from dataclasses import dataclass, field
from enum import Enum
from copy import deepcopy

from .models import Project, Story, Scene, Prompt
from utils import get_logger, ensure_dir


T = TypeVar("T")


class ChangeType(Enum):
    """Types of changes."""
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    REGENERATE = "regenerate"
    MERGE = "merge"


@dataclass
class HistoryEntry:
    """Single history entry."""
    id: str
    timestamp: datetime
    change_type: ChangeType
    target_type: str  # "project", "story", "scene", "prompt"
    target_id: str
    description: str
    before_state: dict | None
    after_state: dict | None
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "change_type": self.change_type.value,
            "target_type": self.target_type,
            "target_id": self.target_id,
            "description": self.description,
            "before_state": self.before_state,
            "after_state": self.after_state,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "HistoryEntry":
        return cls(
            id=data["id"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            change_type=ChangeType(data["change_type"]),
            target_type=data["target_type"],
            target_id=data["target_id"],
            description=data["description"],
            before_state=data.get("before_state"),
            after_state=data.get("after_state"),
            metadata=data.get("metadata", {}),
        )


class HistoryManager:
    """
    Manages change history and enables rollback.

    Features:
    - Track all changes to projects, stories, scenes, prompts
    - View history timeline
    - Rollback to previous states
    - Compare historical versions
    """

    def __init__(self, history_dir: str | Path | None = None):
        """
        Initialize history manager.

        Args:
            history_dir: Directory for history storage
        """
        self.logger = get_logger("HistoryManager")

        if history_dir is None:
            history_dir = Path(__file__).parent.parent / "projects" / ".history"

        self.history_dir = Path(history_dir)
        ensure_dir(self.history_dir)

        # In-memory history (per project)
        self._histories: dict[str, list[HistoryEntry]] = {}
        self._entry_counter = 0

    # ============================================================
    # Recording Changes
    # ============================================================

    def record_change(
        self,
        project_slug: str,
        change_type: ChangeType,
        target_type: str,
        target_id: str,
        description: str,
        before_state: Any = None,
        after_state: Any = None,
        metadata: dict | None = None,
    ) -> HistoryEntry:
        """
        Record a change in history.

        Args:
            project_slug: Project identifier
            change_type: Type of change
            target_type: What was changed (project, story, scene, prompt)
            target_id: ID of the changed item
            description: Human-readable description
            before_state: State before change (will be serialized)
            after_state: State after change (will be serialized)
            metadata: Additional metadata

        Returns:
            Created HistoryEntry
        """
        self._entry_counter += 1
        entry_id = f"h_{project_slug}_{self._entry_counter}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # Serialize states
        before_dict = self._serialize_state(before_state)
        after_dict = self._serialize_state(after_state)

        entry = HistoryEntry(
            id=entry_id,
            timestamp=datetime.now(),
            change_type=change_type,
            target_type=target_type,
            target_id=target_id,
            description=description,
            before_state=before_dict,
            after_state=after_dict,
            metadata=metadata or {},
        )

        # Add to history
        if project_slug not in self._histories:
            self._histories[project_slug] = []

        self._histories[project_slug].append(entry)

        self.logger.debug(f"Recorded: {description}")

        return entry

    def _serialize_state(self, state: Any) -> dict | None:
        """Serialize state to dict."""
        if state is None:
            return None

        if hasattr(state, "model_dump"):
            return state.model_dump(mode="json")
        elif hasattr(state, "to_dict"):
            return state.to_dict()
        elif isinstance(state, dict):
            return deepcopy(state)
        else:
            return {"value": str(state)}

    # ============================================================
    # Convenience Recording Methods
    # ============================================================

    def record_story_change(
        self,
        project_slug: str,
        story: Story,
        change_type: ChangeType = ChangeType.UPDATE,
        description: str = "",
        before_story: Story | None = None,
    ) -> HistoryEntry:
        """Record a story change."""
        return self.record_change(
            project_slug=project_slug,
            change_type=change_type,
            target_type="story",
            target_id=story.title,
            description=description or f"스토리 변경: {story.title}",
            before_state=before_story,
            after_state=story,
        )

    def record_scene_change(
        self,
        project_slug: str,
        scene: Scene,
        change_type: ChangeType = ChangeType.UPDATE,
        description: str = "",
        before_scene: Scene | None = None,
    ) -> HistoryEntry:
        """Record a scene change."""
        return self.record_change(
            project_slug=project_slug,
            change_type=change_type,
            target_type="scene",
            target_id=str(scene.scene_number),
            description=description or f"씬 {scene.scene_number} 변경",
            before_state=before_scene,
            after_state=scene,
        )

    def record_prompt_change(
        self,
        project_slug: str,
        prompt: Prompt,
        change_type: ChangeType = ChangeType.UPDATE,
        description: str = "",
        before_prompt: Prompt | None = None,
    ) -> HistoryEntry:
        """Record a prompt change."""
        return self.record_change(
            project_slug=project_slug,
            change_type=change_type,
            target_type="prompt",
            target_id=str(prompt.scene_id),
            description=description or f"프롬프트 {prompt.scene_id} 변경",
            before_state=before_prompt,
            after_state=prompt,
        )

    # ============================================================
    # History Retrieval
    # ============================================================

    def get_history(
        self,
        project_slug: str,
        limit: int | None = None,
        target_type: str | None = None,
        target_id: str | None = None,
    ) -> list[HistoryEntry]:
        """
        Get history entries.

        Args:
            project_slug: Project identifier
            limit: Maximum entries to return
            target_type: Filter by target type
            target_id: Filter by target ID

        Returns:
            List of history entries (newest first)
        """
        entries = self._histories.get(project_slug, [])

        # Apply filters
        if target_type:
            entries = [e for e in entries if e.target_type == target_type]

        if target_id:
            entries = [e for e in entries if e.target_id == target_id]

        # Sort by timestamp (newest first)
        entries = sorted(entries, key=lambda e: e.timestamp, reverse=True)

        # Apply limit
        if limit:
            entries = entries[:limit]

        return entries

    def get_entry(self, project_slug: str, entry_id: str) -> HistoryEntry | None:
        """Get specific history entry by ID."""
        entries = self._histories.get(project_slug, [])

        for entry in entries:
            if entry.id == entry_id:
                return entry

        return None

    def get_latest(
        self,
        project_slug: str,
        target_type: str,
        target_id: str,
    ) -> HistoryEntry | None:
        """Get the latest entry for a specific target."""
        entries = self.get_history(
            project_slug,
            target_type=target_type,
            target_id=target_id,
            limit=1,
        )
        return entries[0] if entries else None

    # ============================================================
    # Rollback
    # ============================================================

    def rollback(
        self,
        project_slug: str,
        entry_id: str,
    ) -> dict | None:
        """
        Rollback to a previous state.

        Args:
            project_slug: Project identifier
            entry_id: Entry to rollback to

        Returns:
            The before_state from that entry, or None if not found
        """
        entry = self.get_entry(project_slug, entry_id)

        if not entry:
            self.logger.warning(f"Entry not found: {entry_id}")
            return None

        if not entry.before_state:
            self.logger.warning(f"No before_state for: {entry_id}")
            return None

        # Record the rollback as a new entry
        self.record_change(
            project_slug=project_slug,
            change_type=ChangeType.UPDATE,
            target_type=entry.target_type,
            target_id=entry.target_id,
            description=f"롤백: {entry.description}",
            before_state=entry.after_state,
            after_state=entry.before_state,
            metadata={"rollback_from": entry_id},
        )

        self.logger.info(f"Rolled back to: {entry_id}")

        return entry.before_state

    def can_rollback(self, project_slug: str, entry_id: str) -> bool:
        """Check if rollback is possible for an entry."""
        entry = self.get_entry(project_slug, entry_id)
        return entry is not None and entry.before_state is not None

    # ============================================================
    # Persistence
    # ============================================================

    def save_history(self, project_slug: str) -> Path:
        """
        Save history to disk.

        Args:
            project_slug: Project identifier

        Returns:
            Path to saved file
        """
        project_history_dir = self.history_dir / project_slug
        ensure_dir(project_history_dir)

        file_path = project_history_dir / "history.json"

        entries = self._histories.get(project_slug, [])
        data = {
            "project_slug": project_slug,
            "saved_at": datetime.now().isoformat(),
            "entry_count": len(entries),
            "entries": [e.to_dict() for e in entries],
        }

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        self.logger.info(f"Saved {len(entries)} entries for {project_slug}")

        return file_path

    def load_history(self, project_slug: str) -> list[HistoryEntry]:
        """
        Load history from disk.

        Args:
            project_slug: Project identifier

        Returns:
            List of loaded entries
        """
        file_path = self.history_dir / project_slug / "history.json"

        if not file_path.exists():
            return []

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        entries = [
            HistoryEntry.from_dict(e)
            for e in data.get("entries", [])
        ]

        self._histories[project_slug] = entries
        self.logger.info(f"Loaded {len(entries)} entries for {project_slug}")

        return entries

    # ============================================================
    # History Viewer
    # ============================================================

    def format_timeline(
        self,
        project_slug: str,
        limit: int = 20,
    ) -> str:
        """
        Format history as a timeline view.

        Args:
            project_slug: Project identifier
            limit: Maximum entries to show

        Returns:
            Formatted timeline string
        """
        entries = self.get_history(project_slug, limit=limit)

        if not entries:
            return "히스토리가 없습니다."

        lines = [
            "# 변경 히스토리",
            "",
            f"프로젝트: {project_slug}",
            f"총 {len(self._histories.get(project_slug, []))}개 항목 중 최근 {len(entries)}개 표시",
            "",
            "---",
            "",
        ]

        for entry in entries:
            time_str = entry.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            type_emoji = self._get_change_emoji(entry.change_type)

            lines.append(f"### {type_emoji} {entry.description}")
            lines.append(f"- **시간:** {time_str}")
            lines.append(f"- **대상:** {entry.target_type} ({entry.target_id})")
            lines.append(f"- **ID:** `{entry.id}`")

            if entry.metadata:
                lines.append(f"- **메타:** {entry.metadata}")

            lines.append("")

        return "\n".join(lines)

    def _get_change_emoji(self, change_type: ChangeType) -> str:
        """Get emoji for change type."""
        mapping = {
            ChangeType.CREATE: "✨",
            ChangeType.UPDATE: "📝",
            ChangeType.DELETE: "🗑️",
            ChangeType.REGENERATE: "🔄",
            ChangeType.MERGE: "🔀",
        }
        return mapping.get(change_type, "•")

    def format_entry_detail(self, entry: HistoryEntry) -> str:
        """Format a single entry in detail."""
        lines = [
            f"# 변경 상세: {entry.id}",
            "",
            f"**시간:** {entry.timestamp.strftime('%Y-%m-%d %H:%M:%S')}",
            f"**타입:** {entry.change_type.value}",
            f"**대상:** {entry.target_type} ({entry.target_id})",
            f"**설명:** {entry.description}",
            "",
        ]

        if entry.before_state:
            lines.append("## Before")
            lines.append("```json")
            lines.append(json.dumps(entry.before_state, ensure_ascii=False, indent=2)[:500])
            lines.append("```")
            lines.append("")

        if entry.after_state:
            lines.append("## After")
            lines.append("```json")
            lines.append(json.dumps(entry.after_state, ensure_ascii=False, indent=2)[:500])
            lines.append("```")

        return "\n".join(lines)

    # ============================================================
    # Cleanup
    # ============================================================

    def clear_history(self, project_slug: str) -> int:
        """
        Clear all history for a project.

        Args:
            project_slug: Project identifier

        Returns:
            Number of entries cleared
        """
        count = len(self._histories.get(project_slug, []))
        self._histories[project_slug] = []

        # Remove saved file
        file_path = self.history_dir / project_slug / "history.json"
        if file_path.exists():
            file_path.unlink()

        self.logger.info(f"Cleared {count} entries for {project_slug}")

        return count

    def prune_history(
        self,
        project_slug: str,
        keep_count: int = 100,
    ) -> int:
        """
        Prune old history entries.

        Args:
            project_slug: Project identifier
            keep_count: Number of entries to keep

        Returns:
            Number of entries removed
        """
        entries = self._histories.get(project_slug, [])

        if len(entries) <= keep_count:
            return 0

        # Sort by timestamp and keep newest
        sorted_entries = sorted(entries, key=lambda e: e.timestamp, reverse=True)
        self._histories[project_slug] = sorted_entries[:keep_count]

        removed = len(entries) - keep_count
        self.logger.info(f"Pruned {removed} old entries for {project_slug}")

        return removed
