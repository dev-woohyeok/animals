"""Prompt Agent - Generate Sora2 optimized prompts."""

from pathlib import Path
from typing import Any

import yaml

from core.models import Scene, Character, Prompt, PromptStructure
from .base import BaseAgent


class PromptAgent(BaseAgent[list[Prompt]]):
    """
    Generates Sora2-optimized prompts for each scene.

    Features:
    - Character consistency across all prompts
    - Style preset application
    - Best practices integration
    """

    def __init__(self, style_id: str = "cinematic_realistic"):
        super().__init__(
            name="PromptAgent",
            system_prompt_path="sora2_system.md",
        )
        self.style_id = style_id
        self.style_config = self._load_style_config(style_id)
        self.best_practices = self._load_best_practices()

    def _get_default_system_prompt(self) -> str:
        return """You are an expert at writing prompts for Sora2 video generation.

Your task is to create detailed, consistent prompts that will generate coherent 15-second video clips.

PROMPT STRUCTURE (follow this order):
1. Subject/Character Description - Detailed physical appearance (MUST be consistent across all prompts)
2. Setting/Location - Where the scene takes place
3. Action - What is happening (keep it achievable in 15 seconds)
4. Camera Movement - Specific camera work
5. Lighting - Light quality, direction, mood
6. Atmosphere/Mood - Emotional tone

IMPORTANT RULES:
- Be SPECIFIC: "fluffy cream-colored fur" not "golden fur"
- Include camera movement: "slow dolly shot moving toward"
- Specify lighting: "warm golden hour lighting with soft shadows"
- Add atmosphere: "melancholic, lonely atmosphere"
- Keep character description IDENTICAL across all prompts for consistency
- Each prompt should be 100-200 words

Output in YAML format:
```yaml
prompts:
  - scene_id: 1
    english: "Full prompt text..."
    structure:
      character_desc: "..."
      setting: "..."
      action: "..."
      camera: "..."
      lighting: "..."
      atmosphere: "..."
```"""

    def _load_style_config(self, style_id: str) -> dict:
        """Load style configuration."""
        project_root = Path(__file__).parent.parent
        style_path = project_root / "config" / "styles" / f"{style_id}.yaml"

        if style_path.exists():
            with open(style_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        return {}

    def _load_best_practices(self) -> dict:
        """Load Sora2 best practices."""
        project_root = Path(__file__).parent.parent
        bp_path = project_root / "library" / "best_practices" / "sora2_tips.yaml"

        if bp_path.exists():
            with open(bp_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        return {}

    def process(
        self,
        input_data: Any,
        character: Character | None = None,
    ) -> list[Prompt]:
        """
        Generate prompts for all scenes.

        Args:
            input_data: List of Scene objects
            character: Character for consistency (optional)

        Returns:
            List of Prompt objects
        """
        scenes = input_data if isinstance(input_data, list) else [input_data]

        # Build character description for consistency
        char_desc = self._build_character_description(character)

        # Generate prompts
        user_message = self._build_prompt(scenes, char_desc)
        response = self._call_claude(user_message)

        return self._parse_prompts_response(response, scenes, char_desc)

    def _build_character_description(self, character: Character | None) -> str:
        """Build consistent character description."""
        if character:
            return character.sora2_prompt_fragment

        # Default template
        return "[CHARACTER_DESCRIPTION]"

    def _build_prompt(self, scenes: list[Scene], char_desc: str) -> str:
        """Build prompt for generation."""
        # Get style info
        style_info = ""
        if self.style_config:
            style_info = f"""
Style: {self.style_config.get('name', 'Cinematic')}
Base Style: {self.style_config.get('base_prompt', {}).get('style', 'photorealistic')}
Lighting Default: {self.style_config.get('lighting_defaults', {}).get('primary', 'natural')}
"""

        # Get best practice tips
        tips = ""
        if self.best_practices:
            rules = self.best_practices.get("general_rules", [])[:3]
            tips = "\n".join([f"- {r.get('rule', '')}" for r in rules])

        scenes_desc = "\n\n".join([
            f"""Scene {s.id}: {s.title}
- Description: {s.description}
- Action: {s.action}
- Emotion: {s.emotion}
- Camera: {s.camera.movement}, {s.camera.angle}
- Lighting: {s.lighting}"""
            for s in scenes
        ])

        return f"""Generate Sora2 prompts for these scenes.

CHARACTER (use EXACTLY in every prompt):
{char_desc}

{style_info}

Key Tips:
{tips}

SCENES:
{scenes_desc}

Generate a detailed prompt for each scene. Maintain character consistency."""

    def _parse_prompts_response(
        self,
        response: str,
        scenes: list[Scene],
        char_desc: str,
    ) -> list[Prompt]:
        """Parse response into Prompt objects."""
        try:
            data = self._parse_yaml_response(response)
            prompts = []

            for prompt_data in data.get("prompts", []):
                structure_data = prompt_data.get("structure", {})

                prompts.append(Prompt(
                    scene_id=prompt_data.get("scene_id", len(prompts) + 1),
                    english=prompt_data.get("english", ""),
                    structure=PromptStructure(
                        character_desc=structure_data.get("character_desc", char_desc),
                        setting=structure_data.get("setting", ""),
                        action=structure_data.get("action", ""),
                        camera=structure_data.get("camera", ""),
                        lighting=structure_data.get("lighting", ""),
                        atmosphere=structure_data.get("atmosphere", ""),
                    ),
                ))

            return prompts if prompts else self._create_default_prompts(scenes, char_desc)

        except Exception as e:
            self.log(f"Parse error: {e}")
            return self._create_default_prompts(scenes, char_desc)

    def _create_default_prompts(
        self,
        scenes: list[Scene],
        char_desc: str,
    ) -> list[Prompt]:
        """Create default prompts from scenes."""
        prompts = []

        for scene in scenes:
            english = f"{char_desc}. {scene.description}. {scene.action}. {scene.camera.movement} shot, {scene.camera.angle}. {scene.lighting}. {scene.emotion} atmosphere."

            prompts.append(Prompt(
                scene_id=scene.id,
                english=english,
                structure=PromptStructure(
                    character_desc=char_desc,
                    setting=scene.description,
                    action=scene.action,
                    camera=f"{scene.camera.movement}, {scene.camera.angle}",
                    lighting=scene.lighting,
                    atmosphere=scene.emotion,
                ),
            ))

        return prompts

    def regenerate_prompt(
        self,
        prompt: Prompt,
        feedback: str,
        char_desc: str,
    ) -> Prompt:
        """
        Regenerate a single prompt based on feedback.

        Args:
            prompt: Current prompt
            feedback: User feedback
            char_desc: Character description (for consistency)

        Returns:
            Updated prompt
        """
        user_message = f"""Current prompt:
{prompt.english}

Feedback: {feedback}

Character description (MUST keep exactly):
{char_desc}

Regenerate the prompt addressing the feedback. Keep character description identical.
Output in YAML format with scene_id, english, and structure."""

        response = self._call_claude(user_message)

        try:
            data = self._parse_yaml_response(response)
            structure_data = data.get("structure", {})

            return Prompt(
                scene_id=prompt.scene_id,
                english=data.get("english", prompt.english),
                structure=PromptStructure(
                    character_desc=char_desc,
                    setting=structure_data.get("setting", ""),
                    action=structure_data.get("action", ""),
                    camera=structure_data.get("camera", ""),
                    lighting=structure_data.get("lighting", ""),
                    atmosphere=structure_data.get("atmosphere", ""),
                ),
            )

        except Exception as e:
            self.log(f"Regeneration error: {e}")
            return prompt
