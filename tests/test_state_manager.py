"""Tests for StateManager."""

import pytest
from pathlib import Path

from core.state_manager import StateManager
from core.models import Project, ProjectStatus


class TestStateManager:
    """Tests for StateManager class."""

    def test_initialization(self, test_projects_dir):
        """Test StateManager initialization."""
        manager = StateManager(projects_dir=test_projects_dir)

        assert manager.projects_dir == test_projects_dir
        assert manager.session is not None
        assert manager.current_step == "input"

    def test_set_step(self, test_projects_dir):
        """Test setting workflow step."""
        manager = StateManager(projects_dir=test_projects_dir)

        manager.set_step("story")
        assert manager.current_step == "story"

        manager.set_step("scene")
        assert manager.current_step == "scene"

    def test_set_project(self, test_projects_dir, sample_project):
        """Test setting current project."""
        manager = StateManager(projects_dir=test_projects_dir)

        manager.set_project(sample_project)
        assert manager.project == sample_project

    def test_history_tracking(self, test_projects_dir):
        """Test history is tracked."""
        manager = StateManager(projects_dir=test_projects_dir)

        manager.set_step("story")
        manager.set_step("scene")

        history = manager.get_history()
        assert len(history) == 2

    def test_clear_history(self, test_projects_dir):
        """Test clearing history."""
        manager = StateManager(projects_dir=test_projects_dir)

        manager.set_step("story")
        manager.clear_history()

        assert len(manager.get_history()) == 0

    def test_save_project(self, test_projects_dir, sample_project):
        """Test saving project to disk."""
        manager = StateManager(projects_dir=test_projects_dir)
        manager.set_project(sample_project)

        path = manager.save_project()

        assert path.exists()
        assert path.name == "project.json"

    def test_load_project(self, test_projects_dir, sample_project):
        """Test loading project from disk."""
        manager = StateManager(projects_dir=test_projects_dir)
        manager.set_project(sample_project)
        manager.save_project()

        # Create new manager and load
        manager2 = StateManager(projects_dir=test_projects_dir)
        loaded = manager2.load_project(sample_project.slug)

        assert loaded.id == sample_project.id
        assert loaded.name == sample_project.name

    def test_list_projects(self, test_projects_dir, sample_project):
        """Test listing saved projects."""
        manager = StateManager(projects_dir=test_projects_dir)
        manager.set_project(sample_project)
        manager.save_project()

        projects = manager.list_projects()

        assert len(projects) == 1
        assert projects[0]["id"] == sample_project.id

    def test_delete_project(self, test_projects_dir, sample_project):
        """Test deleting project."""
        manager = StateManager(projects_dir=test_projects_dir)
        manager.set_project(sample_project)
        manager.save_project()

        result = manager.delete_project(sample_project.slug)

        assert result is True
        assert len(manager.list_projects()) == 0

    def test_create_snapshot(self, test_projects_dir, sample_project):
        """Test creating state snapshot."""
        manager = StateManager(projects_dir=test_projects_dir)
        manager.set_project(sample_project)
        manager.set_step("prompt")

        snapshot = manager.create_snapshot("test_snapshot")

        assert snapshot["name"] == "test_snapshot"
        assert snapshot["step"] == "prompt"
        assert snapshot["project"] is not None

    def test_restore_snapshot(self, test_projects_dir, sample_project):
        """Test restoring from snapshot."""
        manager = StateManager(projects_dir=test_projects_dir)
        manager.set_project(sample_project)
        manager.set_step("prompt")

        snapshot = manager.create_snapshot()
        manager.set_step("output")

        manager.restore_snapshot(snapshot)

        assert manager.current_step == "prompt"

    def test_reset_session(self, test_projects_dir, sample_project):
        """Test resetting session."""
        manager = StateManager(projects_dir=test_projects_dir)
        manager.set_project(sample_project)
        manager.set_step("output")

        manager.reset_session()

        assert manager.current_step == "input"
        assert manager.project is None
