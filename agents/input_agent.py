"""Input Agent - Parse and structure user input."""

from typing import Any

from core.models import InputData
from .base import BaseAgent


class InputAgent(BaseAgent[InputData]):
    """
    Parses user input and creates structured InputData.

    Handles various input formats:
    - Simple: "골든 리트리버 / 버려짐 / 감동"
    - Detailed: Full description with multiple elements
    """

    def __init__(self):
        super().__init__(
            name="InputAgent",
            system_prompt_path="input_system.md",
        )

    def _get_default_system_prompt(self) -> str:
        return """You are an input parser for an animal story video generator.

Your task is to extract structured information from user input about animal stories.

Extract:
1. animal: The animal type (e.g., "골든 리트리버 강아지", "고양이")
2. situation: The core situation/conflict (e.g., "버려진 후 노인을 만남")
3. emotions: Key emotional tones (list of keywords)
4. ending: The desired ending (if specified)

Output in JSON format:
{
  "animal": "...",
  "situation": "...",
  "emotions": ["...", "..."],
  "ending": "..." or null
}

Be generous in interpretation - if the user provides minimal input, infer reasonable defaults.
Always respond in JSON format only."""

    def process(self, input_data: Any) -> InputData:
        """
        Parse user input into structured InputData.

        Args:
            input_data: Raw user input string

        Returns:
            Structured InputData object
        """
        if isinstance(input_data, InputData):
            return self._normalize(input_data)

        if isinstance(input_data, dict):
            # Normalize string values
            normalized = {}
            for key, value in input_data.items():
                if isinstance(value, str):
                    normalized[key] = value.strip()
                else:
                    normalized[key] = value
            return InputData(**normalized)

        # Parse string input
        raw_input = str(input_data)

        # Check for simple slash-separated format
        if "/" in raw_input:
            return self._parse_simple_format(raw_input)

        # Use Claude to parse complex input
        return self._parse_with_claude(raw_input)

    def _parse_simple_format(self, raw_input: str) -> InputData:
        """Parse simple slash-separated format."""
        parts = [p.strip() for p in raw_input.split("/")]

        animal = parts[0] if len(parts) > 0 else "동물"
        situation = parts[1] if len(parts) > 1 else "감동적인 이야기"
        emotion_str = parts[2] if len(parts) > 2 else "감동"
        ending = parts[3] if len(parts) > 3 else None

        # Parse emotions
        emotions = [e.strip() for e in emotion_str.replace(",", " ").split()]

        return InputData(
            animal=animal,
            situation=situation,
            emotions=emotions,
            ending=ending,
        )

    def _parse_with_claude(self, raw_input: str) -> InputData:
        """Use Claude to parse complex input."""
        response = self._call_claude(
            user_message=f"Parse this input for an animal story video:\n\n{raw_input}"
        )

        try:
            data = self._parse_json_response(response)
            return InputData(
                animal=data.get("animal", "동물"),
                situation=data.get("situation", "이야기"),
                emotions=data.get("emotions", ["감동"]),
                ending=data.get("ending"),
            )
        except Exception as e:
            self.log(f"Parse error: {e}, using defaults")
            return InputData(
                animal=raw_input[:50],
                situation="감동적인 이야기",
                emotions=["감동"],
            )

    def _normalize(self, input_data: InputData) -> InputData:
        """Normalize input data by stripping whitespace."""
        return InputData(
            animal=input_data.animal.strip() if input_data.animal else "",
            situation=input_data.situation.strip() if input_data.situation else "",
            emotions=[e.strip() for e in input_data.emotions],
            ending=input_data.ending.strip() if input_data.ending else None,
            template_id=input_data.template_id,
            character_id=input_data.character_id,
        )

    def validate(self, input_data: InputData) -> tuple[bool, list[str]]:
        """
        Validate input data.

        Returns:
            Tuple of (is_valid, list of issues)
        """
        issues = []

        if not input_data.animal:
            issues.append("동물 종류가 필요합니다")

        if not input_data.situation:
            issues.append("상황/줄거리가 필요합니다")

        if len(input_data.emotions) == 0:
            issues.append("감정 키워드가 필요합니다")

        return len(issues) == 0, issues
