"""Version Agent - Generate and manage A/B variations."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any
from copy import deepcopy

from core.models import Prompt, Scene, Story, TitleSet, Project
from .base import BaseAgent


class PromptVersion:
    """Represents a version of a prompt."""

    def __init__(
        self,
        prompt: Prompt,
        version_id: str,
        variant_type: str,
        parent_version: str | None = None,
        metadata: dict | None = None,
    ):
        self.prompt = prompt
        self.version_id = version_id
        self.variant_type = variant_type  # "original", "variation_a", "variation_b", etc.
        self.parent_version = parent_version
        self.metadata = metadata or {}
        self.created_at = datetime.now()

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "prompt": self.prompt.model_dump(),
            "version_id": self.version_id,
            "variant_type": self.variant_type,
            "parent_version": self.parent_version,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "PromptVersion":
        """Create from dictionary."""
        instance = cls(
            prompt=Prompt(**data["prompt"]),
            version_id=data["version_id"],
            variant_type=data["variant_type"],
            parent_version=data.get("parent_version"),
            metadata=data.get("metadata", {}),
        )
        if "created_at" in data:
            instance.created_at = datetime.fromisoformat(data["created_at"])
        return instance


class VersionAgent(BaseAgent[list[PromptVersion]]):
    """
    Generates and manages A/B variations of prompts.

    Features:
    - Generate alternative versions with different styles
    - Track version history
    - Compare versions side by side
    - Save/load version sets
    """

    def __init__(self, versions_dir: str | Path | None = None):
        super().__init__(
            name="VersionAgent",
            system_prompt_path="version_system.md",
        )

        if versions_dir is None:
            versions_dir = Path(__file__).parent.parent / "projects"
        self.versions_dir = Path(versions_dir)

        # Version storage
        self._versions: dict[int, list[PromptVersion]] = {}  # scene_id -> versions

    def _get_default_system_prompt(self) -> str:
        return """You are a creative video prompt writer specializing in A/B variations.

Given an original Sora2 prompt, create alternative versions that:
1. Maintain the core story and character
2. Change specific elements (camera, lighting, mood, pacing)
3. Offer meaningfully different visual approaches

Variation types:
- camera_variation: Different camera work (angles, movement)
- mood_variation: Different emotional atmosphere
- style_variation: Different visual style (cinematic vs documentary)
- detail_variation: Different level of detail/focus

Output JSON format:
{
  "variations": [
    {
      "type": "camera_variation",
      "prompt": "Full new prompt text...",
      "changes": ["Changed X to Y", "Added Z"],
      "rationale": "Why this variation works"
    }
  ]
}"""

    def process(self, input_data: Any) -> list[PromptVersion]:
        """
        Generate variations for input prompt(s).

        Args:
            input_data: Single Prompt or list of Prompts

        Returns:
            List of PromptVersions including original and variations
        """
        if isinstance(input_data, list):
            all_versions = []
            for prompt in input_data:
                versions = self.generate_variations(prompt)
                all_versions.extend(versions)
            return all_versions

        return self.generate_variations(input_data)

    def generate_variations(
        self,
        prompt: Prompt,
        variation_types: list[str] | None = None,
        count: int = 2,
    ) -> list[PromptVersion]:
        """
        Generate variations of a prompt.

        Args:
            prompt: Original prompt to vary
            variation_types: Types of variations to generate
            count: Number of variations per type

        Returns:
            List of PromptVersions (original + variations)
        """
        if variation_types is None:
            variation_types = ["camera_variation", "mood_variation"]

        versions = []

        # Add original
        original_version = PromptVersion(
            prompt=prompt,
            version_id=f"v_{prompt.scene_id}_original",
            variant_type="original",
            metadata={"is_original": True},
        )
        versions.append(original_version)

        # Generate variations using Claude
        for var_type in variation_types:
            try:
                variation = self._generate_single_variation(
                    prompt, var_type, original_version.version_id
                )
                if variation:
                    versions.append(variation)
            except Exception as e:
                self.log(f"Error generating {var_type}: {e}")

        # Store versions
        self._versions[prompt.scene_id] = versions

        return versions

    def _generate_single_variation(
        self,
        original: Prompt,
        variation_type: str,
        parent_id: str,
    ) -> PromptVersion | None:
        """Generate a single variation."""
        user_message = f"""Create a {variation_type} for this Sora2 prompt:

Original prompt:
{original.english}

Scene info:
- Character: {original.structure.character_desc}
- Setting: {original.structure.setting}
- Action: {original.structure.action}

