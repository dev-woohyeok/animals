"""Scene Agent - Divide story into individual scenes."""

from typing import Any

from core.models import Story, Scene, CameraSettings
from .base import BaseAgent


class SceneAgent(BaseAgent[list[Scene]]):
    """
    Divides story into 15-second scenes.

    Creates:
    - 6+ individual scenes
    - Camera and lighting specifications
    - Scene-level emotional mapping
    """

    def __init__(self, target_scenes: int = 6):
        super().__init__(
            name="SceneAgent",
            system_prompt_path="scene_system.md",
        )
        self.target_scenes = target_scenes

    def _get_default_system_prompt(self) -> str:
        return """You are a professional storyboard artist and cinematographer.

Your task is to divide a story into individual 15-second scenes for video generation.

For each scene, provide:
1. id: Scene number (1, 2, 3...)
2. title: Korean title (2-4 words)
3. title_en: English title
4. duration: Always 15 seconds
5. description: What happens in this scene (2-3 sentences)
6. action: Main action/movement
7. emotion: Primary emotion
8. camera:
   - movement: dolly in, dolly out, tracking, pan, tilt, static, crane
   - angle: wide, medium, close-up, extreme close-up
   - transition: cut, fade, dissolve (from previous scene)
9. lighting: Lighting description
10. key_elements: Important visual elements (3-5 items)

Guidelines:
- Create at least 6 scenes
- Each scene should be visually distinct
- Build emotional progression
- Consider visual continuity between scenes
- Use camera and lighting to enhance emotion

Output in YAML format:
```yaml
scenes:
  - id: 1
    title: "버려진 강아지"
    title_en: "Abandoned Puppy"
    duration: 15
    description: "..."
    action: "..."
    emotion: "슬픔, 고독"
    camera:
      movement: "slow dolly in"
      angle: "wide to close-up"
      transition: "fade in"
    lighting: "cold blue-grey, overcast"
    key_elements:
      - "wet cardboard box"
      - "rainy street"
      - "puppy's sad eyes"
  - id: 2
    ...
```"""

    def process(self, input_data: Any) -> list[Scene]:
        """
        Divide story into scenes.

        Args:
            input_data: Story object

        Returns:
            List of Scene objects
        """
        if isinstance(input_data, dict):
            story = Story(**input_data)
        else:
            story = input_data

        # Build prompt
        user_message = self._build_prompt(story)

        # Call Claude
        response = self._call_claude(user_message)

        # Parse response
        return self._parse_scenes_response(response, story)

    def _build_prompt(self, story: Story) -> str:
        """Build prompt for scene division."""
        arc_description = "\n".join([
            f"- {phase.phase}: {phase.description} ({phase.emotion})"
            for phase in story.arc
        ])

        return f"""Story to divide into scenes:

Title: {story.title}
Synopsis: {story.synopsis}

Story Arc:
{arc_description}

Target: {self.target_scenes}+ scenes, 15 seconds each
Total Duration: {story.total_duration} seconds

Create scenes that capture the emotional journey while being visually engaging."""

    def _parse_scenes_response(self, response: str, story: Story) -> list[Scene]:
        """Parse Claude's response into Scene objects."""
        try:
            data = self._parse_yaml_response(response)
            scenes = []

            for scene_data in data.get("scenes", []):
                camera_data = scene_data.get("camera", {})
                camera = CameraSettings(
                    movement=camera_data.get("movement", "static"),
                    angle=camera_data.get("angle", "medium"),
                    transition=camera_data.get("transition"),
                )

                scenes.append(Scene(
                    id=scene_data.get("id", len(scenes) + 1),
                    title=scene_data.get("title", f"장면 {len(scenes) + 1}"),
                    title_en=scene_data.get("title_en"),
                    duration=scene_data.get("duration", 15),
                    description=scene_data.get("description", ""),
                    action=scene_data.get("action", ""),
                    emotion=scene_data.get("emotion", ""),
                    camera=camera,
                    lighting=scene_data.get("lighting", "natural"),
                    key_elements=scene_data.get("key_elements", []),
                ))

            return scenes if scenes else self._create_default_scenes(story)

        except Exception as e:
            self.log(f"Parse error: {e}, creating default scenes")
            return self._create_default_scenes(story)

    def _create_default_scenes(self, story: Story) -> list[Scene]:
        """Create default scenes from story phases."""
        scenes = []
        scene_id = 1

        for phase in story.arc:
            scenes.append(Scene(
                id=scene_id,
                title=phase.phase,
                duration=15,
                description=phase.description,
                action=phase.beats[0] if phase.beats else phase.description,
                emotion=phase.emotion,
                camera=CameraSettings(
                    movement="static",
                    angle="medium",
                    transition="cut" if scene_id > 1 else "fade in",
                ),
                lighting="natural",
                key_elements=[],
            ))
            scene_id += 1

        # Ensure minimum scenes
        while len(scenes) < self.target_scenes:
            scenes.append(Scene(
                id=scene_id,
                title=f"장면 {scene_id}",
                duration=15,
                description="추가 장면",
                action="동작",
                emotion="감동",
                camera=CameraSettings(
                    movement="static",
                    angle="medium",
                    transition="cut",
                ),
                lighting="natural",
                key_elements=[],
            ))
            scene_id += 1

        return scenes

    def regenerate_scene(
        self,
        scenes: list[Scene],
        scene_id: int,
        feedback: str,
    ) -> list[Scene]:
        """
        Regenerate a specific scene based on feedback.

        Args:
            scenes: Current scenes list
            scene_id: ID of scene to regenerate
            feedback: User feedback

        Returns:
            Updated scenes list
        """
        current_scene = next((s for s in scenes if s.id == scene_id), None)
        if not current_scene:
            return scenes

        prompt = f"""Current scene:
{current_scene.model_dump_json(indent=2)}

Regenerate this scene based on feedback:
{feedback}

Keep the same id and duration. Output single scene in YAML format."""

        response = self._call_claude(prompt)

        try:
            data = self._parse_yaml_response(response)
            scene_data = data if "id" in data else data.get("scene", data)

            camera_data = scene_data.get("camera", {})
            new_scene = Scene(
                id=scene_id,
                title=scene_data.get("title", current_scene.title),
                title_en=scene_data.get("title_en"),
                duration=15,
                description=scene_data.get("description", ""),
                action=scene_data.get("action", ""),
                emotion=scene_data.get("emotion", ""),
                camera=CameraSettings(
                    movement=camera_data.get("movement", "static"),
                    angle=camera_data.get("angle", "medium"),
                    transition=camera_data.get("transition"),
                ),
                lighting=scene_data.get("lighting", "natural"),
                key_elements=scene_data.get("key_elements", []),
            )

            # Replace scene in list
            return [new_scene if s.id == scene_id else s for s in scenes]

        except Exception as e:
            self.log(f"Regeneration error: {e}")
            return scenes
