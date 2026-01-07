"""Regeneration Agent - Handle partial regeneration of content."""

from typing import Any
from copy import deepcopy

from core.models import (
    Story,
    StoryPhase,
    Scene,
    CameraSettings,
    Prompt,
    PromptStructure,
    TitleSet,
    Character,
)
from .base import BaseAgent


class RegenAgent(BaseAgent[Any]):
    """
    Handles partial regeneration of stories, scenes, and prompts.

    Features:
    - Regenerate specific story phases
    - Regenerate individual scenes
    - Regenerate prompts with feedback
    - Modify specific elements (camera, lighting, mood)
    """

    def __init__(self):
        super().__init__(
            name="RegenAgent",
            system_prompt_path="regen_system.md",
        )

    def _get_default_system_prompt(self) -> str:
        return """You are an expert at modifying and regenerating video content.

Given original content and specific feedback, regenerate only the requested parts while maintaining consistency with unchanged elements.

For story modifications:
- Keep overall narrative arc intact
- Modify only specified phases
- Ensure emotional continuity

For prompt modifications:
- Maintain character consistency
- Apply feedback precisely
- Keep Sora2 best practices

Output format matches the input type (Story JSON, Prompt JSON, etc.)"""

    def process(self, input_data: Any) -> Any:
        """
        Process regeneration request.

        Args:
            input_data: Dict with 'content', 'feedback', and 'target'

        Returns:
            Regenerated content
        """
        if not isinstance(input_data, dict):
            raise ValueError("Input must be dict with 'content', 'feedback', 'target'")

        content = input_data.get("content")
        feedback = input_data.get("feedback", "")
        target = input_data.get("target", "all")

        if isinstance(content, Story):
            return self.regenerate_story_phase(content, target, feedback)
        elif isinstance(content, Scene):
            return self.regenerate_scene(content, feedback)
        elif isinstance(content, Prompt):
            return self.regenerate_prompt(content, feedback)

        return content

    # ============================================================
    # Story Regeneration
    # ============================================================

    def regenerate_story_phase(
        self,
        story: Story,
        phase_name: str,
        feedback: str,
    ) -> Story:
        """
        Regenerate a specific story phase.

        Args:
            story: Original story
            phase_name: Phase to regenerate (도입, 전개, 위기, 해결, 결말)
            feedback: User feedback for regeneration

        Returns:
            Story with regenerated phase
        """
        # Find the phase to regenerate
        phase_idx = None
        for i, phase in enumerate(story.arc):
            if phase.phase == phase_name:
                phase_idx = i
                break

        if phase_idx is None:
            self.log(f"Phase '{phase_name}' not found")
            return story

        # Build context
        context = self._build_story_context(story, phase_idx)

        user_message = f"""Regenerate the "{phase_name}" phase of this story based on feedback.

Story context:
{context}

Current "{phase_name}" phase:
{story.arc[phase_idx].description}
Emotion: {story.arc[phase_idx].emotion}

Feedback: {feedback}

Regenerate only this phase. Output JSON:
{{
  "phase": "{phase_name}",
  "description": "New description...",
  "beats": ["beat1", "beat2"],
  "emotion": "emotion keywords"
}}"""

        try:
            response = self._call_claude(user_message)
            data = self._parse_json_response(response)

            # Create new story with modified phase
            new_story = deepcopy(story)
            new_story.arc[phase_idx] = StoryPhase(
                phase=data.get("phase", phase_name),
                description=data.get("description", story.arc[phase_idx].description),
                beats=data.get("beats", story.arc[phase_idx].beats),
                emotion=data.get("emotion", story.arc[phase_idx].emotion),
            )

            return new_story

        except Exception as e:
            self.log(f"Story phase regeneration failed: {e}")
            return story

    def _build_story_context(self, story: Story, current_phase_idx: int) -> str:
        """Build context string for story regeneration."""
        lines = [
            f"Title: {story.title}",
            f"Synopsis: {story.synopsis}",
            "",
            "Story arc:",
        ]

        for i, phase in enumerate(story.arc):
            marker = ">>> " if i == current_phase_idx else "    "
            lines.append(f"{marker}{phase.phase}: {phase.description[:50]}...")

        return "\n".join(lines)

    # ============================================================
    # Scene Regeneration
    # ============================================================

    def regenerate_scene(
        self,
        scene: Scene,
        feedback: str,
        modify_elements: list[str] | None = None,
    ) -> Scene:
        """
        Regenerate a scene based on feedback.

        Args:
            scene: Original scene
            feedback: User feedback
            modify_elements: Specific elements to modify (camera, lighting, action, etc.)

        Returns:
            Regenerated Scene
        """
        if modify_elements is None:
            modify_elements = ["description", "action", "camera"]

        user_message = f"""Modify this scene based on feedback.

Current scene:
- Title: {scene.title}
- Description: {scene.description}
- Action: {scene.action}
- Camera: {scene.camera.movement}, {scene.camera.angle}
- Lighting: {scene.lighting}
- Emotion: {scene.emotion}

Feedback: {feedback}

Elements to modify: {', '.join(modify_elements)}

Output JSON:
{{
  "title": "...",
  "description": "...",
  "action": "...",
  "emotion": "...",
  "camera": {{"movement": "...", "angle": "...", "transition": "..."}},
  "lighting": "..."
}}"""

        try:
            response = self._call_claude(user_message)
            data = self._parse_json_response(response)

            # Create modified scene
            new_scene = deepcopy(scene)

            if "description" in modify_elements and "description" in data:
                new_scene.description = data["description"]

            if "action" in modify_elements and "action" in data:
                new_scene.action = data["action"]

            if "camera" in modify_elements and "camera" in data:
                cam_data = data["camera"]
                new_scene.camera = CameraSettings(
                    movement=cam_data.get("movement", scene.camera.movement),
                    angle=cam_data.get("angle", scene.camera.angle),
                    transition=cam_data.get("transition", scene.camera.transition),
                )

            if "lighting" in modify_elements and "lighting" in data:
                new_scene.lighting = data["lighting"]

            if "emotion" in modify_elements and "emotion" in data:
                new_scene.emotion = data["emotion"]

            return new_scene

        except Exception as e:
            self.log(f"Scene regeneration failed: {e}")
            return scene

    def modify_scene_element(
        self,
        scene: Scene,
        element: str,
        new_value: str,
    ) -> Scene:
        """
        Directly modify a single scene element.

        Args:
            scene: Original scene
            element: Element to modify (camera_movement, camera_angle, lighting, emotion)
            new_value: New value for the element

        Returns:
            Modified Scene
        """
        new_scene = deepcopy(scene)

        if element == "camera_movement":
            new_scene.camera.movement = new_value
        elif element == "camera_angle":
            new_scene.camera.angle = new_value
        elif element == "lighting":
            new_scene.lighting = new_value
        elif element == "emotion":
            new_scene.emotion = new_value
        elif element == "duration":
            new_scene.duration = int(new_value)
        elif element == "action":
            new_scene.action = new_value

        return new_scene

    # ============================================================
    # Prompt Regeneration
    # ============================================================

    def regenerate_prompt(
        self,
        prompt: Prompt,
        feedback: str,
        character: Character | None = None,
    ) -> Prompt:
        """
        Regenerate a prompt based on feedback.

        Args:
            prompt: Original prompt
            feedback: User feedback
            character: Optional character for consistency

        Returns:
            Regenerated Prompt
        """
        char_desc = ""
        if character:
            char_desc = f"\nCharacter reference: {character.sora2_prompt_fragment}"

        user_message = f"""Modify this Sora2 prompt based on feedback.

Current prompt:
{prompt.english}

Structure:
- Character: {prompt.structure.character_desc}
- Setting: {prompt.structure.setting}
- Action: {prompt.structure.action}
- Camera: {prompt.structure.camera}
- Lighting: {prompt.structure.lighting}
- Atmosphere: {prompt.structure.atmosphere}
{char_desc}

Feedback: {feedback}

Regenerate the prompt. Output JSON:
{{
  "english": "Complete new prompt text...",
  "structure": {{
    "character_desc": "...",
    "setting": "...",
    "action": "...",
    "camera": "...",
    "lighting": "...",
    "atmosphere": "..."
  }}
}}"""

        try:
            response = self._call_claude(user_message)
            data = self._parse_json_response(response)

            struct_data = data.get("structure", {})

            return Prompt(
                scene_id=prompt.scene_id,
                english=data.get("english", prompt.english),
                korean=None,  # Needs retranslation
                structure=PromptStructure(
                    character_desc=struct_data.get("character_desc", prompt.structure.character_desc),
                    setting=struct_data.get("setting", prompt.structure.setting),
                    action=struct_data.get("action", prompt.structure.action),
                    camera=struct_data.get("camera", prompt.structure.camera),
                    lighting=struct_data.get("lighting", prompt.structure.lighting),
                    atmosphere=struct_data.get("atmosphere", prompt.structure.atmosphere),
                ),
                quality_score=None,
            )

        except Exception as e:
            self.log(f"Prompt regeneration failed: {e}")
            return prompt

    def modify_prompt_element(
        self,
        prompt: Prompt,
        element: str,
        new_value: str,
    ) -> Prompt:
        """
        Directly modify a single prompt element.

        Args:
            prompt: Original prompt
            element: Element to modify (camera, lighting, atmosphere, etc.)
            new_value: New value

        Returns:
            Modified Prompt with updated text
        """
        new_prompt = deepcopy(prompt)
        new_structure = deepcopy(prompt.structure)

        # Update structure
        if element == "camera":
            new_structure.camera = new_value
        elif element == "lighting":
            new_structure.lighting = new_value
        elif element == "atmosphere":
            new_structure.atmosphere = new_value
        elif element == "setting":
            new_structure.setting = new_value
        elif element == "action":
            new_structure.action = new_value

        new_prompt.structure = new_structure

        # Rebuild prompt text from structure
        new_prompt.english = self._rebuild_prompt_text(new_structure, prompt.structure.character_desc)
        new_prompt.korean = None  # Needs retranslation

        return new_prompt

    def _rebuild_prompt_text(
        self,
        structure: PromptStructure,
        character_desc: str,
    ) -> str:
        """Rebuild prompt text from structure."""
        parts = [
            character_desc,
            structure.setting,
            structure.action,
            structure.camera,
            structure.lighting,
            f"{structure.atmosphere} atmosphere.",
            "Photorealistic 4K cinematic quality.",
        ]
        return " ".join(parts)

    # ============================================================
    # Batch Operations
    # ============================================================

    def regenerate_all_prompts_with_style(
        self,
        prompts: list[Prompt],
        style_change: str,
    ) -> list[Prompt]:
        """
        Apply a style change to all prompts.

        Args:
            prompts: List of prompts
            style_change: Style modification description

        Returns:
            List of modified prompts
        """
        return [
            self.regenerate_prompt(p, f"Apply style change: {style_change}")
            for p in prompts
        ]

    def apply_camera_style(
        self,
        prompts: list[Prompt],
        camera_style: str,
    ) -> list[Prompt]:
        """
        Apply a camera style to all prompts.

        Args:
            prompts: List of prompts
            camera_style: Camera style (e.g., "handheld POV", "cinematic dolly")

        Returns:
            List of modified prompts
        """
        return [
            self.modify_prompt_element(p, "camera", camera_style)
            for p in prompts
        ]