Generate ONE {variation_type} that offers a meaningfully different approach while keeping the core story intact."""

        try:
            response = self._call_claude(user_message)
            data = self._parse_json_response(response)

            if "variations" in data and len(data["variations"]) > 0:
                var_data = data["variations"][0]

                # Create new prompt with variation
                new_prompt = Prompt(
                    scene_id=original.scene_id,
                    english=var_data.get("prompt", original.english),
                    korean=None,  # Will need retranslation
                    structure=original.structure,  # Keep original structure
                    quality_score=None,
                )

                return PromptVersion(
                    prompt=new_prompt,
                    version_id=f"v_{original.scene_id}_{variation_type}",
                    variant_type=variation_type,
                    parent_version=parent_id,
                    metadata={
                        "changes": var_data.get("changes", []),
                        "rationale": var_data.get("rationale", ""),
                    },
                )
        except Exception as e:
            self.log(f"Variation generation failed: {e}")

        return None

    def generate_quick_variations(
        self,
        prompt: Prompt,
    ) -> list[PromptVersion]:
        """
        Generate quick variations without API call.

        Uses template-based variations for speed.
        """
        versions = []

        # Original
        versions.append(PromptVersion(
            prompt=prompt,
            version_id=f"v_{prompt.scene_id}_original",
            variant_type="original",
        ))

        # Camera variation: Add handheld feel
        camera_prompt = deepcopy(prompt)
        camera_prompt.english = prompt.english.replace(
            "dolly", "handheld"
        ).replace(
            "tracking shot", "POV handheld"
        )
        if camera_prompt.english != prompt.english:
            versions.append(PromptVersion(
                prompt=camera_prompt,
                version_id=f"v_{prompt.scene_id}_camera",
                variant_type="camera_variation",
                parent_version=versions[0].version_id,
            ))

        # Mood variation: Change lighting
        mood_prompt = deepcopy(prompt)
        mood_prompt.english = prompt.english.replace(
            "warm", "soft golden"
        ).replace(
            "bright", "gentle diffused"
        )
        if mood_prompt.english != prompt.english:
            versions.append(PromptVersion(
                prompt=mood_prompt,
                version_id=f"v_{prompt.scene_id}_mood",
                variant_type="mood_variation",
                parent_version=versions[0].version_id,
            ))

        return versions

    def get_versions(self, scene_id: int) -> list[PromptVersion]:
        """Get all versions for a scene."""
        return self._versions.get(scene_id, [])

    def get_version(self, version_id: str) -> PromptVersion | None:
        """Get specific version by ID."""
        for versions in self._versions.values():
            for v in versions:
                if v.version_id == version_id:
                    return v
        return None

    def compare_versions(
        self,
        version_a: PromptVersion,
        version_b: PromptVersion,
    ) -> dict[str, Any]:
        """
        Compare two versions and return differences.

        Returns:
            Comparison dict with differences highlighted
        """
        prompt_a = version_a.prompt.english
        prompt_b = version_b.prompt.english

        # Simple word-level diff
        words_a = set(prompt_a.lower().split())
        words_b = set(prompt_b.lower().split())

        only_in_a = words_a - words_b
        only_in_b = words_b - words_a
        common = words_a & words_b

        return {
            "version_a": {
                "id": version_a.version_id,
                "type": version_a.variant_type,
                "word_count": len(prompt_a.split()),
            },
            "version_b": {
                "id": version_b.version_id,
                "type": version_b.variant_type,
                "word_count": len(prompt_b.split()),
            },
            "differences": {
                "only_in_a": list(only_in_a)[:20],
                "only_in_b": list(only_in_b)[:20],
                "common_words": len(common),
            },
            "similarity": len(common) / max(len(words_a), len(words_b)) if words_a or words_b else 1.0,
        }

    def save_versions(
        self,
        project_slug: str,
        scene_id: int | None = None,
    ) -> Path:
        """
        Save versions to disk.

        Args:
            project_slug: Project identifier
            scene_id: Optional specific scene, or all if None

        Returns:
            Path to saved file
        """
        versions_dir = self.versions_dir / project_slug / "versions"
        versions_dir.mkdir(parents=True, exist_ok=True)

        if scene_id is not None:
            # Save single scene versions
            versions = self._versions.get(scene_id, [])
            data = [v.to_dict() for v in versions]
            file_path = versions_dir / f"scene_{scene_id}_versions.json"
        else:
            # Save all versions
            data = {}
            for sid, versions in self._versions.items():
                data[str(sid)] = [v.to_dict() for v in versions]
            file_path = versions_dir / "all_versions.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return file_path

    def load_versions(
        self,
        project_slug: str,
        scene_id: int | None = None,
    ) -> dict[int, list[PromptVersion]]:
        """
        Load versions from disk.

        Args:
            project_slug: Project identifier
            scene_id: Optional specific scene, or all if None

        Returns:
            Dict mapping scene_id to list of versions
        """
        versions_dir = self.versions_dir / project_slug / "versions"

        if scene_id is not None:
            file_path = versions_dir / f"scene_{scene_id}_versions.json"
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                versions = [PromptVersion.from_dict(v) for v in data]
                self._versions[scene_id] = versions
                return {scene_id: versions}
        else:
            file_path = versions_dir / "all_versions.json"
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                for sid_str, versions_data in data.items():
                    sid = int(sid_str)
                    self._versions[sid] = [
                        PromptVersion.from_dict(v) for v in versions_data
                    ]
                return self._versions

        return {}

    def format_comparison(
        self,
        version_a: PromptVersion,
        version_b: PromptVersion,
    ) -> str:
        """Format comparison as readable text."""
        comparison = self.compare_versions(version_a, version_b)

        lines = [
            "# 버전 비교",
            "",
            f"## Version A: {version_a.variant_type}",
            f"```",
            version_a.prompt.english,
            "```",
            "",
            f"## Version B: {version_b.variant_type}",
            "```",
            version_b.prompt.english,
            "```",
            "",
            f"## 유사도: {comparison['similarity']:.0%}",
            "",
            f"### A에만 있는 키워드: {', '.join(comparison['differences']['only_in_a'][:10])}",
            f"### B에만 있는 키워드: {', '.join(comparison['differences']['only_in_b'][:10])}",
        ]

        return "\n".join(lines)
