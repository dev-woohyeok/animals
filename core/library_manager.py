"""Library Manager - Manage characters, templates, and best practices."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from .models import Character, VisualDescription
from utils import get_logger, ensure_dir, slugify


class LibraryManager:
    """
    Manages the library of reusable assets.

    Features:
    - Character library CRUD
    - Story template management
    - Best practices database
    - Search and filter
    """

    def __init__(self, library_dir: str | Path | None = None):
        """
        Initialize library manager.

        Args:
            library_dir: Base directory for library storage
        """
        self.logger = get_logger("LibraryManager")

        if library_dir is None:
            library_dir = Path(__file__).parent.parent / "library"

        self.library_dir = Path(library_dir)
        self.characters_dir = self.library_dir / "characters"
        self.templates_dir = self.library_dir / "templates"
        self.best_practices_dir = self.library_dir / "best_practices"

        # Ensure directories exist
        ensure_dir(self.characters_dir)
        ensure_dir(self.templates_dir)
        ensure_dir(self.best_practices_dir)

        # Cache
        self._characters_cache: dict[str, Character] = {}
        self._templates_cache: dict[str, dict] = {}

    # ============================================================
    # Character Management
    # ============================================================

    def create_character(
        self,
        name: str,
        species: str,
        visual_description: dict[str, Any],
        personality_traits: list[str] | None = None,
    ) -> Character:
        """
        Create a new character.

        Args:
            name: Character name (Korean)
            species: Species in English
            visual_description: Dict with fur, eyes, size, distinctive_features
            personality_traits: Optional personality traits

        Returns:
            Created Character object
        """
        char_id = f"char_{slugify(species)}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # Build visual description
        vis_desc = VisualDescription(
            fur=visual_description.get("fur"),
            eyes=visual_description.get("eyes"),
            size=visual_description.get("size"),
            distinctive_features=visual_description.get("distinctive_features", []),
        )

        # Build Sora2 prompt fragment
        sora2_fragment = self._build_sora2_fragment(species, vis_desc)

        character = Character(
            id=char_id,
            name=name,
            species=species,
            visual_description=vis_desc,
            sora2_prompt_fragment=sora2_fragment,
            personality_traits=personality_traits or [],
        )

        # Save to disk
        self._save_character(character)
        self._characters_cache[char_id] = character

        self.logger.info(f"Created character: {char_id}")
        return character

    def _build_sora2_fragment(
        self,
        species: str,
        vis_desc: VisualDescription,
    ) -> str:
        """Build Sora2-compatible character description."""
        parts = [f"A {species}"]

        if vis_desc.fur:
            parts.append(f"with {vis_desc.fur}")

        if vis_desc.eyes:
            parts.append(f"{vis_desc.eyes}")

        if vis_desc.size:
            parts.insert(1, vis_desc.size)

        if vis_desc.distinctive_features:
            features = ", ".join(vis_desc.distinctive_features)
            parts.append(f"featuring {features}")

        return " ".join(parts)

    def _save_character(self, character: Character) -> Path:
        """Save character to YAML file."""
        file_path = self.characters_dir / f"{character.id}.yaml"

        data = character.model_dump(mode="json")

        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

        return file_path

    def get_character(self, char_id: str) -> Character | None:
        """
        Get character by ID.

        Args:
            char_id: Character ID

        Returns:
            Character or None if not found
        """
        # Check cache
        if char_id in self._characters_cache:
            return self._characters_cache[char_id]

        # Load from disk
        file_path = self.characters_dir / f"{char_id}.yaml"
        if not file_path.exists():
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        character = Character(**data)
        self._characters_cache[char_id] = character
        return character

    def list_characters(
        self,
        species_filter: str | None = None,
    ) -> list[dict[str, Any]]:
        """
        List all characters.

        Args:
            species_filter: Optional species to filter by

        Returns:
            List of character summaries
        """
        characters = []

        for file_path in self.characters_dir.glob("*.yaml"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)

                if species_filter and data.get("species") != species_filter:
                    continue

                characters.append({
                    "id": data.get("id"),
                    "name": data.get("name"),
                    "species": data.get("species"),
                    "created_at": data.get("created_at"),
                })
            except Exception as e:
                self.logger.warning(f"Error loading {file_path}: {e}")

        return sorted(characters, key=lambda x: x.get("created_at", ""), reverse=True)

    def update_character(
        self,
        char_id: str,
        updates: dict[str, Any],
    ) -> Character | None:
        """
        Update a character.

        Args:
            char_id: Character ID
            updates: Fields to update

        Returns:
            Updated Character or None
        """
        character = self.get_character(char_id)
        if not character:
            return None

        # Apply updates
        data = character.model_dump()
        for key, value in updates.items():
            if key in data:
                data[key] = value

        # Rebuild if visual description changed
        if "visual_description" in updates:
            vis_desc = VisualDescription(**data["visual_description"])
            data["sora2_prompt_fragment"] = self._build_sora2_fragment(
                data["species"], vis_desc
            )

        updated = Character(**data)
        self._save_character(updated)
        self._characters_cache[char_id] = updated

        return updated

    def delete_character(self, char_id: str) -> bool:
        """
        Delete a character.

        Args:
            char_id: Character ID

        Returns:
            True if deleted
        """
        file_path = self.characters_dir / f"{char_id}.yaml"

        if file_path.exists():
            file_path.unlink()
            self._characters_cache.pop(char_id, None)
            self.logger.info(f"Deleted character: {char_id}")
            return True

        return False

    def search_characters(self, query: str) -> list[Character]:
        """
        Search characters by name or species.

        Args:
            query: Search query

        Returns:
            List of matching Characters
        """
        query_lower = query.lower()
        results = []

        for file_path in self.characters_dir.glob("*.yaml"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)

                name = data.get("name", "").lower()
                species = data.get("species", "").lower()

                if query_lower in name or query_lower in species:
                    results.append(Character(**data))

            except Exception as e:
                self.logger.warning(f"Error searching {file_path}: {e}")

        return results

    # ============================================================
    # Template Management
    # ============================================================

    def get_template(self, template_id: str) -> dict[str, Any] | None:
        """
        Get story template by ID.

        Args:
            template_id: Template ID

        Returns:
            Template dict or None
        """
        if template_id in self._templates_cache:
            return self._templates_cache[template_id]

        file_path = self.templates_dir / f"{template_id}.yaml"
        if not file_path.exists():
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        self._templates_cache[template_id] = data
        return data

    def list_templates(self) -> list[dict[str, Any]]:
        """
        List all templates.

        Returns:
            List of template summaries
        """
        templates = []

        for file_path in self.templates_dir.glob("*.yaml"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)

                templates.append({
                    "id": data.get("id", file_path.stem),
                    "name": data.get("name"),
                    "description": data.get("description"),
                    "category": data.get("category"),
                })
            except Exception as e:
                self.logger.warning(f"Error loading template {file_path}: {e}")

        return templates

    def create_template(
        self,
        template_id: str,
        name: str,
        description: str,
        story_structure: dict[str, Any],
        category: str = "general",
    ) -> dict[str, Any]:
        """
        Create a new template.

        Args:
            template_id: Unique identifier
            name: Template name
            description: Template description
            story_structure: Story structure definition
            category: Template category

        Returns:
            Created template dict
        """
        template = {
            "id": template_id,
            "name": name,
            "description": description,
            "category": category,
            "story_structure": story_structure,
            "created_at": datetime.now().isoformat(),
        }

        file_path = self.templates_dir / f"{template_id}.yaml"

        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(template, f, allow_unicode=True, default_flow_style=False)

        self._templates_cache[template_id] = template
        self.logger.info(f"Created template: {template_id}")

        return template

    # ============================================================
    # Best Practices
    # ============================================================

    def get_best_practices(self, category: str = "sora2") -> dict[str, Any] | None:
        """
        Get best practices for a category.

        Args:
            category: Category (sora2, story, camera, etc.)

        Returns:
            Best practices dict
        """
        file_path = self.best_practices_dir / f"{category}_tips.yaml"
        if not file_path.exists():
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get_prompt_tips(self) -> list[str]:
        """Get Sora2 prompt writing tips."""
        practices = self.get_best_practices("sora2")
        if not practices:
            return []

        tips = []
        for section in practices.get("sections", []):
            tips.extend(section.get("tips", []))

        return tips

    def get_camera_suggestions(self, emotion: str) -> list[str]:
        """
        Get camera suggestions for an emotion.

        Args:
            emotion: Target emotion

        Returns:
            List of camera movement suggestions
        """
        practices = self.get_best_practices("camera")
        if not practices:
            # Default suggestions
            return [
                "slow dolly in for intimacy",
                "static with slight movement for stability",
                "handheld for authenticity",
            ]

        emotion_lower = emotion.lower()
        for mapping in practices.get("emotion_camera_mapping", []):
            if emotion_lower in mapping.get("emotions", []):
                return mapping.get("camera_suggestions", [])

        return practices.get("default_suggestions", [])
