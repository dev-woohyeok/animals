"""Style Manager - Manage visual style presets and customization."""

from pathlib import Path
from typing import Any
from copy import deepcopy

import yaml

from utils import get_logger, ensure_dir


class StylePreset:
    """Represents a visual style preset."""

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        visual_style: dict[str, Any],
        camera_defaults: dict[str, str],
        lighting_defaults: dict[str, str],
        quality_markers: list[str],
        metadata: dict[str, Any] | None = None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.visual_style = visual_style
        self.camera_defaults = camera_defaults
        self.lighting_defaults = lighting_defaults
        self.quality_markers = quality_markers
        self.metadata = metadata or {}

    def get_quality_suffix(self) -> str:
        """Get quality markers as suffix text."""
        return ". ".join(self.quality_markers) + "."

    def get_camera_for_emotion(self, emotion: str) -> str:
        """Get suggested camera for emotion."""
        emotion_lower = emotion.lower()

        # Check emotion mappings
        emotion_cameras = self.camera_defaults.get("by_emotion", {})
        for key, value in emotion_cameras.items():
            if key in emotion_lower:
                return value

        return self.camera_defaults.get("default", "medium shot")

    def get_lighting_for_mood(self, mood: str) -> str:
        """Get suggested lighting for mood."""
        mood_lower = mood.lower()

        mood_lighting = self.lighting_defaults.get("by_mood", {})
        for key, value in mood_lighting.items():
            if key in mood_lower:
                return value

        return self.lighting_defaults.get("default", "natural lighting")

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "visual_style": self.visual_style,
            "camera_defaults": self.camera_defaults,
            "lighting_defaults": self.lighting_defaults,
            "quality_markers": self.quality_markers,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "StylePreset":
        """Create from dictionary."""
        return cls(
            id=data.get("id", "unknown"),
            name=data.get("name", "Unknown Style"),
            description=data.get("description", ""),
            visual_style=data.get("visual_style", {}),
            camera_defaults=data.get("camera_defaults", {}),
            lighting_defaults=data.get("lighting_defaults", {}),
            quality_markers=data.get("quality_markers", []),
            metadata=data.get("metadata"),
        )


