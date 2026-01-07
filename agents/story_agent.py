"""Story Agent - Generate and expand story structure."""

from typing import Any

from core.models import InputData, Story, StoryPhase, EmotionPoint
from .base import BaseAgent


class StoryAgent(BaseAgent[Story]):
    """
    Generates complete story structure from input.

    Creates:
    - Story arc with phases (도입, 전개, 위기, 해결, 결말)
    - Emotional journey mapping
    - Character development notes
    """

    def __init__(self):
        super().__init__(
            name="StoryAgent",
            system_prompt_path="story_system.md",
        )

    def _get_default_system_prompt(self) -> str:
        return """You are a professional screenwriter specializing in emotional animal stories for short-form video content (90+ seconds, 6+ scenes).

Given an animal and situation, create a compelling story arc with:

1. STRUCTURE (5 phases):
- 도입 (Introduction): Establish the animal's situation, build empathy
- 전개 (Development): Introduce key characters, build connection
- 위기 (Crisis): Moment of tension, danger, or decision
- 해결 (Resolution): The turning point, rescue or change
- 결말 (Ending): Emotional payoff, new beginning

2. EMOTIONAL JOURNEY:
- Start with empathy-building (loneliness, vulnerability)
- Build through hope and setbacks
- End with emotional catharsis (joy, warmth, healing)

3. VISUAL STORYTELLING:
- Think in 15-second scenes
- Each phase should have clear visual potential
- Consider weather, lighting, and setting changes for emotional impact

Output in YAML format:
```yaml
title: "..."
synopsis: "1-2 sentence summary"
arc:
  - phase: "도입"
    description: "..."
    beats:
      - "beat 1"
      - "beat 2"
    emotion: "슬픔, 고독"
  - phase: "전개"
    ...
character_development: "..."
emotional_journey:
  - position: 0.0
    emotion: "슬픔"
    intensity: 80
  - position: 0.5
    emotion: "희망"
    intensity: 50
  ...
total_duration: 90
```

Make the story emotionally engaging while keeping it suitable for short-form video."""

    def process(self, input_data: Any) -> Story:
        """
        Generate story from input data.

        Args:
            input_data: InputData object or dict

        Returns:
            Complete Story object
        """
        if isinstance(input_data, dict):
            input_data = InputData(**input_data)

        # Build prompt
        user_message = self._build_prompt(input_data)

        # Call Claude
        response = self._call_claude(user_message)

        # Parse response
        return self._parse_story_response(response, input_data)

    def _build_prompt(self, input_data: InputData) -> str:
        """Build user prompt for story generation."""
        prompt_parts = [
            f"동물: {input_data.animal}",
            f"상황: {input_data.situation}",
            f"감정 톤: {', '.join(input_data.emotions)}",
        ]

        if input_data.ending:
            prompt_parts.append(f"결말: {input_data.ending}")

        return "\n".join(prompt_parts)

    def _parse_story_response(self, response: str, input_data: InputData) -> Story:
        """Parse Claude's response into Story object."""
        try:
            data = self._parse_yaml_response(response)

            # Parse arc
            arc = []
            for phase_data in data.get("arc", []):
                arc.append(StoryPhase(
                    phase=phase_data.get("phase", ""),
                    description=phase_data.get("description", ""),
                    beats=phase_data.get("beats", []),
                    emotion=phase_data.get("emotion", ""),
                ))

            # Parse emotional journey
            emotional_journey = []
            for point_data in data.get("emotional_journey", []):
                emotional_journey.append(EmotionPoint(
                    position=float(point_data.get("position", 0)),
                    emotion=point_data.get("emotion", ""),
                    intensity=int(point_data.get("intensity", 50)),
                ))

            return Story(
                title=data.get("title", f"{input_data.animal}의 이야기"),
                synopsis=data.get("synopsis", input_data.situation),
                arc=arc,
                character_development=data.get("character_development"),
                emotional_journey=emotional_journey,
                total_duration=data.get("total_duration", 90),
            )

        except Exception as e:
            self.log(f"Parse error: {e}, creating default story")
            return self._create_default_story(input_data)

    def _create_default_story(self, input_data: InputData) -> Story:
        """Create a default story structure."""
        return Story(
            title=f"{input_data.animal}의 이야기",
            synopsis=input_data.situation,
            arc=[
                StoryPhase(
                    phase="도입",
                    description="동물의 현재 상황 소개",
                    beats=["동물 등장", "상황 설명"],
                    emotion="고독, 슬픔",
                ),
                StoryPhase(
                    phase="전개",
                    description="새로운 만남",
                    beats=["인간 캐릭터 등장", "첫 교류"],
                    emotion="호기심, 희망",
                ),
                StoryPhase(
                    phase="위기",
                    description="결정의 순간",
                    beats=["갈등", "선택"],
                    emotion="긴장, 불안",
                ),
                StoryPhase(
                    phase="해결",
                    description="전환점",
                    beats=["변화", "구원"],
                    emotion="안도, 따뜻함",
                ),
                StoryPhase(
                    phase="결말",
                    description="새로운 시작",
                    beats=["행복한 결말"],
                    emotion="기쁨, 감동",
                ),
            ],
            emotional_journey=[
                EmotionPoint(position=0.0, emotion="슬픔", intensity=70),
                EmotionPoint(position=0.3, emotion="희망", intensity=40),
                EmotionPoint(position=0.5, emotion="긴장", intensity=60),
                EmotionPoint(position=0.7, emotion="안도", intensity=70),
                EmotionPoint(position=1.0, emotion="기쁨", intensity=90),
            ],
            total_duration=90,
        )

    def regenerate_phase(self, story: Story, phase_name: str, feedback: str) -> Story:
        """
        Regenerate a specific phase based on feedback.

        Args:
            story: Current story
            phase_name: Phase to regenerate
            feedback: User feedback for improvement

        Returns:
            Updated story
        """
        prompt = f"""Current story:
{story.model_dump_json(indent=2)}

Regenerate the "{phase_name}" phase based on this feedback:
{feedback}

Keep other phases unchanged. Output the complete updated story in YAML format."""

        response = self._call_claude(prompt)
        return self._parse_story_response(response, InputData(
            animal="",
            situation=story.synopsis,
            emotions=[],
        ))
