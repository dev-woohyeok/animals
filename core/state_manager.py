"""State Manager - Session and project state management."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from .models import Project, SessionState, ProjectStatus
from utils import get_logger, ensure_dir, load_yaml, save_yaml, get_timestamp


class StateManager:
    """
    Manages session state and project persistence.

    Handles:
    - Current session state tracking
    - Project save/load operations
    - History management
    - State transitions
    """

    def __init__(self, projects_dir: str | Path | None = None):
        """
        Initialize state manager.

        Args:
            projects_dir: Directory for project storage
        """
        self.logger = get_logger("StateManager")

        # Set projects directory
        if projects_dir is None:
            projects_dir = Path(__file__).parent.parent / "projects"
        self.projects_dir = Path(projects_dir)
        ensure_dir(self.projects_dir)

        # Initialize session state
        self._session = SessionState()
        self._history: list[dict[str, Any]] = []

    @property
    def session(self) -> SessionState:
        """Get current session state."""
        return self._session

    @property
    def current_step(self) -> str:
        """Get current workflow step."""
        return self._session.current_step

    @property
    def project(self) -> Project | None:
        """Get current project."""
        return self._session.project

    def set_step(self, step: str) -> None:
        """
        Set current workflow step.

        Args:
            step: New step name
        """
        old_step = self._session.current_step
        self._session.current_step = step

        # Record in history
        self._add_history_entry("step_change", {
            "from": old_step,
            "to": step,
        })

        self.logger.debug(f"Step changed: {old_step} -> {step}")

    def set_project(self, project: Project) -> None:
        """
        Set current project.

        Args:
            project: Project to set as current
        """
        self._session.project = project
        self._add_history_entry("project_set", {
            "project_id": project.id,
            "project_name": project.name,
        })

    def _add_history_entry(
        self,
        action: str,
        data: dict[str, Any],
    ) -> None:
        """Add entry to session history."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "data": data,
        }
        self._history.append(entry)
        self._session.history.append(entry)

    def get_history(self) -> list[dict[str, Any]]:
        """Get session history."""
        return self._history.copy()

    def clear_history(self) -> None:
        """Clear session history."""
        self._history.clear()
        self._session.history.clear()

    # ============================================================
    # Project Persistence
    # ============================================================

    def save_project(self, project: Project | None = None) -> Path:
        """
        Save project to disk.

        Args:
            project: Project to save (uses current if not specified)

        Returns:
            Path to saved project file
        """
        if project is None:
            project = self._session.project

        if project is None:
            raise ValueError("No project to save")

        # Update timestamp
        project.updated_at = datetime.now()

        # Create project directory
        project_dir = self.projects_dir / project.slug
        ensure_dir(project_dir)

        # Save main project file
        project_file = project_dir / "project.json"
        project_data = project.model_dump(mode="json")

        with open(project_file, "w", encoding="utf-8") as f:
            json.dump(project_data, f, ensure_ascii=False, indent=2)

        self.logger.info(f"Project saved: {project_file}")
        self._add_history_entry("project_saved", {
            "project_id": project.id,
            "path": str(project_file),
        })

        return project_file

    def load_project(self, project_id_or_slug: str) -> Project:
        """
        Load project from disk.

        Args:
            project_id_or_slug: Project ID or slug to load

        Returns:
            Loaded Project instance
        """
        # Try as slug first
        project_dir = self.projects_dir / project_id_or_slug
        project_file = project_dir / "project.json"

        if not project_file.exists():
            # Search by ID
            project_file = self._find_project_by_id(project_id_or_slug)

        if project_file is None or not project_file.exists():
            raise FileNotFoundError(
                f"Project not found: {project_id_or_slug}"
            )

        with open(project_file, "r", encoding="utf-8") as f:
            project_data = json.load(f)

        project = Project(**project_data)
        self._session.project = project

        self.logger.info(f"Project loaded: {project.name}")
        self._add_history_entry("project_loaded", {
            "project_id": project.id,
            "project_name": project.name,
        })

        return project

    def _find_project_by_id(self, project_id: str) -> Path | None:
        """Find project file by ID."""
        for project_dir in self.projects_dir.iterdir():
            if not project_dir.is_dir():
                continue

            project_file = project_dir / "project.json"
            if not project_file.exists():
                continue

            with open(project_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data.get("id") == project_id:
                    return project_file

        return None

    def list_projects(self) -> list[dict[str, Any]]:
        """
        List all saved projects.

        Returns:
            List of project summaries
        """
        projects = []

        for project_dir in sorted(
            self.projects_dir.iterdir(),
            key=lambda p: p.stat().st_mtime if p.is_dir() else 0,
            reverse=True,
        ):
            if not project_dir.is_dir():
                continue

            project_file = project_dir / "project.json"
            if not project_file.exists():
                continue

            try:
                with open(project_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

                projects.append({
                    "id": data.get("id"),
                    "slug": data.get("slug"),
                    "name": data.get("name"),
                    "status": data.get("status"),
                    "created_at": data.get("created_at"),
                    "updated_at": data.get("updated_at"),
                })
            except Exception as e:
                self.logger.warning(f"Error loading project {project_dir}: {e}")

        return projects

    def delete_project(self, project_id_or_slug: str) -> bool:
        """
        Delete a project.

        Args:
            project_id_or_slug: Project ID or slug to delete

        Returns:
            True if deleted successfully
        """
        import shutil

        project_dir = self.projects_dir / project_id_or_slug

        if not project_dir.exists():
            # Try to find by ID
            project_file = self._find_project_by_id(project_id_or_slug)
            if project_file:
                project_dir = project_file.parent

        if not project_dir.exists():
            return False

        shutil.rmtree(project_dir)
        self.logger.info(f"Project deleted: {project_dir}")

        return True

    # ============================================================
    # State Snapshots
    # ============================================================

    def create_snapshot(self, name: str | None = None) -> dict[str, Any]:
        """
        Create a snapshot of current state.

        Args:
            name: Optional snapshot name

        Returns:
            Snapshot dictionary
        """
        snapshot = {
            "name": name or f"snapshot_{get_timestamp()}",
            "timestamp": datetime.now().isoformat(),
            "step": self._session.current_step,
            "project": (
                self._session.project.model_dump(mode="json")
                if self._session.project else None
            ),
        }

        self._add_history_entry("snapshot_created", {
            "name": snapshot["name"],
        })

        return snapshot

    def restore_snapshot(self, snapshot: dict[str, Any]) -> None:
        """
        Restore state from snapshot.

        Args:
            snapshot: Snapshot dictionary to restore
        """
        self._session.current_step = snapshot.get("step", "input")

        if snapshot.get("project"):
            self._session.project = Project(**snapshot["project"])

        self._add_history_entry("snapshot_restored", {
            "name": snapshot.get("name"),
        })

    # ============================================================
    # Reset Operations
    # ============================================================

    def reset_session(self) -> None:
        """Reset current session to initial state."""
        self._session = SessionState()
        self._history.clear()
        self.logger.info("Session reset")

    def reset_to_step(self, step: str) -> None:
        """
        Reset session to a specific step.

        Args:
            step: Step to reset to
        """
        self._session.current_step = step
        self._session.pending_confirmations.clear()

        self._add_history_entry("reset_to_step", {"step": step})
        self.logger.info(f"Reset to step: {step}")