class StyleManager:
    """
    Manages visual style presets and customization.

    Features:
    - Load style presets from YAML
    - Create custom styles
    - Apply styles to prompts
    - Merge and customize styles
    """

    def __init__(self, styles_dir: str | Path | None = None):
        """
        Initialize style manager.

        Args:
            styles_dir: Directory containing style preset files
        """
        self.logger = get_logger("StyleManager")

        if styles_dir is None:
            styles_dir = Path(__file__).parent.parent / "config" / "styles"

        self.styles_dir = Path(styles_dir)
        ensure_dir(self.styles_dir)

        # Cache
        self._presets_cache: dict[str, StylePreset] = {}

        # Load built-in presets
        self._load_built_in_presets()

    def _load_built_in_presets(self) -> None:
        """Load built-in style presets."""
        for file_path in self.styles_dir.glob("*.yaml"):
            try:
                preset = self._load_preset_file(file_path)
                if preset:
                    self._presets_cache[preset.id] = preset
            except Exception as e:
                self.logger.warning(f"Error loading {file_path}: {e}")

    def _load_preset_file(self, file_path: Path) -> StylePreset | None:
        """Load a single preset file."""
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if not data:
            return None

        # Handle flat format (convert to structured)
        if "visual_style" not in data:
            data = self._convert_flat_format(data, file_path.stem)

        return StylePreset.from_dict(data)

    def _convert_flat_format(
        self,
        data: dict[str, Any],
        default_id: str,
    ) -> dict[str, Any]:
        """Convert flat YAML format to structured format."""
        return {
            "id": data.get("id", default_id),
            "name": data.get("name", default_id.replace("_", " ").title()),
            "description": data.get("description", ""),
            "visual_style": {
                "aesthetic": data.get("aesthetic", ""),
                "color_palette": data.get("color_palette", []),
                "texture": data.get("texture", ""),
            },
            "camera_defaults": data.get("camera", {
                "default": "medium shot",
                "by_emotion": {},
            }),
            "lighting_defaults": data.get("lighting", {
                "default": "natural lighting",
                "by_mood": {},
            }),
            "quality_markers": data.get("quality_markers", [
                "Photorealistic 4K cinematic quality"
            ]),
            "metadata": data.get("metadata", {}),
        }

    def get_preset(self, preset_id: str) -> StylePreset | None:
        """
        Get style preset by ID.

        Args:
            preset_id: Preset identifier

        Returns:
            StylePreset or None
        """
        return self._presets_cache.get(preset_id)

    def list_presets(self) -> list[dict[str, str]]:
        """
        List all available presets.

        Returns:
            List of preset summaries
        """
        return [
            {
                "id": preset.id,
                "name": preset.name,
                "description": preset.description,
            }
            for preset in self._presets_cache.values()
        ]

    def create_preset(
        self,
        preset_id: str,
        name: str,
        description: str,
        visual_style: dict[str, Any],
        camera_defaults: dict[str, str] | None = None,
        lighting_defaults: dict[str, str] | None = None,
        quality_markers: list[str] | None = None,
    ) -> StylePreset:
        """
        Create a new style preset.

        Args:
            preset_id: Unique identifier
            name: Display name
            description: Style description
            visual_style: Visual style settings
            camera_defaults: Camera defaults
            lighting_defaults: Lighting defaults
            quality_markers: Quality marker strings

        Returns:
            Created StylePreset
        """
        preset = StylePreset(
            id=preset_id,
            name=name,
            description=description,
            visual_style=visual_style,
            camera_defaults=camera_defaults or {"default": "medium shot"},
            lighting_defaults=lighting_defaults or {"default": "natural lighting"},
            quality_markers=quality_markers or ["Photorealistic 4K cinematic quality"],
        )

        # Save to file
        file_path = self.styles_dir / f"{preset_id}.yaml"
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(preset.to_dict(), f, allow_unicode=True, default_flow_style=False)

        self._presets_cache[preset_id] = preset
        self.logger.info(f"Created preset: {preset_id}")

        return preset

    def create_custom_preset(
        self,
        base_preset_id: str,
        custom_id: str,
        overrides: dict[str, Any],
    ) -> StylePreset | None:
        """
        Create a custom preset based on existing one.

        Args:
            base_preset_id: Base preset to customize
            custom_id: New preset ID
            overrides: Settings to override

        Returns:
            New StylePreset or None if base not found
        """
        base = self.get_preset(base_preset_id)
        if not base:
            return None

        # Deep copy and merge
        data = deepcopy(base.to_dict())
        data["id"] = custom_id
        data["name"] = overrides.pop("name", f"Custom {base.name}")
        data["description"] = overrides.pop("description", f"Based on {base.name}")

        # Apply overrides
        for key, value in overrides.items():
            if key in data:
                if isinstance(data[key], dict) and isinstance(value, dict):
                    data[key].update(value)
                else:
                    data[key] = value

        return self.create_preset(**data)

    def apply_style_to_prompt(
        self,
        prompt_text: str,
        preset_id: str,
        emotion: str | None = None,
        mood: str | None = None,
    ) -> str:
        """
        Apply style preset to a prompt.

        Args:
            prompt_text: Original prompt text
            preset_id: Style preset to apply
            emotion: Optional emotion for camera suggestion
            mood: Optional mood for lighting suggestion

        Returns:
            Styled prompt text
        """
        preset = self.get_preset(preset_id)
        if not preset:
            return prompt_text

        # Build style additions
        additions = []

        # Add camera if specified
        if emotion:
            camera = preset.get_camera_for_emotion(emotion)
            if camera and camera.lower() not in prompt_text.lower():
                additions.append(camera)

        # Add lighting if specified
        if mood:
            lighting = preset.get_lighting_for_mood(mood)
            if lighting and lighting.lower() not in prompt_text.lower():
                additions.append(lighting)

        # Add quality markers
        quality_suffix = preset.get_quality_suffix()

        # Combine
        styled = prompt_text.rstrip(".")
        if additions:
            styled += ". " + ". ".join(additions)
        styled += ". " + quality_suffix

        return styled

    def get_default_preset(self) -> StylePreset:
        """Get the default style preset."""
        default = self.get_preset("cinematic_realistic")

        if default:
            return default

        # Create a basic default if none exists
        return StylePreset(
            id="default",
            name="Default",
            description="Basic default style",
            visual_style={"aesthetic": "photorealistic"},
            camera_defaults={"default": "medium shot"},
            lighting_defaults={"default": "natural lighting"},
            quality_markers=["Photorealistic 4K cinematic quality"],
        )

    # ============================================================
    # Preset Templates for Common Styles
    # ============================================================

    def get_home_video_preset(self) -> StylePreset:
        """Get or create home video style preset."""
        existing = self.get_preset("home_video")
        if existing:
            return existing

        return self.create_preset(
            preset_id="home_video",
            name="Home Video",
            description="Authentic amateur home video aesthetic",
            visual_style={
                "aesthetic": "amateur footage",
                "texture": "slightly grainy",
                "imperfections": True,
            },
            camera_defaults={
                "default": "handheld POV",
                "by_emotion": {
                    "excitement": "shaky handheld",
                    "peaceful": "steady handheld",
                    "curious": "moving closer handheld",
                },
            },
            lighting_defaults={
                "default": "natural indoor lighting",
                "by_mood": {
                    "warm": "warm lamp light with slight overexposure",
                    "bright": "daylight through window, slight overexposure",
                    "intimate": "soft evening indoor light",
                },
            },
            quality_markers=[
                "First person POV handheld home video",
                "Authentic amateur footage aesthetic",
                "Natural imperfections",
                "Slightly grainy low resolution feel",
            ],
        )

    def get_documentary_preset(self) -> StylePreset:
        """Get or create documentary style preset."""
        existing = self.get_preset("documentary")
        if existing:
            return existing

        return self.create_preset(
            preset_id="documentary",
            name="Documentary",
            description="Professional documentary style",
            visual_style={
                "aesthetic": "documentary",
                "color_grading": "natural",
            },
            camera_defaults={
                "default": "observational medium shot",
                "by_emotion": {
                    "intimate": "close-up with shallow depth",
                    "expansive": "wide establishing shot",
                },
            },
            lighting_defaults={
                "default": "natural available light",
            },
            quality_markers=[
                "Documentary style footage",
                "Natural lighting",
                "Real-world authenticity",
                "Professional 4K quality",
            ],
        )
